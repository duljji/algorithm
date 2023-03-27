N = input()

U_check = False
C_check = False
P_check = False

for i in N :
    if i == 'U' :
        U_check = True
    if U_check and i == 'C' :
        C_check = True
        if P_check :
            break
    if C_check and i == 'P' :
            P_check = True
            C_check = False

if U_check and C_check and P_check :
    print("I love UCPC")
else :
    print("I hate UCPC")

