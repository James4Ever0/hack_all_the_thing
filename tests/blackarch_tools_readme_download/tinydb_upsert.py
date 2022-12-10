from tinydb import TinyDB, Query

dbpath = "my_database.json"
# Open a TinyDB database
db = TinyDB(dbpath)

def upsert_data(key,value):
    # Create a query to find the record with the key "foo"
    query = Query()
    query = query.key == "foo"

    # Update the value of the key "foo", creating a new record if it does not exist
    db.upsert({"key": key, "value": value}, query)
    # fucking working?

if __name__ == "__main__":