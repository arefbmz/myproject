from mendeleev import element

Atomic_number = int(input("please write your Atomic number : ").strip())
if 19 <= Atomic_number <= 87:

    E = element(Atomic_number)

    row = E.period
    col = E.group_id
    print(f"Row : {row}")
    print(f"Column : {col}")

else:
    print("Not valid")
