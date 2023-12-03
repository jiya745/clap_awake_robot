import pyaudio
import sounddevice as sd
import numpy as np
threshold = 20
clap = False

def detect_clap(indata,frames,time,status):
    global clap
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm>threshold:
        print("clapped!")
        clap = True
        
def listen_for_clap():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)
    
    
def MainClapExe():
# if __name__ == "__main__":
    while True:
        listen_for_clap()
        if clap == True:
            break
        else:
            pass