from google.cloud import texttospeech
from google.oauth2 import service_account
import pygame


credentials = service_account.Credentials.from_service_account_file('./whosthere-6385b11d40f1.json')
pygame.mixer.init()

# Instantiates a client
client = texttospeech.TextToSpeechClient(credentials=credentials)

def playGreeting(text):
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text="Welcome Home Siena!")

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-US',
                    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open('../bin/output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        pygame.mixer.music.load('../bin/output.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
