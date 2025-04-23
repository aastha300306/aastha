fahrenheit = [32, 45, 64, 72, 100, 212]
celsius = [(f - 32) * 5/9 for f in fahrenheit]

print(f"Temperatures in Fahrenheit: {fahrenheit}")
print(f"Temperatures in Celsius: {celsius}")