def untrue():
    print('Incorrect command!!! Try again.')
#---------------------------------------------------
def metric_l():
    print('1] Kilometers to Meters')
    print('2] Kilometers to Centimeters')
    print('3] Kilometers to Millimeters')
    print('4] Meters to Kilometers')
    print('5] Meters to Centimeters')
    print('6] Meters to Millimeters')
    print('7] Centimeters to Kilometers')
    print('8] Centimeters to Meters')
    print('9] Centimeters to Millimeters')
    print('10] Millimeters to Kilometers')
    print('11] Millimeters to Meters')
    print('12] Millimeters to Centimeters')
    print('13] Back')
    command=int(input('The number of the command is '))
    if command==13:
        length()
    else:
        value=float(input('The value to convert is '))
        if command==1:
            print(f'{value} km = {value*1000} m.')
        elif command==2:
            print(f'{value} km = {value*1000*100} cm.')
        elif command==3:
            print(f'{value} km = {value*1000**2} mm.')
        elif command==4:
            print(f'{value} m = {value/1000} km.')
        elif command==5:
            print(f'{value} m = {value*100} cm.')
        elif command==6:
            print(f'{value} m = {value*1000} mm.')
        elif command==7:
            print(f'{value} cm = {value/10**5} km.')
        elif command==8:
            print(f'{value} cm = {value/100} m.')
        elif command==9:
            print(f'{value} cm = {value*10} mm.')
        elif command==10:
            print(f'{value} mm = {value/10**6} km.')
        elif command==11:
            print(f'{value} mm = {value/1000} m.')
        elif command==12:
            print(f'{value} mm = {value/10} cm.')
        else:
            untrue()
            metric_l()
#---------------------------------------------------
def us_cus_l():
    print('1] Miles to Yards')
    print('2] Miles to Feet')
    print('3] Miles to Inches')
    print('4] Yards to Miles')
    print('5] Yards to Feet')
    print('6] Yards to Inches')
    print('7] Feet to Miles')
    print('8] Feet to Yards')
    print('9] Feet to Inches')
    print('10] Inches to Miles')
    print('11] Inches to Yards')
    print('12] Inches to Feet')
    print('13] Back')
    command=int(input('The number of the command is '))
    if command==13:
        length()
    else:
        value=float(input('The value to convert is '))
        if command==1:
            print(f'{value} mi = {value*1760} yd.')
        elif command==2:
            print(f'{value} mi = {value*1760*3} ft.')
        elif command==3:
            print(f'{value} mi = {value*1760*36} in.')
        elif command==4:
            print(f'{value} yd = {value/1760} mi.')
        elif command==5:
            print(f'{value} yd = {value*3} ft.')
        elif command==6:
            print(f'{value} yd = {value*36} in.')
        elif command==7:
            print(f'{value} ft = {value/1760/3} mi.')
        elif command==8:
            print(f'{value} ft = {value/3} yd.')
        elif command==9:
            print(f'{value} ft = {value*12} in.')
        elif command==10:
            print(f'{value} in = {value/1760/36} mi.')
        elif command==11:
            print(f'{value} in = {value/36} yd.')
        elif command==12:
            print(f'{value} in = {value/12} ft.')
        else:
            untrue()
            us_cus_l()
#---------------------------------------------------
def metric_w():
    print('1] Tonne to Kilogram')
    print('2] Tonne to Gram')
    print('3] Tonne to Milligram')
    print('4] Kilogram to Tonne')
    print('5] Kilogram to Gram')
    print('6] Kilogram to Milligram')
    print('7] Gram to Tonne')
    print('8] Gram to Kilogram')
    print('9] Gram to Milligram')
    print('10] Milligram to Tonne')
    print('11] Milligram to Kilogram')
    print('12] Milligram to Gram')
    print('13] Back')
    command=int(input('The number of the command is '))
    if command==13:
        weight()
    else:
        value=float(input('The value to convert is '))
        if command==1:
            print(f'{value} t = {value*1000} kg')
        elif command==2:
            print(f'{value} t = {value*10**6} g')
        elif command==3:
            print(f'{value} t = {value*10**9} mg')
        elif command==4:
            print(f'{value} kg = {value/1000} t')
        elif command==5:
            print(f'{value} kg = {value*1000} g')
        elif command==6:
            print(f'{value} kg = {value*10**6} mg')
        elif command==7:
            print(f'{value} g = {value/10**6} t')
        elif command==8:
            print(f'{value} g = {value/1000} kg')
        elif command==9:
            print(f'{value} g = {value*1000} mg')
        elif command==10:
            print(f'{value} mg = {value/10**9} t')
        elif command==11:
            print(f'{value} mg = {value/10**6} kg')
        elif command==12:
            print(f'{value} mg = {value/1000} g')
        else:
            untrue()
            metric_w()
#---------------------------------------------------
def us_cus_w():
    print('1] Tons to Pounds')
    print('2] Tons to Ounces')
    print('3] Pounds to Tons')
    print('4] Pounds to Ounces')
    print('5] Ounces to Tons')
    print('6] Ounces to Pounds')
    print('7] Back')
    command=int(input('The number of the command is '))
    if command==7:
        weight()
    else:
        value=float(input('The value to convert is '))
        if command==1:
            print(f'{value} t = {value*2000} lb')
        elif command==2:
            print(f'{value} t = {value*2000*16} oz')
        elif command==3:
            print(f'{value} lb = {value/2000} t')
        elif command==4:
            print(f'{value} lb = {value*16} oz')
        elif command==5:
            print(f'{value} oz = {value/32000} t')
        elif command==6:
            print(f'{value} oz = {value/16} lb')
        else:
            untrue()
            us_cus_w()
#---------------------------------------------------
def metric_v():
    print('1] Cubic meter to Liter')
    print('2] Cubic meter to Milliliter')
    print('3] Liter to Cubic meter')
    print('4] Liter to Milliliter')
    print('5] Milliliter to Cubic meter')
    print('6] Milliliter to Liter')
    print('7] Back')
    command=int(input('The number of the command is '))
    if command==7:
        volume()
    else:
        value=float(input('The value to convert is '))
        if command==1:
            print(f'{value} m3 = {value*1000} l')
        elif command==2:
            print(f'{value} m3 = {value*10**6} ml')
        elif command==3:
            print(f'{value} l = {value/1000} m3')
        elif command==4:
            print(f'{value} l = {value*1000} ml')
        elif command==5:
            print(f'{value} ml = {value/10**6} m3')
        elif command==6:
            print(f'{value} ml = {value/1000} l')
        else:
            untrue()
            metric_v()
#---------------------------------------------------
def us_cus_v():
    print('1] Gallon to Quart')
    print('2] Gallon to Pint')
    print('3] Gallon to Cup')
    print('4] Gallon to Fluid ounce')
    print('5] Quart to Gallon')
    print('6] Quart to Pint')
    print('7] Quart to Cup')
    print('8] Quart to Fluid ounce')
    print('9] Pint to Gallon')
    print('10] Pint to Quart')
    print('11] Pint to Cup')
    print('12] Pint to Fluid ounce')
    print('13] Cup to Gallon')
    print('14] Cup to Quart')
    print('15] Cup to Pint')
    print('16] Cup to Fluid ounce')
    print('17] Fluid ounce to Gallon')
    print('18] Fluid ounce to Quart')
    print('19] Fluid ounce to Pint')
    print('20] Fluid ounce to Cup')
    print('21] Back')
    command=int(input('The number of the command is '))
    if command==21:
        volume()
    else:
        value=float(input('The value to convert is '))
        if command==1:
            print(f'{value} gallon = {value*4} quart')
        elif command==2:
            print(f'{value} gallon = {value*8} pint')
        elif command==3:
            print(f'{value} gallon = {value*16} cup')
        elif command==4:
            print(f'{value} gallon = {value*128} fl oz')
        elif command==5:
            print(f'{value} quart = {value/4} gallon')
        elif command==6:
            print(f'{value} quart = {value*2} pint')
        elif command==7:
            print(f'{value} quart = {value*4} cup')
        elif command==8:
            print(f'{value} quart = {value*32} fl oz')
        elif command==9:
            print(f'{value} pint = {value/8} gallon')
        elif command==10:
            print(f'{value} pint = {value/2} quart')
        elif command==11:
            print(f'{value} pint = {value*2} cup')
        elif command==12:
            print(f'{value} pint = {value*16} fl oz')
        elif command==13:
            print(f'{value} cup = {value/16} gallon')
        elif command==14:
            print(f'{value} cup = {value/4} quart')
        elif command==15:
            print(f'{value} cup = {value/2} pint')
        elif command==16:
            print(f'{value} cup = {value*8} fl oz')
        elif command==17:
            print(f'{value} fl oz = {value/128} gallon')
        elif command==18:
            print(f'{value} fl oz = {value/32} quart')
        elif command==19:
            print(f'{value} fl oz = {value/16} pint')
        elif command==20:
            print(f'{value} fl oz = {value/8} cup')
        else:
            untrue()
            us_cus_v()
#---------------------------------------------------
def length():
    print('1] Metric System')
    print('2] US Customary System')
    print('3] Inch to Centimeter')
    print('4] Feet to Meters')
    print('5] Miles to Kilometers')
    print('6] Back')
    command=int(input('The number of the command is '))
    if command==6:
        return
    if command==1:
        metric_l()
        return
    elif command==2:
        us_cus_l()
        return
    value=float(input('The value to convert is '))
    if command==3:
        print(f'{value} in = {value*2.54} cm')
    elif command==4:
        print(f'{value} ft = {value*0.3048} m') 
    elif command==5:
        print(f'{value} mi = {value*1.60934} km')     
    else:
        untrue()
        length()
#---------------------------------------------------
def weight():
    print('1] Metric System')
    print('2] US Customary System')
    print('3] Ounce to Gram')
    print('4] Pounds to Kilograms')
    print('5] Back')
    command=int(input('The number of the command is '))
    if command==5:
        return
    if command==1:
        metric_w()
        return
    elif command==2:
        us_cus_w()
        return
    value=float(input('The value to convert is '))
    if command==3:
        print(f'{value} oz = {value*28.3495} g')
    elif command==4:
        print(f'{value} lb = {value*0.45359237} kg')
    else:
        untrue()
        weight()
#---------------------------------------------------
def temperature():
    print('1] Celsius to Fahrenheit')
    print('2] Celsius to Kelvin')
    print('3] Celsius to Rankine')
    print('4] Fahrenheit to Celsius')
    print('5] Fahrenheit to Kelvin')
    print('6] Fahrenheit to Rankine')
    print('7] Kelvin to Celsius')
    print('8] Kelvin to Fahrenheit')
    print('9] Kelvin to Rankine')
    print('10] Rankine to Celsius')
    print('11] Rankine to Fahrenheit')
    print('12] Rankine to Kelvin')
    print('13] Back')
    command=int(input('The number of the command is '))
    if command==13:
        return
    value=float(input('The value to convert is '))
    if command==1:
        print(f'{value} °C = {value*1.8+32} °F')
    elif command==2:
        print(f'{value} °C = {value+273.15} K')
    elif command==3:
        print(f'{value} °C = {value*1.8+491.67} °R')
    elif command==4:
        print(f'{value} °F = {(value-32)/1.8} °C')
    elif command==5:
        print(f'{value} °F = {(value-32)/1.8+273.15} K')
    elif command==6:
        print(f'{value} °F = {value+459.67} °R')
    elif command==7:
        print(f'{value} K = {value-273.15} °C')
    elif command==8:
        print(f'{value} K = {(value-273.15)*1.8+32} °F')
    elif command==9:
        print(f'{value} K = {(value-273.15)*1.8+491.67} °R')
    elif command==10:
        print(f'{value} °R = {(value-491.67)/1.8} °C')
    elif command==11:
        print(f'{value} °R = {value-459.67} °F')
    elif command==12:
        print(f'{value} °R = {(value-491.67)/1.8+273.15} K')
    else:
        untrue()
        temperature()
#---------------------------------------------------
def volume():
    print('1] Metric System')
    print('2] US Customary System')
    print('3] Gallons to Liters')
    print('4] Quarts to Liters')
    print('5] Pints to Milliliters')
    print('6] Fluid ounce to Milliliters')
    print('7] Back')
    command=int(input('The number of the command is '))
    if command==7:
        return
    if command==1:
        metric_v()
        return
    elif command==2:
        us_cus_v()
        return
    value=float(input('The value to convert is '))
    if command==3:
        print(f'{value} gallon = {value*3.78541} l')
    elif command==4:
        print(f'{value} quart = {value*0.946} l')
    elif command==5:
        print(f'{value} pint = {value*473} ml')
    elif command==6:
        print(f'{value} fl oz = {value*29.57} ml')
    else:
        untrue()
        volume()
#---------------------------------------------------
while True:
    print('=====Unit Converter=====')
    print('1] Length')
    print('2] Weight')
    print('3] Temperature')
    print('4] Volume')
    print('5] Exit')
    command=int(input('The number of the command is '))
    if command==1:
        length()
    elif command==2:
        weight()
    elif command==3:
        temperature()
    elif command==4:
        volume()
    elif command==5:
        break
    else:   
        untrue()
        continue