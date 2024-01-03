# Priority Queue example
import queue, time, random

def get_pair(i):
    return (0-random.randint(1, 10), random.randint(0, RANGE))

RANGE = 10_000_000

simple_prio = queue.PriorityQueue()
print("Priority Enqueued 1:1, 2:1, 3:1, 4:5, 5:9")
simple_prio.put((-1, 1))
simple_prio.put((-1, 2))
simple_prio.put((-1, 3))
simple_prio.put((-5, 4))
simple_prio.put((-9, 5))

# Dequeue order check
test_out = []
while not simple_prio.empty():
    test_out.append(simple_prio.get_nowait()[1])
print("Simple Priority Queue Dequeued:", ' '.join(map(str, test_out)))

# Speed test
pairs = [get_pair(i) for i in range(RANGE)]
start_time = time.time()
for pair in pairs:
    simple_prio.put(pair)
elapsed = time.time() - start_time
print("Simple priority queue enqueue time:", elapsed)

count = 0
start_time = time.time()
while not simple_prio.empty():
    simple_prio.get_nowait()
    count += 1
elapsed = time.time() - start_time
print("Simple priority queue dequeued items:", count)
print("Simple priority queue dequeue time:", elapsed)
print("-----")