import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar nuestro microfono y ddevolder el audio como texto

def transformar_audio_en_texto():

    # almacenar recongnizer en variable
    r = sr.Recognizer()

    # configurar el mic
    with sr.Microphone() as origen:
        #tiempo d espera a que hables
        r.pause_threshold = 0.8

        #avisar que esta escuchando
        print('Ya puedes hablar')

        #variable de la escucha en AUDIO
        audio = r.listen(origen)

    #manejo de errores

        try:
            #buscar en google la escucha
            pedido = r.recognize_google(audio, language='es-ar')

            #prueba de q pudo entender
            print('Dijiste: ' + pedido)
            return pedido 
        except sr.UnknownValueError:
            #prueba de q no comprendio el audio
            print('Uia, no entendi')

            #devolver error
            return 'Sigo esperando'
        
        #si no puede resolver el pedido
        except sr.RequestError:
            #prueba de q no puede cumplir lo pedido
            print('No hay respuesta para eso')

            #devolver error
            return 'Sigo esperando'
        #error inesperado anda a saber q
        except:
            #prueba fallo algo q no sabemos
            print('Algo salio mal, muy mal')

            #devolver error
            return 'Sigo esperando'

#funcion para que el asistente hable de vuelta :D
#esta es la id de la voz en windows pero si no esta no se cual usara (tenia la voz en ingles yo)
idvoz = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

def hablar(mensaje):
    
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', idvoz)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# informar el dia de la semana
def pedir_dia():
    dia = datetime.date.today()
    print(dia)

    #crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #hay q hacer un diccionario por que datetime te dice los dias de la semana como indice 0 es lunes
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# informal la hora real
def pedir_hora():
    
    #crear una var con la hora
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} horas con {hora.minute} minutos, pero el tiempo es relativo'
    print (hora)
    
    #decir la hora en voz
    hablar(hora)

#ponerle un saludo inicial
def saludo_inicial():

    #crear variable con datos de la hora actual
    hora = datetime.datetime.now()
    if hora.hour > 18 or hora.hour < 6:
        momento = 'Buenas noches'
    elif 6 >= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    #decir saludo
    hablar(f'Hola {momento} soy Marta y seré tu asistente personal, ¿en que te puedo ayudar?')

# funcion central del asistente
def pedir_cosas():

    #iniciar con el saludito
    saludo_inicial()

    #variable de corte ATENTI
    comenzar = True

    while comenzar:
        #prender el mic

        pedido = transformar_audio_en_texto().lower()

        #aca se vienen todos los pedido y lo sabroso de la funcionalidad
        if 'youtube' in pedido:
            hablar('A la orden, abriendo YouTube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'Márta' in pedido:
            hablar('Si?')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Abriendo navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            #aca limpias el pedido para que quede solo lo que se tiene que buscar (sino buscaria la frase entera)
            pedido = pedido.replace('busca en wikipedia','')
            #poner wiki en español
            wikipedia.set_lang('es')
            #si no le podes la sentencia a 1, te lee tooooooda la pagina y no para jaja
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f'Wikipedia dice lo siguiente, cuchá:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            #lo mismo que con Wikipedia, para que busque el objetivo
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            continue
        elif 'reproducir' in pedido:
            hablar ('Enseguida!')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precios de las acciones' in pedido:
            #esto es nomas para usar yfinances
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon' : 'AMZN',
                       'google' : 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada  = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion}es de {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue
        elif 'gracias' in pedido:
            hablar('De nada, sigo atenta')
            continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar por hoy, chupate un limón')
            break

pedir_cosas()