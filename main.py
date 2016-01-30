import time

import network as net
import parser as parse

TICK_TIME = 0.5

bc = net.BClient.bclient_default()
companies = None
def init_tickers():
    return parse.parse_securities(bc.cmd("SECURITIES")[0])

companies = init_tickers()
print(companies)

st = time.time()

while True:
    if time.time() - st >= TICK_TIME:
        st = time.time()
        print("tick")
    else:
        continue
