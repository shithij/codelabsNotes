#Dictionaries

#Creating a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Getting a value
x = thisdict["model"]
print(x)

OR

x = thisdict.get("model")
print(x)

#Change values
thisdict["year"] = 2018

#printing all keys
for x in thisdict:
  print(x)

#printing all values
for x in thisdict:
  print(thisdict[x])

#length of a dictionary
print(len(thisdict))

#Adding into a dictionary
thisdict["color"] = "red"

#removing a key-value pair
thisdict.pop("model")

#copy
mydict = thisdict.copy()

#Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
