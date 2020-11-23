# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
vals = [16844, 61200, 127718]#创建数据系列
fig, ax = plt.subplots()#创建子图
labels = 'Topic1', 'Topic2', 'Topic3'
colors = ['salmon', 'm', 'green']
explode = (0.03, 0.05, 0.05)
ax.pie(vals, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90,radius=0.8)
ax.set(aspect="equal")#设置标题以及图形的对称 #, title='Number of documents in three topics'
plt.show()