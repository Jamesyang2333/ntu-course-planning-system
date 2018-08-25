from coursearrangement import solve
from coursearrangement import ntuCourse
from pprint import pprint
courses = ["bu8201", "ee2003", "ee2004", "ee2007", "ee2008", "hy0001", "mh8300"]
answer = solve.allCombination(courses,[])
print("all answers:" + str(len(answer)))
pprint(answer[:10])