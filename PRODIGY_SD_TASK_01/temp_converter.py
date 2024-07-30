def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    value = float(value)
    
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value} Celsius is equal to {fahrenheit:.2f} Fahrenheit and {kelvin:.2f} Kelvin.")
        
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value} Fahrenheit is equal to {celsius:.2f} Celsius and {kelvin:.2f} Kelvin.")
        
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value} Kelvin is equal to {celsius:.2f} Celsius and {fahrenheit:.2f} Fahrenheit.")
        
    else:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    print("Temperature Conversion Program")
    temp = input("Enter the temperature value: ")
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    
    convert_temperature(temp, unit)

if __name__ == "__main__":
    main()
