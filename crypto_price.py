import json
import time
# from urllib import request
import requests
from requests import Session

from dotenv import dotenv_values
config = dotenv_values(".env")

# For documentation refer:https://coinmarketcap.com/api/documentation/v1/
URL = 'https://pro-api.coinmarketcap.com'

IFTTT = 'https://maker.ifttt.com/trigger/bitcoin_price_emergency/with/key/' + config['IFTTT_KEY']
def fetch_id_map(session,url='/v1/cryptocurrency/'):
  parameters = {
    'start': 1,
    'limit':1500
  }
  try:
    response = session.get(URL+url,params=parameters)
    data = json.loads(response.text)
    with open('map.json','w') as file:
      json.dump(data,file)
    print('Done')
  except :
    print('failed... try again')


def fetch_data(session,url ='/v1/cryptocurrency/listings/latest'):
  parameters = {
    'limit': 2,
  }
  try:
    print('Getting price...')
    response = session.get(URL+url,params=parameters)
    print('Data recieved.')
    price_data = json.loads(response.text)
    return price_data
  except :
    print('failed... try again')


def get_bitcoin_price(obj):
  data = obj['data'][0]['quote']['USD']
  keys = ['price', 'last_updated']
  ret = {k:data[k] for k in keys}
  return ret

def get_etherium_price(obj):
  data = obj['data'][1]['quote']['USD']
  keys = ['price', 'last_updated']
  ret = {k:data[k] for k in keys}
  return ret


def send_notification(price,url=IFTTT):
  print('Sending notification...')
  parameter = {'value1': price}
  requests.post(url,json=parameter)
  print('Notification Sent.')


def main(price):
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config['API_KEY']
  }
  session = Session()
  session.headers.update(headers)
  bitcoin_history = []
  # fetch_id(session)
  while True:
    data_obj = fetch_data(session)
    bitcoin_history.append(get_bitcoin_price(data_obj))
    if bitcoin_history[-1]['price']>=price:
      print(bitcoin_history[-1]['price'], price)
      send_notification(bitcoin_history[-1]['price'])
    print("Will check again in 5 minutes...")
    time.sleep(300) # 5 mins
    


if __name__=='__main__':
  BITCOIN_PRICE_THRESHOLD = 10000  # Set this to whatever you like
  main(BITCOIN_PRICE_THRESHOLD)
