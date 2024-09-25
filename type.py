import time

def print_typing(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.7)

# Example usage
# typing_speed = 0.07  # Adjust this to control the typing speed
# text_to_print = "Hello, I am typing like a person."
# print_typing(text_to_print, typing_speed)
