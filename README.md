# Welcome to ARMSIM!


**ARMSIM** is a basic **ARM** Assembly **SIM**ulator written completely in Python.
<p style="text-align: center;"> <img src="https://github.com/alaabenfatma/ARMSIM/blob/master/rscs/logo.png" alt="LOGO" ></p> 
<p style="text-align: center;"> 
  <img width=90px height=25px src="https://cdn-images-1.medium.com/max/800/1*Ih7G_D_hzoskYTHfa-zNmw.png" alt="build" >
 </p> 
 
<hr/> 

## Usage

ARM code:
```
main: cmp r0, #3
 	  beq end
 	  add r0, r0, #1
 	  bal main
end:
```
Command line:

`python arm.py {yourfile}
`

Output:

```
Executing :  ['ETIQ', ['MAIN']]
Executing :  ['CMP', ['r0', '#3']]
Executing :  ['BEQ', ['fin']]
Executing :  ['ADD', ['r0', 'r0', '#1']]
Executing :  ['BAL', ['main']]
Executing :  ['ETIQ', ['MAIN']]
Executing :  ['CMP', ['r0', '#3']]
Executing :  ['BEQ', ['fin']]
Executing :  ['ADD', ['r0', 'r0', '#1']]
Executing :  ['BAL', ['main']]
Executing :  ['ETIQ', ['MAIN']]
Executing :  ['CMP', ['r0', '#3']]
Executing :  ['BEQ', ['fin']]
Executing :  ['ADD', ['r0', 'r0', '#1']]
Executing :  ['BAL', ['main']]
Executing :  ['ETIQ', ['MAIN']]
Executing :  ['CMP', ['r0', '#3']]
Executing :  ['BEQ', ['fin']]
Executing :  ['ETIQ', ['FIN']]
Executing :  ['@', ['']]
r0 = 3
```
<hr/>

## Detecting Errors
The Lexer and the parser are both capable of tracing errors precisely.

### Example:

```diff
mov r0, #1
mov r1, #2
- mov r2, #
mov r3, #4
```
Command line:

`python arm.py {yourfile}
`

Output:

```
Could not execute the instruction at line: 3
Non-functional instruction: ' ['MOV', ['r2', '#']] '
```

| 🛑 WARNING 🛑|
| --- |
|Some pieces of this code are written in French and they will be eventually translated. Please feel free if you want to translate them yourself. |
