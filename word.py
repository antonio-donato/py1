import docx
nda = docx.Document("NDA.docx")

sections = nda.sections
print("The document contain")
print("{0} sections".format(len(sections)))

paragraphs = nda.paragraphs
print("{0} paragraphs".format(len(paragraphs)))

# for p in paragraphs:
#     print(p.text)
#     print("-"*50)

myList = []
firstLast = [paragraphs[0], paragraphs[-1]]
secondthird = paragraphs[3:70:10]
newList = secondthird.copy()

print(id(secondthird))
print(id(newList))


# for p in newList:
#     print(p.text)
#     print("-"*50)
