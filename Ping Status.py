from ping3 import ping, verbose_ping
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x, y = [], []
i = 0

server_input = input("Server:")

def get_ping():
    while True:
        return ping(server_input, unit= 'ms')

def limit_x_and_y(xlim, ylim):
    xlim = plt.xlim(left=max (0, i-30), right = i + 50)
    ylim = plt.ylim(top=max(0, 200), bottom=1)

def plot(i):
    server = get_ping()
    print(server)
    
    x.append(i)
    y.append(server)
    
    plt.cla()
    plt.plot(x, y)
    return limit_x_and_y(0, 1)
    
ani = FuncAnimation(plt.gcf(), plot, interval=300)
plt.tight_layout()
plt.show()
