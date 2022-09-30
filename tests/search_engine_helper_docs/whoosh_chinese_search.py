
from whoosh.index import create_in
from whoosh.fields import *
​
# 构建索引
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()
writer.add_document(title=u"First document", path=u"/a",content=u"This is the first document we've added!")
writer.add_document(title=u"Second document", path=u"/b", content=u"The second one is even more interesting!")
writer.commit()
​
# 搜索
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    print(results[0])
程序最终输出结果为

<Hit {'path': '/a', 'title': 'First document'}>
官网上的例子，我没有做任何修改，只是添加了两行注释。整个程序分为两部分，第一部分是构建索引的过程，第二部分是搜索的过程。

2. 构建索引
2.1 倒排索引
搜索引擎的关键技术是建立倒排索引，倒排索引记录了哪些文档中包含了某个单词，比如 “酷python” 这个词出现在了你正在看的这篇文章中，假设这篇文章的编号是111， 那么索引中就会记录一条 酷python：111的记录。当你搜索 酷python 这个词的时候，搜索引擎从倒排索引中找到 酷python所对应的文档，如果有多个，搜索引擎则计算文档与搜索词的相关性，并根据相关性进行排序返回给你结果。

2.2 分词
我们在搜索时，所搜索的关键词可能是一个句子，文档里那么多内容，但索引只记录词与文档编号之间的映射关系，因此，不论是构建索引还是根据关键词进行搜索，都得进行分词。对于英语文档，分词是一件简单的事情，因为英语的句子是由若干个单次组成的。而中文的分词则相对复杂，因为我们的词是由单个汉字组成的，而词与词之间是没有空格这种明显的分界的，具体哪几个汉字组成一个词，要看所处的语境，比如 “ 军任命了一名中将 ”， 这里中将就是一个词，但在句子“ 产量三年中将增长两倍 ”， 中将 就不再是一个词。

但你大可不必担心，因为现在的中文分词技术已经非常成熟了，开源库jieba可以满足你绝大部分需求。

2.3 索引模式
现在要为100篇文章构建索引，一篇文章的信息可能包括 文章标题，内容，作者，在构建索引的时候，你需要定义索引模式，就如同定义一张mysql里的表，你需要指出需要存储哪些字段，以及这些字段的类型

from whoosh.fields import TEXT, SchemaClass
from jieba.analyse import ChineseAnalyzer
​
​
analyzer = ChineseAnalyzer()
class ArticleSchema(SchemaClass):
    title = TEXT(stored=True, analyzer=analyzer)
    content = TEXT(stored=True, analyzer=analyzer)
    author = TEXT(stored=True, analyzer=analyzer)
与官网中的例子不同，我通过继承SchemaClass 来实现一个新的类，以此定义索引模式。而且我设置了analyzer 为ChineseAnalyzer， 这样whoosh就可以支持中文索引了，analyzer会对文档中的中文进行分词。

2.4 添加文档
schema = ArticleSchema()
ix = create_in("indexdir", schema, indexname='article_index')
writer = ix.writer()
writer.add_document(title="登鹳雀楼", author="王之涣",content="白日依山尽，黄河入海流，欲穷千里目，更上一层楼")
writer.add_document(title="登高", author="杜甫", content="风急天高猿啸哀，渚清沙白鸟飞回")
writer.add_document(title="胡乱写的", author="黄河恋", content="展示效果")
writer.commit()
create_in 会创建一个名为indexdir 的文件夹，添加文档时，一定要根据你所定义的索引模式进行添加，这样就创建好了索引，添加文档的过程，就如同向mysql的表里写入数据。

3. 搜索
搜索的过程，需要使用open_dir函数打开索引文件，创建Searcher 对象

from whoosh.qparser import QueryParser
from whoosh.index import open_dir
​
ix = open_dir("indexdir", indexname='article_index')
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("黄河")
    results = searcher.search(query)
    print(results[0])
程序输出结果

<Hit {'author': '王之涣', 'content': '白日依山尽，黄河入海流，欲穷千里目，更上一层楼', 'title': '登鹳雀楼'}>
3.1 高亮显示
我们在百度搜索引擎搜索关键词所得到的结果，那些与关键词匹配的部分会被高亮显示，这样方便用户查看内容，这个功能，whoosh同样支持

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("黄河")
    results = searcher.search(query)
    data = results[0]
    text = data.highlights("content")
    print(text)
程序输出结果为

白日依山尽，<b class="match term0">黄河</b>入海流，欲穷千里目
在html文件中，你可以自己来定义match 和 term0 的样式。



3.2 多个字段同时搜索
对多个字段同时搜索，需要使用MultifieldParser

from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.index import open_dir
​
ix = open_dir("indexdir", indexname='article_index')
with ix.searcher() as searcher:
    query = MultifieldParser(["content", 'author'], ix.schema).parse("黄河")
    results = searcher.search(query)
    for data in results:
        print(data)
content中有黄河，或者author有黄河的文档，都可以被搜索出来，程序输出结果

<Hit {'author': '黄河恋', 'content': '展示效果', 'title': '胡乱写的'}>
<Hit {'author': '王之涣', 'content': '白日依山尽，黄河入海流，欲穷千里目，更上一层楼', 'title': '登鹳雀楼'}>
3.3 多个关键词同时搜索
如果你所搜索的内容并不仅仅是一个关键词，而是多个，或者你搜索的是一个句子，搜索引擎会把你的句子进行分词，得到若干个词，这些词作为条件进行搜索，只有被搜索的字段同时满足这些关键词时，才能得到搜索结果，比如下面的搜索

query = MultifieldParser(["content", 'author'], ix.schema).parse("黄河 杜甫")
这个搜索条件不会得到任何结果，原因在于搜索条件等价于

((content:黄河 OR author:黄河) AND (content:杜甫 OR author:杜甫))
被搜索的字段中，比如同时包含黄河与杜甫。如果你希望这些关键词之间是或的关系，那么需要你自己来构建搜索条件

from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.index import open_dir
from whoosh.query import compound, Term
​
ix = open_dir("indexdir", indexname='article_index')
with ix.searcher() as searcher:
    author_query = [Term('author', '黄河'), Term('author', '杜甫')]
    content_query = [Term('content', '黄河'), Term('content', '杜甫')]
    query = compound.Or([compound.Or(author_query), compound.Or(content_query)])
    print(query)
    results = searcher.search(query)
    for data in results:
        print(data)
三个文档都会被搜索到， 如果你搜索的是一个句子，那么你可以使用analyzer 对整个句子进行分词，然后构造搜索条件，我所说的analyzer就是 analyzer = ChineseAnalyzer() 语句创建的对象。

3.4 分页搜索
如果搜索结果太多，那么你需要分页查询

results = searcher.search_page(query, 1)    # 搜索第1页，默认每页10个结果
    print(results.total)   # 搜索到的文档总量，帮助你进行分页
你获取的是第一页的搜索结果，但results.total 会告诉你搜索结果一共有多少条，这样，你就知道该搜索多少页的数据了。
