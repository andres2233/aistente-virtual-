import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime 
import wikipedia
name = 'miguel ' 

engine = pyttsx3.init()   # con esto iniciamos lavoz
voices = engine.getProperty('voices')# aqui extraemos las voces que ha y
engine.setProperty('voice', voices[0].id)# aca podemos elegir la voz que queramos 
#engine.say('iniciando tomara unos segundos   ') # 2) aca le indicamos a la voz que decir a aapneas iniciar
engine.runAndWait()#3) le decimos que se ejecute 
# for i in voices: # con esto podemos ver la voces que existen y su idiomas 
#     print(i)

def talk (text):
    engine.say(text)
    engine.runAndWait()


listener  = sr.Recognizer() # aca esamos inicando la lectura d eaudio 
print("habla...")
def listen():
    try: 
        with sr.Microphone() as source:
            print("Speak Anything :")
            #audio = r.listen(source)
            voice =listener.listen(source)
            print('reconocinedo')
            rec = listener.recognize_google(voice)
            rec = rec.lower()

            if name in rec : 
                rec = rec.replace(name, '')#aqui hemos quitado el nombre ( osea que no repita su propio nombre )
                # talk(rec)
               # print(rec)
    except:
        pass
    return rec # el return es importante por que sin el run() no detectara lo que hemos dicho al llamar a alexa (name)

def run(): 
    rec =  listen()
    if 'busca' in rec : # esto es para cuando le decimos una palabra en espesifico el programa nos ejecutara ;ago en esepecificp    
        search = rec.replace('busca' , '') # aca hacemos lo mismo que con el nombrey borramos 
        talk('buscando' + search) # le indicamos que diga reproducinedo + lo quue hallamos dicho 
        pywhatkit.search(search)
    if 'hora'in rec: 
        hora = datetime.datetime.now().strftime('%I:%M %p') 
        talk('son las :'+ hora )
    elif 'que es'in rec :
        orden = rec.replace('busca', '' )
        info = wikipedia.summary(orden, 1)
        talk(info)
    

run()



    