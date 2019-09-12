import datetime
import requests
import csv
print('Beginning file download. It take some time to Download and read data')

url = 'https://press.radiocut.fm/bicycle-travels-jan-2018.csv'
request = requests.get(url)


with open('/home/rahul/csvFile.csv', 'wb') as csvFile:
    csvFile.write(request.content)

print('Download Complete')

with open('/home/rahul/csvFile.csv') as csvFile:
    readCsv = csv.reader(csvFile)
    header = next(readCsv)
    data = []
    for row in readCsv:
        format = '%Y-%m-%d %H:%M:%S'
        d=datetime.datetime.strptime(row[1], format)
        time = d.time()

        #append source station between 6am to 12pm in data list
        if time > datetime.time(6,0,0) and time < datetime.time(12,0,0):
            data.append([row[3],row[4]])

#make a unique data list
uniqStation = []
for row in data:
    if row not in uniqStation:
        uniqStation.append(row)

#check the list and count
mainData= []
for row in uniqStation:
    count = 0
    for i in data:
        if i[1] == row[1]:
            count+=1
    mainData.append([row[0], row[1], count])

#Then sort and find
bingo = sorted(mainData, key=lambda x: x[2], reverse=True)
top_five = bingo[:5]
# Top five source stations:
# Macacha G«äemes (code: 111): 454 trips
print('Top five source stations:')
for x in top_five:
    print('{} (code: {}): {} trips'.format(x[0],x[1],x[2]))