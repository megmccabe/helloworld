""" from cgi import parse_header
""" 

print("hello world!")
print ("my name is megan!")

list = ["M", "E", "G", "A", "N"]
for letter in list:
    print(letter)

numlist = [1,2,3,4,5,6,7,8,9]
print(sum(numlist))

namelist = ["owen", "megan", "abby", "winston", "Father G", "Father Campo"]

for name in namelist:
    if name == "megan":
        print(":)")

for name in namelist:
    if name.find("Father") != -1:
        print(name + " + ")

print(namelist[0])
print (namelist) 

seventySixTrombones = "big parade"
print(seventySixTrombones)