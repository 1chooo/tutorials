# 本測試可發現若 list 結尾有 0，則 reverse 後會消失

a = ['1', '2', '3', '4', '0', '0']
a.reverse()
ans = ''.join(a)
print(int(ans))

# 我們也可以發現，若是字串，倒轉後 0 也會消失
b = '123400'
b = b[::-1]
print(int(b))