"""
date:2018-7-31
function:�����ײƾ���ץȡ�ɼ���Ϣ(��ѡȡ2016��ٰ��ҵ��˵������Ϣ��
author��susuxuer
"""
import urllib.request
import re
import csv

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

# ��ȡ��Ʊ�����б�
def urlTolist(companies):
    allCodeList =[]
    for item in companies:
        allCodeList.append(item[3])
        #print (item)
    return allCodeList
def get_price(allCodelist):
    for code in allCodelist:
        print('���ڻ�ȡ%s��Ʊ����...' % code)
        if code:
            if code[0] == '6':
                url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
                      '&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
            else:
                url = 'http://quotes.money.163.com/service/chddata.html?code=1' + code + \
                      '&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
            urllib.request.urlretrieve(url, 'D:/GFZQ/GFZQ/project/7_30_test/data/train/code/' + code + '.csv')  # ���Լ�һ������dowmback��ʾ���ؽ���

if __name__=='__main__':
    companies  = get_com_information()
    allCodelist = urlTolist(companies)
    get_price(allCodelist)

