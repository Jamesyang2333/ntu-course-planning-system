a = """MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: course arrangement web
From: chentaoyu802x@gmail.com
To: chentaoyu802x@gmail.com
Date: Thu, 07 Jun 2018 07:36:55 -0000
Message-ID: 
 <152835701577.4316.13780263717447119874@chentaoyudeMacBook-Pro.local>

from: chentaoyu802x@gmail.com
name: Chen Taoyu
 message:test test
-------------------------------------------------------------------------------
[07/Jun/2018 07:36:55] "POST /contact/ HTTP/1.1" 302 0
[07/Jun/2018 07:36:55] "GET /contact/success/ HTTP/1.1" 200 435
[07/Jun/2018 07:37:01] "GET /home/ HTTP/1.1" 200 5407
[07/Jun/2018 07:37:13] "GET /contact/ HTTP/1.1" 200 6324
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: course arrangement web
From: chentaoyu802x@gmail.com
To: chentaoyu802x@gmail.com
Date: Thu, 07 Jun 2018 07:37:18 -0000
Message-ID: 
 <152835703869.4316.7420743718702913797@chentaoyudeMacBook-Pro.local>

from: chentaoyu802x@gmail.com
name: Chen Taoyu
 message:aaaa
-------------------------------------------------------------------------------
[07/Jun/2018 07:37:18] "POST /contact/ HTTP/1.1" 302 0
[07/Jun/2018 07:37:18] "GET /contact/success/ HTTP/1.1" 200 435
[07/Jun/2018 07:37:25] "GET /home/ HTTP/1.1" 200 5407
[07/Jun/2018 07:37:41] "GET /contact/ HTTP/1.1" 200 6324
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: course arrangement web
From: chentaoyu802x@gmail.com
To: chentaoyu802x@gmail.com
Date: Thu, 07 Jun 2018 07:37:45 -0000
Message-ID: 
 <152835706530.4316.9881244546728326258@chentaoyudeMacBook-Pro.local>

from: chentaoyu802x@gmail.com
name: Chen Taoyu
 message:aaaaa
-------------------------------------------------------------------------------
[07/Jun/2018 07:37:45] "POST /contact/ HTTP/1.1" 302 0
[07/Jun/2018 07:37:45] "GET /contact/success/ HTTP/1.1" 200 436
[07/Jun/2018 07:37:49] "GET /home/ HTTP/1.1" 200 5407
[07/Jun/2018 07:37:55] "GET /contact/ HTTP/1.1" 200 6324
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: course arrangement web
From: chentaoyu802x@gmail.com
To: chentaoyu802x@gmail.com
Date: Thu, 07 Jun 2018 07:38:03 -0000
Message-ID: 
 <152835708318.4316.607611077480885846@chentaoyudeMacBook-Pro.local>

from: chentaoyu802x@gmail.com
name: Chen Taoyu
 message:fff
-------------------------------------------------------------------------------
[07/Jun/2018 07:38:03] "POST /contact/ HTTP/1.1" 302 0
[07/Jun/2018 07:38:03] "GET /contact/success/ HTTP/1.1" 200 437
[07/Jun/2018 07:38:07] "GET /home/ HTTP/1.1" 200 5407

"""
email = []
while a:
    for i in range(len(a)):
        if a[i:i+7]=="Subject":
            first = i
        elif a[i:i+2]=="--":
            last = i
            break
    email.append(a[first:last])
    a = a[last:]
    for i in range(len(a)):
        if a[i]!="-":
            new = i
            break
    a = a[new+1:]
for element in email:
    print(element)