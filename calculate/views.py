# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views import generic
from django.views.decorators import csrf
import os, sys
from coursearrangement import solve
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from calculate.models import Myindex,Expectedindex,CourseCode,IndexNumber,Applicant
from calculate.forms import MyIndexForm,ExpectedIndexForm,ContactForm, SwapForm
from coursearrangement.display import writecontent
from django.core.mail import send_mail, BadHeaderError
import random
from calculate.match import match



def mainpage(request):
    return render(request,'home.html')

def contact(request):
    if request.method == 'GET':
        return render(request,"contact.html",{})
    else:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail("course arrangement web","from: "+email+"\n"+"name: "+name+"\n message:"+ message,"chentaoyu802x@gmail.com",['chentaoyu802x@gmail.com'])
        return HttpResponseRedirect('/contact/success/')


def successView(request):
    return render(request,'success.html',{})


def timetable(request):
    return render(request,'timetable.html')


def search(request):
    request.encoding = 'utf-8'
    content = {}
    list = []

    if request.method == "POST":
        list = request.POST.getlist('text')
        names = request.POST.getlist('checkbox')

        j = 0
        n = len(list)
        for i in range(n):
            if list[i-j] == '':
                list.remove(list[i-j])
                j=j+1

        list1=[]
        for i in range(len(list)):
            list[i] = list[i].lower()
            if(list[i] not in list1):
                list1.append(list[i])
        list = list1
        if(len(list)==0):
            return timetable(request)


        for element in names:
            name = 'check'+element
            content[name] = "checked="

        n = len(names)
        for i in range(n):
            names[i] = int(names[i])

        print(names)


        name = 'a'
        i=0
        for element in list:
            content[name] = list[i]
            name = chr(ord(name)+1)
            i = i+1





        list.reverse()
        answer = solve.allCombination(list,names)
        if answer:
            n = len(answer)
            if n==1:
                content['outcome'] = str(n) + " result is available!"
            else:
                content['outcome'] = str(n) + " results are available!"
            if n>10:
                content['suggestion'] = "We’ve curated 10 timetables for you. More index combinations are available at the bottom."
                base = random.randint(0, n)
                dif = n//10
                i=0
                while(i<10):
                    writecontent(i+1,answer[(base+i*dif)%n],content,list)
                    i = i+1
            else:
                i = 0
                while(i<n):
                    writecontent(i+1,answer[i],content,list)
                    i = i+1
            content['result'] = str(answer)
        else:
            content["outcome"] = "Opps! No result!"
            content["suggestion"] = "We suggest you to unclick some time slots or change the courses you select."
            content['result'] = ""

    return render(request, 'timetablelist.html',content)

def temp(request):

    if request.method == 'POST':
        form = SwapForm(request.POST)
        if form.is_valid():
            form.save()

        name = request.POST['name']
        code = request.POST['code']
        current = request.POST['current']
        expected = request.POST['expected']
        email = request.POST['email']
        # id = request.POST['id']

        result = match(code,current,expected,email)

        # for keys in result:
        #     print("{}: {}".format(keys,result[keys]))

        if result["match"]:
            #send mail to both of the ppl
            # send_mail(subject, message, from_email, recipient_list)
            send_mail("Course Swapping MATCH!",message(name,code,current,expected,result["name"],result["email"]),"ntucourseplanner@gmail.com",[email,])
            send_mail("Course Swapping MATCH!",message(result["name"],code,expected,current,name,email),"ntucourseplanner@gmail.com",[result["email"],])

            #delte ppl from both of the database
            p1 = Applicant.objects.get(name=name,code=code,current=current,expected=expected,email=email)
            p1.delete()
            p2 = Applicant.objects.get(id=result["id"])
            p2.delete()

            return redirect("match")

        else:
            return redirect("nomatch")

    else:
        form = SwapForm()

    return render(request,'comming.html',{'form':form})

def message(name,code,current,expected,match_name,match_email):
    return ("Congratulations {}!\nWe have found you a match for {}, to swap {} with {}."
    "\nThe persons name is {}, and you can contact him or her @: {}."
    "\nYour request will now be deleted from our database, "
    "should this swap not work out feel free to submit another request.\nCheers! :)"
    ).format(name,code,current,expected,match_name,match_email)

def matchsuccess(request):
    if request.method == 'POST':
        form = SwapForm(request.POST)
        if form.is_valid():
            form.save()

        name = request.POST['name']
        code = request.POST['code']
        current = request.POST['current']
        expected = request.POST['expected']
        email = request.POST['email']
        # id = request.POST['id']

        result = match(code,current,expected,email)

        # for keys in result:
        #     print("{}: {}".format(keys,result[keys]))

        if result["match"]:
            #send mail to both of the ppl
            # send_mail(subject, message, from_email, recipient_list)
            send_mail("Course Swapping MATCH!",message(name,code,current,expected,result["name"],result["email"]),"ntucourseplanner@gmail.com",[email,])
            send_mail("Course Swapping MATCH!",message(result["name"],code,expected,current,name,email),"ntucourseplanner@gmail.com",[result["email"],])

            #delte ppl from both of the database
            p1 = Applicant.objects.get(name=name,code=code,current=current,expected=expected,email=email)
            p1.delete()
            p2 = Applicant.objects.get(id=result["id"])
            p2.delete()

            return redirect("match")

        else:
            return redirect("nomatch")

    else:
        form = SwapForm()

    return render(request,'match.html',{'form':form})

def nomatch(request):
    if request.method == 'POST':
        form = SwapForm(request.POST)
        if form.is_valid():
            form.save()

        name = request.POST['name']
        code = request.POST['code']
        current = request.POST['current']
        expected = request.POST['expected']
        email = request.POST['email']
        # id = request.POST['id']

        result = match(code,current,expected,email)

        # for keys in result:
        #     print("{}: {}".format(keys,result[keys]))

        if result["match"]:
            #send mail to both of the ppl
            # send_mail(subject, message, from_email, recipient_list)
            send_mail("Course Swapping MATCH!",message(name,code,current,expected,result["name"],result["email"]),"ntucourseplanner@gmail.com",[email,])
            send_mail("Course Swapping MATCH!",message(result["name"],code,expected,current,name,email),"ntucourseplanner@gmail.com",[result["email"],])

            #delte ppl from both of the database
            p1 = Applicant.objects.get(name=name,code=code,current=current,expected=expected,email=email)
            p1.delete()
            p2 = Applicant.objects.get(id=result["id"])
            p2.delete()

            return redirect("match")

        else:
            return redirect("nomatch")

    else:
        form = SwapForm()

    return render(request,'nomatch.html',{'form':form})

def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')





def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'login.html', {},)




@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/home/')

from calculate.forms import UserForm, UserProfileForm
def register(request):
# Like before, get the request's context.
# A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
# Attempt to grab information from the raw form information. # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
        # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
        # Now sort out the UserProfile instance.
        # Since we need to set the user attribute ourselves, we set commit=False.
        # This delays saving the model until we're ready to avoid integrity problem
            profile = profile_form.save(commit=False)
            profile.user = user
        # Did the user provide a profile picture?
        # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        # Invalid form or forms - mistakes or something else? # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

            # Not a HTTP POST, so we render our form using two ModelForm instances. # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        # Render the template depending on the context.
    return render(request,'register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def get_coursecode_list(max_results=0, starts_with=''):
    coursecode_list = []
    if starts_with:
        coursecode_list = CourseCode.objects.filter(name__startswith=starts_with)
    else:
        coursecode_list = CourseCode.objects.all()

    if max_results > 0:
        if (len(coursecode_list) > max_results):
            coursecode_list = coursecode_list[:max_results]

    for coursecode in coursecode_list:
        coursecode.url = encode_url(coursecode.code)

    return coursecode_list


def forum(request):

    top_coursecode_list = CourseCode.objects.order_by('-views')[:10]

    for coursecode in top_coursecode_list:
        coursecode.url = encode_url(coursecode.code)

    context_dict = {'coursecodes': top_coursecode_list}

    coursecode_list = get_coursecode_list()
    context_dict['coursecode_list'] = coursecode_list

    # Render and return the rendered response back to the user.
    return render(request,'forum.html', context_dict)


def coursecode(request,coursecode1_name_url):
    top_coursecode_list = CourseCode.objects.order_by('-views')[:10]

    for coursecode in top_coursecode_list:
        coursecode.url = encode_url(coursecode.code)

    context_dict = {'coursecodes': top_coursecode_list}

    coursecode_list = get_coursecode_list()
    context_dict['coursecode_list'] = coursecode_list

    # Render and return the rendered response back to the user.


    coursecode1_name = decode_url(coursecode1_name_url)
    context_dict = {'coursecode1_name':coursecode1_name,'coursecode1_name_url':coursecode1_name_url}

    try:
        coursecode1 = CourseCode.objects.get(code=coursecode1_name)
        context_dict['coursecode1'] = coursecode1
        indexnumbers = IndexNumber.objects.filter(course=coursecode1)
        for indexnumber in indexnumbers:
            print(indexnumber.index)
        print(indexnumbers)
        context_dict['indexnumbers'] = indexnumbers
    except CourseCode.DoesNotExist:
        pass

    return  render(request,'coursecode.html', context_dict)


def myindex(request, myindex_name_url):
    myindex_name = decode_url(myindex_name_url)
    context_dict = {'myindex_name': myindex_name, 'myindex_name_url': myindex_name_url}


    try:
        myindex = Myindex.objects.get(index=myindex_name)
        context_dict['myindex'] = myindex
        Expectedindexes = Expectedindex.objects.filter(myindex=myindex).order_by('-views')
        context_dict['expectedindexes'] = Expectedindexes
    except Myindex.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request,'myindex.html', context_dict)


def add_myindex(request):
    context_dict = {}

    # A HTTP POST?
    if request.method == 'POST':
        form = MyIndexForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new myindex to the database.
            form.save(commit=True)
            return HttpResponseRedirect('/forum/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = MyIndexForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    context_dict['myindex_form'] = form
    return render(request,'add_myindex.html', context_dict)


def add_expectedindex(request, myindex_name_url):

    context_dict = {}

    myindex_name = decode_url(myindex_name_url)
    context_dict['myindex_name'] = myindex_name
    context_dict['myindex_name_url'] = myindex_name_url
    x = Myindex.objects.get(index=myindex_name)
    if request.method == 'POST':
        form = ExpectedIndexForm(request.POST)
        if form.is_valid():
            ex = form.save()
            ex.views = 0
            ex.myindex.add(x)
            ex.save()
            path = '/forum/'+myindex_name_url
            return HttpResponseRedirect(path)
        else:
            print(form.errors)
    else:
        form = ExpectedIndexForm()
    context_dict['form']=form
    return render(request,'add_expectedindex.html',context_dict)
