import pandas as pd
import json

from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from bid import Bid


def read_data():
    return pd.read_csv('hb_bid_data.tsv', sep='\t').to_dict(orient='records')

if __name__ == "__main__":
    Bid.init()
    
    dataset = read_data()
    
    bulk_data = (Bid(**row).to_dict(True) for row in json_dataset)

    response = bulk(
        connections.get_connection(),
        bulk_data
    )

    print(response)
    

