import threading, sys
print = lambda x: sys.stdout.write("{}\n".format(x))

cnt, num, limit = 0, 3, 10000

class AsyncCount(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.counter = 0
    def run(self):
        global cnt
        while self.counter < limit:
            self.counter += 1
            cnt += 1
        return

threads = [ AsyncCount() for n in range(num) ]
[ t.start() for t in threads ]
[ t.join() for t in threads ]
print("Expected: {}".format(num * limit))
print("Received: {}".format(cnt))

# Expected: 30000
# Received: 24573