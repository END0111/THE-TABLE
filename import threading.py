import threading
import time
def ma_callback():
    print("Finished!")

def start_timer(second, callback):
    def my_sleep():
        print("Timer start!")
        for x in range(1, second + 1):
            print(f"{x} missisipi")
            time.sleep(1)
        callback()
    
    thread = threading.Thread(target=my_sleep)
    thread.start()


start_timer(5, ma_callback)