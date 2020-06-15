import pandas as pd
import numpy as np
from secrets import test_id, dev_name, dev_secret
from secrets import dev_pr_secret, iq_permission
from square.client import Client
import datetime as dt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
#import kivy
# this is screwed, square api only permits spesific search for payment id and only that.
# 
def pull_invoice():#reset it to the last 5 sales
    client = Client(
        access_token = dev_pr_secret,
    )
    result = client.orders.batch_retrieve_orders(
    location_id = test_id, 
    body = {
        client.orders.search_orders(
            body = {
                'location_ids' : test_id,
                "query": {
                    "filter": {
                        "date_time_filter": {
                            "created_at": {
                                "start_at": [ (dt.datetime.today() - dt.timedelta(days=1)), dt.datetime.today()],
                                # "end_at": dt.datetime.today()
        }}}}})})
    df = pd.DataFrame(result.body)
    return df.head(5)


def sandbox_pull_invoice(id_ = test_id):
    client = Client(
        access_token = dev_secret,
        environment = 'sandbox'
    )
    result = client.payments.get_payment( payment_id = id_ )
    # gotta love pandas.
    df = pd.DataFrame(result.body)
    return df
    
    
print(pull_invoice().columns)