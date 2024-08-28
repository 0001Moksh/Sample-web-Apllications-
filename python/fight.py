# # Sure! Here's an example of a simple fight game in Python:

# # python
# import random

# class Character:
#     def __init__(self, name, health, attack_power):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power

#     def attack(self, opponent):
#         damage = random.randint(1, self.attack_power)
#         opponent.health -= damage
#         print(f"{self.name} attacks on {opponent.name} and deals {damage} damage!")
#         if opponent.health <= 0:
#             print(f"{opponent.name} has been defeated!")
#             return True
#         return False

# def main():
#     player = Character("your Player", 100, 20)
#     enemy = Character("Enemy", 100, 15)
    
#     while True:
#         print(f"{player.name}'s health: {player.health}")
#         print(f"{enemy.name}'s health: {enemy.health}")
#         print("1. Attack")
#         print("2. Quit")
        
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             if player.attack(enemy):
#                 break
#             if enemy.attack(player):
#                 break
#         elif choice == "2":
#             print("You quit the game.")
#             break
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()


# # In this game, there are two characters: player and enemy. Each character has a name, health, and attack power. The game continues until either the player or the enemy's health reaches zero.

# # The `attack` method randomly generates a damage value between 1 and the attacker's attack power. It deducts this damage from the opponent's health and prints a message to indicate the attack and the damage dealt.

# # The `main` function runs a loop that allows the player to choose between attacking or quitting the game. Upon attacking, the player and enemy take turns attacking each other until one of them is defeated. Choosing to quit ends the game.

# # Please note that this is a basic implementation, and you can enhance it further by adding more features, such as special abilities, items, or different enemy types.
# #  Generated by Y AI(Powered by ChatGPT-4), search Y AI at Google Play to download it

# # practice python codes
# print("ram ram brother")
# a=(12,4,55,56,7,7)
# print(type(a),"()")
# a={12,43,54,56,32,1}
# print(type(a),"{}")
# a=[12,34,54,66,77,8]
# print(type(a),"[]")
# a='harry: teacher'
# print(type(a),"''")
# a={'harry':'teacher'}
# print(type(a),"'key':'value'")
# a=True
# print(type(a),"True")
# a=None
# print(type(a),"none")
# a=1
# print(type(a),"12,32")
# a=2.3
# print(type(a),"2.3,34.5")
# a=input("Enter the name of your teacher : ")
# b="name ram ram ji sir ,kya haal h brother"
# print(b.replace("name",a))
# print(b.count("ram"))

# set={21,323,45,(267,3283,35,434),0,214,2}
# print(type(set))
# print(len(set))
# set=set.add(999)

# dict={
#     'man':'aadhme',
#     'ghar':'home'
# }
# a=input('type man bro :')
# print(dict[a])

# # set ka question
# album={}
# lang1=input("ankit ki language: ")
# lang2=input("moksh ki language: ")
# lang3=input("naveen ki language: ")
# album['ankit']=lang1
# album['moksh']=lang2
# album['naveen']=lang3
# print(album)

# age=input('enter your age: ')
# age=int(age)
# if(age<18):
#     print("your are below 18")
# elif(age<30):
#     print("your are a teenagers")
# elif(age<50):
#     print("your are older")
# else:
#     print("how can you survive bro")

# a=input("enter 1st Number: ")
# b=input("enter 2nd Number: ")
# c=input("enter 3rd Number: ")
# a=int(a)
# b=int(b)
# c=int(c)

# if(a>b and a>c):
#     print("a is greater")
# elif(b>c and b>a):
#     print("b is greater")
# elif(c>b and c>a):
#     print("c is greater")
# else:
#     print("all are equal")

# # while Loop
# g=int(input('enter a number: '))
# while g<=10:
#     print(" Input became",g)
#     g=g+2

# # for loop 
# range=[132,24,34,545,453,3]
# for a in range:
#     print(a)
# else:
#     print("loop is completed")

# for a in range(9):
#     print(a)
#     if a==4:
#        break
# else:
#     print("ram ram brother")

# for a in range(9):
#     print(a)
#     if a==1:
#        continue 
# else:
#     print("ram ram brother")

# pno=int(input("enter the number to check whether it is a prime or not :"))
# for n in range(2,pno):
#     if(pno%n==0):
#         print("No it is not a prime number")
#         break
# else:
#     print("yes it is prime number")

# # factorial 
# fact=int(input("Enter the number: "))
# ft=1
# for n in range(1,fact+1):
#     ft=ft*n
# print(ft)

# def percent(marks):
#     return print(sum(marks)/3)
# marks1=int(input("maths: "))
# marks2=int(input("science: "))
# marks3=int(input("hindi: "))
# marks=(marks1,marks2,marks3)
# percent(marks)

# def greeting(name="defualt name"):
#     print("Good morning",name)
# name=input("Enter the name: ")
# greeting(name)
# greeting()

# def factorial(number):
#     product=1
#     for i in range(number):
#         product=product*(i+1)
#     return product
# f=int(input("enter the number to calcualate the factorial: "))
# print(factorial(f))

# # to calculate the temperture
# def temp(num):
#     return (num * 9/5) + 32 
# given_temp=int(input("Enter the temperture: "))
# f=temp(given_temp)
# print(f)

# import tensorflow as tf

# # Define a function to take three numbers as input from the user
# def get_numbers():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     num3 = float(input("Enter the third number: "))
#     return num1, num2, num3

# # Get the numbers from the user
# num1, num2, num3 = get_numbers()

# # Define TensorFlow constants for the three numbers
# tf_num1 = tf.constant(num1, dtype=tf.float32)
# tf_num2 = tf.constant(num2, dtype=tf.float32)
# tf_num3 = tf.constant(num3, dtype=tf.float32)

# # Define the sum operation
# sum_op = tf.add_n([tf_num1, tf_num2, tf_num3])

# # Create a TensorFlow session and run the sum operation
# with tf.Session() as sess:
#     result = sess.run(sum_op)
#     print(f"The sum of {num1}, {num2}, and {num3} is: {result}")

# #multiplidcation table of user's number
# def table(num):
#     for n in range(1,11):
#         print(num,"X",n,"=",n*num)
# number=int(input("Multiplication table of: "))
# table(number)

# # strip remover program
# def string(word,sentence):
#     c=sentence.replace(word,"")
#     return c.strip()
# sent="      ram ram bhai sara ne   "
# print(string("bhai",sent))

# # star pattern upper tringle
# def pattern(times):
#     for n in range(0,times):
#         print("*" * (times-n))
# a=int(input("enter the number: "))
# pattern(a)

# # star pattern lower triangle
# def pattern(times):
#     for n in range(0,times):
#         print(" "*(times-n), end="")
#         print("*"*(2*n+1))
# a=int(input("enter the number of line you need:"))
# pattern(a)

# # game of stone paper and scissor
# import random
# replay=input("Let's Play a game snack, water and gun, yes or no: ")
# if replay=="no":
#     print("Ok bro, your bad luck")
# while (replay=="yes"):
#     randNo=random.randint(1,3)
#     print(randNo)
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

# # file management 
# f=open("sample2.txt","a")
# data=f.write("i appending bro \n")
# print(data)
# f.close()

# with open("sample2.txt") as f:
#     data=f.read()
#     print(data)

# # file contain moksh word , yes or not
# f=open("sample2.txt","r")
# data=f.read()
# if ("moksh"):
#     print (data)
# else:
#     print("No , file didn't contain this word")

# # updater score file
# f=open('sample2.txt',"r")
# data=f.read()
# data=int(data)
# print(type(data))
# highScore=int(input("Enter your score: "))
# f=open("sample2.txt","w")
# if ():
#     highScore=str(highScore)
#     data=f.write(highScore)
#     print("Updated Broo")
# elif data < highScore:
#     highScore=str(highScore)
#     data=f.write(highScore)
#     print("Updated Broo")
# else:
#     print("Your score didn't break our high score \n try next time broo ")

# # Multiplication table generater from 2 to 20
# froms=int(input("form: "))
# to=int(input("to: "))
# froms=int(froms)
# to=int(to)
# for i in range(froms,to+1):
#     i=str(i)
#     f=open(f"multi_table{i}.txt","w")
#     for n in range(1,11):
#         i=int(i)
#         multi=n*i
#         i=str(i)
#         n=str(n)
#         multi=str(multi)
#         data=f.write(f"{i} X {n} = {multi}\n")
#     print(i+" ka table Done.")

# # replace donkey type word from the given file
# bad_word_list="donkey"
# f=open("sample2.txt","r")
# data=f.read()
# # data=str(data)
# if bad_word_list in data:
#     print("bad word is exist")
#     bad=input("do you want to replace this bad word: ")
#     if bad=="yes":
#         f=open("sample2.txt","w")
#         replace_with=input("With which word bro: ")
#         data = data.replace(data,replace_with)
#         data=f.write(data)
#         print("Update Done")
#     elif bad=="no":
#         print("Ok brother , i will not replace this word,\nas per your requirment  ..")
#     else:
#         print("Error found, Just write yes or no")
# else:
#     print("bad word is not exist, Thank to God Bro")

# # rename program
# import os
# old="sample.txt"
# new=input("Rename the file: ")
# new+".txt"
# f=open(old,"r")
# data=f.read
# f=open(new,"w")
# content=f.write(data)
# print(data)
# os.remove(old)

# # to get the selected word in file with line no.
# content=True
# f=open("sample2.txt",'r')
# i=1
# while content:
#     content=readline()
#     if 'pyhton' in content.lower():
#         print(f"yes python is exist in this file at {i} line")
# i+=1

# # program to get information of employee using class and objects
# class information():
#     company="Microsoft"
#     def __init__(self):
#         print("Morning Sir")
#     def name(self,name):
#         print(f"Name of Employee: {name}")
#     def salary(self,salary):
#         print(f"Experience of the employee: {salary}")
# request=input("do you want to apply for \nthe Job of AI engineer in microsoft company \n yes or no: ")
# i=1
# while request == "yes":
#     if "yes":
#        print(f"Employee_No.{i}")
#        employees1=information()    
#        names=input("Enter your name: ")
#        salarys=input("Enter your experience: ")
#        employees1.name(names)
#        employees1.salary(salarys)
#        i+=1
#        request=input("Any more employee is present to request, yes or no: ")
#        if request == 'no':
#         print(f"ok fine approx {i-1} is applied in this company")
#     elif(request == "no"):
#         print(f"ok fine approx {i-1} is applied in this company")
#     else:
#         print("Request decision error try again")
#         request=input("Any more employee is present to request, yes or no: ")
# if request=="no":
#     print(f"ok fine approx {i-1} is applied in this company")
# else:
#     print("Request decision error try again")

# # program to get the information from the user and transfer to other file as an record 
# f=open("Employee_record.txt","w")
# class information_collector():
#     def __init__(self):
#         print("Good Morning Sir")
#     def introduction(self,name,year_old,phone_number):
#         data=f.write(f"{name} is {year_old} year old,\nPhone no.{phone_number}.\n")
#     def about_thier_family_back_ground(self,member,total_income_generated,cast):
#         data=f.write(f"He has {member} member in family \nTotal income of his family is {total_income_generated},\nand his cast is {cast}.\n")
#     def qualification(self,tenth_result,twenth_result,course,mark_in_course,known_english):
#         data=f.write(f"He score in 10th class is {tenth_result},\nHe score in 12th class is {twenth_result},\nHe did {course} course and his score is {mark_in_course},\n{known_english}, English.\n")
#     def intro_other_company(self,experience,post,other_company,pre_salary):
#         data=f.write(f"He has {experience} year of experience in {other_company} company as an {post}. He had {pre_salary} salary.\n")
#     def need_from_us(self,salary_acceptation,which_post):
#         data=f.write(f"He apply for the post of {which_post} and his salary acceptation is {salary_acceptation}.\n\n\n")

# request=input("Good morning Sir \nwe hope you are feeling well,\nDo want to apply for the job in our company, Microsoft pvt.limited \nyes or no: ")
# i=1
# while request == "yes":
#     if "yes":
#        print(f"Employee_No.{i}")
#        employees1=information_collector()    
#        names=input("     Enter your name: ")
#        year_olds=input("     Age: ")
#        phone_numbers=input("     Enter your Phone no.: ")

#        members=input("     How many member in your family: ")
#        total_income_generateds=input("     Net Income of your family: ")
#        casts=input("     Your Cast: ")

#        tenth_results=input("     marks in 10th standard: ")
#        twenth_results=input("     marks in 12th standard: ")
#        courses=input("     Which Course you had done: ")
#        mark_in_courses=input("     Marks in Course: ")
#        known_englishs=input("     Do you know English, yes or no: ")

#        other_companys=input("     Your previous Company name: ")
#        posts=input("     At which Post:")
#        experiences=input("     Your experirence in this company: ")
#        pre_salarys=input("     What is your previous Salary: ")

#        salary_acceptations=input("     How much will you accept salary from us: ")
#        which_posts=input("     For which Post had you apply: ")
       
#        employees1.introduction(names,year_olds,phone_numbers)
#        employees1.about_thier_family_back_ground(members,total_income_generateds,casts)
#        employees1.qualification(tenth_results,twenth_results,courses,mark_in_courses,known_englishs)
#        employees1.intro_other_company(experiences,posts,other_companys,pre_salarys)
#        employees1.need_from_us(salary_acceptations,which_posts)

#        i+=1
#        request=input("Good morning Sir \nwe hope you are feeling well,\nDo want to apply for the job in our company, Microsoft pvt.limited \n yes or no: ")
#        if request == 'no':
#         print(f"ok fine approx {i-1} number of employees are applied in this company")
#     else:
#         print("Request decision error try again")
#         request=input("Any more employee is present here to request, yes or no: ")
# if request=="no":
#     print(f"ok fine approx {i-1} is applied in this company")
# else:
#     print("Request decision error try again")

# data=f.write("\n________________Record occured__________________")/

# # tensor flow code
# import tensorflow as tf
# hello= tf.constant("Ram ram")

# with tf.compat.v1.Session() as sees:
#     result=sees.run(hello)
#     print(result.decode())