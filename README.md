# Rhs-Lang
Repository of Compilation Techniques (Learning) with [Library SLY](https://sly.readthedocs.io/en/latest/sly.html).

## Our Grup:
- Ahmad Fauza Aulia
- Fitri Amalia Langgundi
- Nia Zulia Saputri

---

# Documentation

## You Must Know

- [x] this language is created using the SLY library which is supported with PYTHON version 3.*
- [x] this language has the extension .rhs

## Command in Rhs-Lang

| RHS-LANG |  MEAN  |
| -------- |  ----  |
| FI       |  IF    |
| TNIRP    |  PRINT |
| NEHT     |  THEN  |
| ESLE     |  ELSE  |
| ROF      |  FOR   |
| NUF      |  FUN   |
| OT       |  TO    |
| ->       |  ARROW |


## How To Use 

**Follow this steps**
1. Open powershell or bash with the directory this folder `cd ../Rhs-Lang/`
2. And then run file main.py in the Rhs-Lang folder with command:`python .main.py .bahasaku.rhs`

**_NOW, YOU CAN DO IT_**

> You can edit file code in the `Bahasaku.rhs`

## Examples Rhs Lang

### PRINT Hello World!!

**example:**
```
TNIRP "Hello World" 
```

**result**
```
Hello World
```

**or:**
```
a= "Hello World"
TNIRP a 
```

**result**
```
"Hello World"
```

### Addition, Subtraction, Multiplication, Division


**example:**
```
3+2
4-1
3*3
4/2
```

**result**
```
5
3
6
2
```

**or**
```
a=6
b=2
TNIRP a+b
TNIRP a-b
TNIRP a*b
TNIRP a/b
```

**result**
```
8
4
12
3
```

### IF ELSE 

> IF _expr_ THEN _stmt1_ ELSE _stmt2_

**example:**
```
a=6
y="true"
n="false"
FI a==6 NEHT TNIRP y ESLE TNIRP n
```

**result**
```
"true"
```

### FOR

> FOR _expr_ TO _stmt1_ THEN _stmt2_

**example:**
```
ROF i=0 OT 5 NEHT TNIPR i
```

**result**
```
0
1
2
3
4
```

### Function

> NUF functionName() -> Your Code Here...

**example:**
```
NUF ahsheup() -> TNIRP "Mantap Gan!!"

ahsheup()
```

**result**
```
Mantap Gan!!
```

**or:**
```
NUF loop() -> ROF i=0 OT 5 NEHT TNIPR i

loop()
```

**result**
```
Mantap Gan!!
```

### Use Comment

> You can use `'#'` symbol to make comment in your source code.

**example:**
```
I = "U" #but U not I
FI I == "U" NEHT TNIRP "PERFECT" ESLE TNIRP "I'm So Sorry"
#now you know how this works
```

**result**
```
"PERFECT"
```

Good luck, Thanks :)

# NOTE
This is a modified source code for the howCode programming language series.

You can watch the video accompanying this series here: [https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk](https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk)