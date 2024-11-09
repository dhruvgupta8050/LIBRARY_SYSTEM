CHAPTER-1

INTRODUCTION
This chapter gives an overview about the aim , objectives ,background and operation environment, project benefits of the system.
1.1 PROJECT AIM
The project aims and objectives that will be achieved after completion of this project are discussed in this subchapter. The aims and objectives are as follows: 

•	Computerized book issue 
•	Request column for librarian for providing new books 
•	A separate column for digital library 
•	Teacher login page where Teacher can find books issued and date of return. 
•	A search column to search availability of books  
•	Automatic calculate fine for student and also for if student paid the money  
•	Saved Data for Long Time


1.2 BACKGROUND OF PROJECT 

Library Management System is an application which refers to library systems which are generally small or medium in size. It is used by librarian to manage the library using a computerized system where he/she can record various transactions like issue of books, return of books, addition of new books, addition of new students etc.                 
Books and student maintenance modules are also included in this system which would keep track of the students using the library and also a detailed description about the books a library contains. With this computerized system there will be no loss of book record or member record which generally happens when a non-computerized system is used. 
In addition, report module is also included in Library Management System. If user’s position is admin, the user is able to generate different kinds of reports like lists of students registered, list of books, issue and return reports. 
 
All these modules are able to help librarian to manage the library with more convenience and in a more efficient way as compared to library systems which are not computerized. 
                 
1.3 OPERATION ENVIRONMENT 
 
 
PROCESSOR 	INTEL CORE PROCESSOR FOR BETTER PERFORMANCE 
OPERATING SYSTEM 	WINDOWS VISTA ,WINDOWS7, UBUNTU 
MEMORY 	1GB RAM OR MORE 
HARD DISK SPACE 	MINIMUM 3 GB FOR DATABASE USAGE FOR FUTURE 
DATABASE 	MY SQL 


CHAPTER-2
SYSTEM IMPLEMENTATION

2.1 GANTT CHART
![image](https://github.com/user-attachments/assets/02ad8694-33b2-4657-9d38-6821495bb049)
CHAPTER-3
 
SYSTEM ANALYSIS
 
 
In this chapter, we will discuss and analyze about the developing process of Library Management System including software requirement specification (SRS) and comparison between existing and proposed system . The functional and nonfunctional requirements are included in SRS part to provide complete description and overview of system requirement before the developing process is carried out. Besides that, existing vs proposed provides a view of how the proposed system will be more efficient than the  existing one.  
	
3.1 	SOFTWARE REQUIREMENT SPECIFICATION 
3.1.1 GENERAL DESCRIPTION 
 
PRODUCT DESCRIPTION: 
Library Management System is a computerized system which helps user(librarian) to manage the library daily activity in electronic format. It reduces the risk of paper work such as file lost, file damaged and time consuming. It can help user to manage the transaction or record more effectively and timesaving. 
 
PROBLEM STATEMENT: 
The problem occurred before having computerized system includes: 
•	File lost
When computerized system is not implemented file is always lost because of human environment. Sometimes due to some human error there may be a loss of records. 

•	File damaged 
When a computerized system is not there file is always lost due to some accident like spilling of water by some member on file accidentally. Besides some natural disaster like floods or fires may also damage the files.
•	Difficult to search record
When there is no computerized system there is always a difficulty in searching of records if the records are large in number .
 
•	Space consuming 
After the number of records become large the space for physical storage of file and records also increases if no computerized system is implemented. 

•	Cost consuming 
As there is no computerized system the to add each record paper will be needed which will increase the cost for the management of library. 

3.1.2 SYSTEM OBJECTIVES
•	Improvement in control and performance  
The system is developed to cope up with the current issues and problems of library .The system can add user, validate user and is also bug free. 

•	Save cost 
After computerized system is implemented less human force will be required to maintain the library thus reducing the overall cost. 


•	Save time 
Librarian is able to search record by using few clicks of mouse and few search keywords thus saving his valuable time. 


•	Option of online Notice board 
Librarian will be able to provide a detailed description of  workshops going in the college as well as in nearby colleges .


•	Lecture Notes 
Teacher  have a facility to upload lectures notes in a pdf file having size not more than 10mb .
 
3.1.3 SYSTEM REQUIREMENTS 
3.1.3.1NON FUNCTIONAL REQUIREMENTS 

 Product Requirements 
EFFICIENCY REQUIREMENT 
When a library management  system will be implemented  librarian and user will easily access library as searching and book transaction will be very faster . 
                                                                                                                                                                       
RELIABILITY REQUIREMENT 
The system should accurately performs member  registration ,member validation , report generation, book transaction and search  
 
USABILITY REQUIREMENT 
The system is designed  for a user friendly environment so that student and staff of library can perform the various tasks  easily and in an effective way. 
 
ORGANIZATIONAL REQUIREMENT IMPLEMENTATION REQUIREMNTS 
In implementing whole system it Tkinter in client side and  phpMyAdmin as server side scripting language which will be used for database connectivity and the backend i.e. the database part is developed using PyMySQL. 
 




DELIVERY REQUIREMENTS 
The whole system is expected to be delivered in six months of time with a weekly evaluation by the project guide. 

3.1.3.2 FUNCTIONAL REQUIREMENTS 
1.NORMAL USER 
 
1.1	USER LOGIN 
Description  of   feature 
This feature used by the user to login into system. They are required     to  enter user id and password before they are allowed to enter the system .The user id and password will be  verified and if invalid id is there user is allowed to not enter the system. 
 
 
Functional requirements 
-user id is provided when they register  
-The system must only allow user with valid id and password to enter    the system  -The system performs authorization process which decides what user level can access to. 
-The user must be able to logout after they finished using system. 
 
1.2	REGISTER NEW USER 
  Description of feature 
This feature can be performed by all users to register new user to create account. 
 
Functional requirements 
-System must be able to verify information 
-System must be able to delete information if information is wrong 
 
1.3	REGISTER NEW BOOK 
Description of feature 
This feature allows to add new books to the library  Functional requirements 
-System  must be able to verify information 
-System must be able to enter number of copies into table. 
-System must be able to not allow two books having same book id. 
 
1.5   SEARCH BOOK 
 
DESCRIPTION OF FEATURE 
This feature is found in book maintenance part . we can search book based on book id  , book name  ,  publication  or by author name. 
 
Functional requirements 
-	System must be able to search the database based on select search type 
-	System must be able to filter book based on keyword entered 
-	System must be able to show the filtered book in table view 
 
 
1.5  ISSUE BOOKS AND RETURN BOOKS 
 
 DESCRIPTION OF FEATURE  
This feature allows to issue  and return books  and  also view reports of book issued. 
 
Functional requirements 
-System must be able to enter issue information in database. 
-System  must be able to update number of books. 
-System must be able to search if book is available or not before issuing  books 
-System should be able to enter issue and return date information 
     
1.6 EVENT ADDITION 
 
DESCRIPTION OF FEATURE
This feature allows teacher and student to add information about various workshops being conducted in college and colleges nearby. 
 
 
Functional requirements 
-System should be able to add detailed information about events . 
-System should be able to display information on notice board available in the homepage of site  
 
3.2.1SOFTWARE AND HARDWARE REQUIREMENTS
This section describes the software and hardware requirements of the   system 
3.2.1.2 SOFTWARE REQUIREMENTS 
•	Operating system- Windows 7 is used as the operating system as it is stable and supports more features and is more user friendly 
•	Database  MYSQL-MYSQL is used as database as it easy to maintain and retrieve records by simple queries which are in English language which are easy to understand and easy to write. 
•	Development tools and Programming language- Python is used to write the whole code  and make dynamic use  with  Tkinter  for styling work and pymysql  for sever side scripting. 
        3.2.3.3 HARDWARE REQUIREMENTS 
	Intel core i5 2nd generation is used as a processor because it is fast than other processors an provide reliable and stable  and we can run our pc for longtime.  By using this processor we can keep on developing our project without any worries. 
	Ram 1 gb is used as it will provide fast reading and writing capabilities and will in turn sup
 
3.3 	EXISTING VS PROPOSED SYSTEM
i.	Existing system does not have any facility of teachers login or student login whereas  proposed system will have a facility of  student login as well as teacher’s login 
ii.	Existing system does not have a facility of online reservation of books whereas proposed system has a facility of  online reservation of books 
iii.	Existing system does not have any facility of online notice board where description of workshops happening in our college as well as nearby colleges is  being provided. 
iv.	Existing system does not has any option of lectures notes uploaded by teachers whereas proposed system will have this facility 
v.	Existing system does not have any facility to generate student reports as well book issue reports whereas proposed system provides  librarian with a tool to generate reports 
vi.	Existing system does not has any facility for book request and suggestions where as in proposed system after logging in to their accounts student can request books as well as provide suggestions to improve library 
 
3.4 	SOFTWARE TOOLS USED 
   The whole project is based on the Tkinter, python, and MySQL.
3.4.1 Tkinter 
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
The Tk class is instantiated without arguments. This creates a toplevel widget of Tk which usually is the main window of an application. Each instance has its own associated Tcl interpreter.
	3.4.2 Python
		Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation.
3.4.3 Python Modules
	A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.  
CHAPTER-4
SYSTEM IMPLEMENTATION:-
Student Details:-
 ![image](https://github.com/user-attachments/assets/8c1c4ee5-218b-4c31-ba0e-184a32f78349)
 BOOK DETAILS:-
![image](https://github.com/user-attachments/assets/8bdb3f1f-2b9e-403e-be30-420cd66ab60d)
ADD BOOKS:-
![image](https://github.com/user-attachments/assets/2aa445cc-2083-461d-8133-02a7f0d95db5)
ADD STUDENTS:-
![image](https://github.com/user-attachments/assets/0f5922c6-9cb3-495d-a237-0b7e0849a696)
CALCULATE FINE UPDATE:- 
![image](https://github.com/user-attachments/assets/41392cb9-ef7c-4de9-9d5b-12685d04e123)
CHECK BOOK LIST FOR STUDENT ISSUE :- 
![image](https://github.com/user-attachments/assets/a7606c0d-3b80-47d5-8842-baf7a638b31e)

 DELETE STUDENTS DETAILS: - 
 ![image](https://github.com/user-attachments/assets/b94f243d-fdf0-4924-bcad-8e227d537029)
STUDENTS USER LOGIN:-
![image](https://github.com/user-attachments/assets/db049e6b-beb3-49e1-b65a-664df5e9aef9)
Admin Area:-
![image](https://github.com/user-attachments/assets/17d8d535-27aa-438d-b90a-78d72abd6d38)
4.2 MODULE DESCRIPTION
4.2.1 Admin Login:-
	![image](https://github.com/user-attachments/assets/0abb3361-0933-4a1c-8a8c-0fc2c47cf26d)
4.2.2 ADMIN AREA:-
![image](https://github.com/user-attachments/assets/a4988051-fcd5-4373-9c29-defe2e23371b)
4.3 ER Diagram:- 
![image](https://github.com/user-attachments/assets/36a0a18e-2fe0-4d70-ba51-3a773e026a16)



 CHAPTER-5

  CONCLUSION & FUTURE SCOPE


 
This Software provides a computerized version of library management system which will benefit the students as well as the staff of the library. 
It makes entire process online where student can search books, staff can generate reports and do book transactions. It also has a facility for Faculty login where Faculty can login and can see status of books issued as well request for book or give some suggestions. It has a facility of teacher’s login where teachers can add lectures notes and also give necessary suggestion to library .
 
There is a future scope  of this facility that many more features such as online lectures video tutorials can be added by teachers as well as online assignments submission facility , a feature Of group chat where students can discuss various issues of engineering  can be added to this project thus making it more interactive more user friendly and  project which fulfills each users need in the best way possible .
 





 CHAPTER 6 

 REFERENCES 

•       Code With Harry

 

•       https://www.w3schools.com/python/


•	https://www.tutorialspoint.com/python/python_modules.htm


•	https://pypi.org/


•	http://www.techaccess.co.in/


•	https://pypi.org/project/PyMySQL/


•	https://numpy.org/


•	https://docs.python.org/3/library/tkinter.html


•	Yashwant Kanethkar Python Book

								This Product is Maded by DHRUV GUPTA





	
