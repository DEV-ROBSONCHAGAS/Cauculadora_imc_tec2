import FreeSimpleGUI as sg
import func_calc as func
import func_sugs as func_sugs

# Layout da Janela

sg.theme('DarkAmber')
layout = [
    [sg.Text("Calculadora de IMC e Saúde", font=("Helvetica", 16))],
    [sg.Text("Peso (kg):"), sg.Input(key="-PESO-", text_color=('white'), font=('bold'), size=(10, 1))],
    [sg.Text("Altura (m):"), sg.Input(key="-ALTURA-", text_color=('white'), font=('bold'), size=(10, 1))],
    [sg.Button("Calcular"), sg.Button("Sair")],
    [sg.HSeparator()],
    [sg.Text("Resultado:", font=("Helvetica", 12, "bold"))],
    [sg.Text("", key="-RESULTADO-", size=(40, 1))],
    [sg.Text("Sugestão de Atividade:", font=("Helvetica", 12, "bold"))],
    [sg.Text("", key="-SUGESTAO-", size=(40, 2))]
]

window = sg.Window("Saúde em Foco", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Sair"):
        break

    if event == "Calcular":
        try:
            p = float(values["-PESO-"].replace(',', '.'))
            a = float(values["-ALTURA-"].replace(',', '.'))

            imc = func.calcular_imc(p, a)
            status, dica = func_sugs.obter_sugestoes(imc)

            window["-RESULTADO-"].update(f"IMC: {imc:.2f} ({status})")
            window["-SUGESTAO-"].update(dica)
        except ValueError:
            sg.popup_error("Por favor, insira valores numéricos válidos!")

window.close()