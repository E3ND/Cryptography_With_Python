# PlySimpleGUI bibliotec || pip install pysimplegui
import PySimpleGUI as sg

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 = 'zyxwvutsrqponmlkjihgfedcba'
key = 4

# Criptografar
def encrypt(message):
    message = message.lower()
    caracter = ''
    for slot in message:
        if slot == ' ':
            caracter += '0'
            
        elif slot == ',':
            caracter += '1'
        
        elif slot == '.':
            caracter += '2'

        elif slot == '?':
            caracter += '3'
         
        elif slot == 'ç':
            caracter += '4'
         
        elif slot == '!':
            caracter += '5'
         
        elif slot == 'ã':
            caracter += '6'
         
        elif slot == 'õ':
            caracter += '7'
         
        elif slot == 'é':
            caracter += '8'
         
        elif slot == 'á':
            caracter += '9'
         
        elif slot == 'ô':
            caracter += 'ᚠ'
         
        elif slot == 'â':
            caracter += 'ᚢ'

        elif slot == 'ê':
            caracter += 'ᚦ'
         
        else:   
            c_index = alphabet.index(slot)
            caracter += alphabet2[(c_index + key) % len(alphabet)]
    return caracter

# Desencriptografar
def decrypt(message):
    message = message.lower()
    caracter = ''
    for slot in message:
        if slot == '0':
            caracter += ' '
        
        elif slot == '1':
            caracter += ','

        elif slot == '2':
            caracter += '.'

        elif slot == '3':
            caracter += '?'

        elif slot == '4':
            caracter += 'ç'
         
        elif slot == '5':
            caracter += '!'
         
        elif slot == '6':
            caracter += 'ã'
         
        elif slot == '7':
            caracter += 'õ'
         
        elif slot == '8':
            caracter += 'é'
         
        elif slot == '9':
            caracter += 'á'
         
        elif slot == 'ᚠ':
            caracter += 'ô'

        elif slot == 'ᚢ':
            caracter += 'â'

        elif slot == 'ᚦ':
            caracter += 'ê'

        else:
            c_index = alphabet2.index(slot)
            caracter += alphabet[(c_index - key) % len(alphabet)]
    return caracter

# Interface
def interface():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Cifrar')],  
        [sg.Button('Decifrar')],  
    ]
    return sg.Window('Interface', layout=layout, finalize=True)


def criptografar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite a menssagem'),sg.Input(key='message')],
        [sg.Button('Voltar'), sg.Button('Enviar')],
        [sg.Output(size=(50,30))]
    ]
    return sg.Window('Criptografar', layout=layout, finalize=True)

def desencriptografar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite a menssagem'),sg.Input(key='message')],
        [sg.Button('Voltar'), sg.Button('Enviar')],
        [sg.Output(size=(50,30))]
    ]
    return sg.Window('Desencriptografar', layout=layout, finalize=True)

# Janelas iniciais
janela1, janela2, janela3 = interface(), None, None

# Loop  de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    # Ir para próxima janela
    if window == janela1 and event == 'Cifrar':
        janela1.hide()
        janela2 = criptografar()

    if window == janela1 and event == 'Decifrar':
        janela1.hide()
        janela3 = desencriptografar()

    if window == janela2 and event == 'Voltar':
        janela2.hide()            
        janela1.un_hide()  

    if window == janela3 and event == 'Voltar':
        janela3.hide()            
        janela1.un_hide()  

    if window == janela2 and event == 'Enviar':
        # Mandando para função
        print(encrypt(values['message']))

    if window == janela3 and event == 'Enviar':
        # Mandando para função
        print(decrypt(values['message']))