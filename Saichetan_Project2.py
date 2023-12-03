def generate_candidates(input):
    n = len(input)
    for i in range(1, 2**n):
        subset = list()
        for j in range(n):
            if (i & (2**j) > 0):
                    subset.append(input[j])
        yield subset

def verifier(M, candidate):
     return total_stock_value(candidate) <= M

def total_stock_value(candidate):
     total = 0
     for i in range(len(candidate)):
          total += candidate[i][1]
     return total

def total_value(candidate):
    total = 0
    for i in range(len(candidate)):
        total += candidate[i][0]
    return total


def exhaustive_approach(stocks_and_vals_arr, amount):
    best = None
    for candidate in generate_candidates(stocks_and_vals_arr):
        if verifier(amount, candidate):
            if best is None or total_value(candidate) > total_value(best):
                best = candidate

    return total_value(best)

def dynamic_approach(size_of_array, stocks_and_vals_arr, amount):
    memo_table = [[0 for x in range(amount+1)] for x in range(size_of_array+1)]

    for i in range(0, size_of_array+1):
        for j in range(0, amount+1):
            if i == 0 or j == 0:
                memo_table[i][j] = 0
            elif stocks_and_vals_arr[i-1][1] <= j:
                memo_table[i][j] = max(stocks_and_vals_arr[i-1][0] + memo_table[i-1][j-stocks_and_vals_arr[i-1][1]], memo_table[i-1][j])
            else:
                memo_table[i][j] = memo_table[i-1][j]
    return memo_table[size_of_array][amount]
    
with open('input.txt', 'r') as file:
    lines = file.readlines()

i = 0
with open('output.txt', 'w') as outfile:
    while i < len(lines):
        if lines[i] == "\n":
            i += 1
        size_of_array = int(lines[i])
        stocks_and_vals_arr = eval(lines[i+1])
        amount = int(lines[i+2])
        i += 3

        exhaus_output = exhaustive_approach(stocks_and_vals_arr, amount)
        dynam_output = dynamic_approach(size_of_array, stocks_and_vals_arr, amount)

        outfile.write(f"Size: {size_of_array}\nArray: {stocks_and_vals_arr}\nTotal Amount: {amount}\nExhaustive Output: {exhaus_output}\nDynamic Output: {dynam_output}\n\n")