import pymongo
from pymongo import MongoClient
from collections import Counter

# ---------- Fixed Params ------------
mongo.connect('mongodb://act4dgem.cse.iitd.ac.in:27017')
art_client = MongoClient('mongodb://act4dgem.cse.iitd.ac.in:27017')
client = MongoClient('mongodb://10.237.26.159:27017/')
art_db = art_client['media-db']
my_db = client['media-db']
#print(art_db)
#print(my_db)
# -----------------------------------

print("Finding articles...")

x = art_db.articles.find({'$and':[{'text': {'$regex': 'onion | potato', '$options': 'i'}},{'categories':{'$exists':True}}]},
                     no_cursor_timeout=True) 
 

#print ('x is', x,'\n' )
articles = input('Enter name of collection to store resultant articles for development: ')
#print(x.count())
print("Storing articles now...")

coll = my_db[articles]
#print("coll \n",coll) 
art_map = {}
cnt =0
#print ('here \n')
i = 0
for art in x:
    cnt+=1
    i+=1
    if(i>2):
        break
    print('Done for '+str(cnt)+' article')
    url = art['articleUrl']
    #print("art is ",art["_id"])
   
    if url not in art_map:
        art_map[url] = 1
        coll.insert_one(art)

