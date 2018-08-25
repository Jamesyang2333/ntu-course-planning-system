from bs4 import BeautifulSoup
import requests
from coursearrangement.DBHelper import DBHelper

def getDay(day):
    if not day:
        return None
    if(day == "MON"):
        return 0
    elif(day == "TUE"):
        return 1
    elif(day == "WED"):
        return 2
    elif(day == "THU"):
        return 3
    elif(day == "FRI"):
        return 4
    else:
        return 5

def getTime(time, day):
    if day == None:
        return None
    start = int(time[:2])
    end = int(time[5:7])
    start = day * 12 + start - 8
    end = day * 12 + end - 8
    return [start, end]


def save(courseName):
    data = {'acadsem':'2018%1B1','r_course_yr':'','r_subj_code':courseName,'r_search_type':'F','boption':'Search','acadsem':'2018%1B1',"staff_access":"false"}
    #headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

    res = requests.post("https://wish.wis.ntu.edu.sg/webexe/owa/AUS_SCHEDULE.main_display1", data=data)
    #print(res.text)
    #print(type(res))
    #print(type(res.text))
    soup = BeautifulSoup(res.text, "html5lib")
    count = 0
    helper1 = DBHelper()
    for items in soup.find_all('table'):
        if count > 0:
            fieldcount = 0
            indexNo = 0
            indexof = ""
            day = ""
            time = ""
            type = ""
            sessionCount = 1
            for item in items.find_all('td'):
                #print(item.text)
                if fieldcount == 0:
                    indexof = item.text
                elif fieldcount == 1:
                    type = item.text
                elif fieldcount == 3:
                    day = item.text
                elif fieldcount == 4:
                    time = item.text
                if fieldcount == 6:
                    sessionCount += 1
                    strlist = item.text.split(",")
                    if len(strlist) < 5:
                        kind = 0
                    elif int(strlist[3]) % 2 == 1:
                        kind = 1
                    else:
                        kind = 2
                    if(indexof != ""):
                        sessionCount = 1
                        indexNo = int(indexof)
                    dayNo = getDay(day.strip())
                    timeLst = getTime(time, dayNo)
                    if timeLst:
                        timeStr = str(timeLst[0]) + " " + str(timeLst[1])
                    else:
                        timeStr = str(-1) + " " + str(-1)
                    if(indexof != ""):
                        helper1.add_module(courseName, indexNo, sessionCount, timeStr, kind, type)
                    else:
                        helper1.update_module(indexNo, sessionCount, timeStr, kind, type)

                fieldcount += 1
                fieldcount %= 7

        count += 1
