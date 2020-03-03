class Employe:
    nom = ''
    prenom = ''
    telephone = ''
    responsabilites = []

    def printMotto (self):
        print('This is my motto')

emp1 = Employe()
emp1.nom = "Popescu"
emp1.prenom = "Andrei"
emp1.telephone = "12345"
emp1.responsabilites = ['task1', 'task2']

print (emp1.nom)
print (emp1.prenom)
print (emp1.telephone)
print (emp1.responsabilites)
emp1.printMotto()

emp2 = Employe()
emp2.nom = "Popescu"
emp2.prenom = "Andrei"
emp2.telephone = "32145"
emp2.responsabilites = ['task3', 'task4']

print (emp2.nom)
print (emp2.prenom)
print (emp2.telephone)
print (emp2.responsabilites)
emp2.printMotto()

emp3 = Employe()
emp3.nom = "Georgescu"
emp3.prenom = "Adriana"
emp3.telephone = "23145"
emp3.responsabilites = ['task5', 'task4']

print (emp3.nom)
print (emp3.prenom)
print (emp3.telephone)
print (emp3.responsabilites)
emp3.printMotto()

