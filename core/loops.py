print("for loop-----------------")

number = int(input("Enter a number: "))

#for loop informing only the final delimiter using range()
for i in range(number):
    print(str(i))
else: 
    print("End of for loop!")
    
#for loop informing both initial and final delimiters using range()
for i in range(0, number):
    print(str(i))
else: 
    print("End of for loop!")

names = ['Peter', 'Adam', 'James', 'Osvald', 'Matthew']
#for loop through an array of strings using if
for i in names:
    if(i == 'Peter'):
        print('Hey ' + i + '!')
    else:
        print(i)
else: 
    print("End of for loop!")

#for loop through an array of strings using continue and break
for i in names:
    if(i == 'Peter'):
        continue
    elif(i == 'Osvald'):
        break
    else:
        print(i)
else: 
    print("End of for loop!")

print("while loop---------------")
#while loop through an array of strings
i = 0
while i < len(names):
    print(names[i])
    i += 1
else: 
    print("End of while loop!")

#while loop through an array of strings using if
i = 0
while i < len(names):
    if(i == 'Peter'):
        print('Hey ' + names[i] + '!')
    else:
        print(names[i])
    print(names[i])
    i += 1
else: 
    print("End of while loop!")

#while loop through an array of strings using continue and break
i = 0
while i < len(names):
    if(names[i] == 'Peter'):
        i += 1
        continue
    elif(names[i] == 'Osvald'):
        break
    else:
        print(names[i])
    i += 1
else: 
    print("End of while loop!")


