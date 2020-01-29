# Install python-binance https://python-binance.readthedocs.io/en/latest/overview.html
pip install python-binance==0.7.4

# Replace your Binance API key and secret into the code on lines 6 and 7


# Example output
****************************************
Balance = 0.05293446, Percentage = 100, Precision = 2, Quantity = 0.05
Placing buy order for 0.05 of LTCETH
{'symbol': 'LTCETH', 'orderId': 97527599, 'orderListId': -1, 'clientOrderId': 'FH4iMn8HOPDJhDVIIER5Vk', 'transactTime': 1580246332717, 'price': '0.00000000', 'origQty': '0.05000000', 'executedQty': '0.05000000', 'cummulativeQuoteQty': '0.01716750', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'BUY', 'fills': [{'price': '0.34335000', 'qty': '0.05000000', 'commission': '0.00005000', 'commissionAsset': 'LTC', 'tradeId': 7176456}]}
Order Filled? True
****************************************
****************************************
Balance = 0.05985, Percentage = 100, Precision = 2, Quantity = 0.05
Placing sell order for 0.05 of LTCETH
{'symbol': 'LTCETH', 'orderId': 97527601, 'orderListId': -1, 'clientOrderId': 'Kv2x829CQO2tLzAAKyWuU9', 'transactTime': 1580246333220, 'price': '0.00000000', 'origQty': '0.05000000', 'executedQty': '0.05000000', 'cummulativeQuoteQty': '0.01715600', 'status': 'FILLED', 'timeInForce': 'GTC', 'type': 'MARKET', 'side': 'SELL', 'fills': [{'price': '0.34312000', 'qty': '0.05000000', 'commission': '0.00001716', 'commissionAsset': 'ETH', 'tradeId': 7176457}]}
Order Filled? True
****************************************








