#Date :- 26/06/2022
#Eg 1.1 - write write a program to input a number and print its cube.
Num = eval(input("Enter Any Number :- "))
print(Num, "root is :- " ,Num**0.5)


#Eg 1.2 - write a program to input a number and print its square root.
Num = int(input("Enter any number :- "))
S_root = Num**0.3
print("Squre root of", Num, "is :- " , S_root)


#Eg 1.3 write a program that input an integer in a range of 0 to 999 and then print if the integer entered is a 1/2/3 digit numbers

Num1 = int(input("Enter any number in the range of 0-999 :- "))
Num= len(str(Num1))
if Num > 3:
    print ("Please Enter any number in the range of 0-999")
if Num ==1:
    print(Num1," number has 1 digit")
if Num ==2:
    print(Num1,"number has 2 digits")
if Num ==3:
    print(Num1,"number has 3 digits")
    
# Date :- 27/06/2022



    
