# Install python-binance https://python-binance.readthedocs.io/en/latest/overview.html
pip install python-binance==0.7.4

# Replace your Binance API key and secret into the code on lines 6 and 7


# Example output
****************************************
Balance = 0.07970817, Percentage = 100, Precision = 3, Quantity = 0.079
Placing sell order for 0.079 of ETHBTC
{'symbol': 'ETHBTC', 'orderId': 594496891, 'orderListId': -1, 'clientOrderId': 'EsH6AXFY3n52g3VWcoI2l4', 'transactTime': 1580305356102, 'price': '0.00000000', 'origQty': '0.07900000', 'executedQty': '0.07900000', 'cummulativeQuoteQty': '0.00149317', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'SELL', 'fills': [{'price': '0.01890100', 'qty': '0.07900000', 'commission': '0.00000149', 'commissionAsset': 'BTC', 'tradeId': 159481178}]}
Order Filled? True
****************************************
****************************************
last price 0.018901
Balance = 0.00149274, Percentage = 100, Precision = 3, Quantity = 0.078
Placing buy order for 0.078 of ETHBTC
{'symbol': 'ETHBTC', 'orderId': 594496896, 'orderListId': -1, 'clientOrderId': 'BiuXw30vsnJXLNYqVv3OiA', 'transactTime': 1580305357180, 'price': '0.00000000', 'origQty': '0.07800000', 'executedQty': '0.07800000', 'cummulativeQuoteQty': '0.00147470', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'fills': [{'price': '0.01890300', 'qty': '0.01000000', 'commission': '0.00001000', 'commissionAsset': 'ETH', 'tradeId': 159481180}, {'price': '0.01890700', 'qty': '0.06800000', 'commission': '0.00006800', 'commissionAsset': 'ETH', 'tradeId': 159481181}]}
Order Filled? True
****************************************








