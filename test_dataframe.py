'''This is a module for HW3 - Testing, and updated for style in HW4.'''

import pandas as pd
import numpy as np
import hw2_module

#Test Dataframe
DF2 = {'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'col2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
DF_TEST = pd.DataFrame(data=DF2)

#Testing item (2) for HW2
def test_hw2():
    '''This function tests whether the hw2 module works.

    It takes no direct imputs, but the test dataframe is defined globally.
    It outputs true if the dataframe passes the requirements.'''
    value = hw2_module.test_create_dataframe(DF_TEST, list(DF_TEST.columns))
    assert value

#Testing that all columns have values of the correct type
def test_correct_type():
    '''This function tests that all columns in the specified dataframe have the correct type.

    The type needs to be specified in the function and the test dataframe is defined above globally.
    It returns true if all values in all columns have values of the type specified.'''
    type0 = np.int64
    for col in DF_TEST:
        for row in DF_TEST.index:
            assert type(DF_TEST[col][row]) == type0

#Check for nan values
def test_nan_check():
    '''This test checks for nan values anywhere in the dataframe.

    It uses the global dataframe specified above.
    The test is passed if there are no nan values.'''
    assert not DF_TEST.isnull().values.any()


#Check that dataframe has at least one row
def test_rows():
    '''This test checks that the dataframe has at least one row.

    It uses the test dataframe defined globally above.'''
    assert len(DF_TEST.index) >= 1
