def get_city_year(p0, perc, delta, p):
    # Convert percentage to decimal
    perc = perc / 100.0
    
    # Initialize years counter
    years = 0

    # Loop until the population reaches the target
    while p0 < p:
        # Calculate the new population
        p0 = p0 + (p0 * perc) + delta
        
        # Increment the year count
        years += 1
        
        # Check if the population is not increasing enough to reach the target
        if delta <= 0 and p0 <= p0 * (1 + perc):
            return -1
    
    # Return the total years taken to reach or exceed target population
    return years

# Test cases
print(get_city_year(1000, 2, 50, 1200))       # Expected output: 3
print(get_city_year(1000, 2, -50, 5000))      # Expected output: -1
print(get_city_year(1500, 5, 100, 5000))      # Expected output: 15
print(get_city_year(1500000, 2.5, 10000, 2000000))  # Expected output: 10
