import time

import network as net
import parser as parse
import testmind as mind

TICK_TIME = 0.5
MULTIPLIER = 1000000

bc = net.BClient.bclient_default()
companies = None
def init_tickers():
    return parse.parse_securities(bc.cmd("SECURITIES")[0])

companies = init_tickers()
orders = {}
money = 0
print(companies)

st = time.time()

def order_update(data):
    p = parse.parse_orders(data)
    company = p['ASK']['ticker']
    companies[company]['price'] = p['ASK']['price']
    companies[company]['shares'] = p['ASK']['shares']
    orders[company] = p


def security_update(data):
    p = parse.parse_securities(data)
    for k in p:
        for v in p[k]:
            companies[k][v] = p[k][v]
    #print(companies)

def update_all():
    money = parse.parse_my_cash(bc.cmd("MY_CASH")[0])
    print(str(money))
    commands = ["SECURITIES"] + ["ORDERS " + t for t in companies]
    responses = bc.cmd(*commands)
    order_responses = [o for o in responses if o.startswith("SECURITY_ORDERS_OUT")]
    security_responses = [o for o in responses if o.startswith("SECURITIES_OUT")]
    for r in security_responses:
        security_update(r)
    for r in order_responses:
        order_update(r)
update_all()

mind.update_histories(companies)
while True:
    if time.time() - st >= TICK_TIME:
        st = time.time()
        update_all()
        mind.update_histories(companies)
        for i in list(companies.keys()):
            ratio = mind.decide()[i]
            decision = ratio > 0
            if decision:
                cmd = "BID " + i + " " + str(companies[i]['price']+0.01) + " " + str(int(ratio*1000000))
                print(cmd)
                bc.cmd(cmd)
    else:
        continue
