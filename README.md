# Session 5 – Test Cases and code understanding
## time_it implementation using *args and **kwargs
### def time_it(fn, *args, repetitons= 1, **kwargs): 
The repetitons indicate the number of times the function has to be calculated.
## It has these functions defined:
1)  polygon_area : Calculates the area of polygon (sides can be 3 to 6). We have calculated the area of a regular polygon – having all the sides equal. The input is the side length and the number of sides. 
2)  temp_converter : Converts Celsius to Fahrenheit and Fahrenheit to Celsius. The input is the temperature and the unit of the temperature given.
3)  print : It prints the value of the input given in args with a specified separator and end.
4)  squared_power_list : It generates a list by calculating the power of the given number. For example, if 2 is the number we are calculating power of and with start = 0 and end = 5 we get the result as [1, 2, 4, 8, 16, 32].
5)  speed_converter : It converts the given speed in km/hr to different metrics. Here, distance can be km or m or ft or yrd and time can be ms or s or min or hr or day.
## Test Cases
1)  README exists
2)  README has at least 500 words
3)  Methods mentioned in README
4)  README file formatting 
5)  Code Indentation and spaces
6)  Function name should be in small letters
7)  All the above 5 functions used
8)  Repetitions in time_it function should be greater than or equal to 1
9)  fn in time_it should be any of the 5 functions used above 
10) polygon_area must have one positional argument
11) temp_converter must have one positional argument
12) speed_converter must have one positional argument
13) squared_power_list must have one positional argument
14) polygon_area must have one named argument
15) temp_converter must have one named argument
16) speed_converter must have two named arguments
17) squared_power_list must have two named arguments
18) print must have two named arguments
19) polygon_area must have sides as named argument
20) polygon_area named argument must be an integer between 3 and 6
21) polygon_area positional argument must be a number greater than 0
22) Testing polygon_area for equilateral triangle, square, regular pentagon and regular hexagon
23) temp_converter must have temp_given_in as named argument
24) temp_converter named argument must be a string ‘f’ or ‘F’ or ‘c’ or ‘C’
25) temp_converter positional argument must be a number greater than absolute zero temperature (0K or -273.15°C or -459.67°F)
26) Testing temp_converter for Celsius to Fahrenheit and Fahrenheit to Celsius conversion
27) speed_converter must have dist and time as named argument
28) speed_converter named argument must be a string (dist can be km or m or ft or yrd and time can be ms or s or min or hr or day)
29) speed_converter positional argument must be a number greater than 0
30) Testing speed_converter for speed conversion
31) print must have sep and end as named argument
32) squared_power_list must have start and end as named argument
33) squared_power_list named argument must be numbers
34) squared_power_list positional argument must be a number
35) Testing squared_power_list for list
36) squared_power_list start must be lesser than end
