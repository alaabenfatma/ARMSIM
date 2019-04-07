# Welcome to ARMSIM!

**ARMSIM** is a basic **ARM** Assembly **SIM**ulator written completely in Python.
<p style="text-align: center;"> <img src="https://github.com/alaabenfatma/ARMSIM/blob/master/rscs/logo.png" alt="LOGO" ></p> 
<p style="text-align: center;"> 
  <img width=90px height=25px src="https://cdn-images-1.medium.com/max/800/1*Ih7G_D_hzoskYTHfa-zNmw.png" alt="build" >
 </p> 
 
ARM code:
```
main: cmp r0, #3
 	  beq fin
 	  add r0, r0, #1
 	  bal main
fin:
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
