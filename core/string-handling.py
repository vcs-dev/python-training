firstName = "John"
lastName = "Doe"
#string concatenation
print("John " "Doe")
print(firstName + " " + lastName)

#single quoted sentence with character scape \
sentence = 'I don\'t know anything about that.'
print(sentence)
#double quoted sentence (doesn't need character scape)
sentence = "I don't know anything about that."
print(sentence)
#creating a string using using * to reppeat the value
reppeatedString = "hey" * 8
print(reppeatedString)

#array of strings
strings = ['My', 'Name', 'Is', 'John', 'Doe']
print(strings)
#acessing indexes
print(strings[0])
print(strings[:3])
print(strings[3:])
#including a new string at the end of the array
strings.append('!')

#nested arrays of strings
strings2 = ['My', 'Name', 'Is', 'John', 'Doe']
strings.append(strings2)
print(strings)