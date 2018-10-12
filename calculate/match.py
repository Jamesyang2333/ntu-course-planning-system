from calculate.models import Applicant

def match(code,current,expected,email):
    ans = Applicant.objects.exclude(email=email
    ).filter(code=code,current=expected,expected=current
    ).order_by('date')

    result = {"match":False,"name":"","email":"","id":0}

    if ans.count() >0:
        result["match"] = True
        result["name"] = ans[0].name
        result["email"] = ans[0].email
        result["id"] = ans[0].id
        return result
    else:
        return result
