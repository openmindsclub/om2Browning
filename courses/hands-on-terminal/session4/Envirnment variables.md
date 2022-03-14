# what are they?
- variables than can be acessed by all the system:
- needed by the SHELL
- Variable Types

When a shell is running, three main types of variables are present 

-    Local Variables −
    	 A local variable is a variable that is present within the current instance of the shell. It is not available to programs that are started by the shell. They are set at the command prompt.

-    Environment Variables 
	 An environment variable is available to any child process of the shell. Some programs need environment variables in order to function correctly. Usually, a shell script defines only those environment variables that are needed by the programs that it runs.

- Shell Variables 
	 A shell variable is a special variable that is set by the shell and is required by the shell in order to function correctly. Some of these variables are environment variables whereas others are local variables.
[source](https://www.tutorialspoint.com/unix/unix-using-variables.htm)

- (bourne )Shell  (zikenni) `sh`
- bourne again shell `bash`

----
----
 
- Many environment variables are set and then exported from the `/etc/profile` file and the `/etc/bashrc` file. There is a line in /etc/profile that reads:
- `$SHLVL` : how many subshell deep you are 
	- `echo $SHLVL`
	- `bash `
	- `echo $SHLVL`
- `PATH` variable: the one you'll be manipulating "the most":
	- it holds all the paths to your executables files!
	-  `echo $PATH`
	- how to add something to the path?
		- `PATH=$PATH:/opt/flutter` (do another example)
			- the change is only availible for the current session
			- To make it permanent, go into your `.bashrc` file and write the same thing as above (`PATH=$PATH:/opt/flutter`)
			- : separates path entities
			- [ ] show example using my /opt/idea (intellij idea install)
-  WE CAN ALSO CHECK
	-  $USER
	-  $PWD
	-  $LOGNAME
	-  makes you wonder how whoami and pwd , works huh
	
- playing the SHELL game
	- [ ] wait what' is a shell anyway?
	-  `echo $SHELL`
	- `usermod --shell <shell> <user>`
	- `usermod --shell <shell> goku` 
	- `sudo usermod -s /bin/bash $USERNAME`
	- OR `sudo lchsh $USER` (not sure if it works)
	-[source](https://www.tutorialspoint.com/unix/unix-what-is-shell.htm)
- `$?`:
	-  0 : réussi
	-  something else : erreur 

- [ ] i don't think it's important !
- `etc/profile`  contains shell commands that are for all users and .profile found at $HOME is per user.
- What is the difference between Bash_profile and profile?

	- bash_profile is only used upon login. … profile is for things that are not specifically related to Bash, like environment variables $PATH it should also be available anytime. . bash_profile is specifically for login shells or shells executed at login.

Source: https://frameboxxindore.com/linux/what-is-profile-file-in-linux.html

# [ ] use vim /bin/ls

 - [ ] to show them beggining of binary file (EFL)