# Define the speed of light (C)
C: float = 3.0e8  # meters per second

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * c^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display the calculation
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# This makes sure main runs only when the file is executed directly
if __name__ == '__main__':
    main()
