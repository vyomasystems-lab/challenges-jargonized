# 31 x 1 Multiplexer

## Gitpod Environment

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![Gitpod Environment](/images/scr_111.png)

## Verification Enivronment

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test which takes in 31 1-bit and a 5-bit select signal as inputs and routes one of the 31 signals to output based on the select signal value.

Assert statement is used to raise a message when the actual and the expected output don't match.

## Verification Strategy

Firstly, the input singals and select signals where given random values. Many of the times, the test ran successfully but failed when one of the two conditions occured.

```
//Case 1:
Assertion Error: Mux result is incorrect: 00 != 1, sel = 30

//Case2:
Assertion Error: Mux result is incorrect: 01 != 0 , sel = 13
```

Observation: 1. Some issue with select line 13 and 30. 
Inference: Default line must be zero.

## Test Scenario
```
Inputs 0 to 30 : All 1's
Select values : All values ranging from 0 to 30, limits inclusive.
```

Outputs mismatched for the above mentioned bugs. 
![Bugs](/images/scr_112.png)

## Design Bug
```
// Bug 1: both inp12 and inp13 uses 13 as select signal
line 40: 5'b01101: out = inp12;
line 41: 5'b01101: out = inp13; 
```

```
//Bug 2: case for selecting inp30 missing
line 56:   5'b11100: out = inp28;
line 57:   5'b11101: out = inp29;
line 58:   default: out = 0;
line 59: endcase
```

## Design Fix

The modified file is available here ![Modified Mux Module](correct_design/mux.v)





