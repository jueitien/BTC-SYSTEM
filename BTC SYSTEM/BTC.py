level=["1","2","3","4"]
info_container=[]
tutor_container=[]
tutor=[]
student_container=[]
student_sub=[]
subject = ["ENG", "BM", "MT", "SN", "SEJ"]
Level = ["Level1", "Level2", "Level3", "Level4", "Level5"]
pending_request = []
View_Schedule = []
admin_unpw=[]
all_user=[]
all_pending_request=[]
payment=[]
receipt=[]
r=open("login.txt","r")
for pl in r:
    a=pl[:-1].split(",")
    all_user=all_user+[a]
tl=open("login.txt","r")
for i in tl:
    if 'tutor' in i:
        tutor_list=i[:-1].split(",")
        tutor_container=tutor_container+[tutor_list]
Tic=open("tutor class information.txt","r")
for i in Tic:
    class_sch=i[:-1].split(",")
    info_container=info_container+[class_sch]
sl=open("login.txt","r")
for i in sl:
    if 'student' in i:
        student_list=i[:-1].split(",")
        student_container=student_container+[student_list]
Ad=open("login.txt","r")
for i in Ad:
    if 'admin' in i:
        admin_list=i[:-1].split(",")
        admin_unpw=admin_unpw+[admin_list]
r = open('Student req.txt', 'r')
for i in r:
    a = i.strip().split(",")
    all_pending_request=all_pending_request+[a]
r=open("payment.txt","r")
for i in r:
    a=i.strip().split(",")
    payment=payment+[a]
#declan    
def register_tutor():
    level = ["1", "2", "3", "4", "5"]
    subject = ["English", "Math", "Science", "History"]
    print("register tutor")
    print("please insert the tutor information")
    loop=True
    while loop==True:
        new_tutor_username=input("insert the new tutor username: ")
        new_tutor_password=input("insert the new tutor password: ")
        while True:
            new_tutor_level=input("insert new tutor level( [1] Level1,[2] Level2,[3] Level3,[4] Level4 [5] Level5: ")
            if new_tutor_level in level:
                break
            else:
                print("just Allow 1/2/3/4/5, try it again")
        while True:
            new_tutor_subject=input("insert new tutor subject( [1]English [2]Math [3]Science [4]History: ")
            if new_tutor_subject not in ("1","2","3","4","5"):
                print("just Allow 1/2/3/4/5, try it again")
            s = subject[int(new_tutor_subject)-1]
            a=open("login.txt","a")
            a.write(f'{new_tutor_username},{new_tutor_password},Level{new_tutor_level},{s},tutor\n')
            a.close()
            break
            
        while True:
            continue_reg=input("[1]continue [2]exit :")
            if continue_reg=="1":
                break
            elif continue_reg=="2":
                loop=False
                break
            else:
                print("just 1/2!")
                continue

def delete_tutor():
    a=True;list_del=[]
    del_name=input("insert the username for delete tutor: ")
    r=open("login.txt","r")
    for i in r:
        a=i[:-1].split(',')
        list_del=list_del+[a]
    r.close()
    w=open("login.txt","w")
    for p in list_del:
        if p[0]==del_name and 'tutor' in p:
            print("delete sucessful")
        else:
            k=",".join(p)
            w.writelines(f"{k}\n")
def register_receptionist():
    global all_user
    print("Register receptionist")
    print("Please insert the receptionist information")
    loop = True;Temporary_list=[]
    while loop == True:
        new_receptionist_username = input("Insert the new Receptionist username: ")
        new_receptionist_password = input("Insert the new Receptionist password: ")
        m=open("login.txt","a")
        m.write(f'{new_receptionist_username},{new_receptionist_password},receptionist\n')
        m.close()
        a=Temporary_list+[new_receptionist_username]+[new_receptionist_password]+["receptionist"]
        all_user.append(a)
        print("Register Successful")
        while True:
            continue_reg = input("1. Continue | 2. Exit :")
            if continue_reg == "1":
                break
            elif continue_reg == "2":
                loop = False
                break
            else:
                print("Just type 1 or 2")
        continue

def delete_receptionist(receptionist_name,user_role):
    global all_user
    found = False
    with open("login.txt", "r") as receptionist_file:
        for line in receptionist_file:
            receptionist_info = line[:-1].split(',')
            if receptionist_name in receptionist_info and user_role in receptionist_info:
                all_user.remove(receptionist_info)
                found=True
    if found:
        tutor_file=open("login.txt", "w")
        for i in all_user:
            a=",".join(i)
            tutor_file.writelines(f"{a}\n")
        tutor_file.close()
        print(f"{user_role} {receptionist_name} deleted.")
    else:
        print(f"{user_role} {receptionist_name} not found.")


def view_monthly_income_report():
    print("tutor salary")
    print("------------")
    print("Level1 $100\nLevel2 $150\nLevel3 $200\nLevel4 $250\n------------")
    total=0;total_tutor=0
    r=open("receipt.txt","r")
    for i in r:
        a=i[:-1].split(",")
        total=int(a[1])+total
    r=open("login.txt","r")
    for i in r:
        a=i[:-1].split(",")
        if "tutor" in a:
            if a[2] == "Level1":
                total_tutor=total_tutor+100
            elif a[2] == "Level2":
                total_tutor=total_tutor+150
            elif a[2] == "Level3":
                total_tutor=total_tutor+200
            elif a[2] == "Level4":
                total_tutor=total_tutor+250
    print(f"total salary is {total}")
    print(f"total tutor salary is {total_tutor}")
    income=total-total_tutor
    print(f"income of BTC is {income}")

def update_profile_admin():
    all_login_list=[]
    r=open("login.txt","r")
    for i in r:
        a=i[:-1].split(",")
        all_login_list=all_login_list+[a]
    new_username = input("Enter username: ")
    new_password = input("Enter password: ")

  
    for i in all_login_list:
        if "admin" in i:
            i[0]=new_username
            i[1]=new_password
            admin_unpw[0][0]=new_username
            admin_unpw[0][1]=new_password

            print("upload successful")
            print("please logout and enter your new username and password")
    w=open("login.txt","w")
    for i in all_login_list:
        b=",".join(i)
        w.writelines(f"{b}\n")
#ash

def login_lock():
    global lock,admin_unpw
    print("your account already lock,need admin unlock your account")
    while True:
        username_unlock=input("admin username for unlock: ")
        password_unlock=input("admin password for unlock: ")
        if admin_unpw[0][0]+admin_unpw[0][1]==username_unlock+password_unlock:
            print("unlock successful")
            lock=False
            break
        else:
            print('login again')

def update_enrollment():
    try:
        global rep_username,all_user
        student_ls=[];count=0;num=[]
        print("list of student request for update subject")
        for i in all_pending_request:
            count+=1
            num=num+[count]
            print(f"{count}) {i}")
        if num !=[]:
            Student_un=int(input("choose the option: "))
            if Student_un in num:
                for a in all_user:
                    if 'student' in a and a[0]==all_pending_request[Student_un-1][0]:
                        student_ls=student_ls+a
                        for p in a:
                            if p in subject:
                                a=False
                index=all_user.index(student_ls)
                if a==True:
                    print("invalid student")
                else:
                    student_ls[student_ls.index(all_pending_request[Student_un-1][1])]=all_pending_request[Student_un-1][2]
                    all_user[index]=student_ls
                    all_pending_request.remove(all_pending_request[Student_un-1])
                    w=open("login.txt","w")
                    for i in all_user:
                        a=",".join(i)
                        w.writelines(f"{a}\n")
                    w.close()
                    a=open("student req.txt","w")
                    for i in all_pending_request:
                        d=",".join(i)
                        a.writelines(f"{d}\n")
                    a.close()  
                    print("upload successful")
            else:
                print("no this type subject")
        else:
            print("No Subject request")
            return
    except ValueError:
        print("just allow num")
    
def delete_completed_student():
    try:
        global all_user
        count=0;student_ls=[]
        for i in all_user:
            if 'student' in i and "Level4" in i:
                count+=1
                student_ls=student_ls+[i]
                print(f"{count}) {i}")
            else:
                print("no Student")
                return
        del_option=int(input("Enter your option: "))
        all_user.remove(student_ls[del_option-1])
        w=open("login.txt","w")
        for i in all_user:
            a=",".join(i)
            w.writelines(f"{a}\n")
        w.close()
    except ValueError:
        print("just insert number!!")
        delete_completed_student()
def UpdateProfile():
    global all_user,rep_username
    new_username=input("please insert your new username: ")
    new_password=input("please insert your new password: ")
    for i in all_user:
        if i[0]==new_username or i[1]==new_password and 'receptionist'in i:
            print("username or password exist")
            return UpdateProfile()
        else:
            if "receptionist" in i and i[0]==i[0]:
                all_user[all_user.index(i)][0]=new_username
                all_user[all_user.index(i)][1]=new_password
            w=open("login.txt","w")
            for a in all_user:
                b=",".join(a)
                w.writelines(f"{b}\n")
            w.close()


def st_sub():
    global student_sub
    count_subject=True;time=3
    student_sub=[]
    while count_subject==True and time>0:
        new_student_subject=input(f"insert the new student subject(maximum 3 subject), left {time-1} attempt:")
        student_sub=student_sub+[new_student_subject]
        continue_subject=input("yes/no?") 
        if time==1 and continue_subject=='yes':
            print("just up to 3 subject")
            time-=3
        elif continue_subject=='no':
            time-=3
        elif continue_subject=='yes':
            time-=1
        else:
            print("just allow yes/no\n")
            student_sub.pop()
def register_student():
    loop = True
    while loop == True:
        name = input("Enter student's name: ")
        ic_passport = input("Enter IC/Passport: ")
        email = input("Enter email: ")
        contact_number = input("Enter contact number: ")
        address = input("Enter address: ")
        level = input("Enter student's level: ")
        st_sub()
        month_of_enrolment = input("Enter month of enrolment: ")
        a = open("login.txt", "a")
        print(student_sub)
        a.write(f'{name},{ic_passport},{email},{contact_number}.{address},{level},{",".join(student_sub)},{month_of_enrolment}\n')
        print("Register Successful")
        a.close()
        while True:
            continue_reg=input("[1]continue [2]Exit")
            if continue_reg=="1":
                break
            elif continue_reg=="2":
                return
            else:
                print("just allow number")

def accept_payment():
    count=0;num=[];std=[]
    for i in payment:
        if "paid" not in i:
            count+=1
            num=num+[count]
            print(f"{count}) {i}")
            std=std+[i]
    if num==[]:
        print("No payment")
    else:
        choice=int(input("choose the option or insert 0 to exit: "))
        if choice not in num:
            print("no this type of option")
        elif choice==0:
            return
        else:
            payment[payment.index(std[choice-1])].append("paid")
            w=open("payment.txt","w")
            for i in payment:
                v=",".join(i)
                w.writelines(f"{v}\n")
            w.close()
            a=open("receipt.txt","a")
            p=",".join(std[choice-1])
            a.write(f"{p}\n")
            a.close()
        print("accept successful")

#jueitien
def class_information():
    global username,info_container
    while True:
        b=open("tutor class information.txt","a")
        level=input("Level(1/2/3/4): ") 
        subject_ask=input("[1]ENG [2]BM [3]MT [4]SN [5]SEJ: ")
        date=input("date(Mon/Tue/Wed/Tur/Fri): ")
        time=input("time(5:00pm/11:00am etc): ")
        lv=level.strip();sb=subject_ask.strip();dt=date.strip();tm=time.strip()
        if len(lv)==0 or len(sb)==0 or len(dt)==0 or len(tm)==0:
            print("Not allow Null\n")
        elif subject_ask not in ("1","2","3","4","5"):
            print("level and subject just allow num, try it again")
        else:
            s= subject[int(subject_ask)-1]
            b.write(f'{username},Level{level},{s},{date} {time}\n')
            b.close()
            info_container=info_container+[f'{username},Level{level},{s},{date} {time}'.split(',')]
            break
                                       
def update(index):
    global update_error,info_container
    while True:
        print("update your information")
        level=input("Level(1/2/3/4): ") 
        subject=input("[1]ENG [2]BM [3]MT [4]SN [5]SEJ: ")
        date=input("date(Mon/Tue/Wed/Thur/Fri): ")
        time=input("time(5:00pm/11:00am etc): ")
        lv=level.strip();sb=subject.strip();dt=date.strip();tm=time.strip()
        if len(lv)==0 or len(sb)==0 or len(dt)==0 or len(tm)==0:
            print("Not allow Null\n")
        else:
            info_container[index][1]=f"Level{level}"
            if subject=="1":
                info_container[index][2]="ENG"
            elif subject=="2":
                info_container[index][2]="BM"
            elif subject=="3":
                info_container[index][2]="MT"
            elif subject=="4":
                info_container[index][2]="SN"
            elif subject=="5":
                info_container[index][2]="SEJ"
            info_container[index][3]=f"{date} {time}"
            b=open(f"tutor class information.txt","w")
            for i in info_container:
                a=",".join(i)
                b.writelines(f"{a}\n")
            b.close()
            break

def update_info():
    try:
        num=0;num_cont=[];update_list=[]
        global update_error,info_container,info_index
        for i in info_container:
            if i[0]==username:
                update_list=update_list+[i]
        for a in update_list:
            num+=1
            num_cont=num_cont+[num]
            print(f"{num}){a}")
        tutor_choice=int(input("which info need to update or press 0 to exit: "))
        if tutor_choice==0:
            return
        elif tutor_choice in num_cont:
            info_index=info_container.index(update_list[tutor_choice-1])
            update(info_index)   
    except ValueError:
        print("ONLY INT!!!!\n")
        update_info()

def delete_info():
    try:
        num=0;num_cont=[];delete_list=[]
        global delete_error,info_container
        for i in info_container:
            if i[0]==username:
                delete_list=delete_list+[i]
        print("this is your class information\n")
        for a in delete_list:
            num+=1
            num_cont=num_cont+[num]
            print(f"{num}){a}")
        tutor_choice=int(input("which info need to update or press 0 to exit: "))
        if tutor_choice==0:
            return
        elif tutor_choice in num_cont:
            info_index=info_container.index(delete_list[tutor_choice-1])
            info_container.pop(info_index)
            print("delete successful")
            w=open("tutor class information.txt","w")
            for i in info_container:
                a=",".join(i)
                w.writelines(f"{a}\n") 
        else:
            print("No this type of information")
    except ValueError:
        print("ONLY INT!!!!\n")
        delete_info()
    


def list_of_student():
    num=0;num_cont=[];info_list=[]
    global info_container,student_container
    for i in info_container:
        if i[0]==username:
            info_list=info_list+[i]
    for a in info_list:
        num+=1
        num_cont=num_cont+[num]
        print(f"{num}){a}")
    if num_cont!=[]:
        print("this is your class information\n")
        tutor_choice=int(input("which info need to list or press 0 to exit: "))
        if tutor_choice==0:
                return
        elif tutor_choice in num_cont:
            list_choice=info_list[tutor_choice-1]
            for a in student_container: 
                if info_list[tutor_choice-1][1] in a and info_list[tutor_choice-1][2] in a:
                    print(f'Name: {a[0]}\nSubject: {list_choice[1]}\nLevel: {list_choice[2]}\n')
    else:
        print("No class")

        

def reset_tutor():
    while True:
        alllist=[]
        new_un=input("new username: ")
        new_pw=input("new password: ")
        if new_un=="" or new_pw=="":
            print("not allow Null")
        else:
            b=open(f"login.txt","r")
            for tt in tutor_container:
                if tt[0]==new_un and tt[1]==new_pw and 'tutor' in tt:
                    print("username & password exist")
                    return reset_tutor()
                elif tt[1]==new_pw and 'tutor' in tt:
                    print("password exist")
                    return reset_tutor()
                elif tt[0]==new_un and 'tutor' in tt:
                    print("username exist")
                    return reset_tutor()
            for i in b:
                a=i[:-1].split(",")
                if a[0]==username and 'tutor' in a:
                    a[0]=new_un
                    a[1]=new_pw
                alllist=alllist+[a]
            b.close()
            c=open("login.txt","w")
            for h in alllist:
                a=",".join(h)
                c.writelines(f"{a}\n")
            c.close()
            break


#jun
def view_schedule():
    print("Your class schedule:\n")
    a = open("tutor class information.txt", "r")
    for Subject in a:
        b = Subject.strip().split(",")
        if b[1] == student_Level[0] and b[2] in student_sub:
            print(f"Tutor name: {b[0]}\nSubject: {b[2]}\nDate: {b[3]}\n")
    
           
def sent_request_receptionist():
    global lock_req,pending_request,all_pending_request
    print(len(pending_request))
    while True:
        if lock_req == True and len(pending_request) != 0:
            print("pending request sent to receptionist")
            print(pending_request)
            break
        else:
            print("Pending Request not found or request processed.\n")
        print("Send a request to the receptionist to change the subject enrollment")
        print(student_sub)
        old_subject = input("Which subject did you want to change?(enter 0 for exit) : ")
        if old_subject == "0":
            break
        elif old_subject not in student_sub:
            print("\nError,only allowed ENG/BM/SN/SEJ/MT\n")
        elif old_subject in student_sub:
            new_subject = input("Change subject to? :")
            if new_subject not in subject:
                print("\nError,only allowed ENG/BM/SN/SEJ/MT\n")
            elif new_subject in student_sub:
                print("\nSubject is already selected\n")
            else:
                pending_request.append([User_info[0], old_subject, new_subject])
                all_pending_request.append([User_info[0], old_subject, new_subject])
                Sr = open("Student req.txt", "a")
                for i in all_pending_request:
                    j = ",".join(i)
                    Sr.write(j + "\n")
                    lock_req=True
                Sr.close()
                


def delete_pending_request_receptionist():
    try:
        global lock_req
        container = []
        if lock_req==True and len(pending_request) != 0:
            delete = input("Are you sure you want to delete pending request to receptionist(yes/no):")
            if delete == "yes":
                print("your request has been deleted")
                o = open("Student req.txt", "r")
                for a in o:
                    c = a.strip().split(',')
                    if c != pending_request[0]:
                        container = container + [c]
                w = open("Student req.txt", "w")
                for i in container:
                    recall = ",".join(i)
                    w.writelines(f"{recall}\n")
                w.close()
                lock_req=False
                pending_request.pop()
                all_pending_request.pop()
            elif delete == "no":
                return

        else:
            print("Request not found or already processed.")
    except IndexError:
        print("\nNo pending request!!!")
        return


def update_profile():
        userlist = []
        x = 0
        print(f"Your Profile\n{User_info}")
        f = open("login.txt","r")
        for lines in f:
            record = lines.strip().split(",")
            if record[0] == User_info[0] and record[1] == User_info[1]:
                x+=1
                options = input("[1] Change name  [2] Change Password  [0] Back")
                if options == "1":
                    newname = input("Enter your new name: ")
                    User_info[0] = newname
                    print(User_info)
                elif options == "2":
                    newpass = input("Enter your new password: ")
                    User_info[1] = newpass
                    
                    print(User_info)
                elif options == "0":
                    return
                else:
                    print("Invalid option !")
                    return
            else:
                userlist.append(lines)
            
        f.close()
        if x == 1:
            f = open("login.txt","w")
            f.writelines(userlist)
            f.close()
            a = [item.strip() for item in User_info]
            result = ",".join(a)
            users = open("login.txt", "a")
            for i in result:
                users.write(f'{i}')
            users.write(f"\n")
            users.close()
        elif x == 0:
            print("This student doesnt exist")

def payment_status():
    global student_Level,student_sub,username
    list=[]
    print("Level1 $50\nLevel2 $60\nLevel3 $70\nLevel4 $80\n")
    print("------------")
    print("\nYou Subject")
    for i in student_sub:
        print(f"{student_Level} {i}")
    print("------------")
    if student_Level[0]=="Level1":
        total=50*len(student_sub)
    elif student_Level[0]=="Level2":
        total=60*len(student_sub)
    elif student_Level[0]=="Level3":
        total=70*len(student_sub)
    elif student_Level[0]=="Level4":
        total=80*len(student_sub)
    print(f"Total is ${total}")
    payment_res=input("Are you want to pay(yes/no) or press 0 to exit: ")
    if payment_res=='yes':
        a=open("payment.txt","a")
        a.write(f"{username},{total}\n")
        a.close()
        list=[]+[username]+[str(total)]
        payment.append(list)
        print("pay successful")
        print(payment)
    elif payment_res=="no":
        return
    elif payment_res=="0":
        return


login_page=True;lock1=False;lock=False;lock_req=True
while login_page==True:
    time=3;attempt=3;tutor_page=False;admin_page=True;Receptionist_page=False
    type_user=input("which user login?([1]admin [2]receptionist [3]tutor [4]student [5]Exit):")
    if type_user=='1':
        while admin_page==True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if admin_unpw[0][0]==username and admin_unpw[0][1]==password:
                print("login successful")
                loop=True
                while loop==True:
                    print("\n\n[1]register tutor [2]delete tutor [3]register receptionist [4]delete receptionist[5]view income [6]setting [7]logout")
                    Admin_respond=input("choose the option:")
                    if Admin_respond=="1":
                        register_tutor()
                    elif Admin_respond=="2":
                        delete_tutor()
                    elif Admin_respond=="3":
                        register_receptionist()
                    elif Admin_respond=="4":
                        delete_receptionist(input("Enter receptionist username: "),"receptionist")
                    elif Admin_respond=="5":
                        view_monthly_income_report()
                    elif Admin_respond=="6":
                        update_profile_admin()
                    elif Admin_respond=="7":
                        print("Logging out...")
                        admin_page=False
                        break
                        
            else:
                print("wrong password")
                continue
    elif type_user=="2" and lock==False:
        time=3;attempt=3
        while time>=1:
            time-=1
            attempt-=1
            rep_username = input("Enter Your receptionistID:")
            rep_password = input("Enter Your Password:")
            r=open("login.txt","r")
            for a in r:
                p=a[:-1].split(",")
                if rep_username == p[0] and rep_password == p[1] and 'receptionist' in p:
                    print("Login Success")
                    print("\nWelcome, " + rep_username + "\nRole: " +'receptionist')
                    Receptionist_page=True
                    time=-1
            if time==0:
                    print('your account have been log')
                    lock=True
            elif time>0:
                print("wrong password")
                print("invalid user ,left "+str(attempt)+" attempt")
            while Receptionist_page==True:
                print("\nReceptionist Menu:")
                print("1. Register Student")
                print("2. Update Enrollment")
                print("3. Accept Payment")
                print("4. Delete Completed Student")
                print("5. Update Profile")
                print("6. Logout")

                choice = input("Enter your choice: ")
                if choice == "1":
                    register_student()
                elif choice == "2":
                    update_enrollment()
                elif choice == "3":
                    accept_payment()
                elif choice == "4":
                    delete_completed_student()
                elif choice == "5":
                    UpdateProfile()
                elif choice == "6":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif type_user=="2" and lock==True:
        login_lock()
    elif type_user=="3" and lock1==False:
        while time>=1:
            time-=1
            attempt-=1
            username=input("pls insert your username:")
            password=input("pls insert your password:")
            r=open("login.txt","r")
            for i in r:
                p=i[:-1].split(",")
                for b in p:
                    if 'tutor' in b and p[0]==username and p[1]==password:
                        print("login successful")
                        tutor=tutor+p
                        login_page=False
                        tutor_page=True
                        time=-1
                
            if time==0:
                print('your account have been log')
                lock1=True
            elif time>0:
                print("invalid user ,left "+str(attempt)+" attempt")
            while tutor_page==True:
                print("[1]class information | [2]update information | [3]delete information | [4]list of student | [5]setting | [6]logout")
                tutor_respond=input("choose the option: ")
                if tutor_respond=="1":
                    class_information()
                elif tutor_respond=="2":
                    update_info()
                elif tutor_respond=="3":
                    delete_info()
                elif tutor_respond=="4":
                    list_of_student()
                elif tutor_respond=="5":
                    reset_tutor()
                elif tutor_respond=="6":
                    login_page=True
                    break

    elif type_user=="3" and lock1==True:
        print("your account already lock,need admin unlock your account")
        while True:
            username_unlock=input("admin username for unlock: ")
            password_unlock=input("admin password for unlock: ")
            if admin_unpw[0][0]+admin_unpw[0][1]==username_unlock+password_unlock:
                print("unlock successful")
                lock1=False
                break
            else:
                print('login again')
    elif type_user=="4":
        print("Welcome to Student Registration System\n")
        wrong = True;User_info = [];student_sub = [];student_Level = [];pending_request = [];
        for i in range(2, -1, -1):
            username = input("Enter Your StudentID:")
            password = input("Enter Your Password:")
            r=open("login.txt","r")
            for a in r:
                p=a[:-1].split(",")
                if username == p[0] and password == p[1] and 'student' in p:
                    User_info = User_info + p
                    for b in p:
                        if b in subject:
                            student_sub = student_sub + [b]
                        if b in Level:
                            student_Level = student_Level + [b]
                    print(student_Level)
                    print(student_sub)
                    wrong = False
                    print("Login Successful! ")
                    print("Hi", p[0], "! It's Great To See You")
                    r = open('Student req.txt', 'r')
                    for i in r:
                        a = i.strip().split(",")
                        if i[0] == User_info[0][0]:
                            pending_request = pending_request + [a]
                    break
            if wrong == True:
                print(f"Try it again still {i} attempt,Login failed! ")
            else:
                while True:
                    a=True;p=True
                    b = input("""
1.View class schedule
2.Request to change subject enrollment
3.Delete request to receptionist
4.View payment status
5.Update profile 
6.Exit
""")                
                    r=open("receipt.txt","r")
                    for i in r:
                        a=i[:-1].split(",")
                        receipt=receipt+[a]
                    if b == "1":
                        view_schedule()
                    elif b == "2":
                        sent_request_receptionist()
                    elif b == "3":
                        delete_pending_request_receptionist()
                    elif b=="4":
                        for i in payment:
                            if b == "4" and i[0]==username and "paid" not in i:
                                a=False
                                break
                            elif b=="4" and i[0]==username and "paid" in i:
                                p=False
                                break
                        if a==False:
                            print("payment is already done in this month, just waiting for receipt")
                        elif p==False:
                            print("payment accepted")
                            print("your receipt")
                            print("-------------")
                            for i in receipt:
                                if username in i:
                                    for a in i:
                                        print(a)
                        else:
                            payment_status()
                    elif b == "5":
                        update_profile()
                    elif b == "6":
                        break
                    else:
                        print("invalid,Please enter(1,2,3,4,5,6):")
                break
    elif type_user=="5":
        print("exiting...")
        break
else:
    print("pls insert the number")
