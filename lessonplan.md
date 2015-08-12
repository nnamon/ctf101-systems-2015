CTF 101 Systems Security Lesson Plan
====================================

Assumptions
-----------

* Knowledge of C/C++
* Knowledge of Linux/Unix Systems

Topics to Cover
---------------

* Agenda
* Introduction to NUS Greyhats
* Introduction to CTFs
* Introduction to the Pico Platform
* Introduction to Software Exploitation
    * Scripting Languages
        * Source code auditing
        * Classes of Vulnerabilities
    * Contrast with ELF and EXEs
* Representation of Code as Data
* x86-64 Primer

Workshop Agenda
===============

CTF101 is an information security workshop organised by the NUS Greyhats in the
style of an information security CTF, a competition of hacking skill, to impart
the basics of offensive systems and web security.

This workshop does not follow any formal syllabus or framework published by any
academic or commercial entity and is aimed at the beginner level. It is aimed to
run for 10 hours over two days, with 5 hours given to Systems Security, and 5
hours given to Web Security.


Introduction to NUS Greyhats
============================

NUS Greyhats
------------

The NUS Greyhats is an information security special interest group in NUS. We
organise security sharing talks, workshops (like this one), and internal
discussions on novel security research and news. In addition, we also
participate in local and international information security CTF competitions.

/usr/bin/whoami
---------------

I am amon, an information security undergraduate at NUS. I am a member of the
NUS Greyhats core team and the designer of this lesson. I am the founder of the
Nandy Narwhals CTF team and co-founder of the Dystopian Narwhals CTF team. I
have been playing in CTF competitions for more than five years, both local and
international.

I am a Singapore Polytechnic Diploma in Information Security Management alumni
and have organised multiple CTFs, the latest being Dystopia CTF, an introductory
CTF, for the students at SP.

For more information about my CTF teams, some tutorials and for past CTF
writeups, please see the following links:

* [Nandy Narwhals and Dystopian Narwhals site](http://nandynarwhals.org)
* [CTFtime Profile](https://ctftime.org/team/10339)
* [My CTF Partner's Dystopian Narwhals site](http://iwanttoplayaga.me)


Introduction to CTFs
====================

What is a CTF?
--------------

CTF is short for 'Capture the Flag'. In our context, CTF competitions are
infomation security competitions in which participants compromise security to
bypass access control protections in order to obtain a piece of privileged
information called the 'flag'.

Styles of CTFs
--------------

There are two main styles of CTFs:

1. Jeopardy
2. Attack/Defence

### Jeopardy

Jeopardy style CTF competitions feature player vs organiser gameplay where
challenges are packaged in discrete units with a given description and
accompanying challenge material. The challenge material is often hosted on
organiser controlled systems. These challenges are assigned a set number of
points which are granted to the team on completion of the task by entering the
flag in the scoreboard. In some competitions, the challenges are released slowly
over the course of the competition.

Some examples of Jeopardy style CTFs are:

* Hack.lu
* DEFCON CTF Qualifiers
* PoliCTF

### Attack/Defence

Attack/Defence style CTF competitions feature player vs player gameplay where
teams have to simultaenously defend their systems while attacking the competing
team's systems. These systems play host to vulnerable binaries which have to be
kept running and accessible. Teams are penalised if their services are
non-responsive. The objective of attacking is to exploit these vulnerable
services, retrieve the flag, and submit it for points. Once arbitrary control is
achieved, there can be potential for post-exploitation such as denial-of-service
attacks on the service.

Some examples of Attack/Defence style CTFs are:

* Hack in the Box KUL
* DEFCON CTF Finals
* UCSB's iCTF

### Hybrid

Of course, CTFs can be a combination of the two styles. One such example would
be the Cyber Defenders Discovery Camp organised by DSTA.

CTF101
------

We will be employing the analogue of the Jeopardy style CTF for this workshop
to impart some basic security skills.


Introduction to the Pico Platform
=================================

We will be using the PicoCTF Platform 2 as our scoreboard to keep track of
everyone's progress in this workshop.

*Insert instructions on how to access and complete the first sanity check*

Example Challenge: Sanity Check
-------------------------------




Introduction to Software Exploitation
=====================================

Categories of Software
----------------------

We will cover two types of applications in this workshop:

1. Scripts
2. Compiled Binaries

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

Now, this may look like a very simple script, but it is vulnerable to arbitrary
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

Now, the flag file is usually in the current directory in a CTF. So assuming
that there is a file named 'flag' in the same directory, we may read it by
injecting the following:

```
google.com; cat flag
```

### Classes of Vulnerabilities

One method of classifying a vulnerability is the extent of control it grants the
attacker. We have five primary levels of control in increasing severity:

1. Information Leak
2. Denial of Service
3. Arbitrary File Write
4. Arbitrary Code Execution
5. Privilege Escalation

#### Information Leak

An information leak (infoleak for short), is a vulnerability that when
exploited, reveals privileged information about the system or application to the
attacker. The effects of this information being in the control of an attacker
can be varying. Information an attack might be interested in include:

* Password Hashes
* Source Codes
* Binaries
* Pointers and Addresses
* libc Version

While infoleaks are not dangerous by themselves, they are used in conjunction
with another vulnerability to obtain more control over a system.

#### Denial of Service

Denial of Service vulnerabilities are broad and can be destructive or
non-destructive. The common theme between them is that they obstruct and prevent
legitimate users from accessing the service. While Denial of Service attacks can
be caused by congestion of network resources, we focus more on the
vulnerabilties that exist inherently in the application logic.

#### Arbitrary File Write

Arbitrary file write vulnerabilties allow an attacker to create/overwrite files
on the file system with controlled content. Now, this is dangerous on multiple
levels. If the application is privileged and is capable of overwriting system
files such as /etc/shadow and /etc/passwd, an attacker may insert their own
users to log on to the system through SSH. If the application is not privileged,
but has write access to their own directories, an attacker may insert content
that grant access or even perform arbitrary code execution.

An example of arbitrary code execution often appears when exploiting PHP web
applications where arbitrary PHP code is written to the file system and
triggered by the attacker by manipulating the web server to process the file.

#### Arbitrary Code Execution

Certain vulnerabilities grant arbitrary code execution which allows an attacker
to coerce the system into performing any operation she wishes. This may manifest
as a result of injection of evaluated data such as shell commands or scripts, or
on a more fundamental level such as taking control of the instruction pointer to
execute your own machine code. Arbitrary code execution is very closely tied to
privilege escalation where hijacking the control flow of a binary with
privileged access results in granting these privileges to the attacker.

#### Privilege Escalation

Privilege escalation vulnerabilities can exist in multiple forms and are not
necessarily arbitrary code execution bugs.

Representation of Programs as Data
==================================
