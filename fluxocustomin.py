#Primeiro, preparamos o ambiente pyomo. Para isso, executamos os 3 comandos a seguir:

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Criando uma inst�ncia do modelo

modelo = pyo.ConcreteModel()

# Criando vari�veis 

modelo.AB = pyo.Var(domain=pyo.NonNegativeReals)
modelo.AC = pyo.Var(domain=pyo.NonNegativeReals)
modelo.AD = pyo.Var(domain=pyo.NonNegativeReals)
modelo.BC = pyo.Var(domain=pyo.NonNegativeReals)
modelo.CE = pyo.Var(domain=pyo.NonNegativeReals)
modelo.DE = pyo.Var(domain=pyo.NonNegativeReals)
modelo.ED = pyo.Var(domain=pyo.NonNegativeReals)

# Facilitando a forma de chamar as vari�veis no modelo

AB = modelo.AB
AC = modelo.AC
AD = modelo.AD
BC = modelo.BC
CE = modelo.CE
DE = modelo.DE
ED = modelo.ED


#Restri��es de fluxo
modelo.R1 = pyo.Constraint(expr= AB + AC + AD == 50)
modelo.R2 = pyo.Constraint (expr= -AB + BC == 40)
modelo.R3 = pyo.Constraint (expr = -AC - BC + CE == 0)
modelo.R4 = pyo.Constraint (expr= - AD + DE - ED == -30)
modelo.R5 = pyo.Constraint (expr= - CE - DE + ED == -60)

#Restri��es de capacidade
modelo.R6 = pyo.Constraint (expr= AB  <= 10)
modelo.R7 = pyo.Constraint (expr= CE <= 80)


# Fun��o objetivo
modelo.obj = pyo.Objective(expr= 2 * AB + 4 * AC + 9 * AD + 3 * BC + CE + 3 * DE + 2 * ED, sense = minimize)

Z = modelo.obj

# Chamando o solver

opt = SolverFactory('glpk') #outro solver poss�vel � o gurobi
opt.solve(modelo)


#Imprimindo os resultados

modelo.pprint()

print('\n---------------------------------------------------------------------')
print('x_AB = ', pyo.value(AB))
print('x_AC = ', pyo.value(AC))
print('x_AD = ', pyo.value(AD))
print('x_BC = ', pyo.value(BC))
print('x_CE = ', pyo.value(CE))
print('x_DE = ', pyo.value(DE))
print('x_ED = ', pyo.value(ED))
print('Fun��o objetivo = ', pyo.value(Z))
