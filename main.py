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
        df = pd.DataFrame({'Date': [datetime.date(year, mon, day)], 'Symbol': [symbol], 'CNT': 0, 'result': "empty"})
    except http.client.HTTPException as e:
        # other kind of error occured during request
        print('request error')
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
    symbol_list = [  "HIHO", "HIII", "HIMX", "HITI", "HJLI", "HLAH", "HLG", "HLIO",
                    "HLIT", "HLNE", "HLXA", "HMCO", "HMHC", "HMNF", "HMPT", "HMST", "HMTV", "HNNA", "HNRG", "HNST",
                    "HOFT", "HOFV", "HOLI", "HOLX", "HOMB", "HON", "HONE", "HOOK", "HOPE", "HOTH", "HOVNP", "HOWL",
                    "HPK", "HQI", "HQY", "HRMY", "HROW", "HRTX", "HRZN", "HSAQ", "HSDT", "HSIC", "HSII", "HSKA", "HSON",
                    "HST", "HSTM", "HSTO", "HTBI", "HTBK", "HTBX", "HTGM", "HTHT", "HTIA", "HTLD", "HTLF", "HTOO",
                    "HUBG", "HUDI", "HUGE", "HUIZ", "HURC", "HURN", "HUSN", "HUT", "HVBC", "HVBT", "HWBK", "HWC",
                    "HWKN", "HX", "HYAC", "HYFM", "HYMC", "HYRE", "HYW", "HZNP", "IAC", "IART", "IAS", "IBCP", "IBEX",
                    "IBKR", "IBOC", "IBRX", "IBTX", "ICAD", "ICBK", "ICCC", "ICCH", "ICFI", "ICHR", "ICLK", "ICLR",
                    "ICMB", "ICON", "ICPT", "ICUI", "IDBA", "IDCC", "IDEX", "IDN", "IDRA", "IDXX", "IDYA", "IEA", "IEC",
                    "IEP", "IESC", "IFBD", "IFMK", "IFRX", "IGAC", "IGIC", "IGMS", "IGNY", "IHRT", "III", "IIII",
                    "IIIV", "IIN", "IIVI", "IKNA", "IKNX", "IKT", "ILMN", "ILPT", "IMAB", "IMAC", "IMCC", "IMCR",
                    "IMGN", "IMKTA", "IMMP", "IMMR", "IMNM", "IMOS", "IMPL", "IMRA", "IMTE", "IMTX", "IMUX", "IMV",
                    "IMVT", "IMXI", "INBK", "INBX", "INCY", "INDB", "INDI", "INDT", "INFI", "INFN", "INGN", "INKA",
                    "INM", "INMB", "INMD", "INNV", "INO", "INOD", "INOV", "INPX", "INSE", "INSG", "INSM", "INTA",
                    "INTC", "INTG", "INTU", "INTZ", "INVA", "INVE", "INVO", "INVZ", "INZY", "IONS", "IOSP", "IOVA",
                    "IPA", "IPAR", "IPDN", "IPGP", "IPHA", "IPLDP", "IPSC", "IPVI", "IPW", "IPWR", "IQ", "IRBT", "IRCP",
                    "IRDM", "IRIX", "IRMD", "IROQ", "IRTC", "IRWD", "ISAA", "ISBC", "ISEE", "ISIG", "ISLE", "ISNS",
                    "ISPC", "ISRG", "ISSC", "ISTR", "ISUN", "ITAC", "ITCI", "ITHX", "ITI", "ITIC", "ITMR", "ITOS",
                    "ITQ", "ITRI", "ITRM", "ITRN", "IVA", "IVAC", "IZEA", "JACK", "JAGX", "JAKK", "JAMF", "JAN", "JANX",
                    "JAZZ", "JBHT", "JBLU", "JBSS", "JCIC", "JCOM", "JCS", "JCTCF", "JD", "JFIN", "JFU", "JG", "JJSF",
                    "JKHY", "JMPNL", "JNCE", "JOAN", "JOBS", "JOFF", "JOUT", "JRJC", "JRSH", "JRVR", "JSM", "JUGGU",
                    "JUPW", "JVA", "JWEL", "JYAC", "JYNT", "JZXN", "KAII", "KAIIU", "KAIR", "KALA", "KALU", "KALV",
                    "KARO", "KBAL", "KBNT", "KBSF", "KC", "KDMN", "KDNY", "KDP", "KE", "KELYA", "KEQU", "KERN", "KFFB",
                    "KFRC", "KHC", "KIDS", "KIII", "KIN", "KINS", "KINZ", "KIRK", "KLAC", "KLAQ", "KLDO", "KLIC",
                    "KLXE", "KMDA", "KMPH", "KNBE", "KNDI", "KNSA", "KNSL", "KNTE", "KOD", "KOPN", "KOR", "KOSS",
                    "KPLT", "KPTI", "KRBP", "KRKR", "KRMD", "KRNL", "KRNT", "KRNY", "KRON", "KROS", "KRT", "KRTX",
                    "KRUS", "KRYS", "KSI", "KSMT", "KSPN", "KTCC", "KTOS", "KTRA", "KURA", "KURI", "KVHI", "KVSA",
                    "KXIN", "KYMR", "KZIA", "KZR", "LAAAU", "LABP", "LAKE", "LAMR", "LANC", "LAND", "LARK", "LASR",
                    "LATN", "LAUR", "LAWS", "LAZR", "LAZY", "LBAI", "LBC", "LBPH", "LBPS", "LBRDA", "LBTYA", "LCA",
                    "LCAA", "LCAP", "LCNB", "LCUT", "LCY", "LDHA", "LE", "LECO", "LEDS", "LEE", "LEGA", "LEGH", "LEGN",
                    "LEGO", "LESL", "LEVL", "LEXX", "LFMD", "LFST", "LFTR", "LFUS", "LFVN", "LGAC", "LGHL", "LGIH",
                    "LGND", "LGO", "LGVN", "LHAA", "LHCG", "LHDX", "LI", "LIFE", "LILA", "LINC", "LIND", "LINK", "LIQT",
                    "LITE", "LITTU", "LIVE", "LIVK", "LIVN", "LIVX", "LIXT", "LIZI", "LJAQ", "LJPC", "LKCO", "LKFN",
                    "LKQ", "LLNW", "LMACA", "LMAO", "LMAT", "LMB", "LMFA", "LMNL", "LMNR", "LMNX", "LMPX", "LMRK",
                    "LMST", "LNDC", "LNSR", "LNT", "LNTH", "LOAN", "LOB", "LOCO", "LOGI", "LOGC", "LOOP", "LOPE",
                    "LORL", "LOTZ", "LOVE", "LPCN", "LPLA", "LPRO", "LPSN", "LPTH", "LPTX", "LQDA", "LQDT", "LRCX",
                    "LRFC", "LRMR", "LSAQ", "LSBK", "LSCC", "LSEA", "LSTR", "LSXMA", "LTBR", "LTCH", "LTRN", "LTRPA",
                    "LTRX", "LULU", "LUMO", "LUNA", "LUNG", "LUXA", "LVOX", "LVRA", "LVTX", "LWAC", "LWAY", "LX",
                    "LXEH", "LXRX", "LYEL", "LYFT", "LYL", "LYRA", "LYTS", "LZ", "MAAC", "MACA", "MACK", "MACQ", "MACU",
                    "MACUW", "MAGS", "MANH", "MANT", "MAPS", "MAQC", "MAR", "MARA", "MARK", "MARPS", "MASI", "MASS",
                    "MAT", "MATW", "MAXN", "MAYS", "MBCN", "MBII", "MBIN", "MBIO", "MBNKP", "MBOT", "MBRX", "MBTC",
                    "MBUU", "MBWM", "MCAD", "MCBC", "MCBS", "MCFE", "MCFT", "MCHP", "MCHX", "MCMJ", "MCRB", "MCRI",
                    "MDB", "MDCA", "MDGL", "MDGS", "MDIA", "MDJH", "MDLZ", "MDNA", "MDRR", "MDRX", "MDVL", "MDWD",
                    "MDWT", "MDXG", "ME", "MEDP", "MEDS", "MEIP", "MELI", "MEOH", "MERC", "MESA", "MESO", "METC",
                    "METX", "MF", "MFH", "MFIN", "MFNC", "MGEE", "MGI", "MGIC", "MGLN", "MGNI", "MGNX", "MGPI", "MGRC",
                    "MGTA", "MGTX", "MGYR", "MHLD", "MICT", "MIDD", "MILE", "MIME", "MIND", "MINM", "MIRM", "MIRO",
                    "MIST", "MITAU", "MITC", "MITK", "MITO", "MKD", "MKSI", "MKTX", "MKTY", "MLAB", "MLAC", "MLCO",
                    "MLHR", "MLVF", "MMAC", "MMAT", "MMLP", "MMSI", "MMYT", "MNDO", "MNDY", "MNKD", "MNMD", "MNOV",
                    "MNPR", "MNRO", "MNSB", "MNST", "MNTK", "MNTV", "MNTX", "MODV", "MOFG", "MOGO", "MOHO", "MOLN",
                    "MOMO", "MON", "MOR", "MORF"]

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
