# Dictionary storing gravity multipliers for different planets relative to Earth's gravity
# These values represent how much Earth weight should be multiplied by to get weight on that planet
PLANETARY_GRAVITY = {
    "mercury": 0.376,
    "venus": 0.889,
    "mars": 0.378,
    "jupiter": 2.36,
    "saturn": 1.081,
    "uranus": 0.815,
    "neptune": 1.14
}

def get_user_weight():
    """
    Get and validate user's weight input
    Returns:
        float: Valid positive weight in kilograms
    Raises:
        ValueError: If input cannot be converted to float
    """
    while True:
        try:
            # Convert string input to float and validate
            weight = float(input("Enter your weight on earth (kg): "))
            if weight <= 0:
                print("Weight must be a positive number.")
                continue
            return weight
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_planet_name():
    """
    Get and validate planet name input
    Returns:
        str: Valid planet name in lowercase
    """
    # Create comma-separated list of valid planet names
    valid_planets = ", ".join(PLANETARY_GRAVITY.keys())
    while True:
        # Get input, remove whitespace, convert to lowercase
        planet = input(f"Enter the planet name ({valid_planets}): ").strip().lower()
        if planet in PLANETARY_GRAVITY:
            return planet
        print(f"Invalid planet name. Please choose from: {valid_planets}")

def calculate_planetary_weight(earth_weight, planet):
    """
    Calculate weight on specified planet
    Args:
        earth_weight (float): Weight on Earth in kg
        planet (str): Name of target planet
    Returns:
        float: Weight on specified planet in kg
    """
    return earth_weight * PLANETARY_GRAVITY[planet]

def main():
    """
    Main program function that:
    1. Displays welcome message
    2. Gets user input for weight and planet
    3. Calculates new weight
    4. Displays formatted result
    """
    # Program header
    print("Planetary Weight Calculator")
    print("-" * 25)

    # Get user inputs with validation
    earth_weight = get_user_weight()
    planet = get_planet_name()

    # Calculate weight on selected planet and display formatted result
    planet_weight = calculate_planetary_weight(earth_weight, planet)
    print(f"\nYour weight of {earth_weight:.2f}kg on Earth")
    print(f"would be {planet_weight:.2f}kg on {planet.title()}\n")

# Standard Python idiom to ensure main() only runs if file is executed directly
if __name__ == "__main__":
    main()

