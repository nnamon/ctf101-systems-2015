Overview of the Systems Security Lesson at CTF101
=================================================

Assumptions
-----------

* Knowledge of C/C++
* Knowledge of Linux/Unix Systems

Topics to Cover
---------------

* Introduction to the Pico Platform
* Introduction to Software Exploitation
    * Scripting Languages
        * Source code auditing
        * Exploitation of scripts
    * Contrast with ELF and EXEs

* Representation of Code as Data

Introduction to the Pico Platform
=================================


Introduction to Software Exploitation
=====================================

Categories of Software
----------------------

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

The source code for scripts are usually readily available and can be used to
discover vulnerabilities. For example, let's take a look at this simple Python
script that allows a user to ping an arbitrary ip address.

#### Practical 1: Ping

The details for the practical in this example may be found on the Pico CTF
scoreboard.

```python
import sys
import subprocess


def main():
    sys.stdout.write("Enter the IP address or domain of the website you wish"
                     " to ping: ")
    sys.stdout.flush()
    ip = sys.stdin.readline()
    print(subprocess.getoutput("ping -c 1 " + ip))

if __name__ == "__main__":
    main()
```

Exploitation of a program usually begins with processing untrusted user input
without the proper handling. In this example, the user is prompted to supply an
IP address or a domain name to send a single ICMP ping packet. The output of the
ping command is printed to the user.

Now, this looks like a very simple script, but it is vulnerable to arbitrary
shell command injection. This occurs because the user input is directly
concatenated to the subprocess.getoutput call resulting in a malicious actor
being able to supply the following:

```
google.com; ls
```

which results in this full command being executed:

```
ping -c 1 google.com; ls
```


### Exploitation of Scripts

Representation of Programs as Data
==================================
