#list is mutable
#buliding methods of list
#we can  add elements using + or append
my_list=[12,25,"oneteam","meenakshi",14.39]
my_list.append("python")#adds the element to end
print(my_list)
#extend(must be iteratable)
my_list2=[12,25,"oneteam","meenakshi",14.39,"abc"]
my_list2.extend('dell')
print(my_list2)
my_list3=[12,25,"oneteam","meenakshi",14.39,"abc"]
my_list3.extend('1,2,3')#(67) not iteratable, also 
print(my_list3)
#insert(adds a element in that index posn)
my_list4=[12,25,"oneteam","meenakshi",14.39,"abc"]
my_list4.insert(2,'python')
print(my_list4)
#remove(does not return)
my_list5=[12,25,"oneteam","meenakshi",14.39,"abc"]
my_list5.remove(12)
print(my_list5)
#pop(returnsthe value)
my_list6=[12,25,"oneteam","meenakshi",14.39,"abc"]
my_list6.pop()
print(my_list6)
my_list6=[12,25,"oneteam","meenakshi",14.39,"abc"]
my_list6.pop(2)
print(my_list6.pop(2))
print(my_list6)
#index tells us the posn of the element
my_list7=[12,25,"oneteam","meenakshi",14.39,"abc"]
print(my_list6.index(12))
#sort
numbers=[45,15,78,1224]
numbers.sort(reverse=True)
print(numbers)
numbers2=[45,15,78,1224]
numbers2.sort()
print(numbers2)
#STRING METHODS
#
s="my name is Meenakshi ABC  ABC abc"#we can't change a particular letter or word so string is IMMUTABLE
#so in order to convert there wont be change in org
print(s.upper())
print(s.lower())
print(s)
print(s.capitalize())#only first letter is capitalized
print(s.title())#each word is capitalized
print(s.swapcase())#lower to upper, upper to lower
#split gives a list where each elemet is a sentence
print(s.split())
print(s.replace("ABC" ,"we"))
print(s.replace("ABC","we",1))
s2="$$%^my name-is Meenakshi-ABC -ABC abc"
print(s2.partition("-"))#first occurence from there it will split
print(s2.strip("$$%^"))
#gives boolean value
print(s2.isalpha())
print(s.isalpha())#even space gives false value
print(s.isdigit())
s3="123 456"
print(s3.isdigit())
s3="123456"
print(s3.isdigit())
print(s2.isalnum())
print(s3.isalnum())
