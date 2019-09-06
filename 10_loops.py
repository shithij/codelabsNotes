#Loops

#FOR

#Includes 2, excludes 6
for x in range(2, 6):
  print(x)

#Looping through each letter of a string
for x in "banana":
  print(x)

#Break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#WHILE
i = 1
while i < 6:
  print(i)
  i += 1

#break and continue in while too
