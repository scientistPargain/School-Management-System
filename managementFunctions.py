# from overloading import *
from multipledispatch import dispatch
import pymysql as sqltor
from tabulate import tabulate

def connectSQL(*pswrd):
    '''
    Connects you to databae 
    returns --> cursor,mycon

    cursor--> cursor object of databae
    mycon --> connection object of database

    Always close database after your work using mycon (ex- mycon.close()) 
    
    '''
    try:
        passw=input("enter the password")
        mycon= sqltor.connect(host='localhost',user = 'root',password=passw,database='rgnv_school' )


        cursor = mycon.cursor()
        # rowAffctd = cursor.execute(sqlcommand)  #returns no. of rows affected
        # data= cursor.fetchall()  #all data
        return cursor,mycon
    except Exception as e:
        print(e)

def createDB():
    '''
    To create a database rgnv_school if not exists in the computer.'''
    try:
        print('Connecting to sql...')
        cursor,mycon = connectSQL()

        #  Table structure for table 'students'
        
        print('Creating database...')
        cursor.execute('create database rgnv_school;')
        cursor.execute('use test_school;')
        cursor.execute("CREATE TABLE `students` (  `ID` int NOT NULL,  `Name` char(25) NOT NULL,  `Sex` char(1) NOT NULL,  `Class` int NOT NULL,  `House` char(6) DEFAULT NULL,  `Aadhar_no` varchar(12) DEFAULT NULL,  `DOB` date DEFAULT NULL,  `Email` char(30) DEFAULT NULL,  `Father_name` char(30) DEFAULT NULL,  `Mother_name` char(30) DEFAULT NULL,  `Entry_date` datetime DEFAULT CURRENT_TIMESTAMP,  `Last_modified` datetime DEFAULT CURRENT_TIMESTAMP,  PRIMARY KEY (`ID`),  CONSTRAINT `students_chk_1` CHECK ((`Sex` in (_utf8mb4'M',_utf8mb4'F',_utf8mb4'O'))),  CONSTRAINT `students_chk_2` CHECK ((`Class` between 6 and 12)),  CONSTRAINT `students_chk_3` CHECK ((`House` in (_utf8mb4'RED',_utf8mb4'BLUE',_utf8mb4'GREEN',_utf8mb4'YELLOW',_utf8mb4'')))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
        mycon.commit()
        mycon.close()
        print('\nCompleted !!!')
        print('Databae test_school created successfuly.')
    except Exception as e:
        print(e)

def sqlHeader():
    cursor,mycon = connectSQL('paass')
    cursor.execute('select * from students')
    #cursor.desription is a NoneType value without executing a sql command before it 
    header = [i[0] for i in cursor.description] #list of fields at header
    # print(header)
    mycon.close()
    return header

# Addition functions

def addStu(*paswrd):
    '''
    To insert data of new student into database
    (require admin's permission)

    [Name, I.D.,sex, Class, House, Aadhar_no, DOB, Email,Father_name, Mother_name, Ph No., Address, Entry_date, Last_modified]

    "Plan is to create a list of above format every time an insert that into the table with each run using this function"
    '''
    
    # ID = int(input('ENter I.D.: '))  # Cannot use ID as a variable inside a function bcoz according ot vs code it is a constant
    ID = int(input('ENter I.D.: '))  #not null
    Name = input('ENter name: ')  #not null
    Sex = input('ENter sex of student(m/f): ').upper()  #not null
    while Sex not in('F','M','O'):
        Sex = input('ENter sex of student again(m/f): ').upper() #not null
    
    Class = int(input('ENter class(6-12): '))  # not null
    while not (Class>=6 and Class <=12):
        Class = int(input('ENter class Again(6-12): '))  # not null
    
    HouseDict={'B':'BLUE','R':'RED','G':'GREEN','Y':'YELLOW','':''}
    House = input("ENter house(r,b,g,y): ").upper()
    while House not in ('R','B','G','Y',''):
        House = input("ENter house Again  (r,b,g,y): ").upper()
    House=HouseDict[House]
    # else:
        # if House!= '':
        #     dataOrder.append('House') 
        #     stuDat.append(House)

    # PhNo= int(input('enter Phone no.: '))

    Aadhar_no = input('Enter aadhar no. : ')
    while ((Aadhar_no.isalnum() ==False or len(Aadhar_no)!=12) and Aadhar_no!=''):
        Aadhar_no = input('Enter aadhar no. : ')
    # else:
    #     if Aadhar!='':
    #         dataOrder.append('Aadhar_no') 
    #         stuDat.append(Aadhar)

    # DOB= input('Enter date of birth : ')
    Email = input('Enter email address : ')
    # if Email!='':
    #     dataOrder.append('Email') 
    #     stuDat.append(Email)
    Father_name = input("Enter Father's name (without Mr.): ")
    # if Father_name!='':
    #     dataOrder.append('Father_name') 
    #     stuDat.append(Father_name)
    Mother_name = input("Enter Mother's name (without Mrs.): ")
    # if Mother_name!='':
    #     dataOrder.append('Mother_name') 
    #     stuDat.append(Mother_name)

    sampleData=['ID','Name','Sex','Class','House','Aadhar_no','Email','Father_name','Mother_name']

    '''# stuData= {key:eval(value) for (key,value) in zip(sampleData,sampleData) if eval(value)!=''} ''' # append not null values into the list and then convert it into tuple  --using dict comprehensions here
    
    stuData={}
    for key in sampleData:
        if eval(key)!='':
            stuData[key] =eval(key)

    fields,values=list(stuData.keys()), list(stuData.values())  #individual  lists of fields and values entered by user

    
    # for x, y in zip(fields,values):
    #     print('{} {}'.format(x, y))
    printTabular(values,fields)

    finlInp=input('Do you want to enter this record?(y/n)')
    if finlInp=='y':
        # FINAL RECORD INSERTION TO DATABASE

        # finalSqlCmn = "INSERT INTO STUDENTS(var1,var2,var3,...varN) VALUES(val1,val2,val3,...valN);"   #var1,var2 must be without inverted commas

        adSqlCmnd= f"INSERT INTO STUDENTS("
        for i in fields:
            adSqlCmnd+=i+','
        finalSqlCmnd = adSqlCmnd[:-1] + f") VALUES{tuple(values)};"  #removing last comma(,) of adSqlCmnd string which it get in for loop
        print(finalSqlCmnd)
        try:
            cursor,mycon = connectSQL(adSqlCmnd)
            rowsEntrd=cursor.execute(finalSqlCmnd)
            mycon.commit()
            print('Entered ',rowsEntrd,'rows')
        except Exception as e:
            print(e)
            addStu('pass')
        finally:
            mycon.close()
    else:
        print('Not entering record.')

# Deletion functions
#Learn use of overload decorator
@dispatch(int)
def deleteRec(id:int ):
    '''
    To delete data of any student 
    (require admin's permission)
    '''
    cursor,mycon = connectSQL('anything')
    affctedRow=cursor.execute(f"DELETE FROM STUDENTS  WHERE ID ={id}")
    mycon.commit()
    print(f'{affctedRow} record deleted for id {id}')
    mycon.close()

@dispatch(tuple)
def deleteRec(id:tuple):
    '''Delete every id in that tuple that found in db'''
    #If entering tuple, enter more than 1 element

    cursor,mycon=connectSQL('anython')
    affctedRow=cursor.execute(f"delete from students where id in {id}")
    mycon.commit()
    print(f"{affctedRow} records deleted")  #find a way to know which id is not deleted or found in the database from given tuple
    mycon.close()

# Search Functions
@dispatch(int)
def srchById(srchId:int):
    '''
    Returns data(tuple) of searched id
    and returns empty tuple if notihing matching found in database
    '''

    cursor,mycon = connectSQL('select * from students')
    cursor.execute(f'select * from students where id={srchId};')
    data = cursor.fetchall()
    if data==() or data==[]:  #checks if data is a empty list or not ---bcoz whenever nothing will be found in database, it will return empty tuple or list.
        print('No matching id found as ',srchId)
    mycon.close()
    return data

@dispatch(tuple)
def srchById(srchId:tuple):
    '''
    Returns data(tuple) of searched ids
    and returns empty tuple if notihing matching found in database
    '''

    cursor,mycon = connectSQL('select * from students')
    cursor.execute(f'select * from students where id in{srchId};')
    print(f'select * from students where id in{srchId};')
    data = cursor.fetchall()
    if data==() or data==[]:  #checks if data is a empty list or not ---bcoz whenever nothing will be found in database, it will return empty tuple or list.
        print('No matching id found as ',srchId)
    mycon.close()
    return data

def srchByName(srchName:str):
    '''
    Returns data(tuple) of searched name
    and returns empty tuple if notihing matching found in database
    '''
    cursor,mycon = connectSQL('select * from students')
    cursor.execute(f"select * from students where name='{srchName}';")
    data = cursor.fetchall()
    if data==() or data==[]:  #checks if data is a empty (tuple or list) or not ---bcoz whenever nothing will be found in database, it will return empty set or list.
        print('No matching Name found as ',srchName)
    mycon.close()
    return data

def srchByHouse(srchHouse:str):
    '''
    Returns data(tuple) of searched house
    and returns empty tuple if notihing matching found in database
    '''
    cursor,mycon = connectSQL('select * from students')
    cursor.execute(f"select * from students where house='{srchHouse}';")
    data = cursor.fetchall()
    if data==() or data==[]:  #checks if data is a empty list or not ---bcoz whenever nothing will be found in database, it will return empty set or list.
        print('No matching House found as ',srchHouse)
    mycon.close()
    return data

def srchByAadhar(srchAadhar):
    '''
    Returns data(tuple) of searched Aadhar
    and returns empty tuple if notihing matching found in database
    '''
    cursor,mycon = connectSQL('select * from students')
    cursor.execute(f"select * from students where Aadhar_no='{str(srchAadhar)}';")
    data = cursor.fetchall()
    if data==() or data==[]:  #checks if data is a empty list or not ---bcoz whenever nothing will be found in database, it will return empty set or list.
        print('No matching Aadhar no. found as ',srchAadhar)

    mycon.close()
    return data

def srchByEmail(srchEmail:str):
    '''
    Returns data(tuple) of searched Email
    and returns empty tuple if notihing matching found in database
    '''
    cursor,mycon = connectSQL('select * from students')

    cursor.execute(f"select * from students where Email='{srchEmail}';")
    data = cursor.fetchall()
    if data==() or data==[]:  #checks if data is a empty list or not ---bcoz whenever nothing will be found in database, it will return empty set or list.
        print('No matching email found as ',srchEmail)

    mycon.close()
    return data


# Modify Functions
def modifyName(id:int):
    data=srchById(id)
    for row in data:
        print(row)
        print(f"Currently name is {row[1]}.")

    name = input("New Name : ").strip()
    cursor,mycon = connectSQL()
    cursor.execute(f"Update students set name='{name}' where id = {id};")
    mycon.commit()
    print(f'Record updated!! \nSuccesfully modified name to {name}.')
    mycon.close()

def modifyClass(id:int):
    # Try to auto increment this after 1 year through python if user passes and delete if user fails.
    data=srchById(id)
    for row in data:
        print(row)
        print(f'Currently {row[1]} is in class {row[3]}.')

    while True:
        cls = int(input("Enter new class: "))
        if (cls>=6 and cls <=12):
            cursor,mycon = connectSQL()
            cursor.execute(f"Update students set Class={cls} where id = {id};")
            mycon.commit()
            mycon.close()
            print(f'Record updated!! \nNew class set to {cls}')
            break
        else:
            print('Enter a valid class b/w 6 to 12')
            print()
            continue
        

def modifyEmail(id:int):
    data=srchById(id)
    for row in data:
        print(row)
        print(f"Currently email of {row[1]} is {row[7]}.")

    while True:
        email = input("Enter new email: ").strip()
        if ('@' in email) and (len(email.split())==1):
            cursor,mycon = connectSQL()
            cursor.execute(f"Update students set email='{email}' where id = {id};")
            mycon.commit()
            mycon.close()
            print(f"Record succesfully updated!! \nNew email set as {email}")
            break
        else:
            print('Invalid email')
            print('\nCheck if you have written correct email with "@" symbol ')
            print('Check if there is any space in email written by you.')
            print()
            break

def modifyFname(id:int):
    data=srchById(id)
    for row in data:
        print(row)
        print(f"Currently Father's name of {row[1]} is {row[8]}.")

    Fname = input("Enter Father's name to modify: ").strip()
    cursor,mycon = connectSQL()
    cursor.execute(f"Update students set Father_name='{Fname}' where id = {id};")
    mycon.commit()
    print(f"Record updated!! \nSuccesfully modified Father's name to {Fname}.")
    mycon.close()

def modifyMname(id:int):
    data=srchById(id)
    for row in data:
        print(row)
        print(f"Currently Mother's name of {row[1]} is {row[9]}.")

    Mname = input("Enter Mother's name to modify: ").strip()
    cursor,mycon = connectSQL()
    cursor.execute(f"Update students set Mother_name='{Mname}' where id = {id};")
    mycon.commit()
    print(f"Record updated!! \nSuccesfully modified Mother's name to {Mname}.")
    mycon.close()


# Help functions
def help():
    '''
    Prints help
    '''
    print("[1] to display all students")
    print('[2] to add new student')
    print('[3] to delete record')
    print('[4] to modify record ')
    print('[5] help')
    print('[99] to exit')

def programOver():  # thhings u want to do when program ends.
    '''
    to finish the program here'''
    print('thanks for using our software')
    exit()

def printTabular(tabular_data:tuple, header:list):
    '''
    Prints the data beautifully in tabular format as displayed in sql
    
    tabular_data=> tuple data or tuple of tuples returned by sql 
    header=> list you want as heading
    '''
    print()
    print(tabulate(tabular_data,header,tablefmt='psql'))


