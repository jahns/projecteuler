# We need all the unique factors less than or equal to 20
factors = [16, 9, 5, 7, 11, 13, 17, 19]

product = 1

# for each factor multiply the previous product by the new factor
for factor in factors:
    product *= factor

print(product)
