
def raise_to_pow(base, power):
    RESULT=1.0
    for i in range (power):
        RESULT=RESULT * base
    return RESULT
base=float(input('enter base num: '))
power=int(input('enter power: '))
print(raise_to_pow(base,power))
