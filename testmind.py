SAMPLE_LENGTH = 3
BID_THRESH = 0

histories = {}

def update_histories(companies):
    for k in companies:
        if k not in histories:
            histories[k] = [companies[k]["price"]] * SAMPLE_LENGTH
        else:
            for i in range(0, SAMPLE_LENGTH - 1):
                histories[k][SAMPLE_LENGTH - 1 - i] = histories[k][SAMPLE_LENGTH -2 - i]
                histories[k][0] = companies[k]["price"]

def decide():
    avgs = [sum(histories[l]) / len(histories[l]) for l in histories]
    olds = [histories[o][-1] for o in histories]
    ticks = [t for t in histories]
    decides = {}
    for t in range(len(ticks)):
        decides[ticks[t]] = (avgs[t] - olds[t])/histories[ticks[t]][0]
    return decides
