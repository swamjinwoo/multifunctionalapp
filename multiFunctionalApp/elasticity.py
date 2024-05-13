import PySimpleGUI as sg 

class elasticityWindow: 
    def __init__(self): 
        self.layout = [ 
            [sg.Text('Initial Quantity'), sg.Push(), sg.InputText(key='Q1')],
            [sg.Text('Final Quantity'), sg.Push(),sg.InputText(key='Q2')], 
            [sg.Text('Inital Price'), sg.Push(), sg.InputText(key='P1')],
            [sg.Text('Final Price'), sg.Push(),sg.InputText(key='P2')],
            [sg.Text('Result'), sg.Text(key='Result')],
            [sg.Button('Price Elasticity Calculate', key = 'PED')],
            [sg.Button('Home'), sg.Button('Exit')]
        ]
        self.window = sg.Window('Elasticity', self.layout)

    def run(self): 
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break 
            elif event == 'PED': 
                changeQuantity = (int(values['Q2']) - int(values['Q1'])) / int(values['Q1'])
                changePrice = (int(values['P2']) - int(values['P1'])) / int(values['P1'])
                ed = changeQuantity / changePrice 
                if ed == 1: 
                    x = 'Unitary Elastic'
                elif abs(ed) > 1: 
                    x = 'Relatively Elastic'
                else: 
                    x = 'Relatively Inelastic'
                self.window['Result'].update(f'{ed} = {x}')\
                
            elif event == 'Home': 
                self.window.close()
                from home import homeWindow
                homeWindow().run()
