from gtts import gTTS
import os
file=open("student.txt","r")
text=file.read().replace('\n'," ")
print(text)
language='en'
output=gTTS(text=text,lang=language,slow=False)
output.save("output.mp4")
file.close()
os.system("start output.mp4")