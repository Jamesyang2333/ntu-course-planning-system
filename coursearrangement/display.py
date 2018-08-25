from random import randint
from coursearrangement.DBHelper import DBHelper


color1 = ["#FFFAFA","#DA891E","#3F813F","#F6BF1C","#de6950","#526183","#4C4C4C","#74A474","#4499EE","#8EC2F5","#D4D4D4","#55A255"]


def indexcolor(number,oneindex,content,colornumber,coursename,helper1,dict1):

    print(oneindex)
    x = helper1.get_info(oneindex)[0]
    print(x)
    for i in range(6):
        if x[3*i+1] == None:
            break
        elif x[3*i+1] == 0:
            digit = [int(i) for i in x[3*i].split()]
            for element in range(digit[0], digit[1]):
                name = str(number)+"color"+str(element).zfill(2)
                content[name] = color1[colornumber]
                name = str(number) + "content" + str(element).zfill(2)
                content[name] = coursename + "\n" + x[3*i+2]


        elif x[3*i+1] == 1:
            digit = [int(i) for i in x[3*i].split()]
            for element in range(digit[0], digit[1]):
                name = str(number) + "content" + str(element).zfill(2)
                if name in dict1.keys():
                    content[name] = dict1[name] +"\n"+  "Odd week:  "+ coursename + "\n" + x[3*i+2]

                else:
                    content[name] = "Odd week:  " + coursename + "\n" + x[3*i+2]
                    dict1[name] = "Odd week:  " + coursename + "\n" + x[3*i+2]
                    name = str(number) + "color" + str(element).zfill(2)
                    content[name] = color1[colornumber]
        elif x[3*i+1] == 2:
            digit = [int(i) for i in x[3*i].split()]
            for element in range(digit[0], digit[1]):
                name = str(number) + "content" + str(element).zfill(2)
                if name in dict1.keys():
                    content[name] = dict1[name] +"\n"+  "Even week: "+ coursename + "\n" + x[3*i+2]
                    name = str(number) + "color" + str(element).zfill(2)
                    content[name] = color1[1]
                else:
                    content[name] = "Even week: " + coursename + "\n" + x[3*i+2]
                    dict1[name] = "Even week: " + coursename + "\n" + x[3*i+2]
                    name = str(number) + "color" + str(element).zfill(2)
                    content[name] = color1[colornumber]
        print(dict1)
        print(digit)




def writecontent(number,index,content,list):
    helper1 = DBHelper()
    n = len(index)
    for i in range(n):
        name = str(number)+"course"+str(i)
        content[name] = str(list[n-i-1])+'-'+str(index[i])+"; "
    name = str(number) + 'font_color'
    content[name] = "color:" + color1[0]
    name = str(number) +'edge'
    content[name] = color1[1]

    i = 2
    dict1 = {'name': 'content'}
    for element in index:
        indexcolor(number,element,content,i,str(list[n-i+1]),helper1,dict1)
        i = i+1



