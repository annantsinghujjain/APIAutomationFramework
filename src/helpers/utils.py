#helps you to read the json files and provide you the json data
import json


def get_payload_auth():
    # Read from auth.json and return json
    file_data=open("src/Resources/Auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data
