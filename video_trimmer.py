#need_debug(function(setup_parts))

from concurrent.futures import ThreadPoolExecutor # Thread by pool # man+ / youtube+
from datetime import datetime # datetime
from psutil import cpu_count # Process #psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. # multiprocessing.cpu_count() # os.cpu_count() # os.environ['NUMBER_OF_PROCESSORS']
#from shutil import copy, move, disk_usage  # файлы
from time import sleep # time, ctime, perf_counter, strftime, localtime  # время-задержка

import re
import json
import sys
import logging
import tkinter as tk
import os

from threading import (  # Thread # Barrier # работа с потоками #mutli_async
	 Semaphore )

'''
from subprocess import ( # Работа с процессами #console shell=["True", "False"]
	  run ) # check_output, Popen, call, PIPE, STDOUT, TimeoutExpired
'''

from colorama import ( # Cursor # Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows. # Fore.color, Back.color #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
	Fore, Style, init) # Back

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
	level=logging.INFO)

#video_trimmer.py #D:\Books\Development\Source\Values\find_ffmpeg_parts.py

#video_file(short_data)

#regular_expression #tv_series|big_film
crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)") #short_filename_regex #season_and_regex(findall)
#crop_filename_regex = re.compile(r"(_[\d+]{2}s)(.*)") #short_filename_regex #season(findall)

#current_short = crop_filename_regex.sub("", jc.split("\\")[-1])

# --- cpu_optimize ---
ccount = int(cpu_count(logical=True)) #False

if ccount > 1:
	ccount -= 1

unique_semaphore = Semaphore(ccount)

# --- path's ---
path_for_queue = "c:\\downloads\\mytemp\\"
path_to_done = "c:\\downloads\\" # mytemp\\temp\\
#path_for_folder1 = "c:\\downloads\\new\\"
#copy_dst = "c:\\downloads\\combine\\original\\"

job_count = 0

#logging(start)
log_base = "c:\\downloads\\mytemp\\trimmer.json" #unique_logging(test)
log_print = "c:\\downloads\\mytemp\\trim.log"

some_dict = {}

try:
	with open(log_base, encoding="utf-8") as lbf:
		log_dict = json.load(lbf)
except:
	log_dict = {}

	with open(log_base, "w", encoding="utf-8") as lbf:
		json.dump({}, lbf, ensure_ascii=False, indent=2)

init(autoreset=True)

# --- procedures ---

open(log_print, "w", encoding="utf-8").close()

def write_log(desc="", txt=""): #event_log

	if any((not desc, not txt)):
		return

	global log_dict

	try:
		with open(log_base, encoding="utf-8") as lbf:
			log_dict = json.load(lbf)
	except:
		with open(log_base, "w", encoding="utf-8") as lbf:
			json.dump({}, lbf, ensure_ascii=False, indent=2)
	else:
		log_dict[desc.strip()] = txt.strip()

		with open(log_base, "w", encoding="utf-8") as lbf:
			json.dump(log_dict, lbf, ensure_ascii=False, indent=2, sort_keys=True)

	#logging(old/plain)

	try:
		with open(log_print, encoding="utf-8") as lpf:
			lprint = lpf.readlines()
	except:
		lprint = []

	lprint.append("%s:%s\n" % (desc.strip(), txt.strip()))

	if lprint:
		check_log = set()

		for lp in lprint:

			if len(lp.strip()) == 0:
				continue

			if not lp in check_log:
				check_log.add(lp)

		if len(check_log) <= len(lprint) and check_log:
			lprint = sorted(list(check_log), reverse=False) #without_abc(set->list)

		with open(log_print, "w", encoding="utf-8") as lpf:
			lpf.writelines("%s" % lp for lp in lprint) #\n

write_log("debug start", str(datetime.now()))

###debug/trimmer_stop/test_after_debug###
#exit()
#sys.exit()

def most_frequent(list):
	"""
	Самый частый элемент

	Этот короткий скрипт вернёт элемент, чаще всего встречающийся в списке.

	Используются про6двинутые параметры встроенной функции max():

	• первым аргументом она получает множество из элементов списка (помним, что в множестве все элементы уникальны);
	• затем применяет к каждому из них функцию count, подсчитывающую, сколько раз элемент встречается в списке;
	• после этого возвращает элемент множества, который имеет больше всего «попаданий».

	В качестве аргумента можно использовать списки, кортежи и строки.

	>>>numbers = [1,2,1,2,3,2,1,4,2]
	>>>most_frequent(numbers) #2
	"""
	return max(set(list), key=list.count)

#list (string / numbers)
#search_moda([1,2, 2, 4, 4, 5, 7, 7]) #2, 4, 7
def search_moda(lst):
	moda = []

	for i in lst:
		if lst.count(i) != list(set(lst)).count(i):
			moda.append(i)

	return list(set(moda))

def ready_file(filename):
	root = tk.Tk()

	root.title("Обработка завершилась")

	#w = root.winfo_screenwidth() # ширина экрана
	#h = root.winfo_screenheight() # высота экрана
	#w = w//2 # середина экрана
	#h = h//2
	#w = w - 180 # смещение от середины
	#h = h - 180
	#root.geometry('400x400+{}+{}'.format(w, h))

	# creating fixed geometry of the
	# tkinter window with dimensions 240x320
	root.geometry('300x140+0+0') #f(format)
	root.resizable(False,False)

	txt = "Файл %s\nуспешно обработан" % filename

	label = tk.Label(root, font='arial 8', fg='#800', text=txt)

	label.pack(padx=0, pady=5)
	#label.grid(column=0, row=0)

	root.after(3000, root.quit) #5000 = 5 seconds

	root.mainloop()

def seconds_to_time(seconds):

	if not seconds:
		return (0, 0, 0, 0)

	"""
	#totalseconds_unpack(hours/minutes/seconds)

	hours = vduration // 3600 #часы
	minutes = vduration % 3600 // 60 #минуты
	seconds = vduration % 3600 % 60 #секунды
	"""
	seconds_in_day = 86400 #24*3600
	seconds_in_hour = 3600
	seconds_in_minute = 60

	days = hours = minutes = seconds = 0

	dhms = ()

	#totalseconds_unpack(days/hours/minutes/seconds)
	try:
		days = seconds // seconds_in_day
		seconds -= (days * seconds_in_day)
		hours = seconds // seconds_in_hour
		seconds -= (hours * seconds_in_hour)
		minutes = seconds // seconds_in_minute
		seconds -= (minutes * seconds_in_minute)
	except:
		days = hours = minutes = seconds = 0

		dhms = (days, hours, minutes, seconds)

		return dhms #if_error_then_null
	else:
		dhms = (days, hours, minutes, seconds)

		return dhms #if_normal_then_data

class width_height:

	def __init__(self, filename):
		self.filename = filename

	'''
	def get_codecs(self, filename):

		lst = []

		#ffprobe -v error -show_entries stream=codec_name -of csv=p=0:s=x input.m4v
		cmd = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "stream=codec_name", "-of", "csv=p=0:s=x", filename] #output_format
		ci = path_for_queue + "codecs.nfo"

		p = os.system("cmd /c %s > %s" % (" ".join(cmd), ci))

		if p == 0:

			try:
				with open(ci) as f:
					lst = f.readlines()
			except:
				lst = []
			else:
				if lst:
					tmp = [l.strip() for l in lst if l]
					lst = tmp

					#print(lst) #['h264', 'aac']

			if os.path.exists(ci):
				os.remove(ci)

		return lst
	'''

	def get_width_height(self, filename, is_calc=False, maxwidth=640):

		global job_count

		is_owidth = 0 # is_change = False

		#self.filename = filename

		if not self.filename:
			return

		#ffprobe -v error -show_entries stream=width,height -of csv=p=0:s=x input.m4v
		cmd_wh = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x", self.filename] #output_format
		wi = path_for_queue + "wh.nfo"

		os.system("cmd /c %s > %s" % (" ".join(cmd_wh), wi))

		#width_height_str = ""

		width, height = 0, 0

		try:
			with open(wi) as whf:
				width_height_str = whf.readlines()[0].strip()
		except:
			width_height_str = ""

		if os.path.exists(wi):
			os.remove(wi)

		try:
			if "x" in width_height_str:
				width, height = int(width_height_str.split("x")[0]), int(width_height_str.split("x")[-1])

				is_owidth = width

				#job_status = ""

				try:
					job_status = "%s" % str((width, height, self.filename, "ok")) if width <= maxwidth else "%s" % str((width, height, self.filename, "job"))
				except:
					job_status = ""
				finally:
					if job_status:
						print(job_status)
						write_log("debug [w/h/$file$]", "%s" % job_status)

				#if width <= maxwidth: #640
					#print("debug [w/h/$file$]: %s" % str((width, height, self.filename, "ok")))
				if width > maxwidth: #640
					print("debug [w/h/$file$]: %s" % job_status)
					job_count += 1

		except:
			width, height = 0, 0
			print("debug [w/h error]: %s" % self.filename)

		new_height = 0

		is_owidth = width

		if all((is_calc == True, width > maxwidth, width, height)):

			new_height = maxwidth // (width / height)

			width = int(maxwidth)
			height = int(new_height)

			if height % 2 != 0:
				height += 1

			#print(width, height, is_owidth != width)

			wh_status = "x".join([str(width), str(height)]) + " resized" if is_owidth != width else "x".join([str(width), str(height)]) + " no resized"

			if all((width, height, wh_status)):
				print(wh_status)

		return (int(width), int(height), is_owidth != width)

	def get_length(self, filename):
		cmd_fd = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "format=duration", "-of", "compact=p=0:nk=1", self.filename] #output_format
		fdi = path_for_queue + "duration.nfo"

		os.system("cmd /c %s > %s" % (" ".join(cmd_fd), fdi)) #1|und #type1

		duration_list = []

		duration_null = 0

		with open(fdi, encoding="utf-8") as fdif:
			duration_list = fdif.readlines()

		if os.path.exists(fdi):
			os.remove(fdi)

		try:
			if "." in duration_list[0] and duration_list:
				return int(duration_list[0].split(".")[0])
		except:
			return duration_null #if_null_or_error

		print("Duration time is %d" % int(duration_null))

		return duration_null

	def __del__(self):
		print("%s удалён" % str(self.__class__.__name__))

class MyTime:

	def __init__(self):
		pass

	def sleep_with_count(self, ms=5):
		"""Подсчитать сколько времени задержка"""

		stime = datetime.now()

		self.ms = ms

		sleep(self.ms * 60)

		etime = datetime.now()

		#total_time = 0

		dd = hh = mm = ss = 0

		try:
			total_time = abs(stime - etime).seconds
		except:
			print(Style.BRIGHT + Fore.RED + "debug sleeptime", "pass", sep="\t", end="\n")

			total_time = 0
		finally:
			if total_time:
				dd, hh, mm, ss = seconds_to_time(total_time)
				if any((dd, hh, mm, ss)):
					print(Style.BRIGHT + Fore.WHITE + "debug time", "Задержка сработала на : %d дн., %d ч., %d м., %d с." % (dd, hh, mm, ss), sep="\t", end="\n")

# --- dos_shell ---
#dir /r/b/s Short_AAsBBe*.ext > ext.list
#(for /f "delims=" %a in @echo file '%a') > concat.lst
#ffmpeg -f concat -safe 0 -y -i concat.lst -c copy Short_AAsBBe.ext

#setup_parts(fcount=2681, ext=".mp4", is_Trim=Trim, is_Scale=False, is_Sount=False):
"""
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=0:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e01p.mp4
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=383:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e02p.mp4
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=766:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e03p.mp4
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=1149:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e04p.mp4
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=1532:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e05p.mp4
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=1915:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e06p.mp4
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=2298:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e07p.mp4
c:\downloads\mytemp\ffmpeg -y -i C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e.mp4 -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=2681:383" -c:a aac -af "dynaudnorm" C:\Downloads\Combine\Original\Backup\Bolshoy_skachyok_01s11e08p.mp4
"""
def setup_parts(fcount, filename, parts=10, ext=".mp4", is_Trim=True, is_Scale=False, is_Sound=False):

	def one_to_double(cnt):

		if cnt in range(0, 10): #00
			return "".join(["00",str(cnt)])
		elif cnt in range(11, 100): #99
			return "".join(["0",str(cnt)])
		elif cnt > 100:
			return str(cnt)

	framecount = fcount #7010 #video_resize.py #get_length(filename)

	try:
		fname = filename.split("\\")[-1]
	except:
		fname = ""

	cmd_str = []

	#hidden(no_limit_by_minutes)
	"""
	if all((framecount < 60 * 40, framecount)):
		write_log("debug trimtime[error]", "Время должно быть больше 40 минут. [%s]" % str((framecount // 2400, fname)))
		return cmd_str
	#elif not framecount:
		#write_log("debug trimtime[error]", "Не смог прочитать время. [%s]" % fname)
		#return cmd_str
	"""
		
	if filename.split(".")[-1].lower() != "mp4":
		return cmd_str #job_only_mp4_files

	#if framecount % 2 != 0:
		#framecount -= 1

	tp = framecount // parts #framecount // 10(parts) #(debug/test) #parts=10 (default)

	try:
		if tp:
			write_log("debug timepart[calc]", "timepart is: %d" % tp) #606
	except BaseException as e:
		write_log("debug timepart[error]", str(e))

	dl = [ds for ds in range(0, framecount-parts, tp) if all((ds % tp == 0, ds < framecount-parts))] #10(parts) #(debug/test) #parts=10 (default)

	try:
		if dl:
			write_log("debug duration[generate]", "duration's [%d] [%s]" % (len(dl), fname)) #10
	except BaseException as e:
		write_log("debug duration[error]", str(e))

	dct = {}

	try:	
		if len(dl) >= 1:
			dct = {dl[i]:tp for i in range(len(dl))} #debug_test(skip_last_destonation)
	except BaseException as e:
		write_log("debug destonation[error]", str(e))
	else:
		if dct:		
			write_log("debug parttime", str(dct))
		elif not dct:		
			write_log("debug parttime", "Null")			

	#is_Trim = False	

	#if len(dct) == 0:
		#is_Trim = False
	#elif len(dct) >= 1:
		#is_Trim = True

	print("Debug for %s [value]" % fname)

	#print()

	#print("[p]=%s" % str(max(p,key=int)))
	#print("ps=%s" % str(ps))
	#print("[dl]=%s" % str(dl))
	#print("{dct}=%s" % str(dct))

	#change_scale(logic)

	try:	
		if is_Scale:
			try:
				wh = width_height(filename=filename)
				width, height, resized = wh.get_width_height(filename=filename, is_calc=True)
				del wh
			except:
				width = height = 0
				resized = False
				print("Scaled [err]")
				write_log("debug scale[yes]", "Scaled [err] [%s]" % fname)
			else:
				whr = ";".join([str(width), str(height), str(resized), fname])
				print(whr)
				write_log("debug scale[yes]", whr)
	
		elif not is_Scale:
			try:
				wh = width_height(filename=filename)
				width, height, resized = wh.get_width_height(filename=filename, is_calc=True)
				del wh
			except:
				width = height = 0
				resized = False
				print("No scale [err]")
				write_log("debug scale[no]", "No scale [err] [%s]" % fname)
			else:
				whr = ";".join([str(width), str(height), str(resized), fname])
				print(whr)
				write_log("debug scale[no]", whr)
	except BaseException as e:
		write_log("debug scale[error]", str(e))

	try:
		if all((width, height)): #resized
			whr = "x".join([str(width), str(height), str(resized), fname])
			print(whr)
			write_log("debug [scale/status/filename]", whr) #width/height/is_scale/fname
	except BaseException as e:
		write_log("debug error[width/height]", str(e))			

	cnt = 0

	cmd_str = []
	
	for d in dct:

		cnt += 1

		year_regex = re.compile(r"(\([\d+]{4}\))", re.M)

		seas_regex = re.compile(r"(_[\d+]{2,4}s[\d+]{2}e|_[\d+]{2,4}[\d+]{2}s?([\d+]{2}p))", re.M) #se_%~pa #sep_%~pa

		try:
			if any((year_regex.findall(filename.split("\\")[-1]), seas_regex.findall(filename.split("\\")[-1]))):
				ofilename = filename.split("\\")[-1].split(".")[0] + "".join(["_", one_to_double(cnt),"p"])+ext #for_big_films
		except:
			ofilename = filename.split("\\")[-1]
		
		print(d, dct[d], sep="\t\t", end="\n")
		
		if all((width, height)):
			#debug partparameters:('c:\\downloads\\mytemp\\', 0, 'd:\\multimedia\\video\\serials_europe\\Viraji_sudby_Rus\\Viraji_sudby_01s01e.mp4', 268, 640, 360, 'Viraji_sudby_01s01e_001p.mp4')
			cmd_str.append("cmd /c ffmpeg -ss %d -y -i %s -to %d -threads 2 -c:v copy -threads 2 -c:a copy %s" % (d, filename, dct[d], ofilename))
			write_log("debug partparameters", str((path_for_queue, d, filename, dct[d], width, height, ofilename )))
		elif all((not width, not height)):
			cmd_str.append("cmd /c ffmpeg -ss %d -y -i %s -to %d -threads 2 -c:v copy -threads 2 -c:a copy %s" % (d, filename, dct[d], ofilename))
			write_log("debug partparameters", str((path_for_queue, d, filename, dct[d], ofilename )))

	if cmd_str:
		for cs in cmd_str:
			print(cs)
			

	'''
	if all((dct, is_Trim)):
		for d in dct:
			cnt += 1

			year_regex = re.compile(r"(\([\d+]{4}\))", re.M)

			seas_regex = re.compile(r"(_[\d+]{2,4}s[\d+]{2}e|_[\d+]{2,4}[\d+]{2}s?([\d+]{2}p))", re.M) #se_%~pa #sep_%~pa

			if any((year_regex.findall(filename.split("\\")[-1]), seas_regex.findall(filename.split("\\")[-1]))):
				ofilename = filename.split("\\")[-1].split(".")[0] + "".join(["_", one_to_double(cnt),"p"])+ext #for_big_films
			else:
				break

			ofilename = "".join([path_to_done, ofilename]) #job_in_project_folder

			if d == framecount: #test_from_here
				break

			if not ofilename:
				continue

			is_error = False

			try:
				if is_Sound and all((is_Scale, resized, width, height)): #is_Sound=True, is_Scale=True
					cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=%d:%d\" -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, d, filename, dct[d], width, height, ofilename)) #change_scale(vf)
				if is_Sound and all((is_Scale, not resized)): #is_Sound=True, is_Scale=True(resized)
					cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, d, filename, dct[d], ofilename)) #normal_scale(vf)
				if is_Sound and not is_Scale: #is_Sound=True, is_Scale=False
					cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, d, filename, dct[d], ofilename)) #no_change_scale(vf)
				if not is_Sound and all((is_Scale, resized, width, height)): #is_Sound=False, is_Scale=True
					cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=%d:%d\" -threads 2 -c:a copy %s" % (path_for_queue, d, filename, dct[d], width, height, ofilename)) #change_scale(vf)
				if not is_Sound and all((is_Scale, not resized)): #is_Sound=False, is_Scale=True(resized)
					cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a copy %s" % (path_for_queue, d, filename, dct[d], ofilename)) #normal_scale(vf)
				if not is_Sound and not is_Scale: #is_Sound=False, is_Scale=False
					cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a copy %s" % (path_for_queue, d, filename, dct[d], ofilename)) #no_change_scale(vf)

				if all((cmd_str, width, height)) and int(d) <= framecount:
					write_log("debug partparameters", str((path_for_queue, d, filename, dct[d], width, height, ofilename)))
				elif all((cmd_str, not width, not height)) and int(d) <= framecount:
					write_log("debug partparameters", str((path_for_queue, d, filename, dct[d], ofilename)))
			except BaseException as e:
				write_log("debug ffmpeg[error]", str(e))

				is_error = True

			finally:
				if is_error:
					break

		for cs in cmd_str:
			print(cs)

	elif any((not dct, not is_Trim)):
		print("Skip one part")
	'''
	
	'''
	if is_Trim == True: #len(dl) >= 2
		#generate_parts_to_command_line's(is_Trim=True)
		for d in dct: #for v in range(len(dl)): #-1?
			cnt += 1
			#print(c[v], b, one_to_double(cnt))

			year_regex = re.compile(r"(\([\d+]{4}\))", re.M)

			seas_regex = re.compile(r"(_[\d+]{2,4}s[\d+]{2}e|_[\d+]{2,4}[\d+]{2}s?([\d+]{2}p))", re.M) #se_%~pa #sep_%~pa

			if any((year_regex.findall(filename.split("\\")[-1]), seas_regex.findall(filename.split("\\")[-1]))):
				ofilename = filename.split("\\")[-1].split(".")[0] + "".join(["_", one_to_double(cnt),"p"])+ext #for_big_films
			else:
				break

			ofilename = "".join([path_to_done, ofilename]) #job_in_project_folder

			if d == framecount: #test_from_here
				break

			if not ofilename:
				continue

			#dl[v] -> d #tp -> d[dct]

			if is_Sound and all((is_Scale, resized, width, height)): #is_Sound=True, is_Scale=True
				cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=%d:%d\" -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, d, filename, dct[d], width, height, ofilename)) #change_scale(vf)
			if is_Sound and all((is_Scale, not resized)): #is_Sound=True, is_Scale=True(resized)
				cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, d, filename, dct[d], ofilename)) #normal_scale(vf)
			if is_Sound and not is_Scale: #is_Sound=True, is_Scale=False
				cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, d, filename, dct[d], ofilename)) #no_change_scale(vf)
			if not is_Sound and all((is_Scale, resized, width, height)): #is_Sound=False, is_Scale=True
				cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=%d:%d\" -threads 2 -c:a copy %s" % (path_for_queue, d, filename, dct[d], width, height, ofilename)) #change_scale(vf)
			if not is_Sound and all((is_Scale, not resized)): #is_Sound=False, is_Scale=True(resized)
				cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a copy %s" % (path_for_queue, d, filename, dct[d], ofilename)) #normal_scale(vf)
			if not is_Sound and not is_Scale: #is_Sound=False, is_Scale=False
				cmd_str.append("%sffmpeg -ss %d -y -i %s -to %d -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a copy %s" % (path_for_queue, d, filename, dct[d], ofilename)) #no_change_scale(vf)

			if all((cmd_str, width, height)) and int(d) < framecount:
				write_log("debug partparameters", str((path_for_queue, d, filename, dct[d], width, height, ofilename)))
			elif all((cmd_str, not width, not height)) and int(d) < framecount:
				write_log("debug partparameters", str((path_for_queue, d, filename, dct[d], ofilename)))
	elif is_Trim == False: #len(dl) == 1
		cnt += 1

		year_regex = re.compile(r"(\([\d+]{4}\))", re.M)

		seas_regex = re.compile(r"(_[\d+]{2,4}s[\d+]{2}e|_[\d+]{2,4}s[\d+]{2}e?([\d+]{2}p))", re.M)

		if any((year_regex.findall(filename.split("\\")[-1]), seas_regex.findall(filename.split("\\")[-1]))):
			ofilename = filename.split("\\")[-1].split(".")[0] + "".join(["_", one_to_double(cnt),"p"])+ext #for_big_films

		ofilename = "".join([path_to_done, ofilename]) #job_in_project_folder	

		if is_Sound and all((is_Scale, resized, width, height)): #is_Sound=True, is_Scale=True
			cmd_str.append("%sffmpeg -y -i %s -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=%d:%d\" -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, filename, width, height, ofilename))
		if is_Sound and all((is_Scale, not resized)): #is_Sound=True, is_Scale=True(resized)
			cmd_str.append("%sffmpeg -y -i %s -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, filename, ofilename)) #normal_scale(vf)
		if is_Sound and not is_Scale: #is_Sound=True, is_Scale=False
			cmd_str.append("%sffmpeg -y -i %s -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" %s" % (path_for_queue, filename, ofilename)) #no_change_scale(vf)
		if not is_Sound and all((is_Scale, resized, width, height)): #is_Sound=False, is_Scale=True
			cmd_str.append("%sffmpeg -y -i %s -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=%d:%d\" -threads 2 -c:a copy %s" % (path_for_queue, filename, width, height, ofilename)) #change_scale(vf)
		if not is_Sound and all((is_Scale, not resized)): #is_Sound=False, is_Scale=True(resized)
			cmd_str.append("%sffmpeg -y -i %s -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a copy %s" % (path_for_queue, filename, ofilename)) #normal_scale(vf)
		if not is_Sound and not is_Scale: #is_Sound=False, is_Scale=False
			cmd_str.append("%sffmpeg -y -i %s -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a copy %s" % (path_for_queue, filename, ofilename)) #no_change_scale(vf)
	'''

	return cmd_str #debug(null_data)

def walk(dr, files_template=""):
	"""Рекурсивный поиск файлов в пути"""

	# -- default --
	if not files_template:
		return
	else:
		ext_regex = files_template

	#check_and_test_this_block
	try:
		for name in os.listdir(dr):
			path = os.path.join(dr, name)
			if all((os.path.isfile(path), ext_regex.findall(path))):
				yield path
			else:
				yield from walk(path, ext_regex)

	except BaseException as e:
		return f'Error as {str(e)}'

#one_folder("c:\\downloads\\", re.compile(r"(?:(zip))$")) #one_folder #hide_regex(test_logic)
#one_folder("c:\\downloads\\new\\", video_regex)
def one_folder(folder, files_template):
	files = []
	files = ["".join([folder, lf.strip()]) for lf in os.listdir(folder) if files_template.findall(lf.split("\\")[-1]) and os.path.isfile("".join([folder, lf.strip()])) and any((lf.split("\\")[-1].startswith(lf.split("\\")[-1].capitalize()), lf.split("\\")[-1].find(lf.split("\\")[-1]) == 0))]

	return files #['c:\\downloads\\Current_BacthConverter.zip', ...] #capitalize #Abc... #find ~ findall(regex)

#sub_folder("c:\\downloads\\combine\\", re.compile(r"(?:(zip))$")) #sub_folder #hide_regex(test_logic)
def sub_folder(folder, files_template):
	files = []
	files = [lf.strip() for lf in walk(folder, files_template) if files_template.findall(lf.split("\\")[-1]) and os.path.isfile(lf) and any((lf.split("\\")[-1].startswith(lf.split("\\")[-1].capitalize()), lf.split("\\")[-1].find(lf.split("\\")[-1]) == 0))]

	return files #['c:\\downloads\\combine\\Archive\\Adobe_Photoshop_CC_2019.zip', ...] #capitalize #Abc... #find ~ findall(regex)

#def(c[v], c[v+1])
"""
0 479 01
479 958 02
958 1437 03
1437 1916 04
1916 2395 05
2395 2874 06
2874 3353 07
3353 3832 08
3832 4311 09
4311 4790 10
4790 5269 11
5269 5748 12
5748 6227 13
6227 6706 14
6706 7185 15
7185 7664 16
7664 8143 17
"""

#trim_time(c[v], b)
"""
0 479 01
479 479 02
958 479 03
1437 479 04
1916 479 05
2395 479 06
2874 479 07
3353 479 08
3832 479 09
4311 479 10
4790 479 11
5269 479 12
5748 479 13
6227 479 14
6706 479 15
7185 479 16
7664 479 17
"""

#ffmpeg -y -i input.ext -map_metadata -1 -threads 2 -c:v libx264 -vf "trim=%d:%d,scale=%d:%d" -c:a aac -af "dynaudnorm" output_01s01eZZp.ext

#'''
#multiple_jobs(need_look_like_"hello_world_01s01e"_template's)
filter_list = []

def my_args():

	try:
		tmp = [str(sys.argv[i]) for i in range(0, len(sys.argv))]
	except:
		tmp = []
	finally:
		if len(tmp) == 1:
			tmp = []

	return tmp

filter_list = my_args()

short_filter = ""

is_regex_status = False

short_filter = "|".join(filter_list)

try:
	print(short_filter.count("|"), filter_list[1:]) #hide(-1) #debug(count)
except:
	print("no index")
else:
	if short_filter.count("|") - 1 == 0:
		is_regex_status = False
	elif short_filter.count("|") - 1 > 0:
		is_regex_status = True

"""
$ python video_resize.py test test2
2 ['test', 'test2']

$ python video_resize.py test
1 ['test']

$ python video_resize.py
0 []
"""

"""
[] - no filter
["sound_normalize.py", "filter"] #test_one_filter
"""

reg_string = ""

if is_regex_status == True:
	reg_string = re.compile(r"(%s)(.*)(?:(.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2))$" % short_filter, re.M) #Matched_case #Ignore_case
else:
	reg_string = ""

#print(filter_list[1:][0])

# --- video_extentions ---

try:
	my_filter = "|".join(filter_list[1:])
	video_regex = re.compile(r"(%s)(.*)(?:(.avi|.mkv|.asf|.wmv|.mp4|.3gp|.vro|.mpeg|.ts|.tp|.trp|.mov|.flv|.vob|.svi|.m2ts|.mts|.divx|.webm|^.dmf|^.dmfr|^.filepart|^.aria2))$" % my_filter, re.M) #match_by_filter
except:
	video_regex = re.compile(r"(.*)(?:(.avi|.mkv|.asf|.wmv|.mp4|.3gp|.vro|.mpeg|.ts|.tp|.trp|.mov|.flv|.vob|.svi|.m2ts|.mts|.divx|.webm|^.dmf|^.dmfr|^.filepart|^.aria2))$", re.I) #ignorecase_by_anyfile

video_ext = sorted(["avi", "mkv", "mov", "flv", "vob", "webm", "wmv", "mp4"])

#wh = width_height()

lf = lf2 = lf3 = []

lfiles = []

#cdrive = ddrive = 0

try:
	with ThreadPoolExecutor(max_workers=ccount) as e:
		lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex) #local #combine
		nlf = e.submit(sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex) #nlocal #serialy
		nlf2 = e.submit(sub_folder, "d:\\multimedia\\video\\serials_europe\\", video_regex) #nlocal #serialy_rus
		nlf3 = e.submit(sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex) #nlocal #filmy
		nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) #nlocal #filmy(animated)

	lfiles = lf.result()
	lfiles += nlf.result()
	lfiles += nlf2.result()
	lfiles += nlf3.result()
	lfiles += nlf4.result()

	cdrive, ddrive = 1, 1

except:
	with ThreadPoolExecutor(max_workers=ccount) as e:
		lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex) #local #combine

	lfiles = lf.result()

	cdrive, ddrive = 1, 0

finally:
	if not lfiles:
		print("No data for video resolution")
		exit()

ffiles = fullfilenames = set()

#ffiles - unique_filenames
#fullfilenames - find_all_files
with unique_semaphore:
	for lf in lfiles:

		if any((not lf, not lfiles)):
			break

		fname = lf.split("\\")[-1]

		if not fname in ffiles:
			ffiles.add(fname)
			fullfilenames.add(lf)

		#elif fname in ffiles:
			#fullfilenames.add(lf)

if len(ffiles) == len(fullfilenames) and ffiles:
	print("Найдено одинковое количество файлов без повторений")	
if len(ffiles) != len(fullfilenames) and ffiles:
	print("Найдены файлы с повторениями их разница %d" % abs(len(fullfilenames)-len(ffiles)))

	if ffiles:
		lfiles = sorted(list(fullfilenames), reverse=False)

		if not isinstance(lfiles, list):
			lfiles = list(lfiles) #stay_unique_files
	
#'''

# --- test ---
#"""
def parts_to_rejoin(filename):

	if not filename:
		return

	try:
		fname = filename.split("\\")[-1]
	except:
		fname = ""

	wh = width_height(filename=filename) #"C:\\Downloads\\Combine\\Original\\Backup\\Bolshoy_skachyok_01s11e.mp4"

	try:
		len_video = wh.get_length(filename=filename) #"C:\\Downloads\\Combine\\Original\\Backup\\Bolshoy_skachyok_01s11e.mp4"
	except BaseException as e:
		len_video = 0
		print("Video length error!!! [%s]" % fname)
		write_log("debug video[lengtherror]", "[%s] [%s]" % (str(e), fname))
	finally: #else:
		print("Video length ok! [%d] [%s]" % (len_video, fname))
		write_log("debug video[length|file]", "[%d] [%s]" % (len_video, fname))

	#width, height, resized = wh.get_width_height(filename=lf, is_calc=True) #"C:\\Downloads\\Combine\\Original\\Backup\\Bolshoy_skachyok_01s11e.mp4"

	del wh

	#is_Sound=True, is_Scale=True #1(sound_normalize, resize)
	#is_Sound=True, is_Scale=False #2(sound_normalize, no_resize)
	#is_Sound=False, is_Scale=True #3(no_sound, resize)
	#is_Sound=False, is_Scale=False #4(no_sound, no_resize)

	#filter_list

	'''
	open(path_for_queue + "trimmer.cmd", "w", encoding="utf-8").close()

	#ffmpeg_command_line
	for cs in setup_parts(fcount=len_video, filename=filename, ext=".mp4", is_Sound=False, is_Scale=True): #get_filename_from_sys_argv[1] #is_Sound(False)~copy #is_Scale(True)~rescale

		with open(path_for_queue + "trimmer.cmd", "a", encoding="utf-8") as spf:
			spf.writelines("%s\n" % str(cs))
	'''				

	is_error = False

	#run_command_line
	for cs in setup_parts(fcount=len_video, filename=filename, ext=".mp4", is_Sound=False, is_Scale=True): #get_filename_from_sys_argv[1] #is_Sound(False)~copy #is_Scale(True)~rescale
	
		print(" ".join(cs))

		#if cs:
			#write_log("debug [cmd/length/filename]", "cmd: %s, length: %d, file is: %s" % (str(cs), len_video, str(filename)))

		"""
		p = os.system(cs)

		if p != 0:
			write_log("debug run[error]", "Ошибка запуска скрипта для %s" % filename)
			is_error = True
			break
		"""

	if all((not is_error, fname)):
		ready_file(fname)

	"""
	try:
		project_list = os.listdir(path_for_done)
	except:
		project_list = []

	mp4_count = mp4_files = []

	if ".mp4" in project_list:
		mp4_count =[pl.strip() for pl in project_list if ".mp4" in pl]
		mp4_files =["".join([path_for_done, pl]).strip() for mc in mp4_count if os.path.exists("".join([path_for_done, pl]))]

		if len(mp4_count) == len(mp4_files):
			print("Все файлы нашлись")
		elif len(mp4_count) != len(mp4_files):
			print("Не все файлы нашлись или ошибка")

		print("Найдено %d готовых файлов" % len(mp4_count))

		if mp4_count:
			with unique_semaphore:
				for mc in mp4_count:
					print(mc) #console

	if not mp4_count:
		print("Нет готовых файлов в папке")
	"""

	"""
	if mp4_files:

		temp = mp4_files

		try:
			if os.path.exists(mp4_files[-1]) and len(mp4_files) > 1:
				os.remove(mp4_files[-1]) #delete_last_file(test/debug)_from_directory
				temp.remove(mp4_files[-1]) #mp4_files.pop() #delete_last_file(test/debug)_from_list
		except:
			pass
		else:
			if len(temp) != len(mp4_files) and temp:
				mp4_files = sorted(temp, reverse=False)

		with unique_semaphore:
			for mf in mp4_files:

				if any((not mf, not mp4_files)):
					break

				try:
					fname = mf.split("\\")[-1]
				except:
					fname = ""
	
				#print(mf) #logging
				if fname:
					ready_file(fname) #dialog
	"""

#"""

if lfiles:
	with unique_semaphore:
		for lf in lfiles:

			if any((not lf, not lfiles)):
				break

			if not os.path.exists(lf):
				continue

			try:
				parts_to_rejoin(filename=lf) #test_for_find_files(debug) #without_move
			except BaseException as e:
				print("Ошибка при обработке. [%s]" % str(e))
				continue
elif not lfiles:
	print("No files. Programm exited")

if job_count:

	MT = MyTime()
	MT.sleep_with_count(4) #240s ~ 4min
	del MT

write_log("debug end", str(datetime.now()))

# --- trimmer.cmd(only_trim) / path_by_regex_find -> c:\downloads\new (d:\mutlimedia\video\...) (trimed/result_by_fspace);