import time

import network as net
import parser as parse

TICK_TIME = 0.5

bc = net.BClient.bclient_default()
companies = None
def init_tickers():
    return parse.parse_securities(bc.cmd("SECURITIES")[0])

companies = init_tickers()
orders = {}
print(companies)

st = time.time()

def order_update(data):
    p = parse.parse_orders(data)
    company = p['ASK']['ticker']
    companies[company]['price'] = p['ASK']['price']
    orders[company] = p


def security_update(data):
    p = parse.parse_securities(data)
    for k in p:
        for v in p[k]:
            companies[k][v] = p[k][v]
    print(companies)

def update_all():
    commands = ["SECURITIES"] + ["ORDERS " + t for t in companies]
    responses = bc.cmd(*commands)
    order_responses = [o for o in responses if o.startswith("SECURITY_ORDERS_OUT")]
    security_responses = [o for o in responses if o.startswith("SECURITIES_OUT")]
    for r in security_responses:
        security_update(r)
    for r in order_responses:
        order_update(r)

update_all()
while True:
    if time.time() - st >= TICK_TIME:
        update_all()
        st = time.time()
    else:
        continue
