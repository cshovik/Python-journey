#Arithmatic Operator(=,+=,-=,*=)
var = 10
var += 10 # var = var+10
print(var)
var -= 10 #var = var -10
print(var)

#Compare Operator(<,>,<=,>=,!=)
a=10
b=20
a>b

#logical operator
a =10<10 and 2>-1 #false is false and true is true
print(a)

#bitwise operator(&,|,>>,<<,~)
a = 7 | 5
print(a)

b= 7 & 5
print(a)

c= 10<<2 # 10(binary form)=1010
print(c)  #after right shift 2, c= 101000 = 40(decimal form)

d= 10>>2 # 10(binary form)=1010
print(d)  #after left shift 2, c= 001010 = 2(decimal form)

#identity operator(is, is not)
x = 10
a = x is not 10 #output- false
print(a)

#membership operators(in, not in)
pets ={'dog', 'pet', 'wolf'}
a = 'lion' in 'pets' # output - false
print(a)
