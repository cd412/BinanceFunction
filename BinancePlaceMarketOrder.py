import time
import math
from binance.client import Client

############# CONFIG #######
API_KEY = "xxx"
API_SECRET = "xxx"

############################

class Trader(Client):
    def __init__(self, api_key, api_secret):
        super(Trader, self).__init__(api_key, api_secret)
        self.time_offset = self.get_time_offset()
        self.exchange_info = self.get_exchange_info()

    def _request(self, method, uri, signed, force_params=False, **kwargs):
        ### **Developer's note** This function has to be overwritten because it is causing errors when there is a time delay between 
        # the binance server and the local server

        # set default requests timeout
        kwargs['timeout'] = 10

        # add our global requests params
        if self._requests_params:
            kwargs.update(self._requests_params)

        data = kwargs.get('data', None)
        if data and isinstance(data, dict):
            kwargs['data'] = data

            # find any requests params passed and apply them
            if 'requests_params' in kwargs['data']:
                # merge requests params into kwargs
                kwargs.update(kwargs['data']['requests_params'])
                del(kwargs['data']['requests_params'])

        if signed:
            # generate signature
            kwargs['data']['timestamp'] = int(time.time() * 1000 + self.time_offset)
            kwargs['data']['signature'] = self._generate_signature(kwargs['data'])

        # sort get and post params to match signature order
        if data:
            # sort post params
            kwargs['data'] = self._order_params(kwargs['data'])
            # Remove any arguments with values of None.
            null_args = [i for i, (key, value) in enumerate(kwargs['data']) if value is None]
            for i in reversed(null_args):
                del kwargs['data'][i]

        # if get request assign data array to params value for requests lib
        if data and (method == 'get' or force_params):
            kwargs['params'] = '&'.join('%s=%s' % (data[0], data[1]) for data in kwargs['data'])
            del(kwargs['data'])

        self.response = getattr(self.session, method)(uri, **kwargs)
        return self._handle_response()

    def get_time_offset(self):
        # Getting the time difference between the binance server time and the local server
        st = int(self.get_server_time()["serverTime"])
        mt = int(time.time()*1000)
        return st - mt

    def get_precision(self, symbol, type='stepSize'):
        infos = self.exchange_info["symbols"]
        for info in infos:
            if info["baseAsset"] == symbol[:len(info["baseAsset"])]:
                data = info
                break
        if type == "stepSize":
            tick = data["filters"][2]["stepSize"]
            precision = math.floor(-math.log10(float(tick)))
            return precision
        if type == "tickSize":
            tick = data["filters"][0]["tickSize"]
            precision = math.floor(-math.log10(float(tick)))
            return precision
        elif type == "base":
            return data["baseAssetPrecision"]
        elif type == "quote":
            return data["quotePrecision"]

    def place_market_buy(self, symbol, quantity):
        data = self.order_market_buy(symbol=symbol, quantity=quantity)
        return data

    def place_market_sell(self, symbol, quantity):
        data = self.order_market_sell(symbol=symbol, quantity=quantity)
        return data

    def get_balance(self, asset):
        balance = float(self.get_asset_balance(asset)['free'])
        return balance

    def place_market_order(self, base_asset="BTC", quote_asset="USDT", action="sell", percentage=100):
        # Get base asset and quote asset
        symbol = base_asset + quote_asset

        # Determine transaction quantity
        precision = self.get_precision(symbol, "stepSize")
        
        if action == 'sell':
            asset = base_asset
        elif action == 'buy':
            asset = quote_asset
        balance = self.get_balance(asset)

        quantity = round(math.floor(balance * percentage / 100 * (10**precision)) * 10**-precision, precision)
        print("Balance = {}, Percentage = {}, Precision = {}, Quantity = {}".format(balance, percentage, precision, quantity))
        assert quantity > 0.0, "Balance of {} {} is too low to execute trade.".format(balance, asset)

        # Execute trade
        if LIVE_TRADING == True:
            if action == 'sell':
                response = self.place_market_sell(symbol, quantity)
            elif action == 'buy':
                response = self.place_market_buy(symbol, quantity)
            else:
                raise NotImplementedError('Action {} is not implemented.'.format(action))
        else:
            response = {'status': 'Live trading is off'}
        
        # Log
        msg = "Placing {} order for {} of {}".format(action, quantity, symbol)
        print(msg)
        print(response)
        return response['status'] == 'FILLED'


if __name__ == '__main__':
    t = Trader(API_KEY, API_SECRET)
    LIVE_TRADING = True

    # Examples
    print('*'*40)
    resp1 = t.place_market_order(base_asset='LTC', quote_asset='ETH', percentage=100, action='buy')
    print("Order Filled?", resp1)
    print('*'*40)

    print('*'*40)
    resp2 = t.place_market_order(base_asset='LTC', quote_asset='ETH', percentage=100, action='sell')
    print("Order Filled?", resp2)
    print('*'*40)

