from overloading import overload
import pymysql as sqltor


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
    cursor,mycon = connectSQL('paass')
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



