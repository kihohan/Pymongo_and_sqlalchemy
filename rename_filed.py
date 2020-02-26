# rename_field_name
import pymongo
client = pymongo.MongoClient("server")
db = client.collection_name
db.field_name.update({}, {'$rename':{'original_name':'new_name'}}, False, True)
