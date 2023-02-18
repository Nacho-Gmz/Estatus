import psutil, os

if __name__ == '__main__':
    while True:
        activo = 0
        for proc in psutil.process_iter():
            if proc.name().lower() == 'agenda.exe':
                activo = 1
        if activo == 1:
            pass
        else:
            os.system('Agenda.exe')