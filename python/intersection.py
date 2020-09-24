# Alan Baines

import os
import functools
import math
import sys

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
minAcceptable = fileCount - 0

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

# 0 for linear scale
# 1 for log scale
hybridRatio = 0.5

for size,count in sorted(sizeMatrix.items()):
   lengthLog = math.log(count,logbase)
   lengthLinear = count * graphSize / maxSize
   length = (hybridRatio)*lengthLog + (1-hybridRatio)*lengthLinear
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


# number of desired output words
desiredWords = 10000

# make a map of all the words, keyed on their hash value
hashWords = {}
for word in outputList:
   h = hash(word)
   if h not in hashWords:
      hashWords[h] = []
   hashWords[h].append(word)

# sort the hash words keys
hashWordsKeys = sorted(hashWords)

# select the first desired count of words
reducedList = []
def getReducedList():
   for h in hashWordsKeys:
      words = hashWords[h]
      for word in words:
         reducedList.append(word)
         if len(reducedList)>=desiredWords:
            return
getReducedList()
# this should give us the 1000 words with the smallest hashes

print(len(outputList), len(reducedList),len(reducedList) /  len(outputList))
print()

# write 'words.out' to disk
with open('words.out', 'w') as output:
   for word in reducedList:
      print(word, file=output)
print()

print("EOF")

