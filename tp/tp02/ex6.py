bd = {
    "Sara": "12345",
    "Maria": "54321",
    "Alexandra": "23415",
    "Teodora": "34125"
}

name = input("Please enter a name: ")

while name != "stop":
    try:
        print (bd[name])
        name = input("Please enter a name: ")
    except KeyError:
        print ("Je ne connais pas cette personne")
        name = input("Please enter a name: ")