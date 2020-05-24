# Stock_Data_Collector
yfinance stream processor artifacts from AWS pipeline

These are the artifacts of an AWS pipeline that syphons stock prices on a 1m basis from the yfinance python library. The data is pulled by Lambda, transformed in Kinesis, and sent to S3 where it is crawled by Glue and queried by Athena. 

![Image of Data Collector Config](https://github.com/SimulacraAtTanagra/Stock_Data_Collector/blob/master/collector.png?raw=true)
![Image of Kineses Monitoring](https://github.com/SimulacraAtTanagra/Stock_Data_Collector/blob/master/kinesismonitoring.png?raw=true)

Url to Lambda page is: https://oljmt83wqi.execute-api.us-east-2.amazonaws.com/default/stock_collector

