def cost_of_ground_shipping(weight):
  cost = 0
  if (weight <= 2):
    cost = (weight * 1.50) + 20.00
  elif (weight > 2) and (weight <= 6):
    cost = (weight * 3.00) + 20.00
  elif (weight > 6) and (weight <= 10):
    cost = (weight * 4.00) + 20.00
  else:
    cost = (weight * 4.75) + 20.00
  return cost

cost_of_premium_shipping = 125.00

def cost_of_drone_shipping(weight):
  cost = 0
  if (weight <= 2):
    cost = weight * 4.50
  elif (weight > 2) and (weight <= 6):
    cost = weight * 9.00
  elif (weight > 6) and (weight <= 10):
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost

def cheapest_shipping_cost(weight):
  ground_shipping = cost_of_ground_shipping(weight)
  drone_shipping = cost_of_drone_shipping(weight)
  premium_shipping = cost_of_premium_shipping
  if (ground_shipping < drone_shipping) and (ground_shipping < premium_shipping):
    return 'The cheapest shipping method is Ground Shipping. It will cost: '+str(ground_shipping)+'.'
  elif (drone_shipping < ground_shipping) and (drone_shipping < premium_shipping):
    return 'The cheapest shipping method is Drone Shipping. It will cost: '+str(drone_shipping)+'.'
  elif (premium_shipping < ground_shipping) and (premium_shipping < drone_shipping):
    return 'The cheapest shipping method is Premium Shipping. It will cost: '+str(premium_shipping)+'.'
  else:
    return 'Unable to calculate shipping cost for you, please try again later.'

print(cheapest_shipping_cost(40.5))