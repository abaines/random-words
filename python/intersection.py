# Alan Baines

import os
import functools

cwd = os.getcwd()

print("cwd",cwd)
print()


dictionaries = []

for file in os.listdir(cwd):
   if file.endswith(".txt"):
      path = os.path.join(cwd, file)
      dictionaries.append(path)

wordMatrix = {}

for dictPath in dictionaries:
   print(dictPath)
   privateMatrix = {}
   with open(dictPath, 'r', encoding="utf8") as file:
      c = 0
      for line in file:
         word = line.strip().lower()
         if word.isalpha():
            privateMatrix[word] = True
            if c % 1000 is 0:
               # print('   ',word)
               pass
            c = 1 + c

   print("processing private matrix", len(privateMatrix), end = '')
   for word in privateMatrix:
      if word not in wordMatrix:
         wordMatrix[word] = 0
      wordMatrix[word] = 1 + wordMatrix[word]
   print(" complete")
   print()



fileCount = len(dictionaries)
minAcceptable = fileCount - 1

print('minAcceptable',minAcceptable,'of',fileCount)

print()


outputList = []

for word,count in wordMatrix.items():
   if count >= minAcceptable:
      outputList.append(word)

def comparison(a,b):
   if len(a) == len(b):
      return 1 if a > b else -1
   else:
      return len(a) - len(b)

outputList.sort(key=functools.cmp_to_key(comparison))

with open('words.out', 'w') as output:
   for word in outputList:
      print(word, file=output)

print(len(outputList))

