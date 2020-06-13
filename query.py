import pandas as pd
import numpy as np
from secrets import test_id, dev_pr_secret, iqn, iqs, dev_name, dev_secret
import requests
from square.client import Client

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
#import kivy
# square api
# json seems to be the above return
client = Client(
    access_token = dev_secret,
    environment = 'sandbox'
)

def pull_invoice(id_ = test_id):
    result = client.payments.get_payment( payment_id = id_ )
    # gotta love pandas.
    df = pd.DataFrame(result.body)
    return df
    
    
print(pull_invoice())