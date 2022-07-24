# challenges-jargonized
challenges-jargonized created by GitHub Classroom

Notes:

Level1_Design1 Bugs identified
1. Missing case statement for selecting inp30
2. inp12 and inp13 uses sel = 12

Level1_Design2 Bugs identified
1. SEQ_1011 goes to IDLE without validating input, sequence detection problem in the case of "1011011"

Level2_Design Bugs identified
1. ANDN results mismatch
2. Immediate type instructions, for instructions not present, DUT output is 0xa, which should be 0x0.
3. FSRI instruction confused with Immediate type instruction - rs3 part is mistaken
