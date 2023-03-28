from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.cognitiveservices.speech import SpeechRecognizer, SpeechConfig, SpeechSynthesizer 
import requests, uuid

KEY_TEXT_ANALYTICS = "6e1308f15f58491baee64f835be8348a"
ENDPOINT = "https://iandemolang.cognitiveservices.azure.com/"



KEY_SPEECH = "941df93c-aa89-4893-b5de-03e3da8ff867"
SPEECH_REGION= "westeurope"
def voz_a_texto():
    speech_config = SpeechConfig(KEY_SPEECH, region=SPEECH_REGION)
    # audio_config = AudioOutputConfig()
    cliente = SpeechRecognizer(speech_config=speech_config, language="es-ES")
    resultado = cliente.recognize_once_async().get()
    return resultado.text

def texto_a_voz(texto):
    speech_config = SpeechConfig(KEY_SPEECH, region=SPEECH_REGION)
    cliente = SpeechSynthesizer(speech_config=speech_config)
    cliente.speak_text(texto)

def authenticate_client():
    ta_credential = AzureKeyCredential(KEY_TEXT_ANALYTICS)
    text_analytics_client = TextAnalyticsClient(
    endpoint=ENDPOINT,
    credential=ta_credential)
    return text_analytics_client

cliente = authenticate_client()
texto = voz_a_texto()
opinion = cliente.analyze_sentiment([texto], language="es")[0]
print("Opinión general del documento: ", opinion.sentiment)

for oracion in opinion.sentences:
    print("\tOración: \t\"{}\"".format(oracion.text))
    respuesta = cliente.extract_key_phrases([texto], language="es")[0]
    print("Frases clave:")

for frase in respuesta.key_phrases:
    print(frase)
    entidades = cliente.recognize_entities([texto], language="es")[0]
    print("\nEntidades:")

for entidad in entidades.entities:
    print("{}".format(entidad.text))

