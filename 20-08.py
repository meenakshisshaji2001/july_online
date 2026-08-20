#set
s={12,"meenakshi",90,12}
print(s)
s.add("python")
print(s)
s.discard(12)
print(s)
s.discard(4554)
print(s)
s.add(12)
print(s)
s.pop()
print(s)
#s.remove(56)
print(s)
#s.add({9,12})#we can give iteratable elements#instead use s.update([9,12])
print(s)
#instead use
s.update([9,12])
print(s)
s1={45,12}
s2={"python",9,45}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))#elements in s1 and not in s2
#exception handling in python, prevents program from crashing when an error occurs
'''a,b=10,0#causes zero div error
a,b=10,"24"#type error
a=10#no value for b name is not specified
#so qwe give instruction '''
a,b=12,0
try:
    print(a/b)
except:
    print("u cannot divide by zero")#any error that arise it will give this 
print("completed")

a,b=12,0
try:
    print(a/b)
except ZeroDivisionError:#for build
    print("u cannot divide by zero")#any error that arise it will give this 
except TypeError:#for build
    print("please provide an integer value")
except NameError:#for build
    print("please provide correct value of b")
except:
    print("error")
print("completed")

a,b=12,"34"
try:
    print(a/b)
except ZeroDivisionError:
    print("u cannot divide by zero")#any error that arise it will give this 
except TypeError:
    print("please provide an integer value")
except NameError:
    print("please provide correct value of b")
except:
    print("error")
print("completed")

a=12
try:
    print(a/b)
except ZeroDivisionError:
    print("u cannot divide by zero")#any error that arise it will give this 
except TypeError:
    print("please provide an integer value")
except NameError:
    print("please provide correct value of b")
except:#we dont know what error is raised
    print("error")
print("completed")

a=12
try:
    print(a/b)
except ZeroDivisionError:
    print("u cannot divide by zero")#any error that arise it will give this 

except Exception as e:
    print("error",e)
else:
    print("no errors occured")
finally:
    print("completed")




