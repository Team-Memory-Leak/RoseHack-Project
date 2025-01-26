import random

englishDictionary = open("diction/EnglishDictionary", "r")
imageHash = open("diction/ImageHash", "r")
japaneseDictionary = open("diction/JapaneseDictionary", "r")

englishDictionary = englishDictionary.read().split("\n")
imageHash = imageHash.read().split("\n")
japaneseDictionary = japaneseDictionary.read().split("\n")

count = 0
historyIndex = -1

while count != 2:
  correlatedIndex = random.randint(0, len(englishDictionary))
  while correlatedIndex == historyIndex:
    correlatedIndex = random.randint(0, len(englishDictionary))
  print(imageHash[correlatedIndex])
  print(japaneseDictionary[correlatedIndex])

  option1 = random.randint(0, len(englishDictionary) - 1)
  option2 = random.randint(0, len(englishDictionary) - 1)

  while option1 == correlatedIndex or option1 == historyIndex:
    option1 = random.randint(0, len(englishDictionary) - 1)
  while option2 == correlatedIndex or option2 == option1 or option2 == historyIndex:
    option2 = random.randint(0, len(englishDictionary) - 1)

  print("Which of the following is the correct translation of the word above?")

  possibleAnswers = [englishDictionary[correlatedIndex],englishDictionary[option1], englishDictionary[option2]]
  random.shuffle(possibleAnswers)

  print(possibleAnswers[0])
  print(possibleAnswers[1])
  print(possibleAnswers[2])

  count += 1
  historyIndex = correlatedIndex
  