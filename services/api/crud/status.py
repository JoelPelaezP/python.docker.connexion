from connexion.lifecycle import ConnexionResponse


def check_status():
    data = "Service API is up and running!"
    status_code = 200
    headers = {"Content-Type": "text/plain"}
    # return data, status_code, headers
    return ConnexionResponse(body=data, status_code=status_code, headers=headers)
