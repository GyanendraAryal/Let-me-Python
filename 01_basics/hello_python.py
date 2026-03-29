#print("Here we go with python");

#def chai(n):
    #print(n)

#chai(4)
#chai("Lemon Tea")

#chai_one = 'lemon tea'
#chai_two = 'masala tea'
#chai_three = 'giger tea'


#From Coding with Sagar
print("Hello World Again")

name = "Gyanendra"
age = 23
print(name, age)
print("It is ",type(name))


#Datatypes
"""
Numeric-Type:-
    Float- Decimal Numbers
    Int- Whole Numbers
    Complex- Real and Imaginary Part
"""
"""
Boolean Type:-
    True/False
    Logical Operations
"""
"""
None Type:-
    result = None; # Can assign it later
"""
"""
Sequence Type:-
    String:- Sequence of characters, immutable(cannot change)
    List:- Like an array, my_list = ['data1','data2', 'data3'](Mutable)
    Tuple:- ('data1','data2','data3')(immutable)
"""
"""
Set Type:- Unorder collection of unique items.
    -set(mutable)
    -frozenset(immutable)

"""
#Set
unique_number = {1,2,3,3,4,4,2,4,5,6,7,9}
print(unique_number)

#FrozenSet
immutable_set = frozenset([1,2,3,4,5,6,7,6,5,4,8,9,12])
print(immutable_set)

"""
Map:- Collection of key value pairs
"""

person = {
    'name':'gopal', 
    'age':35, 
    'number':989087245, 100: 123.124
    }
print(person)