import psutil
import fcntl
import sys
import termios

# print(psutil.pids())
# p = psutil.Process(8237)
# print(p)
# print(p.cwd())
# print(p.terminal())


pid=27769
with open('/proc/%s/fd/0' % pid, 'w') as fd:
    for char in "ls -la\n":
        fcntl.ioctl(fd, termios.TIOCSTI, char)