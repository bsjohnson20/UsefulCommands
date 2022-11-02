from subprocess import call
import subprocess as sp
import argparse # allow us to run debug mode easily
from datetime import datetime as dt
import logging
import os
# in progress lol
now = dt.now()
current_time = now.strftime("%d-%B-%Y_%H-%M") # time in Day-Month-Year-Hour-Minute
print(current_time)

# test is log dir
#isdir = os.path.isdir('./logs')


if not os.path.exists('./logs'):
    os.makedirs('./logs')
    print('Created log directory')

logging.basicConfig(filename=f'./logs/CommonSettings-{str(current_time)}.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)



def argGet():
    parser = argparse.ArgumentParser(
    description='Quick tools for win\nDark Mode\n File Extensions\n Hidden Files \n etc.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Adding our first argument player name of type string
    parser.add_argument('--debug',
    metavar='debug',
    type=int, # Set what is required, if string returns error
    help='Set to 1 to enable debug logging, 0 to disable. Defaults to 0',
    required=False,
    default=0)
    
    parser.add_argument('--gui',
    metavar='debug',
    type=int, # Set what is required, if string returns error
    help='Set to 1 to enable debug logging, 0 to disable. Defaults to 0',
    required=False,
    default=0)
                        
    return parser.parse_args()

def mainOperation(command):
    logging.debug(' mainOperation function triggered')
    x = sp.run(["powershell",command],capture_output=True) # send a signal to win api, execute powershell
    logging.debug(x)

def enableFileExtensions():
    logging.debug(' File Extensions function triggered')
    
    
    mainOperation(command) # Transmit above to the command transmitter
    # then send args of enabling file extensions

    # hm, I literally don't want to have to enable file extensions EVERY SINGLE TIME I LOGIN >:(
    # IS IT A JPEG? PNG? TXT? Ya don't know with it off.

def darkMode(): # Toggle dark mode on/off
    logging.debug(' Dark mode function triggered')
    try:
        x=int(input('Dark mode: 0\nLight mode: 1\n\nInput: ')) # this is for the args to set True or False for lightmode so inverted.
    except ValueError:
        print('Not a number or not in range')
    mainOperation(f'Set-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value {x}')
    return f"Activated {['Dark mode','Light Mode'][x]}"


def placeholder():
    print('Currently not implemented')




class CommandPipeline:
    def __init__(self,pony='Luna',capture=True,command=''):
        self.command = command
        self.pony = pony
        self.capture = capture
        
        
    def sendCommand(self, command):
        logging.debug(' MainOperation function triggered') # space to give space for DEBUG<space>Main...
        x = sp.run(["powershell",command],capture_output=self.capture) # send a signal to win api, execute powershell
        logging.debug(x)

class System(CommandPipeline):
    def __init__(self):
        super().__init__(self)
        self.CommandPipeline = CommandPipeline
    
    def darkMode(self):
        command = f'Set-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value {x}'
        self.CommandPipeline.sendCommand(self,command)

class FileExplorer(CommandPipeline):
    def __init__(self): 
        super().__init__(self)
        self.CommandPipeline = CommandPipeline # Honestly IDK what I'm doing. I don't understand OOP.

     
    def ShowHiddenFiles(self): # Literally just toggles a checkbox but I want an excuse to code something cool.
        command = '''Push-Location 
    Set-Location HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
    Set-ItemProperty . HideFileExt "0"
    Set-ItemProperty . Show-HiddenFiles -On
    Pop-Location
    Stop-Process -processName: Explorer -force # This will restart the Explorer service to make this work.'''
        self.CommandPipeline.sendCommand(self,command)
    
    
    def ShowTickBoxes(self): # need ps command
        CommandPipeline = CommandPipeline()
    
    
    def ShowFileExtensions(self): # literally ticks a box in explorer totally could do yourself lol
        command = '''Push-Location 
    Set-Location HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
    Set-ItemProperty . HideFileExt "0"
    Set-ItemProperty . Show-HiddenFiles -On
    Pop-Location
    Stop-Process -processName: Explorer -force # This will restart the Explorer service to make this work.'''
        self.CommandPipeline.sendCommand(self,command)


class MainScreen(FileExplorer):
    def __init__(self):
        super().__init__()
        self.FileExplorer = FileExplorer
        
        FileExplorer.ShowFileExtensions(self)
        
        
        
    def options(self):
        while True:
            try:
                operation = int(input("""
    Command 0: Dark mode, enter 1
    Command 1: Enable file extensions
    Command 2: Show hidden items
    Command 3: enable debug mode
    Command 4: not done

        Your command: """))
                commands = [FileExplorer.ShowFileExtensions(self),print()]
                outsideRange= ((operation < 0) or (operation > 4))
                #print(outsideRange)
                if outsideRange == True:
                    print('Unknown operation')
                elif outsideRange == False:
                    # we doing stuff here
                    pass
                    
            except ValueError:
                print('You may have entered a non numerical value, or something outside the possible operations')
            
if __name__ == '__main__':
    Main = MainScreen()
    


#File = FileExplorer()
#File.ShowHiddenFiles()
#File.ShowFileExtensions()

'''
class WindowsSettings:
    def __init__(self):
        pass


def main(debug = 0):
    while True:
        try:
            operation = int(input("""
Command 0: Dark mode, enter 1
Command 1: Enable file extensions
Command 2: Show hidden items
Command 3: enable debug mode
Command 4: not done

    Your command: """))
        
            outsideRange= ((operation < 0) or (operation > 4))
            #print(outsideRange)
            if outsideRange == True:
                print('Unknown operation')
            elif outsideRange == False:
                #print('Valid range')
                break
        except ValueError:
            print('You may have entered a non numerical value, or something outside the possible operations')
            
            
    currentPossibleOperations = [darkMode,enableFileExtensions,placeholder,placeholder,placeholder,placeholder]
    print(f'Executing operation {currentPossibleOperations[operation]()}')
    #currentPossibleOperations[operation]()
    

if __name__ == '__main__':
    args = argGet()
    if args.debug == 0:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug(' This will get logged if it\'s in debug mode')
    
    main(args.debug)
    
    


logging.info("Running CommonSettings app")

logger = logging.getLogger('urbanGUI')'''