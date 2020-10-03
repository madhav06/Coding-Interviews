# Coding-Interviews
Brainstorm coding problems here and questions asked in live Interviews.

## What is ByteCode in Python?
Let's understand how python runs our programs. Python is usually called an interpreted language, however, it combines compiling and interpreting. When we execute a source code(that is a .py file), python first compiles it into a bytecode. The bytecode is a low-level platform-independent representation of your source code, however, it is not the binary machine code and cannot be run by the target machine directly. In fact, it is a set of instructions for a virtual machine which is called the Python Virtual Machine(PVM). After compilition, the bytecode is sent for execution to the PVM. The PVM is an interpreter that runs the bytecode and is part of the python system. The bytecode is platform-independent. Here, CPython compiles the source code into the bytecode and then this bytecode is executed by the CPython virtual machine.

## What is difference between SETS and TUPLES?
TUPLES are a datatype that stores values. SETS are another standard dtatype that also store values, The major difference is SETS, unlike TUPLES cannot have multiple occurances of the same element and store unordered values. Moreover, TUPLES are immutable while SETS are mutable.
