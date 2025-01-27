import random
from collections import Counter

def roll_dice(num_simulations =  1_000_000, *sides):
    """
    Simulates rolling multiple dice a specified number of times and calculates 
    the probabilities of the resulting sums.
    
    Parameters:
        num_simulations (int): The number of times to simulate rolling the dice.
        *sides (int): A variable number of integers representing the number 
                      of sides on each die.
    """
    # Step 1: Simulate rolls
    # For each simulation, roll each die once and compute the sum of the rolls
    rolls = [
        sum(random.randint(1, side) for side in sides) 
        for _ in range(num_simulations)
    ]
    
    # Step 2: Count frequencies of each resulting sum
    frequencies = Counter(rolls)
    
    # Step 3: Calculate probabilities of each outcome
    total_rolls = sum(frequencies.values())  # Total number of simulations
    probabilities = {
        outcome: (count / total_rolls) * 100  # Convert count to percentage
        for outcome, count in sorted(frequencies.items())  # Sort outcomes for display
    }
    
    # Step 4: Print results in a formatted table
    print("OUTCOME    FREQUENCY (%)")
    for outcome, probability in probabilities.items():
        print(f"{outcome:<8} {probability:.2f}%")

# Example usage: Simulates rolling a 4-sided, 6-sided, 6-sided, 10-sided, and 20-sided die
roll_dice(1_000_000, 9, 12, 6, 10)
