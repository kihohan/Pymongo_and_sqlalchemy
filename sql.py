# normal
input_db = create_engine('해당IP', encoding = 'utf8' , 
                         pool_size=20,pool_recycle=3600,connect_args={'connect_timeout':10000} )
query = 'SELCET FORM WHERE;'
MWS_COLT_ITEM = pd.read_sql(query, input_db)
print (MWS_COLT_ITEM.shape)

# chunk 
input_db = create_engine('해당IP', encoding = 'utf8' , 
                         pool_size=20,pool_recycle=3600,connect_args={'connect_timeout':10000} )
query = 'SELCET FORM WHERE;'
chunks = [i for i in pd.read_sql(query, input_db, chunksize = 100000)]
MWS_COLT_ITEM = pd.concat(chunks,sort = False).reset_index().drop('index',1)
