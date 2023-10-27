price = 1000000

has_good_credit = True

if has_good_credit:
    down_payment = 0.01 * 1000000
else:
    down_payment = 0.02 * 1000000

print(int(down_payment))
