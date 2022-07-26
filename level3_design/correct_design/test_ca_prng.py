# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import os
import random


import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

from prng_compute import *

@cocotb.test()
async def run_test_random(dut):

    # clock
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())    

    # reset
    await FallingEdge(dut.clk)
    dut.reset_n.value = 0
    await FallingEdge(dut.clk)  
    dut.reset_n.value = 1
    
    count = 0
    err = []
    

    #input values
    
    initial = random.randint(0,4294967295)
    load_initial = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    updaterule = 90
    defaultupdaterule = 30
    load_update = [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
    nextpattern = [0,0,0,0,0,1,1,1,1,1,1,0,1,1,1]
    expected = [0,0,0,0,initial]
    my_update_rule = defaultupdaterule

    #modelling the ca_prng module

    for i in range(4,15):
        if (load_initial[i]):
            expected.append(initial)
        elif (nextpattern[i]):
            if load_update[i]:
                my_update_rule = updaterule
            expected.append(prng_compute(expected[i],updaterule))
        else:
            expected.append(expected[i])


    for i in range(15):

        print(i)
        init_pattern_data = initial
        load_init_pattern = load_initial[i]
        update_rule = updaterule
        load_update_rule = load_update[i]
        next_pattern = nextpattern[i]

        # driving the input transaction
        
        
        dut.init_pattern_data.value = init_pattern_data
        dut.load_init_pattern.value = load_init_pattern
        dut.update_rule.value = update_rule
        dut.load_update_rule.value = load_update_rule
        dut.next_pattern.value = next_pattern

        
        expected_prng_data = expected[i]
            
              
        # obtaining the output
        await RisingEdge(dut.clk)
        dut_prng_data = dut.prng_data.value
        
        
        cocotb.log.info(f'DUT OUTPUT={hex(dut_prng_data)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_prng_data)}')
        cocotb.log.info(f'DIFFERENCE = {bin(dut_prng_data ^ expected_prng_data)}') #for finding the error
        
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_prng_data)} does not match MODEL = {hex(expected_prng_data)}'

        if (dut_prng_data != expected_prng_data):
            count+=1
            err.append(error_message)
        
    assert count == 0 , f"Bugs Found \n {err}"
            
