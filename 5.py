#---------LIST IN  PYTHON---------------

fruits=["apple","grapes","kiwi","orange"]
#fruits.insert(2,"banana")
#fruits.append("Drangon fruite")
#fruits.pop(2)
print(fruits)
#checking membership in list
print("banana" in fruits)

#slicing of list
number=[1,2,4,3,5,7]
print(number[0:3])
print(number[::2])
print(len(number))
number.sort() #ascending oder
#print(number)
number.reverse() #reverse order first i done sort asecending then done reverse so will get desceding order
print(number)

#common methods
number=[1,2,3,1,3,1,1]
print(number.count(3))  #count()
print(number.count(1))
print(number.index(1))

#-------------TUPLES IN PYTHON-------------------

my_tuple=("coffee","milk","sugar","rice")
print(my_tuple)
print(my_tuple[1]) #accessing particular tuple element
print(my_tuple[0:2])  #silicing from where to where silice= [start:stop:step]
#Tuple operations:
#we can add mutiple tuples using concatention
tuple1=(1,2,3,2,4,6)
tuple2=(2,4,5,6,7)
combined_tuple=tuple1+tuple2 # we can add mutiple tuples using concatentio
print(combined_tuple)

#tuple repetation same tuple repeat multiple times simillar way of items repeat
tuple_new=(1,2,3)
print(tuple_new*4)


#-----SETS IN PYTHON-----------------------

my_set={1,2,3,4,5}
s1={1,2,4,5}
s2={2,3,5,1,6}
#rint(s1|s2)  #--union operation  o/p: 1,2,3,4,5,6
#rint(s1&s2)  #--intersection operation  o/p:1,2,5
#rint(s1-s2)  #--difference operation  o/p: 4

#----SET METHODS---
s1.add(9)
#peint(s1)
s2.remove(2)
s2.pop()
print(s2)
