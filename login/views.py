from urllib import request
from django.shortcuts import render
import mysql.connector as sql
email=""
password=""
usert=""
# Create your views here.
def loginaction(request):
     global email,password,usert
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="shriya123", database="hospital")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
             
            if key== "email":
                email=value  
            if key== "password":
                password=value
            if key=="Types of users":  
                usert=value
            c="select * from users where email='{}' and password='{}' and usert='{}'".format(email,password,usert)
            cursor.execute(c)
            t=tuple(cursor.fetchall())
            if t==():
                return(request,'error.html')
            else:
                return(request,'welcome.html')
        return render(request,'login_page.html') 