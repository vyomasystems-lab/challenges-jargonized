# Sequence Detector

## Gitpod Environment

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![Gitpod Environment](/images/scr_111.png)

## Verification Enivronment

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test which takes in clock, reset, and 1-bit signal as inputs and the seq_seen signal acts as the output which is asserted when the sequence 1011 is seen on the 1-bit input line.

Assert statement is used to raise a message when the actual and the expected output don't match.

## Verification Strategy

Firstly, the clock signal is set up and fed to the DUT. Secondly, the DUT is reset.
For debugging the code, 
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

![Bugs](/images/scr_121.png)

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

After fixing the bugs, both tests successfully passed.

![Verified](/images/scr_122.png)

The modified file is available here ![Modified Mux Module](correct_design/seq_detect_1011.v)






