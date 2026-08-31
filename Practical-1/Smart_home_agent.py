from datetime import datetime

print("== SMART HOME AGENT ==")
print("Date:", datetime.now().strftime("%d-%m-%Y"))

temperature = float(input("Enter Temperature (°C): "))
light_intensity = int(input("Enter Light Intensity (0-100): "))
time = int(input("Enter Current Hour (0-23): "))

fan = "OFF"
light = "OFF"
heater = "OFF"

# Fan control
if temperature > 30:
    fan = "ON"
else:
    fan = "OFF"

# Light control
if (time >= 18 or time < 6) and light_intensity < 40:
    light = "ON"
else:
    light = "OFF"

# Heater control
if temperature < 18 and ((time >= 5 and time <= 8) or (time >= 20 and time <= 23)):
    heater = "ON"
else:
    heater = "OFF"

print("\n== DEVICE STATUS ==")

print("Date:", datetime.now().strftime("%d-%m-%Y"))
print("Fan:", fan)
print("Light:", light)
print("Heater:", heater)
