#!/usr/bin/python3

def list_division(A, B, length):
    C = []
    for i in range(length):
        try:
            c = A[i] / B[i]
        except (TypeError):
            print("wrong type")
            c = 0
        except (ZeroDivisionError):
            print("division by 0")
            c = 0
        except (IndexError):
            print("out of range")
            c = 0
        finally:
            C.append(c)
    return C
