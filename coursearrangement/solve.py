
from coursearrangement.DBHelper import DBHelper
from coursearrangement import ntuCourse
def allCombination(coursesLst, conflicts):
    helper2 = DBHelper()
    slots = []
    result = []
    current = []
    Lst = []
    slots = [True for x in range(144)]
    for i in conflicts:
        slots[i] = False
        slots[i + 72] = False
    n = len(coursesLst)
    can = True
    sequence = []
    count = 0
    for course in coursesLst:
        allmodule = helper2.get_course(course)
        if not allmodule:
            ntuCourse.save(course)
            allmodule = helper2.get_course(course)
            if not allmodule:
                can = False
                break
            else:
                Lst.append(allmodule)
                sequence.append([len(allmodule), count])
        else:
            Lst.append(allmodule)
            sequence.append([len(allmodule), count])
        count += 1
    if not can:
        return []
    newlst = [0 for i in range(n)]
    count = 0
    for pair in sequence:
        newlst[n - 1 - count] = Lst[sequence[count][1]]
        count += 1
    search(n - 1, current, result, slots, Lst)
    return result

def search(n, current, result, slots, Lst):
    allmodule = Lst[n]
    for modules in allmodule:
        can = True
        if int(modules[1].split()[0]) != -1:
            for i in range(1, 7):
                if modules[i * 2 - 1] != None:
                    time = modules[i * 2 - 1].split()
                    start = int(time[0])
                    end = int(time[1])
                    if int(modules[i * 2]) == 0:
                        for j in range(start, end):
                            if(slots[j] == False):
                                can = False
                                break
                            if(slots[j + 72] == False):
                                can = False
                                break
                    elif int(modules[i * 2]) == 1:
                        for j in range(start, end):
                            if(slots[j] == False):
                                can = False
                                break
                    else:
                        for j in range(start, end):
                            if(slots[j + 72] == False):
                                can = False
                                break
                    if not can:
                        break

                else:
                    break

        if can:
            if n == 0:
                current.append(modules[0])
                result.append(list(current))
                current.pop()
            else:
                if int(modules[1].split()[0]) != -1:
                    for i in range(1, 7):
                        if modules[i * 2 - 1] != None:
                            time = modules[i * 2 - 1].split()
                            start = int(time[0])
                            end = int(time[1])
                            if int(modules[i * 2]) == 0:
                                for j in range(start, end):
                                    slots[j] = False
                                    slots[j + 72] = False
                            elif int(modules[i * 2]) == 1:
                                for j in range(start, end):
                                    slots[j] = False
                            else:
                                for j in range(start, end):
                                    slots[j + 72] = False
                current.append(modules[0])
                search(n - 1, current, result, slots, Lst)
                current.pop()
                for i in range(1, 7):
                    if modules[i * 2 - 1] != None:
                        time = modules[i * 2 - 1].split()
                        start = int(time[0])
                        end = int(time[1])
                        if int(modules[i * 2]) == 0:
                            for j in range(start, end):
                                slots[j] = True
                                slots[j + 72] = True
                        elif int(modules[i * 2]) == 1:
                            for j in range(start, end):
                                slots[j] = True
                        else:
                            for j in range(start, end):
                                slots[j + 72] = True

#courses = ["cz1006", "cz1007", "cz1012","cz1011", "cz0001", "cz3001"]
#answer = allCombination(courses)
#print(len(answer))
#print(answer)