import tushare as ts
import pandas as pd
import numpy as np
import datetime
import glob
import time
import csv
import re
from dateutil.parser import parse
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

sns.set_style("whitegrid", {"font.sans-serif": ['KaiTi', 'Arial']})

def get_all_comp():
    all_files = glob.glob(r'D:/GFZQ/GFZQ/xuesu2018/xuesu/*.csv')
    return all_files

def get_wenben(path):
    csvfile = open(path, 'r', encoding='UTF-8')
    reader = csv.reader(csvfile)
    return reader

def get_all_code(): #��ȡȫ��2016�ٰ�ҵ��˵�������ҵ����,ʱ��
    path2 = 'D:/GFZQ/GFZQ/project/7_30_test/data/train/2016all_train.csv'
    reader2 = get_wenben(path2)
    return reader2

def get_com_information(): #��ȡҵ��˵����ʱ�䣬��ƣ�ȫ�ƣ���Ʊ����
    reader2 = get_all_code()
    companies =[]
    for item in reader2:
        companies.append(item)
    return companies

def get_emotion():
    return

#��ȡ��Ʊ�ǵ�����
def get_price(code, date, days):
    year = date[:4]
    month = date[5:7]
    # print("month:%s" % month)
    day = date[8:10]
    # print ("day:%s"%day)
    date = re.sub('/', '-', date)
    now = datetime.datetime(int(year), int(month), int(day))
    delta = datetime.timedelta(days)
    start = now - delta
    end = now + delta  # ���ڻ���
    now = now.strftime('%Y-%m-%d')
    start_date = start.strftime('%Y-%m-%d')
    end_date = end.strftime('%Y-%m-%d')
    #print("from %s to %s"%(start_date,end_date))
    k1 = ts.get_hist_data(code, start= now, end=end_date)
    k2 = ts.get_hist_data(code, start=start_date, end=now)
    #print ( k.head(10) ) #�鿴ǰ10������
    k1 = k1.sort_index(axis=0, ascending=True)  # ��index ������������
    k1 = k1.sort_index(axis=0, ascending=True)
    # ���ƶ�ƽ����������Ԥ��
    lit = ['open', 'high', 'close', 'low']  # ��������ֻ��ȡ��������(��ߡ���͡����̡�����)
    data1 = k1[lit]
    data2 = k2[lit]
    # print (data)
    d_one = data1.index  # ����9�н�object��indexת��Ϊdatetime����
    d_two = []
    d_three = []
    for i in d_one:
        d_two.append(i)
    for i in range(len(d_two)):
        d_three.append(parse(d_two[i]))
    data1_ = pd.DataFrame(data1, index=d_three, dtype=np.float64)
    d_one1 = data1.index  # ����9�н�object��indexת��Ϊdatetime����
    d_two1 = []
    d_three1 = []
    for i in d_one:
        d_two1.append(i)
    for i in range(len(d_two1)):
        d_three1.append(parse(d_two1[i]))
    data2_ = pd.DataFrame(data2, index=d_three1, dtype=np.float64)
    # �����µ�DataFrame����indexΪת����d_three����Ȼ��Ҳ����ʹ��date_range()������ʱ��index
    length1 = len(data1_['close'])
    length2 = len(data2_['close'])
    try:
        ave_close1 = sum(data1_['close']) / (length1)
        ave_close2 = sum(data2_['close']) / (length2)
        last_day1 = data1_['close'][-1]
        last_day2 = data2_['close'][-1]
        fluctuation1 = (last_day1 - ave_close1) / ave_close1   #ҵ��˵�����days����ǵ�����
        fluctuation2 = (last_day2 - ave_close2) / ave_close2   #ҵ��˵����ǰdays����ǵ�����
        change = (ave_close1 - ave_close2)/ave_close2
    except ZeroDivisionError as e:
        fluctuation1 = 0
        fluctuation2 =0
        change = 0

        #print("average_price:%d,last_day_price:%d" % (ave_close, last_day))
    #print('�Ƿ���%0.4f%%' % fluctuation)
    # plt.plot(data2['close'])
    # # ��Ȼ���ݷ�ƽ�ȣ�����������Ҫ�����
    # plt.title('����ÿ�����̼�')
    # plt.show()
    return fluctuation1,fluctuation2,change

def getDifferentDay(all):
    day5 =[]
    day10 =[]
    day20=[]
    day60=[]
    day120 = []
    day250 =[]
    day364 =[]
    for item in all:
        day5.append(item[0])
        day10.append(item[1])
        day20.append(item[2])
        day60.append(item[3])
        day120.append(item[4])
        day250.append(item[5])
        day364.append(item[6])
    return day5,day10,day20,day60 ,day120,day250,day364

def savePriceChange(day5, day10, day20, day60, day120, day250, day364,date,short,full,code):
    # date =[]
    # short =[]
    # full =[]
    # code =[]
    # length =len(companies)
    # for i in range(length):
    #     date.append(companies[i][0])
    #     short.append(companies[i][0])
    #     full.append(companies[i][0])
    #     code.append(companies[i][0])
    # day5_column = pd.Series(day5, name='days5')
    # day10_column = pd.Series(day10, name='days10')
    # day20_column = pd.Series(day20, name='days20')
    # day60_column = pd.Series(day60, name='days60')
    # day120_column = pd.Series(day120, name='days120')
    # day250_column = pd.Series(day250, name='days250')
    # day364_column = pd.Series(day364, name='days364')
    # date_column = pd.Series(date, name='date')
    # short_column = pd.Series(short, name='short')
    # full_column = pd.Series(full, name='full')
    # code_column = pd.Series(code, name='code')

    # result_dict = {' date_column':date
    #                'code_column':code
    #                ''short_column','full_column','day5_column','day10_column','day20_column','day60_column' ,'day120_column ','day250_column','day364_column '
    #                'target_id': target_id,
    #                'similarity': similarity,
    #                'source_title': source_title,
    #                'target_title': target_title}

    predictions =  ['date','code','short','full','day5','day10','day20','day60' ,'day120 ','day250','day364 ']
       # pd.concat([answer_column, question_column], axis=1)
    df1 = pd.DataFrame({'date':date,'code':code,'short':short,'full':full,'day5':day5,'day10': day10,'day20':day20 ,'day60':day60,'day120':day120 ,'day250':day250,'day364':day364},columns=predictions)
    df1.to_csv('D:/GFZQ/GFZQ/project/7_30_test/data/priceChange/priceChange.csv', index=False)

def cal_time(timeUse):
    if timeUse <= 60:
        print ("timeUse:%ssec"%timeUse)
    if 60 < timeUse <=  60*60.0:
        print ("timeUse:%smins"%(timeUse/60.0))
    if 60*60.0 < timeUse <=  60*60*60.0:
        print ("timeUse:%shours"%(timeUse/(60*60.0)))

if __name__ == "__main__":
    time1 = time.clock()
    date1 =[]
    short1 =[]
    full1 =[]
    code1 =[]
    companies = get_com_information()
    length = len(companies)
    allChange = []          #ҵ��˵����ǰ���ǵ�����
    allAfterChange =[]      #ҵ��˵����֮���ǵ�����
    for i in range(length):
        print (companies[i])
        date1.append(companies[i][0])
        short1.append(companies[i][1])
        full1.append(companies[i][2])
        code1.append(companies[i][3])

        code = companies[i][3]  #��Ʊ����
        date = companies[i][0]  #ҵ��˵����ٰ�ʱ��
        priceChange = []
        changeAfterCon =[]
        days = [5, 10, 20, 60, 120, 250, 364]
        #days=[5]
        for j in days:
            try:
                fluctuation1, fluctuation2, change = get_price(code, date, i)
                priceChange.append(change)
                changeAfterCon.append(fluctuation1)
                #print (companies[i][2],fluctuation)
            except AttributeError as e:
                fluctuation1 = 0
                change = 0
                priceChange.append(change)
                changeAfterCon.append(fluctuation1)
                #print ("%s has no code"%companies[i][1])
                #break
            #print (priceChange)
        allChange.append(priceChange)
        allAfterChange.append(changeAfterCon)
    day5, day10, day20, day60, day120, day250, day364 = getDifferentDay(allAfterChange)
    #print (date1)
    #print (short1)
    savePriceChange(day5, day10, day20, day60, day120, day250, day364,date1,short1,full1,code1)
    cal_time(time.clock() - time1)



    ###test
    # code = '002029'
    # start_date = '2016/10/30'
    # days = [5, 10, 20, 60, 120, 250, 364]
    # days =31   #ʱ����
    # all =[]
    # for i in days:
    #     fluctuation1, fluctuation2, change =get_price(code, start_date, i)
    #     all.append(change)
    # for i in all:
    #     print (i)