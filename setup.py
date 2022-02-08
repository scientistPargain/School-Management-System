


'''
MySQL COPY Database

A database is an application used for storing the organized collection of records that can be accessed and manage by the user. It holds the data into tables, rows, columns, and indexes to quickly find the relevant information.

MySQL copy or clone database is a feature that allows us to create a duplicate copy of an existing database, including the table structure, indexes, constraints, default values, etc. Making a duplicate copy of an original database into a new database is very useful when accidentally our database is lost or failure. The most common use of making a duplicate copy of the database is for data backups. It is also useful when planning the major changes to the structure of the original database.

In MySQL, making the clone of an original database is a three-step process: First, the original database records are dumped (copied) to a temporary file that holds the SQL commands for reinserting the data into the new database. Second, it is required to create a new database. Finally, the SQL file is processed, and the data will be copied into the new database.

We need to follow these steps to copy a database to another database:

-First, use the CREATE DATABASE statement to create a new database.
-Second, store the data to an SQL file. We can give any name to this file, but it must end with a .sql extension.
-Third, export all the database objects along with its data to copy using the mysqldump tool and then import this file into the new database.
For the demonstration, we will copy the testdb database to testdb_copy database using the following steps:

Open the MySQL console and write down the password, if we have set during installation. Now we are ready to create a duplicate database of testdb using the command below:
[CREATE DATABASE testdb_copy;]


Now, open a DOS or terminal window to access the MySQL server on the command line. For example, if we have installed the MySQL in the C folder, copy the following folder and paste it in our DOS command. Then, press the Enter key.
[CD C:\Program Files\MySQL\MySQL Server 8.0\bin   ]

In the next step, we need to use the mysqldump tool to copy the database objects and data into the SQL file. Suppose we want to dump (copy) the database objects and data of the testdb into an SQL file located at D:\Database_backup folder. To do this, execute the below statement:
[D:\Database_backup\testdb.sql  ]

The above statement instructs mysqldump tool to log in to the MySQL database server using the username and password and then exports the database objects and data of the testdb database to D:\Database_backup\testdb.sql. It is to note that the operator (>) used for exporting the database from one location to another.

In the next step, we need to import the D:\Database_backup\testdb.sql file into testdb_copy database. To do this, execute the below statement:
[ D:\Database_backup\testdb.sql  ]

(It is to note that the operator (<) used for importing the database from one location to another.)

MySQL COPY Database
Finally, we can verify whether the above operation is successful or not by using the SHOW TABLES command in the MySQL command-line tool:
[SHOW TABLES;  ]


copied from : https://www.javatpoint.com/mysql-copy-database

'''
# import time
# import os

# # install requirements.txt from this file 
# print('\nInstalling requrements, please wait and do not quit...')
# print()
# try:
#     os.system('pip install -r requirements.txt')
#     print('\nSuccesfully installed all requirements.')
# except Exception as e:
#     print(e)
#     print('\nTry installing manually, or run setup.py again.')

from managementFunctions import connectSQL
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


