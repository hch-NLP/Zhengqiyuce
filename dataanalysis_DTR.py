#!/usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
import codecs
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl   #显示中文
from sklearn.model_selection import train_test_split #这里是引用了交叉验证
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import matplotlib.pyplot as plt
def mul_lr():
    pd_data=pd.read_excel('F:\\pycharm\\data\\ZQYC\\data\\zhengqi_train.xls')
    X = pd_data.loc[:, ('V0','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','V29','V30','V31','V32','V33','V34','V35','V36','V37')]
    y = pd_data.loc[:, 'target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
    print('X_train.shape={}\n y_train.shape ={}\n X_test.shape={}\n,  y_test.shape={}'.format(X_train.shape,
                                                                                              y_train.shape,
                                                                                              X_test.shape,
                                                                                              y_test.shape))
    linreg =DecisionTreeRegressor()
    model = linreg.fit(X_train, y_train)
    # pd_datatest = pd.read_excel('F:\\pycharm\\data\\ZQYC\\data\\zhengqi_test.xls')
    # y_pred = model.predict(pd_datatest)
    y_pred = model.predict(X_test)
    print(y_pred)  # 38个变量的预测结果
    sum_mean = 0
    for i in range(len(y_pred)):
        sum_mean += (y_pred[i] - y_test.values[i]) ** 2
    sum_erro = np.sqrt(sum_mean / len(y_pred))  # 这个38是你测试级的数量
    # calculate RMSE by hand
    print("RMSE by hand:", sum_erro)
    plt.figure()
    plt.plot(np.arange(len(y_pred)), y_test, 'go-', label='true value')
    plt.plot(np.arange(len(y_pred)), y_pred, 'ro-', label='predict value')
    plt.title('score')
    plt.legend()
    plt.show()
    # fr = codecs.open('C:\\Users\\lenovo\\Desktop\\result.txt', 'w', 'utf-8')
    # for v in y_pred:
    #     fr.write(str('%.3f' % v)+'\n')
    # fr.flush()
    # fr.close()

if __name__ == '__main__':
    mul_lr()