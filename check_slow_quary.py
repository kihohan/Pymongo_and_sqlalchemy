import pandas as pd
from bson.codec_options import TypeCodec
import pymongo

client = pymongo.MongoClient(f'mongodb://111.111.111.1:10000/?authSource=admin&readPreference=secondaryPreferred')
mongodb = client['DB_NAME']

curren_op = mongodb.current_op()
inprog = pd.DataFrame(curren_op['inprog'])

inprog.loc[(inprog['active'] == True) & (inprog['secs_running'] > 0) & (inprog['op'] == 'query')]['opid']
