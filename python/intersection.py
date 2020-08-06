# Alan Baines

import os

cwd = os.getcwd()

print("cwd",cwd)


dictionaries = []

for file in os.listdir(cwd):
   if file.endswith(".txt"):
      path = os.path.join(cwd, file)
      dictionaries.append(path)


for dictPath in dictionaries:
   print(dictPath)
   with open(dictPath, 'r') as file:
      for line in file:
         print('   ',line.strip())

