#concatenation
mytuple = ('a','b','c','d')
mytuple1 =  ('d','e')
mytuple += mytuple1 ## output -a,b,c,d,e
print(mytuple)
print(mytuple*2)

#indexing
print(mytuple[1])

#slicing
print(mytuple[2:4])

#list
mylist =['a',123,3,14,'john']
mylist2 = ["python",20]
mylist+=mylist2
print(mylist)
#append
mylist.append("10")
print(mylist) 

#insert
mylist.insert(1,30)
print(mylist) # at 1 index 30 is inputed
