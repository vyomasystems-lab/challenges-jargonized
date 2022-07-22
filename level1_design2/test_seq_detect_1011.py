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
    print(f"current_state_value: {dut.current_state.value}")
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    a = [1,0,1,1,0,1,1,0]
    out = [0, 0, 0, 0, 1, 0, 0, 1]
    
    for i in range(8):

        dut.inp_bit.value = a[i]

        await RisingEdge(dut.clk)
        
        print(f"current_state_value: {dut.current_state.value}")
        print(f"next_state_value: {dut.next_state.value}")

        dut._log.info(f'Input : {a[i]} model= {out[i]} DUT={dut.seq_seen.value}')

        assert dut.seq_seen.value == out[i], f"Mux result is incorrect: {dut.seq_seen.value} != {out[i]}, iter = {i}"