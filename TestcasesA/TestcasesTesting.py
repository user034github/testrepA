import pytest
from TestcasesProgram import isLeapYear

@pytest.mark.parametrize("Year", [4, 8, 12])
def test_DivBy4NotBy100(Year):
    assert isLeapYear(Year) == True

@pytest.mark.parametrize("Year", [400, 800, 1200])
def test_DivBy400(Year):
    assert isLeapYear(Year) == True

@pytest.mark.parametrize("Year", [1, 2, 3])
def test_NotDivBy4(Year):
    assert isLeapYear(Year) == False

@pytest.mark.parametrize("Year", [100, 200, 300])
def test_DivBy100NotBy400(Year):
    assert isLeapYear(Year) == False

