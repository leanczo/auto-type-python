from pynput.keyboard import Key, Controller
import time

keyboard  = Controller()
time.sleep(5)

words = ["Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."]

for x in range(len(words)):
    for y in words[x]:
        keyboard.press(y)
        keyboard.release(y)
        time.sleep(0.02)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
