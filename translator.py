#Author: Kahzerx

import os
import time
import sys
import subprocess
from googletrans import Translator#pip install googletrans or python -m pip install googletrans

so = sys.platform

if so == 'win32' or so == 'win64':
	from win10toast import ToastNotifier#pip install win10toast or python -m pip install win10toast
	toaster = ToastNotifier()

elif so == 'linux' or so == 'linux2':#pip install notify2 or python -m pip install notify2
	import notify2


translator = Translator()
#log = 'C:/Users/kahzerx/Downloads/MultiMC/instances/1.13.2/.minecraft/logs/latest.log'
"""
u might need to add a 'r' at the begining of the windows path for it to recognize correctly, like so: r'C:/path/to/log'
"""
log = '/home/kahzerx/.local/share/multimc/instances/1.13.2/.minecraft/logs/latest.log'

prev_size = os.path.getsize(log)
cur_size = os.path.getsize(log)


while True:
	time.sleep(0.04)
	try:
		prev_size = cur_size
		cur_size = os.path.getsize(log)
		
		if prev_size == cur_size:
			continue

		with open(log, 'r') as file:
   			lastline = (list(file)[-1][:-1]).split(' ')
		#print (lastline)

		if '[CHAT]' not in lastline:
			continue

		message = ' '.join(lastline[3:])
		translation = translator.translate(message, dest='en')

		if translation.src == 'en':
			continue

		if so == 'win32' or so == 'win64':
			toaster.show_toast(translation.src, translation.text, threaded=True, icon_path=None, duration=2)
			print('(' + translation.src + ')' + translation.text)

		elif so == 'linux' or so == 'linux2':
			print('(' + translation.src + ')' + translation.text)
			notify2.init("Minecraft Translator")
			n = notify2.Notification(translation.src, translation.text)
			#n.set_location(1000, 500)
			n.timeout = 14000
			n.show()

	except Exception as ex:
		print('Error: ' + str(ex))
