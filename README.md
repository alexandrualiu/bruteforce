# Bruteforce
## This is a python project I used to learn python

***I used this project to go through the language syntax, classes and multithreading and NOT to crack any file. In this description I will just try to explain how the project is structured and not how it should be used***

**Because I have no idea how the python applications should be structured and which are the best practices I have just tried to simulate DI and OOP as I normally use it in C#**

## main.py
This is the entry point of the program where the services are instantiated 

## clients.py
This is the class that does the work - it loads the arguments and decides what to execute - to generate passwords or to try to crack the files. If you want to test you laptop you can do both :-) 

## xlsx
This is the folder where the excel files should reside

## data
This is the folder where the passwords are generted 

## conf
This folder should include different settings of the app

### config.py
Settings class has properties for data, xlsx folders and what characters to use when generating passwords

## services
This folder includes all the services used

### passgen.py
This is PassGenerator class which gets the string. The **get_all** method returns all the combinations of the given letters for a specific length

### repo.py
This is the FileRepository. I use this class to add and read passwords from text files. 

### passwordchecker.py
This is PasswordChecker class and it has check_password method. This should be used in multiple threads that's why I had to use all the **pythoncom** Any suggestion to this method is wellcomed 

