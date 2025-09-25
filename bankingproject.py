import mysql.connector as db
con=db.connect(user='root',password='Saranya@123',host='localhost',
               database='BankingSystem')
cur=con.cursor()
import random
from tabulate import tabulate
print("1.User login","2.Admin login","3.Exit")
while True:
    option=input("Enter a option(1.User login,2.Admin login,3.Exit):")
    if option.isdigit():
        if option=='1':
            while True:
                print("1.Register",
                      "2.login",
                      "3.Exit")
                ch=input("Enter a choice:")
                if ch.isdigit():
                    if ch=='1':
                        res=random.randint(1111,9999)
                        name=input("Enter a name:")
                        age=int(input("Enter a age:"))
                        while True:
                            mobile_no=input("Enter mobile no:")
                            if len(mobile_no)==10 and mobile_no.isdigit():
                                print("correct")
                                break
                            else:
                                print("Invalid mobile number")
                        
                        while True:
                            adhar_no=input("enter adhar no:")
                            if len(adhar_no)==12 and adhar_no.isdigit():
                                print("correct")
                                break
                            else:
                                print("Invalid adhar number")
                        account_type=input("Enter a account type(savings/current):")
                        total_amount=int(input("Enter amount:"))
                        acc_no=mobile_no+str(res)
                        print(acc_no)
                        cur.execute("select(sysdate())")
                        acc_date=cur.fetchone()[0]
                        print(acc_date)
                        pin=int(input("Enter a pin:"))
                        cur.execute('''insert into Register(Username, Age, Mobileno, Adharno,Pin,
                                                            Accounttype, Accountno, Acc_date, Totalamount)
                                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                                    [name,age,mobile_no,adhar_no,pin,account_type,acc_no,acc_date,total_amount]);
                        con.commit()
                        print("user registered successfully")
                        
                    elif ch=='2':
                        existing_account=input("Enter a account:")
                        cur.execute('select Accountno from Register')
                        out=cur.fetchall()
                        for i in out:
                            if i[0]==existing_account:

                                def viewaccountdetails():
                                    cur.execute("select * from Register where Accountno=%s",[existing_account]);
                                    view=cur.fetchall()
                                                
                                    l=['Username','Age','Mobileno','Adharno','Pin','Accounttype',
                                        'Accountno','Acc_date','Totalamount']
                                    print(tabulate(view,headers=l,tablefmt="grid"))

                                            
                                def debitamount(amo):
                                    cur.execute("select Totalamount from Register where Accountno=%s",[existing_account]);
                                    total=cur.fetchone()
                                    if amo<=total[0]:
                                        date=input("Enter a date:")
                                        balance=total[0]-amo
                                        cur.execute("insert into Transctions (Accountno,transctions_type,trans_date,Amount,Balance)values(%s,%s,%s,%s,%s)",
                                                    [existing_account,'debit',date,amo,balance])
                                        cur.execute("update Register set Totalamount=%s where Accountno=%s",[balance,existing_account])
                                        con.commit()
                                        print(" amount debited sucessfully")
                                    else:
                                        print("Insufficient Balance")
                                        
                                        
                                        
                                def creditamount(amo):
                                    cur.execute("select Totalamount from Register where Accountno=%s",[existing_account]);
                                    date=input("Enter a date:")
                                    total=cur.fetchone()
                                    balance=total[0]+amo
                                    cur.execute("insert into Transctions (Accountno,transctions_type,trans_date,Amount,Balance)values(%s,%s,%s,%s,%s)",
                                            [existing_account,'credit',date,amo,balance])
                                    cur.execute("update Register set Totalamount=%s where Accountno=%s",[balance,existing_account])
                                    con.commit()
                                    print(" amount credited sucessfully")
                                            
                                        
                                def new_pin():
                                    new_pin=int(input("Enter a new_pin:"))
                                    cur.execute("update Register set pin=%s where Accountno=%s",[new_pin,existing_account]);
                                    con.commit()
                                    print("updated successfully")
                                    
                                def statement():
                                    cur.execute("select * from Transctions where Accountno=%s",[existing_account]);
                                    view=cur.fetchall()
                                    labels=['trans_id', 'Accountno', 'transctions_type', 'trans_date', 'Amount', 'Balance']
                                    print(tabulate(view,headers=labels,tablefmt='grid'))
                                                                
                                while True:
                                    print("\n====== User Panel ======")
                                    print("1.view account details")
                                    print("2.Debit Amount")
                                    print("3.Credit Amount")
                                    print("4.Pin change")
                                    print("5.statement")
                                    print("6.exit")

                                    ch=input("Enter an option:")
                                    if ch.isdigit():
                                        if ch=='1':
                                               viewaccountdetails()
                                        elif ch=='2':
                                            amount=int(input("Enter a amount:"))
                                            debitamount(amount)
                                        elif ch=='3':
                                            amount=int(input("Enter a amount:"))
                                            creditamount(amount)
                                        elif ch=='4':
                                            new_pin()
                                        elif ch=='5':
                                            statement()
                                        else:
                                            print("exit")
                                            break
                                    else:
                                        print("invalid option")
                                break      
                                           
                                        
                        else:
                            print("account is not there")
                                        
                                    
                    else:
                        print("exit")
                        break
                else:
                    print("Invalid option")
                        
                
                  
        elif option=='2':
            admin_id=input("Enter a id:")
            password=input("Enter a password:")
            
            cur.execute("select*from adminlogin")
            data=cur.fetchall()
            for row in data:
                if admin_id==row[0]:
                    if password==row[1]:
                        print("login sucessfully")
                            
                        def Viewallusers():
                            cur.execute("select Username from Register")
                            data=cur.fetchall()
                            for i in data:
                                
                                print('-',i[0])
                                
                            
                        def Acc_particularuser(user):
                            cur.execute("select Accountno from Register")
                            vi=cur.fetchall()
                            for i in vi:
                                if i[0]==user:
                                    cur.execute("select * from Register where Accountno=%s",[user]);
                                    view=cur.fetchall()
                                    headers=['User_id','Username','Age','Mobileno','Adharno','Pin','Accounttype','Accountno',
                                              'Acc_date','Totalamount']
                                    print(tabulate(view, headers=headers, tablefmt="grid"))
                                    break
                            else:
                                print("Account is not Found")

                                
                            
                        def Tran_particularuser(user):
                            cur.execute("select Accountno from Transctions")
                            all_acc=cur.fetchall()
                            for i in all_acc:
                                if i[0]==user:
                                    cur.execute("select * from Transctions where Accountno=%s",[user]);
                                    view=cur.fetchall()
                                    labels=['trans_id', 'Accountno', 'transctions_type', 'trans_date', 'Amount', 'Balance']
                                    print(tabulate(view,headers=labels,tablefmt='grid'))
                                    break
                                            
                            else:
                                print("Account Transactions is not Found")
                                
                                    
                            
                        def Tran_particularday(day):
                            labels = ['trans_id', 'Accountno', 'transctions_type', 'trans_date', 'Amount', 'Balance']

                            cur.execute("SELECT * FROM Transctions WHERE trans_date = %s", [day])
                            transactions = cur.fetchall()

                            if transactions:
                                print(tabulate(transactions, headers=labels, tablefmt='grid'))
                            else:
                                print("No transactions found for that particular date.")
                            
                            

                        while True:
                            print("\n====== Admin Panel ======")
                            print("1.View all Users")
                            print("2.View complete Account Details of Particular User")
                            print("3.View complete Transactions of Particular User")
                            print("4.View Complete Transactions of Particular Day")
                            print("5.exit")
                                
                            opt=input("Enter a Option:")
                            if opt.isdigit():
                                if opt=='1':
                                    Viewallusers()
                                elif opt=='2':
                                    userr=input("Enter a Account Number:")
                                    Acc_particularuser(userr)
                                elif opt=='3':
                                    userr=input("Enter a Account Number:")
                                    Tran_particularuser(userr)
                                elif opt=='4':
                                    par_day=input("Enter a date(YYYY:MM:DD):")
                                    Tran_particularday(par_day)
                                else:
                                    print("exit")
                                    
                                    break
                            else:
                                 print("invalid option")
                else:
                    print("Incorrect password")
                break
            else:
                print("enter correct admin_id")

        else:
            print("exit")
            break

    else:
        print("Invalid Option")
            
            
       
            
con.cursor()    
con.close()

'''                  *************MYSQL CODE**************
#Banking project
use BankingSystem;
create table Register(User_id int ,Username varchar(20),Age int,Mobileno varchar(20),Adharno varchar(20),Pin int,Accounttype varchar(10),Accountno varchar(20),
Acc_date datetime,Totalamount int);
select*from Register;
insert into Register (Username,Age,Mobileno,Adharno,Pin,Accounttype,Accountno,Acc_date,Totalamount)
values('leela',22,'9392175728','270401404033','1234','savings','92092809809778','2024-06-22 11:12:01',12000),
('saranya',23,'9392175888','314014022300','4321','current','1166644515891','2024-07-01 14:12:01',16000),
('chakradhar',26,'9403075025','366883001422','9392','current','12589678963214','2025-02-05 10:12:01',14000);
truncate table Register;
create table Transctions(trans_id int Auto_increment primary key,Accountno varchar(20),transctions_type varchar(7),trans_date datetime,Amount int,Balance int);
alter table Register add primary key(Accountno);
select*from Transctions;
alter table Transctions add constraint fk_accountno foreign key(Accountno)references Register(Accountno);
select*from Transctions;
select * from Transctions where Accountno='1258967896321455';
select * from Transctions where trans_date='2025-04-21 12:01:07';
update  Transctions set trans_date='2025-03-12 11:12:00' where trans_id='1';
SET SQL_SAFE_UPDATES = 0;
create table adminlogin(admin_id varchar(20),admin_password varchar(20));
insert into adminlogin values('leela saranya','leela123');
select*from adminlogin;
update Register set User_id=4 where Accountno='98765432108613';
SELECT * FROM Transctions WHERE trans_date = '2025-07-07';
truncate table Transctions;
ALTER TABLE Register 
MODIFY COLUMN User_id INT NOT NULL AUTO_INCREMENT,
ADD UNIQUE KEY (User_id);
select(sysdate());

'''
    

