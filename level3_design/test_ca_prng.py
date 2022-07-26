# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from ca_prng import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 



@cocotb.test()
def run_test_random(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    # reset
    dut.reset_n.value <= 0
    yield Timer(10) 
    dut.reset_n.value <= 1

    print(dut.ca_state_reg.value)

    count = 0
    err = []

    ######### CTB : Modify the test to expose the bug #############
    # input transaction

    for i in range(5):

       
        init_pattern_data = random.randint(0,4294967295)
        load_init_pattern = random.randint(0,1)
        update_rule = 0b01011010 #rule 90
        load_update_rule = random.randint(0,1)
        next_pattern = random.randint(0,1)
        
        # expected output from the model
        expected_prng_data = ca_prng(init_pattern_data,load_init_pattern,update_rule,load_update_rule,next_pattern)

        # driving the input transaction
        dut.init_pattern_data.value = init_pattern_data
        dut.load_init_pattern.value = load_init_pattern
        dut.update_rule.value = update_rule
        dut.load_update_rule.value = load_update_rule
        dut.next_pattern.value = next_pattern

        

        yield Timer(1) 

        # obtaining the output
        dut_prng_data = dut.prng_data.value

        print(dut_prng_data, expected_prng_data)

        cocotb.log.info(f'DUT OUTPUT={hex(dut_prng_data)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_prng_data)}')
        
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} for inst = {hex(inst)}'
        
        if (dut_prng_data != expected_prng_data):
            count+=1
            err.append(error_message)
        
        assert count == 0 , f"Bugs Found \n {err}"
            
