def add_recursive(n):
    if n == 1:
        # print("iteration is equal 1, stopped")
        return 1

    return add_recursive(n - 1) + add_recursive(n - 1)


print(add_recursive(30))