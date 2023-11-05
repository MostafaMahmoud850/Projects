from pydub import AudioSegment
from pydub.playback import play
import datetime
from vonage import *

time = input("Enter the alarm: ")
alarm = AudioSegment.from_mp3("sounds/ttsMP3.com_VoiceText_2023-7-10_17_14_33.mp3")
play(alarm)

while True:
    timo = datetime.datetime.now()
    now = timo.strftime("%H:%M:%S")
    if now == time:
        # === play sound ===
        medcine = AudioSegment.from_mp3("sounds/ttsMP3.com_VoiceText_2023-7-10_17_14_33.mp3")
        play(medcine)
        # === send sms ===
        client = vonage.Client(key="a399bd4a", secret="ZT3xNcmxAsbT46R0")
        sms = vonage.Sms(client)
        responseData = sms.send_message(
        {
        "from": "My Robot",
        "to": "201090977262",
        "text": "Hello world",
        }
        )
        # === call phone ===
        client = vonage.Client(
        application_id="34a393ce-b233-460a-a304-ba44d8ad4b84",
        private_key="private.key",
        )
        response = client.voice.create_call({
        'to': [{'type': 'phone', 'number': "201090977262"}],
        'from': {'type': 'phone', 'number': "201090977262"},
        'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
        })

        print(response)

    elif now > time:
        break
