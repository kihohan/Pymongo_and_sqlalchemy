import pymongo
import pandas as pd
from multiprocessing import Pool, Process

# normal
client = pymongo.MongoClient("IP")
db = client.table_name.collection_name
qurey = {}
cursor = db.find(query)
item = pd.DataFrame(list(cursor))

# multiprocessing
def get_item(domain):
    client = pymongo.MongoClient("")
    db = client.table_name.collection_name
    qurey = {'master_cate.depth': domain}
    cursor = db.find(query)
    item = pd.DataFrame(list(cursor))
    return item
with Pool (40) as pool:
    domains = ['beauty','fashion']
    df = pd.concat(pool.map(get_item, domains))

