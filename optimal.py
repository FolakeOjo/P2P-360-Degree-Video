from pulp import *
import random

chunks ={}
users={}
b= {}
v={}
x={}
result = []
alpha={}
b_quality =390
b_max = 10000
chunk_size=4

# A dictionary of the users is created
for i in range(16):
    for j in range(3):
        result.append((i,j))



for t in range(0,16):
    for q in range(0,3):
        x[t,q] = random.randint(1,2)
#variable definition
try:
    for i in range(0,chunk_size):
        chunks[i] = 4
        for t in range(0,16):
            for q in range(0,3):
                b[t,q] = q*b_quality
                #OUTPUT BANDWITH
except Exception, e:
    print e


# Create the 'prob' variable to contain the problem data
prob = LpProblem("Quality of experience", LpMaximize)

# A dictionary called 'ingredient_vars' is created to contain the referenced Variables
Ingred_vars = LpVariable.dicts("User",result,0)

print [x[i] for i in result]

print [x.get(i) for i in result]
# The objective function is added to 'prob' first
#Quality of Experience  
try:
    for tiles in range(16):
        for q in range(3):
            v[tiles] = random.randint(0,2)
            if sum(alpha.values()) == 1:
                for t in range(16):
                    for q in range(3):
                        v[t,q] = random.randint(3,9)
                        alpha[t,q] =random.randint(1,4)
                        #a=((v[t,q] * alpha[t,q]) * b[t,q]) 
      #measuring quality of experience
      #v_sum = (v[t,q] * alpha[t,q]) * b[t,q]
except Exception, e:
    print e

prob += lpSum(random.randint(0,1)*b[i]*[x[i]*Ingred_vars[i] for i in result]), "Objective function"

# The constraints are added to 'prob'
prob +=lpSum([x[i]*Ingred_vars[i] for i in result]) == 90, "The summation musnt exceed 90"
#non-peer Assisted Bandwidth#
for tiles in range(16):
    alpha[tiles] =random.randint(0,1)
    if alpha[tiles] == 1:
        prob +=lpSum([x[i]*Ingred_vars[i] *b[i] for i in result]) <= b_max
    

#peer Assisted Bandwidth
try:
    savedTiles = 0
    for t in range(16):
        for q in range(3):
            if x[t,q] == x[t+1,q+1]:
                savedTiles += ((x[t,q]) - 1)
                #savedTiles += (x[t,q]) - 1
                #OUTPUT SAVED TITLES IN TOTAL
                prob +=lpSum([x[i]*Ingred_vars[i] - savedTiles * b[i] for i in result]) <= b_max
            
    
except Exception, e:
    print e

prob.writeLP("Qoe.lp")
print (prob)

prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue+10)
