from xml.etree.ElementTree import *
import translate

import PySimpleGUI as sg


def main():
    sg.theme('SystemDefault1')
    layout = [
        [sg.Text('Enter an English word')],
        [sg.InputText(key='input',), sg.Button('send', key='send')],
        [sg.Text(key='output_msg'),sg.Button('register', key='register', visible=False)]
    ]

    window = sg.Window('Theme Browser', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'send':
            input_word = values['input']
            translate_obj = translate.Translate()
            translate_word = translate_obj.translate_language_en_to_ja(input_word)
            window['output_msg'].update(value=translate_word)
            window['register'].update(visible=True)        
        elif event == 'register':
            input_word = values['input']
            output_word = values['output_msg']
            # sqLiteで登録処理を追加する
            window['input'].update(value="")
            window['output_msg'].update(value="")
            window['register'].update(visible=False)
    window.close()


if __name__ == '__main__':
    main()
