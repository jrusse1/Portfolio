import time
startTime = time.time()
timer = 60
for i in range(timer):
    print(timer)
    time.sleep(1)
    timer -= 1
endTime = time.time()

print(endTime - startTime)