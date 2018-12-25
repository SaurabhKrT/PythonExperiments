import os

results = []
for f in os.listdir('folder'):
        if f.endswith('.pdf'):
            results.append(f)
print results
