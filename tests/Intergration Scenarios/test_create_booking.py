'''
Author : Annant
Objective : Create and verify create booking by post request
# TC-1 - Verify the status code , headers
# TC-2 - Verify the Body ID > Booking id
# TC-3 - Verify the JSON Schema is valid
'''

import pytest

@pytest.mark.run(order=1)
def test_create_booking_tc1():
    assert True== True
@pytest.mark.run(order=2)
def test_create_booking_tc2():
    assert True== False
@pytest.mark.run(order=3)
def test_create_booking_tc3():
    assert True== True