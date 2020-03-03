girlsList = []
girlsList.append('Ana')
girlsList.append('Diana')
girlsList.append('Alexandra')
girlsList.append('Ana')

# a
girlsList.sort()
print (girlsList)

# b
auxList = []
for name in girlsList:
    if name not in auxList:
        auxList.append(name)

for name in auxList:
    print (name + " " + str(girlsList.count(name)))

# c
occurencesList = []
for name in auxList:
    occurencesList.append(girlsList.count(name))

maxCount = max(occurencesList)
print (maxCount)

for name in auxList:
    if girlsList.count(name) == maxCount:
        print (name)

# d
occurencesList = []
for name in auxList:
    occurencesList.append(girlsList.count(name))

minCount = min(occurencesList)
print (minCount)

for name in auxList:
    if girlsList.count(name) == minCount:
        print (name)

# e
girlsList.reverse()
print (girlsList)