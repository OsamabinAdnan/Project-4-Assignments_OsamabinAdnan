import time  # Import the time module for sleep functionality

def countdown(t):
    """
    Function to create a countdown timer that displays minutes and seconds.
    
    Args:
        t (int): Total time in seconds to count down from
    """
    while t:  # Continue loop while t is greater than 0
        # Convert total seconds into minutes and remaining seconds
        # divmod(t, 60) returns a tuple of (t // 60, t % 60)
        # First value (mins) is the quotient (integer division)
        # Second value (secs) is the remainder (modulo operation)
        mins, secs = divmod(t, 60)
        
        # Format the time as MM:SS with leading zeros
        timer = '{:02d}:{:02d}'.format(mins, secs)
        
        # Print the timer on the same line (overwriting previous output)
        print(timer, end="\r")
        
        # Pause execution for 1 second
        time.sleep(1)
        
        # Decrease the total time by 1 second
        t -= 1
    
    # Print completion message when timer reaches zero
    print('Timer completed!')

# Get user input for the countdown duration
t = input("Enter the time in seconds: ")

# Convert the input string to integer and start the countdown
countdown(int(t))
