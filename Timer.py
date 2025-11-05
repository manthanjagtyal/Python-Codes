import time
import winsound
minutes = int(input("Enter minutes: "))
seconds = minutes * 60
for i in range(seconds, 0, -1):
    mins, secs = divmod(i, 60)
    print(f" Time Left: {mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
print("\nTime's up!")
for _ in range(10):
    winsound.Beep(1000, 600) 
    time.sleep(0.3)
