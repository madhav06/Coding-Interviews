# Coding-Interviews
Brainstorm coding problems here and questions asked in live Interviews.

## What is ByteCode in Python?
Let's understand how python runs our programs. Python is usually called an interpreted language, however, it combines compiling and interpreting. When we execute a source code(that is a .py file), python first compiles it into a bytecode. The bytecode is a low-level platform-independent representation of your source code, however, it is not the binary machine code and cannot be run by the target machine directly. In fact, it is a set of instructions for a virtual machine which is called the Python Virtual Machine(PVM). After compilition, the bytecode is sent for execution to the PVM. The PVM is an interpreter that runs the bytecode and is part of the python system. The bytecode is platform-independent. Here, CPython compiles the source code into the bytecode and then this bytecode is executed by the CPython virtual machine.

## What is difference between SETS and TUPLES?
TUPLES are a datatype that stores values. SETS are another standard dtatype that also store values, The major difference is SETS, unlike TUPLES cannot have multiple occurances of the same element and store unordered values. Moreover, TUPLES are immutable while SETS are mutable.

## What are python datatype?
Numeric(Integer, Float, COmplex number) type datatypes, Boolean(True, False) type datatypes, Sequence(String, List, Tuple) type datatypes, Dictionary type datatypes. So, mainly 6 std. datatypes: Numeric, String, List, Tuples, Boolean and Dictionary.

## Why choose Python?
Less Code, Less Time, Less Money: Python typically involves less code, it also takes less time to complete a job. Thankfully for clients this also means less money. It allows developers to work quickly. 2.Utilized by World Leaders: World leading companies are increasingly choosing python. Of course, the vast majority of IT giants, including Google, Dropbox, Spotify are using it. Other industry giants as well choosing python as preferential language: NASA, Disney, Electronic Arts etc.
Compatible: Python offers compatibility with various platforms and moreover, its free.
Huge Libraries: There are a lot of libraries for Python. As a result, the developers can manage documentation, databases, web browsers, perform unit testing and so on. Additionally, Python can be used for many taks: web and desktop apps development, complex calculation systems, life support management systems, Internet of Things, games and more.
Can we add items in tuples dynamically?
Some tuples(that contain only immutable objects such as strings) are immutable and some other tuples(that contain one or more objects such as lists) are mutable. This is often debatable topic however tuples are immutable in general. You can't add elements to a tuple because of it's immutable property. There is no append() or extend() method for tuples. Similarly, You can't remove elements froma tuple because of it's immutable property. tuples have no remove() or pop() method.

## Python supports compilition or NOT?
Yes indeed compilation is a step in executing a souce code. Our source code is compiled into bytecode. CPython comiles our source code here.

## What are Python arrays?
Arrays in python are data structures that can hold multiple values of the same type. Often, they are misinterpreted as lists or Numpy Arrays. Technically, Arrays in Python are distinct from both these. An array is basically a data structures which can hold more than one value, an ordered series of the same type. Arrays are mutable so we can perform various manipulations as required.

Python Arrays and lists store values in a similar way.But, there is a key difference between the two. A list can store any type of values such as integers, strings etc While An array on the other hand, stores single data type values. For example you have array of integers, an array of strings etc.

Arrays in python can be created after importing the array module as follows: import array as arr The array(data type, value list) function takes two parameters, the first being data type of the value stored, the second being the value list. There is another way to import: from array import*

## Explain object in Python?
An object is an instance of a Class. An object consists of: State: Represented by attributes of an object. Also reflects the properties of an object. Behaviour: Represented by methods of an object. Also reflects the response of an object with other objects. Identity: Gives unique name to an object to interact with other objects.

## Example of real-world class in Python?
```Python3 {
  Class NITTirchy:
      "This is a class"
      estd_date = 1961

      def courses(self):
          print("Computer Science")

          print("Electronics and Instrumentation")

          print("Mechanical")

          print("Civil")
 print(NITTirchy.estd_date)

 print(NITTirchy.courses)
} ```
