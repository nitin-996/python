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

input_string = input("Enter string: ")
n = int(input("Enter n: "))

# Creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets, reverse_alphabets))

# Finding the part of string on which we will do the mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# Finding the mirror string
mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

# Creating the final string
res = prefix + mirror
print("The result is:", res)




# set is mutable.
# each element in the set must be unique and they are immutable

# list and dictionary can be store bcz they are mutable.



collect = {1,2,3,4,5,6}

# to access all items from set we can use for loop

data = set()  # empty set creation


