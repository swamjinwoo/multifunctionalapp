import PySimpleGUI as sg
import numpy_financial as npf


class NPV(): 
    def __init__(self):
        self.layout = [
            [sg.Text('Discount Rate'), sg.Push(),sg.InputText(key='DR')],  
            [sg.Text('Initial Cost'), sg.Push(), sg.InputText(key='IC')],
            [sg.Text('Cash Flows'), sg.Push(), sg.InputText(key='CF', size=(26,4)),sg.Push(),sg.Button('Enter Cash Flow', key='button')],
            [sg.Text('Result'), sg.Text(key='Result')], 
            [sg.Button('Calculate'), sg.Button('Clear')],
            [sg.Button('Home'),sg.Button('Exit')]
        ]
        self.window = sg.Window('Net Present Value', self.layout)
    
    def run(self): 
        cash_flow =[]
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit': 
                break 
            elif values['CF'] and event == 'button':
                cash_flow.append(int(values['CF']))
                self.window['CF'].update('')
            elif event == 'Calculate': 
                r = float(values['DR'])
                i = float(values['IC'])
                cash_flow.insert(0,-abs(i))
                npv = npf.npv(r, cash_flow)#This was looked u
                self.window['Result'].update(round(npv,2))
            elif event == 'Home': 
                self.window.close()
                from home import homeWindow
                homeWindow().run()
            elif event == 'Clear': 
                self.window['Result'].update('')
                self.window['DR'].update('')
                self.window['IC'].update('')
                self.window['CF'].update('')
                cash_flow = []
                