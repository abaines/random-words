# Alan Baines

import os

cwd = os.getcwd()

print("cwd",cwd)


dictionaries = []

for file in os.listdir(cwd):
   if file.endswith(".txt"):
      path = os.path.join(cwd, file)
      dictionaries.append(path)

wordMatrix = {}

for dictPath in dictionaries:
   print(dictPath)
   with open(dictPath, 'r') as file:
      for line in file:
         word = line.strip()
         print('   ',word)
         if word not in wordMatrix:
            wordMatrix[word] = 0
         wordMatrix[word] = 1 + wordMatrix[word]

print(wordMatrix)

fileCount = len(dictionaries)

# print(fileCount)

print()

for word,count in wordMatrix.items():
   if count >= fileCount:
      print(word)

