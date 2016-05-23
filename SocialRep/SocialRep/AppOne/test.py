import matplotlib.pyplot as plt

string = "test_string "

def fonc(var):
    return var



yahoo_url = "http://chartapi.finance.yahoo.com/instrument/1.0/" + "VOD" + "/chartdata;type=quote;range=" + "1d" + "/csv"
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
    timestamp.append(convert_timestamp(line[0])



test_list = [['1463751055', '33.6800', '33.6854', '33.6800', '33.6854', '128900'], ['1463751119', '33.7000', '33.7000', '33.6700', '33.6700', '22200'], ['1463751234', '33.7200', '33.7200', '33.7150', '33.7150', '13700'], ['1463751276', '33.7200', '33.7200', '33.7200', '33.7200', '7600']]


empty = []
listA = [1,2,3,4,5,6]
for line in test_list:
    aux = convert_timestamp(line[0])
    empty.append(aux)

#http://chartapi.finance.yahoo.com/instrument/1.0/VOD/chartdata;type=quote;range=1d/csv
closeP=[]
for i in stock_data:
    closeP.append(i[2])