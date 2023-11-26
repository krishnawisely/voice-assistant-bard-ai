# Voice Assistant With Bard AI
### Abstract
In this project, Bard AI used as LLM(Large Language Model) to get answer for input and converting answer text as voice which is provided by Bard AI.
<br><br>To generate API key -> https://makersuite.google.com/app/apikey 
<br><br>API URL(POST) -> ```https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={YOUR_API_KEY}```
<br>Header -> ```"Content-Type": "application/json"```
<br>payload -> ```{"prompt": { "text" :"What is AI"}}```

### Libraries
- Voice to Text -> speech recognition library ```pip install SpeechRecognition```
- LLM AI -> Bard AI
- Text to Voice -> google text to speech(gTTS) library ```pip install gTTS```
- Play mp3 audio -> pygame library ```pip install pygame```

### Challenges Faced:
- Initialy tried pyaudio library for play audio but could not able to real file. So, i have swiched into pygame library.
- Intialy tried chatGPT but they are not provide free service. So, i have swiched into Bard AI.
