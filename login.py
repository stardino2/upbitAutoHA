import pyupbit
import jwt
import uuid
import requests

def login():
    access = "m1UBokppMrkwGjo7cUBPjQpLH8NUXNDlHCYyvZdN"          # 본인 값으로 변경
    secret = "BUxPdqWEFaJ5e5HZbX5V4lov3bYVoCheF07xNy6U"          # 본인 값으로 변경
    upbit = pyupbit.Upbit(access, secret)
    
    # print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
    # print(upbit.get_balance("KRW"))         # 보유 현금 조회
    
    access_key = access
    secret_key = secret
    server_url = 'https://api.upbit.com/'

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}
    requests.get(server_url + "/v1/accounts", headers=headers)
    return upbit