print("hello world!")
print ("my name is megan!")

list = ["M", "E", "G", "A", "N"]
for letter in list:
    print(letter)

numlist = [1,2,3,4,5,6,7,8,9]
print(sum(numlist))

namelist = ["owen", "megan", "abby", "winston", "Father G", "Father Campo"]

for name in namelist:
    if name is "megan":
        print(":)")

for name in namelist:
    if name.find("Father") is not -1:
        print(name + " + ")

print(namelist[0])