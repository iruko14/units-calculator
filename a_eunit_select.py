mass_list = '''
Which unit do you want to convert?
1.Tons
2.Kilogram
3.Gram
4.Milligram
5.Pound
6.Ounce
'''

length_list = '''
Which unit do you want to convert?
1.Kilometer
2.Meter
3.Centimeter
4.Millimeter
5.Inch
6.Foot
7.Yard
8.Mile
'''

volume_list = '''
Which unit do you want to convert?
1.Cubic kilometer
2.Cubic meter
3.Cubic centimeter
4.Cubic millimeter
5.Cubic mile
6.Acre-foot
7.Cubic yard
8.Cubic foot
9.Cubic inch
10.Liter
11.Deciliter
12.Milliliter
13.Barrel
14.Gallon
15.Quart
16.Pint
17.Liquid ounce
'''

area_list = '''
Which unit do you want to convert?
1.Square kilometer
2.Hectare
3.Square meter
4.Square centimeter
5.Square millimeter
6.Square mile
7.Acre
8.Square yard
9.Square foot
10.Square inch
'''

time_list = '''
Which unit do you want to convert?
1.Century
2.Decade
3.Year
4.Month
5.Week
6.Day
7.Hour
8.Minute
9.Second
10.Millisecond
'''

def get_unit_list(mag_string):
  """
  Returns a unit list based on the provided magnitude string.
  """
  if mag_string == "Mass":
    unit_list = mass_list
  elif mag_string == "Length":
    unit_list = length_list
  elif mag_string == "Volume":
    unit_list = volume_list
  elif mag_string == "Area":
    unit_list = area_list
  else:
    unit_list = time_list
  return unit_list

def get_unit_choice(unit_list):
  """
  Prompts the user for a unit choice from the provided list.
  """
  print(unit_list)
  unit_set = input("Mark the number corresponding to your chosen unit: ")
  return unit_set