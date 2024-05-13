import PySimpleGUI as sg 
from calculator import calculatorWindow
from stopwatch import stopwatchWindow
from NPV import NPV
from sequence import sequenceWindow
from elasticity import elasticityWindow 

class homeWindow: 
    def __init__(self): 
        self.layout =[ 
                      [sg.Push(), sg.Button('Calculator',size = (20,6)),
                        sg.Button('StopWatch', size = (20,6)), sg.Push()], 
                      [sg.Push(), sg.Button('NPV', size = (20,6)), 
                        sg.Button('Sequence', size = (20,6)), sg.Push()],
                      [sg.Push(), sg.Button('Elasticity', size = (20,6)),
                       sg.Button('Exit', size = (20,6)),sg.Push()]
                      ]
        self.window=sg.Window('Home',self.layout)

    def run(self): 
        while True: 
            event, values=self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit': 
                break 
            elif event == 'Calculator': 
                self.window.close()
                calculatorWindow().run()
            elif event == 'StopWatch': 
                self.window.close()
                stopwatchWindow().run()
            elif event == 'NPV': 
                self.window.close()
                NPV().run()
            elif event == 'Sequence': 
                self.window.close()
                sequenceWindow().run()
            elif event == 'Elasticity':
                self.window.close()
                elasticityWindow().run()
                
        self.window.close()
                
