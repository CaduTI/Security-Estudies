import os
import time

with open("hosts.txt", 'r') as host:
    dump = host.read()
    print(dump)

    for ip in dump:
        print("Verificando o IP:",ip)
        print("-" * 60)
        os.system('ping - n 4 {}'.format(ip))
        print("-" * 60)
        time.sleep(4)
