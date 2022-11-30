#String
str1 = "Hello World"
str2 = "Shovik"
print(str1[0])# output H
print(str2[-1])# output k

#substring
print(str1[0:3]) # 3rd index will not include output- hel

#find
str ="attachment"
a= str.find("me") # output - 6
print(a)

#replacement
print(str.replace("me","m")) #output - attachmnt
print(str.replace("ment",""))  #output - attach

#split
splitstr= "Word1.Word2.Word3"
print(splitstr.split(".")) #output - split at where "."- 'word1','word2','word3'

#count
str  = "Cococnut"
print(str.count("C")) #output- 1 bcz capital c is one

#upper
str1 = str.upper()
print(str1.count("C")) #output- 3 bcz capital c is 3

#max
str2 = "!aAAAbBBd"
print(max(str2)) #outpu - d max ascii value count
print(min(str2)) #output - ! min ascii value
