from pynput.mouse import Listener


def moving_cursor(x, y):
    print('position of current mouse {0}'.format((x, y)))

#Collecting the event till stoppef!!!!
with Listener(on_move=moving_cursor) as l:
    l.join()
