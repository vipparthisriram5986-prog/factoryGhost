
import random
import time
import csv

print("=== FACTORY GHOST ===")
print("Industrial Motor Simulator\n")

with open("motor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Reading", "Temperature_C",
        "Vibration_mm_s", "Current_A", "Status"
    ])

    for reading in range(1, 11):
        temperature = random.uniform(35, 55)
        vibration = random.uniform(1, 3)
        current = random.uniform(2, 4)

        if reading >= 7:
            temperature += 35
            vibration += 3.5
            current += 1.5

        if temperature > 75 or vibration > 5:
            status = "WARNING"
        else:
            status = "NORMAL"

        print(
            f"Reading {reading}: "
            f"{temperature:.1f} C, "
            f"{vibration:.1f} mm/s, "
            f"{current:.1f} A - {status}"
        )

        writer.writerow([
            reading,
            round(temperature, 1),
            round(vibration, 1),
            round(current, 1),
            status
        ])

        time.sleep(1)

print("\nSimulation complete!")
print("Saved readings to motor_data.csv")
