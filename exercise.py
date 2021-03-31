
# open the file in read mode
file_csv = open("contacts1.csv", "r")

#open the file in write mode (create and overwrite)
file_new_nome_file = "C:\\Users\\antonio.donato\\Downloads\\OUTPUT.csv"
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

#liste
lista1 = ["uno", "due", "tre", "quattro", "cinque"]

print("==== LIST ==========")
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
print("====================")

if "due" in lista1:
   print(lista1)

#List Comprehension
lista2 = ["Luca", "Maria", "Anna", "Andrea", "Giuditta"]
[print(x) for x in lista2 if x.__contains__("An")]

