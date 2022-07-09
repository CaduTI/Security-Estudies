import os

ping_input = input("Digite endereço em que deseja realizar o ping:")

os.system(f"ping -n 6 {ping_input}")