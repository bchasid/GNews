# This is a sample Pyt  hon script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time

import pandas as pd
from bs4 import BeautifulSoup

import requests
from lxml.html import fromstring
# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr')[:10]:
#     if i.xpath('.//td[7][contains(text(),"yes")]'):
#     #Grabbing IP and corresponding PORT
#     proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#     proxies.add(proxy)
#     return proxies

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
        df = pd.DataFrame({'Date': [datetime.date(year, mon, day)], 'Symbol': [symbol], 'CNT': 0, 'result': "empty"})
    except http.client.HTTPException as e:
        # other kind of error occured during request
        print('request error')
        df = pd.DataFrame({'Date': [datetime.date(year, mon, day)], 'Symbol': [symbol], 'CNT': 0, 'result': "empty"})
    except Exception as e:
        print('other exception')
        df = pd.DataFrame({'Date': [datetime.date(year, mon, day)], 'Symbol': [symbol], 'CNT': 0, 'result': "empty"})
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
    symbol_list = ["UEIC","UEPS","UFCS","UFPI","UFPT","UG","UGRO","UHAL","UIHC","UK","ULBI","ULCC","ULH","ULTA","UMBF","UMPQ","UNAM","UNB","UNIT","UNTY","UONE","UPC","UPLD","UPST","UPWK","URBN","URGN","UROY","USAK","USAP","USAU","USCR","USEG","USIO","USLM","USWS","UTHR","UTMD","UTME","UTSI","UVSP","UXIN","VABK","VACC","VACQ","VALN","VALU","VBFC","VBIV","VBLT","VBTX","VC","VCEL","VCKA","VCNX","VCTR","VCVC","VCYT","VECO","VECT","VELO","VENA","VEON","VERA","VERB","VERI","VERO","VERU","VERV","VERX","VERY","VEV","VFF","VG","VIAC","VIAV","VICR","VIEW","VIH","VII","VINC","VINO","VINP","VIOT","VIR","VIRC","VIRI","VIRT","VIRX","VISL","VITL","VIVE","VIVO","VJET","VKTX","VLAT","VLDR","VLGEA","VLON","VLY","VMAC","VMAR","VMD","VMEO","VNDA","VNET","VNOM","VOD","VOR","VOSO","VOXX","VPCB","VRA","VRAR","VRAY","VRCA","VRDN","VREX","VRM","VRME","VRNA","VRNS","VRNT","VRPX","VRRM","VRSK","VRSN","VRTS","VRTX","VS","VSAT","VSEC","VSTA","VSTM","VTAQ","VTGN","VTIQ","VTNR","VTRS","VTRU","VTSI","VTVT","VUZI","VVOS","VVPR","VWE","VWTR","VXRT","VYGR","VYNE","VYNT","WABC","WAFD","WAFU","WALD","WASH","WATT","WAVE","WB","WBA","WDAY","WDC","WDFC","WEN","WERN","WETF","WEYS","WFCF","WFRD","WHF","WHLM","WHLR","WILC","WIMI","WINA","WING","WINT","WIRE","WISA","WISH","WIX","WKEY","WKHS","WKME","WLDN","WLFC","WLTW","WMG","WMPN","WNEB","WNW","WOOF","WORX","WPRT","WRAP","WRLD","WSBC","WSBF","WSC","WSFS","WSTG","WTBA","WTER","WTFC","WTREP","WTRH","WVE","WVFC","WVVI","WW","WWD","WYNN","XAIR","XBIO","XBIT","XCUR","XEL","XELA","XELB","XENE","XENT","XERS","XFOR","XGN","XLNX","XLRN","XM","XMTR","XNCR","XNET","XOG","XOMA","XONE","XP","XPDI","XPEL","XPER","XRAY","XSPA","XTLB","YELL","YGMZ","YI","YJ","YMAB","YMTX","YNDX","YORW","YQ","YSAC","YTEN","YTRA","YVR","YY","Z","ZBRA","ZCMD","ZEAL","ZEUS","ZG","ZGNX","ZGYH","ZI","ZION","ZIOP","ZIVO","ZIXI","ZKIN","ZLAB","ZM","ZNGA","ZNTE","ZNTL","ZS","ZSAN","ZTAQU","ZUMZ","ZVO","ZWRK","ZY","ZYNE","ZYXI"]

#
#    symbol_list = ["AAPL", "CLOV", "WISH"]
    dft = pd.DataFrame(columns=['Date','Symbol','CNT','result'])
    dft.to_csv('gnews_short.csv')
    for sym in symbol_list:
        df1 = pd.DataFrame(columns=['Date', 'Symbol', 'CNT', 'result'])

        dr = pd.date_range('5/15/2021', '7/14/2021')
        for single_date in dr:
            dft=get_gnews(single_date.day,single_date.month,single_date.year,sym)
            dft.to_csv('gnews_short.csv',mode = 'a', header = False)
            df1=df1.append(dft)
            time.sleep(1)
        df1.to_csv('gnews_shrt_'+sym+'.csv')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
