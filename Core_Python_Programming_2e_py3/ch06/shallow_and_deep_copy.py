#!/usr/bin/env python3

import copy

person = ['name', ['savings', 100.0]]
hubby = person[:]           # slice copy
wifey = list(person)        # fac func copy

for x in person, hubby, wifey:
    print(id(x))

hubby[0] = 'joe'
wifey[0] = 'jane'
print(hubby, wifey)

hubby[1][1] = 50.00  # id of hubby[1] & wifer[1] are actually the same
print(hubby, wifey)
print("id of hubby[1] & wifer[1] is", id(hubby[1]), id(wifey[1]))

wifey2 = copy.deepcopy(person)

'''
The reason is that we have only made a shallow copy. A shallow copy of an
object is defined to be a newly created object of the same type as the original
object whose contents are references to the elements in the original object. In
other words, the copied object itself is new, but the contents are not. Shallow
copies of sequence objects are the default type of copy and can be made in any
number of ways: 
(1) taking a complete slice [:],
(2) using a factory function, e.g., list(), dict(), etc., or
(3) using the copy() function of the copy module.
Your next question should be: When the wife¡¯s name is assigned, how come
it did not affect the husband¡¯s name? Shouldn¡¯t they both have the name
'jane' now? The reason why it worked and we don¡¯t have duplicate names is
because of the two objects in each of their lists, the first is immutable (a string)
and the second is mutable (a list). Because of this, when shallow copies are
made, the string is explicitly copied and a new (string) object created while the
list only has its reference copied, not its members. So changing the names is
not an issue but altering any part of their banking information is. Here, let us
take a look at the object IDs for the elements of each list. Note that the banking
object is exactly the same and the reason why changes to one affects the
other. Note how, after we change their names, that the new name strings
replace the original 'name' string:
'''