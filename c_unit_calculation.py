def get_entry_value(mag_string, chosen_unit, Mass, Length, Volume, Area, Time):
  if mag_string == 'Mass':
      x = Mass[chosen_unit]['value']
  elif mag_string == 'Length':
      x = Length[chosen_unit]['value']
  elif mag_string == 'Volume':
      x = Volume[chosen_unit]['value']
  elif mag_string == 'Area':
      x = Area[chosen_unit]['value']
  else:
      x = Time[chosen_unit]['value']
    
  return x

def get_output_value(mag_string, chosen_ounit, Mass, Length, Volume, Area, Time):
  if mag_string == 'Mass':
    y = Mass[chosen_ounit]['value']
  elif mag_string == 'Length':
    y = Length[chosen_ounit]['value']
  elif mag_string == 'Volume':
    y = Volume[chosen_ounit]['value']
  elif mag_string == 'Area':
    y = Area[chosen_ounit]['value']
  else:
    y = Time[chosen_ounit]['value']

  return y

def entry_convert_op(x, entr_amount):
  x = float(x)
  entr_amount = float(entr_amount)
  x_to_ru = entr_amount * x
  x_to_ru = float(x_to_ru)

  return x_to_ru

def calculate_output_amount(x, y, ru, x_to_ru):
  y = float(y)
  if x and y >= 1:
    y_a = x_to_ru / y
  elif y > ru:
    y_a = x_to_ru * y
  elif y == ru:
    y_a = x_to_ru * 1
  else:
    y_a = x_to_ru / y
  y_a = float(y_a)
  return y_a