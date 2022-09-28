from load_demo_data import data

# a single document, unparsed!

# remember this shit is long!

from whoosh.fields import Schema, TEXT, ID
from whoosh import index
import os, os.path
from whoosh import index
from whoosh import qparser
from whoosh.qparser import QueryParser

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored = True))

# create empty index directory

if not os.path.exists("index_dir"):
    os.mkdir("index_dir")

ix = index.create_in("index_dir", schema)
writer = ix.writer()

# for i in range(df):
writer.add_document(title=str(df.title.iloc[i]), content=str(df2.content.iloc[i]),path=str(i))
writer.commit()