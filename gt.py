variables = [] # array of n variables
coefs = [] # array of m x (n+1) coefficients for constraints, m - number of constraints
c_signs = [] # array of signs for constraints

def check_constraints(var, coefs, signs):
    for j in range(len(coefs)):
        sum = 0
        for i in range(len(var)): sum+=var[i]*coefs[j][i]
        if signs[j] == '<':
            if sum >= coefs[j][-1]: return False
        elif signs[j] == '>':
            if sum <= coefs[j][-1]: return False
        elif signs[j] == '<=':
            if sum > coefs[j][-1]: return False
        elif signs[j] == '>=':
            if sum < coefs[j][-1]: return False
    return True


