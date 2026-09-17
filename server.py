import socket
import sounddevice as sd
import wavio 
import whisper

print("Loading whisper.....")
model = whisper.load_model("base")
print("model is loaded...")
sample_rate = 16000
Duration_sec = 8
Filename = "Bassant.wav"

def Record_to_wav():
    audio = sd.rec(int(Duration_sec * sample_rate),samplerate = sample_rate, channels= 1 , dtype="int16" )
    sd.wait()
    wavio.write(Filename,audio,sample_rate,sampwidth = 2)

def transcribe(Filename):
    result = model.transcribe(Filename)
    text = result["text"].strip().lower()
    print("You said: ",text)
    return text


server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(("0.0.0.0",5000))

print("UDP server is waiting....")

data,addr = server.recvfrom(1024)

print("client: ",data.decode())

print("client Address: ", addr )

server.sendto(b"Hello from UDP server",addr)

while True: 
    Record_to_wav()
    text = transcribe(Filename)
    server.sendto(text.encode(),addr)

server.close()