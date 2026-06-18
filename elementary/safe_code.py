def total_code(code_digits):
    sum_digits = 0
    for PW in code_digits:
        sum_digits += code_digits[PW]
    return sum_digits


def code_is_ok(code_digits):
    if (
        code_digits["five"] + code_digits["three"] == 14
        and code_digits["one"] == code_digits["two"] * 2 - 1
        and code_digits["four"] == code_digits["two"] + 1
        and code_digits["two"] + code_digits["three"] == 10
    ):
        if total_code(code_digits) == 30:
            return True


for safecode in range(0, 100000):
    this_code = str(safecode).zfill(5)

    code_digits = {}
    code_digits["one"] = int(this_code[0])
    code_digits["two"] = int(this_code[1])
    code_digits["three"] = int(this_code[2])
    code_digits["four"] = int(this_code[3])
    code_digits["five"] = int(this_code[4])

    if code_is_ok(code_digits):
        print(safecode)
