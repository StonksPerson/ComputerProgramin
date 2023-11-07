import random
import math

words = open("words.txt")
words = words.readlines()
print(words[math.floor(random.random() * 267751.0)])
print(math.floor(random.random() * 267751.0))
