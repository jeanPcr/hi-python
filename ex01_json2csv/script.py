import json
import csv

src = open("sample.json","r")
dest = open('./csv_file.csv', 'w',encoding='UTF8')
data = json.loads(src.read())
writer = csv.writer(dest)
headers = []
fields = []

for i in data :
    for j in data[i] :
        print(str(data[i][j]))
        headers.append(str(i+"."+j))
        fields.append(str(data[i][j]))

writer.writerow(headers)
writer.writerow(fields)
    


dest.close()
src.close()