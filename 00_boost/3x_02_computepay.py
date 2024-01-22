def computepay(hours, rate):
    if hours > 40:
        pay = 40*rate + (hours-40)*rate*1.5
    else:
        pay = hours * rate
    return pay

string_hours = input('Enter hours : ')
string_rate = input('Enter rate : ')

f_hours = float(string_hours)
f_rate = float(string_rate)

result = computepay(f_hours, f_rate)

print("Pay : ", result)


