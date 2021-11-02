with open('C://Users//chlgo//cj//new_contents.txt','r',encoding='UTF-8') as f :
    data = f.read().split(",")
import pandas as pd
import re
data = pd.DataFrame(data)

title_date=[]
'''url_index = data[data[0].str.startswith('http://naver.me/')].index
data.dropna()
data = data.drop(url_index)'''
title_index = list(data[data[0].str.endswith(':')].index)
event_date=[]
for x in title_index:
    event_string = data[0][x]
    title_date_list = re.findall('\d+',event_string)
    if len(title_date_list) ==1:
        title_date.append(title_date_list[0])
    else:
        title_date.append(title_date_list[0]+'/'+title_date_list[1])
print(len(title_date))
event_time=[]
event_brand=[]

for x in range(len(title_index)-1):
    event_data = data[0][title_index[x]:title_index[x+1]]
    event_data = list(event_data)
    print(title_date[x])
    for index,value in enumerate(event_data):

        if '오후' in value or '낮'in value or '오전' in value:
            event_time.append(value)
            try:

                brand_name = event_data[index+1]
                event_brand.append(brand_name)
                event_date.append(title_date[x])
            except:
                pass
print(len(event_date))
print(len(event_time))
print(len(event_brand))

# dictionary of lists
dict = {'event_date': event_date, 'event_time': event_time, 'event_brand': event_brand}
df = pd.DataFrame(dict)
print(df)