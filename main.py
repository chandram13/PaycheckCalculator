# Marvish Chandra

#pF, pay frequency


# consider withheld income

def paycheckCalc(salary,pF1,pF2,pF3,pF4,pF5,pF6,pF7,pF8,dependents,SI,CI):
    firstPay = (salary * pF1 + (dependents * 500)) * SI * CI
    print(firstPay)
    secondPay = (salary * pF2 + (dependents * 500)) * SI * CI
    print(secondPay)
    thirdPay = (salary * pF3 + (dependents * 500)) * SI * CI
    print(thirdPay)
    fourthPay = (salary * pF4 + (dependents * 500)) * SI * CI
    print(fourthPay)
    fifthPay = (salary * pF5 + (dependents * 500)) * SI * CI
    print(fifthPay)
    sixthPay = (salary * pF6 + (dependents * 500)) * SI * CI
    print(sixthPay)
    seventhPay = (salary * pF7 + (dependents * 500)) * SI * CI
    print(seventhPay)
    eighthPay = (salary * pF8 + (dependents * 500)) * SI * CI
    print(eighthPay)

    paycheckCalc(400000,1.09,0,0,0,0,0,0,0,3,0.02,0.003)
