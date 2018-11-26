bestandsnaam = input("Welk van deze bestanden wil je lezen?")
with open(bestandsnaam) as f:
    for line in f:
        woord1, woord2 = line.strip(',').split(':')
        bestandsnaam[woord1] = woord2
    print(bestandsnaam)

'''
st={'hallo': 'hello', 'hoi': 'hey', 'wiskunde': 'math'}
print (st)
keys=st.split(" | ")
print (keys)
file = open('woorden.txt', 'r')
d = {}

for item in file:
    x = item.split(" ")
    a = x[0]
    b = x[1]
    d[a] = b

print(d)
'''
'''

import csv

dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
w = csv.writer(open("output.csv", "w"))
for key, val in dict.items():
    w.writerow([key, val])

dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
w = open("output.csv", "w")
for key, val in dict.items():
    item = key, val
    woord1, woord2 = item.split(':')
    woorden = [woord1, woord2]
    resultaat = "=".join(woorden)
    w.write(resultaat)
    w.write("/n")
'''
