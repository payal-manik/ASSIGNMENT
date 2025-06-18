# write a function to convert celcius to farenheit

def cel_far(temp):
    result = (temp * (9/5)) + 32
    return  result


print("Temperature in farenheit =",cel_far(103.6))