
import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import cmath
import decimal
from decimal import Decimal

CONTENT_CHECK = [
    'polygon_area', 
    'temp_converter', 
    'print', 
    'squared_power_list', 
    'speed_converter'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in CONTENT_CHECK:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_class_methods():
    code_lines = inspect.getmembers(session5)
    for word in CONTENT_CHECK:
        assert word not in code_lines, 'All Functions not used!'

def test_input_function_name():
    with pytest.raises(ValueError):
            session5.time_it(1, 2, sides=3), 'First positional argument must be function name'

def test_input_repetitions():
    with pytest.raises(ValueError):
            session5.time_it(session5.polygon_area, 2, sides=3, repetitons = 0), 'Number of repetitons must be greater than 0'
    with pytest.raises(ValueError):
            session5.time_it(session5.temp_converter, 2, sides=3, repetitons = -1), 'Number of repetitons must be greater than 0'
    with pytest.raises(ValueError):
            session5.time_it(session5.temp_converter, 2, sides=3, repetitons = 1.1), 'repetitons must be an integer'

def test_polygon_area_positional_arg():
    with pytest.raises(Exception):
            session5.time_it(session5.polygon_area,5, 2, sides=3, repetitons = 10), 'polygon_area must have only one positional argument - side length'

def test_temp_converter_positional_arg():
    with pytest.raises(Exception):
            session5.time_it(session5.temp_converter,100, 50, temp_given_in='f', repetitons = 10), 'temp_converter must have only one positional argument - temperature to be converted'

def test_speed_converter_positional_arg():
    with pytest.raises(Exception):
            session5.time_it(session5.speed_converter,100, 50, dist='km', time='min', repetitons = 10), 'speed_converter must have only one positional argument - speed to be converted'

def test_squared_power_list_positional_arg():
    with pytest.raises(Exception):
            session5.time_it(session5.squared_power_list,100, 50, start=0, end=3, repetitons = 10), 'squared_power_list must have only one positional argument - number to be squared'

def test_polygon_area_named_arg_count():
    with pytest.raises(Exception):
            session5.time_it(session5.polygon_area, 2, height=4, sides=3, repetitons = 10), 'polygon_area must have only one named argument - sides'

def test_temp_converter_named_arg_count():
    with pytest.raises(Exception):
            session5.time_it(session5.temp_converter, 100, temp_given_in='f', value=3, repetitons = 10), 'temp_converter must have only one named argument - temp_given_in'

def test_speed_converter_named_arg_count():
    with pytest.raises(Exception):
            session5.time_it(session5.speed_converter, 100, dist='km', time='min', value=10, repetitons = 10), 'speed_converter must have only two named arguments - dist, time'

def test_squared_power_list_named_arg_count():
    with pytest.raises(Exception):
            session5.time_it(session5.squared_power_list, 100, start=0, end=3, value=10, repetitons = 10), 'squared_power_list must have only two named arguments - start, end'
            
def test_print_named_arg_count():
    with pytest.raises(Exception):
            session5.time_it(session5.print, 1,2,3, sep='-', end=' ***\n', value=10, repetitons = 10), 'print must have only two named arguments - sep, end'

def test_polygon_area_named_arg_key():
    with pytest.raises(Exception):
            session5.time_it(session5.polygon_area, 2, side=3, repetitons = 10), 'polygon_area must have named argument - sides - indicating number of sides'
    with pytest.raises(Exception):
            session5.time_it(session5.polygon_area, 2, 3, repetitons = 10), 'polygon_area must have named argument - sides - indicating number of sides'

def test_polygon_area_named_arg_value():
    with pytest.raises(ValueError):
            session5.polygon_area(2, num_sides=2, repetitons = 10), 'Supports area calculation upto hexagon - sides must be between 3 and 6'
    with pytest.raises(ValueError):
            session5.polygon_area(2, num_sides='a', repetitons = 10), 'Supports area calculation upto hexagon - sides must be between 3 and 6'
    with pytest.raises(ValueError):
            session5.polygon_area(2, num_sides=-1, repetitons = 10), 'Supports area calculation upto hexagon - sides must be between 3 and 6'
    with pytest.raises(ValueError):
            session5.polygon_area(2, num_sides=5.5, repetitons = 10), 'Supports area calculation upto hexagon - sides must be between 3 and 6'

def test_polygon_area_positional_arg_value():
    with pytest.raises(ValueError):
            session5.polygon_area(0, num_sides=4, repetitons = 10), 'Side length must be greater than 0'
    with pytest.raises(ValueError):
            session5.polygon_area(-1, num_sides=5, repetitons = 10), 'Side length must be greater than 0'
    with pytest.raises(ValueError):
            session5.polygon_area('a', num_sides=5, repetitons = 10), 'Side length cannot be a string'

def test_polygon_area_calculation():
    for _ in range(50):
        side_len = random.randint(1,100)
        assert (session5.polygon_area(side_len, 3, 10)) == (math.sqrt(3)/4) * pow(side_len,2), f"Your program returned wrong area of equilateral traiangle"
        assert (session5.polygon_area(side_len, 4, 10)) == (side_len * side_len), f"Your program returned wrong area of square"
        assert (session5.polygon_area(side_len, 5, 10)) == 1/4 * math.sqrt(5*(5+(2*math.sqrt(5)))) * pow(side_len,2), f"Your program returned wrong area of regular pentagon"
        assert (session5.polygon_area(side_len, 6, 10)) == (3 * math.sqrt(3)/2) * pow(side_len,2), f"Your program returned wrong area of regular hexagon"

def test_temp_converter_named_arg_key():
    with pytest.raises(Exception):
            session5.time_it(session5.temp_converter, 100, temp='f', repetitons = 10), 'temp_converter must have named argument - temp_given_in - indicating given temerature'
    with pytest.raises(Exception):
            session5.time_it(session5.temp_converter, 100, 'f', repetitons = 10), 'temp_converter must have named argument - temp_given_in - indicating given temerature'

def test_temp_converter_named_arg_value():
    with pytest.raises(ValueError):
            session5.temp_converter(100, temp_given_in='a', repetitons = 10), "Supports conversion of Celcius to Fahrenheit and Fahrenheit to Celcius - Input 'c'/'C'/'f'/'F'"
    with pytest.raises(ValueError):
            session5.temp_converter(100, temp_given_in=8, repetitons = 10), "Supports conversion of Celcius to Fahrenheit and Fahrenheit to Celcius - Input 'c'/'C'/'f'/'F'"
    with pytest.raises(ValueError):
            session5.temp_converter(100, temp_given_in=100.0, repetitons = 10), "Supports conversion of Celcius to Fahrenheit and Fahrenheit to Celcius - Input 'c'/'C'/'f'/'F'"

def test_temp_converter_positional_arg_value():
    with pytest.raises(ValueError):
            session5.temp_converter(-450, temp_given_in='c', repetitons = 10), 'Temerature cannot be less than absolute 0 (0K or -273.15°C or -459.67°F)'
    with pytest.raises(ValueError):
            session5.temp_converter(-500, temp_given_in='F', repetitons = 10), 'Temerature cannot be less than absolute 0 (0K or -273.15°C or -459.67°F)'
    with pytest.raises(ValueError):
            session5.temp_converter('a', temp_given_in='F', repetitons = 10), 'Temerature cannot be a string'

def test_temp_converter_calculation():
    for _ in range(50):
        temp = random.randint(-100,100)
        assert (session5.temp_converter(temp, 'f', 10)) == (temp - 32) * 5/9, f"Your program returned wrong fahrenheit to celcius conversion"
        assert (session5.temp_converter(temp, 'C', 10)) == (temp * 9/5) + 32, f"Your program returned wrong celcius to fahrenheit conversion"

def test_speed_converter_named_arg_key():
    with pytest.raises(Exception):
            session5.time_it(session5.speed_converter, 100, dist='km', repetitons = 10), 'speed_converter must have named arguments - dist and time - indicating dist and time to be convertered'
    with pytest.raises(Exception):
            session5.time_it(session5.speed_converter, 100, time='min', repetitons = 10), 'speed_converter must have named arguments - dist and time - indicating dist and time to be convertered'
    with pytest.raises(Exception):
            session5.time_it(session5.speed_converter, 100, dis='km', tim='min', repetitons = 10), 'speed_converter must have named arguments - dist and time - indicating dist and time to be convertered'
    with pytest.raises(Exception):
            session5.time_it(session5.speed_converter, 100, 'km','min', repetitons = 10), 'speed_converter must have named arguments - dist and time - indicating dist and time to be convertered'

def test_speed_converter_named_arg_value():
    with pytest.raises(ValueError):
            session5.speed_converter(100, dist=4, time=3, repetitons = 10), "Dist can be km/m/ft/yrd, Time can be ms/s/min/hr/day"
    with pytest.raises(ValueError):
            session5.speed_converter(100, dist='a', time='b', repetitons = 10), "Dist can be km/m/ft/yrd, Time can be ms/s/min/hr/day"
    with pytest.raises(ValueError):
            session5.speed_converter(100, dist='km', time=3, repetitons = 10), "Dist can be km/m/ft/yrd, Time can be ms/s/min/hr/day"
    with pytest.raises(ValueError):
            session5.speed_converter(100, dist=4, time='hr', repetitons = 10), "Dist can be km/m/ft/yrd, Time can be ms/s/min/hr/day"

def test_speed_converter_positional_arg_value():
    with pytest.raises(ValueError):
            session5.speed_converter(0, dist='km', time='min', repetitons = 10), 'Speed must be greater than 0'
    with pytest.raises(ValueError):
            session5.speed_converter(-10, dist='km', time='min', repetitons = 10), 'Speed must be greater than 0'
    with pytest.raises(ValueError):
            session5.speed_converter('a', dist='km', time='min', repetitons = 10), 'Speed cannot be a string'

def test_speed_converter_calculation():
    for _ in range(50):
        speed = random.randint(1,100)
        assert (session5.speed_converter(speed, 'm', 's', 10)) == round(speed*1000/3600,2), f"Your program returned wrong km/hr to m/s conversion"
        assert (session5.speed_converter(speed, 'ft', 'min', 10)) == round(speed*3281/60,2), f"Your program returned wrong km/hr to ft/min conversion"

def test_print_named_arg_key():
    with pytest.raises(Exception):
            session5.time_it(session5.print, 1,2,3, sep='-', repetitons = 10), 'print must have named arguments - sep and end - indicating separator and end'
    with pytest.raises(Exception):
            session5.time_it(session5.print, 1,2,3, time=' ***\n', repetitons = 10), 'print must have named arguments - sep and end - indicating separator and end'
    with pytest.raises(Exception):
            session5.time_it(session5.print, 1,2,3, se='-', e=' ***\n', repetitons = 10), 'print must have named arguments - sep and end - indicating separator and end'
    with pytest.raises(Exception):
            session5.time_it(session5.print, 1,2,3, '-',' ***\n', repetitons = 10), 'print must have named arguments - sep and end - indicating separator and end'

def test_squared_power_list_named_arg_key():
    with pytest.raises(Exception):
            session5.time_it(session5.squared_power_list, 2, start=0, repetitons = 10), 'squared_power_list must have named arguments - start and end - indicating start and end of power'
    with pytest.raises(Exception):
            session5.time_it(session5.squared_power_list, 2, end=5, repetitons = 10), 'squared_power_list must have named arguments - start and end - indicating start and end of power'
    with pytest.raises(Exception):
            session5.time_it(session5.squared_power_list, 2, star=0, en=5, repetitons = 10), 'squared_power_list must have named arguments - start and end - indicating start and end of power'
    with pytest.raises(Exception):
            session5.time_it(session5.squared_power_list, 2, 0,5, repetitons = 10), 'squared_power_list must have named arguments - start and end - indicating start and end of power'

def test_squared_power_list_named_arg_value():
    with pytest.raises(ValueError):
            session5.squared_power_list(2, start='a', end='b', repetitons = 10), "Start and end must be numbers"
    with pytest.raises(ValueError):
            session5.squared_power_list(2, start='a', end=3, repetitons = 10), "Start and end must be numbers"
    with pytest.raises(ValueError):
            session5.squared_power_list(2, start=4, end='b', repetitons = 10), "Start and end must be numbers"

def test_squared_power_list_positional_arg_value():
    with pytest.raises(ValueError):
            session5.squared_power_list('a', start=0, end=5, repetitons = 10), 'Positional argument must be a number'

def test_squared_power_list_named_arg_start_less_than_end():
    with pytest.raises(ValueError):
            session5.squared_power_list(2, start=5, end=0, repetitons = 10), "Start must be less than end"
    with pytest.raises(ValueError):
            session5.squared_power_list(2, start=-5, end=-10, repetitons = 10), "Start must be less than end"

def test_squared_power_list_calculation():
    for _ in range(50):
        assert (session5.squared_power_list(2, start=2, end=5, repetitons=10)) == [4,8,16,32], f"Your program returned wrong list of power"
        assert (session5.squared_power_list(-4, start=-2, end=2, repetitons=10)) == [0.0625,-0.25,1,-4,16], f"Your program returned wrong list of power"
