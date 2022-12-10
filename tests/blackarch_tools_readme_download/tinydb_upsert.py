from tinydb import TinyDB, Query

dbpath = "my_database.json"
# Open a TinyDB database
db = TinyDB(dbpath)

# Create a query to find the record with the key "foo"
query = Query()
query = query.key == "foo"

# Update the value of the key "foo", creating a new record if it does not exist
db.upsert({"key": "foo", "value": "new_value"}, query)

if __name__ == "__main__":