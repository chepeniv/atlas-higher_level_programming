<!--
INSTRUCTIONS:
Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):
    introduction
    id and type
    mutable objects
    immutable objects
    why does it matter and how differently does Python treat mutable and immutable objects
    how arguments are passed to functions and what does that imply for mutable and immutable objects
Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top.

PROJECT OBJECTIVES:
what is an object
difference between a class and an object or instance
difference between immutable object and mutable object
built-in mutable and immutable types
what is a reference
what is an assignment
what is an alias
how to know if two variables are identical
how to know if two variables are linked to the same object
how to display the variable identifier (which is the memory address in the cpython implementation)
-->

# Python3 - Everything is an Object (class essay)
&mdash; _Jos&eacute; 'Chep&eacute;' N. Olmos on September 17, 2024_

<img src="./assets/oop-core-pillars.jpg" height="384"/>

## Introduction

As it turns out, everything in python is an object. That is, according to stackoverflow, "anything that can be assigned to a variable" -- not only values but also functions, classes, modules, and built-in types. This excludes keywords, punctuation, and operators.[^1]
And as i was told by my professor, every object in python inherits either directly or indirectly from the core `object` class. 

But before we go any further, what is a class? That's basically a custom definition of a type, so that we're not just limited to what's out-of-the-box. Classes are basically like OP `struct`s that are found in C. Anyway, objects are instances of a class. To clarify the relation, a class is the blueprint, and an object is the device. This is a one-to-many relation -- one definition, many instances. 

When dealing with objects there are three key pieces of information that we can extract. The first two are the kind of object it is an instance of (`type`) and how is it uniquely identified internally within python (`id`). The final crucial piece of information when dealing with any object is whether or not we can modify it. That is to say, is it mutable or immutable? This also becomes a very important consideration when passing objects around into functions and methods because it will affect the values that our variables hold and, in turn, whether our code behaves as expected or not. These three fundamental properties of an object are the focus of this essay.

## `id()` and `type()`
<!--
variables are basically simple functions that may return either their object or a duplicate of (depending on the language and circumstance)
-->
When dealing with objects in python we often need to find out the class (type) that it belongs to or to extract its unique identifier. There are two builtin functions for these queries respectively `type(obj)` and `id(obj)`. The first, `obj()` takes any object as an argument and returns a `type` object that can then be analysed. It's really that straight forward. Furthermore, there are two other builtin functions related to `type`: `isinstance(obj, (types, ...))` and `issubclass(obj, cls)`. They both return a boolean value. The first, `isinstance` returns `True` if `obj` is any type within the tuple argument `(types, ...)`. The latter, `issubclass` only returns `True` if the type of `obj` is a subclass of `cls`. These may come in handy in use-cases where `type` alone might be a bit too awkward.

`id(obj)`, on the other hand, returns a unique integer memory address of the given variable's object. This _id_ remains unique and constant during the lifetime of the object. If the lifetime of objects do not overlap, then they may at separate points share the same identifier.[^2]
The common use-cases of `id` are to determine what the id of a given object is and whether two variables do indeed _refer_ to the same object in memory. The shorthand for the latter is to simply use the `is` operator, which returns `True` if both of its arguments refer to the same exact object. Although it is similar to `==` they are NOT interchangeable -- their _values_ may be equal, but the _objects_ may be different. We can easily demonstrate this:

```python
>>> x = [0, 1, 2, 3]
>>> y = [0, 1, 2, 3]
>>> x == y
True
>>> x is y
False
>>> id(x)
138308476390208
>>> id(y)
138308476392000
```

These two operators `is` and `==` become quite important when dealing with container types in python because each is implemented with its own peculiarities, leading to inconsistencies across the implementations. Most significantly, what happens when we pass these as arguments to functions that operate on them and when we directly attempt to modify them? Not only this, but we also need to know how assignments are passed around. And here too these two become important. In order to troubleshoot around these cases we may need to use `id` and `is` to get a sense of how a particular object behaves.

More generally, all of these functions discussed are great for debugging purposes, and it is a good idea to check their output regularly in order to get a sense of what's really going on.

## Mutability
<!--
### Why Does This Distinction Matter ?
### How Differently Does Python Treat Mutable and Immutable Objects ?
-->

Objects in python can be one of two types: mutable or immutable. The first kind, mutable means that we are able to change the content or values of the object without changing its identity.[^4] 
Although at runtime the _type_ of an object cannot be altered, if it is mutable its state can be changed. Custom classes are usually mutable as well as the builtin types `list`, `dict`, and `set`. 
If the size or content of a type is expected to change then mutable objects are the way to go.[^3]
To determine which builtin types are mutable or not refer to documentation.

The other kind, immutable objects cannot be altered and attempting to modify them after creation will raise an exception.[^3]
The only real way python modifies an immutable object is by creating a copy based on the modified value of the original.
In other words, all that it is really doing is modifying which object a variable refers to and not actually doing anything to object itself.[^4]
Typically, immutable objects are quicker to access but more expensive to modify since that involves the creation of a whole new object. The builtin primitive datatypes in python are all immutable.

Tuples are a peculiar case. The tuple itself may be immutable, yet its contents may be mutable.[^3]
What this probably looks like under-the-hood is that for mutable elements a tuple might just hold an immutable pointer to the addresses of that object. The pointer element cannot be changed, but the object at that location can.

Mutability is the primary reason why `id` and `is` become such important checks when modifying and moving objects around and to illustrate the difference in expected behavior here's a modified example borrowed from stackoverflow that demonstrates just that[^4]:

```python
x = "hello world" # immutable type
print(x)
func(x)  # "modifies" x
print(x) # output doesn't change

x = ["hello", "world"] # mutable type
print(x)
func(x)  # modifies x
print(x) # actually outputs something different

x = "hello" # immutable type
y = x
print(x)
func(y)  # modifies y
print(x) # x remains unchanged

x = ["hello", 0, True] # mutable type
y = x
print(x)
func(y)  # modifies y 
print(x) # actually outputs something different
```

## Passing Arguments To Functions
<!--
### Implications For Mutable and Immutable Objects
-->


Let's consider how a function acts upon its inputs. Python uses the model "pass by object reference" (otherwise know as "pass by assignment") and i really don't know what that means, _BUT_ depending on the mutability of the argument that gets passed, a function will behave differently.[^5]
This leaves only two ways that a function can manipulate data passed into it.
If an object is immutable then the default behaviour is to pass-by-value, otherwise if an object is mutable then pass-by-reference becomes the default. 

The first, pass-by-value makes an internal copy of the value returned by a variable thereby leaving the original object alone and unmodified.

The second, pass-by-reference actually directly addresses the object returned by a variable and thereby any modifications to its data are reflected outside of the function call.[^5] In this case, it is also possible to simulate pass-by-value behavior by making copies within a function definition and manipulating those instead of the original. This is where container-type cloning comes in handy. It allows us to modify a duplicate and to also have access to the unmodified original.
Usually, pass-by-ref is more efficient than pass-by-val because it doesn't require that a copy be made, and because the object is manipulated directly there is no need to return it.[^5]

<img src="./assets/perhaps-programming.jpg" height="640"/>

[^1]: https://stackoverflow.com/questions/32083871/what-does-everything-mean-when-someone-says-everything-in-python-is-an-object

[^2]: https://www.geeksforgeeks.org/id-function-python

[^3]: https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python

[^4]: https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types

[^5]: https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python
