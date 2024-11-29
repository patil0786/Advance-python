# Simple interest calculation
def simple_interest(p,r,n):
    i = (p*r*n)/100
    amt = p + i
    return {"interest": i, "amount" : amt}

# Take input from users in console
p = int(input("Please enter the Principal in INR"))
n = int(input("Please enter the Number of Years "))
r = float(input("Please enter the Rate of Interest"))

# Calculate interest and amount
result = simple_interest(p,r,n)

print(result)



