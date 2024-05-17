import pandas as pd
from matplotlib import pyplot as plt
from statistics import mean

df1=pd.read_csv('Teams4.csv')
df2=pd.read_csv('IlkerQuery.csv')
df1a=df1.set_index('user')
df2a=df2.set_index('user')

df3=pd.merge(df1, df2, how='right')
type(df3)

plt.plot((df3.MeetingCount+df3.CallCount), df3.YuzlukNot, '.')
plt.xlabel('aktivnost')
plt.ylabel('uspeh')
plt.show()

df4 = df3[(df3.DersPlanYil==2019.0) & (df3.DersPlanDonem==2.0)]

plt.xlabel('aktivnost')
plt.ylabel('uspeh')
plt.plot((df4.MeetingCount+df4.CallCount), df4.YuzlukNot, '.')
plt.scatter(100,100,c='red')
plt.show()

import array
plt.xlabel('aktivnost')
plt.ylabel('uspeh')

EnYuksekDeger=int((max(df4.MeetingCount)))
print(EnYuksekDeger)
for i in range (0,EnYuksekDeger):
    df6=df4.query("MeetingCount == @i")
    if df6.YuzlukNot is None:
        df6.YuzlukNot=50
    avg=mean(df6.YuzlukNot)
   # print(avg)
  #  plt.scatter((df6.MeetingCount+df6.CallCount), df6.YuzlukNot,c='red')
    plt.scatter(i,avg,c='blue')

plt.show()

import array
plt.xlabel('aktivnost')
plt.ylabel('uspeh')

EnYuksekDeger=int((max(df4.MeetingCount)))

for i in range (0,EnYuksekDeger):
    df6=df4.query("MeetingCount == @i")
    if df6.YuzlukNot is None:
        df6.YuzlukNot=50
    avg=mean(df6.YuzlukNot)

   # print(avg)
    plt.scatter((df6.MeetingCount+df6.CallCount), df6.YuzlukNot,c='red')
    plt.scatter(i,avg,c='blue')

plt.show()

import numpy as np
plt.xlabel('aktivnost')
plt.ylabel('uspeh')

#EnYuksekDeger=int(max(df4.MeetingCount))

for i in range (0,50):
    df6=df4.query("MeetingCount == @i")
    if df6.YuzlukNot is None:
        df6.YuzlukNot=50
    avg=mean(df6.YuzlukNot)
   # print(avg)
    # plt.scatter((df6.MeetingCount+df6.CallCount), df6.YuzlukNot,c='red')
    # Plot the data    
    data_line = ax.plot(i,avg, label='Data', marker='o')
    
    plt.scatter(i,avg,c='blue')
#    plt.plot(i,avg)  

plt.show()
