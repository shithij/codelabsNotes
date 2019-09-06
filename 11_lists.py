# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#lists

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

#Accessing elements
print(thislist[1])

#Negative indexing
print(thislist[-1])

#Range of indices
print(thislist[2:5])

#Range of negative indices
print(thislist[-4:-1])

#Adding elements at an index
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

#Looping through the list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Check if an element exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Length of list
print(len(thislist))

#Appending (Will add at the end always)
thislist.append("orange")

#Adding an element in the index of your choice
thislist.insert(1, "orange")

#Removing an element from list
thislist.remove("banana")

#Removing an element by its index. By default the last element will be popped
thislist.pop(1)

#Copying a list to another
mylist = thislist.copy()

######CAN'T DO mylist = thislist as any change made to one list will change the other too

#Joining 2 lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Adding from one list to another using loops
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Constructor to make a list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


