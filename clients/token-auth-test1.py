import requests


def client():
    #token_h = "Token 2627b47c31078f244bd64e89a687f881acebd417"
    credentials = {"username": "Ind102", "password": "xx32L*;;"}
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    # headers = {"Authorization": token_h}
    # response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print('Status Code: ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()




