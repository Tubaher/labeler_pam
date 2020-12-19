# img_viewer.py

import PySimpleGUI as sg
import os.path
import csv
import pandas as pd
# First the window layout in 2 columns

file_list_column = [
    [sg.Text("Choose CSV: "), sg.In(size=(170, 1), enable_events=True, key="-CSV-"), sg.FileBrowse()],
    [sg.Text("Class: "), sg.In(size=(170, 1), enable_events=True, key="-CLASS-")],
    [sg.Text("Images: "), sg.In(size=(170, 1), enable_events=True, key="-IMAGE_PATH-"), sg.Button("NEXT")],
    [sg.Text("Crops: "), sg.In(size=(170, 1), enable_events=True, key="-CROP-"), sg.Button("BACK")],
    [sg.Text("Masks: "), sg.In(size=(170, 1), enable_events=True, key="-MASK-")],
]

# For now will only show the name of the file that was chosen
image_column = [
    [sg.Text("Image")],
    [sg.Image(key="-IMAGE-")]
]


crops_column = [
    [sg.Text("Crop")],
    [sg.Image(key="-CROP_IMG-")]
]

masks_column = [
    [sg.Text("Mask")],
    [sg.Image(key="-MASK_IMG-")]
]


# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column)
    ],
    [
        sg.Column(image_column),
        sg.VSeperator(),
        sg.Column(crops_column),
        sg.VSeperator(),
        sg.Column(masks_column),
    ]
]

window = sg.Window("Labeler PamPam", layout)
n_row = 0
# Run the Event Loop
while True:
    
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-CSV-":
        df = pd.read_csv ('calc_case_description_test_set_simple.csv')
        row = df.iloc[n_row]
        
        window['-CLASS-'].update(row[0])
        window['-IMAGE_PATH-'].update(row[1])
        window['-CROP-'].update(row[2])
        window['-MASK-'].update(row[3])

        try:
            window["-IMAGE-"].update(filename=row[1])
        except:
            pass
        try:    
            window["-CROP_IMG-"].update(filename=row[2])
        except:
            pass    
        try:    
            window["-MASK_IMG-"].update(filename=row[3])
        except:
            pass

    elif event == "NEXT":
        n_row = n_row +  1
        row = df.iloc[n_row]
        
        window['-CLASS-'].update(row[0])
        window['-IMAGE_PATH-'].update(row[1])
        window['-CROP-'].update(row[2])
        window['-MASK-'].update(row[3])

        try:
            window["-IMAGE-"].update(filename=row[1])
        except:
            pass
        try:    
            window["-CROP_IMG-"].update(filename=row[2])
        except:
            pass    
        try:    
            window["-MASK_IMG-"].update(filename=row[3])
        except:
            pass

    elif event == "BACK":
        n_row = n_row -  1
        row = df.iloc[n_row]
        
        window['-CLASS-'].update(row[0])
        window['-IMAGE_PATH-'].update(row[1])
        window['-CROP-'].update(row[2])
        window['-MASK-'].update(row[3])

        try:
            window["-IMAGE-"].update(filename=row[1])
        except:
            pass
        try:    
            window["-CROP_IMG-"].update(filename=row[2])
        except:
            pass    
        try:    
            window["-MASK_IMG-"].update(filename=row[3])
        except:
            pass


        # window["-FILE LIST-"].update(fnames)
    # elif event == "-FILE LIST-":  # A file was chosen from the listbox
    #     try:
    #         filename = os.path.join(
    #             values["-FOLDER-"], values["-FILE LIST-"][0]
    #         )
    #         window["-TOUT-"].update(filename)
    #         window["-IMAGE-"].update(filename=filename)

    #     except:
    #         pass

window.close()