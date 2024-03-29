# Coding-Interviews

Brainstorm coding problems here and questions asked in live Interviews.

## Top 50 React Interview Questions?

React is considered as fastest growing javascript framework. Being a clear winner for front-end developers across the globe, the demand for react developers are increasing exponentially. With all that in mind, here is a set of questions that helpm you nail the react-interview.

#### Difference b/w Real DOM and virtual DOM.

Real DOM - It updates slow. Can directly update HTML. It creates a new DOM if element updates. Here, too much of memory wastage ans the DOM manipulation is very expensive.

Virtual DOM(Document Object Model) - It updates faster. Here we can't update HTML directly. It updates JSX, if element updates. Here, DOM manipulation is easy and no memory wastage as such.

#### What is React, what are its features?

React is frontend JS library developed by FB in 2011. It is used for developing complex and interactive web and mobile UI. It follows the component based approach which helps in building reusable UI components. Has one of the largest community to support.

Featurs:
Uses Virtual DOM instead of Real DOM. Uses server-side rendering. It follows uni-directional data flow.

#### Limitations of React

React is just a library, not a full-blown framework. Its library is very large and takes time to understand. Can be difficult for novice programmers to understand. Coding in React is complex as it uses inline templating and JSX.

#### Advantages of Using React

It increases the application performance. Can be conveniently used on the client as well as server side. Code readability is good due to JSX, easy to integrate with frameworks like Meteor, ANgular etc. Using react, writing UI test cases become extremely easy.

#### What is JSX?

Shorthand for JavaScript XML. JSX makes application robust and boost its performance. They help in understanding HTML file really easy.

```jsx
render() {
	return(
		<div>
		  <h1>Hi There! </h1>
		</div>
	);
}
```

#### Why can't browser read JSX?

Since JSX is not regular JavaScript object and browsers can read only JavaScript objects. Thus to make sure browser read JSX, we transform JSX file into JavaScript objects using jSX transformers like babel and then pass it to the browser.

#### How different is ES6 from ES5?

Syntax has changed in following aspects:

```jsx
/*1. require vs import */
//ES5
var React = require("react");
//ES6
import React from "react";

/* 2. export vs exports */
//ES5
module.exports = Component;
//ES6
export default Component;

/* 3. component vs function */
//ES5
var MyComponent = React.createClass({
  render: function () {
    return;
    <h3>Hello family! </h3>;
  },
});

//ES6
class MyComponent extends React.Component {
  render() {
    return;
    <h3>Hello Family! </h3>;
  }
}

/* props */

//ES5
var App = React.createClass({
  propTypes: { name: React.propTypes.string },
  render: function () {
    <h3>Hello, {this.props.name}!</h3>;
  },
});

//ES6
class App extends React.Component {
  render() {
    return;
    <h3>Hello, {this.props.name}!</h3>;
  }
}

/* state */

// ES5
var App = React.createClass({
  getInitialState: function () {
    return { name: "world" };
  },
  render: function () {
    return;

    <h3>Hello, {this.state.name}!</h3>;
  },
});

// ES6
class App extends React.Component {
  constructor() {
    super();
    this.state = { name: "world" };
  }
  render() {
    return;

    <h3>Hello, {this.state.name}!</h3>;
  }
}
```

#### How Virtual DOM works?

A virtual DOM is a lightweight JavaScript object which originally is just the copy of the real DOM. It is a node tree that lists the elements, their attributes and content as Objects and their properties.
React’s render function creates a node tree out of the React components. It then updates this tree in response to the mutations in the data model which is caused by various actions done by the user or by the system.

This Virtual DOM works in three simple steps:

1. Whenever any underlying data changes, the entire UI is re-rendered in Virtual DOM representation.

2. Then the difference between the previous DOM representation and the new one is calculated.

3. Once the calculations are done, the real DOM will be updated with only the things that have actually changed.

#### In React, everything is component. Explain.

Components are the building blocks of React application's UI. These components split up the entire Ui into small independent and resuable pieces. Then, it renders each of these components independent of each other without affecting the rest of the UI.

#### What is the purpose of render( ) in React.

Each React component must have a render( ) as mandatory. It returns a single React element which is the representation of the native DOM component. If more than one HTML element needs to be rendered, then they must be grouped together inside one one enclosing tag such as: <form>, <div>, <group> etc. It must return the same result each time when it is invoked.

#### How to embed two or more components into one?

We can do this following way:

```jsx
class MyComponent extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello </h1>
        <Header />
      </div>
    );
  }
}

class Header extends React.Component {
  render() {
    return;
    <h1>Header Component </h1>;
  }
}

ReactDOM.render(<MyComponent />, document.getElementById("content"));
```

#### What is Props?

Shorthand for Properties in React. They are read-only components which must be kept pure. They are always passed down from the parent to child components throughout the application. **A\*\*** child component can never send a prop back to the parent component. This helps in maintaing uni-directional data flow and generally used to render generated data dynamically.

#### What's State in React.

States are heart of React Components. States can be kept as simple as possible. Basically, States are the objects which determine components rendering and behaviour. They are mutable unlike props and create dynamic components. accessed via this.state( ).

#### Difference b/w states and props?

| Conditions                                  | State | Props |
| ------------------------------------------- | ----- | ----- |
| Receive initial value from parent component | Yes   | Yes   |
| ------------------------------------------- | ----- | ----- |
| Parent component can change value           | No    | Yes   |
| ------------------------------------------- | ----- | ----- |
| Set default values inside component         | Yes   | Yes   |
| ------------------------------------------- | ----- | ----- |
| Changes inside component                    | Yes   | No    |
| ------------------------------------------- | ----- | ----- |
| Set initial value for child components      | Yes   | Yes   |
| ------------------------------------------- | ----- | ----- |
| Changes inside child components             | No    | Yes   |
| ------------------------------------------- | ----- | ----- |

#### How you update the state of a component?

can be updated using **this.setState()**

```jsx
class MyComponent extends React.Component {
  constructor() {
    super();
    this.state = {
      name: "Madhav",
      id: "101",
    };
  }
  render() {
    setTimeout(() => {
      this.setState({ name: "Rehan", id: "222" });
    }, 2000);
    return (
      <div>
        <h1>Hello {this.state.name}</h1>
        <h2>Hello {this.state.name}</h2>
      </div>
    );
  }
}
ReactDOM.render(<MyComponent />, document.getElementById("content"));
```

#### What is arrow function in React? How it is used?

Arrow functions are brief syntax for writing the function expression. 'fat arrow(=>) the function'. These allow to bind the context of the components properly in ES6. Mostly used while working with higher order functions.

#### what is React Fragment?

It's a common pattern in React which is used for a component to return multiple elements. Fragments let you group a list of children without adding extra nodes to the DOM.

```jsx
render() {
  return (
    <React.Fragment>
      <ChildA />
      <ChildB />
      <ChildC />
    </React.Fragment>
  )
}

```

#### Why using Fragments is better Option over Divs?

1. Fragments are a bit faster and use less memory by not creating an extra DOM node. This only has a real benefit on very large and deep trees.

2. The DOM Inspector is less cluttered.

#### What is lifecycle methods order in mounting?

The lifecycle methods are called in the following order when an instance of component is being created.

```jsx
//constructor()
//static getDerivedStateFromProps()
//render()
//componentDidMount()
```

#### Why should component names start with capital letter?

If you are rendering your component using JSX, the name of that component has to begin with a capital letter otherwise React will throw an error as unrecognized tag.

#### What is React.createClass?

React.createClass allows us to generate component "classes". But with ES6, React allows us to implement component classes that use ES6 JavaScript classes. The end result is the same -- we have a component class. But the style is different. And one is using "custom" JavaScript class system while the other is using "native" JavaScript class system. When using React's **createClass()** method, we pass in an object as an argument. So, we can write a component using **createClass** that looks like this:

```jsx
import React from "react";
const Contacts = React.createClass({
  render() {
    return <div></div>;
  },
});
export default Contacts;
```

#### Difference B/W Stateful and Stateless Components.

| Stores info about component's state change in memory. | Calculates the internal state of the components |
| ----------------------------------------------------- | ----------------------------------------------- |

| Have authority to change state. | Do not have authority to change state |
| ------------------------------- | ------------------------------------- |

| Contains info of past, current and possible future changes in state | Contains no such info as such |
| ------------------------------------------------------------------- | ----------------------------- |

| Stateless components notify them about the requirements of the state change, then they send down props to them | They receive the props from the Stateful components and treat them as callback functions. |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |

#### Different phases of React component's lifecycle?

1. Initial Rendering Phase: This is phase when the component is about to start its life journey and make its way to the DOM.

2. Updating Phase: Once the component gets added to DOM, it can potentially update and re-render only when a prop or state change occurs.

3. Unmounting Phase: This is the final phase of a computer's life cycle in which the component is destroyed and removed from the DOM.

#### What is React Router?

React Router is a powerful routing library built on top of React that helps you add new screens and flows to your application incredibly quickly, all while keeping the URL in sync with what's being displayed on the page.

#### Lifecycle methods of React components

**_componentWillMount( )_** - Executed just before rendering takes place both on client as well as server-side.

**_componentDidMount( )_** - Executed on the client side only after the first render.

**_componentWillReceiveProps( )_** - Invoked as soon as the props are received from the parent class and before another render is called.

**_shouldComponentUpdate( )_** - Returns true or false value based on certain conditions. If want to update, return true else return false.

**_componentWillUpdate( )_** - Called just before rendering takes placein DOM.

**_componentDidUpdate( )_** - Called immediately after rendering takes place.

**_componentWillUnmount( )_** - Called after the component is unmounted from the DOM. It is used to clear up the memory spaces.

#### What is constructor? and purpose for it?

Constructor are used for:

- Initializing values of - props and state
- Binding event handler methods to an instance

```jsx
import React, { Component } from "react";
class myComponent extends Component {
  constructor(props) {
    super(props);
    // Don't call this.setState( ) here!
    this.state = { counter: 0 };
    this.handleClick = this.handleClick.bind(this);
  }
}
```

- Constructor is called only once in the complete lifecycle of a component.
- Constructor is the only place where you should assign **this.state** directly. In Other React's Lifecycle methods, you should use **this.setState( )**.
- If using constructor, you should call **super(props)** before any other statement. If you won't call **super(props)**, this.props will be undefined in the component, which can lead to bugs.

#### reducers in react?

A reducer is a function that determines changes to an application's state. We have tools like Redux, that help manage an application's state change in a single store.

#### Purpose of ContextAPI in react?

If a child component at nth level require a property from a parent component at any level, the information needs to be passed one level by level through props. In an application with lot of nested components, it is difficult.

Context API helps to directly send an information from a parent component to a child component at any level.

#### Explain React Hooks?

Hooks are built-in functions that allow developers to use state and lifecycle methods within component in React. Each component's lifecycle has 3 phases which are mount, unmount and update. Alongside, components have states and props So, Hooks allow developers to use these methods while improving code reuse across component tree.

#### 2 Rules that must be followed using Hooks?

1. Hooks should be called only at the Top Level. Shouldn't be called inside loops, nested functions or conditions.

2. Hooks can only be called from React Function Component.

#### Primary benefits of Hooks?

Through Hooks, you can code in React without using classes. With Hooks, we can re-use exisiting states in our code. Can also help in tightly couple logic in the code.

#### what is Redux?

It is a conventional shape container for JavaScript apps and based on Flux design pattern.small and has no dependancies.

#### Where Redux is used?

Redux is majorly used in a mixture with reacting. Has capability to get used to other view libraries too. Angular, Vue can get mutual with Redux easily.

#### Redux Thunk, Explain?

Known as middleware

#### What is redux-saga?

Documentation that aims to make elevation effects in redux app easier.

#### Main features of redux form?

-- Justification (sync / async) and compliance.
-- Field values determination via redux store.
-- Formatting, normalization and parsing of field standards.

#### Why we use force update in React?

We use force update to power a re-render if there is some form, React is not detecting that requires a revision to UI.

---

## Backend questionnaire on Python, Django etc

---

#### What is ByteCode in Python?

Let's understand how python runs our programs. Python is usually called an interpreted language, however, it combines compiling and interpreting. When we execute a source code(that is a .py file), python first compiles it into a bytecode. The bytecode is a low-level platform-independent representation of your source code, however, it is not the binary machine code and cannot be run by the target machine directly. In fact, it is a set of instructions for a virtual machine which is called the Python Virtual Machine(PVM). After compilition, the bytecode is sent for execution to the PVM. The PVM is an interpreter that runs the bytecode and is part of the python system. The bytecode is platform-independent. Here, CPython compiles the source code into the bytecode and then this bytecode is executed by the CPython virtual machine.

#### What is difference between SETS and TUPLES?

TUPLES are a datatype that stores values. SETS are another standard dtatype that also store values, The major difference is SETS, unlike TUPLES cannot have multiple occurances of the same element and store unordered values. Moreover, TUPLES are immutable while SETS are mutable.

#### What are python datatype?

Numeric(Integer, Float, COmplex number) type datatypes, Boolean(True, False) type datatypes, Sequence(String, List, Tuple) type datatypes, Dictionary type datatypes. So, mainly 6 std. datatypes: Numeric, String, List, Tuples, Boolean and Dictionary.

#### Why choose Python?

Less Code, Less Time, Less Money: Python typically involves less code, it also takes less time to complete a job. Thankfully for clients this also means less money. It allows developers to work quickly. 2.Utilized by World Leaders: World leading companies are increasingly choosing python. Of course, the vast majority of IT giants, including Google, Dropbox, Spotify are using it. Other industry giants as well choosing python as preferential language: NASA, Disney, Electronic Arts etc.
Compatible: Python offers compatibility with various platforms and moreover, its free.
Huge Libraries: There are a lot of libraries for Python. As a result, the developers can manage documentation, databases, web browsers, perform unit testing and so on. Additionally, Python can be used for many taks: web and desktop apps development, complex calculation systems, life support management systems, Internet of Things, games and more.

#### Can we add items in tuples dynamically?

Some tuples(that contain only immutable objects such as strings) are immutable and some other tuples(that contain one or more objects such as lists) are mutable. This is often debatable topic however tuples are immutable in general. You can't add elements to a tuple because of it's immutable property. There is no append() or extend() method for tuples. Similarly, You can't remove elements froma tuple because of it's immutable property. tuples have no remove() or pop() method.

#### Python supports compilition or NOT?

Yes indeed compilation is a step in executing a souce code. Our source code is compiled into bytecode. CPython comiles our source code here.

#### What are Python arrays?

Arrays in python are data structures that can hold multiple values of the same type. Often, they are misinterpreted as lists or Numpy Arrays. Technically, Arrays in Python are distinct from both these. An array is basically a data structures which can hold more than one value, an ordered series of the same type. Arrays are mutable so we can perform various manipulations as required.

Python Arrays and lists store values in a similar way.But, there is a key difference between the two. A list can store any type of values such as integers, strings etc While An array on the other hand, stores single data type values. For example you have array of integers, an array of strings etc.

Arrays in python can be created after importing the array module as follows: import array as arr The array(data type, value list) function takes two parameters, the first being data type of the value stored, the second being the value list. There is another way to import: from array import\*

#### Explain object in Python?

An object is an instance of a Class. An object consists of: State: Represented by attributes of an object. Also reflects the properties of an object. Behaviour: Represented by methods of an object. Also reflects the response of an object with other objects. Identity: Gives unique name to an object to interact with other objects.

#### Example of real-world class in Python?

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

#### Python supports polymorphism or NOT?

Yes, Python support polymorphism. Polumorphism can be carried out through inheritance, with sub classes making use of base class methods or overriding them. Two types of polymorphism: --- Overloading --- Overriding

```Python3 {
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

#### Does Python supports constructor?

Constructors are generally used for instantiating an object. The task of constructors is to initialize to the data members of the class when an object of class is created. In Python the 'init()' method is called as constructor and is always called when an object is created.

```Python3 {
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

```Python3 {
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

#### Where lambda operator will be used in Python3?

Lambda operator or lambda function is a way to create small anonymous functions, functions without a name. These functions are throw-away functions, they are needed where they have been created. They are mainly used in combination with the functions filter(), map() and reduce(). Lambda functions are syntactically restricted to a single expression.

#### Program to find average of numbers in a list.

Can you write a python program to find the average of numbers in a list?

#### Program to reverse a number in python.

Can you write a python program to reverse a number?

#### Program to find the sum of the digits of a number in python.

Can you write a program to find the sum of the digits of a number in python?

#### Program to check if a number is palindrome or not.

Can you write a program to check if a number is a palindrome or not.

#### Program to count the number of digits in a number.

Can you write a program to count the number of digits in a number?

#### Program to check if a number is a prime number.

Can you write a program to check if a number is a prime number?

Prime Number: Prime numbers are whole numbers greater than 1, that have only two factors - 1 and number itself.
first few prime numbers are: 2,3,5,7,11,13,17,19,23,29,31,37.

#### Program to check if a number is an armstrong number.

Can you write a program to check if a number is an armstrong number?

Armstrong number: armstrong number is a numner that is equal to the sum of cubes of its digits.
example: 0, 1, 153, 370, 371, 407
153 = 1*1*1 + 5*5*5 + 3*3*3
370 = 3*3*3 + 7*7*7 + 0*0*0
371 = 3*3*3 + 7*7*7 + 1*1*1
470 = 4*4*4 + 7*7*7 + 0*0*0

#### Program to check if a number is a perfect number.

Can you write a program to check if a number is a perfect number?

Perfect number: A positive integer that is equal to the sum of its proper divisors.
example: 6, 28, 496, 8128 etc

#### Algorithms to solve before python coding round:

"Knowing how to solve algorithms will give you a competitive advantage during job hunt".

Please note that the solution I shared for each problem is just one of many patential solutions,
That could be implemented and therefore feel free to code your own versions.

**Problem 1: Average Words Length**

```Python3 {

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

**Probelm 2: Move Zeroes**

```Python3 {

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

**Problem 3: Matched and Mismatched Words**

```Python3 {

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

**Problem 4: Fill The Blanks**

```Python3 {

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

#### Django Framework

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

```Python3 {
	$ pip3 install django==3.0.3
}
```

#### Create a Django project

```Python 3 {
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

```python3 {
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

```Python3 {
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

```Python3 {
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

```Python3 {
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
