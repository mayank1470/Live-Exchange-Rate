# ExchangRate
This script access the Exchange Rate API to convert currency.
To set this script up start you need to sign up on https://www.currencyconverterapi.com/ (use free one and a disposable mail). The API key will be sent to the mail id
make a note of the api key and run the script
The script will askif you have api key in database or no. Answer with N
Then it will ask for the API key, then for the path to save API key
The key will be saved in db(Currently supports only one API key)
Next time you run the application the system will fetch the country list and then ask for source country code. Then it will ask for destination country code. If they are supported it will proceed and ask for quantity to convert
The system will convert the amount with exhnge rate displayed.
There are some shortcomings of the free API which are listed on the signup page
