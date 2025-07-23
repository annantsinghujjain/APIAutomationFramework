#HTTP Status code

def verify_http_code(response_data,expected_data):
    assert response_data.status_code == expected_data,"Expected HTTP Status : "+expected_data

# All of these are utilities
#Any key , should not be null,of empty

def verify_key(response_data,key):
    assert len(response_data[key]) != 0,"Key is non empty: "+ key
    assert response_data[key] > 0,"key should be greater than zero:" +key
