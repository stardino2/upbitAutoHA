import pyupbit

access = "03prseVHgaVt9xUyETsJIxGoaEWynxroNoQlPESQ"          # 본인 값으로 변경
secret = "DFvZAJM3FpR2jUlxfvHy8KjiplUxrDveH24O7FWX"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW")) 