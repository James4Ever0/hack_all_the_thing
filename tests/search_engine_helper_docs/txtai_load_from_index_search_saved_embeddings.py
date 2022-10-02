import numpy as np
# from txtai.embeddings import Embeddings

# embeddings = Embeddings()
data = np.fromfile('ids.txt', dtype=np.float32).reshape(-1,768)
# embeddings.load("./multilingual_index_demo") # no model out there! fuck.
print("LOAD COMPLETE")
queries = np.fromfile("ann_query_embedding.txt",dtype=np.float32).reshape(1,-1)
# SHAPE: (1, 768) DTYPE: float32

# it still needs gpu.
# reshape this thing.

limit = 5


scores = np.dot(queries, data.T).tolist()  # the damn dot product!
        # uid = embeddings.similarity(query, data)[0][0]
        # this is actually the same. just a miniatured 'indexed' thing.
        uids = [
            sorted(enumerate(score), key=lambda x: x[1], reverse=True)
            for score in scores
        ]
        # #b: index of the query, produced result
        # #doc: index of the document of the produced data
        # #data: different position inside the data, representing different values: (index, score)
        #          #b #doc #data
        # uid= uids[0][0][0]
        uid_list_top5 = np.array(uids)[0, :limit, :]  # allow omitted index???
        # the thing is integer based. so the score is always zero.
        # uid_list_top5 = np.array(uids,dtype=int)[0,:5,0]
        # this is a list, not a numpy array!
        # what is this shit anyway?
        # print(uid_list_top5) # we need different results.
        # breakpoint()
        # you may want set some score filters.
        for uid, score in uid_list_top5:
            uid = int(uid)
            # where is the damn score? wtf?
            answer = data_source[uid]
            print("{}:".format(uid), answer)
            print("score:", score)
        storage_file_name = "demo_txtai_search_results.json"
        data_example_json = {"query": query}
        with open(storage_file_name, "w+") as f:
            answers = []
            for uid, score in uid_list_top5:
                uid = int(uid)
                answer = data_source[uid]
                answers.append(answer)
            data_example_json.update({"answers": answers})
            f.write(json.dumps(data_example_json, ensure_ascii=False, indent=4))
            print("write to %s" % storage_file_name)
