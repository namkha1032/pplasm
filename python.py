# 1. Multiline string (comment): """ nguyennamkha """

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------VARIABLES---------------------------------------------
# ---------------------------------------------------------------------------------------------------
# 1. Casting:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# 2. Get the type: 
type(x)

# 3. Assign many values to multiple vars: 
x, y, z = "Orange", "Banana", "Cherry"

# 4. Assign one value to multiple vars: 
x = y = z = "Orange"

# 5. Unpack a collection:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 

# 6. Output multiple vars: 
print(x, y, z)

# 7. "global" keyword (2 use):
	# - Create a global var inside a func
	# - Change value of global var inside a func

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------DATA TYPES--------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Built-in data types:
str                             # Text Type:
int, float, complex             # Numeric Types:
list, tuple, range              # Sequence Types:
dict                            # Mapping Type:
set, frozenset                  # Set Types:
bool                            # Boolean Type:
bytes, bytearray, memoryview    # Binary Types:
None                            # None Type:

# 2. Get the data type: 
type(x)

# 3. Example:
# Example						                Data Type
x = "Hello World"		                		# str	
x = 20					                    	# int	
x = 20.5				                    	# float	
x = 1j					                    	# complex	
x = ["apple", "banana", "cherry"]	        	# list	
x = ("apple", "banana", "cherry")	        	# tuple	
x = range(6)				                	# range	
x = {"name" : "John", "age" : 36}	        	# dict	
x = {"apple", "banana", "cherry"}	           	# set	
x = frozenset({"apple", "banana", "cherry"})    # frozenset	
x = True					                    # bool	
x = b"Hello"				                	# bytes	
x = bytearray(5)			                	# bytearray	
x = memoryview(bytes(5))	            		# memoryview	
x = None				                    	# NoneType

# 4. Set the data type:
# Example										Data Type
x = str("Hello World")							# str	
x = int(20)										# int	
x = float(20.5)									# float	
x = complex(1j)									# complex	
x = list(("apple", "banana", "cherry"))			# list	
x = tuple(("apple", "banana", "cherry"))		# tuple	
x = range(6)									# range	
x = dict(name="John", age=36)					# dict	
x = set(("apple", "banana", "cherry"))			# set	
x = frozenset(("apple", "banana", "cherry"))	# frozenset	
x = bool(5)										# bool	
x = bytes(5)									# bytes	
x = bytearray(5)								# bytearray	
x = memoryview(bytes(5))						# memoryview

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------DATA TYPES--------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Type convert:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
#Cannot convert complex to other types

# 2. Random
import random
print(random.randrange(1, 10))

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------STRINGS-----------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. String index:
a = "Hello, World!"
print(a[1])

# 2. Loop through string
for x in "banana":
    print(x)

# 3. String length
len(a)

# 4. Check if a phrase appear in a string
print("free" in "The best things in life are free!") # True

# 5. Check if a phrase not appear in a string
print("expensive" not in "The best things in life are free!")

# 6. Slicing string
b = "nguyennamkha"
print(b[6:9]) #nam

# 7. Slice from start
b = "nguyennamkha"
print(b[:9]) #nguyennam

# 8. SLice to end
b = "nguyennamkha"
print(b[6:]) #namkha

# 9. Negative slicing
#    012345678
b = "nguyennam"
#    987654321
print(b[-1:])   #m
print(b[-3:])   #nam
print(b[:-3])   #nguyen
print(b[-6:-1]) #yenna
print(b[-6:8])  #yenna

# 10. Remove whitespace
a.strip()

# 11. Replace string
b = "nguyennamkha"
print(b.replace("nguyen","hehe")) # hehenamkha

# 12. Split string
b = "nguyen nam kha"
print(b.split(" ")) # returns ['nguyen', 'nam', 'kha']

# 13. Concat string
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# 14. Format string
quantity = 3
itemno = 567
price = 49.95
myorder = f"I want to pay {price} dollars for {quantity} pieces of item {itemno}."
print(myorder)

# 15. Escape string
# Code	Result
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# 16. String method
# Method	Description
myStr = "namkha"
myStr.capitalize()	    # Converts the first character to upper case
myStr.casefold()	    # Converts string into lower case
myStr.center()	        # Returns a centered string
myStr.count()	        # Returns the number of times a specified value occurs in a string
myStr.encode()	        # Returns an encoded version of the string
myStr.endswith()	    # Returns true if the string ends with the specified value
myStr.expandtabs()	    # Sets the tab size of the string
myStr.find()	        # Searches the string for a specified value and returns the position of where it was found
myStr.format()	        # Formats specified values in a string
myStr.format_map()	    # Formats specified values in a string
myStr.index()	        # Searches the string for a specified value and returns the position of where it was found
myStr.isalnum()	        # Returns True if all characters in the string are alphanumeric
myStr.isalpha()	        # Returns True if all characters in the string are in the alphabet
myStr.isdecimal()	    # Returns True if all characters in the string are decimals
myStr.isdigit()	        # Returns True if all characters in the string are digits
myStr.isidentifier()	# Returns True if the string is an identifier
myStr.islower()     	# Returns True if all characters in the string are lower case
myStr.isnumeric()	    # Returns True if all characters in the string are numeric
myStr.isprintable()	    # Returns True if all characters in the string are printable
myStr.isspace()	        # Returns True if all characters in the string are whitespaces
myStr.istitle()	        # Returns True if the string follows the rules of a title
myStr.isupper()	        # Returns True if all characters in the string are upper case
myStr.join()	        # Joins the elements of an iterable to the end of the string
myStr.ljust()	        # Returns a left justified version of the string
myStr.lower()	        # Converts a string into lower case
myStr.lstrip()	        # Returns a left trim version of the string
myStr.maketrans()	    # Returns a translation table to be used in translations
myStr.partition()	    # Returns a tuple where the string is parted into three parts
myStr.replace()	        # Returns a string where a specified value is replaced with a specified value
myStr.rfind()	        # Searches the string for a specified value and returns the last position of where it was found
myStr.rindex()	        # Searches the string for a specified value and returns the last position of where it was found
myStr.rjust()	        # Returns a right justified version of the string
myStr.rpartition()	    # Returns a tuple where the string is parted into three parts
myStr.rsplit()	        # Splits the string at the specified separator, and returns a list
myStr.rstrip()	        # Returns a right trim version of the string
myStr.split()	        # Splits the string at the specified separator, and returns a list
myStr.splitlines()	    # Splits the string at line breaks and returns a list
myStr.startswith()	    # Returns true if the string starts with the specified value
myStr.strip()	        # Returns a trimmed version of the string
myStr.swapcase()	    # Swaps cases, lower case becomes upper case and vice versa
myStr.title()	        # Converts the first character of each word to upper case
myStr.translate()	    # Returns a translated string
myStr.upper()	        # Converts a string into upper case
myStr.zfill()	        # Fills the string with a specified number of 0 values at the beginning

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------BOOLEANS----------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Values
# True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# 2. isinstance()
x = 200
print(isinstance(x, int)) # True

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------OPERATORS---------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Arithmetic Operators are used with numeric values to perform common mathematical operations:
# Operator	Name	        Example
# +	        Addition	    x + y	
# -	        Subtraction	    x - y	
# *	        Multiplication	x * y	
# /	        Division	    x / y	
# %	        Modulus	        x % y	
# **	    Exponentiation	x ** y	
# //	    Floor division	x // y

# 2. Assignment Operators are used to assign values to variables:
# Operator	Example	    Same As
# =	        x = 5	    x = 5	
# +=	    x += 3	    x = x + 3	
# -=	    x -= 3	    x = x - 3	
# *=	    x *= 3	    x = x * 3	
# /=	    x /= 3	    x = x / 3	
# %=	    x %= 3	    x = x % 3	
# //=	    x //= 3	    x = x // 3	
# **=	    x **= 3	    x = x ** 3	
# &=	    x &= 3	    x = x & 3	
# |=	    x |= 3	    x = x | 3	
# ^=	    x ^= 3	    x = x ^ 3	
# >>=	    x >>= 3	    x = x >> 3	
# <<=	    x <<= 3	    x = x << 3

# 3. Comparison Operators are used to compare two values:
# Operator	Name	                    Example
# ==	    Equal	                    x == y	
# !=	    Not equal	                x != y	
# >	        Greater than	            x > y	
# <	        Less than	                x < y	
# >=	    Greater than or equal to	x >= y	
# <=	    Less than or equal to	    x <= y

# 4. Logical Operators are used to combine conditional statements:
# Operator	Description	                                                    Example
# and 	    Returns True if both statements are true	                    x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	                x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	not     (x < 5 and x < 10)

# 5. Identity Operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# Operator	Description	                                                Example	Try it
# is 	    Returns True if both variables are the same object	        x is y	
# is not	Returns True if both variables are not the same object	    x is not y

# 6. Membership Operators are used to test if a sequence is presented in an object:
# Operator	Description	                                                                        Example	Try it
# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# 7. Bitwise Operators
# Operator	Name	                Description	                                                                                                Example
# & 	    AND	                    Sets each bit to 1 if both bits are 1	                                                                    x & y	
# |	        OR	                    Sets each bit to 1 if one of two bits is 1	                                                                x | y	
# ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                            x ^ y	
# ~	        NOT	                    Inverts all the bits	                                                                                    ~x	
# <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                        x << 2	
# >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2

# 8. Operator Precedence
# Operator	                                        Description
# ()	                                            Parentheses	
# **	                                            Exponentiation	
# +x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	                                    Multiplication, division, floor division, and modulus	
# +  -	                                            Addition and subtraction	
# <<  >>	                                        Bitwise left and right shifts	
# &	                                                Bitwise AND	
# ^	                                                Bitwise XOR	
# |	                                                Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	    Comparisons, identity, and membership operators	
# not	                                            Logical NOT	
# and	                                            AND	
# or	                                            OR

# ---------------------------------------------------------------------------------------------------
# ---------------------------------PYTHON COLLECTIONS (ARRAYS)---------------------------------------
# ---------------------------------------------------------------------------------------------------
    # There are four collection data types in the Python programming language:
            # List is a collection which is ordered and changeable. Allows duplicate members.
            # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
            # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
            # Dictionary is a collection which is ordered** and changeable. No duplicate members.


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------LISTS---------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Syntax
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# 2. List items
#       - List items are ordered, changeable, and allow duplicate values.
#       - List items are indexed, the first item has index [0], the second item has index [1] etc.

# 3. List length
len(mylist)

# 4. List items - data types
list1 = ["abc", 34, True, 40, "male"] # A list with strings, integers and boolean values:

# 5. List constructor
thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) # note the double round-brackets

# 6. Index
thislist[1]

# 7. Negative index
thislist[-1]

# 8. Range of index
thislist[2:5]

# 9. Range of negative index
thislist[-4:-1]

# 10. Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# 11. Change list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# 12. Change list item - range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# 13. Change list item - insert more items than replace
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# 14. Change list item - insert less items than replace
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']

# 15. Insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']

# 16. Append item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ["apple", "banana", "cherry", "orange"]

# 17. Extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# 18. Extend tuple to list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# 19. Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

# 20. Remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']

# 21. Delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

# 22. Empty (clear) the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # []

# 23. Loop list using for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# 23. Loop list using index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# 23. Loop list using while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# 24. Loop list using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# 25. List comprehension syntax
# newlist = [expression for item in iterable if condition == True]

# 25. List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['apple', 'banana', 'mango']

# 26. List comprehension with condition as expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) # ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# 27. Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# 28. Sort List Numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # [23, 50, 65, 82, 100]

# 29. Sort list descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # [100, 82, 65, 50, 23]

# 30. Customize sort function
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # Sort the list based on how close the number is to 50
print(thislist) # [50, 65, 23, 82, 100]

# 31. Case - insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

# 32. Reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']

# 33. Copy list
        # You cannot copy a list simply by typing list2 = list1, 
        # because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# Using copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Using list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# 34. Join list
# Using operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# Using append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)
# Using extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# 35. List methods
# Method	        Description
mylist.append()	    # Adds an element at the end of the list
mylist.clear()	    # Removes all the elements from the list
mylist.copy()	    # Returns a copy of the list
mylist.count()	    # Returns the number of elements with the specified value
mylist.extend()	    # Add the elements of a list (or any iterable), to the end of the current list
mylist.index()	    # Returns the index of the first element with the specified value
mylist.insert()	    # Adds an element at the specified position
mylist.pop()	    # Removes the element at the specified position
mylist.remove()	    # Removes the item with the specified value
mylist.reverse()	# Reverses the order of the list
mylist.sort()	    # Sorts the list

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------TUPLES------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Syntax
thistuple = ("apple", "banana", "cherry")

# 2. Tuple items
        # Tuple items are ordered, unchangeable, and allow duplicate values.
        # Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# 3. Tuple length
len(thistuple)

# 4. Create Tuple With One Item
thistuple = ("apple",)
print(thistuple)        # ('apple', )
print(type(thistuple))  # <class 'tuple'>
#NOT a tuple
thistuple = ("apple")   
print(thistuple)        # apple
print(type(thistuple))  # <class 'str'>

# 5. Tupe items - data types
tuple1 = ("abc", 34, True, 40, "male") # A tuple with strings, integers and boolean values

# 6. tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# 7. Tuple index: just like List

# 8. Update tuple
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.

# 9. convert tuple to list, change the list, convert back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# 10. Add item to a tuple
# Convert to list, add item, convert back to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
# Add tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

# 11. Remove item
# Convert to list, reove item, convert back to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
# Delete the tuple completely using del
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# 12. Packing tuple
fruits = ("apple", "banana", "cherry")

# 13. Unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

# 14. Using asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)    # apple
print(yellow)   # banana
print(red)      # ['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)    # apple
print(tropic)   # ['mango', 'papaya', 'pineapple']
print(red)      # cherry

# 15. Loop tuples: just like List

# 16. Join tuple using operator +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2

# 17. Multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# 18. Tuple method
# Method            Description
thistuple.count()	#Returns the number of times a specified value occurs in a tuple
thistuple.index()	#Searches the tuple for a specified value and returns the position of where it was found

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------SETS--------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Syntax
myset = {"apple", "banana", "cherry"}

# 2. Sets
        # A set is a collection which is unordered, unchangeable*, unindexed, and do not allow duplicate values.
        # * Note: Set items are unchangeable, but you can remove items and add new items.

# 3. Duplicates are ignored
thisset = {"apple", "banana", "cherry", True, 1, 2, "apple"} # 1 and True are duplicates
print(thisset) # {True, 2, 'cherry', 'apple', 'banana'}

# 4. Set length
len(myset)

# 5. Set item - data types
set1 = {"abc", 34, True, 40, "male"} # A set with strings, integers and boolean values

# 6. set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

# 7. Loop through set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# 8. Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# 9. Add items using add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # {'apple', 'orange', 'banana', 'cherry'}

# 10. Add set using update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"} # tropical can be any iterable object (tuples, lists, dictionaries etc.)
thisset.update(tropical)
print(thisset) # {'pineapple', 'banana', 'papaya', 'apple', 'mango', 'cherry'}

# 11. Remove item using remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # Note: If the item to remove does not exist, remove() will raise an error.
print(thisset) # {'cherry', 'apple'}

# 12. Remove item using discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") # Note: If the item to remove does not exist, discard() will NOT raise an error.
print(thisset) # {'cherry', 'apple'}

# 13. Using pop() to remove a random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop() # return the removed item

# 14. Empty the set using clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # set()

# 15. Delete the set completely using del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # raise error

# 16. Loop set using for
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# 17. Join set usin union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # Note: Both union() and update() will exclude any duplicate items.

# 18. Join set using update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) # Note: Both union() and update() will exclude any duplicate items.

# 19. Keep only the duplicates
# intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) # {'apple'}
#intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) # {'apple'}

# 20. Keep All, But NOT the Duplicates
# symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) # {'microsoft', 'banana', 'google', 'cherry'}
# symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) # {'google', 'cherry', 'banana', 'microsoft'}

# 21. Set methods
# Method	                        Description
myset.add()	                        # Adds an element to the set
myset.clear()	                    # Removes all the elements from the set
myset.copy()	                    # Returns a copy of the set
myset.difference()	                # Returns a set containing the difference between two or more sets
myset.difference_update()	        # Removes the items in this set that are also included in another, specified set
myset.discard()	                    # Remove the specified item
myset.intersection()	            # Returns a set, that is the intersection of two other sets
myset.intersection_update()	        # Removes the items in this set that are not present in other, specified set(s)
myset.isdisjoint()	                # Returns whether two sets have a intersection or not
myset.issubset()	                # Returns whether another set contains this set or not
myset.issuperset()	                # Returns whether this set contains another set or not
myset.pop()	                        # Removes an element from the set
myset.remove()	                    # Removes the specified element
myset.symmetric_difference()	    # Returns a set with the symmetric differences of two sets
myset.symmetric_difference_update()	# inserts the symmetric differences from this set and another
myset.union()	                    # Return a set containing the union of sets
myset.update()	                    # Update the set with the union of this set and others

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------DICTS-------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Syntax
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# 2. Dict
        # Dictionaries are used to store data values in key:value pairs.
        # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# 3. Dict length
len(thisdict)

# 4. Dict data types
# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# 5. dict() constructor
thisdict = dict(name = "John", age = 36, country = "Norway")

# 6. Access item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Using square bracket
print(thisdict["model"]) # Mustang
# Using get()
print(thisdict.get("model")) # Mustang

# 7. Get list of all keys using keys()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys()) # dict_keys(['brand', 'model', 'year'])

# 7. Get list of all values using values()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.values()) # dict_values(['Ford', 'Mustang', 1964])

# 8. Get list of all items using items()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# 9. Check if key exists using in keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("model" in thisdict) # True

# 10. Change items
# Using square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
# Using update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# 11. Add new item
# Using square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
# Using update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# 12. pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) # {'brand': 'Ford', 'year': 1964}

# 13. popitem() remove the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang'}

# 14. del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) # {'brand': 'Ford', 'year': 1964}

# 15. delete entire dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# 16. empty the dict using clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) # {}

# 17. Loop dict
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) # brand model year
for x in thisdict.keys():
  print(x) # brand model year
for x in thisdict:
  print(thisdict[x]) # Ford Mustang 1964
for x in thisdict.values():
  print(x) # Ford Mustang 1964
for x, y in thisdict.items():
  print(x, y) #brand Ford model Mustang year 1964

# 18. Copy a dict
        # You cannot copy a dictionary simply by typing dict2 = dict1, 
        # because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# using copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
# using dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)

# 19. Nested dict
# 1st style
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# 2nd style
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
# 20. Access nested dict
print(myfamily["child2"]["name"]) # Tobias

# 21. Dict methods
# Method	        Description
mydict.clear()	    # Removes all the elements from the dictionary
mydict.copy()	    # Returns a copy of the dictionary
mydict.fromkeys()	# Returns a dictionary with the specified keys and value
mydict.get()	    # Returns the value of the specified key
mydict.items()	    # Returns a list containing a tuple for each key value pair
mydict.keys()	    # Returns a list containing the dictionary's keys
mydict.pop()	    # Removes the element with the specified key
mydict.popitem()	# Removes the last inserted key-value pair
mydict.setdefault()	# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
mydict.update()	    # Updates the dictionary with the specified key-value pairs
mydict.values()	    # Returns a list of all the values in the dictionary

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------IF-ELSE-----------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Syntax
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# 2. Short hand if-else (ternary operator)
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# ---------------------------------------------------------------------------------------------------
# -------------------------------------------WHILE-LOOP----------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Run block of code when condition is no longer true
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") # The else block will NOT be executed if the loop is stopped by a break statement.

# ---------------------------------------------------------------------------------------------------
# -------------------------------------------FOR-LOOP------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. For loop
      # A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
      # This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
      # With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# 2. Loop through list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# 3. Loop through strinng
for x in "banana":
  print(x)

# 4. Loop through range
for x in range(6): # loop from 0 to 5
  print(x)
for x in range(2, 6): # loop from 2 to 5
  print(x)
for x in range(2, 30, 3): # Loop from 2 to 29, increment by 3
  print(x)

# 1. Run block of code when condition is no longer true
for x in range(6):
  print(x)
else:
  print("Finally finished!") # The else block will NOT be executed if the loop is stopped by a break statement.

# ---------------------------------------------------------------------------------------------------
# -------------------------------------------FUNCTION------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") 

# 2. Keyword Arguments (kwargs)
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# 3. Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# 4. Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# 5. Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# ---------------------------------------------------------------------------------------------------
# -------------------------------------------LAMBDA--------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 1. Syntax
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# 2. Function inside function
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# ---------------------------------------------------------------------------------------------------
# -------------------------------------------CLASS---------------------------------------------------
# ---------------------------------------------------------------------------------------------------

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def __str__(self):
    return f"{self.fname} {self.lname}"
  def myfunc(self):
    print("Hello my name is", self.fname, self.lname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# ---------------------------------------------------------------------------------------------------
# -------------------------------------------VISITOR-------------------------------------------------
# ---------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Exp(ABC):
    pass

class IntLit(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, v):
        return v.visitIntLit(self)

class FloatLit(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, v):
        return v.visitFloatLit(self)

class UnExp(Exp):
    def __init__(self, operator, arg):
        self.operator = operator
        self.arg = arg
    def accept(self, v):
        return v.visitUnExp(self)

class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right
    def accept(self, v):
        return v.visitBinExp(self)

class Eval():
    def visit(self, exp):
        return exp.accept(self)
    def visitBinExp(self, exp):
        if exp.operator == "+":
            return self.visit(exp.left) + self.visit(exp.right)
        elif exp.operator == "-":
            return self.visit(exp.left) - self.visit(exp.right)
        elif exp.operator == "*":
            return self.visit(exp.left) * self.visit(exp.right)
        else:
            return self.visit(exp.left) / self.visit(exp.right)      
    def visitUnExp(self,exp):
        if exp.operator == "-":
            return (-1) * self.visit(exp.arg)
        return exp.arg.eval()
    def visitIntLit(self, exp):
        return exp.num
    def visitFloatLit(self, exp):
        return exp.num
    
class PrintPrefix():
    def visit(self, exp):
        return exp.accept(self)
    def visitBinExp(self, exp):
        if exp.operator == "+":
            return "+" + " " + self.visit(exp.left) + " " + self.visit(exp.right)
        if exp.operator == "-":
            return "-" + " " +  self.visit(exp.left) + " " + self.visit(exp.right)
        if exp.operator == "*":
            return "*" + " " +  self.visit(exp.left) + " " +  self.visit(exp.right)
        if exp.operator == "/":
            return "/" + " " +  self.visit(exp.left) + " " +  self.visit(exp.right)
    def visitUnExp(self,exp):
        if exp.operator == "-":
            return "-." + " " +  self.visit(exp.arg)
        return "+." + " " +  self.visit(exp.arg)
    def visitIntLit(self, exp):
        return str(exp.num)
    def visitFloatLit(self, exp):
        return str(exp.num)
    
class PrintPostfix():
    def visit(self, exp):
        return exp.accept(self)
    def visitBinExp(self, exp):
        if exp.operator == "+":
            return self.visit(exp.left) + " " + self.visit(exp.right) + " +" 
        if exp.operator == "-":
            return self.visit(exp.left) + " " + self.visit(exp.right) + " -" 
        if exp.operator == "*":
            return self.visit(exp.left) + " " + self.visit(exp.right) + " *" 
        if exp.operator == "/":
            return self.visit(exp.left) + " " + self.visit(exp.right) + " /"  
    def visitUnExp(self,exp):
        if exp.operator == "-":
            return  self.visit(exp.arg) + " -." 
        return self.visit(exp.arg) + " +."
    def visitIntLit(self, exp):
        return str(exp.num)
    def visitFloatLit(self, exp):
        return str(exp.num)

# ---------------------------------------------------------------------------------------------------
# --------------------------------------------FP-----------------------------------------------------
# ---------------------------------------------------------------------------------------------------

from functools import reduce
# return list of square from 1 to n
def lstSquare1(n):
    return [i*i for i in range(1,n+1)]
def lstSquare2(n):
    return list(map(lambda i: i*i, range(1,n+1)))

# return list of pair ele of lst and n
def dist1(lst,n):
    return [(x,n) for x in lst]
def dist2(lst,n):
    return list(map(lambda x: (x,n),lst))

# return list of ele < n
def lessThan1(lst,n):
    return [i for i in lst if i < n]
def lessThan2(lst,n):
    return list(filter(lambda x: x<n,lst))

# flatten
def flatten(lst):
    return reduce(lambda prev, curr: prev + curr,lst,[])