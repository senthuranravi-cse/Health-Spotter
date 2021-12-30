import csv
from csv import writer
from gtts import gTTS
from playsound import playsound
import string
from datetime import date
import webbrowser
#libraries........................
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()

while True: #infinite loop
    def addadmin():
        n=input("ENTER NEW ADMIN NAME:")
        n1=input("ENTER NEW ADMIN E-MAIL ID:")
        n2=input("ENTER NEW ADMIN AGE:")
        n4=input("ENTER NEW ADMIN PHONE NO:")
        n5=input("ENTER NEW ADMIN NICK-NAME:")
        n3=input("ENTER NEW ADMIN PASSWORD:")
        print("-------------------------------------------------------------------------------")
        n1=n1.lower()
        n=n.capitalize()
        with open('adb.csv', 'r') as f:
            lines = f.readlines()
            for entry in lines:
                if n1 in entry or n4 in entry or n5 in entry:
                    print("Sorry........you login already please signup or try with different mail id")
                else:
                    db1=[n,n1,n2,n3,n4,n5,today,current_time]
                    with open('adb.csv', 'a') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow(db1)
                        f_object.close()
                        text_val = 'successfully login new admin'
                        language = 'en'  
                        obj = gTTS(text=text_val, lang=language, slow=False)  
                        obj.save("ooo.mp3")  
                        playsound("ooo.mp3")
                        print("Successfully add the new admin data")
                        print(n," WELCOME TO OUR FAMILY")
                        print("-------------------------------------------------------------------")
    def void1():
        name=input("Enter your Name:")
        email=input("Enter your email:")
        age=input("Enter your age:")
        place=(input("Enter your place"))
        phone=int(input("Enter your phone no:"))
        password=input("Enter your password:")
        email=email.lower()
        with open('db.csv', 'r') as f:
            lines = f.readlines()
            c=0
            for entry in lines:
                if email in entry or phone in entry:
                    c=c+1
                else:
                    c=0   
        if c>1:
            print("Sorry........you login already please signup or try with different mail id")
        if c==0:
            db1=[name,email,age,place,phone,password,today,current_time]
            with open('db.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(db1)
                f_object.close()
                text_val = 'successfully login we hope this program will help you lot'
                language = 'en'  
                obj = gTTS(text=text_val, lang=language, slow=False)  
                obj.save("els.mp3")  
                playsound("els.mp3")
                print("Successfully login the data")
                print("-------------------------------------------------------------------")
    def void():
        text_val = 'welcome to hospital finder'
        language = 'en'  
        obj = gTTS(text=text_val, lang=language, slow=False)  
        #obj.save("ele.mp3")  
        playsound("ele.mp3") 
                        
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Current Time =", current_time)
        print("Today's date:", today)
        print("---------------Welcome To Hospital Finder-----------------")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        g=input("1)Admin \n2)customer \n3)credits \n")
        if g.upper()=="ADMIN" or g=="1":
            password=input("Enter the password:")
            admin(password)
            ii=input("Do you want to continue in admin page:")
            if ii.upper()=="YES":
                password=input("Enter the password:")
                admin(password)
            elif ii.upper()=="NO":
                void()
        if g.upper()=="CREDITS"or g=="3":
            credit()
        
    def admin(password):
        S=input("Enter your name:")
        S=S.capitalize()
        with open('adb.csv', 'r') as f:
            lines = f.readlines()
            b=0
            for entry in lines:
                if password in entry:
                    b+=1
                    text_val = 'hello boss'
                    language = 'en'  
                    obj = gTTS(text=text_val, lang=language, slow=False)  
                    #obj.save("exa.mp3") 
                    playsound("exa.mp3")
                    print("Hello boss ",S,"!!!!!!!!!")
                    print("Current Time =", current_time)
                    print("Date=",today)
                    d=input("=============>MENU<=================\n1)print all hospital\n2)add hopital\n3)login database\n4)add login\n5)add another admin\n")
                    with open('allindia hospitals.csv', 'r') as f:
                        lines = f.readlines()
                        if d.upper()=="ALL"or d=="1":
                            for entry in lines:
                                print(entry)
                                print("---------------------------------------------------------------------")
                    
                        elif d.upper()=="ADD"or d=="2":
                            no=int(input("how many data you are add now:"))
                            for i in range(1,no+1):
                                a=int(input("sr.no:"))
                                b=input("Name of Insurance Co. :")
                                c=input("State:")
                                d=input("City :")
                                e=input("Provider Name:")
                                f=input("Category code:")
                                g=input("Address:")
                                h=int(input("Pin Code:"))
                                i=int(input("Tel Area code:"))
                                j=int(input("Tel No.:"))
                                k=int(input("Fax No.:"))
                                l=int(input("Not Servicing to Insurance Co., but:"))
                                m=int(input("Provider No.:"))
                                List=[a,b,c,d,e,f,g,h,i,j,k,l,m]
                                with open('allindia hospitals.csv', 'a') as f_object:
                                    writer_object = writer(f_object)
                                    writer_object.writerow(List)
                                    f_object.close()
                                    print("Successfully add the data")
                                    print("-------------------------------------------------------------------")
                          
                        elif d.upper()=="LOGIN " or d.upper()=="LOGIN ADD" or d.upper()=="ADD" or d.upper()=="LA" or d.upper()=="AL"or d=="4":
                            nn=int(input("Enter how many logins you want:"))
                            for i in range(nn):
                                void1()
                        elif d.upper()=="LOGIN DATABASE" or d.upper()=="DATABASE" or d.upper()=="DB" or d.upper()=="LDB" or d=="3":
                            with open('db.csv', 'r') as f:
                                line = f.readlines()
                                for entry in line:
                                    print(entry)
                                    print("---------------------------------------------------------------------")
                                f=input("Do you want to login:")
                                if f.upper()=="YES"or f.upper()=="LOGIN":
                                    void1()
                        elif d.upper()=="ANOTHER ADMIN" or d.upper()=="ADMIN" or d.upper()=="AA" or d.upper()=="AAA" or d.upper()=="ADD ANOTHER ADMIN"or d=="5":
                            addadmin()
                        else:
                            print("SORRY BOSS YOU ENTERED WRONG MENU..............")            
            if b==0:
                print("SORRY YOU ENTERED WRONGLY.............................PLEASE TRY AGAIN........")
                t=input("TRY AGAIN..........\n")
                if t.upper()=="YES":
                    password=input("Enter the password:")
                    admin(password)

    def credit():
        text_val = """this program was developed by senthuran"""
                    
        language = 'en'  
        obj = gTTS(text=text_val, lang=language, slow=False)  
        obj.save("elo.mp3")  
        playsound("elo.mp3")
        print("""...................CODERS.....................
                    ->SENTHURAN RAVI""")
        n=input("If you want visit my website")
        if(n.upper()=="YES"):
            website()
        
        void()

    def website():
        print("open it.......wait a sec")
        webbrowser.open('https://sites.google.com/view/mysite-56/home')
        void()
                        
    
        
    text_val = 'welcome to hospital finder'
    language = 'en'  
    obj = gTTS(text=text_val, lang=language, slow=False)  
    #obj.save("ele.mp3")  
    playsound("ele.mp3") 
                        
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("---------------Welcome To Hospital Finder-----------------")
    print("Current Time =", current_time)
    print("Today's date:", today)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    g=input("1)Admin\n2)customer \n3)credits\n")
    if g.upper()=="ADMIN" or g=="1":
        password=input("Enter the password:")
        admin(password)
        ii=input("Do you want to continue in admin page:")
        if ii.upper()=="YES":
            password=input("Enter the password:")
            admin(password)
        elif ii.upper()=="NO":
            void()
    if g.upper()=="CREDITS" or g=="3":
        credit()
    print("<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    login=input("Do you want to \n 1)Signin \n 2)Signup \n 3)guest \n")
    print("------------------------------------------------------------------------------------")
    if login.upper()=="SIGN IN"or login.upper()=="SIGNIN"or login=="1":
        no=input("Enter your Name:")
        email=input("Enter your email:")
        age=input("Enter your age:")
        place=(input("Enter your place:"))
        phone=(input("Enter your phone no:"))
        password=input("Enter your password:")
        print("-------------------------------------------------------------------------------")
        name=string.capwords(no)
        email=email.lower()
        with open('db.csv', 'r') as f:
            lines = f.readlines()
            for entry in lines:
                if email in entry or phone in entry:
                    print("Sorry........you login already please signup or try with different mail id")
                else:
                    db1=[name,email,age,place,phone,password,today,current_time]
                    with open('db.csv', 'a') as f_object:
                        writer_object = writer(f_object)
                        writer_object.writerow(db1)
                        f_object.close()
                        text_val = 'successfully login we hope this program will help you lot'
                        language = 'en'  
                        obj = gTTS(text=text_val, lang=language, slow=False)  
                        #obj.save("els.mp3")  
                        playsound("els.mp3")
                        print("Successfully login the data")
                        print("-------------------------------------------------------------------")
    if login.upper()=="SIGN UP" or login.upper()=="SIGNUP" or login=="2":
        n=input("Enter your email:")
        n2=(input("Enter your password:"))
        n=n.lower()
        with open('db.csv', 'r') as f:
            lines = f.readlines()
            k=0
            for entry in lines:
                if n in entry :
                    if n2 in entry:
                        k+=1
                        text_val = 'welcome'
                        language = 'en'  
                        obj = gTTS(text=text_val, lang=language, slow=False)  
                        obj.save("elw.mp3")  
                        playsound("elw.mp3")
                        print("Welcome..................................... ")
                        print("-------------------------------------------------------------------------------")
            if k==0:
                print("You are not login till  now please login")
                f=input("Do you want to login:")
                if f.upper()=="YES":
                    void1()
                elif f.upper()=="NO":
                    void()
    u=input("Do you want guidelines:")
    if u.upper()=="YES":
        print("""Guidelines:
                    1)choose which state are you
                    2)type what do you want->if you want all hospital or particular one
                    3)choose place or category or hospital name""")
    
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")          
    o=input("Enter the State:")
    h=string.capwords(o)
    with open('allindia hospitals.csv', 'r') as f:
        lines = f.readlines()
        cnt = 0
        cf=0
        for entry in lines:
            if h in entry:
                cnt += 1

    print("Hospitals in",h,":", cnt)
    if cnt>0:
        io=input("1)print all hospital\n 2)you want specific one:")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        if io.upper()=="PRINT IT"or io.upper()=="PRINT "or io.upper()=="ALL" or io.upper()=="PRINT ALL" or io=="1": #print all hospital
            for entry in lines:
                if h in entry:
                    print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print(entry)
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
            yn=input("Do you want category yes/no:")
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
            if yn.upper()=="YES":
                c=input("Enter nursing or hospital:")
                c=c.capitalize()
                for entry in lines:
                    if h in entry and c in entry:
                        print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                        cf+=1
                        print(entry)
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("There are ",cf,"avaliable in ",h)
                text_val = 'thanks for calling'
                language = 'en'  
                obj = gTTS(text=text_val, lang=language, slow=False)  
                obj.save("a.mp3")  
                playsound("a.mp3")
                print("Thanks for Calling")
            d=input("Do you want to hospital name:")
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
            if d.upper()=="YES":
                name=input("Enter hospital name:")
                c=0
                for entry in lines:
                    if h in entry:
                        if name.upper() in entry:
                            print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                            c+=1
                            print(entry)
                            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                if c==0:
                    print("SORRY SIR.............",name.upper(),"HOSPITAL IS NOT ADDED IN OUR DATABASE SOON WE WILL ADD AND INFORM TO YOU")
                text_val = 'thanks for calling'
                language = 'en'  
                obj = gTTS(text=text_val, lang=language, slow=False)  
                obj.save("c.mp3")  
                playsound("c.mp3")
                print("Thanks for Calling")  
            elif yn.upper()=="NO":
                text_val = 'thanks for calling'
                language = 'en'  
                obj = gTTS(text=text_val, lang=language, slow=False)  
                obj.save("b.mp3")  
                playsound("b.mp3")
                print("Thanks for Calling!!!")
                
        else:
            sc=input("do you want to\n 1)enter hospital name \n 2)place \n 3)category:")
            if sc.upper()=="HOSPITAL NAME" or sc.upper()=="NAME" or sc.upper()=="HOSPITAL "or sc=="1": #hospital name
                c=0
                name=input("Enter hospital name:")
                for entry in lines:
                    if h in entry:
                        if name.upper() in entry:
                            print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                            c+=1
                            print(entry)
                if c==0:
                    print("SORRY SIR.............",name.upper(),"HOSPITAL IS NOT ADDED IN OUR DATABASE SOON WE WILL ADD AND INFORM TO YOU")
                text_val = 'thanks for calling'
                language = 'en'  
                obj = gTTS(text=text_val, lang=language, slow=False)  
                obj.save("c.mp3")  
                playsound("c.mp3")
                
                print("Thanks for Calling")
            elif sc.upper()=="PLACE"or sc=="2": #place
                nam=input("Enter place:")
                for entry in lines:
                    if nam.capitalize() in entry:
                        print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                        cf+=1
                        print(entry)
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("There are ",cf,"hospital avalible in ",nam)
                dd=input("Do you want to choose category:")
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                if dd.upper()=="YES":
                    c=input("Enter nursing or hospital:")
                    for entry in lines:
                        if nam in entry and c.capitalize() in entry:
                            print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                            print(entry)
                            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                            cf=cf+1
                    print("There are ",cf,"avaliable in ",nam)
                    text_val = 'thanks for calling'
                    language = 'en'  
                    obj = gTTS(text=text_val, lang=language, slow=False)  
                    obj.save("d.mp3")  
                    playsound("d.mp3")
                
                    print("Thanks for Calling")
                d=input("Do you want to hospital name:")
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                if d.upper()=="YES":
                    name=input("Enter hospital name:")
                    c=0
                    for entry in lines:
                        if h in entry:
                            if nam.capitalize() in entry:
                                if name.upper() in entry:
                                    print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                                    c+=1
                                    print(entry)
                                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                    if c==0:
                        print("SORRY SIR.............",name.upper(),"HOSPITAL IS NOT ADDED IN OUR DATABASE SOON WE WILL ADD AND INFORM TO YOU")
                    text_val = 'thanks for calling'
                    language = 'en'  
                    obj = gTTS(text=text_val, lang=language, slow=False)  
                    #obj.save("c.mp3")  
                    playsound("c.mp3")
                    print("Thanks for Calling")    
                elif d.upper()=="NO":
                    text_val = 'thanks for calling'
                    language = 'en'  
                    obj = gTTS(text=text_val, lang=language, slow=False)  
                    obj.save("e.mp3")  
                    playsound("e.mp3")
                
                    print("Thanks for Calling")
                
            elif sc.upper()=="CATEGORY" or sc=="3": #category
                c=input("Enter nursing or hospital:")
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                for entry in lines:
                    if h in entry and c.capitalize() in entry:
                        print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                        cf+=1
                        print(entry)
                        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("There are ",cf,"avaliable in ",h)
                n=input("Do you want to search hospital in your places:")
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                if n.upper()=="YES":
                    nam=input("Enter place:")
                    print("------------------------------------------------------------------------------------------------------------------------------------------------")
                    for entry in lines:
                        if nam in entry and c.capitalize in entry:
                            print("""Sr. No.|| Name of Insurance Co.|| State ||City|| Provider Name|| Category ||Code ||Address ||Pin Code || Tel Area ||Code||||Tel No. ||Fax No. ||Not Servicing to 
Insurance Co., but Provider No.""")
                            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                            cf+=1
                            print(entry)
                            print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("There are ",cf,c,"in",nam)
                    text_val = 'thanks for calling'
                    language = 'en'  
                    obj = gTTS(text=text_val, lang=language, slow=False)  
                    obj.save("f.mp3")  
                    playsound("f.mp3")
                    print("Thanks for Calling")
                else:
                    text_val = 'thanks for calling'
                    language = 'en'  
                    obj = gTTS(text=text_val, lang=language, slow=False)  
                    obj.save("g.mp3")  
                    playsound("g.mp3")
                    print("Thanks For Calling")

                    
    elif cnt==0:
        text_val = 'There is no hospital avaliable in your state or you entered wrongly please try again'
        language = 'en'  
        obj = gTTS(text=text_val, lang=language, slow=False)  
        obj.save("ai.mp3")  
        playsound("ai.mp3")
        print("There is no hospital avaliable in your state or you entered wrongly.............")
        print("please try again.........")
        print("---------------------------------------------------------------------------------------------------")
