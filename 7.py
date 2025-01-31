#----DICTIONARY OF PYTHON---
#---KEY:VALUE
birthday= {
    "shwetha" : "18-09-1990",
    "karthik" : "12-02-1992",
    "vaibhav" : "20-04-2018"
}
print(birthday)
#print(birthday["sudha"])  #throwing keyError means this key is not present in the dictory
#so for this kind of error in runtime not good so came up with get() method

print(birthday.get("sudha","Not found"))
print(birthday.get("vaibhav","Not found"))

#need to add new key:value to this dictory we can add runtime also
birthday["sudha"]="2020-01-01"
print(birthday)

#need to update any new value to the dictory we can update value runtime also
birthday["shwetha"]="18-09-1995"
print(birthday)

birthday.pop("shwetha")
print(birthday)


#----DICTIONARY METHODS---LIST of Dict---
dict1={"item": "Sugar",
       "weight": 2,
       "price": 100
       }
dict2={
    "item": "Rice",
    "weight":4,
    "price":150
}
dict3={
    "item":"powder",
    "weight":5,
    "price":200
}
dictory_list=[dict1,dict2,dict3]
print(f"Total weight of {dict1["weight"]+dict2["weight"]+dict3["weight"]} in Kgs")
