from multiprocessing import Process

def multi_insert_data(df, p_cnt = 10):

    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    c = round(len(df) / p_cnt)
    df_chunks = list (chunks(df, c))

    a = df_chunks[0]
    b = df_chunks[1]
    c = df_chunks[2]
    d = df_chunks[3]
    e = df_chunks[4]
    f = df_chunks[5]
    g = df_chunks[6]
    h = df_chunks[7]
    i = df_chunks[8]
    j = df_chunks[9]

    Process(target = insert_data, args=(a,)).start()
    Process(target = insert_data, args=(b,)).start()
    Process(target = insert_data, args=(c,)).start()
    Process(target = insert_data, args=(d,)).start()
    Process(target = insert_data, args=(e,)).start()
    Process(target = insert_data, args=(f,)).start()
    Process(target = insert_data, args=(g,)).start()
    Process(target = insert_data, args=(h,)).start()
    Process(target = insert_data, args=(i,)).start()
    Process(target = insert_data, args=(j,)).start()
