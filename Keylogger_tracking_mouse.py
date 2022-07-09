
from pynput import mouse, keyboard
import re





def tracking_move_mouse(x, y):
    print('Mouse posicionado na posição: {},{}'.format(x, y))


def tracking_scroll_mouse(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


def tracking_click_mouse(x, y, button, click):
    print('{0} no {1}'.format('Clicked' if click else 'Not Clicked', (x, y)))


with mouse.Listener(on_move=tracking_move_mouse, on_click=tracking_click_mouse, on_scroll=tracking_scroll_mouse) as mouse_list:
    mouse_list.join()


#if __name__ == '__main__':

