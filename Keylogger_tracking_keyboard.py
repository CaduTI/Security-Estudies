from pynput import mouse, keyboard
def tracking_input(key):
    key = str(key)
    print(key)


with keyboard.Listener(on_press=tracking_input) as key_list:
    key_list.join()