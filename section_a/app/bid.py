import os
from elasticsearch_dsl import connections, Document, Integer, Date, Keyword, Text
from elasticsearch.helpers import bulk

es_host = os.environ.get('ES_HOST', 'localhost:9200')
connections.create_connection(hosts=[es_host], timeout=20)

class Bid(Document):
    id = Keyword()
    auctionId = Keyword()
    pageviewId = Keyword()
    sessionId = Keyword()
    userId = Keyword()
    country = Keyword()
    device = Keyword()
    bid = Integer()
    bidder = Keyword()
    bidLatency = Integer()
    status = Keyword()
    timestamp = Date()

    class Index:
        name = 'bid'