with open("books.ico", "rb") as image:
    a = image.read()
data = (repr(a))

data = data[2:]  #trim out the b'
data = data[:-1]  #trim out the last '

dataList = data.split('\\x')  #split by hex unit
dataList = dataList[1:] #remove the blank  value at the beginning

totalLen = len(dataList)

i = 0
hexline = ''
lenCount = 0
groupCount = 0
for hex in dataList:
    if(lenCount == totalLen-1):
        hexline += '\\x' + hex
        print('b\'' + hexline + '\'')
    if(i == 16):  #change number of grouping here       
        print('b\'' + hexline + '\'')
        i=0
        hexline = ''
        groupCount += 1

    hexline += '\\x' + hex
    i+=1         
    lenCount += 1