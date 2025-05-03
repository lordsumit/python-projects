import time 

# Take time input from user
start = int(input("Enter the time from where the countdown will start: "))

# Make the loop which will work on it 
print("----\nCountdown begins-----")
while start > 0:
    print(start)
    time.sleep(2)
    start -= 1

print("Countdown complete")