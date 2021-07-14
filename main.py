# This is a sample Pyt  hon script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time

import pandas as pd
from bs4 import BeautifulSoup



def get_gnews(day:int,mon:int,year:int,symbol:str):

    import http.client
    import re
    import socket

    conn = http.client.HTTPSConnection("www.google.com")

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    payload = ""
    # symbol="IBM"
    # day=6
    # mon=7
    # year=2021
    try:
        conn.request("GET",
    #             "/search?q="+symbol+"&biw=930&bih=937&sxsrf=ALeKk02JAmuN12pYhT-qxERYzfKfL0XqVw%3A1626167326884&source=lnt&tbs=cdr%3A1%2Ccd_min%3A"+str(mon)+"%2F"+str(day)+"%2F"+str(year)+"%2Ccd_max%3A"+str(mon)+"%2F"+str(day)+"%2F"+str(year)+"&tbm=nws",
                "/search?q="+symbol+"&biw=930&bih=937&tbs=cdr%3A1%2Ccd_min%3A"+str(mon)+"%2F"+str(day)+"%2F"+str(year)+"%2Ccd_max%3A"+str(mon)+"%2F"+str(day)+"%2F"+str(year)+"&tbm=nws&sxsrf=ALeKk03qXGSoxc5QALiMlSROBB48ZEoo6w%3A1626260334382&ei=bsPuYNHbFpLJkwXlyqeYAQ&oq=AAL&gs_l=psy-ab.3...0.0.0.18275.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.SCFAjSnsf28",
                 payload, headersList)
        response = conn.getresponse()
        result = response.read()
    except socket.timeout as st:
        # do some stuff, log error, etc.
        print('timeout received')
    except http.client.HTTPException as e:
        # other kind of error occured during request
        print('request error')
    else:  # no error occurred
        resultstr = str(result,"latin-1")
        soup = BeautifulSoup(resultstr, 'html5lib')
        div=soup.find("div",{"id":"result-stats"})
        if  div!= None :
            print(symbol, " ", datetime.date(year,mon,day), " ",str(div))
            count=int(str(re.findall("\d{1,3}(?:,\d{3})*", str(div))[0]).replace(',',''))
            df=pd.DataFrame({'Date':[datetime.date(year,mon,day)],'Symbol':[symbol],'CNT':[count],'result':[str(div)]})
        else :
            df = pd.DataFrame({'Date': [datetime.date(year, mon, day)], 'Symbol': [symbol], 'CNT': 0, 'result': "empty"})
    finally:
        conn.close()
    return df



    # from GoogleNews import GoogleNews
    # from newspaper import Article
    # import pandas as pd
    # googlenews = GoogleNews()
    # googlenews = GoogleNews(lang='en')
    # #googlenews = GoogleNews(period='7d')
    # googlenews = GoogleNews(start='07/07/2020',end='07/07/2020')
    # googlenews = GoogleNews(encode='utf-8')
    # #googlenews.get_news('IBM')
    # #result = googlenews.result()
    # #df = pd.DataFrame(result)
    # googlenews.search('IBM')
    # result = googlenews.result()
    # cnt = googlenews.total_count()
    # df = pd.DataFrame(result)
    # cnt1 = 0
    # cnt1 = len(result)
    #
    # for i in range(2,3):
    #     googlenews.getpage(i)
    #     result=googlenews.result()
    #     df = df.append(pd.DataFrame(result))
    #     cnt1 += len(result)
    #
    #
    # print("count is", cnt, " ", cnt1 )
    # df.to_csv("gnews.csv")



if __name__ == '__main__':
 #   print_hi('PyCharm')
   # symbol_list=["CLOV","WISH","AMD","AAL","TLRY","MSFT","OGI","TSLA","SOFI","JD","INTC","UAL","MU","FCEL","MRIN","CPOP","VIVO","ARVLW","SLP","AKYA","IKNA","VOXX","TUSK","SHLS","ACMR","TALK","MASS","OLK","SLN","AFRM","BBGI","CLXT","MTEX","EVLO","GRIN"]
    symbol_list = [ "CPOP", "VIVO", "ARVLW", "SLP", "AKYA", "IKNA", "VOXX", "TUSK", "SHLS", "ACMR", "TALK", "MASS",
               "OLK", "SLN", "AFRM", "BBGI", "CLXT", "MTEX", "EVLO", "GRIN"]
#
#    symbol_list = ["AAPL", "CLOV", "WISH"]
    for sym in symbol_list:
        df1 = pd.DataFrame(columns=['Date','Symbol','CNT','result'])
        dr = pd.date_range('1/1/2021', '7/14/2021')
        for single_date in dr:
            dft=get_gnews(single_date.day,single_date.month,single_date.year,sym)
            dft.to_csv('gnews.csv',mode = 'a', header = False)
            df1=df1.append(dft)
            time.sleep(1)
        df1.to_csv('gnews_'+sym+'.csv,')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
