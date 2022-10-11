# PlySimpleGUI bibliotec || pip install pysimplegui
import PySimpleGUI as sg
import pyperclip

alphabet = 'abcdefghijklmnopqrstuvwxyz,.?çéãõáâàêèóòô!@#$%¨&*()-_+=° 0123456789'
alphabet2 = '9876543210 ,.?çéãõáâàêèóòô!@#$%¨&*()-_+=°zyxwvutsrqponmlkjihgfedcba'

# Criptografar
def encrypt(message, key):
    key = key.isdigit()
    if key:
        message = message.lower()
        caracter = ''
        for slot in message:
            c_index = alphabet.index(slot)
            caracter += alphabet2[(c_index + key) % len(alphabet)]
        return caracter
    else:
        error()
        return ''
    

# Desencriptografar
def decrypt(message, key):
    key = key.isdigit()
    if key:
        message = message.lower()
        caracter = ''
        for slot in message:
            c_index = alphabet2.index(slot)
            caracter += alphabet[(c_index - key) % len(alphabet)]
        return caracter
    else:
        error()
        return ''

# Interface
def interface():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Cifrar'),sg.Button('Decifrar')],  
    ]
    return sg.Window('Interface',size=(300,150), layout=layout, finalize=True)


def criptografar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite a menssagem'),sg.Input(key='message')],
        [sg.Text('Digite a chave em números'),sg.Input(key='key')],
        [sg.Button('Voltar'), sg.Button('Enviar')],
        [sg.Output(size=(50,30))],
        [sg.Button('Copiar')],
    ]
    return sg.Window('Criptografar', layout=layout, finalize=True)

def desencriptografar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite a menssagem'),sg.Input(key='message')],
        [sg.Text('Digite a chave em números'),sg.Input(key='key')],
        [sg.Button('Voltar'), sg.Button('Enviar')],
        [sg.Output(size=(50,30))]
    ]
    return sg.Window('Desencriptografar', layout=layout, finalize=True)

def error():
    sg.theme('Reddit')
    return sg.Window('Erro',
    [[sg.Text('Digite uma chave válida!')],[sg.OK(size=(30)),] ],size=(300,150) ).read(close=True)


# Janelas iniciais
janela1, janela2, janela3, janela4 = interface(), None, None, None

# Loop  de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela3 and event == sg.WIN_CLOSED:
        break

    # Ir para próxima janela
    if window == janela1 and event == 'Cifrar':
        janela1.hide()
        janela2 = criptografar()

    if window == janela2 and event == 'Copiar':
        copy = encrypt(values['message'], values['key'])
        pyperclip.copy(copy)       

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
        print(encrypt(values['message'], values['key']))

    if window == janela3 and event == 'Enviar':
        # Mandando para função
        print(decrypt(values['message'], values['key']))