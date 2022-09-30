from whoosh.index import create_in

from whoosh.fields import TEXT, SchemaClass
from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()

indexDirectory = "indexdir3"

import os
if not os.path.exists(indexDirectory):
    os.mkdir(indexDirectory)
    
class ArticleSchema(SchemaClass):
    title = TEXT(stored=True, analyzer=analyzer)
    content = TEXT(stored=True, analyzer=analyzer)
    author = TEXT(stored=True, analyzer=analyzer)


schema = ArticleSchema()
ix = create_in(indexDirectory, schema, indexname="article_index")
writer = ix.writer()
writer.add_document(title="登鹳雀楼", author="王之涣", content="白日依山尽，黄河入海流，欲穷千里目，更上一层楼")
writer.add_document(title="登高", author="杜甫", content="风急天高猿啸哀，渚清沙白鸟飞回")
writer.add_document(title="胡乱写的", author="黄河恋", content="展示效果")
writer.commit()
from whoosh.qparser import QueryParser
from whoosh.index import open_dir

ix = open_dir(indexDirectory, indexname="article_index")
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("黄河")
    results = searcher.search(query)
    print(results[0])


with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("黄河")
    results = searcher.search(query)
    data = results[0]
    text = data.highlights("content")
    print(text)

from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.index import open_dir

ix = open_dir(indexDirectory, indexname="article_index")
with ix.searcher() as searcher:
    query = MultifieldParser(["content", "author"], ix.schema).parse("黄河")
    results = searcher.search(query)
    for data in results:
        print(data)

query = MultifieldParser(["content", "author"], ix.schema).parse("黄河 杜甫")

from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.index import open_dir
from whoosh.query import compound, Term

ix = open_dir(indexDirectory, indexname="article_index")
with ix.searcher() as searcher:
    author_query = [Term("author", "黄河"), Term("author", "杜甫")]
    content_query = [Term("content", "黄河"), Term("content", "杜甫")]
    query = compound.Or([compound.Or(author_query), compound.Or(content_query)])
    print(query)
    results = searcher.search(query)
    for data in results:
        print(data)

results = searcher.search_page(query, 1)  # 搜索第1页，默认每页10个结果
print(results.total)  # 搜索到的文档总量，帮助你进行分页
