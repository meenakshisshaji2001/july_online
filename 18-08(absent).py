student={"name":"Akash","place":"Kochi"}
# print(student['name'])
print(student.get("age","Key not found"))

# student['age']=29
student.update({"age":29,67:12,'Hobbies':["Coding","Travel"]})
print(student)

print(student.pop(67))

print(student)

print(student.popitem())
print(student)

print(student.values())

'''for k in student.values():
    print(k)'''
print(student.items())

t=(45,9,34,72,1)

print(t.count(34))#ow many times does 34 come
print(t.index(72))

print(sorted(t,reverse=True))
print(min(t))
print(max(t))
print(len(t))

list_size=int(input("Enter the list size : "))
numbers=[]
for n in range(list_size):
    num=int(input("Enter the number : "))
    numbers=numbers+[num]
print("List before sorting : ",numbers)

for i in range(list_size):
        for j in range(0, list_size - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("List after sorting : ",numbers)