#lex_auth_01269446533799116898

def check_perfect_number(number):
    sum = 0
    if number == 0:
        return False
    for i in range(1,number):
        if number%i == 0:
            sum  = sum + i
    if sum == number:
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    perfect_nums = []
    for i in no_list:
        if check_perfect_number(i):
            perfect_nums.append(i)
    return perfect_nums


perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)