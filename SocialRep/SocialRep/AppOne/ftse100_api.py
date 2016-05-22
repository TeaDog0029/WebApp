import matplotlib.pyplot as plt
import datetime
import urllib
import numpy as np


# consumer_key = "dj0yJmk9bEQwNmhTUkphbDFnJmQ9WVdrOU1IZEZRM0psTXpJbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mZQ--"
# consumer_secret = "e562b8fb1c231bf89d70b562c86729889a627eb0"

#stock = "VOD"
#duration = "1d"


# For durations shorter than 10days, the API uses the UNIX time, which we need to transcode
def convert_timestamp(Utimestamp):
    timestamp = datetime.datetime.fromtimestamp(int(Utimestamp)).strftime('%Y-%M-%d %H:%M:%S')
    return timestamp

def graph(stock, duration):
    yahoo_url = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stock + "/chartdata;type=quote;range=" + duration + "/csv"
    raw_data = urllib.request.urlopen(yahoo_url).read().decode()
    stock_data =[]
    split_data = raw_data.split('\n')
    for line in split_data:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'value' not in line and 'volume' not in line:
                stock_data.append(split_line)
    # For the x-axis, we separately build the list:
    timestamp = []
    for line in stock_data:
        aux = convert_timestamp(line[0])
        timestamp.append(aux)
    # "loadtxt" will build us 5 arrays
    closeP, highP, lowP, openP, volume = np.loadtxt(stock_data, delimiter = ',', unpack = True, usecols = (1,2,3,4,5))
    print("%s" % lowP)
    return stock_data
    # Plotting parameters
    #plt.plot(timestamp, volume, label = 'VOD volumes')
    #plt.plot([1,2],[1,4])
    #matplotlib.pyplot.plot([1,2],[1,4])
    #plt.xlabel('Time')
    #plt.ylabel('Volume')
    #plt.title("Vodafone Group Limited - price at the closure")
    #plt.legend()
    # Ultimately not needed
    #plt.show()
    #return raw_data

graph("VOD", "1d")




