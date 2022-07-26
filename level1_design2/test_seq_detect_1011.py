# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    count = 0

    cocotb.log.info('#### CTB: Develop your test here! ######')

    a = [1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1]
    out = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
    
    for i in range(24):

        dut.inp_bit.value = a[i]

        await RisingEdge(dut.clk)
        
        dut._log.info(f'Input : {a[i]} model= {out[i]} DUT={dut.seq_seen.value}')

        if dut.seq_seen.value != out[i]:
            count+=1

    assert count == 0,"Sequence seen is incorrect"