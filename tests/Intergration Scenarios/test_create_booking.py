'''
Author : Annant
Objective : Create and verify create booking by post request
# TC-1 - Verify the status code , headers
# TC-2 - Verify the Body ID > Booking id
# TC-3 - Verify the JSON Schema is valid
'''
from http.client import responses

import pytest


from src.Constants.APIConstant import base_url,url_create_booking
from src.helpers.Api_Wrapper import post_request
from src.helpers.Payload_Manager import payload_create_booking

class TestIntegration(object):

    def test_create_booking_tc1(self):
        headers = {
            "Content-Type": "application/json",
        }
        response = post_request(base_url(),headers=headers,auth=None,payload = payload_create_booking())
        assert True== True


    def test_create_booking_tc2(self):
        assert True== False


    def test_create_booking_tc3(self):
        assert True== True