%%time
def get_item(present_time):
    
    client = pymongo.MongoClient(" .  ")
    db = client['  ']
    collection = '  '
    cursor = db[collection].find({'collect_day': present_time})
    item_d = pd.DataFrame(list(cursor))
    return item_d

def make_parameter(present_date, terms):
    date_chunks = [(datetime.strptime(present_date, '%Y%m%d')  + timedelta(days = i)).strftime('%Y%m%d') for i in range(0,terms)]
    return date_chunks
date_chunks = make_parameter('20191007',terms)

with Pool(terms) as pool:
    df = pd.concat(pool.map(get_item,date_chunks))
