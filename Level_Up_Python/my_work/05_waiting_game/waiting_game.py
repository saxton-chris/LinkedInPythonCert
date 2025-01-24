import random  # Importing the random module to generate a random target wait time
import time    # Importing the time module to measure elapsed time

def waiting_game():
    # Generate a random wait time between 2 and 4 seconds
    wait_time = random.randint(2, 4)

    # Inform the user of the target wait time
    print(f"Your target time is {wait_time} seconds")
    print("---Press Enter---")
    
    # Wait for the user to press Enter to start the timer
    input()
    
    # Record the start time using a high-precision timer
    start = time.perf_counter()

    # Prompt the user to wait for the target time and press Enter again
    print(f"\n...Press Enter again after {wait_time} seconds\n")
    input()  # Wait for the user to press Enter again
    
    # Calculate the elapsed time since the timer started
    elapsed = time.perf_counter() - start

    # Display the elapsed time to the user, formatted to 3 decimal places
    print(f"Elapsed time: {elapsed:.3f} seconds")

    # Compare the user's timing with the target time and provide feedback
    if wait_time == elapsed:
        print("Nailed it!!")  # Exact match
    elif wait_time < elapsed:
        # User was too slow, calculate the difference
        print(f"You pressed Enter {(elapsed - wait_time):.3f} seconds too slow")
    else:
        # User was too fast, calculate the difference
        print(f"You pressed Enter {(wait_time - elapsed):.3f} seconds too fast")


# Ensure the game runs only when the script is executed directly
if __name__ == "__main__":
    waiting_game()
