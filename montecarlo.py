#coding: latin-1
import random

n_trials = 4000
n_hits = 0

for iter in range(n_trials):
    # Pick a random (x,y) value for the unit square.
    x,y = random.uniform(-1.0,1.0), random.uniform(-1.0,1.0)
    if x**2 + y**2 < 1.0:
        n_hits += 1

print "Estimated Pi:"
print 4.0 * n_hits / float(n_trials)
