# coding:utf-8
#day3.py - By: Shengjie Zhu - 周三 10月 9 2019

import pandas as pd
import numpy as np
import xlrd
from sklearn import preprocessing

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
xlsfile = r'E:\03 UCAS_doc\01 Course\python基础\day3\rz.xlsx'

sheet1 = pd.read_excel(xlsfile ,'Sheet1')

sheet1 = sheet1.fillna(0)
sheet1 = sheet1.replace({'体育':'作弊','军训':'缺考'},0)

sheet1['总成绩']=sheet1['英语']+sheet1['体育']+sheet1['军训']+sheet1['数分']+sheet1['高代']+sheet1['解几']

bins1 = [min(sheet1.总成绩)-1,400,450,max(sheet1.总成绩)+1]
labs1 = ['一般','较好','优秀']
insert1 = pd.cut(sheet1.总成绩,bins1,right=False,labels=labs1)
sheet1['总分评价'] = insert1

sheet1['min-max标准化之和']=\
(sheet1['英语']-sheet1['英语'].min())/(sheet1['英语'].max()-sheet1['英语'].min())+\
(sheet1['体育']-sheet1['体育'].min())/(sheet1['体育'].max()-sheet1['体育'].min())+\
(sheet1['军训']-sheet1['军训'].min())/(sheet1['军训'].max()-sheet1['军训'].min())+\
(sheet1['数分']-sheet1['数分'].min())/(sheet1['数分'].max()-sheet1['数分'].min())+\
(sheet1['高代']-sheet1['高代'].min())/(sheet1['高代'].max()-sheet1['高代'].min())+\
(sheet1['解几']-sheet1['解几'].min())/(sheet1['解几'].max()-sheet1['解几'].min())

bins2 = [min(sheet1['min-max标准化之和'])-1,3.5,4.5,max(sheet1['min-max标准化之和'])+1]
labs2 = ['一般','较好','优秀']
insert2 = pd.cut(sheet1['min-max标准化之和'],bins2,right=False,labels=labs2)
sheet1['min-max评价'] = insert2

sheet1['Z-score标准化之和']= \
preprocessing.scale(sheet1['英语'])+preprocessing.scale(sheet1['体育'])+\
preprocessing.scale(sheet1['军训'])+preprocessing.scale(sheet1['数分'])+\
preprocessing.scale(sheet1['高代'])+preprocessing.scale(sheet1['解几'])

bins3 = [min(sheet1['Z-score标准化之和'])-1,-1,2,max(sheet1['Z-score标准化之和'])+1]
labs3 = ['一般','较好','优秀']
insert3 = pd.cut(sheet1['Z-score标准化之和'],bins3,right=False,labels=labs3)
sheet1['Z-score评价'] = insert3

print('\n总成绩评价区间：最低--->400--->450--->最高\n\
min-max评价区间：最低--->3.5--->4.5--->最高\n\
Z-score标准化评价：最低--->-1--->2--->最高\n')
print(sheet1)

