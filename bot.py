from binance_api import Binance
import time

bot = Binance(
    API_KEY='sdfgsdfb24g',
    API_SECRET='sdfag2q3'
)



def current_price():
    # print('ticker/bookTicker')
    x = bot.tickerBookTicker(symbol='ETHBTC')
    return float(x['askPrice'])


def order_price(koef):
    x = round(current_price()*koef, 6)
    print(x, koef)
    return x


def check_bars():
    data = bot.klines(symbol='ETHBTC',
                      interval='1m',
                      limit=1)
    print(data)
    for i in data:
        open_price = float(i[1])
        close_price = float(i[4])
        result = round(open_price*1000000 - close_price*1000000, 7)
        print(open_price, close_price, result)
        # if open_price*1000000 > close_price*1000000:
        #     print('more')
        #     break
        if result <= 0:
            print('false')
            return False

    return True


def create_order(type_order='LIMIT', side_or='SELL', koef=1.00):
    print('createOrder')
    return bot.createOrder(
        symbol='ETHBTC',
        recvWindow=10000,
        side=side_or,
        type=type_order,
        timeInForce='GTC',
        quantity=0.005,
        price=order_price(koef)
    )


def check_status_order():
    print('orderInfo')
    info_order = bot.orderInfo(
        orderId=order_id,
        symbol='ETHBTC',
    )
    return info_order['status']

# current_price()
while True:
    time.sleep(1)
    if check_bars():
        order_data = create_order()
        print(order_data)
        order_id = order_data['orderId']
        break


while True:
    if check_status_order() == 'FILLED':
        create_order('TAKE_PROFIT', side_or='BUY', koef=0.995)
        create_order('STOP_LOSS', side_or='BUY', koef=1.0025)
        break

