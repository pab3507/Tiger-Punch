from flask import Flask, render_template
from tiger_punch import *
app = Flask(__name__)

@app.route('/')
def main():
    global hub
    try:
        hub = libmyo.Hub()
    except MemoryError:
        print("Myo Hub could not be created. Make sure Myo Connect is running.")
        return
    hub.set_locking_policy(libmyo.LockingPolicy.none)
    listener=Listener()
    hub.run(1000, listener)

    return render_template("home.html",synced=listener.is_synced())


@app.route('/play')
def play():
    global hub
    try:
        hub = libmyo.Hub()
    except MemoryError:
        print("Myo Hub could not be created. Make sure Myo Connect is running.")
        return
    hub.set_locking_policy(libmyo.LockingPolicy.none)
    listener=Listener()
    hub.run(1000, listener)

    return render_template("play.html", listen=listener )


if __name__ == '__main__':
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nQuitting ...")
    finally:
        print("Shutting down hub...")
        hub.shutdown()