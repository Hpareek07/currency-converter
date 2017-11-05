import json
from urllib.request import urlopen
import  codecs
url = "https://free.currencyconverterapi.com/api/v4/convert?q="
reader = codecs.getreader('utf-8')

def changecurrency(fromcurrency,tocurrency,amount):
    curr = fromcurrency+"_"+tocurrency
    urlnew = url + curr
    data_obj = urlopen(urlnew)
    data = json.load(reader(data_obj))
    results = data['results']
    list = results[curr]
    print(list['val']*amount)

amount = int(input("Enter the amount of Currency: "))
fromcurrency = input("Enter the currency you want to convert: ")
tocurrency = input("Enter the currency you want to convert in: ")
changecurrency(fromcurrency,tocurrency,amount)