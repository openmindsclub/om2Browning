# BOURNE SHELL

![960ef417382095e75ccddd9e4362f5e4.png](_resources/960ef417382095e75ccddd9e4362f5e4.png)

- Steve Bourne created the Bourne shell (sh) and other Unix tools as a researcher at Bell Labs. The Bourne shell became Unix’s default shell in Version 7 Unix (replacing the original shell written by Ken Thompson) and introduced the concept of “shell scripting” by adding programming capabilities to the command-line interpreter.

# BOURNE-AGAIN SHELL (BASH)

- all the commands you run in the command line, can be used in scripts to automate tasks or something

# 1\. let's get started

`**MOST IF NOT ALL OF THIS IS DIREclTly copy-paested/inspired by [this tutorial](https://gist.github.com/bradtraversy/ac3b1136fc7d739a788ad1e42a78b610) **`
[and this](https://www.youtube.com/watch?v=v-F3YLd6oMw)

1.  create a .sh file
2.  in the beggining write the path to the bash
    
    - [ ] i don't know if it's necessary though
    
    ```bash
    #!/usr/bin/bash
    ```
    

# priting things

use `echo`

- print content of a variable
    use `$` sign before variable name

# 2\. Variables

- always upper case by convention

```bash
echo "welcome into hot4!"
YOU="are the best"
echo "you $YOU"
```

# run script

`./script.sh`

# passing arguments

- every variable is referenced by it's order

```bash
echo "variable 1: $1" 
echo "variable 2: $2" 
```

if we run `./test.sh var1 var2`

# if conditions

```bash
BEST_LICENCE  = "GPL"
CURRENT_LICENCE = "MIT"
if [$CURRENT_LICENCE == $BEST_LICENCE] 
    then
        echo "You're the best sahbi"
    else 
        echo "rigel rouhek sahbi"
fi
```

```bash
BEST_LICENCE="GPL"
CURRENT_LICENCE="MIT"

if [ "$CURRENT_LICENCE" == "$BEST_LICENCE" ]
        then
                echo "You're the best sahbi"
        elif [ $CURRENT_LICENCE == "MIT" ]
                then
                        echo "rigel rouhek sahbi"
        else
                echo "lazem nahedrou..."
fi
```

# getting input

```bash
read -p "are you okay? Y/N " ANSWER
echo "$ANSWER"
```

# case

```bash
read -p "Are you 21 or over? Y/N " ANSWER
case "$ANSWER" in
  [yY] | [yY][eE][sS])
    echo "You can have a beer :)"
    ;;
  [nN] | [nN][oO])
    echo "Sorry, no drinking"
    ;;
  *)
    echo "Please enter y/yes or n/no"
    ;;
esac
```

# LOOPS

## While

```bash
while (condition); do 

done
```

```bash
while true; do
        read -p "did you enjoy the hot sessions? Y/N   " yn

        case $yn in
                [Yy]* )
                        echo "NOICE!!";
                        break;;
                [Nn]* )
                        echo "c'est triste";
                         exit;;
                * ) echo "please answer :("
        esac
done
```

## for

```bash
NAMES="Brad Kevin Alice Mark"
for NAME in $NAMES
  do
    echo "Hello $NAME"
done
```

# function

```bash
function myfunction(){
    echo "this is just another function a jma3a"
}
myfunction
```

# run mulitple processes in the background

- use `&` to separate every process

```bash
process_1 &
process_2_niceone &
hot_3_process &
another_processwhatt &
```
