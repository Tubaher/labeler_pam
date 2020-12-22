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
    [sg.Text("Masks: "), sg.In(size=(170, 1), enable_events=True, key="-MASK-"), sg.Button("SAVE")],
]

# For now will only show the name of the file that was chosen
image_column = [
    [sg.Text("Image")],
    [sg.Image(key="-IMAGE-", size=(100,100))]
]


crops_column = [
    [sg.Text("Crop")],
    [sg.Image(key="-CROP_IMG-", size=(100,100))]
]

masks_column = [
    [sg.Text("Mask")],
    [sg.Image(key="-MASK_IMG-", size=(100,100))]
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
        df = pd.read_csv (values['-CSV-'])
        if n_row <= 0:
            window['BACK'].update(disabled=True)
        elif n_row > 0 and n_row < (df.shape[0] -1):
            window['BACK'].update(disabled=False)
            window['NEXT'].update(disabled=False)
        elif n_row >= (df.shape[0] -1):
            window['NEXT'].update(disabled=True)  
        
        
        row = df.iloc[n_row]
        
        window['-CLASS-'].update(row[0])
        window['-IMAGE_PATH-'].update(row[1])
        window['-CROP-'].update(row[2])
        window['-MASK-'].update(row[3])

        try:
            window["-IMAGE-"].update(filename=row[1], size=(100,100))
        except:
            pass
        try:    
            window["-CROP_IMG-"].update(filename=row[2], size=(100,100))
        except:
            pass    
        try:    
            window["-MASK_IMG-"].update(filename=row[3], size=(100,100))
        except:
            pass

    elif event == "NEXT":

        row[0] = values['-CLASS-']
        row[1] = values['-IMAGE_PATH-']
        row[2] = values['-CROP-']
        row[3] = values['-MASK-']
        
        n_row = n_row +  1

        if n_row <= 0:
            window['BACK'].update(disabled=True)
        elif n_row > 0 and n_row < (df.shape[0] -1):
            window['BACK'].update(disabled=False)
            window['NEXT'].update(disabled=False)
        elif n_row >= (df.shape[0] -1):
             window['NEXT'].update(disabled=True)  

        row = df.iloc[n_row]
        
        window['-CLASS-'].update(row[0])
        window['-IMAGE_PATH-'].update(row[1])
        window['-CROP-'].update(row[2])
        window['-MASK-'].update(row[3])

        try:
            window["-IMAGE-"].update(filename=row[1], size=(100,100))
        except:
            pass
        try:    
            window["-CROP_IMG-"].update(filename=row[2], size=(100,100))
        except:
            pass    
        try:    
            window["-MASK_IMG-"].update(filename=row[3], size=(100,100))
        except:
            pass

    elif event == "BACK":

        row[0] = values['-CLASS-']
        row[1] = values['-IMAGE_PATH-']
        row[2] = values['-CROP-']
        row[3] = values['-MASK-']

        n_row = n_row -  1
        
        if n_row <= 0:
            window['BACK'].update(disabled=True)
        elif n_row > 0 and n_row < (df.shape[0] -1):
            window['BACK'].update(disabled=False)
            window['NEXT'].update(disabled=False)
        elif n_row >=  (df.shape[0] -1):
             window['NEXT'].update(disabled=True) 

        row = df.iloc[n_row]
        
        window['-CLASS-'].update(row[0])
        window['-IMAGE_PATH-'].update(row[1])
        window['-CROP-'].update(row[2])
        window['-MASK-'].update(row[3])

        try:
            window["-IMAGE-"].update(filename=row[1], size=(100,100))
        except:
            pass
        try:    
            window["-CROP_IMG-"].update(filename=row[2], size=(100,100))
        except:
            pass    
        try:    
            window["-MASK_IMG-"].update(filename=row[3], size=(100,100))
        except:
            pass
    
    elif event == 'SAVE':

        if n_row <= 0:
            window['BACK'].update(disabled=True)
        elif n_row > 0 and n_row < (df.shape[0] -1):
            window['BACK'].update(disabled=False)
            window['NEXT'].update(disabled=False)
        elif n_row >= (df.shape[0] -1):
             window['NEXT'].update(disabled=True)  

        row[0] = values['-CLASS-']
        row[1] = values['-IMAGE_PATH-']
        row[2] = values['-CROP-']
        row[3] = values['-MASK-']
        df.to_csv('./test.csv', index=False)


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