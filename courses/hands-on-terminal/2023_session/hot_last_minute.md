Hello as you can see i didn't have a proper presentation, so i'll just use markdown because i like it... and it's easier to write things and yk... I'm free!

1. What is an Operating System
	- An operating system is the software layer that sits between the programs you run and the hardware to help them communicate in an efficient way that is both fast and reliable , some operating systems that you may have encountered are { android , Linux , mac OS , IOS , windows , orbis OS , BSD , symbian , wear os }
---

2. WHAT is linux
	1. Linux is an open-source free “as in freedom” computer operating system , 

	2. Linux  a UNIX like operating system which makes it very flexible, modular and developer friendly 

	3. Linux “the kernel” is initially made by the Swedish programmer Linus Torvalds “just for fun” but after releasing it under the GPL license in 1993 it started being taken seriously and became the biggest collaborative work in the human history(i guess?)

	 4. Linux is now the most popular operating system ever() , running on 100% of world’s super computers ,  97% of the servers , 75% of the phones and tablets , and it powers all the chrome-books and most of if not all embedded devices of the world 
		 - Source : trust me bro
			 - https://www.enterpriseappstoday.com/stats/linux-statistics.html
			 - https://www.fortunebusinessinsights.com/linux-operating-system-market-103037

---

3. Who is it for
	- People who value privacy  “Edward Snowden recommends it ;)”

	- Programmers , Linux supports all IDEs and programming languages

	- Enterprises , Linux is more secure and reliable than it’s competitors making it the best for mission critical applications

	- Computer enthusiasts who like to customize and have full control over their systems

	- Hackers and tinkerers , retro gamers (even just normal gamers with the stream deck now!), governments , minimalists , crypto miners , space helicopters , people with old/low-end hardware , printer fanboys, the nasa..
 
	==> Linux is for everyone ;-) 
 
---

4. Why is this useful for me?/you anyway?
	1. You will you it at UNI
	2. you will use it in the Pro world
	3. You'll use it if you deploy any application 
	4. anyway ,you will just use it you know!! trust me bro

--- 

5. WHY TO use it? Whats the point?
	1. All the previous reasons i mentionned!!
	2. https://www.linode.com/docs/guides/benefits-of-linux/
	3. Security
	4. Tesahqou f les tps!

---

6. What r we gonna learn today?
	1. Basic commands (around 10)
	2. How to connect multiple commands together (the "|" )
	3. how to check for documentation (and yes you can ask the ai but it's always good to know there is another way yk, just in case it's the end of the world and you need to do something i DONT KNOW)

-  Any questions???
	-  [What is a CLI (or terminal)](https://www.redhat.com/en/topics/linux/what-is-linux)
		-  The command line is your direct access to a computer. It's where you ask software to perform hardware actions that point-and-click graphical user interfaces (GUIs) simply can't ask.
		- Command lines are available on many operating systems—proprietary or open source. But it’s usually associated with Linux, because both command lines and open source software, together, give users unrestricted access to their computer.


---

1. The setup on your machines 
	1. You have linux
		1. Great
		2. You don't ....
			1. You can try this website(that was just for the presentation THIS IS NOT A SOLUTION):
				1. https://linuxsurvival.com/
				2. https://www.terminaltemple.com/
			2. Install it (i talk about it at the end of this document)

--- 
2. Lets get practical, exercices and tests on
	1. Your first command!

---
1. ls
Lists the folders and files that are present in the current working directory

```bash
ls 
```

2. pwd
- prints the current working directory (pwd= print working directory)
- Usage!
```bash
pwd
```

3. cd 
	-  allows you to move between directories (cd = change directories)

```bash
cd .. 
cd Directory1
```

4. mkdir
	- Allows you to create one or more directories

```bash
# when it starts with # its a comment
mkdir directory1
# we can create multiple directories
mkdir zrodiya felfel batata tomatich
```


5. touch 
	- Allows you to create one or more files 

```bash
# crate only 1 file
touch file1
# Yes we can specify the extension
touch script.py
# we can create multiple files as with mkdir with direcotories
touch file1 file2 file3 file4.cpp file5.txt
```

6. rm
- Allows you to remove files or direcotories
```bash
rm file
# the -d tells rm that this is a directory if we don't do that rm will complain!
rm -d directory
```

==> You should know that each command has argument/can receive arguments for example in the rm the `-d` is an argument.
==> You can also see read and learn more about that by using the `man` command (which stands for manual)
```bash
# this will display a documentation in which it explains how rm works and also the arguments it can receive and what they mean ect...
man rm
```


7. cp
-  copy files or directories!
```bash
# copy file1 into folder
cp file1 folder/ 
# create a copy of file1 in the same direcotry with another name
cp file1 copy_of_file1
# copy a file into a folder and rename it
cp file1 folder/file1_renamed
# You can do OTHER THINGS if you're stuck you can either look at the manual `man cp`
# Or you can ask some ai 
```

8. mv
- Move files or directories and change names
```bash
# moves file1 into directory
mv file1 directory/
# change the name of a file
mv file1 new_name
# there are other usage i encourage you to look try and just... tinker and try to learn
```


9. echo 
- It's a PRINT
```bash
# will output hello world !
echo hello world
echo I use arch BTW
echo hey hey hey you're learning! it's nice
```


==> Let's introduce you to the redirect symbole
- `>` and `>>`
	- `>` : redirects and overrides the file (means it deletes everything then writes again)
	- `>>` : redirects and appends! ()

```bash
# we have a file named zrodiya
echo hello world > zrodiya
# check the content of the file
echo another hello world > zrodiya
# check the content of the file again,you see that it deleted the first hello world!
# Now if you want to add upon it you use the >>
echo hello world >> zrodiya
echo hello world 2 >> zrodiya
echo this is another line >> zrodiya
# check the content of the file!
```

10. cat
- It does a lot of things but i usually use it to only  to display the content of a file
```bash
cat zrodiya
```


11. grep
- This command is useful if you wanna search for something inside a text (at least that's HOW i use it)
**BUT before the usage**
		--> we need to understand the Pipe `|`
==> The pipe `|` is commonly used in the terminal to perform complex operations that evolve multiple commands, what i use it is just to check if something is inside a working directory 

```bash
# the pipe will take the output of the ls command and 
# give it as an input to the grep command
ls | grep file_name
# there are obviously other more complex and useful usage but, ...
# that's just how i use it myself
```



## Ressources

- Some Basic ressources: i'll only put 3 because otherwise it's overwelming and you do nothing (and yes it happens to ALL of us)
	- https://www.learnlinux.tv/tag/linux-crash-course/ (REALLY GOOD explanations , you can directly check his youtube channels)
	- https://linuxhandbook.com/ 
	- https://www.youtube.com/watch?v=vX92aS1xsaE&list=PLjAHiXDnp3Jkr1wNEcG3Y66kH2tLYIuY- (Français! )
 
- How to install linux:
	-  Yes , You can install it alongside windows (it's called dual boot)
	- You can completely remove windows (like i did)
	- You can use wsl , but it means that you are still a microsoft ``*****`` you give up on your freedom, your data, and all the fun stuff that linux does offer! 
	==> you can check one of the youtube channels i put above (adrien D or learn linux tv), and maybe you can also check https://www.youtube.com/watch?v=10f4899srvc this , and as usual just ... try to understand and experiment,
