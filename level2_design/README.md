# Level2_Design Verification
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

# Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained.


The assert statement is used for comparing the outut to the expected value.

The following error is seen:
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x6 does not match MODEL = 0x0
```

# Test Scenario **(Important)**
Test inputs:mav_putvalue_src1 = 0x0/
    mav_putvalue_src2 = 0x6/
    mav_putvalue_src3 = 0x0/
    mav_putvalue_instr = 0x101010B3\
Expected output: 0x0\                 
Observed output in the DUT: DUT.out=0xc
\
Output mismatches for the above inputs proving that there is a design bug.

# Design Bug
The design produces 0x0 output for all input arguments.

# Design Fix

Updating the design and re-running the test makes the test pass.

![Screenshot (192)](https://user-images.githubusercontent.com/109639328/182215412-e73e9d2e-6c4b-4757-a545-1cd621824dab.png)

