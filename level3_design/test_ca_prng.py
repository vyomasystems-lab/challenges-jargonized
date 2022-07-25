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

          
    ######### CTB : Modify the test to expose the bug #############
    # input transaction

    """ clk,
               input wire           reset_n,

               input wire [31 : 0]  init_pattern_data,
               input wire           load_init_pattern,
               input wire           next_pattern,

               input wire [7 : 0]   update_rule,
               input wire           load_update_rule, """

    for i in range(5):

       
        init_pattern_data = random.randint(0,4294967295)
        load_init_pattern = random.randint(0,1)
        update_rule = 0b01011010 #rule 90
        load_init_pattern = random.randint(0,1)
        next_pattern = random.randint(0,1)
        
        # expected output from the model
        #expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.init_pattern_data.value = init_pattern_data
        dut.load_init_pattern.value = load_init_pattern
        dut.update_rule.value = update_rule
        dut.load_init_pattern.value = load_init_pattern
        dut.next_pattern.value = next_pattern

        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} for inst = {hex(inst)}'
        
        assert dut_output == expected_mav_putvalue, error_message
