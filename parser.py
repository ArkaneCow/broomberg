def parse_my_cash(output):
    price = output.split(' ')[1]
    return float(price)

def parse_my_securities(output):
    list = output.split(" ")
    list.pop(0)
    my_securities = {}

    for i in range(0, len(list) // 3):
        index = i * 3
        ticker = list[index]
        parameters = {}
        parameters["shares"] = int(list[index + 1])
        parameters["dividend"] = float(list[index + 2]) 
        my_securities[ticker] = parameters
        
    return my_securities

def parse_my_orders(output):
    begin = output.find("[") + 1
    end = output.find("]")
    output = output[begin:end]
    list = output.split(" ")
    my_orders = {}

    for i in range(0, len(list) // 4):
        index = i * 4
        ticker = list[index + 1]
        parameters = {}
        parameters["price"] = float(list[index + 2])
        parameters["type"] = list[index]
        parameters["shares"] = int(list[index + 3])
        my_orders[ticker] = parameters
        
    return orders

def parse_securities(output):
    list = output.split(" ")
    list.pop(0)
    securities = {}

    for i in range(0, len(list) // 4):
        index = i * 4
        ticker = list[index]
        parameters = {}
        parameters["net_worth"] = float(list[index + 1])
        parameters["dividend_ratio"] = float(list[index + 2]) 
        parameters["volatility"] = float(list[index + 3])
        securities[ticker] = parameters

    return securities

def parse_orders(output):
    list = output.split(" ")
    list.pop(0)
    orders = {}

    for i in range(0, len(list) // 4):
        index = i * 4
        type = list[index]
        parameters = {}
        parameters["ticker"] = list[index + 1]
        parameters["price"] = float(list[index + 2])
        parameters["shares"] = int(list[index + 3])
        orders[type] = parameters
        
    return orders

def ask_successful(output):
    return output == "ASK_OUT DONE"

def bid_successful(output):
    return output == "BID_OUT DONE"

def clear_bid_successful(output):
    return output == "CLEAR_BID_OUT DONE"

def clear_ask_successful(output):
    return output == "CLEAR_ASK_OUT DONE"

