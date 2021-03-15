# open the file in read mode
file_csv = open("C:\\Users\\Antonio\\Downloads\\contacts1.csv", "r")

#open the file in write mode (create and overwrite)
file_new = open("C:\\Users\\Antonio\\Downloads\\test_py.csv", "w")

#split the red record into the element of the list for each comma divider
contenuto = file_csv.read().split(",")

print("--------------------")
new_contenuto = []
for x in contenuto:
   # save in the list only the element != space
   if x:
      new_contenuto.append(x)
      print(x)

file_new.writelines(["%s\n" % item for item in new_contenuto])

print("--------------------")

file_csv.close()
file_new.close()
