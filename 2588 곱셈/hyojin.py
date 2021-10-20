A = 473
B = 3856

C = str(B)
D = len(C)


def add(A, B):
    for i in range(int(D), 0, -1):
        B_ = C[i - 1]
        print(A * int(B_))
    print(A * B)


add(A, B)
