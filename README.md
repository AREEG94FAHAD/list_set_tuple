# list_set_tuple
List vs tuple vs set
The main distinctions between a list set and a tuple in python
- Indexing not work with set


```
list_a=[1,2,3,4,1]
❌ set_b={1,2,3,4,1} 
tuple_c=(1,2,3,4,1)
```
- Tuple and sets are immutable, which means they are not allowed to add new items.
```
list_a.append(99)
❌ set_b.append(99)
❌ tuple_c.append(99)
```

- Tuple and set do not allow the del function because it is based on index
```
del(list_a[-1])
❌ del(set_b[-1])
❌ del(tuple_c[-1])
```
- remove() method can be used with lists and sets, but not with tuples because they are immutable.
```
list_a.remove(1)
set_b.remove(1)
❌ tuple_c.remove(1)
```

- The discard method can be used only with sets, and the difference between the discard and remove functions is that the first one doesn't return an error if the item is not on set
```
❌ list_a.discard(1).
set_b.discard(1).
❌ tuple_c.discard(1).
```
- The pop method is used with both lists and sets. It is used to remove the last item from a list, while it is used to remove a random item from a set.
```
list_a.pop(1).
set_b.pop(1).
❌ tuple_c.pop(1).
```

- With these functions (set, list, tuple), you can convert a list to a set and a set to a tuple, etc. 
```
alist= list(set_b)
alist= list(tuple_c)
aset = set(list_a)
aset = set(tuple_c)
atuple = tuple(list_a)
atuple = tuple(set_b)
```
- The append () method is used to add a new item to the list at the end , while the add () method is used to add a new item to the set. 
- Adding a new item to a tuple is not allowed because it is immutable.
```
list_a.append(12) 
set_b.add(12)
```
- The insert() method is used to add an item at a specific index.

```
list_a.insert(index, element)
```
- The + operator is used to combine two lists or tuples, while union() is used to combine two sets set. 
```
list_a+list(tuple_c)
tuple_c+tuple(list_a)

a = {1,2,3,4}
b = {1,5,6}
print(a.union(b))
```

- The sort() function is used to change the original list, while sorted () is used to return a new ordered list.
```
list = [4,3,2,1]
list.sort()
print(list) => [1,2,3,4]

list = [4,3,2,1]
print(sorted(list)) => [1,2,3,4]
print(list) => [4,3,2,1]
```

- The update method can be used to update a set by the items in other iterables. Due to the nature of sets, the duplicate items are removed when updating.
```
a = {'x', 1, 4}
b = [3, 4, 1]
c = ('x', 'y', 'z')
a.update(b,c)
print(a)
{1, 3, 4, 'y', 'z', 'x'} 
```
- The len function returns the length (i.e. number of items) of a collection. It works on lists, tuples, and sets.
- The count function can be used to count the number of occurrences of a specific element. It is only used with lists and tuples. Since sets do not contain any duplicate items, the count is 1 for all items.
```
a = [1,4,5,6,1]
b = (3,4)
c = {1,2,3,4}
print(len(a), len(b), len(c))
# 5 2 4
print(a.count(1), b.count(3))
# 2 1
```
### Resource
[Read more](https://towardsdatascience.com/15-examples-to-master-python-lists-vs-sets-vs-tuples-d4ffb291cf07)
