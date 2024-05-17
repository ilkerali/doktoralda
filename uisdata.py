import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df1 = pd.read_csv('Teams4.csv')
df2 = pd.read_csv('IlkerQuery.csv')
df3 = pd.merge(df1, df2, how='right')
Потоа, ги цртаме графиците користејќи matplotlib:
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.plot(df4.MeetingCount+df4.CallCount, df4.YuzlukNot, '.')
plt.xlabel('aktivnost')
plt.ylabel('uspeh')
plt.subplot(1,2,2)
activites = df3.aktivnost.dropna()
plt.plot(activities, df3.uspeh, 'o')
plt.xlabel('aktivnost')
plt.ylabel('uspeh')
plt.tight_layout()
plt.show()
За скатер дијаграмот:
EnYuksekDeger = int(df4.MeetingCount.max())
for i in range(EnYuksekDeger+1):
data = df4[df4.MeetingCount == i]
if not data.empty:
avg = data.YuzlukNot.mean()
plt.scatter(i, avg, c='blue')
plt.xlabel('MeetingCount')
plt.ylabel('Prosecna YuzlukNot')
plt.show()
