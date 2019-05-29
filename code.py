#packages required by the program
import random
import sqlite3
import sqlite3 as It
import sys
import os.path


global price#variable which can be used by all the functions


price=random.randint(10, 100)#initialising the variable with a random value


ausername='admin'#credentials for the admins
apassword='admin'#they are not stored in the database


#if statement that checks if the database files don't exist,
#in which case it creates new ones
if (not os.path.isfile('drivers.db')or(not os.path.isfile('clients6.db'))or(not os.path.isfile('payment.db'))):
    conn = sqlite3.connect("drivers.db")#creates the database file
    cursor = conn.cursor()#enable checking the database records
    cursor.execute("""CREATE TABLE drivers
    (user text, passs text, name text, phone text, email text)
 """)   #sql statement to create the table
    print('Created Database drivers')#message that the table was created
    conn = sqlite3.connect("clients6.db")#creates the database file
    cursor = conn.cursor()#enable checking the database records
    cursor.execute("""CREATE TABLE clients
    (user text, passs text, name text, phone text, address text)
 """)#sql statement to create the table
    print('Created Database clients')#message that the table was created

    con = It.connect('clients6.db')#connects to the table


    conn=sqlite3.connect('payment.db')#creates the database file
    cursor=conn.cursor()#enable checking the database records
    cursor.execute("""CREATE TABLE payment(amount int)""")#sql statement to create the table
    print('Created database payment')#message that the table was created
elif(os.path.isfile('drivers.db')):#if the database already exists
    con = It.connect('drivers.db')#connects to the table
    with con:#opens the connection, and after the block is executed it automatically closes the connection
        cur = con.cursor()#enable checking the database records
        cur.execute('SELECT * FROM drivers')#sql statement to get data from the table
        rows = cur.fetchall()#fetches all the rows from the table
    con.close()#closes the connection to the database
#the next elif statement is exactly the same as the one above, except is for a different database
elif(os.path.isfile('clients.db')):
    con = It.connect('clients.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM clients')
        rows = cur.fetchall()
    con.close()
    print('Read Database')
#elif statement like the one above, does exactly the same thing
elif(os.path.isfile('payment.db')):
    con = It.connect('payment.db')
    with con:
        cur=con.cursor()
        cur.execute('SELECT * FROM payment')
        rows=cur.fetchall()
    con.close
    
else:#end of if statement
    print()#print a blank line


def Run():#start of the program
    print('1) Login as customer')#options menu
    print('2) Login as driver')
    print('3) Register as customer')
    print('4) Register as driver')
    print('5) Login as administrator')
    print('6) Exit')
    choice=input('Make a choice: ')#gets the user input and assigns it to a variable
    if(choice=='1'):#if the user presses 1
        LogInCustomer()#the program goes to the login function for the customer
    elif(choice=='2'):#if the user presses 2
        LogInDriver()#go to the login driver function
    elif(choice=='3'):#if the user presses 3
        RegisterCustomer()#go to the register customer function
    elif(choice=='4'):#if the user presses 4
        RegisterDriver()#go to the register driver function
    elif(choice=='5'):#you get the point
        LoginAdmin()
    elif(choice=='6'):
        quit()#exits the program
    else:#if the user chooses an invalid option
        choice=input('Make a choice: ')#the program goes back to the beginning

def LogInCustomer():#the customer log in 
    user=input('Enter your username: ')#ask the customer for its username
    passw=input('Enter your password: ')#ask the customer for its password
    print()#print a blank line
    conn = sqlite3.connect("clients6.db")#connects to the clients table
    cursor = conn.cursor()#enable checking the database records
    cursor.execute("SELECT * FROM clients WHERE user= ? AND passs= ?",(user, passw))#check if the username and password match with the database
    data = cursor.fetchone()#fetches  the row needed from the table and assigns it to the data variable
    if data is None:#if the information in the database is not the same with the customer input
        print('The user does not exist or password does not match')#print an error message
        print('')#print a blank line
        LogInCustomer()#go back to the start of the function
    else:
        print('User %s authenticated %s' % (user, data[0]))#if the information matches
        CustomerMainMenu()#goes to the main menu
    con.close()#closes the connection to the database
    conn.commit()#sends a COMMIT statement to mysql, so that all the statements are processed

def LoginAdmin():#the admin log in function
    user=input('Enter your username: ')#asks for the username
    passw=input('Enter your password: ')#asks for the password
    if(user==ausername and passw==apassword):#if the two variables set at the beginning of the program match the user's input
        AdminMainMenu()#go to the admin main menu
    else:#if the credentials do not match
        LoginAdmin()#go back to the beginning of the function
   
def LogInDriver():#function for when the driver logs in
    user = input('Please the username: ')#asks for the username
    passs = input('Please enter your password: ')#asks for the password
    conn = sqlite3.connect("drivers.db")#connects to the drivers table
    cursor = conn.cursor()#enable checking the database records
    cursor.execute("SELECT * FROM drivers WHERE user= ? AND passs= ?",
                    (user, passs))))#check if the username and password match with the database information
    data = cursor.fetchone()#fetches  the row needed from the table and assigns it to the data variable
    if data is None:#if the information in the database is not the same with the customer input
        print('The user does not exist or password does not match')#print an error message
        print('')#print a blank line
        
        LogInDriver()#go back to the beginning of the function
    else:#if the details are correct
        print('User %s Authenticated %s' % (user, data[0]))#if the information matches
        DriverMainMenu()#go to the driver main menu
    conn.commit()#sends a COMMIT statement to mysql, so that all the statements are processed
        

def RegisterCustomer():
    print ('Please Register: ')
    print('')
    user = input('Enter Username: ')
    passs = input('Enter Password: ')
    name = input('Enter Name: ')
    phone = input('Enter Phone: ')
    address = input('Enter Address: ')
    conn = sqlite3.connect("clients6.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients VALUES (?, ?, ?, ?, ?)", (user, passs, name, phone, address))
    conn.commit()
    print('Registered')
    print('')
    CustomerMainMenu()

def RegisterDriver():
    print('Please Register: ')
    print('')
    user = input('Enter Username: ')
    passs = input('Enter Password: ')
    name = input('Enter Name: ')
    phone = input('Enter Phone: ')
    email = input('Enter Email: ')
    conn = sqlite3.connect("drivers.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO drivers VALUES (?, ?, ?, ?, ?)", (user, passs, name, phone, email))
    conn.commit()
    print('Registered')
    print('')
    DriverMainMenu()

def CustomerMainMenu():
    print('Welcome to SkyLaundry')
    print()
    print('1) Schedule clothes collection')
    print('2) Reserve a locker')
    print('3) Exit')
    choice=input('Make your choice: ')
    if(choice=='1'):
        ScheduleCollection()
    elif(choice=='2'):
        ReserveLocker()
    elif(choice=='3'):
        quit()
    else:
        CustomerMainMenu()

def DriverMainMenu():
    conn = sqlite3.connect("clients6.db")
    cursor = conn.cursor()
    address=cursor.execute("SELECT address FROM clients")
    data = cursor.fetchone()
    print('Welcome')
    print()
    print('1)Collection orders')
    print('2)Delivering orders')
    print('3)Exit')
    choice=input('Make your choice:')
    if(choice=='1'):
        print('An order has to be picked up at',data)
        DriverMainMenu()
    elif(choice=='2'):
        print('An order has to be delivered to', data)
        DriverMainMenu()
    elif(choice=='3'):
        quit()
    else:
        choice=input('Make your choice:')
        
def ScheduleCollection():
    conn = sqlite3.connect("clients6.db")
    cursor = conn.cursor()
    address=cursor.execute("SELECT address FROM clients")
    data = cursor.fetchone()
    print()
    print('We need your address in order to pick up and send back your laundry.')
    print('We will collect your laundry from ', data)
    print()
    weight=input('What is the weight of your laundry?')
    if(weight=='1')or(weight=='2')or(weight=='3')or(weight=='4')or(weight=='5')or(weight=='6')or(weight=='7')or(weight=='8')or(weight=='9'):
        print('The minimum amount we can process is 10 Kg')
        print()
        ScheduleCollection()
    else:
        print()
        print('You have over 10 Kg of laundry.')
        print('You will now be sent to the payment menu')
        Do10Kg()
        ScheduleCollection()
    
def Do10Kg():
    PrintBill()
    print('Your laundry weighs over 10 Kg')
    print('Would you like to pay now?')
    print('1)Yes')
    print('2)No')
    choice=input('Choose: ')
    if(choice=='1'):
        PayBill()
    elif(choice=='2'):
        print('You have chosen not to pay')
        CustomerMainMenu()
    else:
        choice=input('Choose: ')
        #CustomerMainMenu()


def PrintBill():
    print()
    print('You have £',price,' to pay')

def PayBill():
    print()
    print('You have £',price, ' to pay')
    cnum=input('Enter your credit card number: ')
    ccode=input('Enter your security code: ')
    print('The bill has been paid!')
    price2=0
    print()
    CustomerMainMenu()

def PayLockerBill():
    price2=price+15
    print()
    print('You have £',price2, ' to pay')
    cnum=input('Enter your credit card number: ')
    ccode=input('Enter your security code: ')
    print('The bill has been paid!')
    price2=0
    print()
    CustomerMainMenu()

def ReserveLocker():
    lockernum=random.randint(1,100)
    print()
    print('Please deposit your laundry in locker',lockernum)
    print('It will be ready for collection in maximum 24 hours')
    price2=price+15
    print('You have £',price2,'to pay. Would you like to pay now?')
    print('1)Yes')
    print('2)No')
    choice=input('Choose:')
    if(choice=='1'):
        PayLockerBill()
    elif(choice=='2'):
        print('You have chosen not to pay now')
        CustomerMainMenu()
    else:
        choice=input('Choose:')

def AdminMainMenu():
    print('Welcome back,',ausername)
    print('Main Menu')
    print('1)Pay Driver')
    print('2)Exit')
    choice=input('Choose:')
    if(choice=='1'):
        AdminPayDriver()
    elif(choice=='2'):
        quit()
    else:
        choice==input('Choose:')

def AdminPayDriver():
    con=It.connect('drivers.db')
    with con:
        cur=con.cursor()
        cur.execute('SELECT user FROM drivers')
        rows=cur.fetchall()
       # for x in rows:
           # print(x)
    print()
    driver=random.choice(rows)
    print('The following driver needs to be paid:', driver)
  
    amount=input('Enter the amount you wish to pay:')
    print('You are paying', driver,'£',amount)
    print('1)Yes')
    print('2)No')
    choice2=input('Is this correct?')
    if(choice2=='1'):
        print()
        print('The payment has been made!')
        AdminMainMenu()
    elif(choice=='2'):
        AdminPayDriver()
    else:
        choice2=input('Is this correct?')
    con.close()
        
    
Run()
