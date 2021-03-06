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
}
```

## Python supports polymorphism or NOT?
Yes, Python support polymorphism. Polumorphism can be carried out through inheritance, with sub classes making use of base class methods or overriding them. Two types of polymorphism: --- Overloading --- Overriding
``` Python3 {
Example:

class Fish():
    def swim(self):
        print("fish swims")

    def swim_backward(self):
        print("fish can swim backwards")

    def skeleton(self):
        print("fish skeleton is made of cartilage")

class ClownFish():

    def swim(self):
        print("the clown fish swims")

af = Fish()
af.skeleton()
bf = ClownFish()
bf.swim()

}
```

## Does Python supports constructor?
Constructors are generally used for instantiating an object. The task of constructors is to initialize to the data members of the class when an object of class is created. In Python the 'init()' method is called as constructor and is always called when an object is created.
``` Python3 {
Syntax:

def __init__(self):
#body of the constructor


Example:
class GeekHour:
# default constructor
def __init__(self):
    self.geek = 'Geek Hours'

# method for printing data members
def print_Geek(self):
    print(self.geek)

# creating object of the class
obj = GeekHour()

# calling the instance method
obj.print_Geek()
}
```
Types of constructors:
default: A simple constructor which doesn't accept any arguments. it's definition has only one arguments which is a reference to the instance being constructed.

parameterized: constructor with parameters is known as parameterized constructor. first args as a reference to the instance being constructed known as self and rest of the arguments are provided by the programmer.

``` Python3 {
# Example of default constructor

class CodingNinja:
    # default constructor
    def __init__(self):
        self.geek = 'Coding Ninja Geeky Hour Begins'

    # a method for printing data members
    def print_Geek(self):
        print(self.geek)

# creating object of the class
obj = CodingNinja()

# calling the instance method using the object ->> obj
obj.print_Geek()

# <---                                           Code Break                                              --->
# <---                                           Code Break                                               --->


# Example of parameterized constructor:

class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print('First number = ' + str(self.first))

        print('Second number = ' + str(self.second))

        print('Addition of two = ' + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

# creating object of the class
# this will invoke the parameterized constructor

obj = Addition(1000, 2000)

# perform addition
obj.calculate()

# display result
obj.display()
}
```
## Where lambda operator will be used in Python3?
Lambda operator or lambda function is a way to create small anonymous functions, functions without a name. These functions are throw-away functions, they are needed where they have been created. They are mainly used in combination with the functions filter(), map() and reduce(). Lambda functions are syntactically restricted to a single expression.

## Program to find average of numbers in a list.
Can you write a python program to find the average of numbers in a list?

## Program to reverse a number in python.
Can you write a python program to reverse a number?

## Program to find the sum of the digits of a number in python.
Can you write a program to find the sum of the digits of a number in python?

## Program to check if a number is palindrome or not.
Can you write a program to check if a number is a palindrome or not.

## Program to count the number of digits in a number.
Can you write a program to count the number of digits in a number?

## Program to check if a number is a prime number.
Can you write a program to check if a number is a prime number?

Prime Number: Prime numbers are whole numbers greater than 1, that have only two factors - 1 and number itself.
first few prime numbers are: 2,3,5,7,11,13,17,19,23,29,31,37.

## Program to check if a number is an armstrong number.
Can you write a program to check if a number is an armstrong number?

Armstrong number: armstrong number is a numner that is equal to the sum of cubes of its digits.
example: 0, 1, 153, 370, 371, 407
153 = 1*1*1 + 5*5*5 + 3*3*3
370 = 3*3*3 + 7*7*7 + 0*0*0
371 = 3*3*3 + 7*7*7 + 1*1*1
470 = 4*4*4 + 7*7*7 + 0*0*0

## Program to check if a number is a perfect number.
Can you write a program to check if a number is a perfect number?

Perfect number: A positive integer that is equal to the sum of its proper divisors.
example: 6, 28, 496, 8128 etc

## Algorithms to solve before python coding round:
"Knowing how to solve algorithms will give you a competitive advantage during job hunt".

Please note that the solution I shared for each problem is just one of many patential solutions,
 That could be implemented and therefore feel free to code your own versions.

 Problem 1: Average Words Length

``` Python3 {
	
	sentence1 = "Hi all, I'm Madhav Nandan, I live in India"
	sentence2 = "I love this programming thing and I aspire to open my own startup"

	def solution(sentence):
	    for p in "!?',;.":
	        sentence = sentence.replace(p, '')

	    words = sentence.split()
	    return round(sum(len(word) for word in words)/len(words),2)

	print(solution(sentence1))
	print(solution(sentence2))

# Expected output: 4.2
# Expected output: 4.08
}
```

Probelm 2: Move Zeroes

``` Python3 {

	# Given an array nums, write a fun to move all zeroews to end
	array1 = [0,1,0,3,12]
	array2 = [1,7,0,0,8,0,10,12,0,4]

	def solution(nums):
	    for i in nums:
	        if 0 in nums:
	            nums.remove(0)
	            nums.append(0)
	    return nums

	solution(array1)
	solution(array2)

# Expected output: [1,3,12,0,0]
# Expected output: [1,7,8,10,14,4,0,0,0,0]
}
```

Problem 3: Matched and Mismatched Words

``` Python3 {
	
	# Given two sentences, return an array that has words that appear in one sentence,
	# and not the other and array with the words in common.

	sentence1 = "We are really pleased to meet you in our city"
	sentence2 = "The city was hit really hard last night by earthquake"

	def solution(sentence1, sentence2):
	    set1 = set(sentence1.split())
	    set2 = set(sentence2.split())

	        return sorted(list(set1^set2)), sorted(list(set1&set2))

	print(solution(sentence1, sentence2))

# Expected output: (['The','We','a','are','by','heavy','hit','in','meet','our',
#   'pleased','storm','to','was','you'],
# ['city', 'really']) 
}
```

Problem 4: Fill The Blanks

``` Python3 {
	
	# Given array containing None values fill in None with the most recent
	# non None value in the array 

	array1 = [1, None, 2, 3, None, None, 5, None]

	def solution(array):
	    valid = 0
	    res = []

	    for i in nums:
	        if i is not None:
	            res.append(i)
	            valid = i
	        else:
	            res.append(valid)
	    return res

	solution(array1)

# Expected output: [1, 1, 2, 3, 3, 3, 5, 5]
}
```

## Django Framework

#### What is Django framework ?

Django is high-level python Web Framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development. 
Note: A Web Framework is a collection of tools together in one package that developers can use to build web applications.

#### Features of Django

What is ORM - OBJECT-RELATIONAL-MAPPING, a tool django comes with. Which grealty help us in making database queries.

URL Routing - It help us determining logic based on URL configured.

HTML Templating - Allows us to define and make some presentation logic, insert some dynamic data in our HTML.

Form Handling - A default django features that help us create forms, manage form data and perform validations.

Unit Testing - A standard library module django comes with. This module defines tests using class-based approach.

#### Easiest Way to Install Django

``` Python3 {
	$ pip3 install django==3.0.3
}
```

####  Create a Django project

``` Python 3 {
	# I have project directory on desktop, so first I navigate to that.
	# Then ls to make sure it has django-admin, django manage.py etc
	# Let's follow instructions now.

	$ cd desktop/learning-django
	$ ls
	$ django-admin startproject <projectname>
	$ django-admin startproject wisdompets
} 
```

Screenshot:
![GitHub](https://github.com/madhav06/projectImages/blob/master/install_django.png)

Everything you need to know about django core files:

https://whimsical.com/django-project-6n9oC7gMi9cxYf2BX4xGoB

#### What are Django Apps?

A component in a django project. It is a folder with a set of python files. Each django app supplies a related feature that fits a specific purpose. In overall project, we might have one or many apps.

#### Create a Django app

``` python3 {
	# make sure you are in <your> project dir such that 
	# if you 'ls' (list them), you see manage.py
	$ ls
	$ manage.py wisdompets
	#now to create a django app
	$ python3 manage.py startapp adoptions
	# this will create a new django app inside your proj
	# to verify, open VS Code
	$ code .
}
```

In settings.py file, Add in INSTALLED_APPS = ['adoptions' + preinstall as it is]: We add this because we created this new django app and other apps are here because they are pre-installed and they come default with django.

What are the functions 'Pieces of an App' do ? : Here is the link that properly describes what each pieces do: https://whimsical.com/pieces-of-an-app-Rdo8B4sgzaeAKiogXAebT1

MVC Architecture in Django: 

A detailed overview: https://whimsical.com/mvc-architecture-of-django-YDnK7yge5fS68X4Epn6RrU

What is a Django Model: A model is a class inheriting from django.db.models.Model and it defines database fields as class attributes.

``` Python3 {
	from django.db import models

	class Pet(models.Model):
	    name = models.CHarField(max_length = 100)
	    submitter = models.CharField(max_length = 100)
	    submission_date = models.DateTimeField()
	    description = models.TextField(blank=True)

}
```

What migrations do in django ?

Migrations: migrations are responsible for creating the necessary scripts to change this structure through time as we update our code to change our models.

Several cases when a migration is needed:

-- Adding a Model
-- Adding a Field
-- Removing a Field
-- Changing a Field

A migration creates the corresponding database table. migrations are also needed when a field is added, removed or an existing field is changed.

``` Python3 {
	# Commands for working with migrations are:
	$ python3 manage.py makemigrations
	$ python3 manage.py showmigrations
	$ python3 manage.py migrate
}
```

#### When and Why we use Django-Admin ?

The Django admin application can use our models to automatically build a site area that we can use to create, view, update and delete records. This way we can save time a lot and test our models and get a feel for whether we have the right data or not.

The admin application can also be useful for managing data in production, depending on the type of websites. 

#### A word on Template Syntax.

Syntax for a template has 3 pieces:
-- {{ variable }}
-- {% tag %}
-- {{ variable | filter }}

``` Python3 {
	# example of variable,
	{{variable}} == <h3> {{pet.name}} </h3>

	# example of variable filter,
	{{variable|filter}} == <h3>{{pet.name | capfirst}} </h3>

	# loopsin templates
	{% for pet in pets %}
	    <li> {{ pet.name }} </li>
	 {% endfor %}

}
```

## Elasticsearch (ELK Stack)

#### what is index in elasticsearch?

An index is like a 'database' in a relational database. It has mapping which defines multiple types.  So, We can rougly think of an index like a database.

**MySQL-->Database-->Tables-->Columns/Rows**

**Elasticsearch -->Indices --> Types --> Documents with Properties**

Elasticsearch cluster can contain multiple Indices(database), which in turn contain multiple Types(tables). These types can have multiple documents(rows), and each documents has properties(columns).

Elasticsearch allows us to query multiple indices at the same time.  Indices are very lightweight data organization mechanisms, so elasticsearch will happily let us create hundreds of indices.

Then, searching and querying take format of:
**http://localhost:9200/[index]/[type]/[operation]**

#### what are shards in elasticsearch?

A **shard** is a atomic unit of elasticsearch. shards can be thought as single lucene index that can be hosted anywhere in cluster. They are building blocks of elasticsearch and what facilitate its scalability.

We can use shards is our index size is too large it is about to crash. the one solution we can use here is:

We can split up the indices into pieces of shards, allowing us to distribute operations across shards and nodes to improve performance. When creating index we can define actually how many shards we want.
```
curl -XPUT localhost:9200/example -d '{
    "setting": {
        "index": {
            "number_of_shards": 2,
            "number_of_replicas": 1
        }
    }
}'
```
#### what are replicas in elasticsearch?

They are fail-safe mechanisms and are basically copies of index's shards. Helpful backup system and a good feature elasticsearch has to offer.

When a node fail or crashes, then adding a replica can help us in increasing search performance.
The number of replicas can be defined while creating index, however we can change the number of shards anytime after that.

#### When is flask used and when django for web apps?

We use flask for simple projects where we don't need the power/complexity that django offers. Django has template system, ORM and a lot of other good stuffs. Django is used over flask when we want to use a complete, powerful, well documented system that works together very well.

We use flask if we just want to build an API backend without a lot of things that django has to offer, a basic static site or something that is mostly powered by third-party technology.

If the backend is NoSQL - flask use
For RESTful API - use flask
Need CMS with feature loded - Use django
Need limited admin interface - Use django

#### Why is Python integer size bigger than the integer in C?

Unlike C, Python int are objects that use an internal data structure for storage. It's completely different from basic arithmatic types such as int, real numer etc.

for example, whenever Python finds an assignment like **x = 1**, it tries to construct an integer object. This is done using following data structure:
```
typedef struct {
    PyObject_HEAD
    long ob_ival;
    
} PyIntObject;
```
#### Mutable, Immutable in Python?

Mutable is fancy way of saying that internal state of object is changed. Immutable doesn't allow any changes in the object once it is created.

Mutable  Objects:
 **Lists,**
 **Sets,**
 **Dictionaries,**
 **User-Defined Classes**
 
 |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
 
 Immutable Objects:
 **Strings,**
 **Tuples,**
 **Frozen Sets,**
 **User-Defined Classes***
 
 NOTE: - In Python everything is object. Every object has three attributes.
 
 Identity - This refers to the address that the object refers to in the computer memory
 
 Type - This refers to the kind of object that is created.
 
 Value - This refers to the value stored by the object.
 
 #### Elasticsearch VS MongoDB, which is best suited for distributed enviroment ?
 
 Both these technologies Manage NoSQL data that are highly scalable and have well document-oriented design at the core. 
 
 Elasticsearch is primarily a search server while MongoDB is primarily a database. 
 
 Full-text search is requirement - Elastic is good
 Look log analytics - Elastic is good
 Need tokenizer - Elastic is good
 Maximum document size - 100 MB
 Written in Java
 
 However, 
 
 Data is NoSQL format - MongoDB is good
 Need CRUD Op Without Full-text search - MongoDB is good
 Maximum document size - 16MB
 Written in C++
 
 #### decorators in python?
 
 A decorator takes in a function, adds some functionality and return it. Very powerful and useful tool in Python sice it allows programmers to modify the behaviour of function or class.
 
 #### Can we use lists in dictionary as key?
 
 A dictionary key must be of type 
 
}
}
}












