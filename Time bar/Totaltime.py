import time

# Define the total number of iterations in your loop
total_iterations = 1000

# Iterate over your loop
for i in range(total_iterations, 0, -1):
    # Print the progress bar
    print(f"\rCountdown: {i}/{total_iterations}", end='', flush=True)
    
    # Simulate some work being done
    time.sleep(0.01)

print("\nCountdown complete!")
