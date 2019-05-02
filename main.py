import urllib
import json
api_base='https://free.currconv.com'
currency_list='/api/v7/currencies?apiKey='
api_key='13e965300e13c50227b9'
url_currency_supported=api_base+currency_list+api_key
print('hitting',url_currency_supported)
response=urllib.request.urlopen(url_currency_supported)
data=json.load(response)
country_map=data['results']
supported_country=list(country_map.keys())
source_country=input('Enter the Source Currency Code: ')
destination_country=input('Enter the Destination Country Code: ')
proceedFlag=False
if((source_country in supported_country) and (destination_country in supported_country)):
  proceedFlag=True
if(proceedFlag):
  #Call the API again with the values
  convert_link='/api/v7/convert?q={0}&compact=ultra&apiKey={1}'
  format_country=source_country+'_'+destination_country
  convert_link=convert_link.format(format_country,api_key)
  response=urllib.request.urlopen(api_base+convert_link)
  data=json.load(response)
#   print(data)
  exchange_rate=float(data[format_country])
  quantity=float(input('How much to convert? '))
  print(exchange_rate*quantity,' At exchange rate of: ',exchange_rate)
else:
  print('Country not supported')