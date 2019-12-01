MAXIMUM = 'max'
MINIMUM = 'min' # constants for defining a problem

variables = [] # array of n variables
coefs = [] # array of m x (n+1) coefficients for constraints, m - number of constraints
c_signs = [] # array of signs for constraints
objective = [] # array of coefficients for objective linear function


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


def calc(var, objective):

    sum = 0

    for i in range(len(var)):

        sum += var[i] * objective[i]

    return sum


def calc_diff(var, var2, objective):

    result = calc(var2, objective) - calc(var, objective)

    return result


def find_optimal_direction(var, coefs, signs, objective, problem):
    
    mx = -1000000
    mn = 1000000
    index = None

    for s in [1, -1]:

        for i in range(len(var)):

            var2 = var[:]
            var2[i] += s

            if problem == MAXIMUM:
                if calc_diff(var, var2, objective) > mx:
                    mx = calc_diff(var, var2, objective)
                    index = i
            
            elif problem == MINIMUM:
                if calc_diff(var, var2, objective) < mn:
                    mn = calc_diff(var, var2, objective)
                    index = i

    return index

print (find_optimal_direction([1, 1], [[1, 1, 100], [1, 1, 100]], ['<', '<'], [2, 1], MAXIMUM))
