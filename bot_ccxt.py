import ccxt
print(ccxt.exchanges) # print a list of all available exchange classes

# from variable id
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'sdgdfbfdb',
    'secret': 'nnfg43tefbc',
    'timeout': 30000,
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'
timeframe = '1h'
print(exchange.request('api', 'exchangeInfo')
