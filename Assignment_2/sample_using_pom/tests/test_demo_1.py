import pytest


def test_t1(login_page, logout):
    title = login_page.title
    print(title)
    print('done')

'''
==================================================================================================== 1 error in 19.44s ====================================================================================================
(venv) [15:40:19 ~/Documents/Assignments/Assignment_2/sample_using_pom] 
$ python -m pytest
=================================================================================================== test session starts ===================================================================================================
platform darwin -- Python 3.7.9, pytest-6.3.0.dev150+ged8f424bc, py-1.9.0, pluggy-0.13.1
rootdir: /Users/rajeshsingh/Documents/Assignments/Assignment_2/sample_using_pom
collected 1 item                                                                                                                                                                                                          

tests/test_demo_1.py .                                                                                                                                                                                              [100%]

=================================================================================================== 1 passed in 17.51s ====================================================================================================
(venv) [15:42:03 ~/Documents/Assignments/Assignment_2/sample_using_pom] 

'''