import PySimpleGUI as sg



###########################################

sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.InputText(size=(3,3)), sg.Text('x'), sg.InputText(size=(3,3)), sg.Text("y   = "), sg.InputText(size=(3,3))],
            [sg.InputText(size=(3,3)), sg.Text('x'), sg.InputText(size=(3,3)), sg.Text("y   = "), sg.InputText(size=(3,3))],
            [sg.Text('x: '), sg.Text("", key = "rX"), sg.Text('y: '), sg.Text("", key = "rY")],
            [sg.OK("Calculate", size=(10,1)), sg.Cancel("Exit", size=(10,1))]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"

###########################################

def Cramer(x1, y1, x2, y2, b1, b2):
    print(x1, y1, x2, y2, b1, b2)
    #licze wyznacznik A:

    detA = (x1 * y2) - (y1 * x2)

    print(detA)

    Dx = (b1 * y2) - (b2 * y1)

    print(Dx)

    Dy = (x1 * b2) - (x2 * b1)

    print(Dy)

    x = Dx // detA
    y = Dy // detA

    return (x,y)

resX = ""
resY = ""

while True:             
    event, values = window.read()


    x, y = Cramer(int(values[0]), int(values[1]), int(values[3]), int(values[4]), int(values[2]), int(values[5]))


    window["rX"].update(x)
    window["rY"].update(y)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
