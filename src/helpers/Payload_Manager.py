def payload_create_booking():
    payload = {
    "firstname" : "Annant",
    "lastname": "Singh",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": "Breakfast"
}
    return payload