import csv
import os
print("#####################   LIBRARY MANAGEMENT SYSTEM    #####################")  
#fields for book
fields = ['Book Id','Book Title','Author Name','Publisher','Edition','Price']
fb="Book.csv" #variable name=file name 
#fields for member
field=['Member Id','Member name','Member email','Member phone no']
fm="Member.csv"
#fields for book2
field_2=['Date of Issue','Book ID','Member ID','Member Name']
fb2="Book_2.csv"


def Add_Books():
    print("=======================================================")
    print("------------------- ADD BOOK SCREEN -------------------")
    print("=======================================================")
    book=[]
    csvfilew = open(fb,'a+',newline="")#EOL suppressed 
    csvw=csv.writer(csvfilew)          # writer object
    #csvw.writerow(fields)
    ans='y'
    while ans=='y' or ans=='Y':
        B_id=input("Enter Book id:")
        B_title=input("enter Book title:")
        author=input("Enter author name:")
        publisher=input("Enter publisher name:")
        edition=input("Enter edition:")
        price=int(input("enter price of the book:"))
        book.extend([B_id,B_title,author,publisher,edition,price])
        #print(book)
        csvw.writerow(book)
        book=[]
        print("Book added successfully")
        ans=input("do you wish to continue adding book type (y)-for yes")
    csvfilew.close()

def membership():
    print("=======================================================")
    print("------------------- MEMBERSHIP SCREEN-------------------")
    print("=======================================================")
    while True:
        print("MENU FOR MEMBERSHIP")
        print("1.Do you want to register a member?...press 1")
        print("2.Do you want to cancel a membership?...press 2")
        print("3.Do you want to update a membership?...press 3")
        print("4.Do you want to exit?...press any number")
        ch=int(input("Enter your choice:"))
        if ch==1:
            print("-------------------Register a member---------------------")
            member=[]
            csvfilew = open(fm,'a+')
            csvw=csv.writer(csvfilew,lineterminator='\n')#EOL suppressed 
            #csvw.writerow(field)
            print("--Registered member name--")
            csvfiler = open(fm,'r+')
            csvr=csv.reader(csvfiler,lineterminator='\n')
            for i in csvr:
                print(i)
            csvfiler.close()
            ans='y'
            while ans=='y' or ans=='Y':
                M_Id=input("Enter Member Id")
                M_Name=input("enter Member name")
                M_Email=input("Enter Member\'s email id")
                M_phone=input("Enter Member\'s phone no")
                member.extend([M_Id,M_Name,M_Email,M_phone])
                csvw.writerow(member)
                member=[]
                print("Member registered successfully")
                ans=input("do you wish to continue type (y)-for yes (n) - for no")
            csvfilew.close()

        elif ch==2:
           print("-------------------cancel a membership-------------------")
           csvfilew = open("newmember.csv",'a+',newline="")#EOL suppressed
           csvw=csv.writer(csvfilew)
           #csvw1.writerow(fields)
           id=input("enter the Member\'s id whose membership you want to cancel")
           k=0
           with open(fm,'r+')as csvfiler:
               csvr=csv.reader(csvfiler,lineterminator='\n')
               for row in csvr:
                   if id!=row[0]:
                       csvw.writerow(row)
                   if id==row[0]:
                       k=1
                       print("Membership cancelled successfully")
               if k==0:
                   print("No matching record found! Could not delete anything!!!")
           csvfilew.close()
           os.remove(fm)
           os.rename("newmember.csv",fm)

        elif ch==3:
            print("-------------------update a membership-------------------")
            member=[]
            id=input("Enter Member\'s id which is to be updated")
            csvfilew = open("newm.csv",'a+',newline="")
            csvw=csv.writer(csvfilew)
            csvfiler=open(fm,'r+')
            csvr=csv.reader(csvfiler,lineterminator='\n')
            for row in csvr:
                if id!=row[0]:
                    csvw.writerow(row)
                elif id==row[0]:
                    print("--Previous Data--")
                    print(field)
                    print(row)
                    M_Id=input("Enter Member Id")
                    M_Name=input("Enter Member name")
                    M_Email=input("Enter Member\'s email id")
                    M_phone=input("Enter Member\'s phone no")
                    member.extend([M_Id,M_Name,M_Email,M_phone])
                    csvw.writerow(member)
                    member=[]
                    
                    print("Membership updated successfully")
            csvfiler.close()
            csvfilew.close()
            os.remove(fm)
            os.rename("newm.csv",fm)

        else:
            break;

def Issue_Book():
    Book=[]
    csvfiler=open(fb2,'r+')
    csvr=csv.reader(csvfiler,lineterminator='\n')
    
    print("=======================================================")
    print("------------------- ISSUE BOOK SCREEN-------------------")
    print("========================================================")
    Book_id=input("Enter Book ID:")
    mem_id=input("Enter Member ID:") #mem_id is member ID
    c=0
    
    for i in csvr:
        if (i[1])==Book_id:
            print("Sorry!! Book is already issued")
            c=1
            break
        elif (i[2])==mem_id:
            print("you had already issued a book")
            c=1
            break
    
        
    if c!=1:
        csvfilew=open(fb2,'a+',newline="")
        csvw=csv.writer(csvfilew)
        
        Date_of_Issue=input("Enter the current Date-(DD-MM-YYYY):")
        Book_ID=Book_id
        Member_Id=mem_id
        Member_Name=input("Enter the name : ")
        
        Book.extend([Date_of_Issue,Book_ID,Member_Id,Member_Name])
        csvw.writerow(Book)
        Book=[]
        print("Book issued successfully")
        csvfilew.close()
    
    csvfiler.close()

def Return_Book():
    csvfilew=open("new_Book_2.csv",'a+',newline="")
    csvw=csv.writer(csvfilew)
    
    print("=========================================================")
    print("------------------- RETURN BOOK SCREEN-------------------")
    print("=========================================================")
    mem_id=input("Enter Member ID:") #mem_id is member ID
    
    csvfiler=open(fb2,'r+',newline="")
    csvr=csv.reader(csvfiler)

    
    k=0
    for i in csvr:
        if(i[2])!=mem_id :
            csvw.writerow(i)
            
        if(i[2])==mem_id :
            k=1
            no_days=int(input("How many days it have been since the book was issued?"))
            print("------Details-----")
            print("Date of Issue :",i[0])
            print("Book ID :",i[1])
            print("Member ID :",i[2])
            print("Member Name :",i[3])
            if no_days>14:
                fine=(no_days-14)*2
            else :
                fine=0
            print("Fine :",fine)
            print("Book returned successfully")
            
    if k==0:
        print("You have not issued any book yet")

    csvfilew.close()
    csvfiler.close()
    os.remove(fb2)
    os.rename("new_Book_2.csv",fb2)

def search_record():
    while True:
        print("===========================================================")
        print("------------------- SEARCH RECORD SCREEN-------------------")
        print("===========================================================")
        print("MENU")
        print("1.Books")
        print("2.Members")
        print("3.Exit")
        ch=int(input("Enter choice:"))
        if ch==1:
            ans='y'
            while ans=='y' or ans=='Y':
                print("-------------------Search Book-------------------")
                bn=input("Enter book name to be searched")
                k=0
                with open(fb,'r+')as csvfiler:
                    csvr=csv.reader(csvfiler,lineterminator='\n')
                    print(fields)
                    for row in csvr:
                        if  bn.lower()==(row[1]).lower(): 
                            k=k+1
                            print(row)
                    if k==0:
                        print("-------no record found!!!")
                ans=input("do you wish to continue type y-for yes n - for no")
        elif ch==2:
            ans='y'
            while ans=='y' or ans=='Y':
                print("-------------------Search Member-------------------")
                mn=input("Enter member name to be searched")
                k=0
                with open(fm,'r+')as csvfiler:
                    csvr=csv.reader(csvfiler,lineterminator='\n')
                    print(field)
                    for row in csvr:
                        if  mn.lower()==(row[1]).lower() :
                            k=k+1
                            print(row)
                    
                    if k==0:
                       print("--------no member found!!!")
                ans=input("do you wish to continue type y-for yes n - for no")
        else:
            break;   

def display_record():
    while True:
        print("===========================================================")
        print("-------------------DISPLAY RECORD SCREEN-------------------")
        print("===========================================================")
        print("MENU")
        print("1.Books")
        print("2.Members")
        print("3.Exit")
        ch=int(input("Enter choice:"))
        if ch==1:
          
            print("-------------------Display Book-------------------")
            with open(fb,'r+',newline='\r\n')as csvfiler: #EOL suppressed
               csvr=csv.reader(csvfiler)
               for r in csvr:
                   print(r)
          
        elif ch==2:
            print("-------------------Display Member-------------------")
            with open(fm,'r+',newline='\r\n')as csvfiler:
                csvr=csv.reader(csvfiler)
                for r in csvr:
                    print(r)
        else:
            break;
     


             
  
    
    


reply='yes'
while reply=="YES" or reply=="yes":
    print("==========================================================")
    
    print("---------------  L I B R A R Y     M E N U  --------------")
    print("==========================================================")
    print("1. Add Books")
    print("2. Membership")
    print("3. Issue book")
    print("4. Return book")
    print("5. Search Record")
    print("6. Display Record")
    print("7. exit the screen")
    ch=int(input("accept the choice"))


    if ch==1:
        Add_Books()
    elif ch==2:
        membership()
    elif ch==3:
        Issue_Book()
    elif ch==4:
        Return_Book()
    elif ch==5:
        search_record()
    elif ch==6:
        display_record()
    elif ch==7:
        print("-------Thank you-------")
        break;
    else:
        continue;

    reply=input("do you wish to continue type (yes) for continue")


            
   
