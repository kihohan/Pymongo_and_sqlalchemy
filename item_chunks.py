from multiprocessing import Pool, Process

item_list = list (df['item_doc_id'].unique())
n = int (len (item_list) / 31)
list_split = [item_list[i * n:(i + 1) * n] for i in range((len(item_list) + n - 1) // n )] 

chunk_cnt = [x for x in range(32)]

def get_colt_item(chunk_cnt):    
    client = pymongo.MongoClient(" . ")
    db = client['  ']
    collection = '  '
    cursor = db[collection].find({'_id': {'$in':list_split[chunk_cnt]}})
    item_d = pd.DataFrame(list(cursor))
    return item_d
with Pool(32) as pool:
    colt_item = pd.concat(pool.map(get_colt_item,chunk_cnt))
