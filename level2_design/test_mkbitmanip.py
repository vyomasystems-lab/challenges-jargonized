# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test_Rtype(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    func7_1 = [0x40000000, 0x00000000, 0x60000000, 0x20000000]
    func7_2 = [0x01000000, 0x09000000]
    func3 = [0x0000F000, 0x0000E000, 0x0000C000, 0x00009000, 0x0000D000]
    opcode = 0x000000B3

    for i in func7_1:
        for j in func7_2:
            for k in func3:
                
                ######### CTB : Modify the test to expose the bug #############
                # input transaction

                mav_putvalue_src1 = 0x5
                mav_putvalue_src2 = 0x0
                mav_putvalue_src3 = 0x0
                mav_putvalue_instr = i+j+k+opcode

                if (mav_putvalue_instr == 0x4100f0b3):
                    continue

                # expected output from the model
                expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

                # driving the input transaction
                dut.mav_putvalue_src1.value = mav_putvalue_src1
                dut.mav_putvalue_src2.value = mav_putvalue_src2
                dut.mav_putvalue_src3.value = mav_putvalue_src3
                dut.EN_mav_putvalue.value = 1
                dut.mav_putvalue_instr.value = mav_putvalue_instr
            
                yield Timer(1) 

                # obtaining the output
                dut_output = dut.mav_putvalue.value

                cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
                cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
                
                # comparison
                error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} for inst = {hex(i+j+k+opcode)}'
                
                assert dut_output == expected_mav_putvalue, error_message


