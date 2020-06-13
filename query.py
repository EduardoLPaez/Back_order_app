import pandas as pd
import numpy as np
from secrets import Dev_name, Dev_secret, test_id
import requests
#import kivy
# square api
# json seems to be the above return


def pull_invoice(id_ = test_id):

    payment_id = id_ # will be testing with live after sandbox
        #(got personal issuses with the amount of human err it introduces.)
    # bellow generates the required for responce(halley dam lulla).
    header = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(Dev_secret)}
    # get request ussing the above credentials with (currently) test target id_.
    result = requests.get('https://connect.squareupsandbox.com/v2/payments/{payment_id}', 
    headers=header
    )
    # gotta love pandas.
    df = pd.DataFrame(result.json())
    return df
    
    
print(pull_invoice())