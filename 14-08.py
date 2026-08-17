#list_pgm
my_list=["oneteam",9,34,"kochi",67,89.12,'python']
#          0       1 2   3      4  5      6
print(my_list[3])
#take multiple elements in consideration, slicing
print(my_list[2:5])
print(my_list[:6])
print(my_list[3:])
print(my_list[:])
print(my_list[1:6:2])
print(my_list[::2])

print(my_list[-2:2:-1])
print(my_list[5:0:-1])
print(my_list[-3:])
#list using func
#def is_palindrome(text):
#list comprehension
numbers=[45,899,6,45,5,45,48]

evens=[]
for num in numbers:
    if num%2==0:
        evens=evens+[num]
print(evens)
#or
evens=[num for num in numbers if num%2==0]
