# print("hello world")
# # operator in python
# print(True and False)
# print(True or False)
# print(not True)
# 1
# a=3
# a=str(a)
# b="moksh"
# # b=int(b) {error}
# print(a)
# print(type(a),type(b))
# a=float(a)
# print(type(a),a)

# a=input("enter your age : ")
# a=int(a)
# print(a,type(a))

# #To find remainder in divension operation
# a=25
# b=10
# print(a%b)

# a=input("1st number :")
# b=input("2nd number :")
# a=int(a)
# b=int(b)
# avg=(a+b)/2
# print("avg is :",avg)

# name='''harry is my teacher
#  of python hana harry bro'''
# print("1.)",name[0])
# print("2.)",name[0:19])
# print("3.)",name[0:-10])
# print("4.)",name[0:])
# print("5.)",name[:45])
# print("6.)",name[0:45:2])
# print("7.)",type(name))
# print("8.)",len(name))
# print("9.)",name.replace("harry","moksh"))
# print("10.)",name.count("harry"))

# # string function
# print(name.endswith("bro"))
# print(name.count("r"))
# print(name.find("python"))
# print(name.find("nothing"))
# print(name.capitalize())

# a=input("Enter your teacher name :")
# b=input("Enter date when you send it :")
# c=('''
#   Dear |name|
# you are selected for celebration 

# Date:|date|
# ''')
# c=c.replace("|name|",a)
# c=c.replace("|date|",b)
# print(c)


# # list 
# f=[1,2,0,8,10,2,3]
# print(f)
# print(f[0])
# # print(f[6]) [error]

# f[0]=19 #to change value using index in list
# print(f)

# g=[45,"harry",False,89.505] # we can create list carrying different items
# print(g)
# # list indexing
# print(g[0:2])
# print(g[0:4:2])
# print(type(g))
# print(type(g[2]))

# # list method
# f.sort()
# print(f)

# f.reverse()
# print(f)

# f.append(555)
# print(f)

# f.pop(1)
# print(f)

# f.remove(0)
# print(f)

# f.insert(2,True)
# print(f)


# # tuple
# a=()#tuple with 0 element
# print(type(a))
# a=(1,)#tuple with one element
# print(type(a))
# a=(1,2,7,7,78,)#tuple with more than one element
# print(type(a))

# # tuple method
# print(a.count(7))
# print(a.index(78))

# # dictionary
# dict={
#     'harry':'teacher',
#     "moksh": "master",
#     "list": [4,45,0,455],
#     "tuple":(78,799,66,455555,0,200,6565),
#     'dict':{ "moksh": "master",
#               "javascript":True
#     }
# }
# # dictionary method
# print(type(dict))
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("list"))
# print(dict.get("unknown"))
# print(dict["list"])
# # print(dict["unknown"]) # error

# update_dict={
#     "tom":"jerry",
#     "thor":"hammer"
# }
# dict.update(update_dict)
# print(dict)


# # set
# st=set()# empty set
# print(type(st))

# st={1,2,3,4,(45,66,2),6,1,2,5}
# print(st)
# print(type(st))
# print(len(st))

# # set method
# st.add(9999999)  # can not add dictionary and list in set 
# print(st)

# st.remove(1)
# print(st)

# print(st.pop())
# print(st)

# st.clear()
# print(st)


# # dictionary ka questions 
# moksh_dictionary={
#     "fan":"Panka",
#     "pen":"kalem",
#     "Elephant":"hati",
#     "home":"ghar",
#     "boy":"ladka"
# }
# a=input("enter english word : ")
# print(moksh_dictionary[a])



# # set ka question
# hindi_bhasha={}
# lang1=input('Enter your Bhasha Ankit\n')
# lang2=input('Enter your Bhasha Anshu\n')
# lang3=input('Enter your Bhasha Renu\n')
# lang4=input('Enter your Bhasha Arpit\n')
# hindi_bhasha["Ankit"]=lang1
# hindi_bhasha["Anshu"]=lang2
# hindi_bhasha["Renu"]=lang3
# hindi_bhasha["Arpit"]=lang4
# print(hindi_bhasha)

# # conditional expertions
# # if else ladder in python 
# a=int(input("enter your age :"))
# if(a<10):
#     print("you are a Child")
# elif(a<18):
#     print("you are a teenager")
# elif(a<50):
#     print("your are a old human") 
# elif(a<100):
#     print("you are man")       
# else:
#     print("you are god")

# # logical and relational operators
# age=int(input("enter your age for work: "))
# if(age>=18 and age<=50):
#     print("you can work in our factory")
# else:
#     print("you can not work with us sorry bro ")    

# year=int(input("years of your experience :"))
# if(year>=5 or year>=4):
#     print("yes you can join")
# else:
#     print("sorry, plz get lost from my eyes") 

# slary=int(input("enter your pre income: "))
# if(not slary<=20000 ): 
#     print("sorry, you are lier ,plz get lost") 
# else:
#     print("you can join bro ...")    
 
# # is and in 
# a = None
# if (a is None):
#     print("Yes")
# else:
#     print("No")

# a = [45, 56, 6]
# print(6 in a)
# print(435 in a)

## conditional ka question
# # code the program which is determine the greater number in different number
# num1 = int(input("Enter number 1:"))
# num2 = int(input("Enter number 2:"))
# num3 = int(input("Enter number 3:"))
# num4 = int(input("Enter number 4:"))

# if(num1>num4):
#     f1=num1
# else:
#     f1=num4

# if(num2>num3):
#     f2=num2
# else:
#     f2=num3

# if(f1>f2):
#     print(f1," is greater then all") 
# else:
#     print(f2," is greater than all")
               
# # code a program which determine pass and fail 
# mark1 =int(input("Enter your Mark in Maths: "))
# mark2 =int(input("Enter your Mark in English: "))
# mark3 =int(input("Enter your Mark in Hindi: "))

# percentage=(mark1+mark2+mark3)/3
# print(percentage,"% is your percentage in SA1")

# if(mark1<33 or mark2<33 or mark3<33):
#     print("you are FAIL")
# elif(percentage>40):
#     print("result would be  PASS")
# else:
#     print("result would be  FAIL") 

# # code the program to determine the spam in text
# text=input("comment plz: ")

# if ("click it for win "):
#     spam=True
# elif("won gold"):
#     spam=True
# elif("subcribe to win "):
#     spam=True
# elif("do this to earn "):
#     spam=True
# else:
#     spam=False    

# if(spam):
#     print("This is a spam")
# else:
#     print("This is not a spam ")  

# # code  the program which find name in our records input by user
# name_check= input("enter the name : ")
# name_records=["irfan","sumit","yuvraj","vasu","rajdeep","karn"]
# if (name_check in name_records):
#     print("Yes",name_check,"is present in our record")
# else:
#     print("NO",name_check,"is not present in our record")    

# # code the program which determine the grade of the student
# sub1=int(input("Enter the mark of Maths : "))
# sub2=int(input("Enter the mark of Science : "))
# sub3=int(input("Enter the mark of Hindi : "))
# percentage=(sub1 +sub2 +sub3)/3

# if (sub1<=33 or sub2<=33 or sub3<=33):
#     print("You are Fail")
# else:
#     print("You are Pass")

# if(percentage>=90):
#     print("Grade: A+ ") 
# elif(percentage>=80 ):
#     print("Grade: A ")     
# elif(percentage>=70):
#     print("Grade: B ") 
# elif(percentage>=60 ):
#     print("Grade: C ") 
# elif(percentage>=50 ):
#     print("Grade: D ") 
# elif(percentage>=40):
#     print("Grade: E ")
# else:
#     print("Grade: F")  


# # Loop
# # while loop
# g=int(input("think a number in your mind : "))
# while g<10: # this loop will continue, stop when loop is False
#     print("Yes "+ str(g)) # we can display operation during the calculation
#     g=g+1 #we can operate this after calculation

# print("Done") #display when above is stop

# # fruite list by while loop
# fruite=["banana","mangoes","grapes","watermelon"]
# f=0
# while f<len(fruite):
#     print(fruite[f])
#     f=f+1

# # fruite list by For loop
# fruite=["banana","mangoes","grapes","watermelon"]
# for item in fruite:
#     print(item)

# # Range function
# for num in range(1,5,2):
#     print(num)

# # for with else
# for num in range(3):
#     print(num)
# else:
#     print("now this function false")    

# # break statement in for loop
# for num in range(5):
#     print(num)
#     if num==3:
#        break
# else:
#     ("now this function is false")

# # continue statement in the loop
# for num in range(5):
#     if num==3:
#         continue
#     print(num)

# # pass statement in loop
# for num in range(3):
#     pass
# print("this function is use to do nothing, Just Pass")


# # code the program in which we can type multiplication table 
# Num =int(input("Enter the number to generate its Table : "))
# for t in range(1,11):
#     print(str(Num) + " X " + str(t)+ " = "+ str(Num*t))
#     # OR
#     # print(f"{Num} X {t} = {Num*t}") # Another Way to print table 
# else :
#     print("Done")

# # code the program to detect the prime number or not 
# prime_num = int(input("Enter the number to find, is it prime number or not :"))
# for p in range(2,prime_num):
#     if (prime_num%p==0):
#         print("No, "+ str(prime_num )+" is not a prime number")
#         break
# else:
#     print("Yes, "+ str(prime_num) +" is a prime number")        

# # code the program to find factorial(!) of given number
# factorial_num = int(input("Enter the number to find its factorial :"))
# factorial=1
# # example: 4!=1x2x3x4
# for f in range(1,factorial_num+1):
#     factorial = factorial* f
# print(f"factorial of {factorial_num} is {factorial}")


# # FUNCTIONS
# # 1st way to calculate marks 
# marks0 =[98,19,79,81,29]
# percentage0=sum(marks0)/5
# marks1 =[90,89,92,1,99]
# percentage1=sum(marks1)/5
# marks2 =[78,47,92,20,10]
# percentage2=sum(marks2)/5
# print(percentage1,percentage2)

# # 2nd way to calculate marks with function
# def percent(marks):
#     return (sum(marks)/5)
# marks0 =[98,19,79,81,29]
# percentage0=percent(marks0)
# marks1 =[90,89,92,1,99]
# percentage1=percent(marks1)
# marks2 =[78,47,92,20,10]
# percentage2=percent(marks2)
# print(percentage0,percentage1,percentage2)

# # Default parameter Value
# def greeting(name="default_person"):
#     print("Good morning, "+ name)
# greeting("Moksh")
# greeting()

# # Recursive
# # 1st way to print Factorial
# factorial_bro = 4 
# product=1
# for i in range(factorial_bro):
#     product= product*(i+1)
# print(product)

# # 2nd Way to print Factorial with Function
# def factorial_iter(number):
#     product=1
#     for i in range(number):
#         product = product*(i+1)  
#     return product
# f= factorial_iter(5)
# print(f)

# # 3rd way to print Factorial with function recursive
# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial_recursive(n-1)
# f =factorial_recursive(6)
# print(f)

# # code the program which display stars in triange pattern
# n=5
# for i in range(n):
#     print(" "*(n-i+1),end="")
#     print("*"*(2*i+1),end="")
#     print(" "*(n-i-1),end="")
# # reverse tringle pattern
#     print(" "*(i),end="")
#     print("*"*(2*(n-i)-1),end="")
#     print(" "*(2*n-i-1))

# # code the program which convert celsius to fahrenheit
# def temperture(cel) :
#     return (cel*(9/5))+32
# c=int(input("Enter the temperture in celsius : "))  
# t=temperture(c)    
# print("Temperture in fahrenheite is",str(t))


# #code the game gun, water and snake
# import random
# randNo = random.randint(1,3)
# print("__________Computer: Selected its Wepone____________")
# player2=input("Your Turn: Select any one From {Gun(g) , Water(w) , Snake(s)}: ")

# if player2=="g":
#     player2=1
# elif player2=="w":
#     player2=2
# elif player2=="s":
#     player2=3    
# else:
#     print("Unwanted Error")        

# if randNo == player2:
#     print("Match is Tie")
# elif randNo==1 and player2==3:
#     print("You Loss") 
# elif randNo==2 and player2==1:
#     print("You Loss") 
# elif randNo==3 and player2==2:
#     print("You Loss")   
# elif randNo==1 and player2==2:
#     print("You Win")    
#     print("Party kb dega 🥳")
# elif randNo==2 and player2==3:
#     print("You Win") 
#     print("Party kb dega 🥳")
# elif randNo==3 and player2==1:
#     print("You Win") 
#     print("Party kb dega 🥳")    
# else:
#     print("You type:",player2, "Game performing Well")

# if randNo==1:
#     print("Because Computer select: Gun")
# elif randNo==2:
#     print("Because Computer select: Water")
# else:
#     print("Because Computer select: Snake")   

# # Made by me brother
# # game of stone paper and scissor
# import random
# replay=input("Let's Play a game snack, water and gun, yes or no: ")
# if replay=="no":
#     print("Ok bro, your bad luck")
# while (replay=="yes"):
#     randNo=random.randint(1,3)
#     if randNo==1:
#         randNo="snack"
#     elif randNo==2:
#         randNo="gun"
#     elif randNo==3:
#         randNo="water"
#     else:
#         print("Program not working code mistake was occured")
#     print("Weponse are stand with their first letter")
#     user=input("Enter your wepone: ")
#     if user=="s":
#         user="snack"
#     elif user=="g":
#         user="gun"
#     elif user=="w":
#         user="water"
#     else:
#         print("User error")
    
#     if user=="snack" and randNo=="gun" :
#         print("you loss")
#     elif user=="gun" and randNo=="water":
#         print("you loss")
#     elif user=="water" and randNo=="snack":
#         print("you loss")
#     else:
#         if user=="gun" and randNo=="snack" :
#             print("you win")
#         elif user=="water" and randNo=="gun":
#             print("you win")
#         elif user=="snack" and randNo=="water":
#             print("you win")
#         else:
#             print("tie the game")
    
#     print("Because computer select",randNo)
#     replay=input("Play it again, yes or no: ")
#     if replay=="no":
#        print("Ok Bro Nice Play") 


# # FILE I/O
# # Open function to read the file!
# f =open("sample.txt") # by deflaut read mode is active
# f =open("sample.txt",'r')# sample.txt is a file which placed in my folder
# # f =open("sample.txt",'x')
# # x=={read= r, write= w, append= a, update= +}
# data= f.read(15) # read first 15 charactor from the file
# data= f.read()
# data= f.readline() # readline function
# data= f.readline() # read 2nd line is print = called number of the file 
# # data= f.write("this is an write / append mode")
# print(data)
# f.close() # close() is important when we open any file

# # With function (No need to close like open function)
# with open('sample.txt','r') as f:# all mode are same like in open function
#     data=f.read()
#     print(data)

# # code a function which update the highscore of the game
# def game():
#     return 9990
# current_score=game()  
# with open('sample.txt','r')as s:

#     highScore=s.read()
# if highScore=='' :
#      with open('sample.txt','w')as s:
#         s.write(str(current_score)) 
#         print("Updated Score is: ",str(current_score))
# elif int(highScore)< current_score  :
#      with open('sample.txt','w')as s:
#         s.write(str(current_score))
#         print("Updated Score is: ",str(current_score))
# else:
#     print("HighScore was not break \n CURRENT HIGH SCORE:",str(highScore))

# # code the program which type table 2 to 4 in separte file
# for i in range(10,5):
#         with open(f"table_of_{i}",'w') as f:
#             for n in range(1,11):
#                f.write(f"{i}X{n}={i*n}\n") 
# print("table program is performed by you")                

# # code the program which detect python in file and display the number of line    
# content=True
# i = 1
# with open("sample.txt") as f:
#     while content :
#         content =f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"Yes , python is present in line {i}")     
#         i+=1 

# # code the program which copy the given file
# old_file="sample.txt"
# new_file="sample2.txt"
# with open(old_file,'r')as f:
#     old=f.read()
# with open(new_file,'w') as f:
#     f.write(old)    

# # code the program which detect that 2 files are identical or not
# first_file="sample.txt"
# second_file="sample2.txt"
# with open(first_file,'r') as f:
#     first=f.read()
# with open(second_file,'r')as f:
#     second=f.read()
# if first==second:
#    print("Yes, they are identical")
# else:
#     print("No, they are not identical")

# # code the program which wipe out(clean) the file completly
# wipe_file="sample.txt"
# with open(wipe_file,'w') as f:
#     print("")
# print("wipe out the sample.txt")

# # code the program which rename the file name
# import os
# a_file="sample.txt"
# b_file="renamed_by_python.txt"
# with open(a_file,'r')as f:
#     remove_name=f.read()
# with open(b_file,'w') as f:
#     f.write(remove_name)   
# os.remove(a_file)
# print("file was renamed") 


# # chapter 10 -OOPS(object oriented programming)
# # code the program which is used to store 
# # information of programer in his data by object oriented programming
# class programer:
#     company= "Microsoft"
#     def __init__(self, name, product):
#         self.name = name
#         self.product = product
        
#     def getInfo(self):
#         print(f"The name of the company {self.company}, his programer name is {self.name}, and the product is {self.product} ") 

# harry = programer("harry","Skype")
# monu =programer("monu", "GitHub")

# harry.getInfo()
# monu.getInfo()

# '''
# PascelCase
# camelCase
# '''

## we can also delete the object and object's element with this syntax
# del object_name
#       or  
# del object_element


# #Create the class with the class attribute , 
# # a create an object from it and set a directly using object a=0. 
# # Does this change the class of attribute
# class employee():
#     company='Google'
#     def getsalary(self,signature, sign):
#         print(f'this is salary of employees in {self.company} is {self.salary}\n{signature} {sign}')
#     def greet(self):
#         print("good morning , sir")
# harry=employee() #it sepcify the variable
# harry.salary=100 #it sepcify the variable      
# harry.getsalary('signature h bro','moksh ka sign')# this is call to function getsalary
# # employee.getsalary(harry) # Its second step of harry.getsalary()
# harry.greet() # this is call to function greet


# # code the program which Calculate and capable to square, squareroot and cube
# class Calculater:
#     def __init__(self, number):
#         print(f'{number} is your Number.')
#         self.number = number
#     def square(self):
#         print(f"The square of {self.number} is {self.number **2}")        
#     def squareroot(self):
#         print(f"The squareroot of {self.number} is {self.number **0.5}")     
#     def cube(self):
#         print(f"The cube of {self.number} is {self.number **3}") 
# a = Calculater(3)
# a.square()
# a.squareroot()
# a.cube()

# # code the program in which staticmethod is used
# class Calculater:
#     def __init__(self, number):     # dunder method (no need to call){__x__},x=variable
#         self.number = number
#     def square(self):
#         print(f"The square of {self.number} is {self.number **2}")        
    # @staticmethod         #after this, no need to give self as an element
#     def greet():
#         print("*******Heelo World***********")
# a = Calculater(3)
# a.greet()
# a.square()


# # code the program which is used to train registration
# class train:
#     def __init__(self,name,fare,seats): 
#         self.name = name
#         self.fare = fare
#         self.seats = seats 
#     def getstatus(self):
#         print(f"The name of the Train is {self.name}")
#         print(f"The fare of the train is Rs:{self.fare}")
#         print(f"The available seats are {self.seats} only because it is VIP Bro")
#     def bookticket(self):
#         if self.seats>0:
#            print(f"Your is ticket has been booked and your seat number is {self.seats}")  
#            self.seats=self.seats-1
#         else :
#             print("Sorry train is Full, Try in Tatkal")
# intercity=train("Intercity VIP Express :0001",90,4)    
# intercity.getstatus() 
# intercity.bookticket()
# intercity.bookticket()


# # #Inheritance
# # single Inheritance___________-
# class employee:# parent or Base Class
#     company="Google"
#     product="websites" 
# class programer(employee):#Child or Derived Class
#     company="YouTube"   
# e = employee()
# p = programer()
# print(e.company)# e have it's company name
# print(p.company)# p have it's company name
# print(p.product)# but p have not it's product like e ,so it will print his parent product which is websites

# # Multiple inheritance_______________- 
# class Employee:   # Parent_1 class
#     company="amozon"
#     pincode=122006
# class freeLens:  # parent_2 class
#     name="FREELENSER"
#     company="Fiver"
#     level=0
#     def upgrade(self):
#         self.level=self.level+1
# class programer(Employee,freeLens):# Child Class
#     name="Harry"
# e=Employee()
# f=freeLens()
# p=programer()
# print("1",p.company)
# # Company is selected by the order of parent in child class
# print("2",p.level)
# print("3",p.name)
# print("4",f.name)
# print("5",p.pincode)
# p.upgrade()
# print("6, (After upgrade)",p.level)

# # Multilevel inheritance and super() class 
# class person:
#     country="India"
#     def takebreath(self):
#         print("I am a person and i am start breathing")
# class Employee(person):
#     company="Jio"
#     def takebreath(self):
#         print("Employee: Luckily i am breathing bro")
# class programer(Employee):
#     company = "TATA"
#     def getSalary(self):
#         print("No salary is there for you")
#     def takebreath(self):
#         super().takebreath()# It will print its parent_class's takebreath first and, then it will Execute
#         print("I am a programer. So, i am breathing ")
# p=person()
# e=Employee()
# pr=programer()
# print(p.country)
# print(pr.company)
# print(e.company)
# pr.getSalary()
# pr.takebreath()# Here we have super() class
# p.takebreath()

# # class methods
# class Employee:
#     company="tesla"
#     salary=1000
#     # def changesalary(self,sal): # 1st method of class
#     #     self.__class__.salary=sal# it change an attribute in the class (donnder class)
#     @classmethod  # 2nd method of class (decorater)
#     def changesalary(cls,sal):  # work is same as 1st method 
#         cls.salary=sal # but way to code is different.
# e=Employee()
# print(e.salary) 
# e.changesalary(999)    
# print(e.salary)
# print(Employee.salary)

# # decorator
# class Employee:
#    company="Bharat Gas"
#    salary=100
#    salarybonus=4200

#    @property#getter method
#    def totalsalary(self):
#        return self.salary + self.salarybonus
#    @totalsalary.setter#setter method
#    def totalsalary(self,sal):    
#        self.salarybonus = sal-self.salary

# e=Employee()
# print(e.totalsalary)#when @property is available
# # print(e.totalsalary())#when @property decortor is not there
# e.totalsalary=5800
# print(e.salary)
# print(e.salarybonus)
# print(e.company)

# # Operator Overloading
# class Number:
#     def __init__(self,num):
#         self.num = num
#     def __add__(self,num2):
#         print("Let's Add")
#         return self.num + num2.num #1st time sum induce kraya
#     def __mul__(self,num2):
#         print("Let's Multiple")   
#         return self.num * num2.num
# #similarly __trurdiv__(/) , __sub__(-), __floordiv__(//)
# n1=Number(3)        
# n2=Number(8)
# print(n1*n2)
# print(n1+n2) #2nd time sum induce kraya that's why it called Overloading

# # __str__ Dunder method
# class Number:
#     def __init__(self,num):
#         self.num = num
#     def __add__(self,num2):
#         return self.num + num2.num
#     def __str__(self): # this is also a dunder method
#         return f"Decimal is :{self.num}"
# n1=Number(92)
# n2=Number(12)
# print(n1+n2)
# n=Number(9)
# print(n)

# # code the program by class print 2d & 3d vector 
# class c2dvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def __str__(self):
#        return f"{self.i}i + {self.j}j"
# class c3dvector(c2dvector):       
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
# v2d=c2dvector(67,89)
# v3d=c3dvector(25,3,10)
# print(v2d)
# print(v3d)        

# # code the program employee , his salary and incriment ,
# # change the salary based on incriment 
# class Employee:
#     salary=1000
#     incriment=1.5
#     @property
#     def salaryAfterincriment(self):
#         return self.salary*self.incriment
#     @salaryAfterincriment.setter           # setter
#     def salaryAfterincriment(self,sai):
#         self.incriment = sai/self.salary
# e=Employee()
# print(e.salaryAfterincriment) 
# print(e.incriment)
# e.salaryAfterincriment = 900
# print(e.incriment)

# print(__version__)