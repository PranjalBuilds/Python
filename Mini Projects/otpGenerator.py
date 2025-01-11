import random

def otpGenerator():
    otp = ''
    for i in range(4):
        otp += str(random.randint(0, 9))
    return otp
print(otpGenerator())