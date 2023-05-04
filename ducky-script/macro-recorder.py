from pynput import keyboard

filename = 'macro.txt'

duckscript_map = {
    "Key.enter": "ENTER",
    "Key.ctrl": "CTRL",
    "Key.shift": "SHIFT",
    "Key.alt": "ALT",
    "Key.cmd": "GUI",
    "Key.up": "UP",
    "Key.down": "DOWN",
    "Key.left": "LEFT",
    "Key.right": "RIGHT",
    "Key.delete": "DELETE",
    "Key.page_up": "PAGEUP",
    "Key.page_down": "PAGEDOWN",
    "Key.home": "HOME",
    "Key.esc": "ESC",
    "Key.backspace": "BACKSPACE",
    "Key.insert": "INSERT",
    "Key.tab": "TAB",
    "Key.end": "END",
    "Key.caps_lock": "CAPSLOCK",
    "Key.f1": "F1",
    "Key.f2": "F2",
    "Key.f3": "F3",
    "Key.f4": "F4",
    "Key.f5": "F5",
    "Key.f6": "F6",
    "Key.f7": "F7",
    "Key.f8": "F8",
    "Key.f9": "F9",
    "Key.f10": "F10",
    "Key.f11": "F11",
    "Key.f12": "F12",
    "Key.space": "SPACE",
}

def get_duckscript_command(key):
    if hasattr(key, 'char'):
        return "STRING {}".format(key.char)
    else:
        return duckscript_map.get(str(key), "")

keys_pressed = []

def on_press(key):
    if key == keyboard.Key.esc:
        return False
    else:
        command = get_duckscript_command(key)
        if command.startswith("STRING"):
            keys_pressed.append(command[7:])
        else:
            if keys_pressed:
                with open(filename, 'a') as f:
                    f.write("STRING {}\n".format("".join(keys_pressed)))
                keys_pressed.clear()
            with open(filename, 'a') as f:
                f.write("{}\n".format(command))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

