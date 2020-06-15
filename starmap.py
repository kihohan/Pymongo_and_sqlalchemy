import pymongo
import pandas as pd
from multiprocessing import Pool, Process

def s_amt(collect_site, collect_day):
    client = pymongo.MongoClient("mongodb://############")
    db = client.EPOP_TOP
    collection = db.sell_amt
    cursor = collection.find()
    df = pd.DataFrame(list(cursor))
    return df
  
def make_parameter(present_date, terms):
    date_chunks = [(datetime.strptime(present_date, '%Y%m%d')  + timedelta(days = i)).strftime('%Y%m%d') for i in range(0,terms)]
    return date_chunks
    
dates = make_parameter(date, 7)
site = ['top.11st.co.kr', 'top.coupang.com', 'top.gmarket.co.kr','top.ssg.com']
p = [(s, d) for d in dates for s in site]
with Pool(20) as pool:
    sell_amt = pd.concat(pool.starmap(s_amt,p))
