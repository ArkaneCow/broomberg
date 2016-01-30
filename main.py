import network as net
import parser as parse

bc = net.BClient.bclient_default()
companies = None
def init_tickers():
    return parse.parse_securities(bc.cmd("SECURITIES")[0])

companies = init_tickers()
