import PySimpleGUI as sg 

class sequenceWindow: 
    def __init__(self): 
        self.layout = [
            [sg.Button('Arithmetic Sequence', key = 'AS', size = (20,6)), 
                sg.Button('Geometric Sequence', key = 'GS', size=(20,6))], 
            [sg.Button('Home', size = (20,6)), sg.Button('Exit', size=(20,6))]
        ]
        self.window = sg.Window('Sequence', self.layout)
         
    def run(self): 
        while True: 
            event, _ = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit': 
                break 
            elif event == 'AS': 
                self.window.close()
                asWindow().run()
            elif event == 'GS': 
                self.window.close()
                gsWindow().run()
            elif event == 'Home': 
                self.window.close()
                from home import homeWindow
                homeWindow().run()
                
                
class asWindow: 
    def __init__(self):
        self.layout = [
            [sg.Text('First Term'), sg.Push(), sg.InputText(key='a')], 
            [sg.Text('Common Difference'), sg.Push(), sg.InputText(key='d')],
            [sg.Text('Number of Terms'), sg.Push(), sg.InputText(key='n')],
            [sg.Push(),sg.Text('Result'),sg.Push()],
            [sg.Multiline(size=(60, 5), key='Result', autoscroll=True)],
            [sg.Push(),sg.Button('Calculate'),sg.Push()], 
            [sg.Push(),sg.Button('Home'),sg.Button('Back'), sg.Button('Exit'),sg.Push()]
        ]
        
        self.window=sg.Window('Arithemtic Sequence', self.layout)
        
    def run(self): 
        series = []
        while True: 
            event,values=self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit': 
                break 
            elif event == 'Calculate': 
                if values['a'] and values['d'] and values['n']:
                    for i in range(1,int(values['n'])+1): 
                        t = int(values['a']) + (i - 1) * int(values['d'])
                        series.append(int(t))
                    self.window['Result'].update(series)
                else: 
                    pass
            elif event == 'Back': 
                self.window.close()
                sequenceWindow().run()
            elif event == 'Home': 
                self.window.close()
                from home import homeWindow
                homeWindow().run()
                
class gsWindow: 
    def __init__(self): 
        self.layout = [
            [sg.Text('First Term'), sg.Push(), sg.InputText(key='a')], 
            [sg.Text('Common Ratio'), sg.Push(), sg.InputText(key='r')],
            [sg.Text('Number of Terms'), sg.Push(),sg.InputText(key='n')],
            [sg.Push(),sg.Text('Result'),sg.Push()],
            [sg.Multiline(size=(60, 5), key='Result', autoscroll=True)],
            [sg.Push(),sg.Button('Calculate'),sg.Push()], 
            [sg.Push(),sg.Button('Home'),sg.Button('Back'), sg.Button('Exit'),sg.Push()]
        ]
        self.window = sg.Window('Geometric Sequence', self.layout)
        
    def run(self): 
        sequence = []
        while True: 
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit': 
                break 
            elif event == 'Calculate': 
                if values['a'] and values['r'] and values['n']:
                    for i in range(1, int(values['n']) + 1): 
                        t = int(values['a']) * int(values['r']) ** (i - 1)
                        sequence.append(t)
                    self.window['Result'].update(sequence)
                else: 
                    pass
            elif event == 'Back': 
                self.window.close()
                sequenceWindow().run()
            elif event == 'Home': 
                self.window.close()
                from home import homeWindow
                homeWindow().run()
            
                    
                