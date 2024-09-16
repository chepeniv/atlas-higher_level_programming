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
&mdash; _Jos&eacute; 'Chep&eacute;' N. Olmos on Septemb:er 15, 2024_

<img src="./assets/oop-core-pillars.jpg" height="384"/>

## Introduction

as it turns out, everything in python is an object. that is, according to stackoverflow, "anything that can be assigned to a variable" -- not only values, but also, functions, classes, modules, and built-in types. this excludes keywords, punctuation, and operators.[^1] and as i was told, every object in python inherits either directly or indirectly from the core `object` class. 

but before we go any further, what is a class ? that's basically a custom definition of a type, so that we're not limited to just what's out-of-the-box. classes are basically like OP `struct`s that are found in C. anyway, objects are instances of a class. to clarify the relation, a class is the blueprint, and an object is the device. this is a one-to-many relation -- one definition, many instances. 

when dealing with objects there are three key pieces of information that we can extract. the first two are the kind of object it is an instance of (`type`) and the how is it uniquely identified internally within python (`id`). the final crucial piece of information when dealing with any object is whether or not we can modify it. in other words, is it mutable or immutable. this also becomes a very important consideration when passing these objects around into functions and methods because it will affect the values that our variables hold and, in turn, whether our code behaves as expected or not. these three fundamental properties of an object are the focus of this bLoGpOsT.

## `id()` and `type()`
<!--
variables are basically simple functions that may return either their object or a duplicate of (depending on the language and circumstance)
-->
when dealing with objects in python we often need to find out the class (type) that it belongs to or to extract its unique identifier. there are two builtin functions for these queries respectively `type(obj)` and `id(obj)`. the first, `obj()` takes any object as an argument and returns a `type` object that can then be analysed. it's really that straight forward. furthermore, there are two other builtin functions related to `type`: `isinstance(obj, (types, ...))` and `issubclass(obj, cls)`. they both return a boolean value. the first, `isinstance` returns `True` if `obj` is any type within the tuple argument `(types, ...)`. the later, `issubclass` only returns `True` if the type of `obj` is a subclass of `cls`. these may come in handy in use-cases where `type` alone might be a bit too awkward.

`id(obj)` on the other hand, returns a unique integer memory address of the given variable's object. this _id_ remains unique and constant during the lifetime of the object. if the lifetime of objects do not overlap, then they may at separate points share the same identifier[^2]. the common use-cases of `id` are to determine what the id of a given object is and whether two variables do indeed _refer_ to the same object in memory. the shorthand for the later is to simply use the `is` operator, which returns `True` if both of its arguments refer to the same exact object. although it is similar to `==` they are NOT interchangeable -- _values_ may be the equal, but the objects may be different. we can easily demonstrate this:
```
>>>
```
these two operators `is` and `==` become quite important when dealing with container types in python. because each is implemented with its own peculiarities, leading to inconsistencies across the implementations of the various containers. most significantly, what happens when we pass these as arguments to functions that operate on them and when we directly attempt to modify them. so in order to troubleshoot we may need to use `id` and `is` to get a sense of how a particular container behaves.

more generally, all of these functions discussed are great for debugging purposes, and it is a good idea to check their output in order to get a sense of what's really going on.

## Mutable Objects

## Immutable Object

###	Why Does This Distinction Matter ?

###	How Differently Does Python Treat Mutable and Immutable Objects ?

## How Are Arguments Passed To Functions

### Implications For Mutable and Immutable Objects
<!--
cloning - allows us to modify a duplicate of a container type but also to have accessible to an unmodified original 
-->

<img src="./assets/perhaps-programming.jpg" height="640"/>

[^1]: https://stackoverflow.com/questions/32083871/what-does-everything-mean-when-someone-says-everything-in-python-is-an-object
[^2]: 
