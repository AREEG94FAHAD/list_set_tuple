list_a=[1,2,3,4,1]
set_b={1,2,3,4,1}
tuple_c=(1,2,3,4,1)

# ........... Indexing not work with set.............
print(list_a[0])
#print(set_b[0])
print(tuple_c[0])

# ...........Tuple and sets are immutable, which means they are not allowed to add new items. .............
list_a.append(99)
# set_b.append(99)
# tuple_c.append(99)

# .......Tuple and set do not allow the del function because it is based on index.............
del(list_a[-1])
# del(set_b[-1])
# del(tuple_c[-1])

#.........Remove can be used with lists and sets, but not with tuples because they are immutable.
list_a.remove(1)
set_b.remove(1)
# tuple_c.remove(1)


# ........ The discard method can be used only with sets, and the difference between the discard and remove functions is that the first one doesn't return an error if the item is not on set
# list_a.discard (1).


set_b.discard(1)
# tuple_c.discard(1)

# ........ The pop method is used with both lists and sets. It is used to remove the last item from a list, while it is used to remove a random item from a set.



list_a.pop()
set_b.pop()
# tuple_c.pop()

# ............ With only these functions (set, list, tuple), you can convert a list to a set and a set to a tuple.



# ............ Because sets and lists are immutable, you can add new elements to them, whereas tuples cannot.


list_a.append(12)
set_b.add(12)

# ..... Insert is used to insert elements into special indexes.

list_a(0,15)


# The + operator allows you to combine two lists or tuples, whereas set does not allow you to do so.

list_a+list(tuple_c)
tuple_c+tuple(list_a)

# We can use the union operator to combine two sets. The duplicate elements will be removed.
a = {1,2,3,4}
b = {1,5,6}
print(a.union(b))

# ... sorted can only use with list because set unorder and tuple is immutable

# sort() change orginal list
a = [3,1,5,2]
a.sort()
print(a)


# sorted() return a new sorted list


# .......The update method can be used to update a set by the items in other iterables. Due to the nature of sets, the duplicate items are removed when updating.
a = {'x', 1, 4}
b = [3, 4, 1]
c = ('x', 'y', 'z')
a.update(b,c)
print(a)
{1, 3, 4, 'y', 'z', 'x'} 

# Len and count
#The len function returns the length (i.e. number of items) of a collection. It works on lists, tuples, and sets.
#The count function can be used to count the number of occurrences of a specific element. It is only used with lists and tuples. Since sets do not contain any duplicate items, the count is 1 for all items.
a = [1,4,5,6,1]
b = (3,4)
c = {1,2,3,4}
print(len(a), len(b), len(c))
# 5 2 4
print(a.count(1), b.count(3))
# 2 1