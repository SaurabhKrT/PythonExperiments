import os

results = []
for f in os.listdir('/home/saurabhtiwari/Documents/Analytics Book'):
        if f.endswith('.pdf'):
            results.append(f)
print results
