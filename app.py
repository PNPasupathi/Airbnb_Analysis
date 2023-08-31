import pandas as pd
import numpy as np
import pymongo
# import matplotlib.pyplot as plt
# import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

client=pymongo.MongoClient('mongodb+srv://pnpasupathipn:3915@airbnbproj.hngpd1o.mongodb.net/?retryWrites=true&w=majority')
check=client.test

db=client.get_database('sample_analytics')
acc=db['customers']
for i in acc.find({},{'_id':0}):
    print(i)
    print('')

db=db['transactions']
transaction_count=[]
for i in db.find():
    print(i['transactions'])
    print('')
    transaction_count.append(i['transaction_count'])

transaction_amount=[]
transaction_amt=[]
for i in db.find():
    for j in (i['transactions']):
        transaction_amt.append(j['amount'])
    transaction_amount.append(transaction_amt)
    transaction_amt=[]
transaction_price=[]
transaction_pri=[]
for i in db.find():
    for j in (i['transactions']):
        transaction_pri.append(j['price'])
    transaction_price.append(transaction_pri)
    transaction_pri=[]
transaction_total=[]
transaction_tot=[]
for i in db.find():
    for j in (i['transactions']):
        transaction_tot.append(j['total'])
    transaction_total.append(transaction_tot)
    transaction_tot=[]