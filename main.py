from math import remainder

x=15
print (x)

y=7.5
print (y)

myfloat = float(9.5)
print (myfloat)

x=6.5
x = x * 5
print (x)

x=myfloat * x
print (x)

# Strings
my_string = 'Helo'
print (my_string)

my_string = "halo"
print (my_string)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello +" "+ world
print(helloworld)

a, b, c = 1, 2, 3
print(a, b, c)

number =  1+ (2*3)/4
print(number)

remainder = 10%3
print(remainder)

rem = 10%3
div = 10/3
print(rem,div )
# % is a modulo which is reminds reminder like above

# there are we have ** double start it means that it is power of that number like ^ 2^3=8 2**3=8

squared = 2 ** 5
cubed = 2 ** 3
print(squared, cubed)

lotofhellos = "hello "*10
print(lotofhellos)

# one=1
# two=2
# hello = "hello"
# print (hello + one +two)


color = ["red", "green", "blue"]
print (color[0])
print (color[1])
print (color[2])
print (len(color))

myList = []
myList.append(4)
myList.append(7)
myList.append(8)

print (myList[0])
print (myList[1])
print (myList[2])

Mylist = ["Larry", "Curly", "Moe"]
Mylist.append("Shemp")
Mylist.insert(1, "XXX")

print (Mylist[0])
print (Mylist[1])
print (Mylist[2])
print (Mylist[3])
print (Mylist[4])

Mylist.extend(['here', "Smth"])


# output formatting
a=5
b=6.5
c= "Hello"
print("a is :%d, b is %f, c is %s" % (a,b,c))









# List Methods
# Here are some other common list methods.
#
# list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
# list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
# list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
# list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
# list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
# list.reverse() -- reverses the list in place (does not return it)
# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
# Notice that these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument.
# list = ['larry', 'curly', 'moe']
# list.append('shemp')  ## append elem at end
# list.insert(0, 'xxx')  ## insert elem at index 0
# list.extend(['yyy', 'zzz'])  ## add list of elems at end
# print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
# print(list.index('curly'))  ## 2
#
# list.remove('curly')  ## search and remove that element
# list.pop(1)  ## removes and returns 'larry'
# print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']