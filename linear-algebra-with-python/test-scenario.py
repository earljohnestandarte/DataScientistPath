# The Scenario: The Bakery 🥯You run a bakery that sells three items:
#     Muffins, Cakes, and Cookies.To make them, you need three ingredients:
#         Flour, Sugar, and Eggs.
#             Here is your Recipe Matrix ($R$):(Rows are Items, Columns are Ingredients)
#
#                 Item    | Flour (cups) | Sugar (cups) | Eggs (count)
#                 Muffin  |    2         |     0.5      |     1
#                 Cake    |    3         |     2        |     4
#                 Cookie  |    1         |     1        |     1

import numpy as np

recipe = np.array([
    [2, 0.5, 1],
    [3, 2, 4],
    [1, 1, 1],
])

cost = np.array([0.5, 0.2, 0.3])

item_cost = recipe @ cost

print(f"This is the item costs: {item_cost * 2}")