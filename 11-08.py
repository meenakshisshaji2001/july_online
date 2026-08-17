#function-calls the program whenever required we dont need to repeat every time requiredits keyword is def followed by function name():
def greet():
    print("hello world,welcome")
greet()#calling the function
#say two numbers or two name to be added or printed but not same different every time
def greet(name,age):#inside function-parameters, scope refers to the area it can be used
    print(f"hello{name},you are {age} years old")
greet("meenakshi",25)#inside is knopwn as arguments/positional arguments
greet("sindhu",26)
greet(25,"meenakshi")#position or order is very imp
#default argument
def welcome_note(name,age,place="unknown"):
    print("name:",name)
    print("age:",age)
    print("place:",place)
welcome_note("meenakshi",25)
#keyword argument
def welcome_note(name,age,place="unknown"):
    print("name:",name)
    print("age:",age)
    print("place:",place)

welcome_note(age=25,name="meenakshi")
#args and kwargs
def add(a,b,c):
    print(a+b+c)

add(12,5,3)#we donot know how many nmbers are to be added 
#args,*,here not knowing the number of elments to be added we 
def add(*args):
    total=0
    for num in args:
        total+=num
    print(total)
add(12,5,3)
add(25,78,98)
#kwargs,**,keyvalue is used i.e keyvalue along with its assigned value is printed on the dictionary
def greet(**kwargs):
    print(kwargs)

greet(name="Akash",age=29,place="Kochi")
greet(age=23,name="Reshma")
#in fuction, return keyword is used , why is it used 
# write a function to check whether a number is even or odd
def is_even(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")

is_even(26)
is_even(25)