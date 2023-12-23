import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password="Luffy@pirate1", database="bank_management")

def Accnum():
    bank_code="91910"
    count_query = "SELECT COUNT(*) FROM account"
    x=mydb.cursor()
    x.execute(count_query)
    result=x.fetchone()
    cnt=result[0] +1
    accnum=bank_code + str(cnt)
    return accnum

def OpenAcc():
    name=input("\nEnter the Name: ")
    acc_no=Accnum()
    dob=input("Enter Date of Birth: ")
    contNo=input("Enter the contact number: ")
    add=input("Enter the address: ")
    opBal=input("Enter the opening balance: ")
    data1=(name, acc_no, dob, add, contNo, opBal)
    data2=(name, acc_no, opBal)
    sql1=("insert into account values (%s, %s, %s, %s, %s, %s)")
    sql2=("insert into amount values (%s, %s, %s)")
    x=mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Account Opened Successfully.. and your account number is -->", acc_no, " <--")
    main()

def depAmo():
    amount=int(input("\nEnter the amount you want to deposite: "))
    ac=input("Enter the account number: ")
    a='SELECT * FROM amount WHERE AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    t=result[-1]+amount
    sql=('UPDATE amount SET balance=%s WHERE AccNo=%s')
    d=(t,ac)
    x.execute(sql, d)
    mydb.commit()
    print("\nRs ", amount, " added to your bank account!")
    main()

def withdraw():
    amount=int(input("\nEnter the amount you want to withdraw: "))
    ac=input("Enter the account number: ")
    a='SELECT * FROM amount WHERE AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    if(result[-1]<amount):
        print("Balance not sufficient..")
    else:
        t=result[-1]-amount
        sql=('UPDATE amount SET balance=%s WHERE AccNo=%s')
        d=(t,ac)
        x.execute(sql, d)
        mydb.commit()
        print("Rs", amount, " removed from your bank account!")
    main()
    
def balEnq():
    ac=input("\nEnter the account number: ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    print("\nBalance for account number ", ac, " is --> ", result[-1])
    main()

def disDet():
    ac=input("\nEnter the account number: ")
    a='select * from  account where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    print("\nName: ", result[0])
    print("Account Number: ", result[1])
    print("Date of Birth: ", result[2])
    print("Address: ", result[3])
    print("Contact No", result[4])
    print("Opening Balance: ", result[5])
    main()
    
def CloseAcc():
    ac=input("\nEnter the account number: ")
    q1='delete from account where AccNo=%s'
    q2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(q1, data)
    x.execute(q2, data)
    mydb.commit()
    print("Account is closed !")
    main()
        
def main():
    print("\n\t1. Open new account\n\t2. Deposit Amount\n\t3. Withdraw Amount\n\t4. Balance Enquiry\n\t5. Display Customer Detailes\n\t6. Close an account")
    choice=input("\nEnter the task you want to perform: ")
    if(choice=='1'):
        OpenAcc()
    elif(choice=='2'):
        depAmo()
    elif(choice=='3'):
        withdraw()
    elif(choice=='4'):
        balEnq()
    elif(choice=='5'):
        disDet()
    elif(choice=='6'):
        CloseAcc()
    else:
        print("Invalid input")
        main()
main()