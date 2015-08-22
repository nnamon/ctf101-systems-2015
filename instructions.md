Instructions on Self-Hosting the Challenges
===========================================

This article will describe how to host the challenges on your own virtual
machines.

Requirements:

1. 64-bit Linux (I recommend Ubuntu 14.04 64 bits)
2. socat
3. python
4. gcc
5. git

Please make sure you have the above installed

Workshop Source Files
---------------------

Before we begin, please clone the repository found at
https://github.com/nnamon/ctf101-systems

```
$ git clone https://github.com/nnamon/ctf101-systems
Cloning into 'ctf101-systems'...
remote: Counting objects: 159, done.
remote: Total 159 (delta 0), reused 0 (delta 0), pack-reused 159
Receiving objects: 100% (159/159), 30.53 KiB | 0 bytes/s, done.
Resolving deltas: 100% (50/50), done.
Checking connectivity... done.
```

Now we'l only be interested in the challenges so let's change our directory.

```
$ cd ctf101-systems/challenges/vulnclasses
```

You should find the challenges here.

Console-Based to Networked
--------------------------

Notice that during the workshop, most of the challenges required some form of
network interaction but the source files suggested nothing related to the
handling of these networked connections.

We achieved this using xinetd during the workshop but it's impractical to get
everyone to set up the entire environment so we'll be using socat in this
article.

Let's take the Ping practical as an example:

```
$ cd ping/grader/
$ ls -la
total 12
drwxr-xr-x 2 amon users 100 Aug 22 16:40 .
drwxr-xr-x 4 amon users 100 Aug 22 16:40 ..
-rw-r--r-- 1 amon users  27 Aug 22 16:40 flag
-rw-r--r-- 1 amon users 224 Aug 22 16:40 grader.py
-rw-r--r-- 1 amon users 318 Aug 22 16:40 ping.py
```

Now the ping.py file is a python script and does not have any networking
included. To fix this we make the file executable and then use socat to create a
network wrapper around our script.

```
$ chmod +x ping.py
$ socat TCP4-listen:1337,reuseaddr,fork EXEC:./ping.py

```

You should have socat listening on port 1337 now and will execute the python
script every time someone connects to it on localhost.

```
$ nc localhost 1337
Enter the IP address or domain of the website you wish to ping: google.com;ls
PING google.com (74.125.130.138) 56(84) bytes of data.
64 bytes from sb-in-f138.1e100.net (74.125.130.138): icmp_seq=1 ttl=43
time=4.24 ms

--- google.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 4.246/4.246/4.246/0.000 ms
flag
grader.py
ping.py
```

 You may continue with the rest of the lesson plan from here.


Compiling for your Architecture
-------------------------------

The binary provided in the privilege escalation challenge may not be suitable
for your machine and you may require recompilation. To do this navigate into the
directory and compile it like so:

```
$ cd privesca/graders
$ gcc -o escalate escalate.c
```

Now you have an executable binary file that works on you system.


