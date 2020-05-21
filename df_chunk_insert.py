from multiprocessing import Process
from pymongo import UpdateOne

opr = data.apply(lambda r : UpdateOne({'_id' : r._id}, {'$set':{ 'master_brand_name' : r.master_brand_name }} ), axis=1).to_list()
opr_lst = [list(x) for x in np.array_split(opr, 6)]

def bulk_insert(opr):
    client = pymongo.MongoClient("")
    collection = client.X
    db = collection.Y
    db.bulk_write(opr)
    
Process(target = bulk_insert, args=(opr_lst[0],)).start()
Process(target = bulk_insert, args=(opr_lst[1],)).start()
Process(target = bulk_insert, args=(opr_lst[2],)).start()
Process(target = bulk_insert, args=(opr_lst[3],)).start()
Process(target = bulk_insert, args=(opr_lst[4],)).start()
Process(target = bulk_insert, args=(opr_lst[5],)).start()
