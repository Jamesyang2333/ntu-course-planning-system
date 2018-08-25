from coursearrangement import ntuCourse


list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2 = ['0','1','2','3','4','5','6','7','8','9']

def allcourses():
    for first in list1:
        for second in list1:
            for third in list2:
                for fourth in list2:
                    for fifth in list2:
                        for sixth in list2:
                            courseName = first+second+third+fourth+fifth+sixth
                            if(courseName<="aj3990"):
                                continue
                            else:
                                ntuCourse.save(courseName)
                                print(courseName)

allcourses()


