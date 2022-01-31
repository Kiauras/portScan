import socket
import ipaddress
import socket
from queue import Queue
import threading

print()
address = input('IP or IP range: ')
port = int(input('Port range start (From 1 to 65 000, max range not recommended): '))
port2 = int(input('Port range end: '))

def scanner(port):

    net4 = ipaddress.ip_network(address)
    for x in net4.hosts():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1) # adjust timeout so the script works faster
        result = s.connect_ex((str(x), port)) # keiciam ipaddr i str
        if result == 0:
            print(f'\n{x} Port: {port} is open!')
            s.close()
        else:
            s.close() 
            print(f'\n{x} Port: {port} is closed!') # for testing

# multi threadding 
def threader():
    while True:
        worker = q.get()
        scanner(worker)
        q.task_done()

q = Queue()
for x in range(1): # 100 is how many workers
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(port, port2 +1):
    q.put(worker)

q.join()
print('Finished')



    


    






    
