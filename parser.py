def parse_my_cash(output):
    price = output.split(' ')[1]
    return float(price)

def parse_my_securities(output):
    list = output.split(" ")
    list.pop(0)
    my_securities = {}

    for i in range(0, len(list) / 3):
        index = i * 3
        ticker = list[index]
        parameters = {}
        parameters["shares"] = list[index + 1]
        parameters["dividend"] = list[index + 2] 
        my_securities[ticker] = parameters
        
    return my_securities

def parse_my_orders(output):
    return 0

def parse_securities(output):
    list = output.split(" ")
    list.pop(0)
    securities = {}

    for i in range(0, len(list) / 4):
        index = i * 4
        ticker = list[index]
        parameters = {}
        parameters["net_worth"] = list[index + 1]
        parameters["dividend_ratio"] = list[index + 2] 
        parameters["volatility"] = list[index + 3]
        securities[ticker] = parameters

    return securities

def parse_orders(output):
    begin = output.find("[") + 1
    end = output.find("]")
    output = output.substring[begin:end]
    list = output.split(" ")
    orders = {}

    for i in range(0, len(list) / 3):
        index = i * 3
        ticker = list[index]
        parameters = {}
        parameters["shares"] = list[index + 1]
        parameters["dividend"] = list[index + 2] 
        my_securities[ticker] = parameters
        
    return orders

def ask_successful(output):
    return output == "ASK_OUT DONE"

def bid_successful(output):
    return output == "BID_OUT DONE"

def clear_bid_successful(output):
    return output == "CLEAR_BID_OUT DONE"

def clear_ask_successful(output):
    return output == "CLEAR_ASK_OUT DONE"