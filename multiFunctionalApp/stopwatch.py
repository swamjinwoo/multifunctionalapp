import PySimpleGUI as sg 
import time

class stopwatchWindow(): 
    def __init__(self): 
        self.layout = [
                [sg.Text('Stopwatch', font=('Helvetica', 20), justification='center')],
                [sg.Text('00:00:00', font=('Helvetica', 48), justification='center', key='-TIMER-')],
                [sg.Button('Start', size=(10, 2)), sg.Button('Pause', size=(10, 2)), sg.Button('Reset', size=(10, 2))],
                [sg.Button('Home', size=(10,2)), sg.Push(), sg.Button('Exit', size =(10,2))]
                ]
    
    def run(self):
                self.window = sg.Window('Stopwatch', self.layout, finalize=True)

                running = False
                start_time = None
                paused_time = None
                total_paused_time = 0
                
                while True:
                    event, values = self.window.read(timeout=10)

                    if event == sg.WINDOW_CLOSED or event == 'Exit':
                        break
                    elif event == 'Home': 
                        self.window.close()
                        from home import homeWindow
                        homeWindow().run()
                    elif event == 'Start':
                        if not running:
                            running = True
                            start_time = time.time()
                            paused_time = None
                    elif event == 'Pause':
                        if running:
                            running = False
                            paused_time = time.time()
                    elif event == 'Reset':
                        running = False
                        start_time = None
                        paused_time = None
                        total_paused_time = 0
                        self.window['-TIMER-'].update('00:00:00')

                    if running:
                        if paused_time is not None:
                            total_paused_time += time.time() - paused_time
                            paused_time = None

                        elapsed_time = time.time() - start_time - total_paused_time
                        hours = int(elapsed_time / 3600)
                        minutes = int((elapsed_time % 3600) / 60)
                        seconds = int(elapsed_time % 60)
                        self.window['-TIMER-'].update('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

                self.window.close()