# open the file in read mode
file_csv = open("C:\\Users\\Antonio\\Downloads\\contacts1.csv", "r")

#open the file in write mode (create and overwrite)
file_new_nome_file = "C:\\Users\\Antonio\\Downloads\\test_py.csv"
file_new = open(file_new_nome_file, "w")

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

#print(testo.format(uno, due))

print("--------------------")

#Use format
uno = 1
due = "due"
testo = "questa una riga con dei parametri di test {0} {1}"
file_new.writelines(testo.format(uno, due))

file_csv.close()
file_new.close()

#Read file
file_open = open(file_new_nome_file, "r")
print("====================")
print(file_open.readline())
print("====================")
file_open.close()

print(testo.find("questa"))