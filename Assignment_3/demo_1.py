import pytest

data = [
    ("one", "two", "three"), ("four", "five", "six"), ("seven", "eight", "nine")

]


@pytest.mark.parametrize('param1,param2,param3', data)
def test_data_1(param1, param2, param3):
    print('This is test1')
    print(param1)
    print(param2)
    print(param3)
    assert True


'''
output
$ pytest -vv demo_1.py -s
=================================================================================================== test session starts ===================================================================================================
platform darwin -- Python 3.7.9, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /Users/rajeshsingh/Documents/Assignments/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/rajeshsingh/Documents/Assignments/Assignment_3
collected 3 items                                                                                                                                                                                                         

demo_1.py::test_data_1[one-two-three] This is test1
one
two
three
PASSED
demo_1.py::test_data_1[four-five-six] This is test1
four
five
six
PASSED
demo_1.py::test_data_1[seven-eight-nine] This is test1
seven
eight
nine
PASSED

==================================================================================================== 3 passed in 0.01s ====================================================================================================
(
'''
