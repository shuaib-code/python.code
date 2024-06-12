import itertools as its
words = "MamunTsi" #Selectable characters
r =its.product(words,repeat=10) #Form 8-bit string
# dic = open("MamunTasin.txt", "a") #stored as wifi password dictionary
#wifi password complete line break and write to txt file
x = 0
for i in r:
     # dic.write("".join(i))
     # dic.write("".join("\n"))
     x = x + 1
     print(x)
# dic. close()

print(x)