import boto3
import os
import subprocess
import sys
import json
import shutil

for root, dirs, files in os.walk('/tmp'):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
        

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance as yf

def lambda_handler(event, context):
    sym_list=["FB","SHOP","BYND","NFLX","PINS","SQ","TTD","OKTA","SNAP","DDOG"]
    counter= 0
    for sym in sym_list:
        tickers = yf.Ticker(sym)
        if counter==0:
            x=tickers.history(start="2020-05-14", end="2020-05-15",interval='1m')
            x['name'] = sym
            x.index=x.index.astype(str)
            x['ts'] = x.index
            x=x.reset_index()
            counter+=1
        else:
            z=tickers.history(start="2020-05-14", end="2020-05-15",interval='1m') 
            z['name'] = sym
            z.index=z.index.astype(str)
            z['ts'] = z.index
            z=z.reset_index()
            x=x.append(z, ignore_index=True)
    x=x[['High','Low','name','ts']]
    x.columns=['high','low','name','ts']
    fh = boto3.client("firehose","us-east-2")
    
    for i in range(x.shape[0]):
        data =x.iloc[i].to_json()
        #as_jsonstr = json.dumps(data)
        fh.put_record(
            DeliveryStreamName="stock_delivery_stream9760",
            Record={"Data":data.encode('utf-8')})
    #convert to json
    #as_jsonstr = json.dumps(data)
    
    #initialize boto3 client
    #fh = boto3.client("firehose","us-east-2")
    
    # encode to bytes
    #fh.put_record(
    #    DeliveryStreamName="stock_delivery_stream9760",
    #    Record={"Data":as_jsonstr.encode('utf-8')})
        
    # return
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded:')
    }