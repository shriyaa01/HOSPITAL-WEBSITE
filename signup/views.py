from django.shortcuts import render
import mysql.connector as sql
fn=""
ln=""
un=""
email=""
gender=""
password=""
address=""
usert=""

def signaction(request):
    global fn,ln,un,email,gender,password,address,usert
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="shriya123", database="hospital")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key== "fname":
                fn=value 
            if key== "lname":
                ln=value  
            if key== "username":
                un=value  
            if key== "email":
                email=value  
            if key== "GENDER":
                gender=value
            if key== "password":
                password=value
            if key== "add":
                address=value 
            if key=="Types of users":  
                usert=value
            c="insert into  users Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,un,email,gender,password,address,usert)
            cursor.execute(c)
            m.commit()
        return render(request,'signup_page.html')         