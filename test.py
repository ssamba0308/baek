import pyupbit 

access = "73kVqowGQOGEjdR31221j31j2ifekjkgjekgjekg"          # 본인 값으로 변경
secret = "egjekgj3iekeEEkej3i3j3iejjwiEejiejeEeijg"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회