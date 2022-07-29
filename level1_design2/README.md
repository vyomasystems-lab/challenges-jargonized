# Sequence Detector

## Gitpod Environment

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![Gitpod Environment](/images/scr_111.png)

## Verification Enivronment

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test which takes in clock, reset, and 1-bit signal as inputs and the seq_seen signal acts as the output which is asserted when the sequence 1011 is seen on the 1-bit input line.

Assert statement is used to raise a message when the actual and the expected output don't match.

## Verification Strategy

Firstly, the clock signal is set up and fed to the DUT. Secondly, the DUT is reset.
For debugging the code, a random input vector was hand-coded by me such that the sequence 1011 corrected independently and as part of other 1011 sequences.  

Observation: seq_seen(output) was asserted for independent sequences but not for dependent sequences.

## Test Scenario
```
Input: Hand-coded random vector consisting of the sequence 1011
input = [1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1]
expected out = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
```
![Bugs](/images/scr_121.png)

``` 
 20000.00ns INFO     Input : 1 model= 0 DUT=0
 30000.00ns INFO     Input : 0 model= 0 DUT=0
 40000.00ns INFO     Input : 1 model= 0 DUT=0
 50000.00ns INFO     Input : 1 model= 0 DUT=0
 60000.00ns INFO     Input : 0 model= 1 DUT=1
 70000.00ns INFO     Input : 0 model= 0 DUT=0
 80000.00ns INFO     Input : 1 model= 0 DUT=0
 90000.00ns INFO     Input : 0 model= 0 DUT=0
100000.00ns INFO     Input : 1 model= 0 DUT=0
110000.00ns INFO     Input : 1 model= 0 DUT=0
120000.00ns INFO     Input : 0 model= 1 DUT=1
130000.00ns INFO     Input : 1 model= 0 DUT=0
140000.00ns INFO     Input : 1 model= 0 DUT=0
150000.00ns INFO     Input : 0 model= 1 DUT=0
160000.00ns INFO     Input : 1 model= 0 DUT=0
170000.00ns INFO     Input : 1 model= 0 DUT=0
180000.00ns INFO     Input : 1 model= 1 DUT=0
190000.00ns INFO     Input : 1 model= 0 DUT=0
200000.00ns INFO     Input : 0 model= 0 DUT=0
210000.00ns INFO     Input : 1 model= 0 DUT=0
220000.00ns INFO     Input : 0 model= 0 DUT=0
230000.00ns INFO     Input : 1 model= 0 DUT=0
240000.00ns INFO     Input : 1 model= 0 DUT=0
250000.00ns INFO     Input : 1 model= 1 DUT=1
```

## Design Bug

Observation: When two sequences occured consecutively or occured partially and then completely, output was not asserted. On analysing, the below two bugs were found:

```
// Bug 1: When seq 1011 is seen, no matter the next input, the state machine was reset, ignoring the last seen '1' as the potential start of another valid sequence.
// Lines 67 - 70
SEQ_1011:
   begin
    next_state = IDLE;
   end
```

```
//Bug 2: When seq 101 was seen but the following input was zero, the state machine was reset, ignoring the last seen '10' as the potential start of another valid sequence.
// Lines 60 - 66
SEQ_101:
  begin
    if(inp_bit == 1)
      next_state = SEQ_1011;
    else
      next_state = IDLE;
  end
```

## Design Fix

After fixing the bugs, both tests successfully passed.

![Verified](/images/scr_122.png)

The modified file is available here ![Modified Sequence Detector Module](correct_design/seq_detect_1011.v)






