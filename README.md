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

### Resource
[Read more](https://towardsdatascience.com/15-examples-to-master-python-lists-vs-sets-vs-tuples-d4ffb291cf07)
