import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
# переменные для задачи - подбор арендной недвижимости (учитывать цену, местоположение, состояние)
quantity_money = ctrl.Antecedent(np.arange(40, 200, 1), 'quantity_money')
quantity_needs = ctrl.Antecedent(np.arange(1, 9, 1), 'quantity_needs')
terms_use = ctrl.Antecedent(np.arange(2, 10, 1), 'terms_use')
power = ctrl.Consequent(np.arange(0.5, 4, 1), 'power')
power.automf(names=['low', 'medium', 'high'])

quantity_money['low'] = fuzz.trapmf(quantity_money.universe, [40, 50, 60, 80])
quantity_money['medium'] = fuzz.trapmf(quantity_money.universe, [60, 80, 100, 120])
quantity_money['big'] = fuzz.trapmf(quantity_money.universe, [100, 130, 160, 200])

quantity_needs['low'] = fuzz.trapmf(quantity_needs.universe, [1, 2, 3, 4])
quantity_needs['medium'] = fuzz.trapmf(quantity_needs.universe,[3, 4, 5, 6])
quantity_needs['high'] = fuzz.trapmf(quantity_needs.universe,[5, 7, 8, 9])

terms_use['low'] = fuzz.trapmf(terms_use.universe, [2, 3, 4, 5])
terms_use['medium'] = fuzz.trapmf(terms_use.universe,[4, 5, 6, 7])
terms_use['long'] = fuzz.trapmf(terms_use.universe,[6, 8, 9, 10])

power['low'] = fuzz.trapmf(power.universe, [0.5, 1, 1.25, 1.5])
power['medium'] = fuzz.trapmf(power.universe,[1, 1.5, 2, 2.5])
power['high'] = fuzz.trapmf(power.universe,[2, 2.5, 3, 4])
 #построение графиков
#quantity_money.view()
#quantity_needs.view()
#terms_use.view()
#power.view()
plt.show()
rule1 = ctrl.Rule(quantity_money['big'] & (quantity_needs['high'] | quantity_needs['medium']) & terms_use['long'], power['high'])
rule2 = ctrl.Rule((quantity_money['big'] | quantity_money['medium']) & quantity_needs['medium'] & terms_use['medium'],power['medium'])
rule3 = ctrl.Rule(quantity_money['medium'] & quantity_needs['low'] & terms_use['medium'],power['medium'])
rule4 = ctrl.Rule(quantity_money['low'] & quantity_needs['high'] & (terms_use['medium'] | terms_use['low']),power['low'])
rule5 = ctrl.Rule(quantity_money['big'] & (quantity_needs['medium'] | quantity_needs['low']) & terms_use['long'],power['medium'])
rule6 = ctrl.Rule(quantity_money['big'] & quantity_needs['high'] & terms_use['long'],power['high'])
d_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
simulator= ctrl.ControlSystemSimulation(d_ctrl)

#
simulator.input['quantity_money'] = 140
simulator.input['quantity_needs'] = 8
simulator.input['terms_use'] = 9

#результат
simulator.compute()
print(simulator.output['power'])
#quantity_money.view(sim=simulator)
#quantity_needs.view(sim=simulator)
#terms_use.view(sim=simulator)
power.view(sim=simulator)
plt.show()