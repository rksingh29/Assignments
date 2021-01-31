import pytest
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
data = [
    ("one", "two", "three"), ("four", "five", "six"), ("seven", "eight", "nine")

]


@pytest.mark.parametrize('param1,param2,param3', data)
def test_data_1(param1, param2, param3):
    log.info('This is test1')
    log.info(param1)
    log.info(param2)
    log.info(param3)
    if param3 == 'nine':
        raise Exception('this is exception for nine')
    assert True


'''
output
$  pytest -vv demo_8.py
=========================================== test session starts ============================================
platform darwin -- Python 3.7.9, pytest-6.3.0.dev150+ged8f424bc, py-1.9.0, pluggy-0.13.1 -- /Users/rajeshsingh/Documents/Assignments/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/rajeshsingh/Documents/Assignments/Assignment_8, configfile: pytest.ini
collected 3 items                                                                                          

demo_8.py::test_data_1[one-two-three] 
---------------------------------------------- live log call -----------------------------------------------
2021-01-31 21:55:12 INFO This is test1
2021-01-31 21:55:12 INFO one
2021-01-31 21:55:12 INFO two
2021-01-31 21:55:12 INFO three
PASSED                                                                                               [ 33%]
demo_8.py::test_data_1[four-five-six] 
---------------------------------------------- live log call -----------------------------------------------
2021-01-31 21:55:12 INFO This is test1
2021-01-31 21:55:12 INFO four
2021-01-31 21:55:12 INFO five
2021-01-31 21:55:12 INFO six
PASSED                                                                                               [ 66%]
demo_8.py::test_data_1[seven-eight-nine] 
---------------------------------------------- live log call -----------------------------------------------
2021-01-31 21:55:12 INFO This is test1
2021-01-31 21:55:12 INFO seven
2021-01-31 21:55:12 INFO eight
2021-01-31 21:55:12 INFO nine
FAILED                                                                                               [100%]

================================================= FAILURES =================================================
______________________________________ test_data_1[seven-eight-nine] _______________________________________

param1 = 'seven', param2 = 'eight', param3 = 'nine'

    @pytest.mark.parametrize('param1,param2,param3', data)
    def test_data_1(param1, param2, param3):
        log.info('This is test1')
        log.info(param1)
        log.info(param2)
        log.info(param3)
        if param3 == 'nine':
>           raise Exception('this is exception for nine')
E           Exception: this is exception for nine

demo_8.py:19: Exception
-------------------------------------------- Captured log call ---------------------------------------------
2021-01-31 21:55:12 INFO This is test1
2021-01-31 21:55:12 INFO seven
2021-01-31 21:55:12 INFO eight
2021-01-31 21:55:12 INFO nine
========================================= short test summary info ==========================================
FAILED demo_8.py::test_data_1[seven-eight-nine] - Exception: this is exception for nine
======================================= 1 failed, 2 passed in 0.04s ========================================
(venv) [21:55:12 ~/Documents/Assignments/Assignment_8] 

'''
