# import required packages
from elasticsearch import Elasticsearch

# create Elasticsearch client
es = Elasticsearch()

# search elasticsearch using cmd
count = es.count(index="my-tweets", doc_type='tweet', body={ "query": {"match_all" : { }}})
print("Ok. I've got an index of {0} documents. Let's do some searches...".format(count['count']))
while True:
        try:
            query = input("Enter a search: ")
            result = es.search(index="my-tweets", doc_type='tweet', body={"size": "100", "query": {
    "bool": {
        "must":     { "match": { "message":  query.strip() }},
        "filter": {
          "range": { "date": { "gte": "2018-06-01" }} 
        }
    }
}


            	})
            print("Got %d Hits:" % result['hits']['total'])
            for hit in result['hits']['hits']:
                print("%(date)s %(author)s: %(message)s" % hit["_source"])
        except(KeyboardInterrupt):
            break