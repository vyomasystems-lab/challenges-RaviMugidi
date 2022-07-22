# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    in0=0
    in1=1
    in2=2
    in3=3
    in4=1
    in5=2
    in6=3
    in7=0
    in8=1
    in9=2
    in10=3
    in11=0
    in12=1
    in13=2
    in14=3
    in15=0
    in16=1
    in17=2
    in18=3
    in19=0
    in20=1
    in21=2
    in22=3
    in23=3
    in24=0
    in25=1
    in26=2
    in27=3
    in28=0
    in29=1
    in30=2
    
    sel=15

    dut.inp0.value=in0
    dut.inp1.value=in1
    dut.inp2.value=in2
    dut.inp3.value=in3
    dut.inp4.value=in4
    dut.inp5.value=in5
    dut.inp6.value=in6
    dut.inp7.value=in7
    dut.inp8.value=in8
    dut.inp9.value=in9
    dut.inp10.value=in10
    dut.inp11.value=in11
    dut.inp12.value=in12
    dut.inp13.value=in13
    dut.inp14.value=in14
    dut.inp15.value=in15
    dut.inp16.value=in16
    dut.inp17.value=in17
    dut.inp18.value=in18
    dut.inp19.value=in19
    dut.inp20.value=in20
    dut.inp21.value=in21
    dut.inp22.value=in22
    dut.inp23.value=in23
    dut.inp24.value=in24
    dut.inp25.value=in25
    dut.inp26.value=in26
    dut.inp27.value=in27
    dut.inp28.value=in28
    dut.inp29.value=in29
    dut.inp30.value=in30

    dut.sel.value=sel

    if (sel==0):
        out=in0
    elif (sel==1):
        out=in1
    elif (sel==2):
        out=in2
    elif (sel==3):
        out=in3
    elif (sel==4):
        out=in4
    elif (sel==5):
        out=in5
    elif (sel==6):
        out=in6
    elif (sel==7):
        out=in7
    elif (sel==8):
        out=in8
    elif (sel==9):
        out=in9
    elif (sel==10):
        out=in11
    elif (sel==12):
        out=in12
    elif (sel==13):
        out=in13
    elif (sel==14):
        out=in14
    elif (sel==15):
        out=in15
    elif (sel==16):
        out=in16
    elif (sel==17):
        out=in17
    elif (sel==18):
        out=in18
    elif (sel==19):
        out=in19
    elif (sel==20):
        out=in20
    elif (sel==21):
        out=in21
    elif (sel==22):
        out=in22
    elif (sel==23):
        out=in23
    elif (sel==24):
        out=in24
    elif (sel==25):
        out=in25
    elif (sel==26):
        out=in26
    elif (sel==27):
        out=in27
    elif (sel==28):
        out=in28
    elif (sel==29):
        out=in29
    elif (sel==30):
        out=in30
    assert dut.out.value==out,f"mux result is incorrect"
   

    //cocotb.log.info('##### CTB: Develop your test here ########')
