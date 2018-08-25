from coursearrangement import solve
from pprint import pprint
courses = ["cz2001","cz2002","cz2005","cz2006","cz2007"]
answer = solve.allCombination(courses)
print(len(answer))
pprint(answer)