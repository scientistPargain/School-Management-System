from typing import overload
import pymysql as sqltor
from pymysql import cursors


def connectSQL(*pswrd):
    '''
    Connects you to databae 
    returns --> cursor,mycon

    cursor--> cursor object of databae
    mycon --> connection object of database

    Always close database after your work using mycon (ex- mycon.close()) 
    
    '''
    try:
        mycon= sqltor.connect(host='localhost',user = 'root',password='royal@123',database='rgnv_school' )


        cursor = mycon.cursor()
        # rowAffctd = cursor.execute(sqlcommand)  #returns no. of rows affected
        # data= cursor.fetchall()  #all data
        return cursor,mycon
    except Exception as e:
        print(e)

def sqlHeader():
    cursor,mycon = connectSQL('pass')
    cursor.execute('select * from students')
    #cursor.desription is a NoneType value without executing a sql command before it 
    header = [i[0] for i in cursor.description] #list of fields at header
    # print(header)
    mycon.close()
    return header

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
    Sex = input('ENter sex of student: ').upper()  #not null
    while Sex not in('F','M','O'):
        Sex = input('ENter sex of student: ').upper() #not null
    
    Class = int(input('ENter class: '))  # not null
    while (Class<=6 and Class >=12):
        Class = int(input('ENter class: '))  # not null
    
    HouseDict={'B':'BLUE','R':'RED','G':'GREEN','Y':'YELLOW','':''}
    House = input("ENter house: ").upper()
    while House not in ('R','B','G','Y',''):
        House = input("ENter house: ").upper()
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

    print('Do you want to enter this record')
    for x, y in zip(fields,values):
        print('{} {}'.format(x, y))

    
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

#Learn use of overload decorator
# @overload
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

# @overload
# def deleteRec(id:tuple):
#     cursor,mycon=connectSQL('anython')
#     affctedRow=cursor.execute(f"delete from students where id in {id}")
#     mycon.commit()
#     print(f"{affctedRow} records deleted")
#     mycon.close()


def srchById(srchId):
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

def srchByName(srchName):
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

def srchByHouse(srchHouse):
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

def srchByEmail(srchEmail):
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



def modify():
    '''
    To update data of students
    (require admin's permission)'''
    pass



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



while True:
    print("School Management System")
    help()

    userInp = int(input('Your choice: '))

    if userInp==1:  # Display students or their data
        print('How do you want to display record: ')
        print('[1] by id')  # using letter of first word is more convinient i.e id - [i]
        print('[2] by name')
        print('[3] by house')
        # print('[4] match phone no.')
        print('[4] Aadhar no')
        print('[5] Email')
        print('[6] father name')
        print('[7] mother name')
        print('[8] all record')
        print('[0] to go back')
        print('[99] to exit here')
        while True: 
            disInp = int(input('enter your choice: '))
            if disInp==0: # stop here or go back
                print('Funcitons will stop here')
                break

            elif disInp==1:  # by id

                userInp='y'
                while userInp=='y':
                    srchId = int(input('ENter id: '))  # restriction can be applied here to id
                    data = srchById(srchId)
                    if data!=():
                        print(sqlHeader())
                        for row in data:
                            print(row)
                    userInp=input('DO u want to check another one? (y/n): ')

            elif disInp==2: # by name
                userInp='y'
                while userInp=='y':
                    srchName = (input('ENter name: ')) # upper or lower case can matter.. change the whole to one case
                    
                    data=srchByName(srchName)
                    if data!=():
                        print('THis is running')
                        print(sqlHeader())
                        for row in data:
                            print(row)
                    userInp=input('DO u want to check another one? (y/n): ')

            elif disInp==3:  # by house
                HouseDict={'B':'BLUE','R':'RED','G':'GREEN','Y':'YELLOW','':''}
                print('Enter house:      for example \n\
                    B - Blue (Nanda) House \n\
                    R - Red (Corbett) House \n\
                    G - Green (Gangotri) House \n\
                    Y - Yellow (Rajaji) House \n')      


                userInp='y'
                while userInp=='y':
                    srchHouse = input('House: ').upper()
                    while srchHouse not in('R','B','G','Y'):
                        print('Enter valid house')
                        srchHouse = input('House: ').upper()

                    srchHouse=HouseDict[srchHouse]
                    data= srchByHouse(srchHouse)
                    if data!=():
                        print(sqlHeader())
                        for row in data:
                            print(row)
                    userInp=input('Do you wnat to check another one? (y/n): ')
                        
            # elif disInp==4:  # match phone number
                # phone= 0000000000   # 10 igits phone number
                # while not (phone>1000000000 and phone<10000000000):  # check for more accurate boundaries in internet for indian phone no.
                #     phone = int(input('Enter phone number: '))
                #     print('enter valid phone number... check and try again')
                # print(f"Phone no  {phone} --- Also check for correct phone no. and passed")

            elif disInp==4:  # by Aadhar no
                userInp='y'
                while userInp=='y':
                    srchAadhar = input('ENter Aadhar card no: ') # restriction can be applied here to aadhar no i.e 12 digits
                    while(len(srchAadhar)!=12 or  srchAadhar.isnumeric()==False):
                        print('Enter a valid Aadhar card no. !!')
                        srchAadhar = input('ENter Aadhar card no: ')
                    
                    data=srchByAadhar(srchAadhar)
                    if data!=():
                        print(sqlHeader())
                        for row in data:
                            print(row)
                    userInp=input('DO u want to check another one? (y/n): ')

            elif disInp==5:  # by Email
                userInp='y'
                while userInp=='y':
                    srchEmail = input('ENter Email: ') 
                    while (len(srchEmail.strip().split())!=1):
                        print('Enter only one and valid email !! try again')
                        srchEmail = input('ENter Email: ')

                    data=srchByEmail(srchEmail)
                    if data!=():
                        print(sqlHeader())
                        for row in data:
                            print(row)
                    userInp=input('DO u want to check another one? (y/n): ')     

            # elif disInp==6:  # by father's name
                # Father_name = input("Enter father's name of student (without Mr.) :" ).upper()
                # # now match with the database
                # print('Father name',Father_name)
            
            # elif disInp==7:  # by mother's name
                # Mother_name = input("Enter mother's name (without Mrs.) : ").upper()
                # # now match with the database
                # print('Mother name',Mother_name)
            
            elif disInp==8: # all record
                # show all record 
                sqlcommand = 'select * from students'
                cursor,mycon = connectSQL(sqlcommand)
                rowsAffected = cursor.execute('SELECT * FROM students')  #cursor object returns no. of rows affected

                print(sqlHeader())

                data = cursor.fetchall()
                if data!=():
                    for row in data:
                        print(row)
                else:
                    print('No data in database !!')
                print('Total no. of rows: ',rowsAffected)
                mycon.close()

            elif disInp==99:
                programOver()
                

    elif userInp==2:  # add new student           
        r = 0  # records entered
        userInp='y'
        while userInp=='y':
            addStu('this is pass')  #to add a student's record
            r+=1
            userInp=input('Do you want to enter more record? (y/n) : ')
        else:
            print('Total records entered: ',r)


    elif userInp==3:  # delete record
        print('Know Id then enter [1] \n \
                Know name then enter [2] \n\n\
                **Tip: Using Id is safer, names can coincide')
        userInp='y'
        while userInp=='y':
            id=int(input('enter id of student to be deleted: '))   # after taking id, display all data of user 
            data=srchById(id)
            if data==():
                print('**TIP: \nFirst display or find id you want to delete using display function and then delete it from here.\n\n Will be waiting for you...')
            else:
                for row in data:
                    print(row)
                confrmation=input(f'DO u really want to delete record of {data[0][1]} : ').lower()
                if confrmation=='n':
                    print('Not deleting')
                    break
                else:
                    print('Deleting record...')
                    deleteRec(id)

            userInp=input('Do u want to delete more records? (y/n): ')

    elif userInp==4:  # modify data
        #Also enter the last modified date in this section
        modify()

    elif userInp==5:  # for help module
        help()

    elif userInp==99:  # exit
        programOver()




