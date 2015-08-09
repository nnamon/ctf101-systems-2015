Overview of the Systems Security Lesson at CTF101
=================================================

Assumptions
-----------
* Knowledge of C/C++
* Knowledge of Linux/Unix Systems

Topics to Cover
---------------
* Introduction to Software Exploitation
    * Scripting Languages
        * Source code auditing
        * Exploitation of scripts
    * Contrast with ELF and EXEs

* Representation of Code as Data


Introduction to Software Exploitation
=====================================

Types of Software
-----------------

We will cover two types of applications in this workshop:
1. Scripts
2. Compiled Binary

While the majority of the workshop will cover Compiled Binary exploitation, we
will briefly introduce what scripting languages are, their use in modern
systems, and the common insecure coding problems introduced by programmers.

Scripting Languages
-------------------

Scripting languages like Python, Ruby, Perl, or Bash are used to write
memory-safe and quickly developed programs that run on top of an interpreter
which are often written in a systems language like C. While vulnerabilities do
exist within the interpreter, exploitation of the program logic at the higher
level is more feasible with the exposed attack surface.

### Source Code Auditing



### Exploitation of Scripts

Representation of Programs as Data
==================================
