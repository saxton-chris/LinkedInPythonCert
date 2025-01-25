import time

def schedule_function(execution_time, func, *args):
    """
    Schedules a function to run at a specific timestamp.

    Parameters:
    execution_time (float or int): The timestamp (in seconds since the epoch) at which to execute the function.
    func (callable): The function to be executed.
    *args: Additional arguments to pass to the function when it is executed.

    Raises:
    ValueError: If execution_time is not a float or int, or if it's a negative value.
    """
    # Check if the execution_time is a valid float or int
    if not isinstance(execution_time, (float, int)):
        raise ValueError("execution_time must be a valid float or int representing a timestamp.")
    
    # Ensure the execution_time is non-negative
    if execution_time < 0:
        raise ValueError("execution_time must be a non-negative timestamp.")
    
    # Print a message indicating when the function is scheduled to run
    print(f"{func.__name__}() is scheduled for {time.ctime(execution_time)}")  
    
    # Calculate the delay time in seconds
    delay = execution_time - time.time()

    # Check if the provided function is callable
    if callable(func):
        # If the delay is 0 or negative, execute the function immediately
        if delay <= 0:
            func(*args)
        else:
            # Otherwise, wait for the specified delay and then execute the function
            time.sleep(delay)
            func(*args)

# Example usage:
# Schedule the 'print' function to run 60 seconds from now with the argument "Howdy!"
schedule_function(time.time() + 10, print, "Howdy!")
