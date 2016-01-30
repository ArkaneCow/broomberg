cum_pricevolume = 0.0
cum_volume = 0.0

def meanreversion(aDict):
    if curr_price < vwap(aDict):
        return "BID"
    elif curr_price > vwap(aDict):
        return "ASK"

def vwap(aDict):
    sum_pricequantity += (aDict["price"]*aDict["shares"])
    sum_quantity += aDict["shares"]
    return sum_pricequantity/sum_quantity
