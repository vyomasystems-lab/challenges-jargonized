# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux_random(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    a = []
    for i in range(32):
        a.append(random.randint(0,1))
    
    # input driving
    for i in range(10):
        k = random.randint(0,31)
        dut.sel.value = k
        dut.inp0.value = a[0]
        dut.inp1.value = a[1]
        dut.inp2.value = a[2]
        dut.inp3.value = a[3]
        dut.inp4.value = a[4]
        dut.inp5.value = a[5]
        dut.inp6.value = a[6]
        dut.inp7.value = a[7]
        dut.inp8.value = a[8]
        dut.inp9.value = a[9]
        dut.inp10.value = a[10]
        dut.inp11.value = a[11]
        dut.inp12.value = a[12]
        dut.inp13.value = a[13]
        dut.inp14.value = a[14]
        dut.inp15.value = a[15]
        dut.inp16.value = a[16]
        dut.inp17.value = a[17]
        dut.inp18.value = a[18]
        dut.inp19.value = a[19]
        dut.inp20.value = a[20]
        dut.inp21.value = a[21]
        dut.inp22.value = a[22]
        dut.inp23.value = a[23]
        dut.inp24.value = a[24]
        dut.inp25.value = a[25]
        dut.inp26.value = a[26]
        dut.inp27.value = a[27]
        dut.inp28.value = a[28]
        dut.inp29.value = a[29]
        dut.inp30.value = a[30]

        await Timer(2, units='ns')

        dut._log.info(f'Inputs 0 to 30: {a} sel: {k} model={a[k]} DUT={dut.out.value}')

        assert dut.out.value == a[k], f"Mux result is incorrect: {dut.out.value} != {a[k]}, sel = {k}"

@cocotb.test()
async def test_mux_allone(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    a = [1 for i in range(32)]
    
    # input driving
    for i in range(10):
        k = random.randint(0,31)
        dut.sel.value = k
        dut.inp0.value = a[0]
        dut.inp1.value = a[1]
        dut.inp2.value = a[2]
        dut.inp3.value = a[3]
        dut.inp4.value = a[4]
        dut.inp5.value = a[5]
        dut.inp6.value = a[6]
        dut.inp7.value = a[7]
        dut.inp8.value = a[8]
        dut.inp9.value = a[9]
        dut.inp10.value = a[10]
        dut.inp11.value = a[11]
        dut.inp12.value = a[12]
        dut.inp13.value = a[13]
        dut.inp14.value = a[14]
        dut.inp15.value = a[15]
        dut.inp16.value = a[16]
        dut.inp17.value = a[17]
        dut.inp18.value = a[18]
        dut.inp19.value = a[19]
        dut.inp20.value = a[20]
        dut.inp21.value = a[21]
        dut.inp22.value = a[22]
        dut.inp23.value = a[23]
        dut.inp24.value = a[24]
        dut.inp25.value = a[25]
        dut.inp26.value = a[26]
        dut.inp27.value = a[27]
        dut.inp28.value = a[28]
        dut.inp29.value = a[29]
        dut.inp30.value = a[30]

        await Timer(2, units='ns')

        dut._log.info(f'Inputs 0 to 30: {a} sel: {k} model={a[k]} DUT={dut.out.value}')

        assert dut.out.value == a[k], f"Mux result is incorrect: {dut.out.value} != {a[k]}, sel = {k}"

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    a = [1 for i in range(32)]
    

    dut.inp0.value = a[0]
    dut.inp1.value = a[1]
    dut.inp2.value = a[2]
    dut.inp3.value = a[3]
    dut.inp4.value = a[4]
    dut.inp5.value = a[5]
    dut.inp6.value = a[6]
    dut.inp7.value = a[7]
    dut.inp8.value = a[8]
    dut.inp9.value = a[9]
    dut.inp10.value = a[10]
    dut.inp11.value = a[11]
    dut.inp12.value = a[12]
    dut.inp13.value = a[13]
    dut.inp14.value = a[14]
    dut.inp15.value = a[15]
    dut.inp16.value = a[16]
    dut.inp17.value = a[17]
    dut.inp18.value = a[18]
    dut.inp19.value = a[19]
    dut.inp20.value = a[20]
    dut.inp21.value = a[21]
    dut.inp22.value = a[22]
    dut.inp23.value = a[23]
    dut.inp24.value = a[24]
    dut.inp25.value = a[25]
    dut.inp26.value = a[26]
    dut.inp27.value = a[27]
    dut.inp28.value = a[28]
    dut.inp29.value = a[29]
    dut.inp30.value = a[30]
        
        
    # input driving
    for i in range(32):
        
        dut.sel.value = i
        
        await Timer(2, units='ns')

        dut._log.info(f'Inputs 0 to 30: {a} sel: {i} model={a[i]} DUT={dut.out.value}')

        assert dut.out.value == a[i], f"Mux result is incorrect: {dut.out.value} != {a[i]}, sel = {i}"