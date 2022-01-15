import mysql.connector as ms
import csv
import os
def add(db):
    country=input("Enter the country: ")
    cid=input("Enter the country ID: ")
    capital=input("Enter the capital: ") 
    PM=input("Enter name of the PM: ")
    pres=input("Enter name of the president: ")
    popu=int(input("Enter population: "))
    conti=input("Enter continent from (Asia,Euro,NA,SA,Aus,Africa): ")
    lang=input("Most common language: ")
    curr=input("Currency: ")
    cur=db.cursor() 
    sql="insert into nations values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
    val=(country,cid,capital,PM,pres,popu,conti,lang,curr) 
    cur.execute(sql,val) 
    db.commit()
    print("\t\t\t░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄")
    print("\t\t\t░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄")
    print("\t\t\t░░░░█░░░░░░░░░░░░░░░░░░░░░░█")
    print("\t\t\t░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█")
    print("\t\t\t░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█")
    print("\t\t\t█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█")
    print("\t\t\t█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█")
    print("\t\t\t░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█")
    print("\t\t\t░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█")
    print("\t\t\t░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█")
    print("\t\t\t░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█")
    print("\t\t\t░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█")
    print("\t\t\t░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█")
    print("\t\t\t░░▐▌░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█")
    print("\t\t\t░░░█▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█")
    print("\t\t\t░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀")
    print("\t\t\t░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄")
    print("\t\t\t░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█")
    print("\t\t\t░░█░░▌░█░░█░░█░░░█░░█░░█")
    print("\t\t\t░░█░░▀▀░░██░░█░░░█░░█░░█")
    print("\t\t\t░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█")
    print("\t\t\t░░░░░░░░░░█░░░░▄░░▄██▄▄▀")
    print("\t\t\t░░░░░░░░░░█░░░░▄░░████")
    print("\t\t\t░░░░░░░░░░█▄░░▄▄▄░░▄█")
    print("\t\t\t░░░░░░░░░░░█▀▀░▄░▀▀█")
    print("\t\t\t░░░░░░░░░░░█░░░█░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█▄▄▄▐▄▄▄█")
    print("\t\t\t░░░░░░░▄▄▄▄▀▄▄▀█▀▄▄▀▄▄▄▄")
    print("\t\t\t░░░░░▄▀▄░▄░▄░░░█░░░▄░▄░▄▀▄")
    print("\t\t\t░░░░░█▄▄▄▄▄▄▄▄▄▀▄▄▄▄▄▄▄▄▄█")
    f=open("Countries","w",newline="")
    wr=csv.writer(f)
    wr.writerow(["country","capital","PM","pres","popu","conti","lang","curr","cid"])
    wr.writerows([country,capital,PM,pres,popu,conti,lang,curr,cid])
    f.close()

    return db

def showall(db):
    cur=db.cursor() 
    cur.execute("select * from nations")
    p=cur.fetchall()
    #
    pp=[]
    for i in p:
        qq=list(i)
        pp+=[qq]
        
    for i in pp:
        print("Country  ⣿",4*" ","Capital of the Country  ⣿",4*" ","Prime Minister  ⣿",4*" ","President        ⣿",3*" ","Population",)
        break
    for i in pp:    
        print(i[0],((len("country")-len(i[0])))*" ","⣿",4*" ",i[1],((len("capital of the country")-len(i[1])))*" ","⣿",4*" ",i[2],((len("Prime minister")-len(i[2])))*" ","⣿",4*" ",i[3],((len("president      ")-len(i[3])))*" ","⣿",3*" ",i[4])
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")
    

    for i in pp:
        print("Continent   ⣿",4*" ","Language  ⣿",4*" ","Currency  ⣿",4*" ","Cid")
        break
    for i in pp:    
        print(i[5],((len("continent ")-len(i[5])))*" ","⣿",4*" ",i[6],((len("Language")-len(i[6])))*" ","⣿",4*" ",i[7],((len("currency")-len(i[7])))*" ","⣿",+4*" ",i[8])
    print("\n")


def searchc(db): 
    cur=db.cursor() 
    co=input("Enter the Country Id to search: ") 
    sql="select * from nations where Country_Id=%s" 
    val=(co,)
    cur.execute(sql,val) 
    p=cur.fetchall()
    ##
    pp=[]
    
    for i in p:
        qq=list(i)
        pp+=[qq]
        
    for i in pp:
        print("Country  ⣿",4*" ","Capital of the Country  ⣿",4*" ","Prime Minister  ⣿",4*" ","President        ⣿",3*" ","Population",)
        break
    for i in pp:    
        print(i[0],((len("country")-len(i[0])))*" ","⣿",4*" ",i[1],((len("capital of the country")-len(i[1])))*" ","⣿",4*" ",i[2],((len("Prime minister")-len(i[2])))*" ","⣿",4*" ",i[3],((len("president      ")-len(i[3])))*" ","⣿",3*" ",i[4])
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")
    

    for i in pp:
        print("continent   ⣿",4*" ","Language  ⣿",4*" ","currency  ⣿",4*" ","cid")
        break
    for i in pp:    
        print(i[5],((len("Continent ")-len(i[5])))*" ","⣿",4*" ",i[6],((len("Language")-len(i[6])))*" ","⣿",4*" ",i[7],((len("currency")-len(i[7])))*" ","⣿",+4*" ",i[8])
    print("\n")


def modify(db):
    cur=db.cursor() 
    co=input("Enter the country to modify: ")
    u=str(input("What to Modify? Cap for Capital, Enter P for PM, Pres for President, popu for population,conti for continent, lang for common language,curr for currency: "))
    if u=='P':
        n=str(input("Enter New PM: "))
        sql="update nations set PM=%s where country=%s"
    elif u=='Pres':
        n=str(input("Enter new President: "))
        sql="update nations set President=%s where country=%s"
    elif u=='Cap':
        n=str(input("Enter new Capital: "))
        sql="update nations set Capital=%s where country=%s"
    elif u=='popu':
        n=int(input("Enter new Population: "))
        sql="update nations set Population=%s where country=%s"
    elif u=='conti':
        n=str(input("Enter new Continent: "))
        sql="update nations set Continent=%s where country=%s"
    elif u=='lang':
        n=str(input("Enter new common language: "))
        sql="update nations set language=%s where country=%s"
    elif u=='curr':
        n=str(input("Enter new currency: "))
        sql="update nations set currency=%s where country=%s" 
    val=(n,co) 
    cur.execute(sql,val) 
    db.commit() 
    sql="select * from nations where country=%s" 
    val=(co,) 
    cur.execute(sql,val) 
    p=cur.fetchall()
    ###
    pp=[]

    for i in p:
        qq=list(i)
        pp+=[qq]
        
    for i in pp:
        print("Country  ⣿",4*" ","Capital of the Country  ⣿",4*" ","Prime Minister  ⣿",4*" ","President        ⣿",3*" ","Population",)
        break
    for i in pp:    
        print(i[0],((len("country")-len(i[0])))*" ","⣿",4*" ",i[1],((len("capital of the country")-len(i[1])))*" ","⣿",4*" ",i[2],((len("Prime minister")-len(i[2])))*" ","⣿",4*" ",i[3],((len("president      ")-len(i[3])))*" ","⣿",3*" ",i[4])
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")
    

    for i in pp:
        print("continent   ⣿",4*" ","Language  ⣿",4*" ","currency  ⣿",4*" ","cid")
        break
    for i in pp:    
        print(i[5],((len("Continent ")-len(i[5])))*" ","⣿",4*" ",i[6],((len("Language")-len(i[6])))*" ","⣿",4*" ",i[7],((len("Currency")-len(i[7])))*" ","⣿",+4*" ",i[8])
    print("\n")
def delete(db): 
    cur=db.cursor() 
    co=input("Enter the country to be deleted: ") 
    sql="delete from nations where country=%s" 
    val=(co,) 
    cur.execute(sql,val)
    db.commit()
        
    print("\t\t\t╔══╦╗╔╦══╦═╦╦╦╗ ╔═╦╦═╦╦╗")
    print("\t\t\t╚╗╔╣╚╝║╔╗║║║║╔╝ ╚╗║║║║║║")
    print("\t\t\t ║║║╔╗║╠╣║║║║╚╗ ╔╩╗║║║║║")
    print("\t\t\t ╚╝╚╝╚╩╝╚╩╩═╩╩╝ ╚══╩═╩═╝")
        
import datetime

def takevisa(): 
    db=ms.connect(host="localhost", user="root",passwd="sharath",db="VISA")
    now=datetime.datetime.now()
    if now.strftime("%A")=='Friday':
        print("\n")
        print("\t\t\tServers are down on Sunday, try tommorow")
        print("\t\t\t░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░")
        print("\t\t\t░░░░░░▄▄████▀▀▀▀▀░░░░░░▀▀█▄▄░░░░░░░░░")
        print("\t\t\t░░░▄██▀▀░░░░░░░░░░░░░░░░░░▀██▄░░░░░░░")
        print("\t\t\t░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░░")
        print("\t\t\t░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░░")
        print("\t\t\t██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░░")
        print("\t\t\t██░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░▀█░░░")
        print("\t\t\t█░░░░░░░░░░░░░░░░░░░░░░░░░░▀██▄░░██░░")
        print("\t\t\t█░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░█▄░")
        print("\t\t\t█░░░░░▀▀▀█░░░░░░░░░░░░░░░░░░░░░░░░██░")
        print("\t\t\t█░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄█████▀░█▄")
        print("\t\t\t█░░░░░░░░░░▄▄▄▄▄██████▀▀▀▀▀▀░░░░░░░██")
        print("\t\t\t█░░░░▄█████▀▀▀▀▀░▄▄▄████░░░░░░░░░░░██")
        print("\t\t\t██░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░██")
        print("\t\t\t▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀")
        print("\t\t\t░▀█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░")
        print("\t\t\t░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░")
        print("\t\t\t░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░")
        print("\t\t\t░░░░▀██▄░░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░")
        print("\t\t\t░░░░░░▀██▄░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░")
        print("\t\t\t░░░░░░░░░▀██▄░░░░░░░░░░░▄▄█▀░░░░░░░░░")
        print("\t\t\t░░░░░░░░░░░░▀██▄▄▄▄▄▄▄▄█▀░░░░░░░░░░░░")
        print("\t\t\t░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
        print("\t\t\t░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
        print("\t\t\t░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
        print("\t\t\t░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
        print("\t\t\t░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
        print("\t\t\t░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░")
        print("\n")

        
        main()
    else:
        pass
    ocountry=input("Enter the country whose VISA you are seeking: ")
    cidd=int(input("Enter the country ID: "))
    print("Types of visa: ")
    print("|Travel|Work|Business")
    print("|Student|Refugee|Resident")
    typ=input("Enter type of visa: ")
    ni=int(input("Enter new Date of birth: "))
    nr=int(input('Enter new month of birth(1 for January and so on)'))
    nh=int(input('Enter new year of birth'))
    dob=datetime.date(nh,nr,ni)
    cur=db.cursor() 
    sql="select * from nations where country=%s and Country_Id=%s"
    #you can do something
    val=(ocountry,cidd) 
    cur.execute(sql,val) 
    p=cur.fetchall()
    if p: 
        print("VISA to be Taken",p[0][0]) 
        resp=input("Enter y for yes/n for no to confirm: ")
        if resp=="n": 
            return
        sqlkll="select * from seeker"
        cur.execute(sqlkll,)
        p=cur.fetchall()
        ####
        pp=[]
        kk=[]
        la=[]
        for i in p:
            qq=list(i)
            pp+=[qq]
        for j in range(len(pp)):
            la+=[pp[j][8]]
    
        for w in range(101,100000000000000):
            if w in la:
                pass
            else:
                print(w)
                aa=w
                break
        if resp=="y":
            name=str(input("Enter full name: "))
            country=input("Enter the nationality: ")
            Gender=input("Enter your Gender: ")
            cs=input("Enter civil status: ")
            print("Your VISA entry/ID is: ",aa)  
             
            print("A VISA has been sanctioned")
            if typ=='Resident':
                sqlll="update nations set population=population+1 where country=%s"
                valll=(ocountry,) 
                cur.execute(sqlll,valll)
                db.commit()
                sqllll="select * from nations where country=%s"
                vallll=(ocountry,)
                cur.execute(sqllll,vallll)
                p=cur.fetchall()
                pp=[]
                for i in p:
                    qq=list(i)
                pp+=[qq]                
                for j in range(len(pp)):
                    if pp[j][0]==ocountry:
                        ii=pp[j][4]
                print("New Population of country is(including you now): ",ii)
            sqll="insert into seeker values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            vall=(name,ocountry,country,cidd,dob,Gender,cs,typ,aa)
            cur.execute(sqll,vall)
            db.commit()
            
            q=input("Do you want to give Feedback (if yes press y if no press n): ")
            if q=="y":
                feedback=input("Please give your Feedback: ")
                print("Thank you for your Feedback (^_^) ")
                sqlq="insert into feedbacks values(%s,%s,%s)" 
                valq=(name,country,feedback) 
                cur.execute(sqlq,valq) 
                db.commit()
            else:
                pass
                         
        else:
            print("You are in that same country stupid")
    else:
        
        print("The country does not exits")

    print("\t\t\t ╔══╦╗╔╦══╦═╦╦╦╗ ╔═╦╦═╦╦╗")
    print("\t\t\t ╚╗╔╣╚╝║╔╗║║║║╔╝ ╚╗║║║║║║")
    print("\t\t\t  ║║║╔╗║╠╣║║║║╚╗ ╔╩╗║║║║║")
    print("\t\t\t  ╚╝╚╝╚╩╝╚╩╩═╩╩╝ ╚══╩═╩═╝")
    print("\n")
    print("\t\t\t░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄")
    print("\t\t\t░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄")
    print("\t\t\t░░░░█░░░░░░░░░░░░░░░░░░░░░░█")
    print("\t\t\t░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█")
    print("\t\t\t░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█")
    print("\t\t\t█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█")
    print("\t\t\t█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█")
    print("\t\t\t░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█")
    print("\t\t\t░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█")
    print("\t\t\t░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█")
    print("\t\t\t░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█")
    print("\t\t\t░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█")
    print("\t\t\t░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█")
    print("\t\t\t░░▐▌░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█")
    print("\t\t\t░░░█▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█")
    print("\t\t\t░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀")
    print("\t\t\t░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄")
    print("\t\t\t░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█")
    print("\t\t\t░░█░░▌░█░░█░░█░░░█░░█░░█")
    print("\t\t\t░░█░░▀▀░░██░░█░░░█░░█░░█")
    print("\t\t\t░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█")
    print("\t\t\t░░░░░░░░░░█░░░░▄░░▄██▄▄▀")
    print("\t\t\t░░░░░░░░░░█░░░░▄░░████")
    print("\t\t\t░░░░░░░░░░█▄░░▄▄▄░░▄█")
    print("\t\t\t░░░░░░░░░░░█▀▀░▄░▀▀█")
    print("\t\t\t░░░░░░░░░░░█░░░█░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█░░░▐░░░█")
    print("\t\t\t░░░░░░░░░░░█▄▄▄▐▄▄▄█")
    print("\t\t\t░░░░░░░▄▄▄▄▀▄▄▀█▀▄▄▀▄▄▄▄")
    print("\t\t\t░░░░░▄▀▄░▄░▄░░░█░░░▄░▄░▄▀▄")
    print("\t\t\t░░░░░█▄▄▄▄▄▄▄▄▄▀▄▄▄▄▄▄▄▄▄█")

              

    
def show(db): 
    cur=db.cursor() 
    cur.execute("select seeker.Name,seeker.nationality,seeker.civilstatus,seeker.gender,seeker.dob,seeker.typeofvisa,seeker.visaid,nations.Country,nations.Country_Id,nations.capital,nations.PM,nations.President,nations.Population,nations.continent,nations.Language,nations.currency from seeker,nations where seeker.countryid=nations.Country_Id;") 
    p=cur.fetchall() 
    #print("Name Nationality civilstaus Gender dob TypeOfVisa VisaEntry country Countryid capital PM president population continent language currency")     
    #print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15])
    print("\n") 
    pp=[]
    for i in p:
        qq=list(i)
        pp+=[qq]
        
    for i in pp:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15])

        print("Name             ⣿",4*" ","Nationality    ⣿",4*" ","Civilstatus    ⣿",4*" ","Gender     ⣿",3*" ","Dateofbirth")
        break
    for i in pp:
        print
        print(i[0],((len("Name           ")-len(i[0])))*" ","⣿",4*" ",i[1],((len("nationality  ")-len(i[1])))*" ","⣿",4*" ",i[2],((len("civilstatus  ")-len(i[2])))*" ","⣿",4*" ",i[3],((len("gender   ")-len(i[3])))*" ","⣿",3*" ",i[4])
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")
    

    for i in pp: 
        print("Typeofvisa    ⣿",4*" ","Visa entry   ⣿",4*" ","Country    ⣿",4*" ","Country id        ⣿"," Capital")
        break
    for i in pp:    
        print(i[5],((len("typeofvisa  ")-len(i[5])))*" ","⣿",4*" ",i[6],((len("visa entry ")-len((str(i[6])))))*" ","⣿",4*" ",i[7],((len("country  ")-len(i[7])))*" ","⣿",+4*" ",i[8],((len("countryid ")-len((str(i[8])))))*" ",5*" ","⣿ ",i[9])
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")
    for i in pp: 
        print("Prime minister  ⣿",2*" ","President        ⣿",2*" ","population    ⣿",2*" ","continent       ⣿"," language   ⣿","currency")
        break
    for i in pp:    
        print(i[10],((len("Prime minister")-len(i[10])))*" ","⣿",2*" ",i[11],((len("President      ")-len((i[11]))))*" ","⣿",2*" ",i[12],((len("population  ")-len((str(i[12])))))*" ","⣿",2*" ",i[13],((len("continent ")-len((i[13]))))*" ",3*" ","⣿ ",i[14],((len("language ")-len((i[14]))))*" ","⣿",i[15])
    
    print("\n")
    

def cancelVISA(): 
    db=ms.connect(host="localhost", user="root",passwd="sharath",db="visa") 
    vid=int(input("Enter the VISA number: ")) 
    cur=db.cursor() 
    sqlk="select * from seeker where visaid=%s" 
    valk=(vid,) 
    cur.execute(sqlk,valk) 
    p=cur.fetchall()
    pp=[]
    for i in p:
        qq=list(i)
        pp+=[qq]
    for j in range(len(pp)):
        if vid==pp[j][8]:
            u=vid
            sqlkk="delete from seeker where visaid=%s" 
            valkk=(u,)
            cur.execute(sqlkk,valkk)
            db.commit()
            print("Ticket Number ",u," has been successfuly cancelled")
            break
        else:
            print("Following VISA number doesn't exist")
    print("\t\t ╔══╦╗╔╦══╦═╦╦╦╗ ╔═╦╦═╦╦╗")
    print("\t\t ╚╗╔╣╚╝║╔╗║║║║╔╝ ╚╗║║║║║║")
    print("\t\t  ║║║╔╗║╠╣║║║║╚╗ ╔╩╗║║║║║")
    print("\t\t  ╚╝╚╝╚╩╝╚╩╩═╩╩╝ ╚══╩═╩═╝")
    print("\n")

def modifyinfo(db):
    cur=db.cursor() 
    nn=input("Enter the Name of person whose VISA to be modified: ")
    v=input("Enter the VISAid")
    u=str(input("What to Modify? N for Name, Enter Coun for Country, Nati for Nationality, cid for Country_ID,Dob for DateOfBirth,gen for gender,CS for Civilstatus,type for typeofvisa: "))
    
    if u=='N':
        ne=str(input("Enter New Name: "))
        sql="update seeker set Name=%s where Name=%s and visaid=%s"
    elif u=='Coun':
        print('OK')
        ne=str(input("Enter new country(VISA): "))
        sql="update seeker set countryvisa=%s where Name=%s and visaid=%s"
    elif u=='Nati':
        ne=str(input("Enter your new Nationality: "))
        sql="update seeker set nationality=%s where Name=%s and visaid=%s"
    elif u=='cid':
        ne=int(input("Enter new CountryId: "))
        sql="update seeker set countryid=%s where Name=%s and visaid=%s"
    elif u=='Dob':
        ni=int(input("Enter new Date of birth: "))
        nr=int(input('Enter new month of birth(1 for January and so on): '))
        nh=int(input('Enter new year of birth: '))
        ne=datetime.date(nh,nr,ni)
        sql="update seeker set dob=%s where Name=%s and visaid=%s"
    elif u=='gen':
        ne=str(input("Enter new gender: "))
        sql="update seeker set gender=%s where Name=%s and visaid=%s"
    elif u=='CS':
        ne=str(input("Enter new civilstatus: "))
        sql="update seeker set civilstatus=%s where Name=%s and visaid=%s" 
    elif u=='type':
        ne=str(input("Enter new type of visa: "))
        sql="update seeker set typeofvisa=%s where Name=%s and visaid=%s" 
    val=(ne,nn,v) 
    cur.execute(sql,val) 
    db.commit() 
    sql="select * from seeker where Name=%s and visaid=%s" 
    val=(nn,v) 
    cur.execute(sql,val) 
    p=cur.fetchall()
    print("\n") 
    pp=[]
    for i in p:
        qq=list(i)
        pp+=[qq]
        
    for i in pp:
        print("Name     ⣿",4*" ","country   ⣿",4*" ","nationality    ⣿",4*" ","countryid     ⣿",3*" ","dateofbirth",)
        break
    for i in pp:    
        print(i[0],((len("Name  ")-len(i[0])))*" ","⣿",4*" ",i[1],((len("country ")-len(i[1])))*" ","⣿",4*" ",i[2],((len("nationality  ")-len(i[2])))*" ","⣿",4*" ",i[3],(((len("countryid   ")-len(str(i[3])))))*" ","⣿",3*" ",i[4])
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")
    

    for i in pp: 
        print("gender    ⣿",4*" ","civil status   ⣿",4*" ","type of visa    ⣿",4*" ","visaentry")
        break
    for i in pp:    
        print(i[5],((len("gender  ")-len(i[5])))*" ","⣿",4*" ",i[6],((len("civil status ")-len(i[6])))*" ","⣿",4*" ",i[7],((len("type of visa  ")-len(i[7])))*" ","⣿",+4*" ",i[8])
    print("\n")
def searchv(db): 
    cur=db.cursor() 
    nnn=str(input("Enter the Name of VISA seeker to search: ")) 
    sql="select * from seeker where Name=%s" 
    val=(nnn,)
    cur.execute(sql,val) 
    p=cur.fetchall()
    pp=[]
    for i in p:
        qq=list(i)
        pp+=[qq]
        
    for i in pp:
        print("Name      ⣿",4*" ","country   ⣿",4*" ","nationality    ⣿",4*" ","countryid     ⣿",3*" ","dateofbirth",)
        break
    for i in pp:    
        print(i[0],((len("Name    ")-len(i[0])))*" ","⣿",4*" ",i[1],((len("country ")-len(i[1])))*" ","⣿",4*" ",i[2],((len("nationality  ")-len(i[2])))*" ","⣿",4*" ",i[3],(((len("countryid   ")-len(str(i[3])))))*" ","⣿",3*" ",i[4])
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")
    

    for i in pp:
        print("gender    ⣿",4*" ","civil status   ⣿",4*" ","type of visa    ⣿",4*" ","visaentry")
        break
    for i in pp:    
        print(i[5],((len("gender  ")-len(i[5])))*" ","⣿",4*" ",i[6],((len("civil status ")-len(i[6])))*" ","⣿",4*" ",i[7],((len("type of visa  ")-len(i[7])))*" ","⣿",+4*" ",i[8])
    print("\n")
def VISAinfo(): 
    db=ms.connect(host="localhost", user="root",passwd="sharath",db="VISA") 
    flag=True 
    while flag: 
        print("\t\t\t\t -: M E N U for VISA Information :-") 
        print("\t\t \t1. Display all VISA's") 
        print("\t\t \t2. Search a VISA") 
        print("\t\t \t3. Modify a VISA(only member contact)") 
        print("\t\t \t4. Return to main menu")
        print('\n')
        option=int(input("Enter your option: ")) 
        if option==1: 
            show(db) 
        elif option==2: 
            searchv(db)
        elif option==3: 
            modifyinfo(db) 
        elif option==4: 
            flag=False 

def manage(): 
    db=ms.connect(host="localhost", user="root",passwd="sharath",db="visa") 
    flag=True 
    while flag: 
        print("\t\t⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛ -: M E N U in Manage a Country :- ⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛") 
        print("\t\t\t1. Add a country") 
        print("\t\t\t2. Display all") 
        print("\t\t\t3. Search a country") 
        print("\t\t\t4. Modify a country") 
        print("\t\t\t5. Delete a country") 
        print("\t\t\t6. Return to main menu")
        option=int(input("Enter your option: ")) 
        if option==1: 
            db=add(db) 
        elif option==2: 
            showall(db) 
        elif option==3: 
            searchc(db) 
        elif option==4: 
            modify(db) 
        elif option==5: 
            delete(db) 
        elif option==6:
            flag=False 
            continue         
def main():
    global aa
    aa=101
    print("\t\t\t\t     ░░░░░░░░░░░░░░░░░░░░░░░")
    print("\t\t\t\t     ╔╗╔╗╔╦══╣║╔══╦══╦╗╔╦══╗")
    print("\t\t\t\t     ║╚╝╚╝║║═╣║║╔═╣╔╗║╚╝║║═╣")
    print("\t\t\t\t     ╚╗╔╗╔╣║═╣╚╣╚═╣╚╝║║║║║═╣")
    print("\t\t\t\t      ╚╝╚╝╚══╩═╩══╩══╩╩╩╩══╝")
    print("\t\t\t\t     ░░░░░░░░░░░░░░░░░░░░░░░")
    print("\n")
    flag=True 
    while flag: 
        print("\t\t\t\t -: WELCOME TO VISA SERVICE :-  ") 
        print("\t\t\t1. Manage a country :- ") 
        print("\t\t\t2. Apply for VISA :- ") 
        print("\t\t\t3. Cancel a VISA :- ") 
        print("\t\t\t4. VISA information :- ")
        print("\t\t\t5. Press for Gift :- ")
        print("\t\t\t6. Press to Refer RAJ KUMAR PAL SIR NOTES (^_^) ")
        print("\t\t\t7. Exit (^-^) ")
        print("\n")
        option=int(input("Enter your option: ")) 
        if option==1: 
            manage()
            aa+=1
        elif option==2: 
            takevisa()
            aa+=1
        elif option==3: 
            cancelVISA()
            aa+=1
        elif option==4:
            VISAinfo()
            aa+=1


        elif option==5: 
            s=input("Enter a number: ")
            if s=="1":                
                print("\t\t\t\t██████████████████████████████")
                print("\t\t\t\t███████████╣╣╣╣╣╣╣╣███████████")
                print("\t\t\t\t█████████╣╣╣╣╣╣╣╣╣╣╣╣╣████████")
                print("\t\t\t\t███████╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣███████")
                print("\t\t\t\t██████╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣██████")
                print("\t\t\t\t█████╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█████")
                print("\t\t\t\t████╣╣██╣╣██╣╣╣╣╣╣██╣╣██╣╣████")
                print("\t\t\t\t███╣╣████████╣╣╣╣████████╣╣███")
                print("\t\t\t\t██╣╣╣████████╣╣╣╣████████╣╣╣██")
                print("\t\t\t\t██╣╣╣████████╣╣╣╣████████╣╣╣██")
                print("\t\t\t\t█╣╣╣╣██████╣╣╣╣╣╣██████╣╣╣╣██")
                print("\t\t\t\t█╣╣╣╣╣╣████╣╣╣╣╣╣╣╣████╣╣╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣╣╣╣██╣╣╣╣╣╣╣╣╣╣██╣╣╣╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣████████████████████╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣█")
                print("\t\t\t\t█╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣█")
                print("\t\t\t\t██╣╣╣██╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣██╣╣╣██")
                print("\t\t\t\t██╣╣╣╣██╣╣╣╣╣╣╣╣╣╣╣╣╣╣██╣╣╣╣██")
                print("\t\t\t\t███╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣███")
                print("\t\t\t\t███╣╣╣╣█╣╣╣╣╣╣╣╣╣╣╣╣█╣╣╣╣████")
                print("\t\t\t\t████╣╣╣╣╣██╣╣╣╣╣╣╣╣██╣╣╣╣╣████")
                print("\t\t\t\t█████╣╣╣╣╣╣██╣╣╣╣██╣╣╣╣╣╣█████")
                print("\t\t\t\t███████╣╣╣╣╣╣████╣╣╣╣╣╣███████")
                print("\t\t\t\t████████╣╣╣╣╣╣╣╣╣╣╣╣╣╣████████")
                print("\t\t\t\t███████████╣╣╣╣╣╣╣╣███████████")
                print("\t\t\t\t██████████████████████████████")

            if s=="2":
                
                
                
                print("\t\t\t\t´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`")
                print("\t\t\t\t´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`")
                print("\t\t\t\t´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´")
                print("\t\t\t\t´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´")
                print("\t\t\t\t´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´")
                print("\t\t\t\t´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´")
                print("\t\t\t\t´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´")
                print("\t\t\t\t¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶")
                print("\t\t\t\t¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶")
                print("\t\t\t\t´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´")
                print("\t\t\t\t´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´")
                print("\t\t\t\t´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´")
                print("\t\t\t\t´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´")
                print("\t\t\t\t´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´")
                print("\t\t\t\t´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´")
                print("\t\t\t\t´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´")
                print("\t\t\t\t´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´")
                print("\t\t\t\t´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´")
                









        if (s!="1" and s!="2"):
            print("\t\t\t\t…………………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print("\t\t\t\t……………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█")
            print("\t\t\t\t…………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓")
            print("\t\t\t\t………▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓")
            print("\t\t\t\t……█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█")
            print("\t\t\t\t…▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█")
            print("\t\t\t\t█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█")
            print("\t\t\t\t▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌")
            print("\t\t\t\t…█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█")
            print("\t\t\t\t..█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓█")
            print("\t\t\t\t…█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█")
            print("\t\t\t\t..█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█")
            print("\t\t\t\t..█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█")
            print("\t\t\t\t.█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█")
            print("\t\t\t\t.██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██")
            print("\t\t\t\t..██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██")
            print("\t\t\t\t..█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█")
            print("\t\t\t\t..█▓▒░▒▓███████▓▓▄▀░░▀▄▓▓███████▓▒░▒▓█")
            print("\t\t\t\t….█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█")
            print("\t\t\t\t……█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█")
            print("\t\t\t\t………█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█")
            print("\t\t\t\t………▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀")
            print("\t\t\t\t………….░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░")
            print("\t\t\t\t…………█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█")
            print("\t\t\t\t………….█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█")
            print("\t\t\t\t…………..█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█")
            print("\t\t\t\t…………….█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌")
            print("\t\t\t\t……………..█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█")
            print("\t\t\t\t……………..█▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█")
            print("\t\t\t\t………………█▓▒▓█░░░░▀▀▀▀░░░░░█▓▓█")
            print("\t\t\t\t………………█▓▒▒▓█░░░░ ░░░░░░░█▓▓█")
            print("\t\t\t\t………………..█▓▒▓██▄█░░░▄░░▄██▓▒▓█")
            print("\t\t\t\t………………..█▓▒▒▓█▒█▀█▄█▀█▒█▓▒▓█")
            print("\t\t\t\t………………..█▓▓▒▒▓██▒▒██▒██▓▒▒▓█")
            print("\t\t\t\t………………….█▓▓▒▒▓▀▀███▀▀▒▒▓▓█")
            print("\t\t\t\t……………………▀█▓▓▓▓▒▒▒▒▓▓▓▓█▀")
            print("\t\t\t\t………………………..▀▀██▓▓▓▓██▀")

        elif option==6:
            import webbrowser
            print(webbrowser.open("https://rajkumarsir.webs.com/python-xi-and-xii"))

        elif option==7:            
            print("\t\t\t       ╔══╦╗╔╗        ╔╗ ╔══╦╗   ╔╗  ╔═╦╗ ╔╦══╗") 
            print("\t\t\t       ║══╬╬╝║ ╔═╗╔═╦╦╝║ ║══╣╚╦═╗║╚╗ ║╬║╚╦╝╠╗╔╝")
            print("\t\t\t       ╠══║║╬║ ║╬╚╣║║║╬║ ╠══║║║╬╚╣║║ ║╔╩╗║╔╝║║╔╗")
            print("\t\t\t       ╚══╩╩═╝ ╚══╩╩═╩═╝ ╚══╩╩╩══╩╩╝ ╚╝ ╚═╝ ╚╝╚╝")

            flag=False 
            continue 

if __name__=="__main__":
    main()






