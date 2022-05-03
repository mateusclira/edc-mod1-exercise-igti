import boto3
import botocore
import pandas as pd

#Criar um cliente para interagir com o AWS S3
s3_client = boto3.resource('s3')

'''s3_client.meta.client.download_file("datalake-mateus-igti-edc",
                                    r"data/vgsales.csv",
                                    r"C:\data\vgsales.csv")

df = pd.read_csv("C:\\data\\vgsales.csv", sep=",")
print(df)'''

s3_client.meta.client.upload_file("C:\\Users\\mateus.c.lira\\Downloads\\Data-analysis-challenge\\daily_revenue.csv","datalake-mateus-igti-edc",r"data/daily_revenue.csv")