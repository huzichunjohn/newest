from threading import Timer

def say_hello(name):
    print("hello "+name)

if __name__ == "__main__":
    timer = Timer(5, say_hello("world."))
    timer.start()
