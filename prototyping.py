import psutil

print(psutil.pids())
p = psutil.Process(8237)
print(p)
print(p.cwd())
print(p.terminal())