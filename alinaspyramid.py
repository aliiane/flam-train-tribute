# Ask the user for the height of the pyramid (up to 40 rows)
height = int(input("Enter the height of the pyramid (maximum 40): "))

# Define the letters in your name
name = "ALINA"
name_length = len(name)  # Length of the name "ALINA" is 5

# Loop to build each row of the pyramid
for i in range(height):
    # Pick a letter from your name based on the row number
    char = name[i % name_length]
    
    # Create a row with an odd number of the chosen letter
    symbols = char * (2 * i + 1)
    
    # Center the row to form the pyramid shape
    print(symbols.center(2 * height - 1))
