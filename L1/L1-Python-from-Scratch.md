
# Python from Scratch

## About Python

Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale.

The language Python is named after the BBC show _Monty Python’s Flying Circus_ and has nothing to do with reptiles.

Python supports multiple programming paradigms, including _object-oriented_, _imperative_ and _functional programming_ or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.


Python was conceived in the late 1980s, and its implementation was started in December 1989 by Guido van Rossum at CWI in the Netherlands as a successor to the ABC language (itself inspired by SETL) capable of exception handling and interfacing with the Amoeba operating system. Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, benevolent dictator for life.



## Features

The core philosophy of the language is summarized by the document "PEP 20 (The Zen of Python)", which includes aphorisms such as:

- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Readability counts

Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:

- the high-level data types allow you to express complex operations in a single statement;
- statement grouping is done by **indentation** instead of beginning and ending brackets;
- no variable or argument declarations are necessary.

Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the interpreter, either to perform critical operations at maximum speed, or to link Python programs to libraries that may only be available in binary form (such as a vendor-specific graphics library). Once you are really hooked, you can link the Python interpreter into an application written in C and use it as an extension or command language for that application.


## Installing Python

On Linux machine, Python is usually installed by default. To install Python on other systems, check out the [Python Setup and Usage section in Python help documentation](https://docs.python.org/2.7/using/index.html).

## Using Python

The Python interpreter is usually installed as `/usr/bin/python` on those machines where it is available.

- To start a Python interpreter, type the command in your terminal: `python`.

- To terminate the Python interpreter, type an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.

```
fli@carbon:~$ python
Python 2.7.9 (default, Mar  1 2015, 12:57:24) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

### Executing Python scripts

1. Write down your pyton scrpt and name it as `hello.py` with `.py` extension

2. Your script contents look like this 

```
#!/usr/bin/python

print('Hello World')
```

3. Go to your terminal, make your script excutable

```
chmod +x hello.py
```

4. Run the script in your terminal

```
./hello.py
```

### Using IPython shell

IPython is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers introspection, rich media, shell syntax, tab completion, and history. IPython provides the following features:

- Interactive shells (terminal and Qt-based).
- A browser-based notebook with support for code, text, mathematical expressions, inline plots and other media.
- Support for interactive data visualization and use of GUI toolkits.
- Flexible, embeddable interpreters to load into one's own projects.
- Tools for parallel computing.


To start iPython interactive environment, type `ipython` in your terminal.

## Getting help

- Help is available in IPython sessions using `help( function )` . 

- Some functions (and modules) have very longhelp files. When using IPython, these can be paged using the command `? function` or `function ?` so that the text can be scrolled using page up and down and `q` to `quit`. `??function` or `function??` can be used to type the entire function including both the docstring and the code.

## Libraries

Python has a large standard library, commonly cited as one of Python's greatest strengths, providing tools suited to many tasks. This is deliberate and has been described as a "batteries included" Python philosophy. For Internet-facing applications, a large number of standard formats and protocols (such as MIME and HTTP) are supported. Modules for creating graphical user interfaces, connecting to relational databases, pseudorandom number generators, arithmetic with arbitrary precision decimals,[69] manipulating regular expressions, and doing unit testing are also included.

Some parts of the standard library are covered by specifications, but the majority of the modules are not. They are specified by their code, internal documentation, and test suite (if supplied). However, because most of the standard library is cross-platform Python code, there are only a few modules that must be altered or completely rewritten by alternative implementations.

The standard library is not essential to run Python or embed Python within an application. Blender 2.49, for instance, omits most of the standard library.

As of August 2015, the Python Package Index, the official repository of third-party software for Python, contains more than 65,000 packages offering a wide range of functionality, including:

- graphical user interfaces, web frameworks, multimedia, databases, networking and communications
- test frameworks, automation and web scraping, documentation tools, system administration
- scientific computing, text processing, image processing


## Text Editors/IDE

To edit Python code, you just need a handy text editor. There are many available, check out the following pages 

- [Python Wiki](https://wiki.python.org/moin/PythonEditors)
- [Comparison_of_text_editors in Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_text_editors)
