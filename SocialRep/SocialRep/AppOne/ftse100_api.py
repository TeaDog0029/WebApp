import matplotlib.pyplot as plt
import pylab
import datetime as dt
import urllib
import numpy as np
import matplotlib.dates as mdates
import os


# consumer_key = "dj0yJmk9bEQwNmhTUkphbDFnJmQ9WVdrOU1IZEZRM0psTXpJbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mZQ--"
# consumer_secret = "e562b8fb1c231bf89d70b562c86729889a627eb0"

#stock = "VOD"
#duration = "1d"

def img_folder():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static/AppOne')
    return path

# For durations shorter than 10days, the API uses the UNIX time, which we need to transcode
def convert_timestamp(Utimestamp):
    timestamp = datetime.datetime.fromtimestamp(int(Utimestamp)).strftime('%Y-%M-%d %H:%M:%S')
    return timestamp

def build_dataset(dst_name, src_name, index, UTime):
    for i in src_name:
        aux = float(i[index])
        dst_name.append(aux)

def graph(stock, duration):
    yahoo_url = "http://chartapi.finance.yahoo.com/instrument/1.0/" + stock + "/chartdata;type=quote;range=" + duration + "/csv"
    raw_data = urllib.request.urlopen(yahoo_url).read().decode()
    stock_data =[]
    split_data = raw_data.split('\n')
    # First, we get rud of the header of the document
    for line in split_data:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'value' not in line and 'volume' not in line:
                stock_data.append(split_line)
    # Declaration of our categories
    timestamp = []
    build_dataset(timestamp,stock_data,0,False)
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    timestamp = dateconv(timestamp)
    closeP = []
    build_dataset(closeP,stock_data,1,False)
    highP = []
    build_dataset(highP,stock_data,2,False)
    lowP = []
    build_dataset(lowP,stock_data,3,False)
    openP = []
    build_dataset(openP,stock_data,4,False)
    volume = []
    build_dataset(volume,stock_data,5,False)
    # Plotting parameters
    plt.plot(timestamp, highP, label = 'VOD high prices')
    #pylab.savefig('/Users/thomascriton/Documents/WebApp/SocialRep/SocialRep/AppOne/static/AppOne/highP', bbox_inches = 'tight')
    pylab.savefig(img_folder()+'/highP.png', bbox_inches = 'tight')
    return True




