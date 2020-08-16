
import math
from timeit import default_timer as timer

def time_it(fn, *args, repetitons= 1, **kwargs):
    if(fn not in (temp_converter, polygon_area, squared_power_list, print, speed_converter)):
        raise ValueError("First positional argument must be function name - polygon_area/temp_converter/speed_converter/squared_power_list/print")
    if(repetitons <= 0):
        raise ValueError("Number of repetitons must be greater than 0")
    if(type(repetitons) != int):
        raise ValueError("repetitons should be an integer")
    if(fn==polygon_area or fn==temp_converter or fn==squared_power_list or fn==speed_converter):
        if(len(args) > 1):
            raise Exception("polygon_area, temp_converter, squared_power_list, speed_converter must have only one positional argument")
    if(fn==polygon_area or fn==temp_converter):
        if(len(kwargs) > 1):
            raise Exception("polygon_area and temp_converter must have only one named argument")
    if(fn==squared_power_list or fn==speed_converter or fn==print):
        if(len(kwargs) > 2):
            raise Exception("squared_power_list and print and speed_converter must have only two named arguments")
    if(fn==polygon_area):
        starttime=timer()
        if('sides' not in kwargs.keys()):
            raise Exception("polygon_area must have named argument - sides - indicating number of sides")
        area = polygon_area(*args, kwargs['sides'], repetitons)
        endtime = timer()
        avgtime = (endtime-starttime)/repetitons
    if(fn==temp_converter):
        starttime=timer()
        if('temp_given_in' not in kwargs.keys()):
            raise Exception("temp_converter must have named argument - temp_given_in - indicating Fahrenheit or Celcius")
        temp = temp_converter(*args, kwargs['temp_given_in'], repetitions)
        endtime = timer()
        avgtime = (endtime-starttime)/repetitons
    if (fn==print):
        dict = kwargs        
        if('sep' not in dict.keys() or 'end' not in dict.keys()):
            raise Exception("print must have named arguments - sep and end - indicating separator and end")
        sep = dict.get("sep")
        end = dict.get("end")
        starttime = timer()
        val_print = print(*args,sep=sep,end=end,rep=repetitons)
        endtime = timer()
        avgtime = (endtime-starttime)/repetitons
    if (fn==squared_power_list):
        dict = kwargs
        if('start' not in dict.keys() or 'end' not in dict.keys()):
            raise Exception("print must have named arguments - start and end - indicating start and end")
        start = dict.get("start")
        end = dict.get("end")
        starttime = timer()
        sq_list = squared_list(*args,start,end,repetitons)
        endtime = timer()
        avgtime = (endtime-starttime)/repetitons
    if (fn==speed_converter):
        starttime = timer()
        if('dist' not in kwargs.keys() or 'time' not in kwargs.keys()):
            raise Exception("print must have named arguments - dist and time - indicating dist and time")
        speed_conv = speed_converter(*args,kwargs['dist'],kwargs['time'],repetitons)
        endtime = timer()
        avgtime = (endtime-starttime)/repetitons
    return avgtime

def polygon_area(side_len, num_sides, repetitons):
    if(type(side_len) is str):
        raise ValueError("Input side_len as a number")
    if(num_sides not in (3,4,5,6)):
        raise ValueError("Supports area calculation upto hexagon - sides must be between 3 and 6")
    if(side_len <= 0):
        raise ValueError("Side length must be greater than 0")
    if(num_sides == 3):
        for i in range(repetitons):
            area = (math.sqrt(3)/4) * pow(side_len,2) #area of equilateral triangle
    if(num_sides == 4):
        for i in range(repetitons):
            area = side_len * side_len #area of square
    if(num_sides == 5):
        for i in range(repetitons):
            area = 1/4 * math.sqrt(5*(5+(2*math.sqrt(5)))) * pow(side_len,2) #area of regular pentagon
    if(num_sides == 6):
        for i in range(repetitons):
            area = (3 * math.sqrt(3)/2) * pow(side_len,2) #area of regular hexagon
    return area

def temp_converter(temp, temp_given_in, repetitons):
    if(type(temp_given_in) is not str):
        raise ValueError("Input 'c'/'C'/'f'/'F'")
    if(type(temp) is str):
        raise ValueError("Input temp as a number")
    if(temp_given_in.lower() not in ('f','c')):
        raise ValueError("Supports conversion of Celcius to Fahrenheit and Fahrenheit to Celcius - Input 'c'/'C'/'f'/'F'")
    if((temp_given_in.lower() == 'c' and temp < -273.15) or ((temp_given_in.lower() == 'f' and temp < -459.67))):
        raise ValueError("Temerature cannot be less than absolute 0 (0K or -273.15°C or -459.67°F)")
    if(temp_given_in.lower() == 'f'):
        for i in range(repetitons):
            temparature = (temp - 32) * 5/9 #Fahrenheit to Celcius
    if(temp_given_in.lower() == 'c'):
        for i in range(repetitons):
            temparature = (temp * 9/5) + 32 #Celcius to Fahrenheit
    return temparature

def print(*args,sep,end,rep=1):
    sep=sep
    end=end
    for i in range(rep):
        print(*args,sep=sep,end=end)

def squared_power_list(num,start,end,repetitons):
    if(type(num) == str):
        raise ValueError("Input should be Number")
    if(type(start) == str or type(end) == str):
        raise ValueError("Start and end must be numbers")
    if (start>end):
        raise ValueError("Start has to be lesser than End")  
    for i in range(repetitons):
        temp=[lambda a,x=x: a**x for x in range(start,end+1)]
        sqrs=[c(num) for c in temp]
        temp.clear()
    return sqrs

def speed_converter(value,dist,time,repetitons):
    if(type(value) == str):
        raise ValueError("Input should be Number")
    if(value <= 0):
        raise ValueError("Speed must be greater than 0")
    distance = {"km":1,"m":1000,"ft":3281,"yrd":1094}
    time_dict = {"hr":1,"min":60,"s":3600,"ms":3.6e+6, "day":0.042}
    dist = distance.get(dist)
    time = time_dict.get(time)
    if (dist==None or time == None):
        raise ValueError ("Dist can be km/m/ft/yrd, Time can be ms/s/min/hr/day")
    for i in range(repetitons):
        conv_speed=round((value*(dist/time)),2)
    return conv_speed
