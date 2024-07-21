from Crypto.Util.number import long_to_bytes
mod = 123457
examine_num = 4
'''
credit_card = '543210******1234'
'''
for num in range(1000000):
    num = str(num)
    num = (6 - len(num)) * "0" + num
    num = int('543210' + num + '1234')
    if num % mod != 0:
        continue
    num = str(num)
    sum_ = sum(int(num[i]) if i % 2 == 1 else sum(int(ele) for ele in str(int(num[i]) * 2)) for i in range(len(num) - 1))
    test_examine = 10 - sum_ % 10
    if test_examine == examine_num:
        print(num)
        break


