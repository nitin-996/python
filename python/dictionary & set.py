# set and dictionary are unordered so it does not have indexing feature.
# set does not allow duplicate

# dictionary are mutable
# don't allow duplicate keys


# nested dictinary

student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
    }
}

print(student["subject"]["chem"])  # access data from nested dictionary
print(student["name"])


# logical code for reversing




# zip function = aggregate elements from two or more iterables(list,tuples,sets,etc)
# creates a zip object with paire elements dotred in tuples for each element
input_string = input("Enter string: ")
n = int(input("Enter n: "))

# Creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets, reverse_alphabets))

# Finding the part of string on which we will do the mirror operation
prefix = input_string[:n]  # Corrected slicing
suffix = input_string[n:]  

# Finding the mirror string
mirror = ""
for char in suffix:
    mirror += dict1.get(char, char)  # Using get() to handle characters not found in dict1

# Creating the final string
res = prefix + mirror
print("The result is:", res)


# dictinary comprehention ( used := can replaced for loops and certain lambda function)

# dictionary = { key: expression for (key,value) in iterable }
# dictionary = { key: expression for (key,value) in iterable if conditional}
# dictionary= { key (can put if else condition) for (key,vlue) in iterable}
# dictionary = { key: function(value) for(key,value) in iterable}
cities_in_f = {'new york':32 , "Boston": 75, "LA": 100, "chicago": 55}

cities_in_c = { key: ((value-32)*(5/9)) for ( key,value) in cities_in_f}
print(cities_in_c)
















# set is mutable.
# each element in the set must be unique and they are immutable

# list and dictionary can be store bcz they are mutable.



collect = {1,2,3,4,5,6}

# to access all items from set we can use for loop

data = set()  # empty set creation


