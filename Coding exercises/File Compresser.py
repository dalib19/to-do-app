import PySimpleGUI as sg
from ZipCreator import compact_file
import pathlib

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="file_location")

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="zip_location")

compress_button = sg.Button("Compress")

window = sg.Window("File compressor", layout=[
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button]
])

while True:
    events, values = window.read()
    file_locations = values["file_location"].split(";")
    zip_location = values["zip_location"]

    compact_file(file_locations, zip_location)



window.close()