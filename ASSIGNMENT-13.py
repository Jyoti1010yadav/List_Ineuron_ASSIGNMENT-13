# 1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using list
num=int(input("how many itens  you want to store. "))
l=[]
for  i in range (0,num):
    item=input("Enter items.")
    l.append(item)
print(l)    
print()
# 2. Write a python script to get the data type of a list.
l=["jyoti",1,"ashu",2,89.6,45,"dost"]
for i in l:
    print(i)
print()    

# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java", "C", "Python"]
print("last elements of mylist",mylist,"is ",mylist[-1])
print()

# 4. Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" 
# (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print("before change any ",thislist)
thislist[1]="NoSQL"
thislist[3]="Flutter"
print("after change ",thislist)
print()

# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]
mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append("Python")
print(mylist)
print()

# 6. Write a python program to append elements from another list to the current list.
# (firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
firstlist.extend(secondlist)
print(firstlist)
print()

# 7. Write a python program to Print all items by referring to their index number (thislist = 
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in range(len(thislist)):
    print(i,thislist[i])
print()    
# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

# 9. Write a Python script to create a list of city names taken from the user.
total_cities=int(input("Enter how many city name you want to enter "))
l=[]
for i in range(total_cities):
    city=input(" Enter city name ")
    l.append(city)
print(l)
print()

