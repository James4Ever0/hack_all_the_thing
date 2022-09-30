
from whoosh.index import create_in
from whoosh.fields import *
​
from whoosh.qparser import QueryParser

from whoosh.fields import TEXT, SchemaClass
from jieba.analyse import ChineseAnalyzer
​
analyzer = ChineseAnalyzer()
class ArticleSchema(SchemaClass):
    title = TEXT(stored=True, analyzer=analyzer)
    content = TEXT(stored=True, analyzer=analyzer)
    author = TEXT(stored=True, analyzer=analyzer)

schema = ArticleSchema()
ix = create_in("indexdir3", schema, indexname='article_index')
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
