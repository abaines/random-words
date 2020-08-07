# Alan Baines

import os
import functools
import math

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

def round_sig(number, digits=6):
   import math
   logsize = math.log10(abs(number))
   dig = max(1,digits)-logsize-1
   # print('dig',dig,'logsize',logsize)
   return round(number,math.ceil(dig))


outputList = []
sizeMatrix = {}
maxSize = -1
graphSize = 60 # how big the max graph bar should be

for word,count in wordMatrix.items():
   size = len(word)
   if count >= minAcceptable and size>1:
      outputList.append(word)
      if size not in sizeMatrix:
         sizeMatrix[size] = 0
      sizeMatrix[size] = 1 + sizeMatrix[size]
      maxSize = max(maxSize,sizeMatrix[size])

# yay math to figure out log base to get max graph bar length given on the largest count
logbase = math.exp( math.log(maxSize) / graphSize )
print(maxSize,' -> ',logbase,' & ',round_sig( maxSize/graphSize ))
print()

for size,count in sorted(sizeMatrix.items()):
   length1 = math.log(count,logbase)
   length2 = count * graphSize / maxSize
   length = 0.5*length1 + 0.5*length2
   print(
      str(size).rjust(2,' '), # not likely to have words with more than 99 characters
      str(count).rjust(5,' '), # not likely to have more than 99,999 words of any given size
      "■"*int(length) # mmmm repeating characters!
      )
print()


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

