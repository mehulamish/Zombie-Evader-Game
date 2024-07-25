import mysql.connector as mc
conn=mc.connect(host='localhost',user='root',password='*********',database='student')  # as per your device settings
def fun():
    mycursor=conn.cursor()
    mycursor.execute('create database hospital')
def maketable():
    mycursor=conn.cursor()
    sql="create table if not exists hospital(hospital_id int primary key,Hospital_name varchar(25),Bed_count int,city varchar(25) check(city in(\"delhi\",\"Mumbai\",\"kolkata\",\"chennai\")), departments int)"
    mycursor.execute(sql)
    conn.commit()
def insertuser():
    mycursor=conn.cursor():
    hosid=int(input("Enter hospital id"))    
    hosname=input("Enter hospital name")
    bedcount=int(input("Enter number of beds"))
    city=input("Enter City")
    hosdept=int(input("Enter number of departments"))
    sql='insert into hospital values(%s,%s,%s,%s)'
    val=(hosid,hosname,bedcount,city,hosdept)
    mysql.execute(sql,val)
    conn.commit()
    
def insertmultiple():
    mycursor=conn.cursor()
    l=[]
    a=int(input("enter the number of records"))
    for i in range(a):
        hosid=int(input("Enter hospital id"))    
        hosname=input("Enter hospital name")
        bedcount=int(input("Enter number of beds"))
        city=input("Enter City")
        hosdept=int(input("Enter number of departments")
        val=(hosid,hosname,bedcount,city,hosdept)
        l.append(val)
    sql="insert into hospital values(%s,%s,%s,%s,%s)"
    mycursor.executemany(sql,l)
    conn.commit()
insertmultiple()
    
