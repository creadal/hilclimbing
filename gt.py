MAXIMIZE = 'max'
MINIMIZE = 'min' # constants for defining a problem

variables = [] # array of n variables
coefs = [] # array of m x (n+1) coefficients for constraints, m - number of constraints
c_signs = [] # array of signs for constraints
objective = [] # array of coefficients for objective linear function


def check_constraints(var, coefs, signs):

    for j in range(len(coefs)):

        sum = 0

        for i in range(len(var)): sum += var[i] * coefs[j][i]

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
    direction = None

    for s in [1, -1]:

        for i in range(len(var)):

            var2 = var[:]
            var2[i] += s

            if not check_constraints(var2, coefs, signs):
                continue

            if problem == MAXIMIZE:
                
                if calc_diff(var, var2, objective) > mx:

                    mx = calc_diff(var, var2, objective)
                    index = i
                    direction = s
            
            elif problem == MINIMIZE:

                if calc_diff(var, var2, objective) < mn:

                    mn = calc_diff(var, var2, objective)
                    index = i
                    direction = s

    return index, direction


def is_optimal(var, objective, problem, signs):

    if problem == MAXIMIZE:

        for s in [-1, 1]:

            for i in range(len(var)):
                
                var2 = var[:]
                var2[i] += s

                if not check_constraints(var2, coefs, signs):
                    continue

                if calc_diff(var, var2, objective) > 0:

                    return False

    if problem == MINIMIZE:

        for s in [-1, 1]:

            for i in range(len(var)):
                
                var2 = var[:]
                var2[i] += s

                if not check_constraints(var2, coefs, signs):
                    continue

                if calc_diff(var, var2, objective) < 0:

                    return False
    return True


def solve(var, coefs, signs, objective, problem):

    while not is_optimal(var, objective, problem, signs):

        i, d = find_optimal_direction(var, coefs, signs, objective, problem)
        var[i] += d


variables = [50, 0]
coefs = [[1, 0, 0], [0, 1, 0], [1, 1, 100]]
c_signs = ['>=', '>=', '<=']
objective = [2, 1]

solve(variables, coefs, c_signs, objective, MAXIMIZE)

print (variables)
