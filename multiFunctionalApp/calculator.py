import PySimpleGUI as sg 


class calculatorWindow: 
    def __init__(self): 
        self.col_1 = [ 
            [sg.Button('7', size = (4,2),font="bold"),sg.Button('8', size = (4,2),font="bold"),sg.Button('9', size = (4,2),font="bold"),],
            [sg.Button('4', size = (4,2),font="bold"),sg.Button('5', size = (4,2),font="bold"),sg.Button('6', size = (4,2),font="bold"),],
            [sg.Button('1', size = (4,2),font="bold"),sg.Button('2', size = (4,2),font="bold"),sg.Button('3', size = (4,2),font="bold"),],
            [sg.Button('Home', size = (4,2),font="bold"),sg.Button('0', size = (4,2),font="bold"),sg.Button('.', size = (4,2),font="bold", key="-DOT-"),]
        ]

        self.col_2 = [ 
            [sg.Button('*', size = (4,2),font="bold",key="-MULTIPLY-")],
            [sg.Button('-', size = (4,2),font="bold", key="-SUBTRACT-")],
            [sg.Button('+', size = (4,5),font="bold", key="-ADD-")],
        ]

        self.col_3 = [ 
            [sg.Button('/', size = (4,2),font="bold", key="-DIVIDE-")],
            [sg.Button('<--', size = (4,2),font="bold", key="-CLEAR-")],
            [sg.Button('CE', size = (4,2),font="bold", key="-CLEARALL-")],
            [sg.Button('=', size = (4,2),font="bold", key="-EQUAL-")],
        ]
        self.layout = [ 
                [sg.HorizontalSeparator()],
                [sg.Text(font = (None, 30), size = (15,1), key = "-INPUT-")],
                [sg.HorizontalSeparator()],
                [sg.Col(self.col_1),sg.VerticalSeparator(),sg.Col(self.col_2), sg.Col(self.col_3)]
        ]
        self.window = sg.Window('Calculator', self.layout)
        
    def run(self):
        num = [str(i) for i in range(10)]
        history = '' 
        operator = ["-DIVIDE-", "-ADD-", "-SUBTRACT-", "-MULTIPLY-"]
        while True: 
                event,values = self.window.read()

                if event == sg.WINDOW_CLOSED: 
                    break 
                if event in num: 
                    if len(history) < 12: 
                        history += event
                        self.window["-INPUT-"].update(int(history)) 
                elif event in operator: 
                    op = event 
                    num_1 = float(history) 
                    history = ''
                elif event == "-EQUAL-": 
                    num_2 = float(history)
                    if op == "-ADD-": 
                        result = num_1 + num_2
                    elif op == "-SUBTRACT-": 
                        result = num_1 - num_2
                    elif op == "-MULTIPLY-": 
                        result = num_1 * num_2
                    elif op == "-DIVIDE-": 
                        result = num_1 / num_2

                    self.window["-INPUT-"].update(result) 
                elif event == "-CLEAR-": 
                    if len(history) > 0: 
                        history = history[:-1]
                        self.window["-INPUT-"].update(history) 
                elif event == "-CLEARALL-": 
                    self.window['-INPUT-'].update("")
                    history =''
                elif event == 'Home':
                    self.window.close()
                    from home import homeWindow
                    homeWindow().run()

                    
        
        self.window.close()