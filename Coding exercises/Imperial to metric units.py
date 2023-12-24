import PySimpleGUI as sg

def convert_f(feet, inches):
    meters = float(feet)*0.3048 + float(inches)*0.0254
    return meters

feet_label = sg.Text("Enter feet:")
input_box1 = sg.InputText(tooltip="Enter feet", key="Feet")

inches_label = sg.Text("Enter inches:")
input_box2 = sg.InputText(tooltip="Enter inches", key="Inches")

convert_button = sg.Button("Convert", key="conversion_button")
conversion_value = sg.Text(key="conversion_text")

window = sg.Window('Conversion from imperial to metric units', layout=[
    [feet_label, input_box1],
    [inches_label, input_box2],
    [convert_button, conversion_value]
])

while True:
    events, values = window.read()
    match events:
        case "conversion_button":
            feet = values["Feet"]
            inches = values["Inches"]
            if feet != "":
                feet = values["Feet"]
            else:
                feet = 0
            if inches != "":
                inches = values["Inches"]
            else:
                inches = 0

            meters = convert_f(feet, inches)
            window['conversion_text'].update(value=f"{feet} ft {inches} converts to {str(meters)[:4]} meters")
        case sg.WIN_CLOSED:
            break

window.close()