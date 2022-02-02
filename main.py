from managementFunctions import *

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
                confrmation=input(f'DO u really want to delete record of {data[0][1]} ? (y/n): ').lower()
                if confrmation=='n':
                    print('Not deleting')
                    break
                else:
                    print('Deleting record...')
                    deleteRec(id)

            userInp=input('Do u want to delete more records? (y/n) : ')

    elif userInp==4:  # modify data
        #Also enter the last modified date in this section
        ckMore='y'
        while ckMore=='y':  #repeatng if user wants to modify another record
            inpId=int(input('Enter id whose record u want to update: '))
            data=srchById(inpId)
            if data!=():
                for row in data:
                    print(row)


            entrAgain='y' #element to re-run this while at the same time on user's demand.
            while entrAgain=='y':  #repeting if user demand to modify something else
                while 1:  #repeating if user enters wrong options
                    print('WHat you would like to modify of this record.')
                    print("[1] To modify Name")
                    print("[2] To modify Class")
                    print("[3] To modify Email")
                    print("[4] To modify Father's Name")
                    print("[5] To modify Mother's Name")
                    print("[0] to go back")
                    print("[99] to exit here")
                    print('Or you can modify multiple things at a time . i.e [23] will modify class[2] and Email[3]\n or [123] will modify name[1], class[2] and email[3] ')

                    userInp = int(input("What do you want to modify: "))
                    if ("0" or "1" or "2" or "3" or "4" or "5" or "99"  in str(userInp)) and (userInp>=0 and userInp<=543210 ):
                        break
                    else:
                        print('Enter valid option!!')
                        print()
                        print("Options should be greater than 0 and less than 543210\n-> if you are trying to exit at the same time then exit in next turn without any another option.")


                if userInp==99:
                    programOver()
                if ('0' or '1' or '2' or '3' or '4' or '5' in str(userInp)) :
                    userInps=list(str(userInp))
                    print(userInps)
                    for userInp in userInps:
                        if userInp=="0":
                            break
                        elif userInp=="1":
                            modifyName(inpId)
                        elif userInp=="2":
                            modifyClass(inpId)
                        elif userInp=="3":
                            modifyEmail(inpId)
                        elif userInp=="4":
                            modifyFname(inpId)
                        elif userInp=="5":
                            modifyMname(inpId)
                        elif userInp=="99":
                            programOver()
                else:
                    print('Enter valid options!!') 

                entrAgain=input('DO you want to modify something else?(y/n) :').lower()
                if entrAgain!='y':
                    entrAgain='n'  #So that the program can terminate after this
                

            ckMore=input('Do you want to modify another record?(y/n) : ').lower()  #Asking user if he/she wants to modify another record
        
    elif userInp==5:  # for help module
        help()

    elif userInp==99:  # exit
        programOver()




