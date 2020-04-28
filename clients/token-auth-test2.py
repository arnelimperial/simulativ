import requests


def client():
    token_h = "Token 3510e46bca9a149ccc00ad96da73d8f432b2ef70"
    # Register a new user account
    # new_user = {
    #     "email": "test@test.io",
    #     "username": "Ind103",
    #     "first_name": "A",
    #     "last_name": "I",
    #     "password1": "xx32L*;;",
    #     "password2": "xx32L*;;"
    # }
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=new_user)

    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print('Status Code: ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()




