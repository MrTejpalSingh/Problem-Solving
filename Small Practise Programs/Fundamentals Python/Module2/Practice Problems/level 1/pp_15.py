# lex_auth_0127136075580375041172

def check_22(num_list):
    for i in range(len(num_list)-1):
        if num_list[i] == 2:
            if num_list[i+1] == 2:
                return True
    return False

print(check_22([3, 2, 5, 1, 2, 1, 2, 2]))