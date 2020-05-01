file = open("../../data/data.json","r")
string = file.read()
print(type(string))
string = "Data = \n" + string
file.close()
file2 = open("../../data/data.json","w")
#file2 = open("../../data/data.json","w")
file2.write(string)
