from a_eunit_select import *
from b_ounit_select import *
from c_unit_calculation import *
from d_output_result import *

print('Welcome to the Unit Calculator!')
mag_entry = input('''What magnitude do you want to convert?
1.Mass
2.Length
3.Volume
4.Area
5.Time
Mark the number corresponding to each magnitude: ''')

mag_dict = {
    "1": "Mass",
    "2": "Length",
    "3": "Volume",
    "4": "Area",
    "5": "Time"
}

if mag_entry in mag_dict:
  # Get the corresponding magnitude string
  mag_string = mag_dict[mag_entry]

  # Print the selected magnitude and "selected"
  print(f"{mag_string} selected")
else:
  # Print an error message if the input is invalid
  print(f"Invalid input: '{mag_entry}'. Please select a valid number (1-5).")

# Get the unit list
unit_list = get_unit_list(mag_string)

# Get the user's chosen unit
chosen_unit = get_unit_choice(unit_list)

#Units tab dictionary
Mass = {
    0: {
        'unit': 'ru',
        'value': 1
    },
    1: {
        'unit': 'Tons',
        'value': 1000
    },
    2: {
        'unit': 'Kilogram',
        'value': 1
    },
    3: {
        'unit': 'Gram',
        'value': 0.001
    },
    4: {
        'unit': 'Milligram',
        'value': 0.000001
    },
    5: {
        'unit': 'Pound',
        'value': 0.4535920000001679
    },
    6: {
        'unit': 'Ounce',
        'value': 0.0283495
    }
}

Length = {
    0: {
        'unit': 'ru',
        'value': 1
    },
    1: {
        'unit': 'Kilometer',
        'value': 1000
    },
    2: {
        'unit': 'Meter',
        'value': 1
    },
    3: {
        'unit': 'Centimeter',
        'value': 0.01
    },
    4: {
        'unit': 'Millimeter',
        'value': 0.001
    },
    5: {
        'unit': 'Inch',
        'value': 0.0254
    },
    6: {
        'unit': 'Foot',
        'value': 0.3048
    },
    7: {
        'unit': 'Yard',
        'value': 0.9144
    },
    8: {
        'unit': 'Mile',
        'value': 1609.34
    },
}

Volume = {
    0: {
        'unit': 'ur',
        'value': 1
    },
    1: {
        'unit': 'Cubic kilometer',
        'value': 1000000000
    },
    2: {
        'unit': 'Cubic meter',
        'value': 1
    },
    3: {
        'unit': 'Cubic centimeter',
        'value': 0.000001
    },
    4: {
        'unit': 'Cubic millimeter',
        'value': 0.000001
    },
    5: {
        'unit': 'Cubic mile',
        'value': 4168181825.4
    },
    6: {
        'unit': 'Acre-foot',
        'value': 0.0283168466
    },
    7: {
        'unit': 'Cubic yard',
        'value': 0.764554858
    },
    8: {
        'unit': 'Cubic foot',
        'value': 0.0283168466
    },
    9: {
        'unit': 'Cubic inch',
        'value': 0.0000163871
    },
    10: {
        'unit': 'Liter',
        'value': 0.001
    },
    11: {
        'unit': 'Deciliter',
        'value': 0.0001
    },
    12: {
        'unit': 'Milliliter',
        'value': 0.000001
    },
    13: {
        'unit': 'Barrel',
        'value': 0.1192404712
    },
    14: {
        'unit': 'Gallon',
        'value': 0.00378541103373138
    },
    15: {
        'unit': 'Quart',
        'value': 0.0011365225
    },
    16: {
        'unit': 'Pint',
        'value': 0.0005682613
    },
    17: {
        'unit': 'Liquid ounce',
        'value': 0.0000295735
    },
}

Area = {
    0: {
        'unit': 'ur',
        'value': 1
    },
    1: {
        'unit': 'Square kilometer',
        'value': 1000000
    },
    2: {
        'unit': 'Hectare',
        'value': 10000
    },
    3: {
        'unit': 'Square meter',
        'value': 1
    },
    4: {
        'unit': 'Square centimeter',
        'value': 0.0001
    },
    5: {
        'unit': 'Square millimeter',
        'value': 0.000001
    },
    6: {
        'unit': 'Square mile',
        'value': 2589988.1103
    },
    7: {
        'unit': 'Acre',
        'value': 4046.8564224
    },
    8: {
        'unit': 'Square yard',
        'value': 0.83612736
    },
    9: {
        'unit': 'Square foot',
        'value': 0.09290304
    },
    10: {
        'unit': 'Square inch',
        'value': 0.00064516
    },
}

Time = {
    0: {
        'unit': 'ur',
        'value': 1
    },
    1: {
        'unit': 'Century',
        'value': 3155760000
    },
    2: {
        'unit': 'Decade',
        'value': 315576000
    },
    3: {
        'unit': 'Year',
        'value': 31557600
    },
    4: {
        'unit': 'Month',
        'value': 2628000
    },
    5: {
        'unit': 'Week',
        'value': 604800
    },
    6: {
        'unit': 'Day',
        'value': 86400
    },
    7: {
        'unit': 'Hour',
        'value': 3600
    },
    8: {
        'unit': 'Minute',
        'value': 60
    },
    9: {
        'unit': 'Second',
        'value': 1
    },
    10: {
        'unit': 'Millisecond',
        'value': 0.001
    },
}

#chosen_unit convert to int
chosen_unit = int(chosen_unit)

# Print the entry unit
if mag_string == 'Mass':
  unit_print = Mass[chosen_unit]['unit']
elif mag_string == 'Length':
  unit_print = Length[chosen_unit]['unit']
elif mag_string == 'Volume':
  unit_print = Volume[chosen_unit]['unit']
elif mag_string == 'Area':
  unit_print = Area[chosen_unit]['unit']
else:
  unit_print = Time[chosen_unit]['unit']
print(unit_print,' is selected')
    
#Select the amount of the entry unit
entr_amount = input('select an amount: ')

# Get the output unit list
unit_list = get_unit_list_o(mag_string)

# Get the user's chosen output unit
chosen_ounit = get_unit_choice_o(unit_list)

#o_chosen_unit convert to int
chosen_ounit = int(chosen_ounit)

# Print the exit unit
if mag_string == 'Mass':
    o_unit_print = Mass[chosen_ounit]['unit']
elif mag_string == 'Length':
    o_unit_print = Length[chosen_ounit]['unit']
elif mag_string == 'Volume':
    o_unit_print = Volume[chosen_ounit]['unit']
elif mag_string == 'Area':
    o_unit_print = Area[chosen_ounit]['unit']
else:
  o_unit_print = Time[chosen_ounit]['unit']
print(o_unit_print,' is selected as the output unit')

#Defining ru
ru = 1
ru =float(ru)

#Get the entry unit conversion value
x = get_entry_value(mag_string, chosen_unit, Mass, Length, Volume, Area, Time)

#Get the output unit conversion value
y = get_output_value(mag_string, chosen_ounit, Mass, Length, Volume, Area, Time)

#Convert x amount to ru
x_to_ru = entry_convert_op(x, entr_amount)

#Convert x_to_ru to output amount
y_a = calculate_output_amount(x, y, ru, x_to_ru)

#Final results printing
output_results(entr_amount, unit_print, o_unit_print, y_a)