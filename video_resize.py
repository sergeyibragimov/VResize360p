# -*- coding: utf-8 -*-

# --- manual ---

# PyCharm/Spyder(anaconda) (Оптимизировать и уменьшить код, для анализа)
# "удалить" лишние комментарии, чтобы был чистый код

# optimize_days.py / scprle.py / video_trimmer2.py

# threadsing vs asyncio

# Проверить процедуры, классы, алгоритмы и т.п. которые можно убрать(почистить)

# from contextlib import contextmanager
# from os import getcwd # cpu_count # текущая папка # cpu_count
# from random import randint
# from tempfile import NamedTemporaryFile # pip install --user tempfile
# import argparse  # system # sys.argv -> argparse
# import gevent.monkey # pip install --user gevent # is_async(debug)
# import io
# import multiprocessing
from PIL import (
	Image,
	ImageDraw,
	ImageFont,
)  # image, text_to_image, fontfamily # pip install --user Pillow
from concurrent.futures import ThreadPoolExecutor  # Thread by pool # man+ / youtube
from datetime import datetime, timezone  # datetime
from functools import reduce
from getmac import get_mac_address  # pip install --user getmac # mac_tools
from infi.systray import (
	SysTrayIcon,
)  # systray(notify) for task bar # pip install --user infi.systray
from mac_vendor_lookup import (
	MacLookup,
)  # pip install --user mac_vendor_lookup # MacLookup().lookup("cc:32:e5:59:ae:12")
from psutil import (
	cpu_count,
)  # viirtual_memory # pip install --user psutil # psutil (process and system utilities)
from shutil import (
	disk_usage,
	copy,
	move,
)  # файлы # usage(total=16388190208, used=16144154624, free=244035584)
from subprocess import (
	run,
)  # TimeoutExpired, check_output, Popen, call, PIPE, STDOUT # Работа с процессами # console shell=["True", "False"]
from threading import Semaphore  # # Thread # Barrier # работа с потоками # mutli_async
from time import (
	time,
	sleep,
)  # ctime, perf_counter, strftime, localtime  # время-задержка
from win10toast import (
	ToastNotifier,
)  # An easy-to-use Python library for displaying Windows 10 Toast Notifications
import asyncio  # TaskGroup(3.11+)
import ctypes
import json  # JSON (словарь)
import logging  # журналирование и отладка
import matplotlib.pyplot as plt  # import matplotlib
import ntplib  # pip install --user ntplib # server time
import os  # система
import psutil
import pyttsx3  # files_dict
import re  # regular_expression # .*(\?|$)
import socket  # socket_commands
import sqlite3 as sql  # sqlite db-api
import sys  # system
import xml.etree.ElementTree as xml  # ?pip
import zipfile  # zip archive # backup(job)/after(del/if_done) # UserWarning: Duplicate name

# Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.
# Back, Cursor # Fore.color, Back.color # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE # pip install --user colorama
from colorama import Fore, Style, init

# debug_modules
exit()

# mklink /h videoresize.py video_resize.py

start = time()

files_count: int = 0

# abspath_or_realpath
basedir: str = os.path.dirname(
	os.path.abspath(__file__)
).lower()  # folder_where_run_script
script_path: str = os.path.dirname(
	os.path.realpath(__file__)
).lower()  # is_system_older

dletter: str = "".join(
	[basedir.split("\\")[0], "\\"]
)  # "".join(script_path[0:5]) if script_path else "".join(os.getcwd()[0:5])

# --- path's ---
path_for_queue: str = r"d:\\downloads\\mytemp\\"
path_to_done: str = "%sdownloads\\list\\" % dletter  # "c:\\downloads\\" # ready_folder

# go_in_project_folder
os.chdir(path_for_queue)

try:
	assert os.path.exists(path_to_done), ""
except AssertionError:
	try:
		os.mkdir(path_to_done)
	except:
		exit()  # path_to_done: str = "c:\\downloads\\"

# @folder_with_jobs
path_for_folder1: str = "%sdownloads\\new\\" % dletter
# path_for_folder1: str = str("e:\\multimedia\\video\\").title() # (serials|kino|tvshow)(\?|$) # "c:\\downloads\\new\\"
# path_for_folder1: str = str("e:\\multimedia\\video\\serials_europe\\").title()
# path_for_folder1: str = str("e:\\multimedia\\video\\serials_conv\\").title()
# path_for_folder1: str = str("e:\\multimedia\\video\\").title()

# @download_source_and_segments
path_for_segments: str = (
	"%sdownloads\\mytemp\\segments\\" % dletter
)  # for_m3u8(ts_segments)
copy_src: str = "%sdownloads\\combine\\original\\tvseries\\" % dletter
copy_src2: str = "%sdownloads\\combine\\original\\bigfilms\\" % dletter

# logging(start)
log_base: str = "%s\\video_resize.json" % script_path  # main_debug(json)
log_print: str = "%s\\resize.log" % script_path
log_file: str = "%s\\videoresize.log" % script_path  # main_debug(logging)

try:
	assert os.path.exists(path_for_segments), ""
except AssertionError:
	os.mkdir(path_for_segments)

try:
	assert os.path.exists(copy_src), ""
except AssertionError:
	os.mkdir(copy_src)

try:
	assert os.path.exists(copy_src2), ""
except AssertionError:
	os.mkdir(copy_src2)

if not "mytemp" in basedir:
	basedir: str = "%sdownloads\\mytemp\\" % dletter

# logging.basicConfig(level=logging.INFO)

# @logging
# with_encoding # utf-8 -> cp1251
# filename / lineno / name / levelname / message / asctime # save_logging_manuals

open(log_file, "w", encoding="utf-8").close()

# '''
try:
	dsize: int = disk_usage(r"%s" % dletter).free  # "c:\\"
	assert dsize, ""
except AssertionError:
	logging.basicConfig(
		format="%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s",
		level=logging.INFO,
	)  # no_file
finally:
	if dsize // (1024**2) > 0:  # any_Mb # debug
		logging.basicConfig(
			handlers=[logging.FileHandler(log_file, "w", "cp1251")],
			format="%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s",
			level=logging.INFO,
		)
	else:
		logging.basicConfig(
			format="%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s",
			level=logging.INFO,
		)  # no_file
# '''
# logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s',	level=logging.INFO) # no_file # no_file # debug

logging.info(f"@start {str(datetime.now())}")

logging.info("%s" % ";".join([basedir, script_path]))

mytime: dict = {
	"jobtime": [9, 18, 5],
	"dinnertime": [12, 14],
	"sleeptime": [0, 8],
	"anytime": [True],
}  # sleep_time_less_hour # debug

# logging...("debug {variable|procedure}") -> logging...("@{variable|procedure}")
# IntelliJ(PyCharm default font name)


"""
@contextmanager
def atomic_writes(path, mode="w", encoding="utf-8"):
	mode = mode if mode == "wb" else "w"

	temp_file = NamedTemporaryFile(mode, encoding=encoding, delete=False)

	try:
		yield temp_file
	except Exception as e:
		temp_file.close()
		os.unlink(temp_file.name)
		print(f"Ошибка {e}!")
	else:
		temp_file.close()

		try:
			os.rename(temp_file.name, path)
		except OSError as e:
			os.unlink(temp_file.name)
			print(f"Ошибка {e}!")
"""


# 640x360 -> 1280x720 -> 1920x1080 # 16/9(hd)

# @16/9(hd) # 8/16
async def hd_generate(
	from_w: int = 640, from_h: int = 360, to_max: int = 1920, bit: int = 8
) -> list:  # 5 # 1920x1080 # 2500- > 1920
	scales: list = []

	"""
	try:
		to_max = max(from_w, from_h) * 4
		assert bool(to_max <= 1920), "" # "Больше значения по умолчанию %d" % to_max
	except AssertionError:
		logging.warning("Больше значения по умолчанию %d" % to_max)
		to_max -= (to_max - 1920) # to_max = 1920
		# raise err
	"""
	to_max = max(from_w, from_h) * 4

	while to_max > 1920:
		to_max -= to_max - 1920

	try:
		# w <= to_max, h <= to_max
		scales = list(
			set(
				[
					"x".join([str(w), str(h)])
					for w in range(from_w, to_max, bit)
					for h in range(from_h, to_max, bit)
					if w / h == (16 / 9) and all((h, w >= h))
				]
			)
		)
	except BaseException as e:  # if_error
		scales = []
		logging.error("Ошибка hd маштабов @hd_generate/scales [%s]" % str(e))
	finally:
		if not scales:
			scales.append("x".join([str(from_w), str(from_h)]))

		scales.sort(reverse=False)
		logging.info(";".join(scales))  # print(scales) # logging_or_print_scales(;)

	return scales


# @hd_list # ?


# @4/3(sd) # 8/16
async def sd_generate(
	from_w: int = 640, from_h: int = 480, to_max: int = 1920, bit: int = 8
) -> list:  # 5 # 1920x1440 # 2500 -> 1920

	scales: list = []

	"""
	try:
		to_max = max(from_w, from_h) * 4
		assert bool(to_max <= 1920), "" # "Больше значения по умолчанию %d" % to_max
	except AssertionError:
		logging.warning("Больше значения по умолчанию %d" % to_max)
		to_max -= (to_max - 1920) # to_max = 1920
		# raise err
	"""
	to_max = max(from_w, from_h) * 4

	while to_max > 1920:
		to_max -= to_max - 1920

	try:
		# w <= to_max, h <= to_max
		scales = list(
			set(
				[
					"x".join([str(w), str(h)])
					for w in range(from_w, to_max, bit)
					for h in range(from_h, to_max, bit)
					if w / h == (4 / 3) and all((h, w >= h))
				]
			)
		)
	except BaseException as e:  # is_error
		scales = []
		logging.error("Ошибка sd маштабов @sd_generate/scales [%s]" % str(e))
	finally:
		if not scales:
			scales.append("x".join([str(from_w), str(from_h)]))

		scales.sort(reverse=False)
		logging.info(",".join(scales))  # print(scales) # logging_or_print_scales(,)

	return scales


# @sd_list # ?


# antoher_aspect_ratio(is_no_sd/is_no_hd) # 8/16
async def ar_generate(
	from_w: int = 640, from_h: int = 360
) -> list:  # to_max: int = 2500, bit: int = 8 # 1920x1080
	"""
	1.0, 1.5555555555555556, 1.6, 1.66, 1.75, 1.85, 2.0,
	2.2, 2.35, 2.39, 2.4, 2.55, 2.76, 2.3333333333333335
	"""

	list_ar: list = []
	# list_ar: list = [1/1, 14/9, 16/10, 1.66/1, 1.75/1, 1.85/1, 2/1]
	# list_ar += [2.2/1, 2.35/1, 2.39/1, 2.4/1, 2.55/1, 2.76/1, 21/9]
	# list_ar += [16/9, 4/3] # hd/sd

	darbase_dict: dict = {}

	try:
		with open(dar_base, encoding="utf-8") as dbf:
			darbase_dict = json.load(dbf)
	except:
		darbase_dict = {}

	dar_list_ar: list = [*darbase_dict] if darbase_dict else []

	if dar_list_ar:
		list_ar.extend(dar_list_ar)  # add_from_darbase(+additional_dar_data)
		# list_ar.extend(list(set(list_ar) ^ set(dar_list_ar)) # compare_different(is_unique)

	list_ar = list(set(list_ar))
	list_ar.sort(reverse=False)

	scales: list = []
	scales_result: list = []  # width
	# scales_result2: list = [] # height

	"""
	try:
		to_max = max(from_w, from_h) * 4
		assert bool(to_max <= 1920), "Больше значения по умолчанию"
	except AssertionError as err:
		logging.warning("Больше значения по умолчанию %d" % to_max)
		to_max -= (to_max - 1920)
		raise err
	"""
	to_max = max(from_w, from_h) * 4

	while to_max > 1920:
		to_max -= to_max - 1920

	for la in filter(lambda x: x, tuple(list_ar)):

		try:
			assert list_ar, ""
		except AssertionError:  # if_null
			break

		try:
			first, second = from_h * la, from_h  # width # from_w, from_w / la # height
		except:
			first = second = 0
		# else:
		# if all((to_max, any((first > to_max, second > to_max)))): # limit_width(height)_by_max
		# continue

		if not isinstance(first, int):
			first = int(first)
		if first % 2 != 0:
			first -= 1

		if not isinstance(second, int):
			second = int(second)
		if second % 2 != 0:
			second -= 1

		try:
			assert first and second, ""  # is_assert_debug
		except AssertionError:
			continue
		else:
			if all((first, second)):
				scales.append((first, second))  # add_all
			if all((from_w, from_h)) and not (from_w, from_h) in scales:
				scales.append((from_w, from_h))  # default_for_any

	# width*height / aspect_ratio
	try:
		# scales_result = list(set(["x".join([str(round(f, 3)), str(round(s, 3))]) for f, s in scales if all((f, s))])) # float_list(sep)
		scales_result = list(
			set(
				[
					"x".join([str(f), str(s), str(round(f / s, 3))])
					for f, s in scales
					if all((f, s))
				]
			)
		)  # str_list(width/height/ar)
	except BaseException as e:  # if_error
		scales_result = []
		logging.error(
			"Ошибка дополнительных маштабов @ar_generate/scales_result/ar [%s]" % str(e)
		)  # width/height
	finally:
		scales_result.sort(reverse=False)  # any_length

		scales = scales_result if scales_result else []  # null_or_some_data

		if scales:  # if_some_data
			logging.info(",".join(scales))  # list_by_separate(sep)

	return scales


# ffmpeg -y -i input -c:v libx264 -vf scale=640:-1 -c:a aac -af dynaudnorm output # stay_profile_high # stay_metadata
# use_by_default_manual(height % 2 == 0) # "720" >= 640

"""
import re

emails = input().split()

res = filter(lambda x: re.findall(r'^[\w]+@[\w]+.[\w]', x), emails)
print(*res)

"""

# ((1682355156 / 1000) // 60) % 60 ~ 19min
# time.time() * 1000 = ?ms (1682355745739.1763) ~ (1682355745739.1763 // 60) % 60 ~ 28min

dt = datetime.now()

# worktime monday-saturday(0-5) (00:00 - 18:00) / weekdays "saturday"-sunday(5-6) (00:00 - 18:00)
# is_zoomtime everyday (22:00 - 24:00)
if (
	dt.minute < 60
):  # any((dt.weekday() <= mytime["jobtime"][2], dt.weekday() > mytime["jobtime"][2]))
	# ishide_console_on_start

	is_error: bool = False

	kernel32 = ctypes.WinDLL("kernel32")
	user32 = ctypes.WinDLL("user32")

	SW_HIDE, SW_SHOW = 0, 6

	try:
		hWnd = kernel32.GetConsoleWindow()
		# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6) # console_popup_window # samples_for_window # show
		# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) # console_popup_window # samples_for_window # hide
	except BaseException as e:  # if_error
		is_error = True
		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
	finally:
		if is_error == False:
			if hWnd:
				if (
					dt.hour >= mytime["jobtime"][0]
				):  # mytime["jobtime"][0] <= dt.hour <= mytime["jobtime"][1] # hide_in_job_time
					user32.ShowWindow(hWnd, SW_HIDE)  # new

					# print(f"Приложение успешно свёрнуто в {str(dt)}")
					with open(
						basedir + "\\minimized_vr.pid", "w", encoding="utf-8"
					) as mpf:
						mpf.write(f"Приложение успешно свёрнуто в {str(dt)}")
				else:  # if_another_time
					user32.ShowWindow(hWnd, SW_SHOW)  # new

					# print(f"Приложение успешно разсвёрнуто в {str(dt)}")
					with open(
						basedir + "\\maximized_vr.pid", "w", encoding="utf-8"
					) as mpf:
						mpf.write(f"Приложение успешно разсвёрнуто в {str(dt)}")


init(autoreset=True)  # init text color's

job_count: int = 0

# --- CPU optimize ---
ccount: int = int(cpu_count())  # logical=True # False
unique_semaphore = Semaphore(ccount)

envdict = os.getenv.__globals__  # переменные_среды

# error_save_json
# '''
environ_file: str = "".join([path_for_queue, "environ.json"])
try:
	environ_dict = dict(envdict["environ"])
	assert environ_dict, ""
except AssertionError:  # if_null
	environ_dict = {}
	# raise err # logging.warning
except BaseException:  # if_error
	environ_dict = {}
finally:
	with open(environ_file, "w", encoding="utf-8") as eff:
		json.dump(
			environ_dict, eff, ensure_ascii=False, indent=4
		)  # environ_dict(some) / environ_dict(null)
# '''

# environ_block(windows) # debug(is_error)
userprofile: str = envdict["environ"][
	"userprofile"
].lower()  # os.getenv("USERPROFILE") # r"c:\\users\\sergey
programfiles: str = envdict["environ"][
	"programfiles"
].lower()  # os.getenv("PROGRAMFILES") # r"c:\\program files
# userdomain: str = envdict["environ"]["userdomain"].lower() # os.getenv("USERDOMAIN") # SERGEYPC # debug
# username: str = envdict["environ"]["username"].lower() # os.getenv("USERNAME") # Sergey # debug
# logonserver: str = envdict["environ"]["logonserver"].lower() # os.getenv("LOGONSERVER") # r"\\SERGEYPC" # debug

# allusersprofile # r"c:\\programdata
# appdata # r"c:\\users\\sergey\\appdata\\roaming
# asl.log # destination=file
# commonprogramfiles # r"c:\\program files\\common files
# commonprogramfiles(x86) # r"c:\\program files (x86)\\common files
# commonprogramw6432 # r"c:\\program files\\common files
# computername # sergey_pc
# comspec # r"c:\\windows\\system32\\cmd.exe
# email # r"c:\\users\\sergey\\appdata\\roaming\\the bat!
# fp_no_host_check # no

# popular_env
"""
# homedrive
# homepath
# localappdata
# 'logonserver
# number_of_processors
# 'os
# path
# pathext
# processor_architecture
# processor_identifier
# processor_level
# processor_revision
# programdata
# programfiles(x86)
# programw6432
# prompt
# psmodulepath
# public
# pycharm community edition
# sessionname
# systemdrive
# systemroot
# temp
# tmp
# userdomain
# userdomain_roamingprofile
# username
# windir
"""

# --- json's(+combine) ---
abr_base: str = "".join([path_for_queue, "abr.json"])  # abr_calc
backup_base: str = "".join([path_for_queue, "backup.json"])  # abr_calc
bitrated_base: str = "".join(
	[path_for_queue, "bitratebase.json"]
)  # optimal_vbr_and_abr # filename_1000_384.mp4
br_base: str = "".join([path_for_queue, "br.json"])  # (vbr/abr)_calc
cfilecmd_base: str = "".join(
	[path_for_queue, "cfcd.json"]
)  # Command line for job file + not optimized
copy_folders: str = r"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\current.lst"  # is_current_short_folders # +copy
dar_base: str = "".join([path_for_queue, "dar.json"])  # d(isplay)aspect_ratio
days_base: str = "".join([path_for_queue, "days_ago.json"])  # файлы до месяца(json)
desc_base: str = "".join([path_for_queue, "descriptions.json"])  # descriptions
desc_base_temp: str = "".join(
	[path_for_queue, "descriptions_temp.json"]
)  # descriptions(is_debug/is_manual)
error_base: str = "".join([path_for_queue, "error.json"])  # any_error_for_debug
filecmd_base2: str = "".join(
	[path_for_queue, "lfcd.json"]
)  # Command line for job file # last_jobs
filecmd_base: str = "".join(
	[path_for_queue, "fcd.json"]
)  # Command line for job file # current_jobs
files_by_days: str = "".join([path_for_queue, "days_ago.lst"])  # файлы до месяца(lst)
files_by_month: str = "".join(
	[path_for_queue, "month_forward.lst"]
)  # файлы от месяца(lst)
files_by_year: str = "".join([path_for_queue, "calc_year.lst"])  # файлы от года(lst)
foldcnt_base: str = "".join(
	[path_for_queue, "fcount.json"]
)  # папки и количество файлов(json)
fps_base: str = "".join([path_for_queue, "fps.json"])  # fps(frame_rates)
jobs_base: str = "".join([path_for_queue, "jobs.json"])  # ?
month_base: str = "".join(
	[path_for_queue, "month_forward.json"]
)  # файлы от месяца(json)
new_optimize_base: str = "".join(
	[path_for_queue, "neop.json"]
)  # new_or_optimize(is_learn)
padeji_base: str = "".join([path_for_queue, "padeji.json"])  # words_ends
par_base: str = "".join([path_for_queue, "par.json"])  # p(ixel)aspect_ratio
paths_base: str = "".join([path_for_queue, "sdpaths.json"])  # short_folder
sar_base: str = "".join([path_for_queue, "sar.json"])  # s(cale)aspect_ratio
sfilecmd_base: str = "".join(
	[path_for_queue, "sfcd.json"]
)  # Sorted for job file + joined
short_folders2: str = "".join(
	["c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\", "short.lst"]
)  # current_folders(copy)
short_folders: str = "".join([path_for_queue, "short.lst"])  # current_folders # +orig
short_text: str = "".join(
	["c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\", "short.txt"]
)  # current_folders(copy)
some_base: str = "".join([path_for_queue, "somebase.json"])  # filename + meta
soundtrack_base: str = "".join(
	[path_for_queue, "soundtrack.json"]
)  # popular_sound_track
soundtrack_tbase: str = "".join(
	[path_for_queue, "tsoundtrack.json"]
)  # temp_sound_track(debug_json)
std_base: str = "".join([path_for_queue, "std.json"])  # s(peed)/t(ime)/d(ata)
top_folder2: str = "".join(
	["c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\", "curr.lst"]
)  # eng(+rus).lst_to_update # debug(no_updates)
top_folder: str = "".join(
	["c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\", "cur_top.lst"]
)
trends_base: str = "".join([path_for_queue, "trends.json"])  # last_jobs # try_sort
twoday_base2: str = "".join(
	["c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\", "two_days.lst"]
)  # файлы за прошлый 2 дня
twoday_base: str = "".join([path_for_queue, "two_days.lst"])  # файлы за прошлый 2 дня
unique_base: str = "".join([path_for_queue, "unique_data.json"])  # meta_data
vbr_base: str = "".join([path_for_queue, "vbr.json"])  # vbr_calc
vr_files: str = "".join(
	[path_for_queue, "video_resize.lst"]
)  # files(files_from_video_resize.dir) # txt -> json
vr_folder: str = "".join(
	[path_for_queue, "video_resize.dir"]
)  # folders_with_files(length > 1) # txt -> json
year_base: str = "".join([path_for_queue, "calc_year.json"])  # файлы от года(json)


async def combine_br():  # abr + vbr(combine_equal_files)
	try:
		with open(abr_base, encoding="utf-8") as abf:
			abr_dict = json.load(abf)
	except:
		abr_dict = {}

	try:
		with open(vbr_base, encoding="utf-8") as vbf:
			vbr_dict = json.load(vbf)
	except:
		vbr_dict = {}

	# '''
	try:
		with open(some_base, encoding="utf-8") as sbf:
			somebase_dict = json.load(sbf)
	except:
		somebase_dict = {}
	else:
		somebase_dict = {
			k.strip(): v for k, v in somebase_dict.items() if len(v.split(":")) > 1
		}  # try_filter_by_new
	# '''

	with open(br_base, "w", encoding="utf-8") as bbf:
		json.dump({}, bbf, ensure_ascii=False, indent=4, sort_keys=True)

	br_dict: dict = {}

	# filename / vbr(abr) / "additional_param"
	if all((vbr_dict, abr_dict, somebase_dict)):
		# br_dict = {k: [v, v2, int(v3.split(":")[0]), int(v3.split(":")[1])] for k, v in vbr_dict.items() for k2, v2 in abr_dict.items() for k3, v3 in somebase_dict.items() if all((k, k2, k3, k == k2, k == k3)) and os.path.exists(k)} # len(v3.split(":")) > 1
		br_dict = {
			k: [v, v2]
			for k, v in vbr_dict.items()
			for k2, v2 in abr_dict.items()
			if all((k, k2, k == k2)) and os.path.exists(k)
		}  # len(v3.split(":")) > 1
	elif all((vbr_dict, abr_dict, not somebase_dict)):
		br_dict = {
			k: [v, v2, 0, 0]
			for k, v in vbr_dict.items()
			for k2, v2 in abr_dict.items()
			if all((k, k2, k == k2)) and os.path.exists(k)
		}

	# "filename_%s_%s.mp4" % (str(v), str(v2)) # debug

	try:
		with open(bitrated_base, encoding="utf-8") as bbf:
			bitrate_dict = json.load(bbf)
	except:
		bitrate_dict = {}

		with open(bitrated_base, "w", encoding="utf-8") as bbf:
			json.dump(bitrate_dict, bbf, ensure_ascii=False, indent=4, sort_keys=True)

	# full_path -> my_path
	# st = "d:\\multimedia\\video\\big_films\\1962\\Vzlyotnaya_polosa(1962).mp4"
	# print(st.replace("\\".join(st.split("\\")[:-1:]), "c:\\downloads")) # first(auto_src_path), second(manual_dst_path)
	# print("".join([st.replace("\\".join(st.split("\\")[:-1:]), "c:\\downloads").split(".")[0]]))

	# converter_to_optimal_vbr+abr
	# vbr # -b:v 1000K -maxrate 1000K -bufsize 2000K # abr # -b:a 192k

	# regenerate_every_run  # debug(path/bitrate)
	if all((br_dict, somebase_dict)):  # new_jobs # +vbr/abr
		# if all((v[2], v[3])): # +width/height
		# bitrate_dict = {k.strip(): "cmd /c c:\\downloads\\mytemp\\ffmpeg -hide_banner -y -i \"%s\" -threads 2 -c:v libx264 -b:v %dK -maxrate %dK -bufsize %dK -vf \"scale=\"%d:%d\"\" -threads 2 -c:a aac -b:a %dK \"%s\"" % (
		# k, v[0], v[0], v[0]*2, v[2], v[3], v[1], "".join([k.replace("\\".join(k.split("\\")[:-1:]), "c:\\downloads\\combine\\original").split(".")[0] + "_%s_%s%s" % (str(v[0]), str(v[1]), ".mp4")])) for k, v in br_dict.items()}

		bitrate_dict = {
			k.strip(): 'cmd /c c:\\downloads\\mytemp\\ffmpeg -hide_banner -y -i "%s" -preset medium -threads 2 -c:v libx264 -b:v %dK -maxrate %dK -bufsize %dK -threads 2 -c:a aac -b:a %dK "%s"'
			% (
				k,
				v[0],
				v[0],
				v[0] * 2,
				v[1],
				"".join(
					[
						k.replace(
							"\\".join(k.split("\\")[:-1:]),
							"c:\\downloads\\combine\\original",
						).split(".")[0]
						+ "_%s_%s%s" % (str(v[0]), str(v[1]), ".mp4")
					]
				),
			)
			for k, v in br_dict.items()
		}
		bitrate_dict = {
			k.strip(): v
			for k, v in bitrate_dict.items()
			if os.path.exists(k) and k in [*somebase_dict]
		}  # check_exists # with_optimized_jobs(new)
	elif all((br_dict, not somebase_dict)):  # default # +vbr/abr
		bitrate_dict = {
			k.strip(): 'cmd /c c:\\downloads\\mytemp\\ffmpeg -hide_banner -y -i "%s" -preset medium -threads 2 -c:v libx264 -b:v %dK -maxrate %dK -bufsize %dK -threads 2 -c:a aac -b:a %dK "%s"'
			% (
				k,
				v[0],
				v[0],
				v[0] * 2,
				v[1],
				"".join(
					[
						k.replace(
							"\\".join(k.split("\\")[:-1:]),
							"c:\\downloads\\combine\\original",
						).split(".")[0]
						+ "_%s_%s%s" % (str(v[0]), str(v[1]), ".mp4")
					]
				),
			)
			for k, v in br_dict.items()
		}
		bitrate_dict = {
			k.strip(): v for k, v in bitrate_dict.items() if os.path.exists(k)
		}  # check_exists	# without_optimized_jobs(no_jobs)

	if bitrate_dict:
		with open(bitrated_base, "w", encoding="utf-8") as bbf:
			json.dump(bitrate_dict, bbf, ensure_ascii=False, indent=4, sort_keys=True)

	with open(br_base, "w", encoding="utf-8") as bbf:
		json.dump(br_dict, bbf, ensure_ascii=False, indent=4, sort_keys=True)


asyncio.run(combine_br())  # combine_br_for_unique_filenames # at_start


async def read_br():  # read_biitrate_base_for_equal_files
	try:
		with open(br_base, encoding="utf-8") as bbf:
			br_dict = json.load(bbf)
	except:
		br_dict = {}

		with open(br_base, "w", encoding="utf-8") as bbf:
			json.dump(br_dict, bbf, ensure_ascii=False, indent=4, sort_keys=True)

	return br_dict  # some/null


# psoundtrack.json?

# "convert": "".join([path_for_queue, "convert.lst"])

# {key_by_filename_without_ext:filename}
files_base: dict = {
	"backup": "".join([path_for_queue, "backup.lst"]),
	"current": "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\current.lst",
	"hours": "".join([path_for_queue, "hours.cfg"]),
	"timing": "".join([path_for_queue, "video_resize.xml"]),
	"lastjob": "".join([path_for_queue, "last.xml"]),
	"soundtrack": "".join([path_for_queue, "psoundtrack.lst"]),
	"stracks": "".join([path_for_queue, "soundtrack.lst"]),
	"trends": "".join([path_for_queue, "trends.lst"]),
}

"""
for _, v in files_base.items():
	try:
		assert os.path.exists(v), ""
	except AssertionError:
		open(v, "w").close()
	else:
		continue
"""

open(files_base["soundtrack"], "w", encoding="utf-8").close()

# ctme.hour # ctime.weekday()

# --- regex_codes ---
# seasyear = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))", re.M) # MatchCase # season_and_year(findall) # +additional(_[\d+]{2}p)
# big_film_regex = re.compile(r"\([\d+]{4}\)", re.M) # MatchCase # cinema(findall)

# Mesto_vstrechi_220124_00p # crop_filename_regex(_[\d+]{2}p) # 'Mesto_vstrechi_220124'

# IgnoreCase # short_filename_regex # short_year(sub)_regex # default_filter # (57)
crop_filename_regex = re.compile(
	r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)", re.I
)  # skip_additional(_[\d+]{2}p)
# crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)|_[\d+]{2}p))(.*)", re.I)
# template_for_seasonvar_filter(season_and_episode)(tv_series_only) # (2)
crop_filename_regex2 = re.compile(r"([sS]{1}[\d+]{1,2})\.([eE]{1}[\d+]{1,2})", re.I)

lang_regex = re.compile(
	r"_[A-Z]{1}[a-z]{2}$", re.M
)  # MatchCase # europe_language(find_all) # (6)

# .webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf

# MatchCase # find_files(findall)
video_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s[\d+]{2}e|\([\d+]{4}\)))(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap|^.srt))$",
	re.M,
)  # (38) # +additional(_[\d+]{2}p)
# IgnoreCase
video_ext_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s[\d+]{2}e|\([\d+]{4}\)))(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap|^.srt))$",
	re.I,
)  # (37) # +additional(_[\d+]{2}p)

# --- Overload process ---

# 5%
big_process: list = []
pid_process: list = []
skip_process: list = []

open("c:\\downloads\\mytemp\\overload.csv", "w", encoding="utf-8", newline="").close()

with open("c:\\downloads\\mytemp\\overload.csv", "a", newline="") as ocf:
	ocf.write("pid;proc_name\n")


# --- procedures ---

# ---
# Serials_conv_path = r"d:\multimedia\video\serials_conv\"
# serials_conv(reverse=True)
# dir /r/b/ad/od- "*.*" > eng.lst
# Serials_Europe_path = r"D:\Multimedia\Video\Serials_Europe\"
# serials_europe(reverse=True)
# dir /r/b/ad/od- "*.*" > rus.lst
# ---

# mp4 to m3u8(is_for_server)
# dc = {"file1": 2, "file2": 4, "file3": 3} # {"file1": 2, "file3": 3, "file2": 4}


# group_of_data # super
"""
async def group_by_age(people):
	result = {}
	for name, age in people:
		if age in result:
			result[age].append(name)
		else:
			result[age] = [name]
	return result
"""


async def dict_filter(dct: dict = {}, sort_index: int = -1) -> dict:  # 16

	try:
		assert dct, "Пустой словарь @dict_filter/dct"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Пустой словарь @dict_filter/dct")
		raise err
		return []
	except BaseException as e2:  # if_error
		logging.error("Пустой словарь @dict_filter/dct [%s]" % str(e2))
		return []

	dct_new: dict = {}
	lst_new: list = []  # default_list

	lst_new = list(
		set(
			[
				(k, v)
				for k, v in dct.items()
				if all((os.path.exists(k), k.split(".")[-1], k, v))
			]
		)
	)

	if all((lst_new, sort_index != -1)):
		lst_sort: list = []  # sorted_list

		try:
			len_tuple = len(lst_new[0])
		except:
			len_tuple = 0

		try:
			if len_tuple >= sort_index:
				lst_sort = sorted(
					lst_new, key=lambda lst: lst[sort_index]
				)  # sorted_tuple_list_by_num_field(logic)
		except:
			lst_sort = sorted(
				lst_new, key=lambda lst: lst[0]
			)  # sorted_tuple_list_by_first_field(error)

		dct_new = {
			k: v
			for ls in lst_sort
			for k, v in dct.items()
			if all((len(lst_new) > 0, ls[0].strip() == k.strip()))
		}  # sorted_dict_by_tuple(list)

	elif all((lst_new, sort_index == -1)):
		dct_new = {
			ls[0]: ls[1] for ls in lst_sort if all((len(lst_new) > 0, ls))
		}  # no_sorted_dict_by_tuple

	return dct_new  # any_result


# cl_filter = compare_list([1,1,2,3,4,5]) # True # cl_filter = compare_list([]) # False
async def compare_list(
	lst: list = [],
	is_le: bool = False,
	is_ge: bool = False,
	is_e: bool = False,
	is_ne: bool = False,
) -> bool:  # 1

	try:
		assert lst and isinstance(
			lst, list
		), "Пустой список или другой формат списка @compare_list/lst"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Пустой список или другой формат списка @compare_list/lst")
		raise err
		return False
	except BaseException as e3:  # if_error
		logging.error(
			"Пустой список и другой формат списка @compare_list/lst [%s]" % str(e3)
		)
		return False

	if is_le:
		return len(set(lst)) <= len(lst)  # True(if_less_or_equal) # LE
	if is_ge:
		return len(lst) >= len(set(lst))  # True(if_great_or_equal) # GE
	if is_e:
		return len(lst) == len(set(lst))  # True(if_equal) # E
	if is_ne:
		return len(lst) != len(set(lst))  # True(if_not_equal) # NE

	return len(set(lst)) <= len(lst)  # True(if_less_or_equal) # LE # default_result


async def calc_number_of_day(
	is_default: bool = True,
	day: int = 0,
	month: int = 0,
	year: int = 0,
	sleep_if: str = "",
	find_c3: int = 0,
	find_c4: int = 0,
) -> tuple:  # 4

	# calc_number_of_day
	if is_default:
		dt_calc = datetime.now()  # day / month / year

		dt_str = ".".join([str(dt_calc.day), str(dt_calc.month), str(dt_calc.year)])
	elif not is_default:
		dt_str = ".".join([str(day), str(month), str(year)])

	if all((sleep_if, dt_str == sleep_if, is_default == False)):
		sleep(2)

	c1, c2, c3, c4 = 0, 0, 0, 0

	# 10.09.1994 # 33.6.31.4
	# 1.4.2023 # 12.3.32.5

	sm = []

	for ds in filter(lambda x: x, tuple(dt_str)):
		try:
			if int(ds) > 0:
				sm.append(int(ds))
		except:
			continue
	else:  # is_no_break
		if len(sm) >= 0:
			is_day_calc = (
				"Число дня получено!" if sm else "Число дня неизвестно!"
			)  # is_no_lambda
			print(is_day_calc)

	calc1 = calc2 = False
	calc3 = calc4 = False

	c1 = sum(sm)
	if c1 >= 10:
		calc1 = True
		c2 = int(str(c1)[0]) + int(str(c1)[1])
		while c2 > 10:
			c2 = int(str(c1)[0]) + int(str(c1)[1])
			# c1 = int(c2) # str -> int
			# print(c1, c2, 1)
	elif c1 < 10:  # all((c1 < 10, not calc1)):
		c2 = int(str(c1))
		# print(c2, 2)
		calc2 = True

	c3 = (
		33 - int(str(dt_str.split(".")[0])[1]) * 2
		if dt_str.split(".")[0].startswith("0")
		else 33 - int(dt_str.split(".")[0])
	)  # is_no_lambda

	if c3 >= 10:
		calc3 = True
		c4 = int(str(c3)[0]) + int(str(c3)[1])
		while c4 > 10:
			c4 = int(str(c3)[0]) + int(str(c3)[1])
			# c3 = int(c4) # str -> int
			# print(c3, c4, 3)
	elif c3 < 10:  # all((c3 < 10, not calc3)):
		c4 = int(str(c3))
		# print(c4, 4)
		calc4 = True

	if (
		all((c3, find_c3 == c3))
		and all((c4, find_c4 == c4))
		and any((calc1, calc2, calc3, calc4))
	):
		print(c1, c2, c3, c4, dt_str, "from def")

	return (int(c1), int(c2), int(c3), int(c4), dt_str)


async def month_to_seasdays(month: int = 0, year: int = 0) -> tuple:

	try:
		assert (
			1 <= month <= 12
		), f"Неверный индекс месяца @month_to_seasdays/{month}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(f"Неверный индекс месяца @month_to_seasdays/{month}")
		raise err
		return ("", 0)
	except BaseException as e4:  # if_error
		logging.error("Неверный индекс месяца @month_to_seasdays/month [%s]" % str(e4))
		return ("", 0)

	seas: str = ""
	days: int = 0

	if month in [12, 1, 2]:
		if month == 12:
			days = 31
		elif month == 1:
			days = 31
		elif all((month == 2, year)):
			if year % 4 == 0:
				days = 29
			elif year % 4 != 0:
				days = 28
		elif all((month == 2, not year)):
			days = 28  # short_month
		seas = "Winter"

	elif month in [3, 4, 5]:
		if month == 3:
			days = 31
		elif month == 4:
			days = 30
		elif month == 5:
			days = 31
		seas = "Spring"

	elif month in [6, 7, 8]:
		if month == 6:
			days = 30
		elif month == 7:
			days = 31
		elif month == 8:
			days = 31
		seas = "Summer"

	elif month in [9, 10, 11]:
		if month == 9:
			days = 30
		elif month == 10:
			days = 31
		elif month == 11:
			days = 30
		seas = "Autumn"

	return (seas, days)


async def fromdaytohny():
	dt = datetime.today()
	ny = datetime(dt.year + 1, 1, 1)
	d = ny - dt

	try:
		mm, ss = divmod(d.seconds, 60)
		hh, mm = divmod(mm, 60)
	except:
		return ""
	else:
		return f"До нового года осталось {d.days} дней, {hh} час. {mm} мин. {ss} сек."
		# return last2str(maintxt="До нового года осталось", endtxt=f"{hh} час. {mm} мин. {ss} сек.", count=d.days, kw="ден")


async def date_to_week() -> dict:  # 2
	# Creating an dictionary with the return
	# value as keys and the day as the value
	# This is used to retrieve the day of the
	# week using the return value of the
	# isoweekday() function
	weekdays = {
		1: "Monday",
		2: "Tuesday",
		3: "Wednesday",
		4: "Thursday",
		5: "Friday",
		6: "Saturday",
		7: "Sunday",
	}

	try:
		# Getting current date using today()
		# function of the datetime class
		todays_date = datetime.today()

		try:
			mts = await month_to_seasdays(
				month=todays_date.month, year=todays_date.year
			)
		except:
			mts = ("", 0)

		try:
			cnod = await calc_number_of_day(
				day=todays_date.day, month=todays_date.month, year=todays_date.year
			)
		except:
			cnod = (0, 0, 0, 0, str(todays_date))

		# Using the isoweekday() function to
		# retrieve the day of the given date
		day = todays_date.isoweekday()
		# print("The date", todays_date, "falls on", weekdays[day])

		try:
			fdth = await fromdaytohny()
		except:
			fdth = ""

	except:
		return {
			"date": "unknown",
			"weekday": "unknown",
			"season(days)": "unknown",
			"number_of_day": "unknown",
			"days_to_ny": "unknown",
		}  # false_date
	else:
		return {
			"date": todays_date,
			"weekday": weekdays[day],
			"season(days)": str(mts),
			"number_of_day": str(cnod),
			"days_to_ny": str(fdth),
		}  # true_date / season(days_in_month) / days_to_newyear


async def jdate(
	dd: int = 1,
	mm: int = 1,
	yy: int = 1970,
	hou: int = 9,
	minut: int = 0,
	secon: int = 0,
):  # julian_date(is_unixtime) # debug
	a = int((14 - mm) / 12)
	y = yy + 4800 - a
	m = mm + 12 * a - 3

	"""
	JDN mod 7	0	1	2	3	4	5	6
	День недели	Пн	Вт	Ср	Чт	Пт	Сб	Вс
	"""

	jdn_dict: dict = {}

	jdn_dict["0"] = "Пн"
	jdn_dict["1"] = "Вт"
	jdn_dict["2"] = "Ср"
	jdn_dict["3"] = "Чт"
	jdn_dict["4"] = "Пт"
	jdn_dict["5"] = "Сб"
	jdn_dict["6"] = "Вс"

	try:
		jdn = dd + int((153 * m + 2) / 5) + 365 * y + int(y / 4) - 32083
	except:
		jdn = -1

	try:
		jd = jdn + ((hou - 12) / 24) + (minut / 1440) + (secon / 86400)
	except:
		jd = -1

	if jdn % 7 in range(0, 7):
		return jdn_dict[str(jdn)]
	else:
		return ""

	return (jdn, jd)


# datetime.fromtimestamp(1707646971.451722).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # '2024-02-11 15:22:51.451'
def unixtime_to_date(unixtime: float = 0.0) -> str:  # os.path.getmtime(file) # async

	utd = ""

	try:
		assert unixtime, ""
	except:
		try:
			dt = datetime.now()
		except:
			dt = None
		else:
			dtu = datetime(
				year=dt.year,
				month=dt.month,
				day=dt.day,
				hour=dt.hour,
				minute=dt.minute,
				second=dt.second,
				microsecond=dt.microsecond,
			).timestamp()
			# utd = datetime.fromtimestamp(dtu).strftime('%Y-%m-%d %H:%M:%S') # current_datetime # no_ms # type1
			utd = datetime.fromtimestamp(dtu).strftime("%Y-%m-%d %H:%M:%S.%f")[
				:-3
			]  # current_datetime # ms # type2
			# (dt, micro) = datetime.fromtimestamp(dtu).strftime('%Y-%m-%d %H:%M:%S.%f').split('.') # split_datetime_and_ms # type3
			# utd = "%s.%03d" % (dt, int(micro) / 1000)

	else:
		# utd = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S") # no_ms # type1
		utd = datetime.fromtimestamp(unixtime).strftime("%Y-%m-%d %H:%M:%S.%f")[
			:-3
		]  # ms # type2
		# (dt, micro) = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S.%f').split('.') # split_datetime_and_ms # type3
		# utd = "%s.%03d" % (dt, int(micro) / 1000)

	return utd


# date_to_unixtime() # 1707646971.451722 # without_file
# datetime.now() # datetime.year/datetime.month/datetime.day
# year: int = 1970, month: int = 1, day: int = 1, hh: int = 0, mm: int = 0, ss: int = 0 # is_split_datetime_by_str
def date_to_unixtime() -> float:  # async
	dtu = 0.0

	try:
		dt = datetime.now()
	except:
		dt = None
	else:
		dtu = datetime(
			year=dt.year,
			month=dt.month,
			day=dt.day,
			hour=dt.hour,
			minute=dt.minute,
			second=dt.second,
			microsecond=dt.microsecond,
		).timestamp()  # current_datetime

	return dtu


# @redate_files # @create_and_old_time_list
async def redate_files(lst: list = []):
	if len(lst) > 1:
		create_time_list = sorted(
			[os.path.getmtime(l) for l in lst], reverse=False
		)  # list
		old_time_list = [os.path.getmtime(l) for l in lst]  # list
		new_time_list = zip(create_time_list, old_time_list, lst)  # generator(one_time)

		try:
			create_and_old_time_list = [
				i
				for i in len(create_time_list)
				if create_time_list[i] != old_time_list[i]
			]
		except:
			create_and_old_time_list = []

		if create_and_old_time_list:
			for ctl, otl, pf in new_time_list:
				try:
					assert all((otl, ctl, pf)), ""
				except AssertionError:  # if_null(date/some_files)
					continue

				if all((ctl, otl, ctl != otl)):  # if_diff_time
					logging.info(
						"@project_file[utime][description] %s"
						% ";".join([unixtime_to_date(ctl), unixtime_to_date(otl), pf])
					)
					# write_log("debug project_file[utime][description]", "%s" % ";".join([unixtime_to_date(ctl), unixtime_to_date(otl), pf]))
					os.utime(
						pf, times=(otl, ctl)
					)  # sort_and_update_some_date # old -> new
				else:
					continue

	return


# gcd_list = gcd_from_numbers([i for i in range(20) if i]) # filter_integers_from_to
async def gcd_from_numbers(lst: list = []) -> list:

	try:
		assert lst, "Пустой список @gcd_from_numbers/lst"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Пустой список @gcd_from_numbers/lst")
		raise err
		return []
	except BaseException as e5:  # if_error
		logging.error("Пустой список @gcd_from_numbers/lst [%s]" % str(e5))
		return []

	equal_mod: list = []

	tmp = [l for l in filter(lambda x: x, tuple(lst))]  # skip_zero_by_filter
	if all((tmp, len(tmp) <= len(lst))):
		lst = tmp  # skip_zero

	# wait_to_found_divmod
	if all((min(lst) > 0, min(lst) < max(lst))):  # convert_to_generator(refactor)
		for i in range(min(lst), max(lst) + 1):
			for l1 in range(len(lst) - 1):
				for l2 in range(l1 + 1, len(lst)):
					if all((l1 != l2, i > 1)) and all(
						(lst[l1] % i == 0, lst[l2] % i == 0, lst[l1] < lst[l2])
					):
						equal_mod.append({"l1": lst[l1], "l2": lst[l2], "i": i})

	return equal_mod  # result(divmod_in_list/null_list)


open(twoday_base, "w", encoding="utf-8").close()  # clean_every_day


# is_period: is_week(7 days), is_month(30 days), is_year(year)
def ff_to_days(
	ff: str = "",
	period: int = 30,
	is_dir: bool = False,
	is_period: list = [False, False, False],
	is_less: bool = True,
	is_any: bool = False,
) -> tuple:  # count_is_after # default(month)

	try:
		assert ff and os.path.exists(
			ff
		), f"Файл отсуствует @ff_to_days/{ff}"  # is_assert_debug # ff
	except AssertionError:  # if_null
		logging.warning("Файл не существует @ff_to_days/%s" % ff)
		# raise err
		return ("", -1, None)  # null_filename / bad_status / unknown_type
	except BaseException as e6:  # if_error
		logging.error("Файл не существует @ff_to_days/%s [%s]" % (ff, str(e6)))
		return ("", -1, None)

	if is_any:
		is_less = False

	if is_less:
		is_any = False

	try:
		is_dir = not os.path.isfile(ff)
	except:
		is_dir = False

	dt = datetime.now()  # include_month_and_year_for_dir

	days = 366 if dt.year % 4 == 0 else 365

	try:
		today = datetime.today()  # datetime
		fdate = os.path.getmtime(ff)  # unixdate(file/folder) # modify # dir /t:w
		# fdate = os.path.getctime(ff)  # unixdate(file/folder) # create # dir /t:c
		ndate = datetime.fromtimestamp(fdate)  # datetime
	except:
		return ("", -1, is_dir)  # null_filename / bad_status / is_dir
	else:
		try:
			assert (
				period >= 0
			), f"Ошибка периода @ff_to_days/{period}"  # is_assert_debug
		except AssertionError as err:  # if_null
			logging.warning("Ошибка периода @ff_to_days/%s" % ff)
			raise err
			return ("", -1, is_dir)  # default_result / bad_status / is_dir
		except BaseException as e7:  # if_error
			logging.error("Ошибка периода @ff_to_days/%s [%s]" % (ff, str(e7)))
			return ("", -1, is_dir)
		else:
			if period >= 0 and is_period.count(False) == len(
				is_period
			):  # period_by_per_days(less_or_any)
				if (
					is_less
					and abs(today - ndate).days <= period
					or not is_less
					and abs(today - ndate).days >= period
					or all((ndate.month <= dt.month, ndate.year == dt.year))
					and is_dir
				) and is_any == False:  # less_or_equal_month_current_year_by_datetime(for_dir)
					return (
						ff,
						abs(today - ndate).days,
						is_dir,
					)  # (file/folder)name / count_days / is_dir
				elif all(
					(
						is_any == True,
						abs(today - ndate).days >= 0,
						period >= 0
						or all((ndate.month > 0, ndate.year > 0, ndate.day > 0))
						and is_dir,
					)
				):  # any_period_by_datetime(for_dir)
					return (
						ff,
						abs(today - ndate).days,
						is_dir,
					)  # (file/folder)name / count_days / is_dir
			elif period >= 0 and is_period.count(True) > 0:

				is_new_period: bool = False

				# is_period: is_week(7 days), is_month(30 days), is_year(year)
				if is_period[0] and abs(today - ndate).days // 7 <= 1:
					period, is_new_period = 8, True
				elif is_period[1] and abs(today - ndate).days // 30 <= 1:
					period, is_new_period = 31, True
				elif is_period[2] and abs(today - ndate).days // 365 <= 1:
					period, is_new_period = days + 1, True  # +1(for_list)

				if abs(today - ndate).days <= 2:  # append_every_day
					with open(twoday_base, "a", encoding="utf-8") as tdf:
						tdf.writelines("%s\n" % ff.split("\\")[-1])

				if all(
					(period, is_new_period, abs(today - ndate).days in range(0, period))
				):  # current / change_period / less_period
					return (
						ff,
						abs(today - ndate).days,
						is_dir,
					)  # (file/folder)name / count_days / is_dir
				elif all(
					(period, not is_new_period, abs(today - ndate).days >= 0)
				):  # current / not_change_period / any_period
					return (
						ff,
						abs(today - ndate).days,
						is_dir,
					)  # (file/folder)name / count_days / is_dir
			# else:
			# return ("", -1, is_dir) # default_result / bad_status / is_dir

	return ("", -1, is_dir)  # default_result / bad_status / is_dir


if os.path.exists(twoday_base):
	if os.path.getsize(twoday_base) != 0:
		copy(twoday_base, twoday_base2)
	elif os.path.getsize(twoday_base) == 0 and os.path.exists(twoday_base2):
		os.remove(twoday_base2)


all_list: list = []
lang_list: list = []


# clear_last_by_period(json)
with open(days_base, "w", encoding="utf-8") as dbf:
	json.dump({}, dbf, ensure_ascii=False, indent=4, sort_keys=True)

with open(month_base, "w", encoding="utf-8") as mbf:
	json.dump({}, mbf, ensure_ascii=False, indent=4, sort_keys=True)

with open(year_base, "w", encoding="utf-8") as ybf:
	json.dump({}, ybf, ensure_ascii=False, indent=4, sort_keys=True)

with open(foldcnt_base, "w", encoding="utf-8") as fbf:
	json.dump({}, fbf, ensure_ascii=False, indent=4, sort_keys=False)

# clear_last_by_period(lst)
open(files_by_days, "w", encoding="utf-8").close()
open(files_by_month, "w", encoding="utf-8").close()
open(files_by_year, "w", encoding="utf-8").close()


# generate_paths_for_manual_run # debug # top100_rus.lst # top100_eng.lst
async def folders_from_path(
	is_rus: bool = False,
	template: list = [],
	need_clean: bool = False,
	is_tvseries: bool = True,
	cntfiles: int = 4,
):  # -> list:

	global all_list

	folder_scan: list = []
	folder_scan_full: list = []
	folder_desc_files: list = []

	# new

	if all((is_rus, is_tvseries)):
		mydir = "d:\\multimedia\\video\\serials_europe\\"
		# efile = ".\\top100_rus.lst" # generate_to_current_folder
		mydir2 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\top100_rus.lst"  # folder -> file
		mydir3 = (
			"d:\\multimedia\\video\\serials_europe\\top100_rus.lst"  # folder -> file
		)
		mydir4 = (
			"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\rus.lst"  # folder -> file
		)
	elif all((not is_rus, is_tvseries)):
		mydir = "d:\\multimedia\\video\\serials_conv\\"
		# efile = ".\\top100_eng.lst" # generate_to_current_folder
		mydir2 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\top100_eng.lst"  # folder -> file
		mydir3 = "d:\\multimedia\\video\\serials_conv\\top100_eng.lst"  # folder -> file
		mydir4 = (
			"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\eng.lst"  # folder -> file
		)

	"""
	if any((is_rus, not is_rus)) and is_cinema: # skip_if_no_rus
		mydir = "d:\\multimedia\\video\\big_films\\"
		# efile = ".\\top100.lst" # generate_to_current_folder
		mydir2 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\top100.lst" # folder -> file
		mydir3 = "d:\\multimedia\\video\\big_films\\top100.lst" # folder -> file
		mydir4 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\top.lst" # folder -> file
	"""

	# delete_last_list_by_language # debug

	# pass_1_of_3

	rus_regex = re.compile(r"_Rus", re.M)
	sym_or_num = re.compile(r"^[a-z0-9]", re.I)
	# ext_regex = re.compile(r"\.[a-z]{3,}$", re.I)

	# full_paths # video_regex

	found_list: list = []
	full_list: list = []

	# if_more_one_file_then_save # debug
	try:
		# folder_scan_full = list(set(["".join([mydir, df]) for df in os.listdir(mydir) if os.path.exists("".join([mydir, df])) and df])) # old
		folder_scan_full = list(
			set(
				[
					os.path.join(mydir, df)
					for df in os.listdir(mydir)
					if os.path.exists(os.path.join(mydir, df)) and df
				]
			)
		)
		assert folder_scan_full, ""
	except AssertionError:
		folder_scan_full = []
		return []  # @all_list

	folder_scan_full.sort(key=os.path.getmtime)  # reverse=False # sort_by_abc

	try:
		with open(desc_base, encoding="utf-8") as dbf:
			desc_dict = json.load(dbf)
	except:
		desc_dict = {}

		with open(desc_base, "w", encoding="utf-8") as dbf:
			json.dump(desc_dict, dbf, ensure_ascii=False, indent=4, sort_keys=True)

	if not is_tvseries:
		desc_dict = {}

	"""
	try:
		with open(desc_base_temp, encoding="utf-8") as dbtf:
			desc_dict2 = json.load(dbtf)
	except:
		desc_dict2 = {}
	"""

	desc_dict_filter: dict = {}

	# clear_old_desc # replace)1)/is_old(0)
	try:
		desc_dict_filter = {
			k.strip(): v.replace(";(", ";").replace(");", ";").strip()
			if v != v.replace(";(", ";").replace(");", ";")
			else v.strip()
			for k, v in desc_dict.items()
		}
	except:
		desc_dict_filter = {}
	else:
		if all(
			(desc_dict_filter, len(desc_dict_filter) <= len(desc_dict), is_tvseries)
		):  # desc_dict # tvseries_only

			dsc_cnt = abs(len(desc_dict_filter) - len(desc_dict))

			if dsc_cnt:
				print(
					Style.BRIGHT + Fore.CYAN + "будет обновлено",
					Style.BRIGHT + Fore.WHITE + "%d" % dsc_cnt,
					Style.BRIGHT + Fore.YELLOW + "записей",
				)

			desc_dict.update(
				desc_dict_filter
			)  # desc_new = {**desc_dict, **desc_dict_filter}

	logging.info(
		"@desc_dict[update][1] %d [%s]" % (len(desc_dict), str(datetime.now()))
	)

	# pass_2_of_3 # only_folder_names

	# debug # tvseries / cinema
	if is_tvseries:
		ccmd = r"cmd /c dir /r/b/ad/od- *.*"  # folders # cmd /k

	lang_list: list = []
	folder_scan: list = []

	if os.path.exists(mydir):
		os.chdir(mydir)

	os.system(
		"%s >> %s" % (ccmd, mydir3)
	)  # is_list_in_current_folder # 0 - ok, 1 - error

	try:
		with open(mydir3) as mdf:  # utf-8
			lang_list = mdf.readlines()
	except BaseException as e8:  # if_error
		logging.error(
			"debug lang_list[error] [%s] [%s]" % (str(e8), str(datetime.now()))
		)  # logging.warning("Пустой список @folder_from_path/lang_list")
	finally:  # else
		logging.info(
			"@lang_list[length] %s [%s]" % (str(len(lang_list)), str(datetime.now()))
		)

		# is_languages

		folder_scan = folder_scan[::-1]  # reverse(newer_to_oldest)
		# folder_scan = folder_scan[0:1000] if len(folder_scan) > 1000 else folder_scan # limit_folders_for_scan

		if all(
			(folder_scan, lang_list, is_tvseries)
		):  # folder_list(reverse) / folder_list_by_lang # tvseries_only
			if is_rus:
				folder_scan_rus = [
					rus_regex.sub("", ll).strip()
					for ll in filter(lambda x: sym_or_num.findall(x), tuple(lang_list))
					if all(
						(rus_regex.sub("", ll), len(rus_regex.sub("", ll)) <= len(ll))
					)
				]  # filter_rus
				if all((folder_scan_rus, len(folder_scan_rus) <= len(lang_list))):
					folder_scan = folder_scan_rus
			elif not is_rus:
				folder_scan_eng = [
					ll.strip()
					for ll in filter(lambda x: sym_or_num.findall(x), tuple(lang_list))
					if ll
				]
				if all((folder_scan_eng, len(folder_scan_eng) <= len(lang_list))):
					folder_scan = folder_scan_eng

			with open(
				mydir2, "w", encoding="utf-8"
			) as mf:  # resave # top_file_by_lang # debug
				mf.writelines(
					"%s\n" % fs.strip()
					for fs in filter(
						lambda x: sym_or_num.findall(x), tuple(folder_scan)
					)
				)  # int/str # is_by_count(top)

	try:
		if os.path.exists(mydir3):
			os.remove(mydir3)  # copy(mydir3, mydir2)
	except BaseException as e9:  # if_error
		logging.error("%s" % str(e9))

	logging.info(
		"@folder_scan[list][2] %d [%s]" % (len(folder_scan), str(datetime.now()))
	)

	# pass_3_of_3

	fsf_set = set()

	len_and_codepage = set()

	fold_and_date: list = []

	# clear_before_load(every_run_update)
	result_days: dict = {}
	result_month: dict = {}
	result_year: dict = {}

	# clear_last_by_period
	try:
		with open(days_base, encoding="utf-8") as dbf:
			result_days = json.load(dbf)
	except:
		with open(days_base, "a", encoding="utf-8") as dbf:
			json.dump(result_days, dbf, ensure_ascii=False, indent=4, sort_keys=True)

	try:
		with open(month_base, encoding="utf-8") as mbf:
			result_month = json.load(mbf)
	except:
		with open(month_base, "a", encoding="utf-8") as mbf:
			json.dump(result_month, mbf, ensure_ascii=False, indent=4, sort_keys=True)

	try:
		with open(year_base, encoding="utf-8") as ybf:
			result_year = json.load(ybf)
	except:
		with open(year_base, "a", encoding="utf-8") as ybf:
			json.dump(result_year, ybf, ensure_ascii=False, indent=4, sort_keys=True)

	"""
	result = {}
	for name, age in people:
		if age in result:
			result[age].append(name)
		else:
			result[age] = [name]
	"""

	group_error: bool = False

	if folder_scan_full:  # count_folders
		logging.info(
			"Найденов папок %s [%s]" % (str(len(folder_scan_full)), str(datetime.now()))
		)  # folder_counts / date_scan

	print(
		"Загрузка папок и период загрузки или обработки. Ждите... %s"
		% str(datetime.now()).split(" ")[-1]
	)  # is-color

	tfiles_dict: dict = {}  # debug
	tfiles: list = []

	open(
		os.path.join(path_for_queue, "video_resize.int"), "w", encoding="utf-8"
	).close()  # clear_last_list # debug

	s = l = a = 0

	all_period_dict: dict = {}

	sf: int = 0
	fsizes: list = []
	files: list = []

	for fsf in filter(lambda x: os.path.isdir(x), tuple(folder_scan_full)):
		# group_by_season # debug(need_fast)
		# '''

		try:
			if os.path.isdir(fsf):
				list_files = os.listdir(fsf)
		except:
			list_files = []

		# @period
		# '''
		today = datetime.now()
		fdate = os.path.getmtime(fsf)
		ndate = datetime.fromtimestamp(fdate)
		# '''

		# @count
		len_desc = len(list(filter(lambda x: "txt" in x, tuple(list_files))))
		len_files = len(list(filter(lambda x: "mp4" in x, tuple(list_files))))

		fsizes = [os.path.getsize(os.path.join(fsf, f)) for f in os.listdir(fsf)]
		files = [
			os.path.join(fsf, f)
			for f in os.listdir(fsf)
			if os.path.exists(os.path.join(fsf, f))
		]
		sf += sum(fsizes)

		try:
			await redate_files(lst=files)
		except:
			pass

		try:
			days_ago = abs(today - ndate).days
			assert bool(days_ago >= 0), ""
		except AssertionError:  # if_none(today)
			days_ago = 0

		try:
			max_days_by_year = 366 if today.year % 4 == 0 else 365
		except:
			max_days_by_year = 365

		# any_day / limit_by_month / limit_by_year
		period_list_fitler = [
			days_ago / 7 <= 4,
			days_ago / 30 <= 12,
			days_ago / max_days_by_year <= max_days_by_year,
		]  # day / month / year # float
		# period_list_fitler = [days_ago % 7 <= 4, days_ago % 30 <= 12, days_ago % max_days_by_year <= max_days_by_year] # day / month / year # mod
		# period_list_fitler = [days_ago / 7 > 0, days_ago / 30 > 0, days_ago / max_days_by_year > 0] # day / month / year # skip_some

		is_day = is_month = is_year = False

		if all((period_list_fitler[-1], len_files)):
			is_year = True
			s += len_files  # debug
			l += 1
			logging.info("@datetime [year] [%s]" % fsf)
			year_status = (
				"Этот год"
				if days_ago / max_days_by_year == 0
				else "%d лет назад" % (days_ago // max_days_by_year)
			)
			all_period_dict[year_status.strip()] = [fsf.split("\\")[-1], len_files]

		if all((period_list_fitler[1], len_files)):
			is_month = True
			s += len_files  # debug
			l += 1
			logging.info("@datetime [month] [%s]" % fsf)
			month_status = (
				"Этот месяц"
				if days_ago / 30 == 0
				else "%d месяцев назад" % (days_ago // 30)
			)
			all_period_dict[month_status.strip()] = [fsf.split("\\")[-1], len_files]

		if all((period_list_fitler[0], len_files)):
			is_day = True
			s += len_files  # debug
			l += 1
			logging.info("@datetime [day] [%s]" % fsf)
			week_status = (
				"Эта неделя"
				if days_ago / 7 == 0
				else "%d недель назад" % (days_ago // 7)
			)
			all_period_dict[week_status.strip()] = [fsf.split("\\")[-1], len_files]

		if any((is_day, is_month, is_year)):
			logging.info(
				"@datetime [day/month/year] [%s] [%s]"
				% (fsf, str([is_day, is_month, is_year]))
			)

		if sf:
			sf_calc: int = 0
			sf_calc_status: str = ""

			if len(str(sf)) in range(7, 10):
				sf_calc = sf // (1024**3)
				sf_calc_status = "".join([str(sf_calc), "Gb"])
			elif len(str(sf)) in range(4, 7):
				sf_calc = sf // (1024**2)
				sf_calc_status = "".join([str(sf_calc), "Mb"])
			else:
				sf_calc = sf // (1024**2)
				sf_calc_status = "".join([str(sf_calc), "Mb"])

			logging.info(
				"@datetime [current_filesize] [%s] [%s]" % (fsf, sf_calc_status)
			)
		# '''

		try:
			assert all((len_desc, len_files)), "Нет файлов для обработки"
		except AssertionError as err:  # if_null
			logging.warning("Нет файлов для обработки [%s]" % fsf)
			raise err
			continue
		except BaseException as e:  # if_error
			logging.error("Ошибка при получении файлов [%s] [%s]" % (fsf, str(e)))

		if all((len_desc > 0, len_files > 0)):  # default_count(skip_null)

			if all(
				(cntfiles, len_files, len_files <= cntfiles)
			):  # debug_for_logging_by_count # folder/desc/files
				print(
					Style.BRIGHT
					+ Fore.GREEN
					+ "папка %s, %d описаний, %d файлов"
					% (fsf.split("\\")[-1], len_desc, len_files)
				)
				logging.info(
					"папка %s, %d описаний, %d файлов [ok]"
					% (fsf.split("\\")[-1], len_desc, len_files)
				)  # by_count

			elif all(
				(cntfiles, len_files, len_files > cntfiles)
			):  # debug_for_logging_by_count # folder/desc/files
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "папка %s, %d описаний, %d файлов"
					% (fsf.split("\\")[-1], len_desc, len_files)
				)
				logging.info(
					"папка %s, %d описаний, %d файлов [+]"
					% (fsf.split("\\")[-1], len_desc, len_files)
				)  # by_count

			# logging.info("папка %s, %d описаний, %d файлов" % (fsf.split("\\")[-1], len_desc, len_files)) # logging_for_all

			try:
				max_file = list(filter(lambda x: "txt" in x, tuple(list_files)))[
					-1
				]  # last_file
			except:
				max_file = ""
			else:
				if max_file:  # if_not_null
					logging.info(
						"@list_files/max_file %s"
						% ";".join([fsf.split("\\")[-1], max_file])
					)
				else:
					logging.warning(
						"debug list_files/max_file is null %s" % fsf.split("\\")[-1]
					)

			try:
				mfile_name = (
					max_file.split("\\")[-1].split(".")[0].split("s")[0]
				)  # number_season
			except:
				mfile_name = ""
			finally:
				if all(
					(mfile_name, not mfile_name.endswith("s"), max_file)
				):  # if_not_null
					mfile_name += "s"
					logging.info(
						"@mfile_name %s" % ";".join([fsf.split("\\")[-1], mfile_name])
					)
				elif not mfile_name:
					logging.warning("debug mfile_name is null %s" % fsf.split("\\")[-1])

			try:
				list_filter = [
					lf.strip()
					for lf in list_files
					if all((mfile_name, mfile_name in lf, not lf.endswith(".txt")))
				]  # filter_by_season
			except:
				list_filter = []
			finally:
				# debug # try_unique_by_tfiles
				if all(
					(
						list_filter,
						len(list_filter) < len_files,
						not (fsf, len(list_filter)) in tfiles,
					)
				):  # all((list_filter, len(list_filter) <= len_files)) # default # if_not_null
					tfiles.append((fsf, len(list_filter)))  # yes_filter
					s += len(list_filter)  # default
					l += 1
					logging.info(
						"@list_filter/folder/files [+] %s"
						% ";".join([fsf.split("\\")[-1], str(len(list_filter))])
					)
				elif all((not list_filter, not (fsf, len_files) in tfiles)):  # if_null
					tfiles.append((fsf, len_files))  # default(no_filter)
					s += len_files  # default
					l += 1
					logging.info(
						"@list_filter/folder/files [-] %s"
						% ";".join([fsf.split("\\")[-1], str(len_files)])
					)

		# elif all((len_desc > 0, len_files == 0)):
		## print(Style.BRIGHT + Fore.RED + "папка %s, %d описаний, нет файлов" % (fsf.split("\\")[-1], len_desc))
		# logging.info("папка %s, %d описаний, нет файлов [null]" % (fsf.split("\\")[-1], len_desc)) # by_count

	if all((l, l <= len(folder_scan_full))):
		if l != len(folder_scan_full):  # length(diff)
			logging.info(
				"@length %s [diff]" % ";".join([str(l), str(len(folder_scan_full))])
			)
		elif l == len(folder_scan_full):  # length(ok)
			logging.info("@length %s [equal]" % ";".join([str(l)]))

	# select_average_count_of_files(default_select_by_count)
	def avg_calc(s, l):
		try:
			ag = lambda s, l: s // l
			assert all((s, l)), ""
		except AssertionError:  # BaseException as e10
			ag = 0
			logging.warning("@ag division by zero")
		else:
			avg = ag(s, l)
			ag = avg if avg else 0

		return ag

	try:
		a = avg_calc(s, l)  # avg_calc(100, 2) # 50
	except BaseException as e10:
		a = 0  # if_error_not_change
		logging.error("debug cntfile/avg %s" % str(e10))
	else:
		if any((s, l, a)):
			cntfiles = (
				a if a > cntfiles else cntfiles
			)  # avg(is_change)/cntfiles(no_change)
			logging.info(
				"@cntfiles/sum/len/avg/is_rus %s"
				% ";".join([str(cntfiles), str(s), str(l), str(a), str(is_rus)])
			)

	# '''
	# all_period_dict = {k:v for k, v in all_period_dict.items() if all((v[1], v[1] - cntfiles < 0))}
	# all_period_dict = {k:v for k, v in all_period_dict.items() if all((v[1], v[1] - cntfiles > 0))}
	all_period_dict = {
		k: v for k, v in all_period_dict.items() if all((v[1], v[1] <= cntfiles))
	}

	# files_by_year(txt)/@calc_year.lst # year_base(json)/@calc_year.json
	year_ago_dict: dict = {}

	try:
		with open("".join([script_path, "\\calc_year.json"]), encoding="utf-8") as cjf:
			year_ago_dict = json.load(cjf)
	except:
		year_ago_dict = {}

		with open(
			"".join([script_path, "\\calc_year.json"]), "w", encoding="utf-8"
		) as cjf:
			json.dump(year_ago_dict, cjf, ensure_ascii=False, indent=4, sort_keys=False)

	year_count = {
		k: v for k, v in all_period_dict.items() if any(("год" in k, "лет" in k))
	}

	# year_ago_dict.update(year_count)
	year_ago_dict = year_count

	if year_ago_dict:
		with open(
			"".join([script_path, "\\calc_year.json"]), "w", encoding="utf-8"
		) as cjf:
			json.dump(year_ago_dict, cjf, ensure_ascii=False, indent=4, sort_keys=False)

		with open(
			"".join([script_path, "\\calc_year.lst"]), "w", encoding="utf-8"
		) as clf:
			clf.writelines("%s\n" % v[0] for _, v in year_ago_dict.items())

	# files_by_month(txt)/@month_forward.lst # month_base(json)/@month_forward.json
	month_ago_dict: dict = {}

	try:
		with open(
			"".join([script_path, "\\month_forward.json"]), encoding="utf-8"
		) as mjf:
			month_ago_dict = json.load(mjf)
	except:
		month_ago_dict = {}

		with open(
			"".join([script_path, "\\month_forward.json"]), "w", encoding="utf-8"
		) as mjf:
			json.dump(
				month_ago_dict, mjf, ensure_ascii=False, indent=4, sort_keys=False
			)

	month_count = {k: v for k, v in all_period_dict.items() if "месяц" in k}

	# month_ago_dict.update(month_count)
	month_ago_dict = month_count

	if month_ago_dict:
		with open(
			"".join([script_path, "\\month_forward.json"]), "w", encoding="utf-8"
		) as mjf:
			json.dump(
				month_ago_dict, mjf, ensure_ascii=False, indent=4, sort_keys=False
			)

		with open(
			"".join([script_path, "\\month_forward.lst"]), "w", encoding="utf-8"
		) as mlf:
			mlf.writelines("%s\n" % v[0] for _, v in month_ago_dict.items())

	# files_by_days(txt)/@days_ago.lst #days_base(json)/@days_ago.json
	days_ago_dict: dict = {}

	try:
		with open("".join([script_path, "\\days_ago.json"]), encoding="utf-8") as djf:
			days_ago_dict = json.load(djf)
	except:
		days_ago_dict = {}

		with open(
			"".join([script_path, "\\days_ago.json"]), "w", encoding="utf-8"
		) as djf:
			json.dump(days_ago_dict, djf, ensure_ascii=False, indent=4, sort_keys=False)

	week_count = {k: v for k, v in all_period_dict.items() if "недел" in k}

	# days_ago_dict.update(week_count) # update_current_by_week
	days_ago_week = week_count

	if all((days_ago_dict, days_ago_week)):
		with open(
			"".join([script_path, "\\days_ago.json"]), "w", encoding="utf-8"
		) as djf:
			json.dump(days_ago_dict, djf, ensure_ascii=False, indent=4, sort_keys=False)

		with open(
			"".join([script_path, "\\days_ago.lst"]), "w", encoding="utf-8"
		) as dlf:
			dlf.writelines("%s\n" % v[0] for _, v in days_ago_dict.items())
	# '''

	try:
		# tfiles_sorted = sorted(tfiles, key=lambda tfiles: tfiles[0]) # folder_by_abc # type_1_of_2 # multiple
		tfiles_sorted = sorted(
			list(set(tfiles)), key=lambda tfiles: tfiles[1]
		)  # count_by_abc # type_1_of_2 # multiple
	except:
		tfiles_sorted = []
	else:
		# filter_by_count # debug_for_manual(is_fast) # 6types
		try:
			# tfiles_filter = [(fold, cnt) for fold, cnt in tfiles_sorted if all((cnt, cnt % cntfiles == 0))] # path/count # if_mod_by_avg(equal_count)
			# tfiles_filter = [(fold, cnt) for fold, cnt in tfiles_sorted if all((cnt, cnt - cntfiles > 0))] # path/count # if_more_files(classify=0) # 777Gb
			tfiles_filter = [
				(fold, cnt)
				for fold, cnt in tfiles_sorted
				if all((cnt, cnt - cntfiles < 0))
			]  # path/count # if_less_files(classify=1) # 422Gb
			# tfiles_filter = [(fold, cnt) for fold, cnt in tfiles_sorted if all((cnt, cnt == 2))] # path/count # is_double(two_files)
			# tfiles_filter = [(fold, cnt) for fold, cnt in tfiles_sorted if all((cntfiles, cnt, cnt <= cntfiles))] # path/count # range_between >= 1 # default
			# tfiles_filter = [(fold, cnt) for fold, cnt in tfiles_sorted if cnt > 0] # path/count # any_count_not_null
			# tfiles_filter = [(fold, cnt) for fold, cnt in tfiles_sorted if all((cnt, cntfiles, cnt % cntfiles <= cntfiles - 1))] # path/count # cnt_by_mod # debug
		except:
			tfiles_filter = []
		else:
			if (
				not tfiles_filter
			):  # hide_if_use_the_type(debug/test) # pass_2_of_2(logic)
				tfiles_filter = [
					(fold, cnt)
					for fold, cnt in tfiles_sorted
					if all((cnt, cnt - cntfiles > 0))
				]  # path/count # if_more_files(classify=0) # 777Gb

			tfiles_sorted = list(
				set(tfiles_filter)
			)  # update_sorted_by_filter # try_unique

			print()

			for f, c in tfiles_sorted:  # updates_count
				if all(
					(cntfiles, c, tfiles_sorted)
				):  # avg/default # count(sorted_list)
					print(
						Style.BRIGHT
						+ Fore.CYAN
						+ "папка %s, %d файлов" % (f.split("\\")[-1], c)
					)
					logging.info(
						"папка %s, %d файлов [ok]" % (f.split("\\")[-1], c)
					)  # by_count

		# save_folder_base_by_count
		try:
			with open(foldcnt_base, encoding="utf-8") as fbf:
				tfiles_dict = json.load(fbf)
		except:
			tfiles_dict = {}

			with open(foldcnt_base, "w", encoding="utf-8") as fbf:
				json.dump(tfiles_dict, ensure_ascii=False, indent=4, sort_keys=False)

		for f, c in tfiles_sorted:  # tfiles_filter -> tfiles_sorted
			tfiles_dict[f.strip()] = c

		with open(foldcnt_base, "w", encoding="utf-8") as fbf:
			json.dump(tfiles_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False)

		with open(
			os.path.join(path_for_queue, "video_resize.int"), "w", encoding="utf-8"
		) as vrif:  # (a)ppend_two_list(a) / (w)rite_save_last_list
			vrif.writelines(
				"%s\n" % str(k.split("\\")[-1]) for k in [*tfiles_dict]
			)  # for k, _ in tfiles_dict.items() # only_short_fold # for_select
		# '''

	for fsf in filter(lambda x: os.path.isdir(x), tuple(folder_scan_full)):

		if not fsf.strip() in fsf_set:
			fsf_set.add(fsf.strip())  # add_if_not_runned
		else:
			continue  # skip_if_runned

		is_found: bool = False
		is_not_found: bool = False
		is_two_desc: bool = False

		# is_folder: bool = False

		try:
			if not os.path.isfile(fsf):
				list_files = os.listdir(fsf)
			assert list_files, ""
		except AssertionError as err:  # if_null
			logging.error(
				"Нет файлов в папке %s [%s] [%s]" % (fsf, str(err), str(datetime.now()))
			)
			continue
		else:
			is_found = (
				len(list(filter(lambda x: "mp4" in x, tuple(list_files)))) >= 0
				and len(list(filter(lambda x: "txt" in x, tuple(list_files)))) == 1
			)  # desc(1) / files(0/1)
			is_not_found = (
				len(list(filter(lambda x: "mp4" in x, tuple(list_files)))) == 0
				and len(list(filter(lambda x: "txt" in x, tuple(list_files)))) == 0
			)  # desc(0) / files(0)
			is_two_desc = (
				len(list(filter(lambda x: "mp4" in x, tuple(list_files)))) >= 0
				and len(list(filter(lambda x: "txt" in x, tuple(list_files)))) >= 2
			)  # desc(2) / files(0/1)

		if list_files:  # is_folder_not_null
			logging.info(
				"Файлы в папке %s %d [%s]" % (fsf, len(list_files), str(datetime.now()))
			)  # folder_name / count_files / date_scan

		# path_to_description
		try:
			full_list = list(
				set(
					[
						"\\".join([fsf, ol]).strip()
						for ol in filter(lambda x: "txt" in x, tuple(list_files))
						if ol
					]
				)
			)
		except BaseException as e11:  # if_error
			full_list = []
			logging.error(
				"Пустой список или нет описаний @folder_from_path/full_list [%s] [%s]"
				% (str(e11), str(datetime.now()))
			)
		else:
			full_list.sort(reverse=False)
			logging.info(
				"Список из описаний найдено @folder_from_path/full_list %s [%s]"
				% (str(len(full_list)), str(datetime.now()))
			)

		# descriptions # debug
		# """
		if len(list(filter(lambda x: "txt" in x, tuple(list_files)))) > 0 and all(
			(full_list, is_tvseries)
		):  # tvseries_only

			# "﻿10 причин моей ненависти": "﻿10 причин моей ненависти;(10 Things I Hate About You);7 Jul 2009"
			# "Адаптация": "Адаптация;6 Feb 2017"

			# 911 (9-1-1) 3 Jan 2018 # 911 (9-1-1) 3.01.2018 # one_info_different_date_types

			desc_regex = re.compile(
				r"(.*)\s\((.*)\)\s([\d+]{1,2}\s[A-Z]{3}\s[\d+]{4})", re.I
			)  # rus / eng / date

			dlist = []

			codepage: str = ""

			for fl in tuple(full_list):  # description_files

				try:
					with open(fl, encoding="utf-8") as flf:  # codepage1
						dlist = flf.readlines()
				except:
					dlist = []
				else:
					codepage = "utf-8"

					dlist_strip = [
						dl.strip() for dl in filter(lambda x: x, tuple(dlist))
					]
					dlist = dlist_strip

				# with open(fl, encoding="cp1251") as flf: # codepage2
				# with open(fl, encoding="cp866") as flf: # codepage3
				# with open(fl, encoding="iso8859_5") as flf: # codepage4
				# with open(fl, encoding="koi8_r") as flf: # codepage5

				if not dlist:
					try:
						with open(fl) as flf:  # codepage4
							dlist = flf.readlines()
					except:
						dlist = []
					else:
						codepage = ""

						dlist_strip = [
							dl.strip() for dl in filter(lambda x: x, tuple(dlist))
						]
						dlist = dlist_strip

			# days_and_folder: list = []
			# days_and_folder_dict: dict = {}

			for dl in tuple(dlist):  # only_first_line # debug

				try:
					assert (
						dlist
					), f"Пустой список описаний @folders_from_path/{dl}"  # dlist # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning(
						"Пустой список описаний @folders_from_path/dlist [%s]"
						% str(datetime.now())
					)
					raise err
					break

				try:
					assert dl, ""
				except:
					continue
				else:
					len_and_codepage_str = ";".join([str(len(dlist)), codepage])

					if (
						not len_and_codepage_str in len_and_codepage
					):  # try_without_dublicates
						len_and_codepage.add(len_and_codepage_str)

						logging.info(
							"Список описаний @folders_from_path/dlist/codepage/date [%s] '%s' [%s]"
							% (str(len(dlist)), codepage, str(datetime.now()))
						)

				parse_list = []

				# txt = "Две девицы на мели (2 Broke Girls) 19 Sep 2011"
				# list(desc_regex.findall(txt)[0]) # ('Две девицы на мели', '2 Broke Girls', '19 Sep 2011')

				# txt = "13 клиническая () 22 Dec 2022"
				# list(desc_regex.findall(txt)[0]) # ['13 клиническая', '', '22 Dec 2022']

				if desc_regex.findall(dl):
					parse_list = list(desc_regex.findall(dl)[0])

				if all(
					(parse_list, dl, is_tvseries)
				):  # any_description / some_data / tvseries_only
					filter_list = [
						l.strip() for l in parse_list if l
					]  # 3(eng) # 2(rus)

					if any(
						(filter_list[0][0].isalpha(), filter_list[0][0].isnumeric())
					):  # check_first_syms
						desc_dict[filter_list[0].strip()] = ";".join(
							filter_list[1:]
						).strip()

			if all((desc_dict, is_tvseries)):  # some_desc(tvseries_only)

				with open(desc_base, "w", encoding="utf-8") as dbf:
					json.dump(
						desc_dict, dbf, ensure_ascii=False, indent=4, sort_keys=True
					)
			# """

			# config = {"ff": fsf, "period": days, "is_dir": False, "is_less": False, "is_any": True} # **config # fsf(default) -> None(debug)
			# ff_to_days(ff=fsf, period=days, is_dir=False, is_less=False, is_any=True)

			dt = datetime.now()

			days = 366 if dt.year % 4 == 0 else 365  # by_year # is_no_lambda

			try:
				ftd = ff_to_days(
					ff=fsf, period=days, is_dir=False, is_less=False, is_any=True
				)  # period=30(is_month)/days(is_year) # by_Year # type1
				# ftd = ff_to_days(ff=fsf, period=12*days, is_dir=False, is_less=True, is_any=False) # period=30(is_month)/days(is_year) # 12_Year_and_less # type2
			except:
				ftd = (None,)  # if_error2(None)

			day_ago = month_ago = year_ago = 0

			if (
				len(ftd) > 1
				and os.path.exists(ftd[0])
				and ftd[0] != None
				and is_tvseries
			):  # ftd[1] >= 0: # is_cinema
				try:
					folder_or_file = (
						"Папка: %s" % fsf if ftd[-1] else "Файл: %s " % ftd[0]
					)  # is_no_lambda # type1
					if ftd[1] <= 31:  # +maxdays
						day_ago = "%d дней назад" % (ftd[1] % 30)
					elif ftd[1] // 30 in range(1, 12):  # ftd[1] > 30
						month_ago = "%d месяцев назад" % (ftd[1] // 30)
					elif ftd[1] // 365 > 0:  # ftd[1] > 365
						year_ago = "%d лет назад" % (ftd[1] // 365)
				except:
					folder_or_file = (
						"Папка: %s" % fsf
						if not os.path.isfile(ftd[-1])
						else "Файл: %s" % ftd[0]
					)  # is_no_lambda # type2
				finally:
					period_list = (
						[str(day_ago), str(month_ago), str(year_ago)]
						if any((day_ago, month_ago, year_ago))
						else []
					)  # some_period/null(list)
					period_ago = (
						";".join(period_list) if len(period_list) > 0 else ""
					)  # some_periods/null(str)

					try:
						assert (
							ftd[1] >= 0
						), "Нет данных о количества дней или имени папки"  # is_assert_debug
					except AssertionError as err:  # if_null
						# print(Style.BRIGHT + Fore.YELLOW + "%s [%s]" % (folder_or_file, str(datetime.now()))) # folder(file) / datetime # skip_logging_if_need
						logging.warning(
							"folder_or_file/datetime %s [%s]"
							% (folder_or_file, str(datetime.now()))
						)  # if_null(is_color)
						raise err
					except BaseException as e12:  # if_error
						# print(Style.BRIGHT + Fore.RED + "%s [%s] [%s]" % (folder_or_file, str(datetime.now()), str(e12))) # folder(file) / datetime / error
						logging.error(
							"folder_or_file/error/datetime %s [%s] [%s]"
							% (folder_or_file, str(e12), str(datetime.now()))
						)  # if_error(is_color)
					else:
						fold_and_date.append(
							(folder_or_file, period_ago, str(datetime.now()))
						)
						# print(Style.BRIGHT + Fore.WHITE + "%s %s [%s]" % (folder_or_file, str(days_ago), str(datetime.now()))) # folder(file) / dayago /datetime # is_color
						logging.info(
							"folder_or_file/period/datetime %s %s [%s]"
							% (folder_or_file, str(period_ago), str(datetime.now()))
						)  # if_ok(is_color)

						days = month = year = 0

						if ftd[1] <= 31:  # current_days # debug
							try:
								days_str = (
									"%d дней" % ftd[1] if ftd[1] > 0 else "этот день"
								)
								if days_str in [*result_days]:  # only_days
									result_days[days_str].append(fsf.split("\\")[-1])
								else:
									result_days[days_str] = [fsf.split("\\")[-1]]
							except BaseException:
								group_error = True
							else:
								days = ftd[1]  # current_days
						elif ftd[1] // 30 > 0:  # calc_month # debug
							try:
								month_str = (
									"%d месяцев" % (ftd[1] // 30)
									if (ftd[1] // 30) <= 12
									else "другой год"
								)
								if month_str in [*result_month]:  # only_month
									result_month[month_str].append(fsf.split("\\")[-1])
								else:
									result_month[month_str] = [fsf.split("\\")[-1]]
							except BaseException:
								group_error = True
							else:
								if ftd[1] // 30 in range(1, 13):
									month = ftd[1] // 30  # calc_month(1..12)
								elif ftd[1] // 30 > 12:
									year += 1  # next_year(calc)

									year_str = "%d лет" % year
									if year_str in [*result_year]:  # only_year
										result_year[year_str].append(
											fsf.split("\\")[-1]
										)
									else:
										result_year[year_str] = [fsf.split("\\")[-1]]
						elif ftd[1] // 365 > 0:  # calc_year # debug
							try:
								year += int(ftd[1] // 365)  # calc_year

								year_str = (
									"%d лет" % (ftd[1] // 365)
									if (ftd[1] // 365) > 0
									else "этот год"
								)
								if year_str in [*result_year]:  # only_year
									result_year[year_str].append(fsf.split("\\")[-1])
								else:
									result_year[year_str] = [fsf.split("\\")[-1]]
							except BaseException:
								group_error = True

						if any((days, month, year)):
							logging.info(
								"Days: %d, Month: %d, Year: %d [ago]"
								% (days, month, year)
							)
							logging.info(
								"days/folder/datetime: %d [%s] [%s]"
								% (ftd[1], fsf.split("\\")[-1], str(datetime.now()))
							)

			files: list = []
			files2: list = []
			files3: list = []

			sym_or_num_regex = re.compile(
				r"([A-Z]{1,}|[0-9]{1,})", re.M
			)  # Abc -> [A] # aBc -> [B] # aBC -> [BC] # a1B -> [1, B]

			if not group_error:
				if result_days:
					# @classify_by_folders
					try:
						with open(days_base, encoding="utf-8") as dbf:
							result_temp = json.load(dbf)
					except:  # if_error_read
						result_temp = {}
					else:
						if result_temp != result_days:
							result_temp.update(result_days)
							result_days = result_temp
							result_temp = {}

					for k, v in result_days.items():
						result_temp[k] = list(set(v))

					for k, v in result_temp.items():
						if isinstance(v, list):
							for lf in filter(
								lambda x: sym_or_num_regex.findall(x), tuple(v)
							):
								if isinstance(lf, str) and all(
									(lf, not lf.strip() in files)
								):
									files.append(lf.strip())

					# if clear_before_load not_use_result_temp(result_days)

					# @files_by_days
					if files:
						tmp = list(set(files))
						with open(
							files_by_days, "w", encoding="utf-8"
						) as fbdf:  # w -> a
							fbdf.writelines(
								"%s\n" % f for f in filter(lambda x: x, tuple(tmp))
							)

						logging.info(
							"@files_by_days [%d] [%s]" % (len(tmp), str(datetime.now()))
						)  # files -> tmp

					# @days_base
					if result_temp:
						with open(
							days_base, "w", encoding="utf-8"
						) as dbf:  # w -> a # debug
							json.dump(
								result_temp,
								dbf,
								ensure_ascii=False,
								indent=4,
								sort_keys=True,
							)  # save_unique # debug

				if result_month:
					# @classify_by_folders
					try:
						with open(month_base, encoding="utf-8") as mbf:
							result_temp2 = json.load(mbf)
					except:  # if_error_read
						result_temp2 = {}
					else:
						if result_temp2 != result_month:
							result_temp2.update(result_month)
							result_month = result_temp2
							result_temp2 = {}

					for k, v in result_month.items():
						result_temp2[k] = list(set(v))

					for k, v in result_temp2.items():
						if isinstance(v, list):
							for lf in filter(
								lambda x: sym_or_num_regex.findall(x), tuple(v)
							):
								if isinstance(lf, str) and all(
									(lf, not lf.strip() in files2)
								):
									files2.append(lf.strip())

					# if clear_before_load not_use_result_temp(result_month)

					# @files_by_month
					if files2:
						tmp = list(set(files2))
						with open(
							files_by_month, "w", encoding="utf-8"
						) as fbmf:  # w -> a
							fbmf.writelines(
								"%s\n" % f for f in filter(lambda x: x, tuple(tmp))
							)

						logging.info(
							"@files_by_month [%d] [%s]"
							% (len(tmp), str(datetime.now()))
						)  # files2 -> tmp

					# @month_base
					if result_temp2:
						with open(
							month_base, "w", encoding="utf-8"
						) as mbf:  # w -> a # debug
							json.dump(
								result_temp2,
								mbf,
								ensure_ascii=False,
								indent=4,
								sort_keys=True,
							)  # save_unique # debug

				if result_year:
					# @classify_by_folders
					try:
						with open(year_base, encoding="utf-8") as ybf:
							result_temp3 = json.load(ybf)
					except:  # if_error_read
						result_temp3 = {}
					else:
						if result_temp3 != result_year:
							result_temp3.update(result_year)
							result_year = result_temp3
							result_temp3 = {}

					for k, v in result_year.items():
						result_temp3[k] = list(set(v))

					for k, v in result_temp3.items():
						if isinstance(v, list):
							for lf in filter(
								lambda x: sym_or_num_regex.findall(x), tuple(v)
							):
								if isinstance(lf, str) and all(
									(lf, not lf.strip() in files3)
								):
									files3.append(lf.strip())

					# if clear_before_load not_use_result_temp(result_year)

					# @files_by_year
					if files3:
						tmp = list(set(files3))
						with open(
							files_by_year, "w", encoding="utf-8"
						) as fbyf:  # w -> a
							fbyf.writelines(
								"%s\n" % f for f in filter(lambda x: x, tuple(tmp))
							)

						logging.info(
							"@files_by_year [%d] [%s]" % (len(tmp), str(datetime.now()))
						)  # files3 -> tmp

					# @year_base
					if result_temp3:
						with open(
							year_base, "w", encoding="utf-8"
						) as ybf:  # w -> a # debug
							json.dump(
								result_temp3,
								ybf,
								ensure_ascii=False,
								indent=4,
								sort_keys=True,
							)  # save_unique # debug

			# find_folders_by_month(by_time) # is_all_days
			if all(
				(len(ftd) > 1, ftd[0] != None, ftd[1] >= 0, is_tvseries)
			):  # period=30 -> period=days # tvseries_only
				if is_found:  # desc(0/1), files(1) # some_found

					if template:
						tmp = [
							lf.strip()
							for t in template
							for lf in list_files
							if all((t, lf, lf.lower().endswith(t.lower())))
						]

						if tmp:  # add_with_template
							folder_desc_files.append(fsf)

					elif not template:
						folder_desc_files.append(fsf)  # add_without_template_by_count

					found_list.append(fsf.split("\\")[-1])  # file_or_folder

					# change_datetime_at_folder_by_last_(access/modify/create)_date
					maxdate_m = ""  # maxdate_c = maxdate_m = maxdate_a = ""

					try:
						files = [
							os.path.join(fsf, f)
							for f in os.listdir(fsf)
							if os.path.exists(os.path.join(fsf, f))
						]
						files = [f.strip() for f in files if os.path.isfile(f)]
					except:
						files = []

					try:
						maxdate_folder = os.path.getctime(
							fsf
						)  # create(min) # debug # pass_1_of_2
						# maxdate_folder = os.path.getatime(fsf) # access(max) # debug # pass_1_of_2
					except:
						maxdate_folder = None

					# maxdate_c = max(files, key=os.path.getctime) # 'C:\\Python27\\LICENSE.txt' # created
					# maxdate_a = max(files, key=os.path.getatime) # 'C:\\Python27\\LICENSE.txt' # access
					maxdate_m = max(
						files, key=os.path.getmtime
					)  # 'C:\\Python27\\LICENSE.txt' # modified

					try:
						maxdate_file = os.path.getmtime(
							maxdate_m
						)  # modify # debug # pass_2_of_2
					except:
						maxdate_file = None

					if all(
						(
							maxdate_folder != None,
							maxdate_file != None,
							maxdate_folder != maxdate_file,
						)
					):
						os.utime(
							fsf, times=(maxdate_folder, maxdate_file)
						)  # is_recovery_datetime # old -> new

					files = [
						f.strip()
						for f in filter(lambda x: video_regex.findall(x), tuple(files))
						if os.path.exists(f)
					]  # x.endswith("mp4")

					try:
						await redate_files(lst=files)
					except:
						pass

					# folder_desc_files # parse_soundtracks_from_filename

					desc_list: list = []
					parse_list: list = []
					# parse_filename: list = []

					def http_trace_to_soundtrack_parse(line: str = ""):

						# global parse_filename

						no_prot_ext: str = ""

						try:
							assert (
								line
							), f"Пустая строка @http_trace_to_soundtrack_parse/{line}"  # is_assert_debug
						except AssertionError as err:  # if_null
							logging.warning(
								f"Пустая строка @http_trace_to_soundtrack_parse/{line}"
							)
							raise err
							return no_prot_ext
						except BaseException as e13:  # if_error
							logging.error(
								"Пустая строка @http_trace_to_soundtrack_parse/line [%s]"
								% str(e13)
							)
							return no_prot_ext

						parse_regex = re.compile(r"http(.*)\.mp4", re.I)

						filename = line  # "http://data11-cdn.datalock.ru/fi2lm/7d2b2f94011f33cd73b7dbf603374c89/7f_The.Hundred.S07E11.720p.rus.LostFilm.TV.a1.14.08.20.mp4"
						try:
							no_prot_ext = parse_regex.findall(filename)[
								0
							]  # ://data11-cdn.datalock.ru/fi2lm/7d2b2f94011f33cd73b7dbf603374c89/7f_The.Hundred.S07E11.720p.rus.LostFilm.TV.a1.14.08.20
						except:
							no_prot_ext = ""

						if all((no_prot_ext, no_prot_ext.count("/") > 0)):
							no_prot_ext = (
								no_prot_ext.split("/")[-1]
								.replace("7f_", "")
								.replace(".", "_")
								.strip()
							)  # The_Hundred_S07E11_720p_rus_LostFilm_TV_a1_14_08_20

							# parse_filename.append(no_prot_ext)

							return no_prot_ext
						else:
							return no_prot_ext

					dt = datetime.now()

					try:
						dsize: int = disk_usage("d:\\").free
					except:
						dsize: int = 0

					is_backup: bool = False
					is_backup = (
						dt.hour >= 0,
						dsize // (1024**2) > 0,
					)  # debug # all_day # limit_1mb(ok) # is_default

					try:
						desc_list = [
							ld.strip()
							for ld in os.listdir(fsf)
							if ld.lower().endswith(".txt")
						]
					except BaseException as e14:  # if_null
						desc_list = []
						logging.info("%s" % ";".join([fsf, str(e14)]))
						# raise e14

					if all((len(desc_list) == 1, is_backup.count(True))):
						try:
							with open(
								"\\".join([fsf, desc_list[-1]]), encoding="utf-8"
							) as fdf:
								parse_list = fdf.readlines()
						except:
							parse_list = []

						# if_look_like_download_path_change_soundtracks # save_to(soundtrack_base)
						try:
							tmp = [
								"\\".join(
									[
										"c:\\downloads\\combine\\original\\tvseries",
										".".join(
											[http_trace_to_soundtrack_parse(pl), "mp4"]
										),
									]
								)
								for pl in filter(lambda x: x, tuple(parse_list))
								if http_trace_to_soundtrack_parse(pl)
							]  # http(s)...mp4
							assert (
								tmp
							), "Пустой список файлов @folders_from_path/tmp/#notvseries"  # is_assert_debug
						except AssertionError:  # if_null
							tmp = []
							logging.warning(
								"Пустой список файлов @folders_from_path/tmp/#notvseries/%s"
								% str(datetime.now())
							)  # when_null_folder
							# raise err
						except BaseException as e15:  # if_error
							tmp = []
							logging.error(
								"Пустой список файлов @folders_from_path/tmp/#notvseries/%s [%s]"
								% (str(datetime.now()), str(e15))
							)  # when_null_folder
						# finally: # hide_download_project_list_with_count
						# if tmp:
						# print("%d downloaded projects" % len(tmp)) #print(";".join(tmp)) #; print() # need_another_comment
						# sleep(0.5)

						st_list: list = []

						try:
							with open(files_base["stracks"], encoding="utf-8") as sf:
								st_list = sf.readlines()
						except:
							st_list = []

						try:
							with open(soundtrack_base, encoding="utf-8") as sbf:
								soundtrack_dict = json.load(sbf)
						except:
							soundtrack_dict = {}

						is_error = False

						# x[0].isalpha() -> x[0] == x[0].upper() # pass_1_of_2
						try:
							soundtrack_filter = {
								t.strip(): sl.strip()
								for sl in filter(
									lambda x: any(
										(
											x[0] == x[0].isalpha(),
											x[0] == x[0].isnumeric(),
										)
									),
									tuple(st_list),
								)
								for t in tmp
								if any(
									(
										sl.lower().strip() in t.lower().strip(),
										sl.strip() in t,
									)
								)
								and tmp
							}  # t.replace(sl, "*" * len(sl)).strip() # descrypt/debug
						except:
							soundtrack_filter = {}
							is_error = True
						else:
							is_error = False

						soundtrack_filter_top = {}

						# update_havent_soundtracks(filter) # pass_2_of_2
						soundtrack_filter_top = {
							k: v
							for k, v in soundtrack_filter.items()
							if all((k, not k in [*soundtrack_dict]))
						}  # if_new_soundtrack(filter_current_files)

						if any(
							(not soundtrack_filter, not soundtrack_filter_top)
						):  # if_some_null
							continue  # skip_desc_if_no_soundtrack

						if soundtrack_filter_top:
							soundtrack_filter = {}
							soundtrack_filter.update(soundtrack_filter_top)

						if all(
							(
								soundtrack_filter_top,
								len(soundtrack_dict) >= 0,
								is_error == False,
							)
						):  # it_was_new(else_skip) # some_soundtracks(or_newbase) # soundtrack_filter
							soundtrack_dict.update(
								soundtrack_filter
							)  # update_base_from_filter

							# soundtrack_tbase(decrypt/debug/backup) -> soundtrack_base(original) # file
							# soundtrack_filter(decrypt/debug) # soundtrack_dict(original/backup) # json

							# filter(lambda x: lst.count(x) != list(set(lst)).count(x), tuple(lst)) # search_moda

							# soundtrack_dict -> soundtrack_filter

							try:
								soundtrack_count = [
									(
										v.strip(),
										list(soundtrack_dict.values()).count(v.strip),
									)
									for k, v in soundtrack_dict.items()
									if sl.lower().strip() in k.lower().strip()
								]
							except:
								soundtrack_count = []
							else:
								if soundtrack_count:

									soundtrack_count_sorted = sorted(
										soundtrack_count,
										key=lambda soundtrack_count: soundtrack_count[
											1
										],
									)  # sorted_by_value
									soundtrack_count = [
										(scs[0], int(scs[1]))
										for scs in soundtrack_count_sorted
										if isinstance(soundtrack_count_sorted, tuple)
									]

									print(
										Style.BRIGHT
										+ Fore.CYAN
										+ "debug soundtrack_count[low] '%d soundtrack count'"
										% len(soundtrack_count)
									)  # is_color # %s/str

							try:
								soundtrack_count = {
									v.strip(): str(
										list(soundtrack_dict.values()).count(v.strip())
									)
									for k, v in soundtrack_dict.items()
								}
							except:
								soundtrack_count = {}
							else:
								if soundtrack_count:

									soundtrack_count_list = [
										(k, int(v)) for k, v in soundtrack_count.items()
									]
									soundtrack_count_sorted = sorted(
										soundtrack_count_list,
										key=lambda soundtrack_count_list: soundtrack_count_list[
											1
										],
									)  # sorted_by_value
									stc = {
										scs[0]: scs[1]
										for scs in soundtrack_count_sorted
									}  # sorted_json
									soundtrack_count = (
										stc if stc else {}
									)  # is_no_lambda

									print(
										Style.BRIGHT
										+ Fore.WHITE
										+ "debug soundtrack_count[combine] '%s'"
										% str(soundtrack_count)
									)  # is_color # %d/len

									try:
										soundtrack_count_new = {
											k: int(v)
											for k, v in soundtrack_count.items()
										}
										s = sum(list(soundtrack_count_new.values()))
										l = len(soundtrack_count_new)
										a = s / l
										class_dict = {
											k: round((v / s) * 100, 2)
											for k, v in soundtrack_count_new.items()
											if v - a > 0
										}  # 0..100%(popular_classify)
									except BaseException as e16:  # if_error
										class_dict = {}
										print(
											Style.BRIGHT
											+ Fore.RED
											+ "debug soundtrack_count[error] '%s %s'"
											% (str(None), str(e16))
										)
										logging.info(
											"@soundtrack_count[error] %s %s"
											% (str(None), str(e16)),
											is_error=True,
										)  # is_color
									else:
										try:
											sort_class = {
												s: v
												for s in sorted(
													class_dict,
													key=class_dict.get,
													reverse=False,
												)
												for k, v in class_dict.items()
												if all((s, k, v, s == k))
											}
										except:
											sort_class = {}

										if all(
											(
												sort_class,
												len(sort_class) <= len(class_dict),
											)
										):  # is_sorted_dict # less_or_equal
											class_dict = sort_class

										class_status = (
											str(class_dict) if class_dict else ""
										)  # is_no_lambda
										if class_status:
											print(
												Style.BRIGHT
												+ Fore.CYAN
												+ "debug soundtrack_count[popular] '%s'"
												% class_status
											)  # is_color
											logging.info(
												"@soundtrack_count[popular] %s"
												% class_status
											)

							with open(soundtrack_base, "w", encoding="utf-8") as sbf:
								json.dump(
									soundtrack_dict,
									sbf,
									ensure_ascii=False,
									indent=4,
									sort_keys=True,
								)  # is(decrypt/debug)

						# x[0].isalpha() -> x[0] == x[0].upper()

						with open(
							files_base["soundtrack"], "a", encoding="utf-8"
						) as fbsf:
							fbsf.writelines(
								"%s\n" % t.strip()
								for t in filter(
									lambda x: any(
										(
											x[0] == x[0].isalpha(),
											x[0] == x[0].isnumeric(),
										)
									),
									tuple(tmp),
								)
							)

				if is_not_found:  # desc(0), files(0) # create_null(any_time)
					try:
						if not os.path.exists("\\".join([fsf, "00s00e.txt"])):
							open(
								"\\".join([fsf, "00s00e.txt"]), "w", encoding="utf-8"
							).close()
					except:
						pass  # nothing_to_do_if_error # is_continue
					else:
						print(
							Style.BRIGHT
							+ Fore.CYAN
							+ "Описание и файлы не найдены в папке",
							Style.BRIGHT + Fore.WHITE + "%s" % fsf,
							end="\n",
						)  # is_color's
						logging.info("@fsf[is_not_found][ok] %s" % fsf)  # is_create

				if is_two_desc:  # desc(2), files(0/1) # delete_null(any_time)
					try:
						desc_list = [
							os.path.join(fsf, f)
							for f in filter(
								lambda x: x.lower().endswith(".txt"), os.listdir(fsf)
							)
							if os.path.exists(os.path.join(fsf, f))
						]

						assert desc_list, "В папке %s нет описания" % fsf
					except AssertionError as err:  # if null
						logging.warning("В папке %s нет описания" % fsf)
						raise err
					except BaseException as e17:  # if_error
						desc_list = []
						logging.error("Папка: %s, ошибка: %s" % (fsf, str(e17)))
					else:
						desc_list.sort(reverse=False)
						desc_status = (
							desc_list[0] if desc_list else None
						)  # first_file / no_description
						logging.info("Папка: %s, файл: %s" % (fsf, str(desc_status)))

					try:
						if (
							os.path.exists(desc_list[0]) and len(desc_list) >= 2
						):  # "\\".join([fsf, "00s00e.txt"])
							os.remove(desc_list[0])  # "\\".join([fsf, "00s00e.txt"])
					except:
						pass  # nothing_to_do_if_error # is_continue
					else:
						print(
							Style.BRIGHT
							+ Fore.YELLOW
							+ "Удаляю лишнее описание в папке",
							Style.BRIGHT + Fore.WHITE + "%s" % fsf,
							end="\n",
						)  # is_color's
						logging.info(
							"@fsf[is_two_desc_found][ok] %s" % fsf
						)  # is_delete

			# hide_if_not_need_sort
			# temp = sorted(found_list, reverse=False) # sort_by_string
			# temp = sorted(found_list, key=len, reverse=False) # sort_by_key

			if found_list:  # debug
				found_list = sorted(
					found_list, key=len, reverse=True
				)  # temp # reverse(False -> True)

				# debug # is_regenerate_every_time # any((x[0] == x[0].isalpha(), x[0] == x[0].isnumeric()
				with open(
					mydir4, "w", encoding="utf-8"
				) as mf:  # resave # debug # found_by_period
					mf.writelines(
						"%s\n" % fs.strip()
						for fs in filter(
							lambda x: sym_or_num.findall(x), tuple(found_list)
						)
					)  # int/str # is_all(lang)

	print(
		"Загрузка папок и период загрузки или обработки. Завершена... %s"
		% str(datetime.now()).split(" ")[-1]
	)  # is-color

	# if folder_scan:
	# print(folder_scan)

	try:
		all_list += folder_scan  # is_skip_await
	except:
		all_list = []

	# all_list = await all_list

	# return folder_scan # default


ffp: list = []

# '''
# async_create(new)
async def ffp_generate():

	global all_list

	# async with asyncio.TaskGroup() as tg:
	task1 = asyncio.create_task(
		folders_from_path(is_rus=True, is_tvseries=True, cntfiles=8),
		name="folders_from_path_rus",
	)  # old
	task2 = asyncio.create_task(
		folders_from_path(is_rus=False, is_tvseries=True, cntfiles=8),
		name="folders_from_path_no_rus",
	)  # old
	# task1 = tg.create_task(folders_from_path(is_rus = True, is_tvseries = True), name="folders_from_path_rus")
	# task2 = tg.create_task(folders_from_path(is_rus = False, is_tvseries = True), name="folders_from_path_no_rus")

	ffp.append(task1)  # old
	ffp.append(task2)  # old

	await asyncio.gather(*ffp)  # ok_if_runned / debug(is_no_return) # old


asyncio.run(ffp_generate())  # if_off_some_disk
# '''

# current_list(is_full) # is_ok
if all_list:
	try:
		tmp = list(
			set(
				[
					al.strip()
					for al in filter(
						lambda x: any(
							(x[0] == x[0].isalpha(), x[0] == x[0].isnumeric())
						),
						tuple(all_list),
					)
					if al
				]
			)
		)  # unique
	except:
		tmp = []  # null_if_error
	else:
		all_list = tmp  # int/str(no_error)


# @clear_segments
async def clear_segments(lst: list = []):
	try:
		files = [
			os.path.join(path_for_segments, f)
			for f in os.listdir(path_for_segments)
			if os.path.exists(os.path.join(path_for_segments, f))
		]
	except:
		files = []

	try:
		assert lst, ""
	except AssertionError:
		lst = []
		files2 = []
	else:
		files2 = lst

	try:
		seg1 = [fn.split(".")[0] for fp, fn in os.path.split(files)]  # segments
		seg2 = [fn.split(".")[0] for fp, fn in os.path.split(files2)]  # files
	except BaseException as e:
		seg1 = seg2 = []
		logging.error("@clear_segments [%s]" % str(e))
	finally:
		if all((seg1, seg2)):  # any -> all
			logging.info(
				"@clear_segments %d сегментов и %d файлов найдено для очистки"
				% (len(seg1), len(seg2))
			)
		elif any((seg1, seg2)):
			# @clear_segments 0 сегментов и 0 файлов частично найдено для очистки или нет данных
			logging.info(
				"@clear_segments %d сегментов и %d файлов частично найдено для очистки или нет данных"
				% (len(seg1), len(seg2))
			)

	# group_by_set # a = [1,2,3]; b = [2,4,6]
	# '''
	try:
		seg_filter = list(
			set(seg2) ^ set(seg1)
		)  # different(two_list) # [1, 3, 4, 6] # type1
		# seg_filter = list(set(seg2) & set(seg1)) # unique(two_list) # [2] # type2
		## seg_filter = list(set(seg1) - set(seg2)) # stay_different(only_first/clear_unique/one_list) # [1, 3] # type3
		assert seg_filter, ""
	except AssertionError:
		seg_filter = list(
			set(seg1) - set(seg2)
		)  # stay_different(only_first/clear_unique/one_list) # [1, 3] # type3
		logging.warning("@clear_segments[null] нет сегметов после фильтрации")
	except BaseException as e8:
		seg_filter = []
		logging.error("@clear_segments[error] [%s]" % str(e8))
	finally:
		if seg_filter:
			logging.info(
				"@clear_segments[filter] %d отфильтровано сегментов и файлов"
				% len(seg_filter)
			)
		else:
			logging.info("@clear_segments[filter] не найдено сегментов и файлов")
	# '''

	try:
		files = [
			f.strip() for f in files if f.split("\\")[-1].split(".")[0] in seg_filter
		]
		assert files, ""
	except AssertionError:
		files = []
		logging.warning("@files[null] Файлов для синхронизации сегментов не найдено")
	except BaseException as e:
		logging.error("@files[error] %s" % str(e))
	else:
		logging.info(
			"@files[some] Найдено %d файлов для синхронизации сегментов" % len(files)
		)

	need_delete_list: list = []

	for f in files:

		try:
			assert files, ""
		except AssertionError:
			break

		try:
			assert f and os.path.exists(f), ""
		except AssertionError:
			continue

		if not f in need_delete_list:
			need_delete_list.append(f)

	if need_delete_list:
		for ndl in need_delete_list:
			if os.path.exists(ndl):
				# os.remove(ndl) # debug
				# logging.info("@clear_segments[delete] Файл %s с отсутствующим сегментом удален" % ndl)
				logging.info(
					"@clear_segments[delete] Файл %s с отсутствующим сегментом удален!"
					% ndl
				)  # debug


asyncio.run(clear_segments(lst=all_list))


# 1684 [None, None] Текущий список папок, общий список папок # current_list_length / is_full_list / status's
all_list_status = (
	"Общий список в %d папках" % len(all_list)
	if all_list
	else "Общего списка в папках не найдено"
)  # str(debug) -> int(count) # is_no_lambda

print(
	Style.BRIGHT + Fore.YELLOW + "%d" % len(all_list),
	Style.BRIGHT + Fore.WHITE + "%s" % all_list_status,
)
logging.info(
	"@shared_list %d %s [%s]" % (len(all_list), all_list_status, str(datetime.now()))
)

# abc_or_num_regex = re.compile(r"^[A-Z0-9]", re.I)

try:
	# temp = list(set([al.strip() for al in all_list if abc_or_num_regex.findall(al)])) # filter_by_regex
	temp = list(set([al.strip() for al in tuple(all_list) if al]))
except:
	temp = []
finally:
	if all((temp, len(temp) <= len(all_list))):
		all_list = sorted(temp, reverse=False)  # sort_by_string
		# all_list = sorted(temp, key=len, reverse=False) # sort_by_legnth

os.chdir(r"c:\\downloads\\mytemp")  # is_change_drive_and_folder

# ff_to_days(ff: str = "", period: int = 7, is_dir: bool = False, is_less=True, is_any=False) # use_for_full_folders(date_modified_by_less_days)

# @ update_top(3types/2files)

# current.lst # files_base["current"](file) # 2
# cur_top.lst # top_folder(file) # 4
# top100_eng.lst # mydir3(path) # folders_from_path(is_rus=False) # top100_eng.lst -> eng.lst # 4(in)
# top100_rus.lst # mydir3(path) # folders_from_path(is_rus=True) # top100_rus.lst -> rus.lst # 4(in)
# curr.lst # for_manual_run # cur_top.lst -> curr.lst # 1

# x[0].isalpha() -> x[0] == x[0].upper()

# top100(rus+eng)_save # pass_1_of_4 # pass # @curr_top.lst(default)
with open(top_folder, "w", encoding="utf-8") as tff:
	tff.writelines(
		"%s\n" % al.strip()
		for al in filter(
			lambda x: any((x[0] == x[0].isalpha(), x[0] == x[0].isnumeric())),
			tuple(all_list),
		)
	)  # is_top

# top_list = all_list

filter_top_list = [al.strip() for al in tuple(all_list) if al]  # shorts

# load_meta_base(fitler) #1
try:
	with open(some_base, encoding="utf-8") as sbf:
		somebase_dict = json.load(sbf)
except:
	somebase_dict = {}

	with open(some_base, "w", encoding="utf-8") as sbf:
		json.dump(somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True)

if filter_top_list:

	# old # only_folders / no_backup # is_count_equal_template
	filter_top_by_folders = list(
		set(
			[
				ftl.strip()
				for ftl in filter_top_list
				for k in [*somebase_dict]
				if ftl.strip() and k.split("\\")[-1].startswith(ftl)
			]
		)
	)  # k, _ in somebase_dict.items()

	filter_get_middle = (
		len(filter_top_by_folders) // 2
		if len(filter_top_by_folders) // 2 > 0
		else len(filter_top_by_folders)
	)  # middle / full

	filter_top_by_folders = (
		filter_top_by_folders[0:100]
		if len(filter_top_by_folders) > 100
		else filter_top_by_folders
	)  # only_100/less_100 # is_need_sort # top_100
	# filter_top_by_folders.sort(reverse=False)

	# '''
	def topfolder_write(
		filename: str = "", lst: list = [], isalpha: bool = True, isnumeric: bool = True
	):
		if all((isalpha, isnumeric)):
			with open(filename, "w", encoding="utf-8") as tff:  # top_folder -> filename
				tff.writelines(
					"%s\n" % l.strip()
					for l in filter(
						lambda x: any(
							(x[0] == x[0].isalpha(), x[0] == x[0].isnumeric())
						),
						tuple(lst),
					)
				)  # int/str # is_top # filter_top_by_folders -> lst
		elif all((isalpha, not isnumeric)):
			with open(filename, "w", encoding="utf-8") as tff:  # top_folder -> filename
				tff.writelines(
					"%s\n" % l.strip()
					for l in filter(lambda x: x[0] == x[0].isalpha(), tuple(lst))
				)  # str # is_top # filter_top_by_folders -> lst
		else:
			with open(filename, "w", encoding="utf-8") as tff:  # top_folder -> filename
				tff.writelines(
					"%s\n" % l.strip() for l in filter(lambda x: x, tuple(lst))
				)  # any # is_top # filter_top_by_folders -> lst

	# '''

	# top100(rus+eng)_by_template # pass_2_of_3 # pass # @cur_top.lst
	# if filter_top_by_folders:
	# with open(top_folder, "w", encoding="utf-8") as tff:
	# tff.writelines("%s\n" % ftbf.strip() for ftbf in filter(lambda x: any((x[0] == x[0].isalpha(), x[0] == x[0].isnumeric())), tuple(filter_top_by_folders))) # int/str # is_top

	logging.info(
		"@filter_get_middle[count] %d [%s]" % (filter_get_middle, str(datetime.now()))
	)

	dt = datetime.now()

	days = 366 if dt.year % 4 == 0 else 365  # by_year # is_no_lambda

	filter_for_new_backup = list(
		set(
			[
				k.strip()
				for k in [*somebase_dict]
				if ff_to_days(
					ff=k, period=days, is_dir=False, is_less=False, is_any=True
				)[0]
				!= None
			]
		)
	)  # by_Year # type1 # for k, _ in somebase_dict.items()
	# filter_for_new_backup = list(set([k.strip() for k in [*somebase_dict] if ff_to_days(ff = k, period = 12*days, is_dir=False, is_less=True, is_any=False)[0] != None])) # 12_year_and_less # type2 # for k, v in somebase_dict.items()

	filter_for_new_backup = (
		filter_for_new_backup[0:100]
		if len(filter_for_new_backup) > 100
		else filter_for_new_backup
	)  # only_100/less_100 # is_need_sort # top_100
	# filter_for_new_backup.sort(reverse=False)

	# top100(rus+eng)_by_template # pass_3_of_3 # pass # @curr.lst
	# if filter_for_new_backup:
	# with open(top_folder2, "w", encoding="utf-8") as tff2:
	# tff2.writelines("%s\n" % ffnb.strip() for ffnb in filter(lambda x: any((x[0] == x[0].isalpha(), x[0] == x[0].isnumeric())), tuple(filter_for_new_backup))) # int/str # is_top

	logging.info(
		"@filter_for_new_backup[count] %d [%s]"
		% (len(filter_for_new_backup), str(datetime.now()))
	)

	# config = {"ff": fsf, "period": 30, "is_dir": False, "is_less": True, "is_any": False} # **config # fsf(default) -> None(debug)
	# ff_to_days(ff=fsf, period=30, is_dir=False, is_less=True, is_any=False)[0] != None # top_folder2 # curr.lst # date_modified_by_less_days

	# check_last_backup

	clb: list = []

	# try_load_last_backup
	try:
		with open(files_base["backup"], encoding="utf-8") as bjf:
			clb = bjf.readlines()
	except:
		clb = []

	# """
	async def save_top_folder():
		tasks = []

		task1 = asyncio.create_task(
			topfolder_write(filename=top_folder, lst=filter_top_by_folders)
		)
		task2 = asyncio.create_task(
			topfolder_write(filename=top_folder2, lst=filter_for_new_backup)
		)
		task3 = asyncio.create_task(
			topfolder_write(
				filename=files_base["backup"],
				lst=filter_for_new_backup,
				isnumeric=False,
			)
		)

		tasks.append(task1)
		tasks.append(task2)
		tasks.append(task3)

		await asyncio.gather(*tasks)

	asyncio.run(save_top_folder())
	# """


async def memory_usage_psutil(proc_id) -> any:
	# return the memory usage in percentage like top

	try:
		process = psutil.Process(proc_id)  # os.getpid()
		mem = process.memory_percent()

		assert (
			mem
		), f"Ошибка сохранения значения памяти @memory_usage_psutil/{mem}"  # is_assert_debug
	except AssertionError as err:  # if_null
		mem = 0
		logging.warning(f"Ошибка сохранения значения памяти @memory_usage_psutil/{mem}")
		raise err
	except BaseException as e:  # if_error
		mem = 0
		logging.error(
			"Ошибка сохранения значения памяти @memory_usage_psutil/mem [%s]" % str(e)
		)

	return mem


# is_overload_process
try:
	curProcesses = psutil.process_iter()
except:
	curProcesses = None

if curProcesses:
	for eachProcess in curProcesses:
		# Observe the two different forms of access.
		try:
			mem: float = asyncio.run(
				memory_usage_psutil(int(eachProcess.pid))
			)  # print(eachProcess.pid)

			if int(mem) > 80:  # "80"->85
				print(eachProcess.name(), end="\n")
				logging.warning("Overload: %s" % eachProcess.name())

				if all(
					(
						not eachProcess.name() in big_process,
						not eachProcess.name() in skip_process,
					)
				):
					big_process.append(eachProcess.name())

					if not eachProcess.pid in pid_process:
						pid_process.append(eachProcess.pid)

				with open(
					"c:\\downloads\\mytemp\\overload.csv", "a", newline=""
				) as ocf:
					ocf.write(
						";".join([str(eachProcess.pid), str(eachProcess.name())]) + "\n"
					)

		except:
			mem: float = 0
	else:  # is_no_break
		print("Процессы проанализированы")

	# debug
	# exit

	if any((big_process, pid_process)):
		print(big_process, pid_process, end="\n")

# delete_last_days_log
new_dict: dict = {}

open(log_print, "w", encoding="utf-8").close()


def write_log(
	desc: str = "", txt: str = "", is_error: bool = False, is_logging: bool = False
):  # event_log(is_all)

	try:
		assert desc, f"Пустое описание @write_log/desc/{txt}"  # is_assert_debug
	except AssertionError:  # as err:  # if_null
		desc = str(None)
		logging.warning("Пустое описание @write_log/%s/%s" % (desc, txt))
		# raise err # have_null
	except BaseException as e:  # if_error
		logging.error("Пустое описание @write_log [%s]" % str(e))
		# return

	try:
		assert txt, "Пустой комменатрий @write_log/desc/txt"  # is_assert_debug
	except AssertionError:  # as err:  # if_null
		txt = str(None)
		logging.warning("Пустой комменатрий @write_log/%s/%s" % (desc, txt))
		# raise err # have_null
	except BaseException as e:  # if_error
		logging.error("Пустой комментарий @write_log [%s]" % str(e))
		# return

	global log_dict  # debug

	try:
		with open(log_base, encoding="utf-8") as lbf:
			log_dict = json.load(lbf)
	except:
		log_dict = {}

		with open(log_base, "w", encoding="utf-8") as lbf:
			json.dump(log_dict, lbf, ensure_ascii=False, indent=4)

	# add_any_error_from_logging_to_errorbase
	try:
		with open(error_base, encoding="utf-8") as ebf:
			error_dict = json.load(ebf)
	except:
		error_dict = {}

		with open(error_base, "w", encoding="utf-8") as ebf:
			json.dump(error_dict, ebf, ensure_ascii=False, indent=4, sort_keys=True)

	if all((desc != None, txt != None, isinstance(desc, str), isinstance(txt, str))):
		if any(
			(
				"error" in txt.lower().strip(),
				"error" in desc.lower().strip(),
				is_error == True,
			)
		):
			logging.error(txt.strip())  # logging_with_error
			error_dict[desc.strip()] = ",".join(["video_resize.py", txt.strip()])
		if all((txt.strip(), is_logging == True)):  # is_error != True
			# logging.info(";".join([desc.strip(), txt.strip()])) # logging
			logging.info(
				" ".join([desc.strip().replace("debug ", "@"), txt.strip()])
			)  # logging # debug

		log_dict[desc.strip()] = txt.strip()

	try:
		dsize: int = disk_usage("c:\\").free
		assert dsize, ""
	except AssertionError:
		pass
	else:
		with open(log_base, "w", encoding="utf-8") as lbf:
			json.dump(log_dict, lbf, ensure_ascii=False, indent=4, sort_keys=True)

		if error_dict:  # save_any_error_dict(skip_null)
			with open(error_base, "w", encoding="utf-8") as ebf:
				json.dump(
					error_dict, ebf, ensure_ascii=False, indent=4, sort_keys=True
				)  # errors(+exists)

		if os.path.exists(log_base) and os.path.getsize(log_base):
			fsizes_lst = [
				(os.path.getsize(log_base) // (1024**i), i)
				for i in range(1, 4)
				if os.path.getsize(log_base) // (1024**i) > 0
			]
			logging.info("@dsize write_log[1] size: %s" % str(fsizes_lst))
		else:
			logging.info("@dsize write_log[1] dsize: %dMb" % dsize // (1024**2))

	# logging(old/plain)

	lprint: list = []

	try:
		with open(log_print, encoding="utf-8") as lpf:
			lprint = lpf.readlines()
	except:
		lprint: list = []
	else:
		if all((desc, txt)):
			lprint.append("%s:%s\n" % (desc.strip(), txt.strip()))

	if lprint:
		check_log = set()

		for lp in filter(lambda x: x, tuple(lprint)):

			try:
				assert len(lp.strip()) > 0, "Строка пустая"
			except AssertionError as err:
				raise err  # logging.warning
				continue

			if not lp in check_log:
				check_log.add(lp)

		if all((check_log, len(check_log) != len(lprint))):
			lprint = sorted(list(check_log), reverse=False)  # wit_abc(set->list)
			# lprint = list(check_log)  # with_abc(set->list)

		try:
			dsize: int = disk_usage("c:\\").free
			assert dsize, ""
		except AssertionError:
			pass
		else:
			with open(log_print, "w", encoding="utf-8") as lpf:
				lpf.writelines(
					"%s\n" % lp.strip() for lp in filter(lambda x: x, tuple(lprint))
				)  # not_null(logging)

			if os.path.exists(log_print) and os.path.getsize(log_print):
				fsizes_lst = [
					(os.path.getsize(log_print) // (1024**i), i)
					for i in range(1, 4)
					if os.path.getsize(log_print) // (1024**i) > 0
				]
				logging.info("@dsize write_log[2] size: %s" % str(fsizes_lst))
			else:
				logging.info("@dsize write_log[2] dsize: %dMb" % dsize // (1024**2))


# check_function_by_error(logging)
def log_error(f):
	def inner(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except BaseException as e:
			write_log("debug error", "%s" % str(e), is_error=True)
			logging.error("%s" % str(e))
			# raise e

	return inner


# Равных по времени? # ffmpeg -i input.mkv -c copy -f segment -segment_time 10 -y output%03d.mkv # 10sec(every_part)
# Или по размеру файла? # mkvmerge -o output.mkv --split 100M input.mkv # 100mb(every_part)


async def mp4_to_m3u8(
	filename: str = "", is_run: bool = False, is_stay: bool = False, ext: str = "mp4"
) -> tuple:

	try:
		assert filename and os.path.exists(
			filename
		), f"Файл отсутствует @mp4_to_m3u8/{filename}"  # is_assert_debug # filename
	except AssertionError as err:  # if_null
		logging.warning("Файл отсутствует @mp4_to_m3u8/%s" % filename)
		raise err
		return (False, "", "no_run")
	except BaseException as e:  # if_error
		logging.error("Файл отсутствует @mp4_to_m3u8/%s [%s]" % (filename, str(e)))
		return (False, "", "no_run")

	try:
		folder = "\\".join(filename.split("\\")[0:-1]).strip()
	except:
		folder = ""

	# some_ext: str = ""

	try:
		fname = filename.split("\\")[-1]
	except:
		fname = ""
	# else:
	# if all((filename.split(".")[-1] != ext, ext)):
	# some_ext = filename.split(".")[-1]

	try:
		if not os.path.exists(path_for_segments):
			os.mkdir(path_for_segments)
	except:
		os.system(
			'cmd /c mkdir "%s"' % path_for_segments
		)  # create_null_m3u8_by_job # cmd /k

	try:
		m3u8_file = "".join(
			[path_for_segments, ".".join([fname.split(".")[0], "m3u8"])]
		)
	except:
		m3u8_file = ""
	else:
		if not os.path.exists(m3u8_file) and m3u8_file:
			os.system(
				'cmd /c copy nul "%s"' % m3u8_file
			)  # create_null_m3u8_by_job # cmd /k

	cmd: str = ""

	# %filename%.m3u8 (main_m3u8_playlist) # %filename%%index%.ts (parts_count)

	async def seg_and_playlist_counts(fname: str = "") -> tuple:

		m3u8_regex = re.compile(
			r"^(%s)(.*)(?:(m3u8|ts))$" % fname, re.I
		)  # "filename" / is_index / "m3u8(ts)" # IgnoreCase

		some_files = [
			m3u8_regex.findall(lf)
			for lf in os.listdir(path_for_segments)
			if m3u8_regex.findall(lf)
		]  # save_found_tuple_to_list

		playlist_count: int = 0
		index_count: int = 0

		for sf in some_files:
			if len(sf) == 3:
				index_count += 1
			elif len(sf) == 2:
				playlist_count += 1
			else:  # <2 # >3
				continue

			# print(sf) # (filename, is_index, is_ext) # (filename, is_ext)

		return (index_count, playlist_count)

	if all((folder, fname, m3u8_file)):
		# ffmpeg -hide_banner -y -i "input.mp4" -threads 2 -c:a aac -af "dynaudnorm" -f segment -segment_time 1200 -threads 2 -c:v libx264 -vf "scale=-640:-1,pp=al" -reset_timestamps 1 -map 0 "output_0%dp.mp4" # ffmpeg/every_20min(by_parts)
		# ffmpeg -hide_banner --user -i "filename.mp4" -threads 2 -c copy -start_number 0 -hls_time 1200 -hls_list_size 0 -f hls "filename.m3u8" # ffmpeg/every_20min(mp4->m3u8)
		cmd = (
			"cmd /c "
			+ "".join([path_for_queue, "ffmpeg.exe"])
			+ ' -hide_banner -y -i "%s" -preset medium -threads 2 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls "%s"'
			% (filename, m3u8_file)
		)

		if is_run:
			try:
				p = os.system(cmd)
				assert bool(p == 0), ""
			except AssertionError:
				if p != 0:
					if os.path.exists(m3u8_file):  # delete_if_error_run
						os.remove(m3u8_file)

					return (False, cmd, "run")
			else:
				if p == 0:
					if is_stay == False and os.path.exists(
						m3u8_file
					):  # delete_if_stay_false
						os.remove(m3u8_file)

					try:
						index_count, playlist_count = await seg_and_playlist_counts(
							fname=fname
						)
					except:
						index_count = playlist_count = 0
					else:
						if any(
							(index_count, playlist_count)
						):  # ts_segment_count / playlist_count
							print(
								"Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]"
								% (
									index_count,
									playlist_count,
									filename,
									str(datetime.now()),
								)
							)
							write_log(
								"debug counts",
								"Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]"
								% (
									index_count,
									playlist_count,
									filename,
									str(datetime.now()),
								),
							)

					return (True, cmd, "run")

		elif not is_run:
			if is_stay == False and os.path.exists(m3u8_file):  # delete_if_stay_false
				os.remove(m3u8_file)

			try:
				index_count, playlist_count = await seg_and_playlist_counts(fname=fname)
			except:
				index_count = playlist_count = 0
			else:
				if any(
					(index_count, playlist_count)
				):  # ts_segment_count(is_null) / playlist_count
					print(
						"Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]"
						% (index_count, playlist_count, filename, str(datetime.now()))
					)
					write_log(
						"debug counts",
						"Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]"
						% (index_count, playlist_count, filename, str(datetime.now())),
					)

			return (True, cmd, "no_run")


# @log_error
async def myboottime() -> tuple:
	# global hbd

	hbd: int = 0  # hours_by_days

	# 1622103515 unixdate / 8600 daytime / 3600 hours

	"""
	import psutil
	from datetime import datetime

	# returns the time in seconds since the epoch
	last_reboot = psutil.boot_time()

	# converting the date and time in readable format
	print(datetime.fromtimestamp(last_reboot)) # 2021-10-22 11:38:05.776664

	mdate = datetime.fromtimestamp(last_reboot)

	dnow = datetime.now()

	ddate = int(abs(mdate - dnow).seconds) // 3600 # different_by_hours

	print(ddate) # 20

	# need_difference_for_days
	"""
	# True - days_by_hour, False - hours

	last_reboot = psutil.boot_time()

	mdate = datetime.fromtimestamp(last_reboot)

	dnow = datetime.now()

	is_hd_status: bool = False

	try:
		ddate: int = int(abs(mdate - dnow).seconds) // 3600  # different_by_hours

		assert (
			ddate >= 0
		), f"Пустое количество часов или только включили PC @myboottime/{ddate}"  # is_assert_debug
	except AssertionError as err:  # if_null
		ddate: int = 0
		logging.warning(
			f"Пустое количество часов или только включили PC @myboottime/{ddate}"
		)
		raise err
	except BaseException as e:  # if_error
		ddate: int = 0
		logging.error(
			"Пустое количество часов или только включили PC @myboottime/ddate [%s]"
			% str(e)
		)

	try:
		if ddate > 24:  # more_day
			hbd = ddate // 24  # days_by_hours
			write_log(
				"debug daytime", "started %d days ago" % hbd
			)  # debug daytime:"started 4 days 52 hours ago"
			is_hd_status = True
		elif ddate <= 24:  # one_day
			hbd = ddate  # hours
			write_log("debug daytime", "started today %d hours ago" % ddate)
			is_hd_status = False
	except:
		write_log("debug daytime", "unknown boottime")
		hbd = 666  # if_error_null_days

	return (hbd, is_hd_status)


dayago, is_hd_status = asyncio.run(myboottime())  # temporary_hidden

try:
	if dayago != 666:
		if is_hd_status:
			print("Days ago %d" % dayago)
			logging.info("Days ago %d" % dayago)
		elif is_hd_status == False:
			print("Hours ago %d" % dayago)
			logging.info("Hours ago %d" % dayago)
except:
	write_log("debug worktime[mac]", "Unknown days/hours")
	logging.error("debug worktime[mac] Unknown days/hours")

write_log("debug start", f"{str(datetime.now())}")

# debug
# exit()

# """
# from mac_vendor_lookup import MacLookup # pip install --user mac-vendor-lookup
# from mac_vendor_lookup import AsyncMacLookup

# print(MacLookup().lookup("00:80:41:12:FE")) #VEB KOMBINAT ROBOTRON

dt = datetime.now()

dt_day = 0

if dt.month == 2:  # 28/29days
	if dt.year % 4 != 0:
		dt_day = 28
	elif dt.year % 4 == 0:
		dt_day = 29
elif dt.month in [4, 6, 9, 11, 12]:  # 30days
	dt_day = 30
elif dt.month in [1, 3, 5, 7, 8, 10]:  # 31days
	dt_day = 31


async def find_mac(mac_address: str = ""):
	# update_mac_address_database # hide_for_debug
	# if any((dt.day == 1, dt.day % 5 == 0, all((dt.day == dt_day, dt_day)))) and any((dt.hour < 9, dt.hour > 18)): # every_first_day/every_5day/every_optimal_end_month(update_if_no_job_time)
	try:
		mac = MacLookup()  # default
	except:
		mac = await MacLookup()  # if_error

	try:
		mac.update_vendors()  # <- This can take a few seconds for the download #is_json
	except:
		await mac.update_vendors()

	try:
		m_to_v = await mac.lookup(mac_address)
	except:
		m_to_v = str(datetime.now())  # str(None)
		# print(mac.lookup(mac_address))

	return m_to_v


# async def main():
# mac = AsyncMacLookup()
# print(await mac.lookup("98:ED:5C:FF:EE:01"))
# """

# https://macvendors.com/

lanmacs: dict = {}  # use_macs_in_squid_rules(for_proxy)
acl: dict = {}

# default_load

try:
	with open("".join([script_path, "\\lanmacs.json"]), encoding="utf-8") as ljf:
		lanmacs = json.load(ljf)
except:
	with open("".join([script_path, "\\lanmacs.json"]), "w", encoding="utf-8") as ljf:
		json.dump(lanmacs, ljf, ensure_ascii=False, indent=4, sort_keys=True)


try:
	with open("".join([script_path, "\\squid.json.acl"]), encoding="utf-8") as sajf:
		acl = json.load(sajf)
except:
	with open(
		"".join([script_path, "\\squid.json.acl"]), "w", encoding="utf-8"
	) as sajf:
		json.dump(acl, sajf, ensure_ascii=False, indent=4, sort_keys=True)


# squid_rules(generate_values_to_rules)
"""
acl iptv arp c4:2f:ad:59:20:28 #ip.split(".")[-1] #?type
http_access access iptv
"""


async def ip_to_mac(ip: str = "") -> tuple:  # single_by_async

	try:
		# eth_mac = get_mac_address(interface="eth0") # linux
		# win_mac = get_mac_address(interface="Ethernet 3") # "linux"
		ip_mac = get_mac_address(ip=ip, network_request=True)  # "192.168.0.1" # default
		# ip6_mac = get_mac_address(ip6="::1")
		# host_mac = get_mac_address(hostname="localhost") # is_need
		# updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)
	except:
		ip_mac = ""

	"""
	# Enable debugging
	from getmac import getmac
	getmac.DEBUG = 2  # DEBUG level 2
	print(getmac.get_mac_address(interface="Ethernet 3"))

	# Change the UDP port used for updating the ARP table (UDP packet)
	from getmac import getmac
	getmac.PORT = 44444  # Default is 55555
	print(getmac.get_mac_address(ip="192.168.0.1", network_request=True))
	"""

	try:
		with open("".join([script_path, "\\squid.json.acl"]), encoding="utf-8") as sajf:
			acl = json.load(sajf)
	except:
		with open(
			"".join([script_path, "\\squid.json.acl"]), "w", encoding="utf-8"
		) as sajf:
			json.dump(acl, sajf, ensure_ascii=False, indent=4, sort_keys=True)

	if all((ip, ip_mac)):
		print("Получаю сведения ip: %s" % ip)
		print("Сведения ip, mac: %s" % ";".join([ip, ip_mac]))
		write_log(
			"debug ip_to_mac", ";".join([ip, ip_mac, str(datetime.now())])
		)  # only_positive

		if not ip_mac.strip() in [*acl]:  # if_new(onlydate)
			today_check = str(datetime.today()).split(" ")[0]

			# acl iptv arp c4:2f:ad:59:20:28 #181 # http_access access iptv # ?datetime # rules_for_squid_from_json
			try:
				mac_to_vendor = await find_mac(
					mac_address=ip_mac.replace("-", ":").upper()
				)  # asyncio.run
				asyncio.sleep(0.05)  # is_async_run # debug
				assert mac_to_vendor, ""
			except AssertionError:  # if_null
				mac_to_vendor = (
					str(datetime.now())
					if not str(datetime.today()).split(" ")[0] in str(datetime.now())
					else today_check
				)  # update_datetime/date_no_time
			except BaseException:  # if_error
				mac_to_vendor = str(None)

			try:
				assert ip_mac.strip() in [*acl], (
					"Нет записи о %s" % ip_mac.strip()
				)  # is_assert_debug
			except AssertionError as err:
				logging.warning("Нет записи о %s" % ip_mac.strip())
				raise err
				acl[ip_mac.strip()] = [
					"acl ip%s arp %s #%s"
					% (ip.split(".")[-1], ip_mac, ip.split(".")[-1]),
					"http_access access ip%s" % ip.split(".")[-1],
					mac_to_vendor,
					"new!",
				]
			else:
				logging.info("Обновление записи о %s" % ip_mac.strip())
				acl[ip_mac.strip()] = [
					"acl ip%s arp %s #%s"
					% (ip.split(".")[-1], ip_mac, ip.split(".")[-1]),
					"http_access access ip%s" % ip.split(".")[-1],
					mac_to_vendor,
					"update",
				]
				acl[ip_mac.strip()][2] = (
					str(datetime.now())
					if not str(datetime.today()).split(" ")[0] in acl[ip_mac.strip()][2]
					else str(datetime.today()).split(" ")[0]
				)  # full/date_no_time

	elif not ip_mac:
		# print("Нет сведений по ip: %s и он был пропущен" % ip) # no_negative
		write_log("debug ip_to_mac[nomac]", "%s [%s]" % (ip, str(datetime.now())))

	if acl:  # some_acl_squid_rules
		with open(
			"".join([script_path, "\\squid.json.acl"]), "w", encoding="utf-8"
		) as sajf:
			json.dump(acl, sajf, ensure_ascii=False, indent=4, sort_keys=True)

	return (ip, ip_mac)


# >>> ip_address = '123.45.67.89'
# >>> numbers = list(map(int, ip_address.split('.')))
# >>> '2002:{:02x}{:02x}:{:02x}{:02x}::'.format(*numbers)
# '2002:7b2d:4359::'


def ipv4_to_ipv6(
	ip_address: str = "127.0.0.1",
):  # if_offline_convert_ipv4_to_ipv6 # no_async
	numbers: list = []  # ip_address(list)
	host: str = ""  # hostname

	try:
		if len(ip_address.split(";")) == 1:  # ipv4
			numbers = list(map(int, ip_address.split(".")))  # ipv6(only_ipv6/list)
		elif len(ip_address.split(";")) > 1:  # hostname / ipv4
			try:
				host = ip_address.split(";")[0]  # hostname(first/str)
			except:  # if_error(hostname)
				host = str(None)

			numbers = list(
				map(int, ip_address.split(";")[-1].split("."))
			)  # ipv6(second/list)
		else:  # if_unknown
			return "Offline"  # min(no_ip) # "Unknown"
	except:  # if_error
		return "Offline"  # no_ip # "Error"
	else:
		if all((numbers, not host)):
			return "2002:{:02x}{:02x}:{:02x}{:02x}::".format(*numbers)  # ipv6
		elif all((numbers, host)):
			return ";".join(
				[host, "2002:{:02x}{:02x}:{:02x}{:02x}::".format(*numbers)]
			)  # hostname/ipv6
		else:
			return "Offline"  # if_unknown


squid_base2: str = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\squid.json.acl"
squid_base: str = "".join([script_path, "\\squid.json.acl"])
squidr_base2: str = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\squid.acl"
squidr_base: str = "".join([script_path, "\\squid.acl"])

# backup_json_to_list
try:
	with open(squid_base, encoding="utf-8") as sajf:
		acl = json.load(sajf)
except:
	acl = {}
else:
	if acl:
		open(squidr_base, "w", encoding="utf-8").close()  # clean
		with open(squidr_base, "a", encoding="utf-8") as saf:  # append(is_unique)
			saf.writelines("%s\n" % v[0] for _, v in acl.items())  # rule
			saf.writelines("%s\n" % v[1] for _, v in acl.items())  # access

		acl_list: list = []

		try:
			with open(squidr_base, encoding="utf-8") as saf:  # load(ready)
				acl_list = list(
					set(
						[s.strip() for s in filter(lambda x: x, tuple(saf.readlines()))]
					)
				)  # read_rules_and_access
		except:
			acl_list = []
		else:
			acl_list.sort(reverse=False)  # sort(rules/access)_for_squid

			if acl_list:
				with open(squidr_base, "w", encoding="utf-8") as saf:  # resave(sorted)
					saf.writelines("%s\n" % al for al in acl_list)  # rules_and_access

				if os.path.getsize(squidr_base):
					if os.path.exists(squidr_base2) and any(
						(
							os.path.getsize(squidr_base)
							!= os.path.getsize(squidr_base2),
							os.path.getmtime(squidr_base)
							> os.path.getmtime(squidr_base2),
						)
					):
						copy(squidr_base, squidr_base2)
					elif not os.path.exists(squidr_base2):
						copy(squidr_base, squidr_base2)


async def hostname_and_ip() -> tuple:  # get_hostname_and_ip

	try:
		hostname = socket.gethostname()  # default_hostname
	except:
		hostname = ""

	try:
		IPAddr = socket.gethostbyname(hostname)  # default_ip
	except:
		IPAddr = ""
	finally:
		try:
			assert hostname, ""
		except AssertionError:
			try:
				hostname = socket.getfqdn(
					IPAddr
				)  #  DESKTOP-L7B4S7M (I'm in a windows machine) # is_hostname
			except AssertionError:
				hostname = socket.gethostname()  # is_ip

	try:
		assert (
			hostname and IPAddr
		), f"Пустой Host или IP, @hostname_and_ip/{hostname}/{IPAddr}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(
			"Пустой Host или IP, @hostname_and_ip/%s/%s" % (hostname, IPAddr)
		)
		raise err
		return ("", "")
	except BaseException as e:  # if_error
		logging.error(
			"Пустой Host или IP, @hostname_and_ip/%s/%s [%s]"
			% (hostname, IPAddr, str(e))
		)
		return ("", "")

	write_log(
		"debug hostname_and_ip", ";".join([hostname, IPAddr, str(datetime.now())])
	)  # positive

	return (hostname, IPAddr)  # ('SergeyPC', '192.168.1.109')


async def current_ip() -> tuple:  # get_ip_by_current_lan

	try:
		host, ip = await hostname_and_ip()
	except:
		host = ip = ""

	try:
		assert ip, f"Пустой ip адресс @current_ip/{ip}"  # is_assert_debug
	except AssertionError as err:  # if_null
		ip = ""
		logging.warning("Пустой ip адресс @current_ip/ip")
		raise err
	except BaseException as e:  # if_error
		ip = ""
		logging.error("Пустой ip адресс @current_ip/ip [%s]" % str(e))
	else:
		write_log(
			"debug current_ip", "%s [%s]" % (";".join([ip, host]), str(datetime.now()))
		)  # positive

	return (ip, host)


async def ipconfig_to_base():

	global lanmacs

	try:
		ip_address, _ = await current_ip()  # ip_template
	except:
		ip_address = ""

	ip: str = ""

	if ip_address.count(".") == 3:
		ip = ".".join(ip_address.split(".")[:-1])  # 192.168.1

	if ip:  # ip_range
		for i in range(1, 255):

			curr_ip = ".".join([ip, str(i)])

			try:
				cip, cmac = await ip_to_mac(ip=curr_ip)
				assert cmac, ""  # is_assert_debug # if_mac_null
			except AssertionError:  # if_null
				continue  # if_null_skip_ip
			except BaseException:  # if_error
				cip = cmac = ""
				continue  # if_error_skip_ip
			else:
				if all((cmac, cip)):  # save_if_all_info
					write_log(
						"debug ipconfig_to_base[mac]",
						"%s [%s]" % (cmac, str(datetime.now())),
					)
					write_log(
						"debug ipconfig_to_base[ip]",
						"%s [%s]" % (cip, str(datetime.now())),
					)

					# mac_to_vendor(combine_info) # manual_base(is_no_ban)

					# try:
					# mac_to_vendor = MacLookup().lookup(cmac) # "cc:32:e5:59:ae:12" # 'TP-LINK TECHNOLOGIES CO.,LTD.'
					# except:
					# mac_to_vendor = ""

					try:
						last_info = lanmacs[cmac.strip()]
					except:
						last_info = ""

					# socket.gethostbyaddr("192.168.1.1") #('MYSHARE', [], ['192.168.1.1']) # socket.gethostbyaddr("192.168.1.1")[0] # 'MYSHARE'
					# socket.getfqdn("192.168.1.1") #  'MYSHARE' (I'm in a windows machine)
					try:
						combine_info = (
							";".join(
								[socket.gethostbyaddr(curr_ip)[0].strip(), cip.strip()]
							)
							if socket.gethostbyaddr(curr_ip)
							else cip.strip()
						)  # pass_1_of_2
						if not ";" in combine_info:
							combine_info = (
								";".join([socket.getfqdn(cip.strip()), cip.strip()])
								if socket.getfqdn(cip.strip())
								else cip.strip()
							)  # pass_2_of_2

					except:
						combine_info = cip.strip()

					is_update: bool = all(
						(last_info, combine_info, last_info != combine_info)
					)
					is_new: bool = any(
						(
							all((not last_info, combine_info)),
							all((not cmac.strip() in [*lanmacs], cmac)),
						)
					)
					is_exist: bool = last_info == combine_info

					if any((is_new, is_update)):  # if_updated(vendor) / if_new(vendor)

						if is_new:
							print(
								Style.BRIGHT
								+ Fore.GREEN
								+ "информация по ip %s добавлена в базу" % cip.strip()
							)
						if is_update:
							print(
								Style.BRIGHT
								+ Fore.BLUE
								+ "информация по ip %s обновлена в базе" % cip.strip()
							)
						if is_exist:
							print(
								Style.BRIGHT
								+ Fore.YELLOW
								+ "информация по ip %s найдена в базе" % cip.strip()
							)

						lanmacs[
							cmac.strip()
						] = combine_info  # host;"ip";mac_to_vendor # "ip";mac_to_vendor
				else:
					continue  # if_some_data_null
		else:  # is_no_break
			print(
				"Компьютеры с ip адресами начинающимися %s просканированны" % ip
			)  # is_color


# generate(mac_and_ip_address) / use_main_ip
async def ip_config():

	# async with asyncio.TaskGroup() as gp:
	task = asyncio.create_task(ipconfig_to_base())  # old
	# task = tg.create_task(ipconfig_to_base())

	await task  # old


def time_to_ms() -> int:  # unixtime -> ms

	try:
		tim = int(time() * 1000)  # time() - unixtime # * 1000 = ms

		assert (
			tim >= 0
		), f"Ошибка конвертирования времени @time_to_ms/{tim}"  # is_assert_debug
	except AssertionError as err:  # if_null
		tim = 0
		logging.warning(f"Ошибка конвертирования времени @time_to_ms/{tim}")
		raise err
	except BaseException as e:  # if_error
		tim = 0
		logging.error("Ошибка конвертирования времени @time_to_ms/tim [%s]" % str(e))

	return int(tim)  # ms # 1681467127489


# change_full_to_short(if_need_or_test_by_logging) # temporary_not_use
def full_to_short(filename) -> str:

	try:
		assert filename and os.path.exists(
			filename
		), f"Файл отсутствует @full_to_short/{filename}"  # is_assert_debug # filename
	except AssertionError:
		logging.warning("Файл отсутствует @full_to_short/%s" % filename)
		# raise err
		# return filename # skip_result
	except BaseException as e:
		logging.error("Файл отсутствует @full_to_short/%s [%s]" % (filename, str(e)))

	try:
		short_filename: str = "".join(
			[filename[0], ":\\...\\", filename.split("\\")[-1]]
		).strip()  # is_ok
	except:
		try:
			short_filename: str = filename.split("\\")[
				-1
			].strip()  # default_short_without_drive
		except:
			short_filename: str = filename.strip()  # if_error_stay_old_filename

	return short_filename


# count_level_from_full("c:\\mytemp\\downloads\\hello.world") # need_folder_by_level # 4
def count_level_from_full(filename) -> int:

	try:
		assert filename and os.path.exists(
			filename
		), f"Файл отсуствует @count_level_from_full/{filename}"  # is_assert_debug # filename
	except AssertionError as err:  # if_null
		logging.warning("Файл отсуствует @count_level_from_full/%s" % filename)
		raise err
		return 0
	except BaseException as e:  # if_error
		logging.error(
			"Файл отсуствует @count_level_from_full/%s [%s]" % (filename, str(e))
		)
		return 0

	try:
		level_count = len(filename.split("\\")) if filename else 0  # is_no_lambda
	except BaseException as e:
		level_count: int = 0
		write_log(
			"debug level_count[filename][error]",
			"%s [%s]" % (filename, str(e)),
			is_error=True,
		)
	else:
		if not os.path.isfile(
			"\\".join(filename.split("\\")[0 : level_count - 1])
		):  # if_folder(skip_file)
			write_log(
				"debug level_count[filename]", "%s [%d]" % (filename, level_count)
			)  # logging_file_by_level

	return level_count


# slugify("Hello, world") # Hello-world
# slugify("My name is Sergey, my age is 39") # My-name-is-Sergey-my-age-is-39
# slugify("prog-help.ru-Python  KivyKivyMD создание шаблонов для уменьшения кода")
# prog-helpru-Python--KivyKivyMD-создание-шаблонов-для-уменьшения-кода


# @log_error
def slugify(s: str = "") -> str:

	try:
		assert s, f"Пустая строка @slugify/{s}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(f"Пустая строка @slugify/{s}")
		raise err
		return ""
	except BaseException as e:  # if_error
		logging.error("Пустая строка @slugify/s [%s]" % str(e))
		return ""

	# if not s:
	# return ""

	try:
		s = s.strip()  # s.lower().strip()
		s = re.sub(r"[^\w\s-]", "", s)
		s = re.sub(r"[\s_-]", "-", s)
		s = re.sub(r"^-+|-+$", "", s)
	except:
		s = ""

	return s


# kill_process_by_name(debug) # percent?
# @log_error
async def kill_proc_by_name(
	proc_name: str = "", kill: bool = True
):  # if_not_kill_found
	"""
	os.system("taskkill /f /im %s" % proc_name)
	"""

	PROCNAME = proc_name

	found: bool = False

	try:
		for proc in psutil.process_iter():

			if proc.name == PROCNAME:
				found = True

				p = psutil.Process(proc.pid)

				if not "SYSTEM" in p.username and kill:
					# write_log("debug kill", str(proc.name))
					proc.kill()
	except:
		return False
	else:
		return found


# kill_process_by_pid
# @log_error
async def kill_proc_by_pid(proc_pid):

	try:
		os.system("taskkill /f /pid %s" % proc_pid)
	except:
		return


try:
	dtw = asyncio.run(date_to_week())
except BaseException as e:
	logging.error("Ошибка даты [%s]" % str(e))
	write_log("debug dtw[error]", "Ошибка даты [%s]" % str(e), is_error=True)
else:
	write_log(
		"debug dtw[ok]",
		"Today is: %s, weekday is: %s, season(days): %s, number_of_day: %s, days_to_ny: %s"
		% (
			dtw["date"],
			dtw["weekday"],
			dtw["season(days)"],
			dtw["number_of_day"],
			dtw["days_to_ny"],
		),
	)

# debug
# sys.exit() # spyder_debug
# exit() # python_debug(no_run) # debug # stop_if_some_error(is_long)

# dsize = dsize2 = 0

try:
	dsize: int = disk_usage("c:\\").free // (1024**2)
except:
	dsize: int = 0

try:
	dsize2: int = disk_usage("d:\\").free // (1024**2)
except:
	dsize2: int = 0

mem: float = psutil.virtual_memory()[2]  # need_less_80(ram)

logging.info("@mem %s" % str(round(mem, 3)))

ctme = datetime.now()


async def utc_time(dt=datetime.now()):

	gmt = datetime.utcnow()  # datetime.datetime(2023, 2, 23, 3, 47, 36, 326713)
	cur_gmt = datetime.now()  # ?

	try:
		gmt = abs(cur_gmt - gmt).seconds // 3600  # 5

		assert gmt in range(
			-12, 13
		), f"Ошибка часового пояса или отрицательный часовой пояс @utc_time/{gmt}"  # is_assert_debug
	except AssertionError as err:  # if_null
		gmt = 999
		logging.warning(
			f"Ошибка часового пояса или отрицательный часовой пояс @utc_time/{gmt}"
		)
		raise err
	except BaseException as e:  # if_error
		gmt = 999
		logging.error(
			"Ошибка часового пояса или отрицательный часовой пояс @utc_time/gmt [%s]"
			% str(e)
		)

	return gmt


async def ntp_to_utc():
	try:
		c = ntplib.NTPClient()
		response = c.request(
			"asia.pool.ntp.org", version=3
		)  # "uk".pool.ntp.org # internet_sync_time
		# print(response.offset) #0.22685885429382324
	except BaseException as err:
		raise err
		return ("", "")
	else:
		# print(datetime.fromtimestamp(response.tx_time, timezone.utc)) #2023-06-28 02:59:11.460592+00:00 # gmt+5
		return datetime.fromtimestamp(response.tx_time, timezone.utc)


utc = asyncio.run(utc_time())


async def shutdown_if_time(utcnow: int = utc, no_date: str = ""):

	global ctme

	# mytime: dict = {"jobtime": [9, 18, 5], "dinnertime": [12, 14], "sleeptime": [0, 8], "anytime": [True]} # sleep_time_less_hour # debug

	write_log("debug utctime", "Utc: %s" % str(utcnow))  # time_zone(gmt)

	# if all((no_date in str(datetime.today()).split(" ")[0], no_date)):
	# return

	if (
		ctme.hour < mytime["sleeptime"][1]
	):  # utcnow <= ctme.hour < mytime["sleeptime"][1] # shutdown_after_8am
		# run(["cmd", "/c", "shutdown", "/a"], shell=False)  # stop_timer(is_need_hide_no_cancel) # kill_proc_by_name("shutdown.exe") # stop_timer_by_app # 1
		# run(["cmd", "/c", "shutdown", "/s", "/t", "3600", "/c", "Чтобы отменить выключение, выполните в командной строке shutdown /a"], shell=False)  # shutdown(1hour) (midnight - 7am) # start_after # if_no_updates #1.1
		# run(["cmd", "/c", "shutdown", "/s", "/t", "1800", "/c", "Чтобы отменить выключение, выполните в командной строке shutdown /a"], shell=False)  # shutdown(30min) (midnight - 7am) # start_after
		run(
			[
				"cmd",
				"/c",
				"shutdown",
				"/g",
				"/t",
				"900",
				"/c",
				"Чтобы отменить выключение, выполните в командной строке shutdown /a",
			],
			shell=False,
		)  # shutdown(15min) (midnight - 7am) # start_after # if_updates
		# run(["cmd", "/c", "shutdown", "/g", "/t", "600", "/c", "Чтобы отменить выключение, выполните в командной строке shutdown /a"], shell=False) # shutdown(10min) (midnight - 7am) # start_after # if_updates

		# """
		try:
			if os.path.exists("d:\\"):
				sleep(900)
		except BaseException as e:
			print("job[timeout] [%s]" % str(e))
			write_log("debug job[timeout]", "%s" % str(e), is_error=True)
		# """

		exit()

	elif (
		ctme.hour >= mytime["sleeptime"][1]
	):  # ctme.hour % 3 == 0 # every_3_hours_by_divmod # stop_shutdown_by_time
		run(["cmd", "/c", "shutdown", "/a"], shell=False)  # stop_timer_after_7am(more)

		try:
			res = await kill_proc_by_name(
				"shutdown.exe"
			)  # stop_timer_by_app # asyncio.run(
		except:
			res = False
		else:
			if res:
				write_log(
					"debug res[kill_proc_by_name]",
					"shutdown [%s]" % str(datetime.now()),
				)

	# if_equal_time(mytime["sleeptime"][1])_pass


# min_2status
# dspace's / no_download_files / no_sleep_time(backup_time) / is_skip_overload_cpu_more_80("85")

# cpu_overload(try_stop_SysMain/Superfetch)

# add_holidays(if_holidays_then_run)


async def skip_run_date():
	dt = datetime.now()

	# need_unique_world_holidays
	holidays: dict = {
		"1.1": "Новый год",
		"8.3": "Международный женский день",
		"7.1": "Рождество",
	}
	holiday_status: bool = False

	day = month = ""

	day = str(dt.day).split("0")[-1] if str(dt.day).startswith("0") else str(dt.day)
	month = (
		str(dt.month).split("0")[-1] if str(dt.month).startswith("0") else str(dt.month)
	)

	try:
		holiday_status = holidays[".".join([day, month])]
	except:
		holiday_status = False
	else:
		if holiday_status:
			return True

	return holiday_status


# @select_optimal_time_or_create_new
# dspace(+reserve) # midnight - 6am # 11pm # overload(85) # 1
# is_status: tuple = (not dsize2, any((ctme.hour < mytime["sleeptime"][1], ctme.hour > 22)), mem > 80) # dspace(is_need_hide) / before_8am_or_more_10pm / overload(80->85)
# dspace(+reserve) # midnight - 6am # 11pm # no_overload # 2
# is_status: tuple = (not dsize2, any((ctme.hour < mytime["sleeptime"][1], ctme.hour > 22))) # dspace(is_need_hide) / before_8am_or_more_10pm
# dspace(+reserve) # midnight - 6am # stop_after_15h # no_overload # 3
# is_status: tuple = (not dsize2, any((ctme.hour < mytime["sleeptime"][1], ctme.hour > 15)), dayago > 18, mem >= 82) # dspace(is_need_hide) / before_8am(more_3pm) / run_more_18h / overload(80->85/avg~82)
# is_status: tuple = (ctme.hour < mytime["sleeptime"][1], dayago > 15, mem >= 82) # beforer_8am / stop_after_15h / overload(80->85/avg~82) # default
# midnight - 7am # stop_after_15h # no_overload # 4
is_status: tuple = (
	ctme.hour < mytime["sleeptime"][1],
	dayago > 15,
)  # before_7am / stop_after_15h # default

srd = asyncio.run(skip_run_date())


if is_status.count(True) > 0 and not srd:
	print("0[3182] %s" % str(is_status), mem)
	# sys.exit()

	try:
		ut = asyncio.run(utc_time())  # uzb(ut=5)
	except:
		ut = 0

	if any(
		(ut <= ctme.hour < mytime["sleeptime"][1], ctme.hour < mytime["sleeptime"][1])
	):  # debug # 5 <= x < 8
		asyncio.run(shutdown_if_time())  # no_date="29.08.2023"

	exit()


# Sound notify

# @log_error
def sound_notify(text: str = ""):  # 2
	try:
		if text:
			engine = pyttsx3.init()
			engine.say(text)
			engine.runAndWait()
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "Не смог произнести текст! [%s]" % str(e))
		write_log(
			"debug soundnotify[error]",
			"Не смог произнести текст! [%s]" % str(e),
			is_error=True,
		)
	else:
		if text:
			print(Style.BRIGHT + Fore.GREEN + "Текст [%s] успешно произнесён" % text)
			write_log("debug soundnotify[ok]", "Текст [%s] успешно произнесён" % text)


# --- Files by template to list ---

filter_list: list = []


# 2
async def my_args() -> list:  # 2

	tmp: list = []
	# some_list: list = []

	# sys.argv -> "argparse" # hide_docstring

	abc_or_num_regex = re.compile(r"^[A-Z0-9].*", re.I)

	# old_command_line_arguments
	try:
		tmp = [str(sys.argv[i]) for i in range(0, len(sys.argv)) if sys.argv[i]]
	except:
		tmp = []
	else:
		if len(tmp) == 1:
			tmp = []  # no_filter

			print(
				Style.BRIGHT + Fore.YELLOW + "Не найдено аргументов",
				Style.BRIGHT + Fore.WHITE + "[%s]" % str(datetime.now()),
			)  # is_color
			write_log(
				"debug sys[noargs]", "Не найдено аргументов [%s]" % str(datetime.now())
			)
		elif len(tmp) > 1:
			temp = tmp[1:]  # skip_script_name_and_have_filter

			# temp2 = list(set([t.strip() for t in temp if abc_or_num_regex.findall(t)])) # start(abc/123) # is_ok
			temp2 = list(
				set(
					[
						f.strip()
						for f in filter(
							lambda x: abc_or_num_regex.findall(x), tuple(temp)
						)
					]
				)
			)  # start(abc/123) # debug

			temp3 = list(
				set(
					[t2.strip() if len(t2) >= 2 else "".join([t2, "_"]) for t2 in temp2]
				)
			)  # length >= 2 # debug

			tmp = sorted(temp3, reverse=False)  # sort_by_string
			# tmp = sorted(temp3, key=len, reverse=False) # sort_by_key

		print(
			Style.BRIGHT
			+ Fore.CYAN
			+ "Найдено %d аргументов [%s]" % (len(tmp), str(datetime.now()))
		)  # is_color
		write_log(
			"debug sys[args]",
			"Найдено %d аргументов [%s]" % (len(tmp), str(datetime.now())),
		)

	return tmp  # some_list


async def battery_info():
	# import psutil

	try:
		battery = psutil.sensors_battery()
		plugged = battery.power_plugged
		percent = battery.percent
	except:
		pass
	else:
		if plugged:
			if percent == 0:  # 0
				print(
					Style.BRIGHT
					+ Fore.RED
					+ f"Зарядка подключена, заряд батареи: {percent}%"
				)
			elif percent >= 75:  # 75-100
				print(
					Style.BRIGHT
					+ Fore.GREEN
					+ f"Зарядка подключена, заряд батареи: {percent}%"
				)
			elif percent in range(20, 50):  # 20-50
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ f"Зарядка подключена, заряд батареи: {percent}%"
				)
			else:  # other
				print(f"Зарядка подключена, заряд батареи: {percent}%")  # is_no_color

			write_log(
				"debug battery_info[plugged]",
				f"Зарядка подключена, заряд батареи: {percent}% [{str(datetime.now())}]",
			)
		elif not plugged:
			if all((percent != None, isinstance(int(percent), int))):  # float -> int
				print(f"Зарядка отключена, заряд батареи: {percent}%")

			write_log(
				"debug battery_info[unplugged]",
				f"Зарядка отключена, заряд батареи: {percent}% [{str(datetime.now())}]",
			)

	return (plugged, percent)  # battery


# --- Find files by period(max_days) ---


# filename(str)/period(int)/is_select(bool)
def mdate_by_days(
	filename,
	period: int = 30,
	is_select: bool = False,
	is_dir: bool = False,
	is_less: bool = False,
	is_any: bool = False,
) -> any:  # default(month) #14

	try:
		assert filename and os.path.exists(
			filename
		), f"Файл отсутствует @mdate_by_days/{filename}"  # is_assert_debug # filename
	except AssertionError as err:  # if_null
		logging.warning("Файл отсутствует @mdate_by_days/%s" % filename)
		raise err
		return None
	except BaseException as e:  # if_error
		logging.error("Файл отсутствует @mdate_by_days/%s [%s]" % (filename, str(e)))
		return None

	# debug_for_folder
	today = datetime.today()  # datetime
	fdate = os.path.getmtime(filename)  # unixdate(file/folder) # modify
	ndate = datetime.fromtimestamp(fdate)  # datetime

	logging.info("@mdate_by_days Файл %s был изменён в %s" % (filename, str(ndate)))

	try:
		is_dir = not os.path.isfile(
			filename
		)  # is_folder_filter(True) / is_file_fitler(False)
	except:
		is_dir = False  # if_error_is_not_folder

	"""
	# date_between
	# by_days/by_week/by_month/by_year(less) # by_minute/by_hour
	# by_days/by_week/by_month/by_year(more) # by_minute/by_hour
	"""

	if is_any:
		is_less = False

	if is_less:
		is_any = True

	days_period: int = period

	if days_period:
		# print("File: %s" % filename)
		write_log("debug files[days]", "Days for period: %d" % days_period)
	elif not days_period:
		# print("File: %s" % filename)
		write_log("debug files[days]", "Days for period: Today")

	try:
		# default_calendar_week #is_abs
		week_status = (
			f"Week for period: {int(days_period // 7)}"
			if days_period // 7 > 0
			else "Week: None"
		)
	except BaseException as e:
		week_status = "Week [error] [%s]" % str(e)
	finally:
		write_log(
			"debug files[week]", week_status
		)  # "Week for period: %d" % days_period // 7

	try:
		# default_calendar_month #is_abs
		month_status = (
			f"Month for period: {int(days_period // 30)}"
			if days_period // 30 > 0
			else "Month: None"
		)
	except BaseException as e:
		month_status = "Month [error] [%s]" % str(e)
	finally:
		write_log(
			"debug files[month]", "%s" % month_status
		)  # "Month for period: %d" % days_period // 30

	dt = datetime.now()

	max_days_by_year: int = 0

	def is_year_leap() -> int:

		try:
			max_days_by_year = 366 if dt.year % 4 == 0 else 365
		except:
			max_days_by_year: int = 365

		return max_days_by_year

	max_days_by_year = is_year_leap()

	try:
		year_status = (
			f"Year for period: {int(days_period // max_days_by_year)}"
			if days_period // max_days_by_year > 0
			else "Year: None"
		)
	except BaseException as e:
		year_status = "Year [error] [%s]" % str(e)
	finally:
		write_log(
			"debug files[year]", "%s" % year_status
		)  # "Year for period: %d" % days_period // 365

	try:
		days_ago: int = abs(today - ndate).days  # default=file/folder
		assert bool(days_ago >= 0), ""
	except AssertionError:  # if_none(today)
		days_ago: int = 0

		debug_status = "debug folder[today]" if is_dir else "debug file[today]"

		# print("%s. [%s]" % (filename, str(e)))
		write_log(debug_status, "%s. [%s]" % (filename, str(e)), is_error=True)

		return days_ago  # if_error_use_current_day(try_skip/today)
	else:
		if (
			is_less == True
			and all((period >= 0, days_ago <= period))
			or is_less == False
			and days_ago >= period
		) and is_any == False:
			debug_status = (
				"debug file[dayago][folder]" if is_dir else "debug file[dayago][file]"
			)

			write_log(
				debug_status, "Days ago: %d, last file: %s" % (days_ago, filename)
			)

		elif all((is_any == True, days_ago >= 0, period >= 0)):
			write_log(
				"debug file[dayago]",
				"Days ago: %d, last file: %s" % (days_ago, filename),
			)

		return days_ago


async def datetime_from_file(filename) -> tuple:  # 4
	fdate = os.path.getmtime(
		filename
	)  # unixdate # 1648708605.2300806 # <class 'float'> # modify

	try:
		ndate = datetime.fromtimestamp(
			fdate
		)  # datetime.datetime(2022, 3, 31, 11, 36, 45, 230081) # <class 'datetime.datetime'>
	except:
		ndate = datetime.today()  # current
		logging.info(
			"@datetime_from_file Файл %s был изменён в %s 'error'"
			% (filename, str(ndate))
		)

		return (ndate, False)  # current_date + error_status
	else:
		logging.info(
			"@datetime_from_file Файл %s был изменён в %s 'ok'" % (filename, str(ndate))
		)
		return (ndate, True)  # current_date + normal_status


# @log_error
async def days_by_list(lst: list = [], is_avg: bool = False):  # 8

	try:
		assert lst and isinstance(
			lst, list
		), "Пустой список или другой формат списка @days_by_list/lst"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Пустой список или другой формат списка @days_by_list/lst")
		raise err
		return None
	except BaseException as e:  # if_error
		logging.error(
			"Пустой список или другой формат списка @days_by_list/lst [%s]" % str(e)
		)
		return None

	avg_list: list = []
	sum_days: int = 0
	len_days: int = 0
	max_days: int = -1

	today = datetime.today()  # datetime
	try:
		# lst = list(days_by_list_gen()) # new(yes_gen)
		lst: list = list(
			set(
				[
					l.strip()
					for l in filter(lambda x: os.path.exists(x), tuple(lst))
					if l
				]
			)
		)
	except:
		lst: list = []
	finally:
		lst.sort(reverse=False)  # sort_by_string
		# lst.sort(key=len, reverse=False) # sort_by_length

	with unique_semaphore:
		for l in tuple(lst):

			try:
				assert lst, f"Пустой список @days_by_list/{l}"  # lst # is_assert_debug
			except AssertionError as err:  # if_null
				logging.warning("Пустой список @days_by_list/lst")
				raise err
				break
			except BaseException as e:  # if_error
				logging.error("Пустой список @days_by_list/lst [%s]" % str(e))
				break

			try:
				fdate = os.path.getmtime(l)  # unixdate # modify
				ndate = datetime.fromtimestamp(fdate)  # datetime
			except:
				continue
			else:
				logging.info("@lst Файл %s был изменён в %s" % (l, str(ndate)))

			try:
				days_ago = abs(today - ndate).days
				assert bool(days_ago >= 0), ""
			except AssertionError:
				days_ago = 0
			finally:
				if days_ago != None:
					if is_avg:
						avg_list.append(days_ago)  # add_all_days_for_filter
					if max_days < days_ago:
						max_days = days_ago  # default_max_days

	if all((is_avg, avg_list)):

		temp = sorted(avg_list, reverse=False)
		if temp:
			avg_list = temp

		sum_days: int = reduce(lambda x, y: x + y, avg_list)  # sum_days = sum(avg_list)
		len_days: int = len(avg_list)

		try:
			avg_days: int = (lambda s, l: s // l)(sum_days, len_days)
		except:  # DevideByZero
			avg_days: int = 0
		finally:
			max_days = (
				avg_days if avg_days != None else 0
			)  # use_avg_days_or_one_day_by_default

	return max_days


# @log_error
def fspace(src: str = "", dst: str = "", is_Log: bool = False) -> bool:  # 11

	try:
		assert src and os.path.exists(
			src
		), f"Файл отсутствует @fspace/{src}"  # is_assert_debug # src
	except AssertionError:  # if_null
		logging.warning("Файл отсутствует @fspace/%s" % src)
		# raise err
		return False
	except BaseException as e:  # if_error
		logging.error("Файл отсутствует @fspace/%s [%s]" % (src, str(e)))
		return False

	try:
		fsize: int = os.path.getsize(src)
		dsize: int = disk_usage(dst[0] + ":\\").free
	except BaseException as e:  # if_error
		fsize: int = 0
		dsize: int = 0
		logging.error(
			"Нет размера файла или размера диска @fspace/%s [%s]" % (src, str(e))
		)

	fspace_status: bool = False

	try:
		fspace_status = all(
			(fsize, dsize, int(fsize // (dsize / 100)) <= 100)
		)  # fspace(ok-True,bad-False)
	except:
		fspace_status = False  # fspace(error-False)
	finally:
		return fspace_status


# fpath, fname = split_filename('c:\\downloads\\hello.wolrd') # use_filename_from_init
def split_filename(filename) -> tuple:  # 19

	try:
		assert filename and os.path.exists(
			filename
		), f"Файл отсутствует @split_filename/{filename}"  # is_assert_debug # filename
	except AssertionError as err:  # if_null
		logging.warning("Файл отсутствует @split_filename/%s" % filename)
		raise err
		return ("", "")
	except BaseException as e:  # if_error
		logging.error("Файл отсутствует @split_filename/%s [%s]" % (filename, str(e)))
		return ("", "")

	try:
		file_path, file_name = os.path.split(filename)
		assert (
			file_path and file_name
		), f"Имя папки или имя файла не указано @split_filename/{file_path}/{file_name}"  # is_assert_debug
	except AssertionError as err:  # if_null
		file_path = file_name = ""
		logging.warning(
			"Имя папки или имя файла не указано @split_filename/%s" % filename
		)
		raise err
	except BaseException as e:  # if_error
		file_path = file_name = ""
		logging.error(
			"Имя папки или имя файла не указано @split_filename/%s [%s]"
			% (filename, str(e))
		)

	return (
		file_path.strip(),
		file_name.strip(),
	)  # return os.path.split(filename) # ('c:\\downloads', 'hello.wolrd')


# fullname = join_filename(file_path, file_name): # split_filename -> join_filename
def join_filename(file_path, file_name) -> str:  # 3
	return os.path.join(
		file_path.strip(), file_name.strip()
	)  # 'c:\\downloads\\hello.wolrd'


# --- Notify center

# update_icons_if_need
icons: dict = {
	"cleaner": "c:\\downloads\\mytemp\\cleaner.ico",
	"complete": "c:\\downloads\\mytemp\\complete.ico",
	"different": "c:\\downloads\\mytemp\\different.ico",
	"error": "c:\\downloads\\mytemp\\error.ico",
	"finish": "c:\\downloads\\mytemp\\finish.ico",
	"main": "c:\\downloads\\mytemp\\main.ico",
	"moved": "c:\\downloads\\mytemp\\moved.ico",
	"movie": "c:\\downloads\\mytemp\\movie.ico",
	"search": "c:\\downloads\\mytemp\\search.ico",
	"skip": "c:\\downloads\\mytemp\\skip.ico",
	"tg": "c:\\downloads\\mytemp\\tg.ico",
	"user": "c:\\downloads\\mytemp\\user.ico",
	"work": "c:\\downloads\\mytemp\\work.ico",
}


# @log_error
def MyNotify(txt: str = "", icon: str = "", sec: int = 10):  # 19
	error: bool = False

	try:
		assert icon and os.path.exists(
			icon
		), f"Файл отсутствует @MyNotify/{icon}"  # is_assert_debug # icon
	except AssertionError as err:  # if_null
		error = True
		logging.warning("Файл отсутствует @MyNotify/%s" % icon)
		raise err
	except BaseException as e:  # if_error
		error = True
		logging.error("Файл отсутствует @MyNotify/%s [%s]" % (icon, str(e)))

	# ---- init(show) notify ----
	try:
		# отобразить_оповещение_в_трее
		toaster = ToastNotifier()
	except:
		error = True
	finally:
		if error == False:
			if all((txt, icon, sec)):
				# threaded - в потоке
				# icon_path - ссылка_на_иконку_для_оповещений(ico)
				# duration - задержка в секундах
				toaster.show_toast(
					"Моя программа", txt, threaded=True, icon_path=icon, duration=sec
				)

				while toaster.notification_active():
					sleep(0.1)
		elif error == True:
			if all((txt, sec)):
				print(Style.BRIGHT + Fore.CYAN + f">>> {txt}")  # no_icon_or_some_error
				sleep(sec)
			# print(Fore.RESET)


# --- Find files in folders ---


# @log_error
def walk(dr: str = "", files_template: str = ""):

	"""Рекурсивный поиск файлов в пути"""

	# -- default --
	if not files_template:
		return
	else:
		ext_regex = files_template

	# check_and_test_this_block
	try:
		for name in os.listdir(dr):
			path = os.path.join(dr, name)
			if all((os.path.isfile(path), ext_regex.findall(path))):
				yield path
			else:
				yield from walk(path, ext_regex)

	except BaseException as e:
		return f"Error as {str(e)}"


# one_folder("c:\\downloads\\combine\\", re.compile(r"(?:(zip))$")) # one_folder
# one_folder("c:\\downloads\\new\\", video_regex)
def one_folder(folder, files_template) -> list:
	try:
		if not os.path.exists(folder) and os.listdir(
			folder
		):  # disk_usage(folder[0] + ":\\").free:
			print("Создаётся папка %s т.к. она отсуствует" % folder)
			write_log(
				"debug one_folder[create]",
				"Создаётся папка %s т.к. она отсуствует" % folder,
			)
	except BaseException as e:
		write_log(
			"debug one_folder[error]",
			"Ошибка создания папки %s [%s]" % (folder, str(e)),
			is_error=True,
		)
	finally:
		try:
			os.mkdir(folder.title())  # type1
		except BaseException as e:
			os.system(r"cmd /c mkdir %s" % folder.title())  # type2(error) # cmd /k

			write_log(
				"debug one_folder[folder]!",
				"Папка %s уже создана [%s] [%s]"
				% (folder, str(e), str(datetime.now())),
				is_error=True,
			)
		else:
			write_log(
				"debug one_folder[folder]",
				"Папка %s успешно создана [%s]" % (folder, str(datetime.now())),
			)

	def one_folder_to_files(folder=folder, files_template=files_template):
		for lf in os.listdir(folder):
			if (
				files_template.findall(lf.strip())
				and os.path.isfile(os.path.join(folder, lf.strip()))
				and any(
					(
						lf.split("\\")[-1].startswith(lf.split("\\")[-1].capitalize()),
						lf.split("\\")[-1].find(lf.split("\\")[-1]) == 0,
					)
				)
			):
				yield os.path.join(folder, lf.strip())

	try:
		files = list(one_folder_to_files())
	except BaseException as e:
		files = []  # if_error_null_list
		write_log("debug error_one_folder", "%s [%s]" % (folder, str(e)), is_error=True)
	finally:
		write_log("debug count_one_folder", "%d" % len(files))

	return list(
		files
	)  # ['c:\\downloads\\Current_BacthConverter.zip', ...] # capitalize # Abc... # find ~ findall(regex)


# sub_folder("c:\\downloads\\combine\\", re.compile(r"(?:(zip))$")) # sub_folder # hide_regex(test_logic)
def sub_folder(folder, files_template) -> list:
	try:
		if not os.path.exists(folder) and os.listdir(
			folder
		):  # disk_usage(folder[0] + ":\\").free:
			print("Создаётся подпапка %s т.к. она отсуствует" % folder)
			write_log(
				"debug sub_folder[create]",
				"Создаётся подпапка %s т.к. она отсуствует" % folder,
			)
	except BaseException as e:
		write_log(
			"debug sub_folder[error]",
			"Ошибка создания подпапки %s [%s]" % (folder, str(e)),
			is_error=True,
		)
	finally:
		try:
			os.mkdir(folder.title())  # type1
		except BaseException as e:
			os.system(r"cmd /c mkdir %s " % folder.title())  # type2(error) # cmd /k

			write_log(
				"debug sub_folder[folder]!",
				"Папка %s уже создана [%s] [%s]"
				% (folder, str(e), str(datetime.now())),
				is_error=True,
			)
		else:
			write_log(
				"debug sub_folder[folder]",
				"Папка %s успешно создана [%s]" % (folder, str(datetime.now())),
			)

	def sub_folder_to_files(folder=folder, files_template=files_template):
		for lf in walk(folder, files_template):
			if (
				files_template.findall(lf.split("\\")[-1])
				and os.path.isfile(lf)
				and any(
					(
						lf.split("\\")[-1].startswith(lf.split("\\")[-1].capitalize()),
						lf.split("\\")[-1].find(lf.split("\\")[-1]) == 0,
					)
				)
			):
				yield lf.strip()

	try:
		files: list = list(sub_folder_to_files())
	except BaseException as e:
		files: list = []  # if_error_null_list
		write_log("debug error_sub_folder", "%s [%s]" % (folder, str(e)), is_error=True)
	finally:
		write_log("debug count_sub_folder", "%d" % len(files))

	return list(
		files
	)  # ['c:\\downloads\\combine\\Archive\\Adobe_Photoshop_CC_2019.zip', ...] # capitalize # Abc... # find ~ findall(regex)


# --- Math ---


def most_frequent(list) -> any:  # int(str) # None
	"""
	Самый частый элемент

	Этот короткий скрипт вернёт элемент, чаще всего встречающийся в списке.

	Используются про6двинутые параметры встроенной функции max():

	• первым аргументом она получает множество из элементов списка (помним, что в множестве все элементы уникальны);
	• затем применяет к каждому из них функцию count, подсчитывающую, сколько раз элемент встречается в списке;
	• после этого возвращает элемент множества, который имеет больше всего «попаданий».

	В качестве аргумента можно использовать списки, кортежи и строки.

	>>>numbers = [1,2,1,2,3,2,1,4,2]
	>>>most_frequent(numbers) # 2
	"""
	try:
		mf = max(set(list), key=list.count)  # default
	except:
		mf = None

	return mf


# hms(7500)) # Should print 02h05m00s
# @log_error
def hms(seconds: int = 0):  # 37 # @ms_to_time
	try:
		h: int = seconds // 3600
		m: int = seconds % 3600 // 60
		s: int = seconds % 3600 % 60
		assert any(
			(h, m, s)
		), f"Нет какой-то величины времени @hms/{h}/{m}/{s}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Нет какой-то величины времени @hms/%d" % seconds)
		raise err

	try:
		assert isinstance(h, int) and isinstance(m, int) and isinstance(s, int), ""
	except AssertionError:
		h, m, s = int(h), int(m), int(s)

	try:
		ms_time = (h * 3600) + (m * 60) + s
	except:
		ms_time = 0

	return ms_time

	"""
	if any((h, m, s)):
		return '{:02d}:{:02d}:{:02d}'.format(
			h, m, s)  # hh:mm:ss # '{:02d} час. {:02d} мин. {:02d} сек.'.format(h, m, s) # hh mm ss
	else:  # logic(another_time)
		return "%d" % seconds # ms
	"""


# @log_error
async def avg_lst(lst: list = []) -> int:  # default_list / in_arg_is_filesizes_list #4

	sum_lst: int = reduce(lambda x, y: x + y, lst)  # sum_lst = sum(lst)
	len_lst: int = len(lst)

	try:
		avg_size: int = (lambda s, l: s // l)(sum_lst, len_lst)  # by_lambda

		assert (
			avg_size
		), f"Пустая сумма или длина списка нулевая @avg_list/{avg_size}"  # is_assert_debug
	except AssertionError as err:  # if_null
		avg_size: int = 0
		logging.warning(f"Пустая сумма или длина списка нулевая @avg_list/{avg_size}")
		raise err
	except BaseException as e:  # if_error
		logging.error(
			"Пустая сумма или длина списка нулевая @avg_list/avg_size [%s]" % str(e)
		)
		try:
			avg_size = sum(lst) / len(lst)
		except:
			avg_size = 0
	finally:
		return avg_size


# @log_error
async def screen_clear():  # 3
	# for mac and linux(here, os.name is 'posix')

	if os.name == "posix":
		os.system("clear")
	else:
		# for windows platfrom
		os.system("cls")


asyncio.run(screen_clear())  # clear_screen
asyncio.run(battery_info())  # battery_info(after_clear_screen)


# print out some text

# wait for 5 seconds to clear screen
# sleep(5)
# now call function we defined above
# screen_clear()

# --- dos_shell(-c copy (fast_copy) / without diff param) ---
# (dir /r/b/s Short_AAsBBe*p.ext) > ext.lst # check_sort
# (for /f "delims=" %a in (ext.lst) do @echo file '%a') > concat.lst
# ffmpeg -f concat -safe 0 -y -i concat.lst -c copy Short_AAsBBe.ext

# cmd_file (%%a) # cmd_line (%a)

# --- Classes / OOP ---

# values_in_dict(oop)
"""
class FileInfo:

	__slots__ = ["filename", "filesize"]

	def __init__(self, filename, filesize):
		self.filename = filename
		self.filesize = filesize

	def printinfo(self):
		print(self.filename, self.filesize, sep = ": ")

finfo = FileInfo("somefilename", 0)
print(finfo.filename, finfo.filesize, sep = ": ") # somefilename: 0
# finfo.printinfo() # ?
"""

# 2
class Get_AR:

	__slots__ = ["width", "height"]

	def __init__(self, width, height):
		# self.__time = time() # unix_time # hidden_attribute # self._GET_AR__time
		# self.filename = filename
		self.width = width
		self.height = height

	def width_to_ar(
		self, width: int = 0, height: int = 0, owidth: int = 640, islogic=(True, 360)
	) -> tuple:  # islogic (True/False, oheight) #5 #debug

		try:
			assert (
				width and height
			), f"Ширина или высота пустая @width_to_ar/{width}/{height}"  # is_assert_debug
		except AssertionError:  # if_null
			logging.warning(
				"Ширина или высота пустая @width_to_ar/%d/%d [%s]"
				% (width, height, str(datetime.now()))
			)
			# raise err
			return (0, 0, 0)
		except BaseException as e:  # if_error
			logging.error(
				"Ширина или высота пустая @width_to_ar/%d/%ds [%s] [%s]"
				% (width, height, str(e), str(datetime.now()))
			)
			return (0, 0, 0)

		"""Calculate width"""

		try:
			if all((islogic[0], int(islogic[1]) > 0)):
				one = height / islogic[1]  # is_ratio(float)
				two: int = width // one  # is_width(int)

				if two != width:
					if not isinstance(two, int):
						two = int(two)
					if all((two % 2 != 0, two)):
						two -= 1
					logging.info(
						"calc[2] @width_to_ar/width/height [diff] %s"
						% "x".join([str(round(one, 3)), str(round(two, 3))])
					)
				elif two == width:
					logging.info(
						"calc[2] @width_to_ar/width/height [equal] %s"
						% "x".join([str(round(one, 3)), str(round(two, 3))])
					)
		except BaseException as e:
			one = two = 0
			logging.error("calc[2] @width_to_ar [error] %s" % str(e))

		"""Specify the Width To Retain the Aspect Ratio"""

		if width > owidth and owidth:  # if_need_optimal_ar # with_change
			first = width / owidth  # 720/640=1.125 # is_ratio(float)
			second: int = height // first  # 406/1.125=360 # is_height(int)

			if not isinstance(second, int):
				second = int(second)  # height(float->int)
			if all((second % 2 != 0, second)):
				second -= 1  # height(-1)

			woh_dict = {
				"width": owidth,
				"second": second,
				"height+": height,
			}  # new/new/old
			logging.info("@woh_dict [width/height] %s" % str(woh_dict))

			first_second_ar_str = str(
				(first, second, str(round(int(first) / int(second), 2)))
			)

			if second != height:
				write_log(
					"debug first_second_ar_str [not_optimized][width]",
					"%s" % "x".join([str(width), str(height)]),
				)
			if second == height:
				write_log(
					"debug first_second_ar_str [optimized][width]",
					"%s" % first_second_ar_str,
				)

			return (
				int(owidth),
				int(second),
				round(int(owidth) / int(second), 2),
			)  # 640, 360, 640/360
		else:
			if width <= owidth and height:
				if width != owidth:
					woh_dict = {"width": width, "owidth": owidth, "height": height}
				else:
					woh_dict = {"width": width, "height": height}
				logging.info("@woh_dict [width] %s" % str(woh_dict))
			return (0, 0, 0)

	def height_to_ar(
		self, width: int = 0, height: int = 0, oheight: int = 360, islogic=(True, 640)
	) -> tuple:  # islogic (True/False, owidth) # 4 # debug

		try:
			assert (
				width and height
			), f"Высота пустая @height_to_ar/{width}/{height}"  # is_assert_debug
		except AssertionError as err:  # if_null
			logging.warning(
				"Высота пустая @height_to_ar/%d/%d [%s]"
				% (width, height, str(datetime.now()))
			)
			raise err
			return (0, 0, 0)
		except BaseException as e:  # if_error
			logging.error(
				"Высота пустая @height_to_ar/%d/%d [%s] [%s]"
				% (width, height, str(e), str(datetime.now()))
			)
			return (0, 0, 0)

		"""Caclulate height"""

		try:
			if all((islogic[0], int(islogic[1]) > 0)):
				one = width / islogic[1]  # is_ratio(float)
				two: int = height // one  # is_height(int)

				if two != height:
					if not isinstance(two, int):
						two = int(two)
					if all((two % 2 != 0, two)):
						two -= 1
					logging.info(
						"calc[2] @height_to_ar/width/height [diff] %s"
						% "x".join([str(round(one, 3)), str(round(two, 3))])
					)
				elif two == height:
					logging.info(
						"calc[2] @height_to_ar/width/height [equal] %s"
						% "x".join([str(round(one, 3)), str(round(two, 3))])
					)
		except BaseException as e:
			one = two = 0
			logging.error("calc[2] @height_to_ar [error] %s" % str(e))

		"""Specify the Height To Retain the Aspect Ratio"""

		if height > oheight and oheight:  # with_change
			first = height / oheight  # 432/360 = 1.2 # is_ratio(float)
			second: int = width // first  # 1024/1.2 = 853 # is_width(int)

			if not isinstance(second, int):
				second = int(second)  # width(float->int)
			if all((second % 2 != 0, second)):
				second -= 1  # width(-1)

			woh_dict = {
				"width": second,
				"second": oheight,
				"width+": width,
			}  # new/new/old
			logging.info("@woh_dict [width/height] %s" % str(woh_dict))

			first_second_ar_str = str(
				(first, second, str(round(int(first) / int(second), 2)))
			)

			if second != width:
				write_log(
					"debug first_second_ar_str [not_optimized][height]",
					"%s" % "x".join([str(width), str(height)]),
				)
			if second == width:
				write_log(
					"debug first_second_ar_str [optimized][height]",
					"%s" % first_second_ar_str,
				)

			return (
				int(second),
				int(oheight),
				round(int(second) / int(oheight), 2),
			)  # 640, 360, 640/360
		else:
			if height <= height and width:
				if height != oheight:
					woh_dict = {"width": width, "height": height, "oheight": oheight}
				else:
					woh_dict = {"width": width, "height": height}
				logging.info("@woh_dict [height] %s" % str(woh_dict))
			return (0, 0, 0)


# @calc_vbr # manual_convert
"""
Самым безопасным способом будет CRF с ограничением битрейта:
ffmpeg -i input -c:v libx264 -preset veryslow -crf 23 -maxrate X -bufsize 2M output.mp4

Где Х - это максимальный битрейт в мегабитах в секунду, например 6M - 6 мегабит в секунду. Теперь считаем наш предел по этим самым мегабитам:
Битрейт в мегабитах = размер файла в гигабайтах / (количество минут * .0075)

Для часового файла с лимитом в 1,5 гигабайт это 1,5 / (60*0.0075) = 3,3 мегабита в секунду. Не забудьте, что хотя бы 128 килобит нужно оставить на звук.
Их придется вычесть из максимального битрейта для видео. Вот тут есть калькулятор.
Тогда:
ffmpeg -i input -c:v libx264 -preset veryslow -crf 23 -maxrate 3M -bufsize 2M -acodec aac -b:a 128k output.mp4

Это, на самом деле, очень мало, но точно влезет в лимит. Достаточно приличным для большинства файлов битрейтом считаю что-то в районе 10 мегабит в секунду,
но на самом деле все зависит от картинки, если много статики, то и 3 может хватить.. Ну и я надеюсь, что файлы у вас все же не часовые. :)

Тоже самое, но с битрейтом вместо CRF, можно тоже попробовать, и сравнить результаты:
ffmpeg -i input -vcodec libx264 -preset veryslow -b:v 3M -pass 1 -an -f mp4 NUL
ffmpeg -i input -vcodec libx264 -preset veryslow -b:v 3M -pass 2 -acodec aac -b:a 128k output.mp4
Это добро идет двумя последовательными строками в bat-файл, должно выполняться одно за другим.

Использовать HEVC (H.265), наверное, нецелесообразно для 1080P. Но попробовать можно:
ffmpeg -i input -c:v libx265 -preset slower -crf 23 -maxrate 3M -bufsize 2M output.mp4

Если вдруг окажется, что у полученного файла средний битрейт получился ниже лимита, значит он был ограничен целевым качеством CRF. Тогда качество можно повысить,
для этого цифру нужно понизить. Например, -crf до 21.
"""

"""
DUR=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$f")
ABR=448000
# target size
TRG=1470000000
VBR=$(echo "$TRG * 8 / $DUR - $ABR" | bc)
"""

# 9
class MyMeta:
	def __init__(self):  # self -> self, filename # init_attribute
		self.__time = time()  # unix_time # hidden_attribute # self._MyMeta__time
		pass  # self.filename = filename

	"""@unique_data.json"""

	def get_meta(self, filename) -> bool:  # 8

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_meta/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_meta/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return False
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_meta/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return False

		metacmd = (
			path_for_queue
			+ "ffprobe.exe -v quiet -print_format json -show_format -show_streams %s > %s"
			% (self.filename, unique_base)
		)

		try:
			p = os.system(metacmd)
			assert bool(p == 0), ""
		except AssertionError:
			if p != 0 or not os.path.exists(unique_base):
				# error_read_param(tags) # logging
				return False
		else:
			if p == 0 and os.path.exists(unique_base):
				# import_need_param(tags) # code
				return True

	def get_mkv_audio(self, filename, is_log: bool = True):  # 4

		self.filename: str = filename

		try:
			assert (
				self.filename.split(".").lower() == "mkv"
			), f"Выбран другой формат @get_mkv_audio/{self.filename}"  # is_assert_debug
		except AssertionError as err:  # if_null
			logging.warning(
				"Выбран другой формат @get_mkv_audio/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return []
		except BaseException as e:  # if_error
			logging.error(
				"Выбран другой формат @get_mkv_audio/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return []

		lst: list = []

		cmd: list = [
			path_for_queue + "ffprobe.exe",
			"-loglevel",
			"error",
			"-select_streams",
			"-show_streams",
			"-show_entries",
			"stream=index,codec_name:tags=:disposition=",
			"-of",
			"csv",
			filename,
		]  # output_format
		ca: str = "".join([path_for_queue, "atracks.nfo"])

		try:
			p = os.system(
				"cmd /c %s > %s" % (" ".join(cmd), ca)
			)  # stream,1,vorbis # stream,2,aac # stream,3,mp3 # cmd /k
			assert bool(p == 0), ""
		except AssertionError:
			return []
		else:
			if p == 0:

				try:
					with open(ca) as f:
						lst = f.readlines()
				except BaseException as e:
					lst: list = []
					if is_log:
						write_log(
							"debug get_audiotracks[error]",
							"%s [%s]" % (self.filename, str(e)),
							is_error=True,
						)
				else:
					if lst:
						try:
							lst = [
								l.split(",")[-1].lower().strip() for l in lst if l
							]  # audio_codecs(aac)
						except:
							lst = []

						if lst:
							if is_log:
								write_log(
									"debug get_audiotracks[ok]", "%s" % self.filename
								)

		if os.path.exists(ca):
			os.remove(ca)

	# input.mkv
	def get_codecs(self, filename, is_log: bool = True) -> list:  # 10

		self.filename: str = filename

		lst: list = []

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_codecs/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_codecs/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return lst
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_codecs/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return lst

		# ffprobe -v error -show_entries stream=codec_name -of csv=p=0:s=x input.m4v
		cmd: list = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=codec_name",
			"-of",
			"csv=p=0:s=x",
			filename,
		]  # output_format
		ci: str = "".join([path_for_queue, "codecs.nfo"])

		try:
			p = os.system("cmd /c %s > %s" % (" ".join(cmd), ci))  # cmd /k
			assert bool(p == 0), ""
		except AssertionError:
			return []
		else:
			if p == 0:

				try:
					with open(ci) as f:
						lst = f.readlines()
				except BaseException as e:
					lst: list = []
					if all((is_log, len(lst) < 2)):
						write_log(
							"debug get_codecs[error]",
							"%s [%s]" % (self.filename, str(e)),
							is_error=True,
						)
				else:
					if lst:

						def codecs_gen(lst=lst):  # 2
							for l in filter(lambda l: l, tuple(lst)):
								yield l.strip()

						try:
							tmp = list(codecs_gen())  # new(yes_gen)
						# tmp = [l.strip() for l in filter(lambda l: l, tuple(lst))]
						except:
							tmp = []
						else:  # finally
							lst = [t.strip() for t in filter(lambda x: x, tuple(tmp))]
							lst = lst[0:2]  # vcodec/acodec
							if len(lst) == 2:
								if is_log:
									# print(lst) # ['h264', 'aac']
									write_log(
										"debug get_codecs[ok]", "%s" % self.filename
									)

		if os.path.exists(ci):
			os.remove(ci)

		return lst

	def get_width_height(
		self,
		filename,
		is_calc: bool = False,
		is_log: bool = True,
		is_def: bool = False,
		maxwidth: int = 640,
	) -> tuple:  # 18

		global job_count

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_width_height/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_width_height/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return (0, 0, False)
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_width_height/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return (0, 0, False)

		# is_owidth, is_change = 0, False

		# ffprobe -v error -show_entries stream=width,height -of csv=p=0:s=x input.m4v
		cmd_wh: list = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=width,height",
			"-of",
			"csv=p=0:s=x",
			self.filename,
		]  # output_format
		wi: str = "".join([path_for_queue, "wh.nfo"])

		os.system("cmd /c %s > %s" % (" ".join(cmd_wh), wi))  # cmd /k

		# width_height_str = ""

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
				width, height = int(width_height_str.split("x")[0]), int(
					width_height_str.split("x")[-1]
				)

		except:
			width, height = 0, 0
			if is_log:
				print("debug [w/h error]: %s" % self.filename)
		finally:
			if is_def:
				if all((width, height)):
					return (int(width), int(height), False)
				elif any((not width, not height)):
					return (0, 0, False)

		ga = Get_AR(width, height)

		if not isinstance(ga.width, int):
			ga.width = int(ga.width)
		if not isinstance(width, int):
			width = int(width)

		if not isinstance(ga.height, int):
			ga.height = int(ga.height)
		if not isinstance(height, int):
			height = int(height)

		# is_normal, is_all, is_diff = False, False, False

		# aspect ratio block / start
		try:
			is_hd: bool = ga.width / ga.height == 16 / 9
		except:
			is_hd: bool = False

		try:
			is_sd: bool = ga.width / ga.height == 4 / 3
		except:
			is_sd: bool = False

		w = h = ar = 0  # None # 0x0x0

		sar = par = dar = 0  # sar/dar(ffmpeg)

		try:
			with open(sar_base, encoding="utf-8") as sbf:
				sar_dict = json.load(sbf)
		except:
			sar_dict = {}

			with open(sar_base, "w", encoding="utf-8") as sbf:
				json.dump(sar_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True)

		# one_file
		try:
			sar = ga.width / ga.height if ga.width > width else width / height
		except:
			sar = 0
		else:
			if all((ga.width > width, ga.height)):  # key~full_sar
				wha_str = str(
					{
						"sar": str(round(sar, 3)),
						"ga.width": ga.width,
						"ga.height": ga.height,
						"ar": str(round(ga.width / ga.height, 3)),
					}
				)
				# sar_dict[str(sar)] = [self.filename, wha_str]
			elif all((ga.width <= width, width, height)):
				wha_str = str(
					{
						"sar": str(round(sar, 3)),
						"width": width,
						"height": height,
						"ar": str(round(width / height, 3)),
					}
				)
				# sar_dict[str(sar)] = [self.filename, wha_str]
			else:
				wha_str = str(
					{
						"sar": str(round(sar, 3)),
						"width": width,
						"height": height,
						"ar": str(round(width / height, 3)),
					}
				)

			if wha_str:
				if all((not is_sd, not is_hd)):
					sar_dict[str(sar)] = [self.filename, wha_str]
				elif any((is_sd, is_hd)):
					sar_dict[str(sar)] = [
						self.filename,
						wha_str,
						str(is_sd),
						str(is_hd),
					]

		with open(sar_base, "w", encoding="utf-8") as sbf:
			json.dump(sar_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True)

		try:
			with open(par_base, encoding="utf-8") as pbf:
				par_dict = json.load(pbf)
		except:
			par_dict = {}

			with open(par_base, "w", encoding="utf-8") as pbf:
				json.dump(par_dict, pbf, ensure_ascii=False, indent=4, sort_keys=True)

		try:
			par = (
				sar / (ga.width / ga.height)
				if ga.width > width
				else sar / (width / height)
			)
		except:
			par = 0
		else:
			if all((ga.width > width, ga.height)):  # key~full_par
				wha_str = str(
					{
						"par": str(round(par, 3)),
						"sar": str(round(sar, 3)),
						"ga.width": ga.width,
						"ga.height": ga.height,
						"ar": str(round(ga.width / ga.height, 3)),
					}
				)
			elif all((ga.width <= width, width, height)):
				wha_str = str(
					{
						"par": str(round(par, 3)),
						"sar": str(round(sar, 3)),
						"width": width,
						"height": height,
						"ar": str(round(width / height, 3)),
					}
				)
			else:
				wha_str = str(
					{
						"par": str(round(par, 3)),
						"sar": str(round(sar, 3)),
						"width": width,
						"height": height,
						"ar": str(round(width / height, 3)),
					}
				)

			if wha_str:
				if all((not is_sd, not is_hd)):
					par_dict[str(par)] = [self.filename, wha_str]
				elif any((is_sd, is_hd)):
					par_dict[str(par)] = [
						self.filename,
						wha_str,
						str(is_sd),
						str(is_hd),
					]

		with open(par_base, "w", encoding="utf-8") as pbf:
			json.dump(par_dict, pbf, ensure_ascii=False, indent=4, sort_keys=True)

		try:
			with open(dar_base, encoding="utf-8") as dbf:
				dar_dict = json.load(dbf)
		except:
			dar_dict = {}

			with open(dar_base, "w", encoding="utf-8") as dbf:
				json.dump(dar_dict, dbf, ensure_ascii=False, indent=4, sort_keys=True)

		dar = sar * par

		if any((sar, par)):  # key~full_dar(skip_par)
			if all((ga.width > width, ga.height)):  # key~full
				sd_str = str(
					{
						"dar": str(round(dar, 3)),
						"sar": str(round(sar, 3)),
						"par": str(round(par, 3)),
						"ga.width": ga.width,
						"ga.height": ga.height,
					}
				)
			elif all((ga.width <= width, width, height)):
				sd_str = str(
					{
						"dar": str(round(dar, 3)),
						"sar": str(round(sar, 3)),
						"par": str(round(par, 3)),
						"width": width,
						"height": height,
					}
				)
			else:
				sd_str = str(
					{
						"dar": str(round(dar, 3)),
						"sar": str(round(sar, 3)),
						"par": str(round(par, 3)),
						"width": width,
						"height": height,
					}
				)

			if sd_str:
				if all((not is_sd, not is_hd)):
					dar_dict[str(dar)] = [self.filename, sd_str]
				elif any((is_sd, is_hd)):
					dar_dict[str(dar)] = [self.filename, sd_str, str(is_sd), str(is_hd)]

		with open(dar_base, "w", encoding="utf-8") as dbf:
			json.dump(dar_dict, dbf, ensure_ascii=False, indent=4, sort_keys=True)

		if any((sar, dar)):  # if_some(ffmpeg) # skip_par # convert
			if all((ga.width > width, ga.height)):  # key~full
				if any(
					(
						(ga.width / ga.height) == (16 / 9),
						(ga.width / ga.height) == (4 / 3),
					)
				):
					spd_str = str(
						{
							"sar": str(round(sar, 3)),
							"dar": str(round(dar, 3)),
							"ga.width": ga.width,
							"ga.height": ga.height,
							"is_(hd/sd)": [
								(ga.width / ga.height) == (16 / 9),
								(ga.width / ga.height) == (4 / 3),
							],
						}
					)  # "par":str(round(par,3))
				else:
					spd_str = str(
						{
							"sar": str(round(sar, 3)),
							"dar": str(round(dar, 3)),
							"ga.width": ga.width,
							"ga.height": ga.height,
						}
					)
			elif all((ga.width <= width, width, height)):
				if any(((width / height) == (16 / 9), (width / height) == (4 / 3))):
					spd_str = str(
						{
							"sar": str(round(sar, 3)),
							"dar": str(round(dar, 3)),
							"width": width,
							"height": height,
							"is_(hd/sd)": [
								(width / height) == (16 / 9),
								(width / height) == (4 / 3),
							],
						}
					)
				else:
					spd_str = str(
						{
							"sar": str(round(sar, 3)),
							"dar": str(round(dar, 3)),
							"width": width,
							"height": height,
						}
					)

			if spd_str:
				print(
					Style.BRIGHT
					+ Fore.GREEN
					+ "%s" % "x".join([full_to_short(self.filename), spd_str])
				)  # is_color(join)
				write_log("debug ar[list]", "%s" % "x".join([self.filename, spd_str]))
		elif all((not sar, not par, not dar)):  # if_null # can't convert
			if all((ga.width > width, ga.height)):  # key~full
				wh_str = str({"ga.width": str(ga.width), "height": str(ga.height)})
			elif all((ga.width <= width, width, height)):
				wh_str = str({"width": str(width), "height": str(height)})
			else:
				wh_str = str({"width": str(width), "height": str(height)})

			if wh_str:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "x".join([full_to_short(self.filename), wh_str])
				)  # is_color(join)
				write_log(
					"debug ar[list][some_null]",
					"%s" % "x".join([self.filename, wh_str]),
				)

		try:
			w, h, ar = ga.width_to_ar(width=ga.width, height=ga.height, owidth=640)

			assert (
				w and h and ar
			), f"Ошибка высоты, ширины и маштаба видео или файл уже обработан @get_width_height/{w}/{h}/{ar}"  # is_assert_debug
		except AssertionError:  # if_null
			logging.warning(
				"Ошибка высоты, ширины и маштаба видео или файл уже обработан @get_width_height/%s/%s"
				% (self.filename, "x".join([str(w), str(h), str(ar)]))
			)
			# raise err
		except BaseException as e:  # if_error
			logging.error(
				"Ошибка высоты, ширины и маштаба видео или файл уже обработан @get_width_height/%s/%s [%s]"
				% (self.filename, "x".join([str(w), str(h), str(ar)]), str(e))
			)
		else:
			if all(
				(ga.width > maxwidth, w, h, ar, is_calc)
			):  # if_need_optimize_script_by_width # ga.width <= maxwidth # if_not_need_optimize_script_by_width

				# int_optimized_width_and_height
				if not w != int(w):
					w = int(w)

				if not h != int(h):
					h = int(h)

				# int_default_width_and_height
				try:
					ow, oh = int(ga.width), int(ga.height)
				except:
					ow = oh = 0

				if any((w, h, ar)):  # calc_optimize_width_and_height
					logging.info(
						"Высота, ширина и маштаб видео [need_optimize] @get_width_height/%s/%s"
						% (self.filename, "x".join([str(w), str(h), str(ar)]))
					)

				if any((ow != w, oh != h)):  # compate_default_width_and_height_by_calc
					logging.info(
						"Высота, ширина и маштаб видео [default] @get_width_height/%s/%s"
						% (self.filename, "x".join([str(ow), str(oh), str(ow / oh)]))
					)

				if is_log:
					write_log(
						"debug filename[aratio]",
						f"file:{self.filename}, scale:{w}x{h}x{round(w / h, 2)}",
					)
					if any((ow != w, oh != h)):
						write_log(
							"debug filename[aratio][not_oprimized]",
							f"file:{self.filename}, scale:{ow}x{oh}x{round(ow / oh, 2)}",
						)

				try:
					job_status: str = (
						"%s" % str((ga.width, ga.height, self.filename, "ok"))
						if ga.width <= maxwidth
						else "%s" % str((ga.width, ga.height, self.filename, "job"))
					)
				except:
					job_status: str = ""

				# if width <= maxwidth:  # 640
				# print("debug [w/h/$file$]: %s" % job_status)
				if ga.width > maxwidth:  # 640
					if is_log:
						print("debug [w/h/$file$]: %s" % job_status)
					job_count += 1

		# elif all((w, h, not ar)):  # optimal(width_and_height)

		# is_normal = is_all = False
		# is_diff = True

		# return (int(w), int(h), False)

		is_nwidth = w if w != ga.width else 0
		is_nheight = h if h != ga.height else 0

		# del ga # clear_mem # debug

		# debug # @get_width_height # 0x0x640

		try:
			assert (
				is_nwidth and is_nheight and width
			), f"Нет данных для обновления маштаба или файл уже обработан @get_width_height/{is_nwidth}/{is_nheight}/{width}"  # is_calc(T/F) # is_assert_debug
		except AssertionError:  # if_null
			logging.warning(
				"Нет данных для обновления маштаба или файл уже обработан @get_width_height/%s/%s"
				% (
					self.filename,
					"x".join([str(is_nwidth), str(is_nheight), str(width)]),
				)
			)
			# raise err
			return (
				int(width),
				int(height),
				False,
			)  # logic2 # owidth/oheight/error(no_calc)
		except BaseException as e:  # if_error
			logging.error(
				"Нет данных для обновления маштаба или файл уже обработан @get_width_height/%s/%s [%s]"
				% (
					self.filename,
					"x".join([str(is_nwidth), str(is_nheight), str(width)]),
					str(e),
				)
			)
			return (
				int(width),
				int(height),
				False,
			)  # logic3 # owidth/oheight/error(no_calc)
		else:
			logging.info(
				"Данные по маштабу получены @get_width_height/%s/%s"
				% (
					self.filename,
					"x".join([str(width), str(height), str(width > is_nwidth)]),
				)
			)
			return (
				int(is_nwidth),
				int(is_nheight),
				width > is_nwidth,
			)  # logic1 # nwidth/nheight/calced(vwidth > owidth)

	def get_length(self, filename) -> int:  # 40

		duration_list: list = []
		duration_null: int = 0
		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_length/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_length/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return duration_null
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_length/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return duration_null

		cmd_fd: list = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"format=duration",
			"-of",
			"compact=p=0:nk=1",
			self.filename,
		]  # output_format
		fdi: str = "".join([path_for_queue, "duration.nfo"])

		os.system("cmd /c %s > %s" % (" ".join(cmd_fd), fdi))  # 1|und # type1 # cmd /k

		with open(fdi, encoding="utf-8") as fdif:
			duration_list = fdif.readlines()

		if os.path.exists(fdi):
			os.remove(fdi)

		try:
			duration_null: int = int(
				duration_list[0].split(".")[0]
			)  # if duration_list # is_assert_debug # duration_null //= 2 # is_true_time
		except:
			duration_null: int = 0
		finally:
			"""
			# snapshot_at_end
			if duration_null:
					try:
							parts = 10

							intervals = duration_null // parts
							intervals = int(intervals)
							interval_list = [(i * intervals, (i + 1) * intervals) for i in range(
									parts)]  # [(0, 537), (537, 1074), (1074, 1611), (1611, 2148), (2148, 2685), (2685, 3222), (3222, 3759)]

							ffmpeg_path = path_for_queue + "ffmpeg.exe"
							script_path = path_for_queue

					except:
							return duration_null # exit_without_changes
					else:
							for il in interval_list:
									try:
											cmd_snapshot = "%s -hide_banner -y -i %s -ss %d -vf 'scale=width:-1' -vframes 1 %s\image0%d.jpg" % (ffmpeg_path, self.filename, il, script_path)
											os.system(cmd_snapshot)  # is_generate_slideshow_for_current_file
									except:
											continue # break

			"""
			return duration_null

	# ffprobe -v error -select_streams v:0 -show_entries stream=level -of default=noprint_wrappers=1 <filepath> # level=50
	# ffprobe -v error -select_streams v:0 -show_entries stream=level -of default=noprint_wrappers=1:nokey=1 <filepath> # 50
	# ffprobe -v error -select_streams v:0 -show_entries stream=profile,level -of default=noprint_wrappers=1 <filepath> # ['profile=Main\n', 'level=30\n', 'profile=LC\n']

	# D:\Multimedia\Video\Big_Films\1947\Eta_zamechatelnaya_jizn(1947).mp4

	def get_profile_and_level(self, filename) -> tuple:  # 8

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_profile_and_level/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_profile_and_level/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return ("", "")
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_profile_and_level/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return ("", "")

		cmd_pl: list = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=profile,level",
			"-of",
			"default=noprint_wrappers=1",
			self.filename,
		]  # output_format
		plf: str = "".join([path_for_queue, "profile_and_level.nfo"])

		os.system(
			"cmd /c %s > %s" % (" ".join(cmd_pl), plf)
		)  # profile=High # level=50 # cmd /k

		pl_list: list = []

		with open(plf, encoding="utf-8") as plff:
			pl_list = plff.readlines()

		if len(pl_list) > 2:
			pl_list = pl_list[0:2]

		if os.path.exists(plf):
			os.remove(plf)

		is_have: bool = False

		try:
			if pl_list:
				is_have = True
		except:
			return ("", "")
		else:
			if is_have:
				# write_log("debug profilelevel", ";".join([pl_list[0].split("=")[-1].lower().strip(), pl_list[1].split("=")[-1].lower().strip(), filename]))

				return (
					pl_list[0].split("=")[-1].lower().strip(),
					pl_list[1].split("=")[-1].lower().strip(),
				)  # [main,30]

	def get_fps(
		self, filename, is_calc: bool = False, is_log: bool = True
	):  # -> any #18

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_fps/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_fps/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return 0
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_fps/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return 0

		fps_list: list = []

		# default=noprint_wrappers=1:nokey=1 # 24000/1001
		# default=noprint_wrappers=1 # r_frame_rate=24000/1001

		cmd_fps: list = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=r_frame_rate",
			"-of",
			"default=noprint_wrappers=1:nokey=1",
			self.filename,
		]  # output_format
		fpsf: str = "".join([path_for_queue, "framerate.nfo"])

		# ffprobe.exe -v error -show_entries stream=r_frame_rate -of default=noprint_wrappers=1 input

		os.system("cmd /c %s > %s" % (" ".join(cmd_fps), fpsf))  # cmd /k

		# fps_examples(23 - 60)
		# r_frame_rate=24000/1001 # 24000/1001 # round(23.97602397602398, 2)
		# r_frame_rate=25/1 # 25/1 # 25
		# r_frame_rate=24/1001 # 24/1001 # 0,023976023976024
		# r_frame_rate=2397/1001 # 2397/1001 # 2,394605394605395

		with open(fpsf, encoding="utf-8") as fpsfd:
			fps_list = fpsfd.readlines()

		r_frame_rate_regex = re.compile(r"[\d+].*[\d+]", re.M)

		fps_value: float = 0.0

		if len(fps_list) >= 1:
			for fl in fps_list:
				if r_frame_rate_regex.findall(fl):

					try:
						frame_rate: int = int(
							r_frame_rate_regex.findall(fl)[0].split("/")[0]
						)  # 24000
						some_value: int = int(
							r_frame_rate_regex.findall(fl)[0].split("/")[1]
						)  # 1001
					except:
						break
					else:
						if all((frame_rate, some_value)):
							try:
								fps_value = round(frame_rate / some_value, 2)
							except:
								fps_value = 0

								return 0
							else:
								# is_full_fps_logics
								if 23 <= fps_value <= 60:  # calc_from_23_to_60
									fps_value = int(fps_value)

								if all(
									(23 <= frame_rate <= 60, not fps_value)
								):  # fps_is_from_23_to_60
									fps_value = int(frame_rate)

								if not fps_value:
									if 2 <= len(str(frame_rate)) <= 3:  # 23..60(XXX)
										fps_value = float(str(frame_rate)[0:2])
									elif len(str(frame_rate)) == 4:  # 2397 / 2997
										fps_value = float(
											".".join(
												[
													str(frame_rate)[0:2],
													str(frame_rate)[2:4],
												]
											)
										)

								if not fps_value:
									break

		if os.path.exists(fpsf):
			os.remove(fpsf)

		try:
			fps = fps_value if fps_value else 0  # is_no_lambda

			assert (
				fps
			), f"Не могу получить скорость кадров @get_fps/{fps}"  # is_assert_debug
		except AssertionError as err:  # if_null
			fps: int = 0
			logging.warning(
				"Не могу получить скорость кадров @get_fps/%s" % self.filename
			)
			raise err
		except BaseException as e:  # if_error
			fps: int = 0
			logging.error(
				"Не могу получить скорость кадров @get_fps/%s [%s]"
				% (self.filename, str(e))
			)

		try:
			with open(fps_base, encoding="utf-8") as fbf:
				fps_dict = json.load(fbf)
		except:
			fps_dict = {}

			with open(fps_base, "w", encoding="utf-8") as fbf:
				json.dump(fps_dict, fbf, ensure_ascii=False, indent=4, sort_keys=True)

		fpsdict: dict = {}

		# --- fps_descriptions_from_google ---
		"""
		>16 FPS: recreating the look of the silent era movies
		24 FPS: the most cinematic look
		30 FPS: used by TV and excellent for live sports
		60 FPS: walking, candles being blown out, etc.
		120 FPS: people running, nature videography, etc.
		240 FPS: balloons exploding, water splashes, etc.
		480 FPS: skateboard tricks, skiing, surfing, etc.
		960+ FPS: Hyper-slow motion. Think about the explosion
		"""

		fpsdict[23] = [
			"Film; High definition video with NTSC Compatibility",
			"This is 24 FPS slowed down by 99.9% (1000/1001) to easily transfer film to NTSC video. Many HD formats (some SD formats) can record at this speed and is usually preferred over true 24 FPS because of NTSC compatibility.",
		]
		fpsdict[24] = [
			"Film; High Definition Video",
			"This is the universally accepted film frame rate. Movie theaters almost always use this frame rate. Many high definition formats can record and play back video at this rate, though 23.98 is usually chosen instead (see below).",
		]
		fpsdict[25] = [
			"PAL; HD video",
			"The European video standard. Film is sometimes shot at 25 FPS when destined for editing or distribution on PAL video.",
		]
		fpsdict[29] = [
			"NTSC; HD video",
			"This has been the color NTSC video standard since 1953. This number is sometimes inaccurately referred to as 30 FPS.*",
		]
		fpsdict[30] = [
			"HD video, early black and white NTSC video",
			"Some HD video cameras can record at 30 FPS, as opposed to 29.97 FPS. Before color was added to NTSC video signals, the frame rate was truly 30 FPS. However, this format is almost never used today.*",
		]
		fpsdict[47] = ["Unknown(47)", "FPS 47"]
		fpsdict[48] = ["Unknown(48)", "FPS 48"]
		fpsdict[50] = [
			"PAL; HD video",
			"This refers to the interlaced field rate (double the frame rate) of PAL. Some 1080i HD cameras can record at this frame rate.",
		]
		fpsdict[59] = [
			"HD video with NTSC compatibility",
			"HD cameras can record at this frame rate, which is compatible with NTSC video. It is also the interlaced field rate of NTSC video. This number is sometimes referred to as 60 FPS but it is best to use 59.94 unless you really mean 60 FPS.",
		]
		fpsdict[60] = [
			"HD video",
			"High definition equipment can often play and record at this frame rate but 59.94 FPS is much more common because of NTSC compatibility.",
		]
		fpsdict[71] = ["Unknown(71)", "FPS 71"]
		fpsdict[72] = ["Unknown(72)", "FPS 72"]
		fpsdict[92] = ["Unknown(92)", "FPS 92"]
		fpsdict[96] = ["Unknown(96)", "FPS 96"]
		fpsdict[100] = ["Unknown(100)", "FPS 100"]
		fpsdict[120] = ["Unknown(120)", "people running, nature videography, etc."]
		fpsdict[240] = ["Unknown(240)", "balloons exploding, water splashes, etc."]
		fpsdict[480] = ["Unknown(480)", "skateboard tricks, skiing, surfing, etc"]

		try:
			fps_desc = (
				";".join(fpsdict[fps])
				if fpsdict[fps][1]
				else "[Unknown framerate] [%s] [%s]" % (self.filename, str(fps))
			)  # fps_desc(full/unknown) # filename / fps_value # is_no_lambda
		except:
			fps_desc = "[Unknown framerate] [%s] [%s]" % (
				self.filename,
				str(fps),
			)  # filename / fps_value

		if any((fps, fps_desc)):
			fps_dict[self.filename.strip()] = [
				fps,
				fps_desc,
				str(type(fps)),
			]  # fps_value / fps_desc(full/unknown) / int(float)

		try:
			if fps:
				write_log(
					"debug fps[calc]", "Файл: [%s], FPS: %s" % (self.filename, str(fps))
				)  # filename / fps_value
		except:
			write_log(
				"debug fps[calc][unknown]", "Файл: [%s], FPS: None" % self.filename
			)  # filename

		try:
			if fps_desc:
				write_log(
					"debug get_fps[description]",
					"[%s] [%s]" % (fps_desc, self.filename),
				)  # fps_description / filename
		except:
			write_log(
				"debug get_fps[description][unknown]", "[None] [%s]" % self.filename
			)  # filenname

		try:
			if all((fps, fpsdict[fps][0])):
				write_log(
					"debug get_fps[type]",
					"Framerate type for [%s] [%s]" % (fpsdict[fps][0], self.filename),
				)  # framerate_type / filename
		except:
			write_log(
				"debug get_fps[type][unknown]",
				"Unknown framerate type for [None] [%s]" % self.filename,
			)  # filename

		try:
			if all((fps, fpsdict[fps])):
				write_log(
					"debug fps[data]",
					";".join([str(fps), str(fpsdict[fps]), self.filename]),
				)  # fps_value / fps_description / filename
		except:
			write_log(
				"debug fps[data][unknown]", ";".join([str(fps), self.filename])
			)  # fps_value / filename

		with open(fps_base, "w", encoding="utf-8") as fbf:
			json.dump(fps_dict, fbf, ensure_ascii=False, indent=4, sort_keys=True)

		return fps  # no_fps(null)

	def calc_vbr(
		self, width: int = 0, height: int = 0, filename: str = ""
	) -> int:  # fps - r_frame_rate #33 # # is_check_and_update
		"""Video Bitrate (kbps) 350(ULD), 350 - 800(LD), 800 - 1200(SD), 1200 – 1900(HD), 1900 – 4500(FHD)"""

		self.filename: str = filename

		scales_set = filenames_set = set()

		try:
			fname = self.filename.split("\\")[-1]
		except:
			fname = ""

		vbr_var: list = []

		try:
			assert (
				width and height
			), f"Высота или ширина указаны не верно @calc_vbr/{width}/{height}"  # is_assert_debug
		except AssertionError as err:
			width, height, is_change = self.get_width_height(
				filename=self.filename
			)  # pass_1_of_3 # no_calc("find_scale_and_status") # debug
			logging.warning(
				"Высота или ширина указаны не верно @calc_vbr/width/height/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
		except BaseException as e:
			logging.error(
				"Высота или ширина указаны не верно @calc_vbr/width/height/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)

		# temporary_hidden
		"""
		if any((not width, not height)):
			width, height, is_change = self.get_width_height(
				filename=self.filename)  # pass_1_of_3 # no_calc("find_scale_and_status")
		"""

		if (
			not os.path.exists(self.filename)
			or any((not filename, not width, not height))
			or not fname
		):  # not_exists # if_some_null
			return 0

		# old_vbr
		# motion = 4 if all((height > 720, height)) else 2  # motion={Middle motion:2, High motion:4} # baseline(1), main(2), high(4) # look_like_profile

		owidth, oheight = width, height

		fnames_set = set()  # (5) # scales_set # (5)

		try:
			ar = width / height

			assert (
				ar
			), f"Не верное значения ширины или высоты видео @calc_vbr/{ar}"  # is_assert_debug
		except AssertionError as err:  # if_null
			ar = 0
			logging.warning(
				"Не верное значения ширины или высоты видео @calc_vbr/%s"
				% self.filename
			)
			raise err
		except BaseException as e:  # if_error
			ar = 0
			logging.error(
				"Не верное значения ширины или высоты видео @calc_vbr/%s [%s]"
				% (self.filename, str(e))
			)

		# width(640) # scale # 1:1

		try:
			width: float = (
				640 if owidth > 640 else owidth
			)  # 640(if_width_more) # is_no_lambda

			assert (
				width
			), f"Ширина видео не должно быть пустым @calc_vbr/{width}"  # is_assert_debug
		except AssertionError as err:  # if_null
			width: float = 0
			logging.warning(
				"Ширина видео не должно быть пустым @calc_vbr/%s" % self.filename
			)
			raise err
		except BaseException as e:  # if_error
			width: float = 0
			logging.error(
				"Ширина видео не должно быть пустым @calc_vbr/%s [%s]"
				% (self.filename, str(e))
			)

		try:
			height: float = width / ar  # 360p

			assert (
				height
			), f"Высота видео не должно быть пустым @calc_vbr/{height}"  # is_assert_debug
		except AssertionError as err:  # if_null
			height: float = 0  # 360p
			logging.warning(
				"Высота видео не должно быть пустым @calc_vbr/%s" % self.filename
			)
			raise err
		except BaseException as e:  # if_error
			height: float = 0  # 360p
			logging.error(
				"Высота видео не должно быть пустым @calc_vbr/%s [%s]"
				% (self.filename, str(e))
			)

		if not isinstance(height, int):
			height = int(height)  # 360.000
		if all((height % 2 != 0, height)):
			height += 1  # 360

		if not isinstance(width, int):
			width = int(width)  # 640.000
		if all((width % 2 != 0, width)):
			width += 1  # 640

		if any((not width, not height)) and all((owidth, oheight)):
			width, height = owidth, oheight  # restore(width/height)

		if any((owidth != width, owidth / oheight != width / height)) and all(
			(width >= height, height)
		):  # oheight != height # filter(width/"height"/ar)

			try:
				oscale, nscale = "x".join([str(owidth), str(oheight)]), "x".join(
					[str(width), str(height)]
				)
			except:
				oscale = nscale = ""

			if all((not fname in fnames_set, fname)):
				fnames_set.add(fname)

			if not filename in filenames_set:
				filenames_set.add(filename)

				if all((not nscale in scales_set, nscale)):
					scales_set.add(nscale)  # new_scale(logging)

				# print(Style.BRIGHT + Fore.BLUE + "Старый маштаб: %s, новый маштаб: %s, файл: %s" % (oscale, nscale, filename) # ~cmd(with_scale)
				write_log(
					"debug rescale",
					"Старый маштаб: %s, новый маштаб: %s, файл: %s"
					% (oscale, nscale, filename),
				)  # ~cmd(with_scale)

		# height(360p) # scale # 1:1

		try:
			height: float = (
				360 if oheight > 360 else oheight
			)  # 360(if_height_more) # is_no_lambda

			assert (
				height
			), f"Пустое значение высоты видео @calc_vbr/{height}"  # is_assert_debug
		except AssertionError as err:  # if_null
			height: float = 0
			logging.warning("Пустое значение высоты видео @calc_vbr/%s" % self.filename)
			raise err
		except BaseException as e:  # if_error
			height: float = 0
			logging.error(
				"Пустое значение высоты видео @calc_vbr/%s [%s]"
				% (self.filename, str(e))
			)

		try:
			width: float = height * ar  # 640.000

			assert (
				width
			), f"Пустое значение ширины видео @calc_vbr/{width}"  # is_assert_debug
		except AssertionError as err:  # if_null
			width: float = 0
			logging.warning("Пустое значение ширины видео @calc_vbr/%s" % self.filename)
			raise err
		except BaseException as e:  # if_error
			width: float = 0
			logging.error(
				"Пустое значение ширины видео @calc_vbr/%s [%s]"
				% (self.filename, str(e))
			)

		if not isinstance(height, int):
			height = int(height)  # 360.000
		if all((height % 2 != 0, height)):
			height += 1  # 360

		if not isinstance(width, int):
			width = int(width)  # 640.000
		if all((width % 2 != 0, width)):
			width += 1  # 640

		# @sd
		try:
			sd_scales = asyncio.run(
				sd_generate(from_w=width, from_h=height)
			)  # insert_calc_width_and_height(sd) # debug

			assert sd_scales, "sd_generate нет sd aspect ratio"
		except AssertionError:
			sd_scales = asyncio.run(
				sd_generate(from_w=owidth, from_h=oheight)
			)  # insert_default_width_and_height
		except BaseException:
			sd_scales = []  # clear_sd_scales_if_error

		if sd_scales:
			try:
				tmp = [
					ss.strip()
					for ss in sd_scales
					if any(
						(
							"x".join([str(owidth), str(oheight)]) == ss,
							"x".join([str(width), str(height)]) == ss,
						)
					)
				]
			except:
				tmp = []

			if tmp:
				write_log(
					"debug sd_count[found]", "%s %s" % (";".join(tmp), filename)
				)  # str(tmp)
		else:
			write_log(
				"debug sd_count[notfound]",
				"%s %s" % ("x".join([str(owidth), str(oheight)]), filename),
			)

		# @hd
		try:
			hd_scales = asyncio.run(
				hd_generate(from_w=width, from_h=height)
			)  # insert_calc_width_and_height(hd) # debug

			assert hd_scales, "hd_generate нет hd aspect ratio"
		except AssertionError:
			hd_scales = asyncio.run(
				hd_generate(from_w=owidth, from_h=oheight)
			)  # insert_default_width_and_height
		except BaseException:
			hd_scales = []  # clear_hd_scales_if_error

		if hd_scales:
			try:
				tmp = [
					hs.strip()
					for hs in hd_scales
					if any(
						(
							"x".join([str(owidth), str(oheight)]) == hs,
							"x".join([str(width), str(height)]) == hs,
						)
					)
				]
			except:
				tmp = []
			else:
				if tmp:
					write_log(
						"debug hd_count[found]", "%s %s" % (";".join(tmp), filename)
					)  # str(tmp)
		else:
			write_log(
				"debug hd_count[notfound]",
				"%s %s" % ("x".join([str(owidth), str(oheight)]), filename),
			)

		# @ar
		try:
			ar_scales = asyncio.run(
				ar_generate(from_w=width, from_h=height)
			)  # insert_calc_width_and_height(hd) # debug

			assert ar_scales, "ar_generate нет aspect ratio"
		except AssertionError:
			ar_scales = asyncio.run(
				ar_generate(from_w=owidth, from_h=oheight)
			)  # insert_default_width_and_height
		except BaseException:
			ar_scales = []  # clear_ar_scales_if_error

		if ar_scales:
			try:
				tmp = [
					a_s.strip()
					for a_s in ar_scales
					if any(
						(
							"x".join([str(owidth), str(oheight)]) == a_s,
							"x".join([str(width), str(height)]) == a_s,
						)
					)
				]
			except:
				tmp = []
			else:
				if tmp:
					write_log(
						"debug ar_count[found]", "%s %s" % (";".join(tmp), filename)
					)  # str(tmp)
		else:
			write_log(
				"debug ar_count[notfound]",
				"%s %s" % ("x".join([str(owidth), str(oheight)]), filename),
			)

		if any((not width, not height)) and all((owidth, oheight)):
			width, height = owidth, oheight  # restore(width/height)

		if any((oheight != height, owidth / oheight != width / height)) and all(
			(width, height)
		):  # width >= height(some_display)

			try:
				oscale2, nscale2 = "x".join([str(owidth), str(oheight)]), "x".join(
					[str(width), str(height)]
				)
			except:
				oscale2 = nscale2 = ""

			if all((not fname in fnames_set, fname)):
				fnames_set.add(fname)

			if all((not nscale2 in scales_set, nscale2)):
				scales_set.add(nscale2)  # new_scale(logging)

				# print(Style.BRIGHT + Fore.BLUE + "Старый маштаб: %s, новый маштаб: %s, файл: %s" % (oscale2, nscale2, filename)) # ~cmd(with_scale)

				write_log(
					"debug rescale[2]",
					"Старый маштаб: %s, новый маштаб: %s, файл: %s"
					% (oscale2, nscale2, filename),
				)  # ~cmd(with_scale)

		try:
			fsize = os.path.getsize(self.filename)
			gl = self.get_length(self.filename)
		except:
			fsize = gl = 0
		else:
			if all((fsize, gl)):

				try:
					# vbr_list = list(vbr_gen()) # new(yes_gen)
					# vbr_list: list = [i for i in range(1, height * 2) if ((i * gl) / 8) * 1000 >= fsize and i % 16 == 0 and i >= height] # default
					vbr_list: list = [
						i
						for i in range(1, height * 2)
						if ((i * gl) / 8) * 1000 <= fsize
						and i % 16 == 0
						and i >= height
					]

					assert (
						vbr_list
					), "Пустой список частоты видео @calc_vbr/vbr_list"  # is_assert_debug
				except AssertionError:  # if_null
					vbr_list: list = []
					logging.warning("Пустой список частоты видео @calc_vbr/vbr_list")
					# raise err
				except BaseException as e:  # if_error
					vbr_list: list = []
					logging.error(
						"Пустой список частоты видео @calc_vbr/vbr_list [%s]" % str(e)
					)

				tmp = list(set([vl for vl in filter(lambda x: x, tuple(vbr_list))]))
				vbr_list = sorted(tmp, reverse=False)

				if vbr_list:
					vbr_var.append(max(vbr_list))  # first_vbr

		# second_vbr
		"""
		try:
			fps = self.get_fps(filename=self.filename, is_log=False)
		except:
			fps = 0
		else:
			if all((width, height)):
				if all((height < 720, motion <= 2)):
					vbr_var.append(int(width * height * fps * 8) // 1000)
				elif all((height >= 720, motion == 4)):
					vbr_var.append(int(width * height * fps * motion * 0.07) // 1000)
		"""

		try:
			assert (
				vbr_var
			), "Пустое значение частоты видео @calc_vbr/vbr_var"  # find_some_vbr # is_assert_debug
		except AssertionError:  # null_vbr # if_null
			logging.warning(
				"Пустое значение частоты видео @calc_vbr/%s" % self.filename
			)
			# raise err
			return 0
		except BaseException as e:  # if_error
			logging.error(
				"Пустое значение частоты видео @calc_vbr/%s [%s]"
				% (self.filename, str(e))
			)
			return 0
		else:
			return max(vbr_var)  # use_max_vbr

	"""
	K = 0.25
	width = 640
	height = 480
	fps = 15
	time = 20 минут = 1200 секунд
	Если программа-перекодировщик просит значение битрэйта, то выдаём ему значение (по формуле 1):

	Bitrate_kbps = (0.25 * 640 * 480 * 15) / 1024 = 1125 kbps
	"""

	def some_bitrate(
		self,
		filename,
		K: int = 0.25,
		width: int = 640,
		height: int = 480,
		fps: float = 15,
		ms: int = 1200,
	):  # 6
		try:
			sb = (K * width * height * fps) // 1024  # ?kbps # is_assert_debug
		except:
			sb = 0  # if_error

		return (filename, width, height, fps, ms, sb)  # bitrate_params(+result)

	def get_gop(self, filename, fps: int = 0, is_log: bool = True) -> int:  # 7

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_gop/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_gop/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return 0
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_gop/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return 0

		try:
			if not self.fps:
				self.fps = self.get_fps(filename=self.filename, is_log=True)
		except:
			self.gop = 0
		else:
			try:
				if self.fps:
					self.gop = self.fps * 2
			except BaseException as e:
				self.gop = 0

				if is_log:
					write_log(
						"debug get_gop[error]",
						"%s [%s]" % (self.filename, str(e)),
						is_error=True,
					)
			else:
				if is_log:
					write_log(
						"debug get_gop",
						"# ".join([self.filename, str(self.fps), str(self.gop)]),
					)

		return self.gop

	def calc_cbr(
		self, filename, abitrate: int = 128
	) -> int:  # 10 # is_check_and_update
		"""
		Constant Bit Rate
		You can target a bitrate with -b:v. This is best used with two-pass encoding. Adapting an example from the x264 encoding guide: your video is 10 minutes (600 seconds) long and an output of 50 MB is desired. Since bitrate = file size / duration:

		(50 MB * 8192 [converts MB to kilobits]) / 600 seconds = ~683 kilobits/s total bitrate
		683k - 128k (desired audio bitrate) = 555k video bitrate
		"""

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @calc_cbr/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # is_null
			logging.warning(
				"Файл отсутствует @calc_cbr/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return 0
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @calc_cbr/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return 0

		if not abitrate:
			abitrate = 128

		try:
			fsize: int = os.path.getsize(self.filename)

			assert (
				fsize
			), f"Не могу определить размер файла @calc_cbr/{fsize}"  # is_assert_debug
		except AssertionError as err:  # if_null
			fsize: int = 0
			logging.warning(
				"Не могу определить размер файла @calc_cbr/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
		except BaseException as e:  # if_error
			fsize: int = 0
			logging.error(
				"Не могу определить размер файла @calc_cbr/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
		else:
			fsize /= 1024**2

		try:
			dur: int = self.get_length(filename=filename)

			assert (
				dur
			), f"Не могу определить длину видео @calc_cbr/{dur}"  # is_assert_debug
		except AssertionError as err:  # if_null
			dur: int = 0
			logging.warning(
				"Не могу определить длину видео @calc_cbr/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
		except BaseException as e:  # if_error
			dur: int = 0
			logging.error(
				"Не могу определить длину видео @calc_cbr/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)

		if any((not fsize, not dur)):
			return 0
		elif all((fsize, dur, abitrate)):
			"""
			f, d, a = 120, 300, 128
			c = int(round(f * 8192 / d, 1)) # 3276K
			c -= a # 3148K
			"""

			try:
				cbr = int(round(fsize * 8192 / dur - abitrate, 1))
				# cbr = int(round(fsize * 8 / dur - abitrate, 1))
				cbr -= abitrate
			except:
				cbr = 0

			return cbr

	def lossy_audio(
		self,
		filename,
		abitrate: int = 128,
		channels: int = 5,
		def_channels: int = 2,
		audio_format: str = "aac",
	) -> int:  # 14
		"""
		Only certain audio codecs will be able to fit in your target output file.

		Container;Audio formats supported
		MKV/MKA;Opus, Vorbis, MP2, MP3, LC-AAC, HE-AAC, WMAv1, WMAv2, AC3, E-AC3, TrueHD
		MP4/M4A;Opus, MP2, MP3, LC-AAC, HE-AAC, AC3, E-AC3, TrueHD
		FLV/F4V;MP3, LC-AAC, HE-AAC
		3GP/3G2;LC-AAC, HE-AAC
		MPG;MP2, MP3
		PS/TS Stream;MP2, MP3, LC-AAC, HE-AAC, AC3, TrueHD
		M2TS;AC3, E-AC3, TrueHD
		VOB;MP2, AC3
		RMVB;Vorbis, HE-AAC
		WebM;Vorbis, Opus
		OGG;Vorbis, Opus
		There are more container formats available than those listed above, like mxf. Also, E-AC3 is only officially (according to Dolby) supported in mp4 (for example, E-AC3 needs editlist to remove padding of initial 256 silence samples).

		***

		{The bitrates listed here assume 2-channel stereo and a sample rate of 44.1kHz or 48kHz. Mono, speech, and quiet audio may require fewer bits.
		libopus – usable range ≥ 32Kbps. Recommended range ≥ 64Kbps [.opus]
		libfdk_aac default AAC LC profile – recommended range ≥ 128Kbps; see AAC Encoding Guide. [.aac]
		libfdk_aac -profile:a aac_he_v2 – usable range ≤ 48Kbps CBR. Transparency: Does not reach transparency. Use AAC LC instead to achieve transparency [.aac]
		libfdk_aac -profile:a aac_he – usable range ≥ 48Kbps and ≤ 80Kbps CBR. Transparency: Does not reach transparency. Use AAC LC instead to achieve transparency [.aac]
		libvorbis – usable range ≥ 96Kbps. Recommended range -aq 4 (≥ 128Kbps) [.ogg, .oga или .sb0]
		libmp3lame – usable range ≥ 128Kbps. Recommended range -aq 2 (≥ 192Kbps) [.mp3]
		ac3 or eac3 – usable range ≥ 160Kbps. Recommended range ≥ 160Kbps [.ac3]
		Example of usage:

		ffmpeg -i input.wav -c:a libfaac -q:a 330 -cutoff 15000 output.m4a
		aac – usable range ≥ 32Kbps (depending on profile and audio). Recommended range ≥ 128Kbps
		Example of usage:
		ffmpeg -i input.wav output.m4a
		libtwolame – usable range ≥ 192Kbps. Recommended range ≥ 256Kbps
		mp2 – usable range ≥ 320Kbps. Recommended range ≥ 320Kbps
		The vorbis and wmav1/wmav2 encoders are not worth using.
		The wmav1/wmav2 encoder does not reach transparency at any bitrate.
		The vorbis encoder does not use the bitrate specified in FFmpeg. On some samples it does sound reasonable, but the bitrate is very high.

		To calculate the bitrate to use for multi-channel audio: (bitrate for stereo) x (channels / 2).
		Example for 5.1 (6 channels) Vorbis audio: 128Kbps x (6 / 2) = 384Kbps}
		"""

		# ffprobe -v error -show_entries stream=channels,channel_layout -of default=nw=1 input.wav # channels=6 channel_layout=5.1
		# ffprobe -v error -show_entries stream=channel_layout -of csv=p=0 input.wav # 5.1

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсуствует @lossy_audio/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсуствует @lossy_audio/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return 0
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсуствует @lossy_audio/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return 0

		# abitrate # channels
		if audio_format.lower() in ["opus"]:
			abitrate: int = 64
		elif audio_format.lower() in ["aac", "libfdk_aac", "vorbis", "libvorbis"]:
			abitrate: int = 128
		elif audio_format.lower() in ["mp3", "libmp3lame"]:
			abitrate: int = 192
		elif audio_format.lower() in ["ac3", "eac3"]:
			abitrate: int = 160

		try:
			abr: int = int(round(abitrate * (channels / def_channels), 1))

			assert (
				abr
			), f"Немогу определить частоту аудио @lossy_audio/{abr}"  # is_assert_debug
		except AssertionError as err:  # if_null
			abr: int = 0
			logging.warning(
				"Немогу определить частоту аудио @lossy_audio/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
		except BaseException as e:  # if_error
			abr: int = 0
			logging.error(
				"Немогу определить частоту аудио @lossy_audio/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)

		return abr  # -b:a XXXk

	def get_channels(self, filename, is_log: bool = True) -> int:  # 5

		self.filename: str = filename

		try:
			assert self.filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @get_channels/{self.filename}"  # is_assert_debug # self.filename
		except AssertionError as err:  # if_null
			logging.warning(
				"Файл отсутствует @get_channels/%s [%s]"
				% (self.filename, str(datetime.now()))
			)
			raise err
			return 0
		except BaseException as e:  # if_error
			logging.error(
				"Файл отсутствует @get_channels/%s [%s] [%s]"
				% (self.filename, str(e), str(datetime.now()))
			)
			return 0

		clcmd: list = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=channels",
			"-of",
			"default=noprint_wrappers=1",
			"%s" % self.filename,
		]
		clf: str = "".join([path_for_queue, "channels.nfo"])

		os.system("cmd /c %s > %s" % (" ".join(clcmd), clf))  # "channels=2" # cmd /k

		with open(clf, encoding="utf-8") as clfd:
			channels_list = clfd.readlines()

		try:
			if len(channels_list) == 1 and channels_list[0].split("=")[-1]:  # normal
				self.channel = int(channels_list[0].split("=")[-1])

			elif len(channels_list) > 1:
				channels_list = channels_list[0:1]  # only_first
				self.channel = int(channels_list[0].split("=")[-1])
		except:
			self.channel = 0

			if is_log:
				print(
					Style.BRIGHT
					+ Fore.RED
					+ "Ошибка аудио канала для файла %s" % self.filename
				)
				write_log(
					"debug audio_channel[error]",
					"Ошибка аудио канала для файла %s" % self.filename,
				)
		else:
			if self.channel:  # mono(1)/stereo(2)/...

				channel_dict: dict = {}

				channel_str: str = ""

				if int(self.channel) == 1:
					channel_dict["1"] = f"{str(self.channel)};Mono"
				elif int(self.channel) == 2:
					channel_dict["2"] = f"{str(self.channel)};Stereo"
				elif int(self.channel) == 3:
					channel_dict["3"] = f"{str(self.channel)};Stereo/Surround"
				elif int(self.channel) == 4:
					channel_dict["4"] = f"{str(self.channel)};Quad/Side Quad/Surround"
				elif int(self.channel) == 5:
					channel_dict["5"] = f"{str(self.channel)};(Front)/Side"
					channel_dict["5.1.4"] = f"{str(self.channel)};Atmos"
				elif int(self.channel) == 6:
					channel_dict[
						"6"
					] = f"{str(self.channel)};Hexagonal (Back)/Front/(Side)"
				elif int(self.channel) == 7:
					channel_dict["7"] = f"{str(self.channel)};Side/Surround"
					channel_dict["7.1"] = f"{str(self.channel)};Wide/Surround"
					channel_dict["7.1.2"] = f"{str(self.channel)};Immersive"
					channel_dict["7.1.4"] = f"{str(self.channel)};Atmos/Immersive"
				elif int(self.channel) == 8:
					channel_dict["8"] = f"{str(self.channel)};Octagonal"
				elif int(self.channel) == 9:
					channel_dict["9"] = f"{str(self.channel)};Surround"
				elif int(self.channel) == 10:
					channel_dict["10.2"] = f"{str(self.channel)};Surround"
				elif int(self.channel) == 11:
					channel_dict["11"] = f"{str(self.channel)};Surround"
					channel_dict["11.1"] = f"{str(self.channel)};Surround"
					channel_dict["11.1.4"] = f"{str(self.channel)};Atmos"
				elif int(self.channel) == 22:
					channel_dict["22.2"] = f"{str(self.channel)};Surround"
				else:
					channel_dict[str(self.channel)] = "Unknown channel"

				try:
					assert channel_dict[str(self.channel)], ""
				except AssertionError:  # if_null
					channel_str = "Unknown channel"  # use_channel_number
				else:
					channel_str = channel_dict[
						str(self.channel)
					]  # descrition_by_channel(json)

				if is_log:
					print(
						Style.BRIGHT + Fore.CYAN + "Аудио канал для файла",
						Style.BRIGHT
						+ Fore.WHITE
						+ "%s [%s]" % (full_to_short(self.filename), channel_str),
					)
					write_log(
						"debug audio_channel",
						"Аудио канал для файла %s [%s]" % (self.filename, channel_str),
					)

		if os.path.exists(clf):
			os.remove(clf)

		return self.channel

	def get_frame_quality(self, filename, is_log: bool = True) -> float:  # 2
		"""
		Let's try to understand this with some simple calculations, but as I said before are actually done by much more complex compression algorithms.
		The calculation would be something like this:

		BIT RATE / FRAME RATE = Quality of each frame, (Mb?) = VBR / FPS
		This means that if you record something at 24 fps on a camera that uses a compression codec at 200 mbps, you have the following calculation:

		200 / 24 = 8.3 Megabits approximately in each frame
		This means that to form each of the frames that were taken in that second, 8.3 Mb were used. There are 24 photos of 8.3 Mb each forming a second of video.
		If you use the same camera to record at 60 fps, you would have:

		200 / 60 = 3.3 Mb approximately for each frame.
		So, you will have 60 frames of 3.3 Mb for every second of video.
		"""

		self.filename, frame_quality = filename, 0

		owidth: int = 0
		oheight: int = 0
		# is_change2 = False

		any_dstr = ""

		try:
			owidth, oheight, is_change2 = self.get_width_height(
				filename=self.filename, is_calc=False, is_log=False, is_def=True
			)  # frame_by_scale("find_scale_and_status")
		except:
			owidth = oheight = 0
		else:
			if (owidth / oheight) == (16 / 9):
				any_dstr = ";".join([str(owidth), str(oheight), "hd"])
			elif (owidth / oheight) == (4 / 3):
				any_dstr = ";".join([str(owidth), str(oheight), "sd"])
			else:
				any_dstr = ";".join(
					[str(owidth), str(oheight), str(round(owidth / oheight, 3))]
				)

			logging.info("@any_dstr file: %s [%s]" % (self.filename, any_dstr))

		# is_change2 = False

		# Наименование;Разрешение;Ширина(width);Высота(height);Кадров в сек.(fps);Скорость (Мб/с)
		"""
		UHD (4K);2160p;3840;2160;60;20-50
		UHD (4K);2160p;3840;2160;30;13-34
		2K;1440p;2560;1440;60;9-18
		2K;1440p;2560;1440;30;6-13
		FullHD;1080p;1920;1080;60;4,5-9
		FullHD;1080p;1920;1080;30;3-6
		HD;720p;1280;720;60;2,25-6
		HD;720p;1280;720;30;1,5-4
		SD;480p;854;480;30;0,5-2
		SD;360p;640;360;30;0,4-1
		SD;240p;426;240;30;0,3-0,7
		"""

		if not os.path.exists(filename) or any(
			(not filename, not owidth, not oheight)
		):  # not_exists # if_some_null
			return 0

		try:
			vbr: int = self.calc_vbr(
				filename=self.filename, width=owidth, height=oheight
			)
		except BaseException as e:
			vbr: int = 0

			if is_log:
				write_log(
					"debug calc_vbr[fq]",
					"%s" % ";".join([self.filename, str(e)]),
					is_error=True,
				)

		try:
			fps: int = self.get_fps(filename=self.filename, is_log=True)
		except BaseException as e:
			fps: int = 0

			if is_log:
				# "debug get_fps[fq]": "d:\\multimedia\\video\\serials_conv\\Better_Call_Saul\\Better_Call_Saul_02s10e.mp4;dump() missing 1 required positional argument: 'fp'",
				write_log(
					"debug get_fps[fq]",
					"%s" % ";".join([self.filename, str(e)]),
					is_error=True,
				)

		try:
			if all((vbr, fps)):
				frame_quality: float = float(
					str(round(vbr / fps, 2))[0:]
				)  # one_frame_video_no_filesize
		except BaseException as e:
			frame_quality: float = 0

			if is_log:
				write_log(
					"debug fq[error]",
					"Не могу определить Frame Quality для %s"
					% ";".join([self.filename, str(e)]),
					is_error=True,
				)
		else:
			if is_log:
				if frame_quality:

					try:
						fq_value = (
							float(round(frame_quality, 2))
							if isinstance(frame_quality, float)
							else int(frame_quality)
						)  # round_or_int # is_no_lambda
					except:
						fq_value = int(frame_quality)

					write_log(
						"debug fq[filesize]",
						"Блок Frame Quality по размеру файла для %s составляет %s"
						% (self.filename, str(fq_value)),
					)  # frameq_quality = vbr / fps
				else:
					write_log(
						"debug fq[filesize][unknown]",
						"Блок Frame Quality по размеру файла для %s неизвестен"
						% self.filename,
					)

		return frame_quality

	# calc # is_run(script), is_zip(backup) # is_pad(unknown)
	def sd_to_hd(
		self,
		input_file: str = "",
		swidth: int = 0,
		sheight: int = 0,
		is_run: bool = False,
		is_pad: bool = True,
		is_zip: bool = False,
		prefix: str = "_hd",
	) -> str:  # 3

		self.filename: str = input_file

		# ffmpeg -y -i input_file -vf "scale=1440:1080:flags=lanczos,pad=1920:1080:240:0" -c:a copy  output_file

		pheight = sheight

		# another_aratio(debug/test) # without_all_scales
		try:
			pwidth: float = pheight * (16 / 9)
		except:
			pwidth: float = 0

		try:
			swidth: float = pwidth * (3 / 4)
		except:
			swidth: float = 0

		if all((pwidth % 2 != 0, pwidth)):
			pwidth += 1
		if not isinstance(pwidth, int):
			pwidth = int(pwidth)

		if all((swidth % 2 != 0, swidth)):
			swidth += 1
		if not isinstance(swidth, int):
			pwidth = int(swidth)

		try:
			padx: int = abs(pwidth - swidth) // 2
		except:
			padx: int = 0
		else:
			if padx % 2 != 0:
				padx += 1  # - -> +
			if not isinstance(padx, int):
				padx = int(padx)

		try:
			is_ok: bool = (
				sheight == pheight
				and swidth < pwidth
				and all((swidth, sheight, pwidth, pheight))
			)  # difference_height
		except:
			is_ok: bool = False

		output_file = ""

		try:
			start_input_file, *middle_input_file, end_input_file = input_file.split(".")
		except:
			start_input_file = middle_input_file = end_input_file = []
		else:
			sml = (start_input_file, *middle_input_file, end_input_file)
			write_log(
				"debug input_file[parts][sth]", "%s" % str(sml)
			)  # start(filename) / in_side / end(ext)

		try:
			fext = input_file.split(".")[-1]  # sml[-1]
			fnshort = input_file.split(".")[0] + "_%sp%s.%s" % (
				str(sheight),
				prefix,
				fext,
			)  # sml[0]
			output_file = fnshort  # is_nlocal
		except:
			output_file, fext = "-f null", input_file.split(".")[-1]
		else:
			if output_file:
				new_output = "".join([path_to_done, fnshort.split("\\")[-1]])
				output_file = new_output  # is_local

		sth_cmd: str = ""

		# scale=640:360:flags=lanczos,pad=640:480:0:60 # padx ~ (480 - 360) // 2

		try:
			if all(
				(
					int(swidth) != int(pwidth),
					int(sheight) == int(pheight),
					swidth,
					pwidth,
				)
			):

				"""
				try:
						# swidth, pwidth, sheight, pheight = 640, 640, 360, 480 # debug/test

						# '''
						pheight = swidth * (3/4) # pheight = 640 * (3/4) = 480 # +/- 1

						pady = (pheight - sheight) // 2 # pady = (480 - 360) // 2 = 60 # +/- 1
						# '''
				except:
						pheight = pady = 0
						sth_cmd = ""
				else:
				"""
				if sheight % 2 != 0:  # need_up(scale.height) # 16:9 -> 4:3 # debug
					sheight += 1

				if pheight % 2 != 0:  # need_up(pad.height) # 16:9 -> 4:3 # debug
					pheight += 1

				if padx % 2 != 0:  # need_up(x.pad) # 16:9 -> 4:3 # debug
					padx += 1

				if any((swidth, sheight, pwidth, pheight, padx)):
					write_log(
						"debug sth[scale][pad]",
						";".join(
							[
								str(swidth),
								str(sheight),
								str(pwidth),
								str(pheight),
								str(padx),
								input_file,
							]
						),
					)

				# -preset medium -threads 2
				sth_cmd = (
					path_for_queue
					+ 'ffmpeg -hide_banner -y -i "%s" -preset medium -threads 2 -c:v libx264 -vf "scale=%s:%s:flags=lanczos,pad=%s:%s:%s:0" -threads 2 -c:a copy "%s"'
					% (
						input_file,
						str(int(swidth)),
						str(int(sheight)),
						str(int(pwidth)),
						str(int(pheight)),
						str(int(padx)),
						output_file,
					)
				)

		# elif all((int(swidth) == int(pwidth), int(sheight) == int(pheight))):
		# sth_cmd = path_for_queue + "ffmpeg -hide_banner -y -i \"%s\" -preset medium -threads 2 -c:v libx264 -vf \"scale=%s:%s:flags=lanczos\" -threads 2 -c:a copy \"%s\"" % (input_file, str(int(swidth)), str(int(sheight)), output_file)

		except:
			sth_cmd = ""
		else:
			if all(
				(is_run, is_zip in [True, False], sth_cmd, is_ok)
			):  # script_before_job_start(in)
				# """

				# short_01s01e_xxxp.mp4 > short.zip

				# zip(job/test_when_file_added)

				is_error, zip_name = False, ""

				start_time = time()

				try:
					pcmd = os.system(sth_cmd)
					assert bool(pcmd == 0), ""
				except AssertionError:  # as e:
					is_error = True

					print(
						Style.BRIGHT
						+ Fore.RED
						+ "Ошибка запуска скрипта для файла %s" % input_file
					)
					write_log(
						"debug zip[scale][error][sdtohd]",
						"Ошибка запуска скрипта для файла %s" % input_file,
						is_error=True,
					)
				else:
					is_error = False

					zip_name = (
						crop_filename_regex.sub("", input_file.split("\\")[-1]) + ".zip"
					)

					print(
						Style.BRIGHT + Fore.GREEN + "Скрипт успешно завершён для файла",
						Style.BRIGHT + Fore.WHITE + "%s" % full_to_short(input_file),
					)
					write_log(
						"debug zip[scale][done][sdtohd]",
						"Скрипт успешно завершён для файла %s" % input_file,
					)

				end_time = time()

				is_minute = False

				try:
					ms_to_min = abs(
						end_time - start_time
					).seconds  # ms -> minute(seconds)
					ms_to_min //= 60
					ms_to_min %= 60
				except:
					ms_to_min = 0
				else:
					if ms_to_min > 60:
						ms_to_min %= 60

						is_minute = True

				write_log(
					"debug ms_to_min[sdtohd]", "%s [%s]" % (ms_to_min, str(is_minute))
				)

				try:
					if all(
						(pcmd == 0, zip_name, not is_error, "." in output_file, is_zip)
					):  # run(ok)/backup(zip_name)/no_error/some_file(output)/normal_length
						zip_backup = zipfile.ZipFile(
							"".join([path_for_queue, zip_name]), mode="w"
						)  # a(append) / # w(rewrite)

						try:
							zipfiles = zip_backup.namelist()
						except:
							zipfiles = []

						try:
							file = os.path.basename(output_file)
						except BaseException as e:
							write_log(
								"debug zip_backup[file][sdtohd][error]",
								"%s [%s]" % (str(e), str(datetime.now())),
								is_error=True,
							)
						else:
							try:
								if not file in zipfiles:
									# first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)
									zip_backup.write(
										output_file, compress_type=zipfile.ZIP_DEFLATED
									)
							except:
								# first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)
								zip_backup.write(
									output_file, compress_type=zipfile.ZIP_DEFLATED
								)

					# process_zip(sth_cmd, input_file, is_zip)
				except BaseException as e:
					write_log(
						"debug zip[error][sdtohd]",
						"Ошибка архивации файла %s [%s]" % (input_file, str(e)),
						is_error=True,
					)
				else:
					if os.path.exists("".join([path_for_queue, zip_name])):
						if is_zip:
							zip_backup.close()

					if os.path.exists(output_file) and "." in output_file:
						if is_zip:
							os.remove(output_file)

					if any((is_run, is_zip)):
						print(
							Style.BRIGHT
							+ Fore.CYAN
							+ "Архив %s готов и файл %s добавлен или обновлён за %d мин."
							% (zip_name, full_to_short(output_file), ms_to_min)
						)
						write_log(
							"debug zip[done][sdtohd]",
							"Архив %s готов и файл %s добавлен или обновлён за %d мин."
							% (zip_name, output_file, ms_to_min),
						)

		# backup(delete/if_ok)
		# """

		# @sws_flags %s # -vf flags=%s
		# fast_bilinear / bilinear / bicubic / experimental / neighbor / area / bicublin / gauss / sinc / >lanczos< / spline / "print_info" / accurate_rnd / full_chroma_int / full_chroma_inp / bitexact

		try:
			if sth_cmd:
				write_log("debug sdtohd", "%s [%s]" % (input_file, sth_cmd))
			elif not sth_cmd:  # maybe_ready
				write_log(
					"debug sdtohd[nocmd]", "%s [%s]" % (input_file, str(datetime.now()))
				)

		except:
			sth_cmd = ""

		if not pwidth:  # not pheight / not padx:
			return ""

		return sth_cmd

	# calc # is_run(script), is_zip(backup) # is_pad(.T.=sd_bars/.F.=hd_rescale)
	def hd_to_sd(
		self,
		input_file: str = "",
		swidth: int = 0,
		sheight: int = 0,
		is_run: bool = False,
		is_pad: bool = True,
		is_zip: bool = False,
		prefix: str = "_sd",
	) -> str:  # 3

		self.filename: str = input_file

		# ffmpeg -y -i input_file -vf "scale=640:360:flags=lanczos,pad=640:480:0:60" -c:a copy output_file

		pwidth = swidth

		# another_aratio(debug/test) # without_all_scales
		# if (swidth / sheight) != (4/3):

		try:
			pheight: float = pwidth / (4 / 3)
		except:
			pheight: float = 0

		if all((pheight % 2 != 0, pheight)):
			pheight -= 1
		if not isinstance(pheight, int):
			pheight = int(pheight)

		try:
			pady: int = abs(pheight - sheight) // 2
		except:
			pady: int = 0
		else:
			if pady % 2 != 0:
				pady += 1  # - -> +
			if not isinstance(pady, int):
				pady = int(pady)

		try:
			is_ok: bool = (
				swidth == pwidth
				and sheight <= pheight
				and all((swidth, sheight, pwidth, pheight))
			)  # difference_height
		except:
			is_ok: bool = False

		output_file = ""

		try:
			start_input_file, *middle_input_file, end_input_file = input_file.split(".")
		except:
			start_input_file = middle_input_file = end_input_file = []
		else:
			sml = (start_input_file, *middle_input_file, end_input_file)
			write_log(
				"debug input_file[parts][hts]", "%s" % str(sml)
			)  # start(filename) / in_side / end(ext)

		try:
			fext = input_file.split(".")[-1]  # sml[-1]
			fnshort = input_file.split(".")[0] + "_%sp%s.%s" % (
				str(sheight),
				prefix,
				fext,
			)  # sml[0]
			output_file = fnshort  # is_nlocal
		except:
			output_file, fext = "-f null", input_file.split(".")[-1]
		else:
			if output_file:
				new_output = "".join([path_to_done, fnshort.split("\\")[-1]])
				output_file = new_output  # is_local

		hts_cmd: str = ""

		# scale=640:480:flags=lanczos,pad=640:360:60:0 # padx ~ (480 - 360) // 2

		try:
			if all(
				(
					int(swidth) == int(pwidth),
					int(pheight) != int(sheight),
					sheight,
					pheight,
				)
			):

				"""
				try:
						# swidth, pwidth, sheight, pheight = 640, 640, 480, 360 # debug/test

						# '''
						pheight = swidth / (16/9) # pheight = 640 / (16/9) = 360 # +/- 1

						padx = (sheight - pheight) // 2 # padx = (480 - 360) // 2 = 60 # +/- 1
						# '''
				except:
						pheight = padx = 0
						hts_cmd = ""
				else:
				"""
				if sheight % 2 != 0:  # need_up(scale.height) # 4:3 -> 16:9 # debug
					sheight += 1

				if pheight % 2 != 0:  # need_up(pad.height) # 4:3 -> 16:9 # debug
					pheight += 1

				if pady % 2 != 0:  # need_up(y.pad) # 4:3 -> 16:9 # debug
					pady += 1

				if any((swidth, sheight, pwidth, pheight, pady)):
					write_log(
						"debug hts[scale][pad]",
						";".join(
							[
								str(swidth),
								str(sheight),
								str(pwidth),
								str(pheight),
								str(pady),
								input_file,
							]
						),
					)

				# -preset medium -threads 2
				hts_cmd = (
					path_for_queue
					+ 'ffmpeg -hide_banner -y -i "%s" -preset medium -threads 2 -c:v libx264 -vf "scale=%s:%s:flags=lanczos,pad=%s:%s:0:%s" -threads 2 -c:a copy "%s"'
					% (
						input_file,
						str(int(swidth)),
						str(int(sheight)),
						str(int(pwidth)),
						str(int(pheight)),
						str(int(pady)),
						output_file,
					)
				)

				# if all((int(swidth) == int(pwidth), int(sheight) == int(pheight))):
				# hts_cmd = path_for_queue + "ffmpeg -hide_banner -y -i \"%s\" -preset medium -threads 2 -c:v libx264 -vf \"scale=%s:%s:flags=lanczos\" -threads 2 -c:a copy \"%s\"" % (input_file, str(int(swidth)), str(int(sheight)), output_file)
		except:
			hts_cmd = ""
		else:
			if all(
				(is_run, is_zip in [True, False], hts_cmd, is_ok)
			):  # script_before_job_start(in)
				# """
				# short_01s01e_xxxp.mp4 > short.zip

				# zip(job/test_when_file_added)

				is_error, zip_name = False, ""

				start_time = time()

				try:
					pcmd = os.system(hts_cmd)
					assert bool(pcmd == 0), ""
				except AssertionError:  # as e:
					is_error = True

					print(
						Style.BRIGHT
						+ Fore.RED
						+ "Ошибка запуска скрипта для файла %s" % input_file
					)
					write_log(
						"debug zip[scale][error][hdtosd]",
						"Ошибка запуска скрипта для файла %s" % input_file,
						is_error=True,
					)
				else:
					is_error = False

					zip_name = (
						crop_filename_regex.sub("", input_file.split("\\")[-1]) + ".zip"
					)

					print(
						Style.BRIGHT + Fore.GREEN + "Скрипт успешно завершён для файла",
						Style.BRIGHT + Fore.WHITE + "%s" % full_to_short(input_file),
					)
					write_log(
						"debug zip[scale][done][hdtosd]",
						"Скрипт успешно завершён для файла %s" % input_file,
					)

				end_time = time()

				is_minute = False

				try:
					ms_to_min = abs(
						end_time - start_time
					).seconds  # ms -> minute(seconds)
					ms_to_min //= 60
					ms_to_min %= 60
				except:
					ms_to_min = 0
				else:
					if ms_to_min > 60:
						ms_to_min %= 60

						is_minute = True
						write_log(
							"debug ms_to_min[hdtosd]",
							"%s [%s]" % (ms_to_min, str(is_minute)),
						)

				try:
					if all(
						(pcmd == 0, zip_name, not is_error, "." in output_file, is_zip)
					):  # run(ok)/backup(zip_name)/no_error/some_file(output)/normal_length
						zip_backup = zipfile.ZipFile(
							"".join([path_for_queue, zip_name]), mode="w"
						)  # a(append) / # w(rewrite)

						try:
							zipfiles = zip_backup.namelist()
						except:
							zipfiles = []

						try:
							file = os.path.basename(output_file)
						except BaseException as e:
							write_log(
								"debug zip_backup[file][hdtosd][error]",
								"%s [%s]" % (str(e), str(datetime.now())),
								is_error=True,
							)
						else:
							try:
								if not file in zipfiles:
									zip_backup.write(
										output_file, compress_type=zipfile.ZIP_DEFLATED
									)  # first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)
							except:
								zip_backup.write(
									output_file, compress_type=zipfile.ZIP_DEFLATED
								)  # first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)

					# process_zip(hts_cmd, input_file, is_zip)
				except BaseException as e:
					write_log(
						"debug zip[error][hdtosd]",
						"Ошибка архивации файла %s [%s]" % (input_file, str(e)),
						is_error=True,
					)
				else:
					if os.path.exists("".join([path_for_queue, zip_name])) and is_zip:
						zip_backup.close()

					if os.path.exists(output_file) and "." in output_file and is_zip:
						os.remove(output_file)

					if any((is_run, is_zip)):
						print(
							Style.BRIGHT
							+ Fore.CYAN
							+ "Архив %s готов и файл %s добавлен или обновлён за %d мин."
							% (zip_name, output_file, ms_to_min)
						)
						write_log(
							"debug zip[done][sdtohd]",
							"Архив %s готов и файл %s добавлен или обновлён за %d мин."
							% (zip_name, output_file, ms_to_min),
						)

		# backup(delete/if_ok)
		# """

		# @sws_flags %s # -vf flags=%s
		# fast_bilinear / bilinear / bicubic / experimental / neighbor / area / bicublin / gauss / sinc / >lanczos< / spline / "print_info" / accurate_rnd / full_chroma_int / full_chroma_inp / bitexact

		try:
			if hts_cmd:
				write_log("debug hdtosd", "%s [%s]" % (input_file, hts_cmd))
			elif not hts_cmd:  # maybe_ready
				write_log(
					"debug hdtosd[nocmd]", "%s [%s]" % (input_file, str(datetime.now()))
				)
		except:
			hts_cmd = ""

		if not pheight:  # not pwidth / not pady:
			return ""

		return hts_cmd

	def __del__(self):
		print("%s удалён" % str(self.__class__.__name__))


# 12
class MyTime:

	__slots__ = ["seconds"]

	def __init__(self, seconds: int = 2):  # init_attribute
		# self.__time = time() # unix_time # hidden_attribute # self._MyTime__time
		self.seconds = seconds

	def seconds_to_time(self, seconds: int = 2) -> tuple:  # 5

		try:
			assert (
				seconds
			), f"Не указано время в ms для конвертации @seconds_to_time/{seconds}"  # is_assert_debug
		except AssertionError as err:  # if_null
			logging.warning(
				f"Не указано время в ms для конвертации @seconds_to_time/{seconds}"
			)
			raise err
			return (0, 0, 0, 0)

		"""
		# totalseconds_unpack(hours/minutes/seconds)

		hours = vduration // 3600 # часы
		minutes = vduration % 3600 // 60 # минуты
		seconds = vduration % 3600 % 60 # секунды
		"""

		seconds_in_day: int = 86400  # 24*3600
		seconds_in_hour: int = 3600
		seconds_in_minute: int = 60

		days: int = 0
		hours: int = 0
		minutes: int = 0
		seconds: int = 0

		dhms: tuple = ()

		# totalseconds_unpack(days/hours/minutes/seconds)
		try:
			days = seconds // seconds_in_day
			seconds -= days * seconds_in_day
			hours = seconds // seconds_in_hour
			seconds -= hours * seconds_in_hour
			minutes = seconds // seconds_in_minute
			seconds -= minutes * seconds_in_minute
		except:
			days = hours = minutes = seconds = 0
		finally:
			dhms: tuple = (days, hours, minutes, seconds)

			return dhms  # if_normal_then_data

	# diff_date's -> hh:mm:ss
	def seconds_to_hms(self, date1, date2) -> tuple:  # 15

		self.date1, self.date2 = date1, date2

		try:
			# delta = datetime(2022, 8, 1) - datetime.now() # 21:14:XX # # -180 2:45:57 # test
			# delta = datetime.now() - datetime(dt.year, 1, 1)  # differense_new_year # 26, 21:12:20 # test
			delta = abs(self.date1 - self.date2)
		except:
			return (0, 0, 0, 0)

		# 152 # 0, 0, 2, 2 # 152 ~ mm=2
		# 2000 # 0, 0, 33, 33 # 2000 ~ mm=33
		# 5000 # 0, 1, 23, 83 # 5000 ~ hh=1/mm=23min/ss=83

		try:
			assert (
				delta.days >= 0 and delta.seconds >= 0
			), "Нет количества дней или секунд @seconds_to_hms/delta/*"  # is_assert_debug
		except AssertionError as err:  # if_null
			logging.warning(
				"Нет количества дней или секунд @seconds_to_hms/delta/* [%s]"
				% str(datetime.now())
			)
			raise err
			return (0, 0, 0, 0)
		except BaseException as e:  # if_error
			logging.error(
				"Нет количества дней или секунд @seconds_to_hms/delta/* [%s] [%s]"
				% (str(e), str(datetime.now()))
			)
			return (0, 0, 0, 0)
		else:
			# print(delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60)
			return (
				delta.days,
				delta.seconds // 3600,
				(delta.seconds // 60) % 60,
				delta.seconds % 60,
			)

	def sleep_with_count(
		self, ms: int = 2, is_log: bool = True
	):  # ms = 2 # is_ms_not_global #3
		"""Подсчитать сколько времени задержка"""

		# get_default
		try:
			# self.ms = self.seconds if self.seconds else 2 # try_load_seconds_to_pause(default~2ms)
			self.ms = (
				ms if ms else 2
			)  # try_load_seconds_to_pause(default~2ms) # is_no_lambda
		except:
			self.ms = 2  # if_error_default_only

		stime = datetime.now()

		sleep(self.seconds * 60)

		etime = datetime.now()

		# total_time = 0

		dd: int = 0
		hh: int = 0
		mm: int = 0
		# ss: int = 0

		try:
			total_time: int = abs(stime - etime).seconds
		except:
			total_time: int = 2

			if is_log:
				print(Style.BRIGHT + Fore.RED + "debug sleeptime", "pass", end="\n")

		finally:
			if total_time:
				dd, hh, mm, _ = self.seconds_to_time(seconds=total_time)  # ss -> _
				if any((dd, hh, mm)):
					if is_log:
						print(
							Style.BRIGHT + Fore.WHITE + "debug time",
							"Задержка сработала на : %d дн., %d ч., %d м."
							% (dd, hh, mm),
							end="\n",
						)


# 8
class MyString:

	# __slots__ = ["maintext", "endtext", "count", "kw"]

	def __init___(self):  # self -> self, maintext, endtext, count, kw # init_attribute
		self.__time = time()  # unix_time # hidden_attribute # self._MyString__time
		# pass # self.maintext, self.endtext, self.count, self.kw = maintext, endtext, count, kw

	def last2str(
		self, maintxt: str = "", endtxt: str = "", count: int = 1, kw: str = ""
	) -> str:  # hide_args_use_slots #26
		"""
		описание (округление) количество ключевое-слово(для_словаря)
		last2str(maintxt='кол-во', endtxt='в файле', count=1, kw='минут')

		# склонение имен существительных
		# кого/чего (родительный падеж) # 1 # нет
		# кто/что (именительный падеж) # 2 # есть
		# кого/что (винительный падеж) # 3 # вижу
		# кому/чему (дательный падеж) # дать
		# кем/чем (творительный падеж) # доволен
		# ком/чём (предложный падеж) # думать
		"""
		if maintxt:  # self.maintext
			# self.lendict = f"{maintxt} "
			self.lendict: str = "{txt} ".format(txt=maintxt)
		else:
			self.lendict: str = ""

		first = second = three = ""

		# def_dict: dict = {}

		# текст с падежами сохранить в структуре словаря(dict) -> json (manual/dump)
		try:
			with open(padeji_base, encoding="utf-8") as jf:
				def_dict = json.load(jf)
		except BaseException as e:
			isDebug: bool = not e == None or len(e) == 0
			if isDebug == True:
				write_log("debug padeji", str(e), is_error=True)

			def_dict = {}

			with open(padeji_base, "w", encoding="utf-8") as jf:
				json.dump(def_dict, jf, ensure_ascii=False, indent=4)

		# save_data
		if not def_dict:
			def_dict = {
				"1": [
					"файлов",
					"секунд",
					"часов",
					"минут",
					"процесов",
					"строк",
					"записей",
					"элементов",
					"сезонов",
					"процентов",
					"дисков",
					"папок",
					"недель",
					"дней",
					"устройств",
					"задач",
					"штуки",
				],
				"2": [
					"файл",
					"секунда",
					"час",
					"минута",
					"процес",
					"строка",
					"запись",
					"элемент",
					"сезон",
					"процент",
					"диск",
					"папка",
					"неделя",
					"день",
					"устройство",
					"задача",
					"штука",
				],
				"3": [
					"файла",
					"секунды",
					"часа",
					"минуты",
					"процеса",
					"строки",
					"записи",
					"элемента",
					"сезона",
					"процента",
					"диска",
					"папки",
					"недели",
					"дня",
					"устройства",
					"задачи",
					"штуку",
				]
				# "4": ["файлу", "секунде", "часу". "минуте", "процесу", "строке", "записи", "элементу", "сезону", "проценту", "диску", "папке", "неделю", "день", "устройству", "задачу", "штуку"],
				# "5": ["файлом", "секундой", "часом", "минутой", "процесом", "строкой", "записью", "элементом", "сезоном", "диском", "папкой", "неделей", "дню", "устройству", "задаче", "штуке"],
				# "6": ["файле", "секунде", "часе", "минуте", "процесе", "строке", "записи", "элементе", "сезоне", "диске", "папке", "неделе", "дне", "устройстве", "задаче", "штуке"]
			}

		with open(padeji_base, "w", encoding="utf-8") as jf:
			json.dump(def_dict, jf, ensure_ascii=False, indent=4)  # sort_keys=True,

		# load_data
		def_dict: dict = {}

		try:
			with open(padeji_base, encoding="utf-8") as jf:
				def_dict = json.load(jf)
		except:
			return  # exit_if_error_read

		kl: list = []

		# keyword_regex = ""
		keyword_regex = re.compile(r"(" + kw + ")", re.I)  # ?self.kw

		# найти падежи для указанного существительного
		kl: list = []
		for dd in def_dict:
			# print(type(dd), type(def_dict[dd]), end="\n")

			if dd and isinstance(def_dict[dd], list):
				for kw_l in def_dict[dd]:
					if keyword_regex.findall(kw_l):
						kl.append(kw_l)

		# print(kl) # when_only_debug

		# добавить окончания в падежи в соответствии найденного
		if len(kl) == 3:
			first = kl[0]
			second = kl[1]
			three = kl[2]

			if kw:
				write_log("debug last2str[keyword]", "последнее слово было %s" % kw)
		else:
			print("error dict padeji")
			write_log("debug dict", "error dict padeji")

		self.endtxt = endtxt  # self.endtext

		cnt = count  # ?self.count
		if cnt >= 11 and cnt <= 19:
			self.lendict += f"{cnt} " + first  # 'файлов/секунд/часов/минут/..'
		elif cnt % 10 == 1:
			self.lendict += f"{cnt} " + second  # 'файл/секунда/час/минута/..'
		elif cnt % 10 in (2, 3, 4):
			self.lendict += f"{cnt} " + three  # 'файла/секунды/часа/минуты/..'
		else:
			self.lendict += f"{cnt} " + first  # 'файлов/секунд/часов/минут/..'
		if self.endtxt:
			self.lendict += " " + self.endtxt
		return self.lendict


"""
f = File("data.txt", "r") # with File("data.txt", "r") as f: pass

del f # clear_mem # debug
"""


class File:
	def __init__(self, filename, mode):
		self.file = open(filename, mode)

	def __del__(self):
		self.file.close()


# @log_error
def clear_null_data_list(lst: list = []) -> list:  # 4
	"""Как удалить пустые строки из массива в python?"""

	temp: list = []

	try:
		assert lst, "Пустой список @clear_null_data_list/lst"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Пустой список @clear_null_data_list/lst")
		raise err
		return temp
	except BaseException as e:  # if_error
		logging.error("Пустой список @clear_null_data_list/lst [%s]" % str(e))
		return temp

	try:
		lst = list(filter(len, lst))
	except:
		lst = []
	finally:
		return lst


# --- Filter files ---


# folders_to_move
# @log_error
async def folders_filter(
	lst=[],
	folder: str = "",
	is_Rus: bool = False,
	is_Ukr: bool = False,
	is_log: bool = True,
) -> list:

	temp: list = []

	if any((not folder, not lst)):
		return temp

	main_folder = folder

	try:
		folder_list = os.listdir(main_folder)
	except:
		folder_list = []
		return folder_list  # no_folders

	temp: list = []

	try:
		# full_folder = list(folder_gen())
		# full_folder: list = ["".join([main_folder, fl]) for fl in folder_list if os.path.exists("".join([main_folder, fl]))] # old
		full_folder: list = [
			os.path.join(main_folder, fl)
			for fl in folder_list
			if os.path.exists(os.path.join(main_folder, fl))
		]
	except BaseException as e:
		full_folder: list = []
		if is_log:
			write_log(
				"debug move[folder][error][1]",
				"Ошибка генерации списка основных папок [%s]" % str(e),
				is_error=True,
			)

	if full_folder:
		tmp = list(set([ff.strip() for ff in filter(lambda x: x, tuple(full_folder))]))
		full_folder = sorted(tmp, key=os.path.getmtime)  # reverse=False

		if all((not is_Rus, not is_Ukr)):
			if is_log:
				write_log(
					"debug move[folder][1]",
					"Найдено %d основных папок [Eng]" % len(full_folder),
				)
		elif any((is_Rus, is_Ukr)):
			if is_log:
				write_log(
					"debug move[folder][1]",
					"Найдено %d основных папок [Eur]" % len(full_folder),
				)

	# --- save_folders_and_files(text/json) / null_folders / end ---

	try:
		# folder_with_files = list(files_from_folders_gen()) # new(yes_gen)
		folder_with_files: list = list(
			set(
				[
					ff.strip()
					for ff in filter(lambda x: os.path.exists(x), tuple(full_folder))
					if all((len(os.listdir(ff)) >= 1, ff))
				]
			)
		)  # 1_description # >1_videos
	except BaseException as e:
		folder_with_files: list = []
		# Ошибка генерации списка папок с файлами [[WinError 267] Неверно задано имя папки: 'd:\\multimedia\\video\\serials_conv\\01s01e.txt']
		write_log(
			"debug move[folder][error][2]",
			"Ошибка генерации списка папок с файлами [%s]" % str(e),
			is_error=True,
		)
	finally:
		folder_with_files.sort(reverse=False)  # sort_by_string
		# folder_with_files.sort(key=len, reverse=False) # sort_by_length

		# if folder_with_files:
		if all((not is_Rus, not is_Ukr)):
			if is_log:
				write_log(
					"debug move[folder][2]",
					"Найдено %d папок с файлами [Eng]" % len(folder_with_files),
				)
		elif any((is_Rus, is_Ukr)):
			if is_log:
				write_log(
					"debug move[folder][2]",
					"Найдено %d папок с файлами [Eur]" % len(folder_with_files),
				)

	try:
		folder_without_files: list = list(
			set(
				[
					ff.strip()
					for ff in filter(lambda x: os.path.exists(x), tuple(full_folder))
					if all((len(os.listdir(ff)) == 0, ff))
				]
			)
		)  # no_files
	except BaseException as e:
		folder_without_files: list = []
		write_log(
			"debug move[folder][error][3]",
			"Ошибка генерации списка папок без файлов [%s]" % str(e),
			is_error=True,
		)
	else:
		folder_without_files.sort(reverse=False)  # sort_by_string
		# folder_without_files.sort(key=len, reverse=False) # sort_by_length

		# if folder_without_files:
		if is_log:
			write_log(
				"debug move[folder][3][no_files]",
				"Нет файлов в %d папках" % len(folder_without_files),
			)

	# --- save_folders_and_files(text/json) ---

	# @vr_folder / @vr_files / debug/test

	files: list = []

	def folder_gen2(folder_list=folder_list):  # 4
		for fl in folder_list:
			if os.path.exists("".join([main_folder, fl])):
				yield "".join([main_folder, fl])

	try:
		# tmp2 = list(folder_gen2()) # new(yes_gen)
		# tmp2: list = list(set(["".join([main_folder, fl]) for fl in folder_list if os.path.exists("".join([main_folder, fl]))])) # old
		tmp2: list = list(
			set(
				[
					os.path.join(main_folder, fl)
					for fl in folder_list
					if os.path.exists(os.path.join(main_folder, fl))
				]
			)
		)
	except BaseException as e:
		tmp2: list = []

		if is_log:
			write_log(
				"debug move[folder][error][2]",
				"Ошибка генерации файлов для фильтрации [%s]" % str(e),
				is_error=True,
			)
	finally:
		full_folder2 = sorted(tmp2, reverse=False)
		# full_folder2 = sorted(tmp2, key=reverse=False)

	if full_folder2:
		try:
			# full_folder2 = list(ff2_gen()) # new(yes_gen)
			full_folder2: list = list(
				set(
					[
						ff2.strip()
						for ff2 in filter(lambda x: os.path.exists(x), tuple(temp))
						if ff2
					]
				)
			)
		except:
			full_folder2: list = []
		finally:
			full_folder2.sort(reverse=False)  # sort_by_string
			# full_folder2.sort(key=len, reverse=False) # sort_by_length

		with unique_semaphore:
			for ff2 in tuple(full_folder2):

				if os.path.exists(ff2):
					try:
						myfiles = os.listdir(ff2)
					except:
						myfiles = []
					else:
						try:
							# temp = list(fullname_gen()) # new(yes_gen)
							temp: list = [
								"\\".join([ff2, mf]).strip()
								for mf in filter(lambda x: x, tuple(myfiles))
							]
						except:
							temp: list = []

						tmp = list(
							set([t.strip() for t in filter(lambda x: x, tuple(temp))])
						)
						files += sorted(tmp, reverse=False)

		try:
			if files:
				temp = list(set(files))  # filter_unique_filenames
				files = sorted(temp, reverse=False)

				# current_files(dict)
				try:
					with open(vr_files, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except:
					ff_last = {}

					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(
							ff_last, vff, ensure_ascii=False, indent=4, sort_keys=True
						)

				# current_jobs(list)

				try:
					ff_dict = {
						f.strip(): os.path.getsize(f)
						for f in filter(lambda x: os.path.exists(x), tuple(files))
						if all((video_ext_regex.findall(f.split("\\")[-1]), f))
					}  # {filename: filesize}
				except:
					ff_dict = {}
				else:
					if all((len(ff_dict) >= 0, ff_last)):  # null_or_some # last_files
						ff_dict.update(ff_last)

				if ff_dict:
					ff_dict = {
						k: v for k, v in ff_dict.items() if os.path.exists(k)
					}  # check_exist_folder

					with open(vr_files, "w", encoding="utf-8") as vff:
						# vff.writelines("%s\n" % f.strip() for f in files) # save_files(txt) # need_json
						json.dump(
							ff_dict, vff, ensure_ascii=False, indent=4, sort_keys=True
						)  # save_list_files(exists) # is_files

		except BaseException as e:
			if is_log:
				write_log(
					"debug vr_files[error]",
					"%s [%s]" % (str(e), str(datetime.now())),
					is_error=True,
				)
		else:
			if is_log:
				write_log("debug vr_files", "ok [%s]" % str(datetime.now()))

		def folder_gen21(files=files):  # 2
			for f in filter(
				lambda x: os.path.exists("\\".join(x.split("\\")[0:-1])), tuple(files)
			):
				if all((os.listdir("\\".join(f.split("\\")[0:-1])), f)):
					yield "\\".join(f.split("\\")[0:-1]).strip()

		# if is_Rus:
		# pass # trouble_rus_rename(project_name = r"C:\Downloads\new\13_klinicheskaya_01s01e.mp4", dest_folder = r"D:\Multimedia\Video\Serials_Europe\13_Klinicheskaya_Rus")

		try:
			# full_folder2 = list(folder_gen21()) # new(yes_gen) # is_all_folders(with/without)_files_for_descriptions
			tmp2: list = list(
				set(
					[
						"\\".join(f.split("\\")[0:-1]).strip()
						for f in filter(
							lambda x: os.path.exists("\\".join(x.split("\\")[0:-1])),
							tuple(files),
						)
						if all(
							(len(os.listdir("\\".join(f.split("\\")[0:-1]))) >= 0, f)
						)
					]
				)
			)
		except:
			tmp2: list = []
		finally:
			full_folder2 = sorted(tmp2, reverse=False)  # sort_by_string
			# full_folder2 = sorted(tmp2, key=len, reverse=False) # sort_by_length

		try:
			if full_folder2:

				try:
					with open(vr_folder, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except:
					ff_last = {}

					with open(vr_folder, "w", encoding="utf-8") as vff:
						json.dump(
							ff_last, vff, ensure_ascii=False, indent=4, sort_keys=True
						)
				else:
					# pass_1_of_2(not_exists_folders)
					try:
						check_folders: list = [
							ff_check.strip()
							for ff_check in filter(
								lambda x: x, tuple(list(ff_last.keys()))
							)
							if not os.path.exists(ff_check)
						]  # restore_folders(clear_without_desc)
					except:
						check_folders: list = []
					else:
						for cf in filter(lambda x: x, tuple(check_folders)):

							if not os.path.exists(cf):
								write_log(
									"debug check_folders",
									"Папка %s не найдена [%s]" % (cf, ff_last[cf]),
								)  # ; ff_last[cf] # fullpath(short_foldername)

					tmp = list(set(check_folders))

					check_folders = sorted(tmp, reverse=False)  # sort_by_string
					# check_folders = sorted(tmp, key=len, reverse=False) # sort_by_length

					check_f_status = (
						";".join(check_folders) if check_folders else ""
					)  # is_no_lambda

					write_log("debug check_folders", "%s" % check_f_status)

					# pass_2_of_2(need_true_short_rename_is_ignorecase) # get_without_seasepis_and_extension
					try:
						check_files: list = list(
							set(
								[
									crop_filename_regex.sub("", f.split("\\")[-1])
									for ff_check in filter(
										lambda x: x, tuple(list(ff_last.values()))
									)
									for f in filter(
										lambda x: os.path.exists(x), tuple(files)
									)
									if crop_filename_regex.sub("", f.split("\\")[-1])
									in ff_check
									and crop_filename_regex.sub(
										"", f.split("\\")[-1]
									).lower()
									< len(ff_check.lower())
								]
							)
						)
					except:
						check_files: list = []
					finally:
						check_files.sort(reverse=False)

						# check_files = sorted(tmp, reverse=False) # sort_by_string
						# check_files = sorted(tmp, key=len, reverse=False) # sort_by_length

					check_f_status = (
						";".join(check_files) if check_files else ""
					)  # is_no_lambda

					write_log("debug check_files", "%s" % check_f_status)

				# ff_dict: dict = {} # debug/test

				# {folder:short_folder(for_filter)}
				try:
					ff_dict = {
						ff2.strip(): ff2.split("\\")[-1].strip()
						for ff2 in filter(
							lambda x: os.path.exists(x), tuple(full_folder2)
						)
						if all((os.listdir(ff2), ff2))
					}
				except:
					ff_dict = {}
				else:
					if all((len(ff_dict) >= 0, ff_last)):  # null_or_some # last_files
						ff_dict.update(ff_last)

				if ff_dict:
					ff_dict = {
						k: v for k, v in ff_dict.items() if os.path.exists(k)
					}  # check_exist_files

					with open(vr_folder, "w", encoding="utf-8") as vff:
						# vff.writelines("%s\n" % ff2.strip() for ff2 in full_folder2) # save_folders(txt) # need_json
						json.dump(
							ff_dict, vff, ensure_ascii=False, indent=4, sort_keys=True
						)  # save_list_files(exists) # is_folder

						# some_shortfolders_or_null_list # no_keys_only_values

					sfolders = (
						sorted(list(set(ff_dict.values())), reverse=False)
						if temp
						else []
					)  # is_no_lambda
					# sfolders = sorted(list(set(ff_dict.values())), key=len, reverse=False) if temp else []

				if all((sfolders, len(sfolders) <= 20)):
					print(
						sfolders[0 : len(sfolders)],
						"==>",
						"Папки с описаниями и файлами",
					)
					write_log(
						"debug fullfolders[names]",
						"%s" % ";".join(sfolders[0 : len(sfolders)]),
					)
				elif len(sfolders) > 20:
					print(sfolders[0:20], "==>", "Папки с описаниями и файлами")
					write_log(
						"debug fullfolders[names]", "%s" % ";".join(sfolders[0:20])
					)
				else:
					write_log(
						"debug fullfolders[null]", "Нет папок с описаниями и файлами"
					)

				# print(sfolders, "==>", "Папки с описаниями и файлами")
				# write_log("debug fullfolders[names]", "%s" % ";".join(sfolders))

				# try_save_from_trends_no_by_current_jobs # skip_trends
				try:
					with open(trends_base, encoding="utf-8") as tbf:
						trends_dict = json.load(tbf)
				except:
					trends_dict = {}

				first_len = second_len = 0

				first_len: int = len(trends_dict)

				# get_not_optimized
				try:
					with open(some_base, encoding="utf-8") as sbf:
						somebase_dict = json.load(sbf)
				except:
					somebase_dict = {}

					with open(some_base, "w", encoding="utf-8") as sbf:
						json.dump(
							somebase_dict,
							sbf,
							ensure_ascii=False,
							indent=4,
							sort_keys=True,
						)

				# '''
				first_len = second_len = 0

				first_len = len(trends_dict)

				trends_dict = {
					k: v
					for k, v in trends_dict.items()
					for s in sorted(
						trends_dict, key=lambda trends: ((trends[1], trends[0]))
					)
					if k == s
				}

				# os.path.getmtime() -> str(datetime.fromtimestamp())
				# "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2]) in str(datetime.today()) # filter_by_datetime
				# "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2]) in str(datetime.fromtimestamp(os.path.getmtime(k))) # filter_by_modify_date

				# update_every_run
				if all(
					(somebase_dict, len(trends_dict) >= 0)
				):  # current_trends_by_month(not_optimizied_job)
					trends_dict = {
						crop_filename_regex.sub(
							"", k.split("\\")[-1]
						).strip(): unixtime_to_date(os.path.getmtime(k))
						for k, v in somebase_dict.items()
						if "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2])
						in unixtime_to_date(os.path.getmtime(k))
					}  # stay_not_optimized_jobs_by_current_month

					write_log(
						"debug trends_dict[save1]",
						"%s"
						% ";".join([";".join([*trends_dict]), str(datetime.now())]),
					)

				elif all(
					(not somebase_dict, trends_dict)
				):  # current_trends_by_month(no_base)
					trends_dict = {
						k: v
						for k, v in trends_dict.items()
						if "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2])
						in v.strip()
					}  # stay_only_this_month(other_clear)

					write_log(
						"debug trends_dict[save2]",
						"%s"
						% ";".join([";".join([*trends_dict]), str(datetime.now())]),
					)

				second_len = len(trends_dict)

				if all((trends_dict, second_len)):  # second_len <= first_len
					# save_by_(optimize_base/disks_count)
					with open(trends_base, "w", encoding="utf-8") as tbf:
						json.dump(
							trends_dict,
							tbf,
							ensure_ascii=False,
							indent=4,
							sort_keys=False,
						)  # is_try_without_sort # save_by_modified

					with open(files_base["trends"], "w", encoding="utf-8") as fbtf:
						fbtf.writelines("%s\n" % t for t in [*trends_dict])
				# '''

				sfolders: list = []

				# split_date(YMD/YM/Y)
				# str(datetime.today()).split(" ")[0] # '2024-01-27'
				# "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2]) # '2024-01'
				# "-".join(str(datetime.today()).split(" ")[0].split("-")[0:1]) # '2024'

				"""
				# filter_trends_by_today(month/year)
				try:
					first_len: int = len(trends_dict)
					# trends_dict = {k: v for k, v in trends_dict.items() if str(datetime.today()).split(" ")[0].strip() in v.strip()} # stay_only_today(other_clear)
					trends_dict = {k: v for k, v in trends_dict.items() if "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2]) in v.strip()} # stay_only_in_current_month(other_clear)
				except:
					trends_dict = {k: v for k, v in trends_dict.items() if all((k, v))} # all_data_exists(all_trends)
				finally:
					second_len: int = len(trends_dict)
				"""

				if trends_dict or second_len != first_len:  # trends_list_by_count
					sfolders = (
						sorted([*trends_dict], reverse=False) if second_len else []
					)  # sort_no_need(some_data)

				with open(
					short_folders, "w", encoding="utf-8"
				) as sff:  # save_any_folders
					sff.writelines(
						"%s\n" % sf.strip()
						for sf in filter(lambda x: x, tuple(sfolders))
					)  # current_folders(short)

				if len(sfolders) >= 1 and os.path.exists(
					short_folders
				):  # if_more_or_equal_short_by_count
					with open(
						short_folders2, "w", encoding="utf-8"
					) as sff2:  # save_more_or_equal_one_folder
						sff2.writelines(
							"%s\n" % sf.strip()
							for sf in filter(lambda x: x, tuple(sfolders))
						)  # current_short(list)

					"""
					# @short_text # 'abc' 'bcd' # create_multiline # debug
					# quotes_short = list(set([sf.strip() for sf in sfolders])) # 4type1
					quotes_short = list(set([" ".join(['\'', sf, '\'']).strip() for sf in sfolders])) # 4type2
					with open(short_text, "w", encoding="utf-8") as stf:
						# stf.writelines("%s\n" % " ".join(quotes_short)) # save_short's_in_one_line(str) # type1
						stf.writelines("%s\n" % qs.strip() for qs in quotes_short) # save_short's_in_multiple_line(str) # type2
					"""
				elif len(sfolders) == 0:
					os.system("cmd /c copy nul %s" % short_folders2)  # cmd /k

		except BaseException as e:
			if is_log:
				write_log(
					"debug vr_folder[error]",
					"%s [%s]" % (str(e), str(datetime.now())),
					is_error=True,
				)

		else:
			if is_log:
				write_log("debug vr_folder", "ok [%s]" % str(datetime.now()))

	# need_check_full_folder_by_short(re.compile)
	folders_to_move: list = []

	job_file_set = set()

	prc: int = 0
	prc_brf: int = 0
	cnt: int = 0
	max_cnt: int = len(lst)

	# pass_1_of_2
	for l in filter(lambda x: x, tuple(lst)):
		for ff in filter(lambda y: y, tuple(full_folder)):

			try:
				fname = l.split("\\")[-1].strip()  # short_job(src)
				short_file = crop_filename_regex.sub("", fname)  # short_job(src)
				folder = ff.split("\\")[-1].strip()  # folder_only

				new_file = short_folder = ""

				if lang_regex.findall(folder) and any(
					(is_Rus, is_Ukr)
				):  # crop_lang_from_folder
					short_folder = lang_regex.sub("", folder)

				# len(short_folder) < len(full_folder) # eur(filter) # Igry < Igry_Rus
				try:
					is_Rus_filter = folder[0 : len(short_folder)] == short_file and all(
						(
							len(folder[0 : len(short_folder)]) < len(folder),
							folder,
							short_folder,
							short_file,
						)
					)
				except:
					is_Rus_filter = False

				# len(full_folder) == len(short_folder) # eng(filter) # Games == Games
				try:
					is_Eng_filter = folder[0 : len(short_file)] == short_file and all(
						(
							len(folder) == len(folder[0 : len(short_file)]),
							folder,
							short_file,
						)
					)
				except:
					is_Eng_filter = False

				# other_file = "\\".join([ff, fname])

				if any(
					(is_Rus_filter, is_Eng_filter)
				):  # and other_file.split("\\")[-2] == fname[0:len(other_file.split("\\")[-2])] # Rus/Eng # Compare_short_filename
					try:
						if all(
							(not is_Rus, not is_Ukr, not short_folder)
						) and os.path.exists(
							ff
						):  # english
							new_file = "\\".join([ff, fname])
						elif any((is_Rus, is_Ukr)) and os.path.exists(ff):  # europe
							if all((short_folder, len(short_folder) < len(folder))):
								new_file = "\\".join([ff, fname])
					except BaseException as e:
						new_file = ""  # if_unknown_logic

						if os.path.exists(ff):  # all_languages(error)
							if is_log:
								print(
									Style.BRIGHT
									+ Fore.RED
									+ "Файл %s прочитан с ошибкой %s" % (l, str(e))
								)
								write_log(
									"debug folder[short][error]",
									"%s [%s]" % ("\\".join([ff, fname]), str(e)),
									is_error=True,
								)

					else:
						if new_file and os.path.exists(ff):  # all_languages(no_error)
							if is_log:
								print(
									Style.BRIGHT + Fore.CYAN + "Файл",
									Style.BRIGHT
									+ Fore.WHITE
									+ "%s" % full_to_short(new_file),
									Style.BRIGHT + Fore.CYAN + "успешно прочитан",
								)
								write_log(
									"debug folder[short]", "%s" % "\\".join([ff, fname])
								)

				# elif all((not is_Rus_filter, not is_Eng_filter)):

				# write_log("debug folder[nolang]", "Нет языка для %s" % "\\".join([ff, fname]))

				if new_file:
					fname2 = new_file.split("\\")[-1].strip()  # short_job(dst)
					short_file2 = crop_filename_regex.sub("", fname2)  # short_job(dst)

			except BaseException as e:
				fname = fname2 = short_file = short_file2 = folder = new_file = ""

				if is_log:
					write_log(
						"debug param[error]",
						"Файл: %s, ошибка: %s" % (l, str(e)),
						is_error=True,
					)

			else:
				try:
					equal_short_filenames = fname == fname2 and all((fname, fname2))
				except:
					equal_short_filenames = False

				try:
					equal_short_template = short_file == short_file2 and all(
						(short_file, short_file2)
					)
				except:
					equal_short_template = False

				try:
					filter_path_by_length = folder[
						0 : len(short_file)
					] == short_file and all(
						(
							len(folder) == len(folder[0 : len(short_file)]),
							folder,
							short_file,
							not short_folder,
						)
					)  # if_english
				except:
					filter_path_by_length = False
				else:
					if not filter_path_by_length:
						filter_path_by_length = folder[
							0 : len(short_folder)
						] == short_file and all(
							(
								len(folder[0 : len(short_folder)]) < len(folder),
								folder,
								short_file,
								short_folder,
							)
						)  # if_europe

			# local(exists) / equal_short_filenames / equal_short_template / filter_path_by_length(template)
			if os.path.exists(l):
				if all(
					(equal_short_filenames, equal_short_template, filter_path_by_length)
				):
					if all((not new_file in job_file_set, new_file)):

						cnt += 1

						prc = cnt / max_cnt
						prc *= 100

						if prc == prc_brf:
							if is_log:
								print(
									Style.BRIGHT
									+ Fore.WHITE
									+ "Обработанно %d процента данных. [%s]"
									% (int(prc), fname2)
								)

							prc_brf = int(prc)

						job_file_set.add(new_file)

						try:
							filename_by_template = (
								fname[0 : len(short_file) + 1]
								== fname2[0 : len(short_file2) + 1]
							)
						except:
							filename_by_template = False

						# ["_", "("] # tv_series/cinema # l[0] <= new_file[0] # all_drives
						if all(
							(l[0] < new_file[0], filename_by_template)
						):  # difference_drive
							full_path = ff + "\\" + short_file

							# "\\".join(new_file.split("\\")[0:-1]) # path_without_file

							# debug/test
							season_regex = re.compile(
								r"_[\d+]{2,4}s", re.M
							)  # M(atchCase) # +additional(_[\d+]{2}p)
							folder_regex = re.compile(r"\([\d+]{4}\)")

							# ff(full_folder_path_no_filename) -> fname(short_filename_without_path) # debug/test

							try:
								if season_regex.findall(fname):
									write_log(
										"debug folder[season]",
										"%s [%s]"
										% (l, ",".join(season_regex.findall(fname))),
									)
								if folder_regex.findall(fname):
									write_log(
										"debug folder[cinema]",
										"%s [%s]"
										% (l, ",".join(folder_regex.findall(fname))),
									)
							except BaseException as e:
								write_log(
									"debug folder[error]",
									"Ошибка обработки папки [%s]" % str(e),
									is_error=True,
								)

							try:
								scan_files: list = [
									"\\".join([ff, ld]).strip()
									for ld in os.listdir(ff)
									if os.path.exists("\\".join([ff, ld]))
								]  # video_regex.findall(ld)
							except BaseException as e:
								scan_files: list = []
								write_log(
									"debug scanfiles[error]",
									"%s" % str(e),
									is_error=True,
								)

							if "txt" in scan_files:  # have_description

								# @description.json # (.*)\s\(.*\)\s([\d+]{1,2}\s[A-Za-z]{3}\s[\d+]{4}) # "rus" (0) / eng (1) / "date" (2)

								desc_regex = re.compile(
									r"(.*)\s\(.*\)\s([\d+]{1,2}\s[A-Za-z]{3}\s[\d+]{4})"
								)

								try:
									desc_filter: list = [
										(
											desc_regex.findall(sf)[0],
											desc_regex.findall(sf)[1],
											desc_regex.findall(sf)[2],
										)
										for sf in scan_files
										if sf.count("txt") > 0
										and desc_regex.findall(sf)
										and len(desc_regex.findall(sf)) >= 2
									]
								except:
									desc_filter: list = []
								finally:
									if sf:
										write_log(
											"debug desc_filter!",
											"Parse description for %s" % sf,
										)

								if desc_filter:
									for df in desc_filter:  # tuple -> str
										print(
											Style.BRIGHT + Fore.WHITE + "%s" % str(df)
										)  # print_for_json_data_from_tuple
										write_log(
											"debug desc_filter", "%s" % str(df)
										)  # logging_for_json_data_from_tuple

								tmp = list(
									set(
										[
											sf.strip()
											for sf in filter(
												lambda x: video_regex.findall(
													sf.split("\\")[-1]
												),
												tuple(scan_files),
											)
										]
									)
								)

								scan_files = sorted(tmp, reverse=False)

								write_log(
									"debug scanfiles", ";".join(scan_files)
								)  # only_video_files

							# compare_registry_and_rename_if_need # find_some_in_base_for_is_equal_status(local/nlocal)(os_listdir)

							# debug/test

							def diffreg(
								local_file: str = "", nlocal_file: str = ""
							):  # local_shortfile(for_check) # nlocal_file(for_path) # 3

								local_equal: list = []
								nlocal_equal: list = []

								try:
									fpath = "\\".join(
										nlocal_file.split("\\")[0:-1]
									)  # folder_for_rename_nlocal_to_local_file
								except:
									fpath = ""

								try:

									try:
										local_equal.append(local_file.strip())  # local
									except:
										local_equal = []

									try:
										nlocal_equal = [
											nf.strip()
											for nf in os.listdir(fpath)
											if all(
												(
													local_equal[0].lower().strip()
													== nf.lower().strip(),
													local_equal[0].strip()
													!= nf.strip(),
													fpath,
												)
											)
										]  # nlocal(filter)
									except:
										nlocal_equal = []

								except:
									return False  # if_some_error(get_param/list)
								else:
									try:
										if all(
											(
												local_equal[0].lower().strip()
												== nlocal_equal[0].lower().strip(),
												local_equal[0].strip()
												!= nlocal_equal[0].strip(),
											)
										):  # equal_by_one_registry # diff_by_filename
											return True  # found
										else:
											return False  # not_found
									except:
										return False  # if_some_error(logic)

							# +asyncio
							if (
								diffreg(l.split("\\")[-1], new_file)
								and l[0] < new_file[0]
								and is_log
							):
								print(
									Style.BRIGHT
									+ Fore.WHITE
									+ "Разные регистры, но один файл %s" % l
								)
								write_log(
									"debug diffreg",
									"Разные регистры, но один файл %s"
									% l.split("\\")[-1],
								)

							# need_rename_new_file_to_l_for_one_registry

							# Надо ...: d:\multimedia\video\serials_europe\Zveroboy_Rus\Zveroboy c:\...\Zveroboy_01s09e.mp4=>d:\...\Zveroboy_01s09e.mp4

							if os.path.exists(new_file):
								if is_log and all((l, new_file)):
									# full_path # difference

									print(
										Style.BRIGHT + Fore.CYAN + "Надо обновить:",
										Style.BRIGHT + Fore.YELLOW + "%s" % full_path,
										Style.BRIGHT
										+ Fore.WHITE
										+ "%s"
										% "~>".join([full_to_short(l), new_file]),
									)
									write_log(
										"debug isupdate",
										"%s" % "~>".join([l, new_file]),
									)

							elif not os.path.exists(new_file):
								if is_log and all((l, new_file)):
									# full_path # difference

									print(
										Style.BRIGHT + Fore.GREEN + "Надо записать:",
										Style.BRIGHT + Fore.YELLOW + "%s" % full_path,
										Style.BRIGHT
										+ Fore.WHITE
										+ "%s"
										% "=>".join([full_to_short(l), new_file]),
									)
									write_log(
										"debug isnew", "%s" % "~>".join([l, new_file])
									)

							if is_log:
								write_log(
									"debug folder[file]", ";".join([l, new_file])
								)  # difference

							folders_to_move.append(
								";".join([l, new_file])
							)  # difference # hidden_when_debug

	# sleep(2) # end_logging(debug)

	# pass_2_of_2
	if folders_to_move:
		temp = list(set(folders_to_move))

		folders_to_move = sorted(temp, reverse=False)

		with unique_semaphore:
			for ftm in folders_to_move:

				if is_log:
					print(
						Style.BRIGHT + Fore.GREEN + "%s" % ftm.split(";")[0],
						Style.BRIGHT + Fore.WHITE + "->",
						Style.BRIGHT + Fore.GREEN + "%s" % ftm.split(";")[-1],
					)  # src_to_dst
					write_log(
						"debug folder[filemove]",
						";".join([ftm.split(";")[0], ftm.split(";")[-1]]),
					)  # logging(local_to_nlocal)

		sleep(2)  # end(set_and_sorted)

	return folders_to_move


move_files_list: list = []


# @log_error
async def process_move(
	file1: str = "",
	file2: str = "",
	is_copy: bool = False,
	is_eq: bool = True,
	avg_size: int = 0,
):  # 40

	global move_files_list

	try:
		assert (
			file1 and file2 and os.path.exists(file1)
		), f"Не указан один из файлов или нет откуда копировать @process_move/{file1}/{file2}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(
			"Не указан один из файлов или нет откуда копировать @process_move/%s/%s"
			% (file1, file2)
		)
		raise err
		return
	except BaseException as e:  # if_error
		logging.error(
			"Не указан один из файлов или нет откуда копировать @process_move/%s/%s [%s]"
			% (file1, file2, str(e))
		)
		return

	if os.path.exists(file1):
		move_files_list.append((file1, file2, is_copy, is_eq, avg_size))

	try:
		normal_fname: bool = file1.split("\\")[-1] == file2.split("\\")[-1]
	except:  # BaseException
		normal_fname: bool = False
		logging.warning(
			"Имя файла при копировании или переносе уникально @process_move/%s/%s"
			% (file1.split("\\")[-1], file2.split("\\")[-1])
		)
		# raise err
	finally:
		try:
			fname = file1.split("\\")[-1].strip()  # if_ok_use_short
		except:
			fname = file1  # if_error_use_full

		try:
			fast_move: bool = os.path.exists(file1) and all(
				(os.path.getsize(file1) <= avg_size, avg_size >= 0)
			)  # exist_is_avg_null(is_avg)
		except:
			fast_move: bool = False

		try:
			# fast_move_status = "Быстрый перенос %s" % file1 if fast_move else "Обычный перенос %s" % file1 # is_no_lambda # old
			fast_move_status = (
				"Обычный перенос %s" % file1,
				"Быстрый перенос %s" % file1,
			)[
				fast_move
			]  # ternary
		except BaseException as e:
			fast_move_status = "Неизвестный перенос %s [%s]" % (file1, str(e))

		write_log(
			"debug process_move!", "%s %s [%d]" % (fname, fast_move_status, avg_size)
		)  # Star_Wars_The_Bad_Batch_02s03e.mp4, True, 133138825

	try:
		fname1: str = (
			full_to_short(file1) if file1.split("\\")[-1] else file1
		)  # is_no_lambda
	except:
		fname1: str = file1

	try:
		fname2: str = (
			full_to_short(file2) if file2.split("\\")[-1] else file2
		)  # is_no_lambda
	except:
		fname2: str = file2
	try:
		is_new: bool = os.path.exists(file1) and not os.path.exists(file2)
	except:
		is_new: bool = False

	try:
		is_update: bool = os.path.exists(file1) and os.path.exists(file2)
	except:
		is_update: bool = False

	try:
		equal_fsize = all((is_update, os.path.getsize(file1) == os.path.getsize(file2)))
	except:
		equal_fsize = False

	try:
		if is_eq:
			is_eqdi: bool = normal_fname == True  # equals_filenames
		elif not is_eq:
			is_eqdi: bool = any((normal_fname, not normal_fname))  # diff_filenames
	except:
		is_eqdi: bool = normal_fname == True  # equals_filenames_by_error

	try:
		if (
			any((is_new, is_update))
			and all(
				(
					fspace(file1, file2),
					any((file1[0] < file2[0], file2[0] >= file1[0])),
					file1 != file2,
				)
			)
			and all((is_eqdi, equal_fsize == False))
		):  # file2[0] >= file1[0]
			try:
				if not is_copy:
					move(file1, file2)
				elif is_copy:
					copy(file1, file2)
			except:
				pass  # return # exit_procedure_if_error
			else:
				if all((is_new, not is_update)):
					print(
						Style.BRIGHT
						+ Fore.WHITE
						+ "%s ~> %s" % (fname1.strip(), fname2.strip())
					)  # file1, file2
				elif all((is_update, not is_new)):
					print(
						Style.BRIGHT
						+ Fore.BLUE
						+ "%s ~> %s" % (fname1.strip(), fname2.strip())
					)  # file1, file2

				write_log("debug readyfile", "%s ~> %s" % (file1, file2))

		elif (
			all(
				(
					file1.split("\\")[-1] == file2.split("\\")[-1],
					any((file1[0] < file2[0], file2[0] >= file1[0])),
					file1 != file2,
					is_copy == False,
				)
			)
			and equal_fsize == True
		):
			os.remove(file1)
			write_log(
				"debug need_delete[equal][move]",
				";".join(
					[file1.title(), file2.title(), str(equal_fsize), str(is_copy)]
				),
			)  # %s/%s/%s/%s

		elif (
			all(
				(
					file1.split("\\")[-1] == file2.split("\\")[-1],
					any((file1[0] < file2[0], file2[0] >= file1[0])),
					file1 != file2,
					is_copy == True,
				)
			)
			and equal_fsize == True
		):
			write_log(
				"debug need_delete[equal][copy]",
				";".join(
					[file1.title(), file2.title(), str(equal_fsize), str(is_copy)]
				),
			)  # %s/%s/%s/%s

	except BaseException as e:
		if str(e):  # not fspace(file1, file2) # skip_if_fspace_bad
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Ошибка обработки файла %s или нет места на %s [%s]"
				% (file1, file2[0], str(e))
			)
	finally:
		if fspace(file1, file2):  # reserve(dspace)(ok)
			if equal_fsize == False:
				if os.path.exists(file1):
					MyNotify(txt=f"Файл {file2} будет обновлен", icon=icons["moved"])
				elif not os.path.exists(file1):
					MyNotify(txt=f"Файл {file2} был обновлен", icon=icons["moved"])
			elif equal_fsize == True:
				if any((file1[0] < file2[0], file2[0] >= file1[0])) and file1 != file2:
					MyNotify(
						txt=f"Файл {full_to_short(file1)} будет удален, т.к. файл уже существует",
						icon=icons["skip"],
					)
					write_log(
						"debug [dspace][equal][file1]",
						f"Файл {file1} будет удален, т.к. файл уже существует",
					)
					# os.remove(file1)
		# elif fspace(file1, file2) == False: # reserve(dspace)(bad)
		# MyNotify(txt=f"Ошибка записи файла {full_to_short(file1)} нет места", icon=icons["error"])
		# write_log("debug [dspace][error][file1]", f"Ошибка записи файла {file1} нет места")


# @log_error
async def process_delete(file1: str = ""):  # 14

	try:
		assert file1 and os.path.exists(
			file1
		), f"Файл отсутствует @process_delete/{file1}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(
			"Файл отсутствует @process_delete/%s [%s]" % (file1, str(datetime.now()))
		)
		raise err
		return
	except BaseException as e:  # if_error
		logging.error(
			"Файл отсутствует @process_delete/%s [%s] [%s]"
			% (file1, str(e), str(datetime.now()))
		)
		return

	try:
		fname = file1.split("\\")[-1].strip()
	except:
		fname = ""
	else:
		write_log("debug process_delete", "%s" % fname)
	try:
		if os.path.exists(file1):
			os.remove(file1)

			print(Style.BRIGHT + Fore.CYAN + "%s" % file1)

			write_log("debug dubfile", "%s" % file1)

			print()

	except BaseException as e:
		if str(e):
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Ошибка обработки файла %s [%s]" % (file1, str(e))
			)
	finally:
		if os.path.exists(file1):
			MyNotify(txt=f"Файл {file1} будет удалён", icon=icons["cleaner"])
		elif not os.path.exists(file1):
			MyNotify(txt=f"Файл {file1} был удалён", icon=icons["cleaner"])

	# MT = MyTime(seconds=2)
	# MT.sleep_with_count(ms=MT.seconds)
	# del MT # clear_mem # debug


# @log_error
def process_zip(cmd, filename):  # 3
	pass


async def seasonvar_parse(
	filename, is_log: bool = True
) -> any:  # convert_parsefile_to_normal_file #7

	write_log(
		"debug start[seasonvar_parse]", "%s [%s]" % (filename, str(datetime.now()))
	)

	try:
		assert filename and os.path.exists(
			filename
		), f"Файл отсутствует @seasonvar_parse/{filename}"  # is_assert_debug # filename
	except AssertionError as err:  # if_null
		logging.warning(
			"Файл отсутствует @seasonvar_parse/%s [%s]"
			% (filename, str(datetime.now()))
		)
		raise err
		return None
	except BaseException as e:  # if_error
		logging.error(
			"Файл отсутствует @seasonvar_parse/%s [%s] [%s]"
			% (filename, str(e), str(datetime.now()))
		)
		return None

	# temp: list = []

	# short_filename / parse_file_result
	temp: str = ""
	temp2: str = ""
	copyfile: str = ""

	copyfile = filename  # original_file

	try:
		fullpath = "\\".join(filename.split("\\")[0:-1])
	except:
		fullpath = ""

	# print()

	print(
		Style.BRIGHT + Fore.YELLOW + "Обработка файла",
		Style.BRIGHT + Fore.WHITE + "%s" % filename,
	)

	try:
		part1, *part2, part3 = filename.split("\\")[-1].split(".")
	except:
		part1 = part2 = part3 = ""
	else:
		filename_parts = (part1, *part2, part3)
		write_log(
			"debug filename[original]", "%s [%d]" % (filename, len(filename_parts))
		)

	# 7f_Avenue.5.S02.E03.2022.WEB-DL.1080p.ExKinoRay.a1.25.10.22.mp4
	# 7f_Nadvoe.S01.E06.2022.WEB-DL.1080p.a1.31.10.22.mp4
	# 7f_The.White.Lotus.S02.E01.2022.WEB-DL.1080p.ExKinoRay.a1.31.10.22.mp4

	# S01.E01 -> 01s01e # debug_by_some_name # debug/test # trouble_autorename -> parse_autorename
	def trouble_autorename(filename):  # 9
		# clear_seasonvar_prefix_first

		write_log("debug start[trouble_autorename]", "%s" % str(datetime.now()))

		# old_filename = filename if os.path.exists(filename) else "" # is_no_lambda # old
		old_filename = ("", filename)[os.path.exists(filename)]  # ternary

		try:
			assert (
				old_filename
			), f"Возможно файл отсутствует @trouble_autorename/{old_filename}"  # is_assert_debug
		except AssertionError:  # if_null
			logging.warning(
				f"Возможно файл отсутствует @trouble_autorename/{old_filename}"
			)
			# raise err
			return  # return None
		except BaseException as e:  # if_error
			logging.error(
				"Возможно файл отсутствует @trouble_autorename/old_filename [%s]"
				% str(e)
			)
			return

		# if not old_filename:  # exit_if_nullname
		# return None

		# filename = "c:\\temp\\7f_The.White.Lotus.S02.E01.2022.WEB-DL.1080p.ExKinoRay.a1.31.10.22.mp4"
		seep_regex = re.compile(r".*([sS]{1}[\d+]{1,2})\.([eE]{1}[\d+]{1,2}).*", re.I)
		crop_filename_regex3 = re.compile(
			r"7f_(.*)\.[sS]{1}[\d+]{1,2}\.[eE]{1}[\d+]{1,2}", re.I
		)

		def gen_to_list(filename=filename):  # 2
			for se in seep_regex.findall(filename):
				for seval in se:
					if seval:
						yield seval.strip()

		# ('S02', 'E01') # 7f_The.White.Lotus.S02.E01.2022.WEB-DL.1080p.ExKinoRay.a1.31.10.22.mp4
		try:
			# seep_str = list(gen_to_list()) # new(yes_gen)
			# [seval.strip() for se in seep_regex.findall(filename) for seval in se if seval]

			seep_str = "".join(seep_regex.findall(filename.split("\\")[-1])[0])
		except BaseException as e:
			seep_str = ""

			write_log(
				"debug seep_str[error]",
				"%s [%s] [%s]" % (filename, str(e), str(datetime.now())),
				is_error=True,
			)  # filename/error/datetime

			return None

		try:
			with open(vr_folder, encoding="utf-8") as vff:
				vf = json.load(vff)
		except:
			vf = {}

		# 'The_White_Lotus_S02E01.mp4' # need_examples
		try:
			seep_str: str = (
				"\\".join(filename.split("\\")[:-1])
				+ "\\"
				+ "_".join(
					[
						crop_filename_regex3.findall(filename.split("\\")[-1])[
							0
						].replace(".", "_"),
						seep_str,
					]
				)
				+ "".join([".", filename.split("\\")[-1].split(".")[-1]])
			)  # ; print(seep_str)
			assert seep_str, ""  # is_assert_debug
		except AssertionError as err:  # if_null
			seep_str: str = ""
			logging.warning(
				"Null templated filename [%s] [%s]" % (filename, str(datetime.now()))
			)
			raise err
			# write_log("debug seep_str[notemp]!", "Null templated filename [%s] [%s]" % (filename, str(err)), is_error=True) # hidden
		except BaseException as e:  # if_error
			seep_str: str = ""
			logging.error(
				"Error templated filename [%s] [%s] [%s]"
				% (filename, str(e), str(datetime.now()))
			)
			write_log(
				"debug seep_str[notemp]!",
				"Error templated filename [%s] [%s]" % (filename, str(e)),
				is_error=True,
			)  # is_hidden(debug)

		# (filename_by_template, short_by_base)
		tmp = list(
			set(
				[
					(seep_str.strip(), v)
					for _, v in vf.items()
					if all((v, seep_str, v in seep_str))
				]
			)
		)

		if tmp:
			write_log(
				"debug seep_str[temp]", "[%s] %s" % (filename, str(tmp))
			)  # print(filename_and_same)
		else:
			write_log(
				"debug seep_str[notemp]", "Not found same filenames [%s]" % filename
			)

		write_log(
			"debug seep_str[move]",
			"%s -> %s [%s]" % (filename, seep_str, str(datetime.now())),
		)  # filename/list/datetime

		# os.move(filename, seep_str)

		write_log("debug end[trouble_autorename]", "%s" % str(datetime.now()))

		return seep_str

	async def soundtrack_save():  # 2
		# вытащить_все_озвучки(поиграть_с_регистром)_из_списка_файлов(сохранить_их_в_логи)# debug/test

		# @soundtrack.json(base) # @soundtrack.lst(only_soundtracks_seasonvar_311022) # logging_known_soundtrack_by_file # {filename:soundtrack}

		# if_list_changed(big)_try_load_from(soundtrack.lst) # english(latin)_only

		# ручной поиск, из имени файла при записи или скачивании
		""" """

		# @files_base["soundtrack"] # manual_parse

		soundtrack: list = [
			"СТС",
			"ДТВ",
			"Swe",
			"KvK",
			"FOX",
			"2x2",
			"ТНТ",
			"MTV",
			"Ukr",
			"NTb",
			"SET",
			"Ozz",
			"SNK",
			"НТВ",
			"ТВ3",
			"Kyle",
			"DDP5",
			"Diva",
			"AMZN",
			"3xRus",
			"RenTV",
			"Getty",
			"2xRus",
			"RuDub",
			"Gravi",
			"Kerob",
			"FiliZa",
			"Cuba77",
			"RusTVC",
			"lunkin",
			"Amedia",
			"Goblin",
			"Котова",
			"AniDub",
			"qqss44",
			"Jetvis",
			"Kravec",
			"Disney",
			"SHURSH",
			"Ancord",
			"ylnian",
			"7turza",
			"AltPro",
			"HDCLUB",
			"SATRip",
			"Sci-Fi",
			"Кравец",
			"JimmyJ",
			"Kinozal",
			"Hamster",
			"1 канал",
			"HDREZKA",
			"AniFilm",
			"Сыендук",
			"RiperAM",
			"HDRezka",
			"Пифагор",
			"Files-x",
			"TVShows",
			"To4kaTV",
			"GraviTV",
			"Nicodem",
			"BaibaKo",
			"SoftBox",
			"ColdFilm",
			"DexterTV",
			"Alehandr",
			"Оригинал",
			"LostFilm",
			"Субтитры",
			"Домашний",
			"STEPonee",
			"CrazyCat",
			"Ultradox",
			"filmgate",
			"novafilm",
			"gravi-tv",
			"AlexFilm",
			"FilmGate",
			"GreenTea",
			"AniMedia",
			"GoldTeam",
			"AniLibria",
			"Axn SciFi",
			"CasStudio",
			"seasonvar",
			"MediaClub",
			"Невафильм",
			"Aleksan55",
			"Шадинский",
			"Novamedia",
			"turok1990",
			"NewStudio",
			"Nikolspup",
			"CBS Drama",
			"Universal",
			"MrMittens",
			"cinemaset",
			"Seryy1779",
			"SDI Media",
			"Paramount",
			"Nataleksa",
			"25Kuzmich",
			"ExKinoRay",
			"Persona99",
			"Sony Turbo",
			"ZoneVision",
			"WarHead.ru",
			"films.club",
			"East Dream",
			"1001cinema",
			"Shachiburi",
			"BenderBEST",
			"Sony Sci-Fi",
			"Zone Vision",
			"SAFARISOUND",
			"GeneralFilm",
			"Nickelodeon",
			"AngelOfTrue",
			"Субтитры VP",
			"Studio Band",
			"RG_Paravozik",
			"SHIZAProject",
			"Кураж-Бамбей",
			"RG.Paravozik",
			"www.Riper.AM",
			"TEPES TeamHD",
			"scarfilm.org",
			"AnimeReactor",
			"DreamRecords",
			"by_761OPiter",
			"Kuraj-Bambey",
			"кубик в кубе",
			"VO-production",
			"ViruseProject",
			"DIVA Universal",
			"www.riperam.org",
			"Wentworth Miller",
			"TVHUB",
			"LineFilm",
			"DUB",
			"MrMittens",
			"KYRAZ.BAMBEI",
			"DenSBK",
		]

		with open(files_base["stracks"], "w", encoding="utf-8") as sf:
			sf.writelines(
				"%s\n" % st.strip() for st in filter(lambda x: x, tuple(soundtrack))
			)

		try:
			# soundtrack_list = sorted(soundtrack, reverse=True) # cba_by_index
			# soundtrack_list = sorted(soundtrack, reverse=False) # abc_by_index

			soundtrack_list = sorted(soundtrack, key=len, reverse=True)  # cba_by_length
			# soundtrack_list = sorted(soundtrack, key=len, reverse=False) # abc_by_length
		except:
			soundtrack_list = []

		try:
			with open(soundtrack_base, encoding="utf-8") as sbf:
				soundtrack_dict = json.load(sbf)
		except:
			soundtrack_dict = {}

			with open(soundtrack_base, "w", encoding="utf-8") as sbf:
				json.dump(
					soundtrack_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)
		else:
			# soundtrack_in_filename_by_low_string
			try:
				soundtrack_filter = {
					filename.strip(): sl.strip()
					for sl in filter(lambda x: x, tuple(soundtrack_list))
					if any(
						(
							sl.lower().strip() in filename.lower().strip(),
							sl.strip() in filename,
						)
					)
				}
			except:
				soundtrack_filter = {}

			if soundtrack_filter:
				soundtrack_dict.update(soundtrack_filter)

		if len(soundtrack_dict) >= 0:

			# filter(lambda x: lst.count(x) != list(set(lst)).count(x), tuple(lst)) # search_moda

			try:
				soundtrack_count = [
					(v.strip(), list(soundtrack_dict.values()).count(v.strip))
					for k, v in soundtrack_dict.items()
					if sl.lower().strip() in k.lower().strip()
				]
			except:
				soundtrack_count = []
			else:
				if soundtrack_count:

					soundtrack_count_sorted = sorted(
						soundtrack_count,
						key=lambda soundtrack_count: soundtrack_count[1],
					)  # sorted_by_value
					soundtrack_count = [
						(scs[0], int(scs[1]))
						for scs in soundtrack_count_sorted
						if isinstance(soundtrack_count_sorted, tuple)
					]

					# write_log("debug soundtrack_count[low]", "%s" % str(soundtrack_count))
					write_log(
						"debug soundtrack_count[low]",
						"%d soundtrack count" % len(soundtrack_count),
					)

			try:
				soundtrack_count = {
					v.strip(): str(list(soundtrack_dict.values()).count(v.strip()))
					for k, v in soundtrack_dict.items()
				}
			except:
				soundtrack_count = {}
			else:
				if soundtrack_count:

					soundtrack_count_list = [
						(k, int(v)) for k, v in soundtrack_count.items()
					]
					soundtrack_count_sorted = sorted(
						soundtrack_count_list,
						key=lambda soundtrack_count_list: soundtrack_count_list[1],
					)  # sorted_by_value
					stc = {
						scs[0]: scs[1] for scs in soundtrack_count_sorted
					}  # sorted_json
					soundtrack_count = stc if stc else {}  # is_no_lambda

					write_log(
						"debug soundtrack_count[combine]", "%s" % str(soundtrack_count)
					)
					# write_log("debug soundtrack_count[combine]", "%d soundtracks count" % len(soundtrack_count))

					try:
						soundtrack_count_new = {
							k: int(v) for k, v in soundtrack_count.items()
						}
						s = sum(list(soundtrack_count_new.values()))
						l = len(soundtrack_count_new)
						a = s / l
						class_dict = {
							k: round((v / s) * 100, 2)
							for k, v in soundtrack_count_new.items()
							if v - a > 0
						}  # 0..100%(popular_classify)
					except BaseException as e:
						class_dict = {}
						write_log(
							"debug soundtrack_count[error]",
							"%s [%s]" % (str(None), str(e)),
							is_error=True,
						)
					else:
						try:
							sort_class = {
								s: v
								for s in sorted(
									class_dict, key=class_dict.get, reverse=False
								)
								for k, v in class_dict.items()
								if all((s, k, v, s == k))
							}
						except:
							sort_class = {}

						if all(
							(sort_class, len(sort_class) <= len(class_dict))
						):  # is_sorted_dict # less_or_equal
							class_dict = sort_class

						class_status = (
							str(class_dict) if class_dict else ""
						)  # is_no_lambda
						if class_status:
							write_log(
								"debug soundtrack_count[popular]", "%s" % class_status
							)

			with open(soundtrack_base, "w", encoding="utf-8") as sbf:
				json.dump(
					soundtrack_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)

	await soundtrack_save()

	# replace_template_if_list_here_or_not_skip(current) # get_links_from(Download_manager_hostory)_for_study_and_parse

	# ...

	# 7f_...(last_clean_up_list/new"debug"_in_down_list)

	# (.*) ?=> .* # debug/test(parser's)

	# 7f_Vstrechnaya.polosa.1.seriya.iz.4.2008.XviD.DVDRip.kinozal.tv.a1.03.02.13.mp4 # "^[\b0-9]f_([A-Za-z\.\d+]{1,}).*([\d+]{1,2})\.seriya\.iz\.([\d+]{1,2})"  # [('Vstrechnaya.polosa.', '1', '4')] # 01s(length=3)

	# manual_rules(short_templates) # try_from_files(+put_rules)

	# @clear_word_block # is_need_templates

	# ^A_(tvseries_with_noun/not_include) # is_template
	# clean_from_startswith(ignore -> match) # manual # debug/test
	clear_start_regex = re.compile(
		r"^(?:(\[Anistar\.org\][\.\_]{1}|The_|Marvels_|Marvel\'s_|DC_|DC\'s_|Tom_Clancys_))",
		re.I,
	)

	rus_regex = re.compile(r"[А-Яа-я]", re.I)

	# '''
	try:
		with open(files_base["stracks"], encoding="utf-8") as sf:
			stl = sf.readlines()
	except:
		stl = []
	else:
		if stl:
			tmp = [sl.strip() for sl in stl if not rus_regex.findall(sl)]
			st = "".join(["_", "|".join(tmp)]).replace("|", "|_").replace(" ", "_")
	# '''

	if not stl:
		# _[\d+]{4}(tvseries_with_year/include) # is_template
		# _US|_UK(tvseries_with_city/include) # is_template
		# clear_words(ignore -> match) # debug/test # [\_\.]{1}[S]{1}[\d+]{2}[\_\.]{1} # manual # debug/test
		clear_words_regex = re.compile(
			r"(?:(_Sezon_|\[[AZaz\.]{1,}\]_|\_\-|_TVShows|_LV|_KB|_WEB-DL|_[\d+]{4}))",
			re.I,
		)  # is_clear_soundtrack(regex/in_list)
	elif stl and st:
		clear_words_regex = re.compile(
			r"(?:(_Sezon_|\[[AZaz\.]{1,}\]_|\_\-|%s|_[\d+]{4}))" % st, re.I
		)  # is_clear_soundtrack(regex/in_list)

	# clear_double(ignore -> match) # Alone__Arctic__06s11e ~> Alone_Arctic_06s11e # manual # debug/test
	clear_double_regex = re.compile(r"([_]{2,})", re.M)

	# unique_filename_regex = re.compile(r"([^A-Za-zА-Яа-я0-9\-\.\(\)\[\]]{1,}|[nbsp]{4}|[\-]{2,})", re.I) # ([^A-Za-zА-Яа-я0-9\-\.\(\)\[\]]{1,}|[nbsp]{4}|[\-]{2,})) -> - # is_sep
	# fname = unique_filename_regex.sub("", fname) ?-> fname = slugify(fname)

	def parse_autorename(
		filename, ff_last: list = [], ind: int = 0
	) -> str:  # short/full/fullpath/listfiles # is_log=True #57

		write_log("debug start[parse_autorename]", "%s" % str(datetime.now()))

		if all((trouble_autorename(filename) != None, filename)):  # != None
			print(
				Style.BRIGHT + Fore.CYAN + "%s" % trouble_autorename(filename)
			)  # true_autorename_if_not_none # debug/test

		# print(Style.BRIGHT + Fore.YELLOW + "%s" % filename)

		global temp2

		# """
		# all((test.count(".") != filename.count("."), fullpath)) # converted_file # normal_file(filter)
		if all((video_ext_regex.findall(filename), filename)) and not is_log:

			# new_file = "\\".join([fullpath, filename.replace("..", ".")]) # replace_by_string

			dot_regex = re.compile(r"[\.]{2,}")
			new_file = "\\".join(
				[fullpath, dot_regex.sub(".", filename)]
			)  # replace_by_regex

			# move(copyfile, "\\".join([fullpath, fullname]))
			if is_log and all((copyfile, new_file)):
				print(
					Style.BRIGHT + Fore.WHITE + "%s" % "~~>".join([copyfile, new_file])
				)
				write_log("debug parse[files]", "%s" % "~~>".join([copyfile, new_file]))

			if all(
				(
					filename != clear_start_regex.sub("", filename),
					len(clear_start_regex.sub("", filename)) < len(filename),
					clear_start_regex.sub("", filename),
				)
			) and os.path.exists(
				copyfile
			):  # clear_start_regex.findall(filename):
				filename = clear_start_regex.sub("", filename)

			if all(
				(
					filename != clear_words_regex.sub("", filename),
					len(clear_words_regex.sub("", filename)) < len(filename),
					clear_words_regex.sub("", filename),
				)
			) and os.path.exists(
				copyfile
			):  # clear_words_regex.findall(filename):
				filename = clear_words_regex.sub("", filename)

			if all(
				(
					filename != clear_double_regex.sub("_", filename),
					len(clear_double_regex.sub("_", filename)) < len(filename),
					clear_double_regex.sub("_", filename),
				)
			) and os.path.exists(
				copyfile
			):  # clear_double.findall(filename):
				filename = clear_double_regex.sub("_", filename)

			orig_filename = copyfile
			new_filename = "\\".join([fullpath, filename])  # default_rename_by_fullpath

			clear_punc_regex = re.compile(
				r"[\!\# \$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?]{1,}", re.M
			)
			if all(
				(
					filename != clear_punc_regex.sub("", filename),
					filename,
					clear_punc_regex.sub("", filename),
				)
			):
				write_log(
					"debug parse_autorename[punc]",
					"%s [%s]" % (clear_punc_regex.sub("", filename), str(ind)),
				)  # filename = clear_punc_regex.sub("", filename)
			# new_filename = "\\".join([fullpath, filename]) # rename_without_punc_by_fullpath

			try:
				change_filename = "$".join([orig_filename, new_filename])
			except:
				change_filename = ""
			else:
				temp = {}
				temp2 = change_filename

				# check_short_fullname_in_lowercase # pass_1_of_2
				temp = {
					orig_filename.strip(): new_filename.strip()
					for ff in ff_last
					if all(
						(
							crop_filename_regex.sub("", ff.split("\\")[-1])
							.lower()
							.strip()
							== crop_filename_regex.sub("", new_filename.split("\\")[-1])
							.lower()
							.strip(),
							change_filename,
						)
					)
				}
				# temp = {orig_filename.strip():new_filename.strip() for ff in ff_last if all((crop_filename_regex.sub("", ff.split("\\")[-1]).lower().strip() == crop_filename_regex.sub("", change_filename.split("$")[-1].split("\\")[-1]).lower().strip(), change_filename))}

				# if_equal_shortfilenames # debug/test(logic)
				# '''
				if (
					crop_filename_regex.sub("", new_filename.split("\\")[-1])
					.lower()
					.strip()
					== crop_filename_regex.sub(
						"", change_filename.split("$")[-1].split("\\")[-1]
					)
					.lower()
					.strip()
				):
					write_log(
						"debug crop_filename_regex!",
						"%s"
						% crop_filename_regex.sub("", new_filename.split("\\")[-1])
						.lower()
						.strip(),
					)
				# '''

				if temp and is_log:
					print(
						temp,
						"Найден(о) %d файл(а, ов) для добавления или обновления"
						% len(temp),
						"[%s]" % str(ind),
						end="\n",
					)  # message_console2
					write_log(
						"debug parsefound[%s]" % str(ind),
						"Найден(о) %d файл(а, ов) для добавления или обновления [%s]"
						% (len(temp), new_filename),
					)

				write_log("debug end[parse_autorename]", "%s" % str(datetime.now()))

				return temp2  # return(result)

		write_log("debug end[parse_autorename][unknown]", "%s" % str(datetime.now()))

		return ""  # if_not_autorename(null_string)

	# """

	# path_for_folder1 # check_in_this_folder # autorename # debug/test

	try:
		with open(vr_files, encoding="utf-8") as vff:
			ff_last = json.load(vff)  # {filename:filesize}
	except:
		ff_last = {}

	# filename = r"7f_Beauty.and.the.Beast.S01E19.720p.WEB.rus.LostFilm.TV.a1.17.05.15.mp4"
	# try_filter = "".join(filename.split("\\")[-1].replace("7f_","").replace(".", "_")); print(try_filter)
	# Beauty_and_the_Beast_S01E19_720p_WEB_rus_LostFilm_TV_a1_17_05_15_mp4

	if ff_last:
		try:
			ff_last = {
				k: v for k, v in ff_last.items() if os.path.exists(k)
			}  # stay_only_exists(or_null)
		except:
			ff_last = {}  # skip_with_error
		else:
			with open(vr_files, "w", encoding="utf-8") as vff:
				json.dump(
					ff_last, vff, ensure_ascii=False, indent=4, sort_keys=True
				)  # save_without_error

	# convert_fullname_to_(fullpath / shortfilename)
	try:
		fp, fn = split_filename(filename)
	except:
		fn = filename.split("\\")[-1].strip()  # fp
	finally:
		temp = fn

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})", re.I
		)  # [('Hudson.and.Rex.', 's04', 'e01')] # length=3

		# temp = "7f_Hudson.and.Rex.s04e01.HD1080p.WEBRip.Rus.BaibaKo.tv.a1.10.10.21.mp4"  # 1

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Hudson.and.Rex.', 's04', 'e01')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Hudson.and.Rex.', 's04', 'e01'] # len(filelearn) >= 3

		"""
		is_error = False

		try:
			if filename != filename.replace(filename, word_to_word_dict[filename]):
				is_error = False
		except:
			is_error = True
		else:
			filename = word_to_word_dict[filename]
		"""

		seas = epis = ""

		try:
			if all(
				(
					filelearn[-2][0].lower() == "s",
					"".join(filelearn[-2][1:]).isnumeric(),
				)
			):  # 04s
				if all(
					(
						filelearn[-1][0].lower() == "e",
						"".join(filelearn[-1][1:]).isnumeric(),
					)
				):  # 01e
					if len(filelearn) >= 3:
						seas = "".join(
							["".join(filelearn[-2][1:]), filelearn[-2][0]]
						).lower()
						epis = "".join(
							["".join(filelearn[-1][1:]), filelearn[-1][0]]
						).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 03s02e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Hudson_and_Rex_04s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Hudson_and_Rex_04s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Hudson_and_Rex_04s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [1]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [1]" % (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=1
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})x([\d+]{2})", re.I
		)  # [('Ordinator.', '3', '02')] # length=3
		# temp = "7f_Ordinator.3x02-FleshofMyFlesh.a2.27.05.20.mp4"  # 2

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # Tags: [('Ordinator.', '3', '02')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Ordinator.', '3', '02'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2], "s"])
					if len(str(filelearn[-2])) == 1
					else "".join([filelearn[-2], "s"])
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(str(filelearn[-1])) == 1
					else "".join([filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 03s02e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True
			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Ordinator_03s02e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Ordinator_03s02e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Ordinator_03s02e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [2]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [2]" % (copyfile, str(e)),
				is_error=True,
			)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=2
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([\d+]{2})-([A-Za-z\.\-\d+]{1,}).*([\d+]{1}[sS]{1})ezon", re.I
		)  # [('10', 'Borgia.', '2s')] # length=3
		# temp = "7f_10-Borgia.2sezon.2012.720p.BDRip.AVC-Srg6161.a1.03.11.16.mp4"  # 3

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('10', 'Borgia.', '2s')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['10', 'Borgia.', '2s'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[0][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = (
					"".join(["0", filelearn[-1]])
					if len(filelearn[-1]) == 2
					else filelearn[-1]
				)
				epis = (
					"".join(["0", filelearn[0], "e"])
					if len(filelearn[0]) == 1
					else "".join([filelearn[0], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 02s10e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Borgia_02s10e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Borgia_02s10e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Borgia_02s10e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [3]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [3]" % (copyfile, str(e)),
				is_error=True,
			)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=3
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([\d+]{2}).*[\.]{1,}([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})",
			re.I,
		)  # [('15', 'Grand.', 's05')] # length=3
		# temp = "7f_15..Grand.s05.2021.WEB-DLRip.Files-x.a1.18.09.21.mp4"  # 4

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('15', 'Grand.', 's05')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['15', 'Grand.', 's05'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[0][0:]).isnumeric(),
					"".join(filelearn[-1][1:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
				epis = (
					"".join(["0", filelearn[0], "e"])
					if len(filelearn[0]) == 1
					else "".join([filelearn[0], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 05s15e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Grand_05s15e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # ; filename = filename[1:] # Grand_05s15e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Grand_05s15e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [4]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [4]" % (copyfile, str(e)),
				is_error=True,
			)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=4
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# unique(check_for_rus)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,})\.([\d+]{2})\.seriya\.iz\.([\d+]{2})", re.I
		)  # [('Emili', '02', '20')]
		# temp = "7f_Emili.02.seriya.iz.20.1990.XviD.TVRip.a1.09.03.14.mp4"  # 5

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Emili', '02', '20')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Emili', '02', '20'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-1][0:]).isnumeric(),
					"".join(filelearn[-2][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = "01s"
				epis = (
					"".join(["0", filelearn[-2], "e"])
					if len(filelearn[-2]) == 1
					else "".join([filelearn[-2], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s02e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_epis

			# Emili_01s02e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Emili_01s02e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Emili_01s02e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [5]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [5]" % (copyfile, str(e)),
				is_error=True,
			)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=5
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[\b0-9]f_([A-Za-z\.\-\d+]{1,}).*\[([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})",
			re.I,
		)  # [('House.of.Cards.', 'S04', 'E01')] # length=3
		# temp = "7f_House.of.Cards.[S04E01].720p.1kanal.[qqss44].a1.19.03.16.mp4"  # 6

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('House.of.Cards.', 'S04', 'E01')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['House.of.Cards.', 'S04', 'E01'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][1:]).isnumeric(),
					"".join(filelearn[-1][1:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]]).lower()
				epis += "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 04s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# House_of_Cards_04s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # House_of_Cards_04s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # House_of_Cards_04s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [6]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [6]" % (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=6
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\d+]{1,}|[A-Za-z\.\d+]{1,})).*([sS]{1}[\d+]{1}).*([\d+]{2})",
			re.I,
		)  # [('How.to.Get.Away.with.Murder.', 'S2', '10')] # length=3 # debug/test # delete '-'
		# temp = "7f_How.to.Get.Away.with.Murder.-.S2.10.,.a1.23.10.18.mp4"  # 7

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('How.to.Get.Away.with.Murder.', 'S2', '18')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['How.to.Get.Away.with.Murder.', 'S2', '10'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-1][0:]).isnumeric(),
					"".join(filelearn[-2][1:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2][-1], filelearn[-2][0]])
					if len(filelearn[-2]) == 2
					else "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]])
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(filelearn[-1]) == 1
					else "".join([filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 02s10e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# How_to_Get_Away_with_Murder_02s10e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # How_to_Get_Away_with_Murder_02s10e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # How_to_Get_Away_with_Murder_02s10e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [7]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [7]" % (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=7
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# unique(check_for_rus)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([eE]{1}[\d+]{2})",
			re.I,
		)  # [('The.Lost.Tomb.', 'E11')] # length=2 # .* -> \. # debug/test
		# temp = "7f_The.Lost.Tomb.E11.HDTVRip.BTT-TEAM.a1.08.07.16.mp4"  # 8

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('The.Lost.Tomb.', 'E11')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['The.Lost.Tomb.', 'E11'] # len(filelearn) >= 2

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][1:]).isnumeric(), len(filelearn) >= 2)):
				seas = "01s"
				epis = (
					"".join(["0", "".join(filelearn[-1][1:]), filelearn[-1][0]])
					if len(filelearn[-1]) == 2
					else "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s11e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis

			# The_Lost_Tomb_01s11e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # The_Lost_Tomb_01s11e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # The_Lost_Tomb_01s11e.mp

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [8]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [8]" % (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=8
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# unique(check)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})x([\d+]{2})", re.I
		)  # [('BirdsofPrey', '1', '13')] # length=3
		# temp = "7f_BirdsofPrey1x13-Rus.a1.19.03.13.mp4"  # 9

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('BirdsofPrey', '1', '13')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['BirdsofPrey', '1', '13'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2], "s"])
					if len(filelearn[-2]) == 1
					else "".join([filelearn[-2], "s"])
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(filelearn[-1]) == 1
					else "".join([filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s13e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# BirdsofPrey_01s13e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # BirdsofPrey_01s13e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # BirdsofPrey_01s13e.mp4 # uniq

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [9]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [9]" % (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=9
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[\b0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.([\d+]{2})\.serija",
			re.I,
		)  # [('Korolj.Kvinsa.', '1', '06')] # length=3
		# temp = "7f_Korolj.Kvinsa.1.sezon.06.serija.iz.25.1998-1999.XviD.DVDRip.a1.18.09.12.mp4"  # 10

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Korolj.Kvinsa.', '1', '06')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Korolj.Kvinsa.', '1', '06'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2], "s"])
					if len(filelearn[-2]) == 1
					else "".join([filelearn[-2], "s"])
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(filelearn[-1]) == 1
					else "".join([filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s06e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Korolj_Kvinsa_01s06e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Korolj_Kvinsa_01s06e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Korolj_Kvinsa_01s06e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [10]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [10]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=10
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([sS]{1}\.[\d+]{1}).*([\d+]{2})",
			re.I,
		)  # [('The.King.of.Queens.', 's.6', '01')] # length=3 # debug/test
		# temp = "7f_The.King.of.Queens.s.6.01.DougLessPart1[Ezekiel2517].a1.21.12.12.mp4"  # 11

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('The.King.of.Queens.', 's.6', '01')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['The.King.of.Queens.', 's.6', '01'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = (
					"".join(
						["0", filelearn[-2].split(".")[-1], filelearn[-2].split(".")[0]]
					)
					if len(filelearn[-2].split(".")[-1]) == 1
					else "".join(
						[filelearn[-2].split(".")[-1], filelearn[-2].split(".")[0]]
					)
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(filelearn[-1]) == 1
					else "".join([filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 06s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# The_King_of_Queens_06s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # The_King_of_Queens_06s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # The_King_of_Queens_06s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [11]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [11]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=11
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([\d+]{2})\-([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})", re.I
		)  # [('01', 'Vlast.v.nochnom.gorode.', 's05')] # length=3
		# temp = "7f_01-Vlast.v.nochnom.gorode.s05-2018.720p.WEB-DLRip.AVC-Srg6161.a1.24.09.18.mp4"  # 12

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('01', 'Vlast.v.nochnom.gorode.', 's05')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['01', 'Vlast.v.nochnom.gorode.', 's05'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					filelearn[-1][0].lower() == "s",
					"".join(filelearn[-1][1:]).isnumeric(),
					"".join(filelearn[0][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]])
				epis = "".join([filelearn[0], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 05s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Vlast_v_nochnom_gorode_05s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Vlast_v_nochnom_gorode_05s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Vlast_v_nochnom_gorode_05s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [12]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [12]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=12
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[sS]{1}([\d+]{2})[x]([\d+]{2})", re.I
		)  # [('Bridzhertony', '02', '01')] # length=3
		# temp = "7f_BridzhertonyS02x01.a1.29.03.22.mp4"  # 13

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Bridzhertony', '02', '01')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Bridzhertony', '02', '01']
		filelearn.insert(
			1, "."
		)  # ; print("Split data(# 2): %s" % str(filelearn)) # ['Bridzhertony', '.', '02', '01'] # len(filelearn) >= 4

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 4,
				)
			):
				seas = "".join(["".join(filelearn[-2][0:]), "s"])
				epis = "".join(["".join(filelearn[-1][0:]), "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 02s01e

		if all((swap_seasepis, len(filelearn) >= 4)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Bridzhertony_02s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Bridzhertony_02s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Bridzhertony_02s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [13]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [13]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=13
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})", re.I
		)  # [('InTheDark', 'S02', 'E01')] # length=3
		# temp = "7f_InTheDarkS02E01.a1.25.06.21.mp4"  # 14

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('InTheDark', 'S02', 'E01')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['InTheDark', 'S02', 'E01']
		filelearn.insert(
			1, "."
		)  # ; print("Split data(# 2): %s" % str(filelearn)) # ['InTheDark', '.', 'S02', 'E01'] # len(filelearn) >= 4

		try:
			if all(
				(
					filelearn[-2][0].lower() == "s",
					"".join(filelearn[-2][1:]).isnumeric(),
					len(filelearn) >= 4,
				)
			):
				if all(
					(
						filelearn[-1][0].lower() == "e",
						"".join(filelearn[-1][1:]).isnumeric(),
					)
				):
					seas = "".join(
						["".join(filelearn[-2][1:]), filelearn[-2][0]]
					).lower()
					epis = "".join(
						["".join(filelearn[-1][1:]), filelearn[-1][0]]
					).lower()

		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 02s01e

		if all((swap_seasepis, len(filelearn) >= 4)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# InTheDark_02s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # InTheDark_02s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # InTheDark_02s01e.mp4 # debug/test

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [14]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [14]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=14
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})\.sezon\.([\d+]{2})\.seria", re.I
		)  # [('Bratja.po.oruzhiju.', '1', '04')] # length=3
		# temp = "7f_Bratja.po.oruzhiju.1.sezon.04.seria.iz.10.2001.x264.BDRip.720p.MediaClub.a6.02.08.20.mp4"  # 15

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Bratja.po.oruzhiju.', '1', '04')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Bratja.po.oruzhiju.', '1', '04'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2], "s"])
					if len(filelearn[-2]) == 1
					else "".join([filelearn[-2], "s"])
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(filelearn[-1]) == 1
					else "".join([filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s04e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Bratja_po_oruzhiju_01s04e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Bratja_po_oruzhiju_01s04e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Bratja_po_oruzhiju_01s04e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [15]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [15]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=15
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# check_for_rus

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,})-([\d+]{3}).*", re.I
		)
		# temp = "7f_Bleach-001.a1.10.07.12.mp4"  # ([\w+\.]{1,}\.)-([\d+]{3}.*) # 16

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Bleach', '001')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Bleach', '001'] # len(filelearn) >= 2

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][0:]).isnumeric(), len(filelearn) >= 2)):
				seas = "01s"
				epis = (
					"".join([filelearn[-1], "e"])
					if len(filelearn[-1]) in [2, 3]
					else "".join(["0", filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s001e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis

			# Bleach_01s001e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Nu-ka_vse_vmeste_04s01e # Bleach_01s001e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Bleach_01s001e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [16]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [16]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			# parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath
			# print(Style.BRIGHT + Fore.YELLOW + "%s [16]" % filename); write_log("debug parse_autorename[16]", f"{filename}") # debug(is_color)

			temp2 = parse_autorename(filename, ff_last=ff_last, ind=16)
			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.Vypusk-([\d+]{2})", re.I
		)  # [('Nu-ka.vse.vmeste.', '4', '01')] # length=3
		# temp="7f_Nu-ka.vse.vmeste.4.sezon.Vypusk-01.ot.2022.09.02.a1.06.09.22.mp4"  # ([\w+\.\-]{1,})\.([\d+]{1})\.sezon\.Vypusk-([\d+]{2}).* # 17

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Nu-ka.vse.vmeste.', '4', '01')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Nu-ka.vse.vmeste.', '4', '01'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2].split(".")[0], "s"])
					if len(filelearn[-2].split(".")[0]) == 1
					else "".join([filelearn[-2].split(".")[0], "s"])
				)
				epis = (
					"".join(["0", filelearn[-1].split(".")[0], "e"])
					if len(filelearn[-1].split(".")[0]) == 1
					else "".join([filelearn[-1].split(".")[0], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 04s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Nu-ka_vse_vmeste_04s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Nu-ka_vse_vmeste_04s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Nu-ka_vse_vmeste_04s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [17]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [17]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			# parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath
			# print(Style.BRIGHT + Fore.YELLOW + "%s [17]" % filename); write_log("debug parse_autorename[17]", f"{filename}") # debug(is_color)

			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=17
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[\.]{1,}([\d+]{1})\.s-n\.([\d+]{1,2})\.s",
			re.I,
		)  # [('Voyna.mirov.', '1', '1')]
		# temp="7f_Voyna.mirov..1.s-n.1.s..-.[FOX].a1.19.11.19.mp4"  # season/series # 18

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Voyna.mirov.', '1', '1')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Voyna.mirov.', '1', '1'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2], "s"])
					if len(filelearn[-2]) == 1
					else "".join([filelearn[-2], "s"])
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(filelearn[-1]) == 1
					else "".join([filelearn[-1], "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e

		# Voyna_mirov_01s01e # addition_logic
		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Voyna_mirov_01s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Voyna_mirov_01s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Voyna_mirov_01s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [18]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [18]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=18
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# check_for_rus

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([eE]{1}[\d+]{2})",
			re.I,
		)  # [('Sobor.', 'E04')] # \. -> .* # debug/test
		# temp="7f_Sobor.E04.2021.WEB-DL.720p.a1.23.12.21.mp4"
		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Sobor.', 'E04')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Sobor.', 'E04']

		seas = epis = ""

		try:
			if all(
				(
					filelearn[-1][0].lower() == "e",
					"".join(filelearn[-1][1:]).isnumeric(),
					len(filelearn) >= 2,
				)
			):
				seas = "01s"
				epis = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s04e

		# Sobor_01s04e # addition_logic
		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis

			# Sobor_01s04e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Sobor_01s04e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Sobor_01s04e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [19]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [19]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=19
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# debug(7f_Himera.s01.e01.WEB-DLRip.25Kuzmich.a1.15.09.22.mp4 -> "Himera_s01_01s01e.mp4"/Himera_01s01e.mp4)/test

	# debug/test # "rus"/eng_filenames_template

	# 7f_Staya.S01.E06.2022.WEB-DL.1080p.a1.14.10.22.mp4 # 23(20)
	# 7f_Avenue.5.S02.E01.2022.WEB-DL.1080p.ExKinoRay.a1.11.10.22.mp4 # 23(20)
	# 7f_Hudozhnik.s01.e13.WEB-DL.1080.25Kuzmich.a1.18.10.22.mp4 # 23(20)
	# 7f_Nina.s01.e09.XviD.SATRip.25Kuzmich.a1.13.10.22.mp4 # 23(20)
	# 7f_Zhizn.po.vyzovu.S01.E07.2022.WEBRip.1080p.a1.29.09.22.mp4 # 20
	# 7f_Himera.s01.e01.WEB-DLRip.25Kuzmich.a1.15.09.22.mp4 # 20
	# 7f_Klassnaya.Katya.S01.E17.2022.WEB-DL.1080p.a1.03.10.22.mp4 # 20

	# '''
	is_need_change, swap_seasepis = False, ""  # --- 20(is_rus_include) ---

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([sS]{1}[\d+]{2})\.([eE]{1}[\d+]{2})",
			re.I,
		)  # [('Zhizn.po.vyzovu.', 'S01', 'E07')] # debug/test
		# temp="7f_Zhizn.po.vyzovu.S01.E07.2022.WEBRip.1080p.a1.29.09.22.mp4"

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Zhizn.po.vyzovu.', 'S01', 'E07')] # [('Himera.', 's01', 'e01')] # [('Staya.', 'S01', 'E06')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Zhizn.po.vyzovu.', 'S01', 'E07'] # ['Himera.', 's01', 'e01'] # ['Staya.', 'S01', 'E06']

		# seas = epis = ""  # hide_if_try_except_no_logic # debug/test

		try:
			if all(
				(
					filelearn[-1][0].lower() == "e",
					"".join(filelearn[-1][1:]).isnumeric(),
					filelearn[-2][0].lower() == "s",
					"".join(filelearn[-2][1:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]]).lower()
				epis = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s07e # 01s01e # 01s06e

		# Zhizn_po_vyzovu_01s07e # Himera_01s01e # addition_logic
		if all((swap_seasepis, len(filelearn) >= 3)):  # length=4 ~> length=3
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Zhizn_po_vyzovu_01s07e # Himera_01s01e # Staya_01s06e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Zhizn_po_vyzovu_01s07e # Himera_01s01e # Staya_01s06e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Zhizn_po_vyzovu_01s07e.mp4 # Himera_01s01e.mp4 # Staya_01s06e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [20]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [20]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=20
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2
	# '''

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*(S[1,2])\.ep([\d+]{1,2})", re.I
		)  # [('Ice.Age.Scrat.Tales.TVShows.', 'S1', 'ep1')]
		# temp="7f_Ice.Age.Scrat.Tales.TVShows.S1.ep1.a1.08.10.22.mp4"

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Ice.Age.Scrat.Tales.TVShows.', 'S1', '1')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Ice.Age.Scrat.Tales.TVShows.', 'S1', '1']

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-1][0:]).isnumeric(),
					filelearn[-2][0].lower() == "s",
					"".join(filelearn[-2][1:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", filelearn[-2][1], filelearn[-2][0]])
					if len(filelearn[-2]) == 2
					else "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]])
				)
				epis = (
					"".join(["0", filelearn[-1], "e"])
					if len(filelearn[-1]) == 1
					else "".join(["".join(filelearn[-1][0:]), "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Ice_Age_Scrat_Tales_TVShows_01s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Ice_Age_Scrat_Tales_TVShows_01s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Ice_Age_Scrat_Tales_TVShows_01s01e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [21]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [21]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=21
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([\d+]{1,2})[\.]{1,}(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*[\d+]{4}",
			re.I,
		)  # [('01', 'Avatar.')]
		# temp="7f_01..Avatar.2022.WEB-DL.720p.Files-x.a1.12.09.22.mp4"

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('01', 'Avatar.')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['01', 'Avatar.']

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[0][0:]).isnumeric(),
					len(filelearn[0]) in range(1, 3),
					len(filelearn) >= 2,
				)
			):
				seas = "01s"  # debug/is_skip(season)
				epis = (
					"".join(["0", "".join(filelearn[0][0:]), "e"])
					if len(filelearn[0]) == 1
					else "".join(["".join(filelearn[0][0:]), "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis

			# Avatar_01s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Avatar_01s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Avatar_01s01e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [22]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [22]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=22
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# with_soundtrack(unique)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(\[.*\]).*\.(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,}))\.([\d+]{1,2})\.\-\.([\d+]{1,2})",
			re.I,
		)  # [('[AniMaunt]', 'Duncanville', '3', '01')]
		# temp="7f_[AniMaunt].Duncanville.3.-.01.a1.22.10.22.mp4"

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('[AniMaunt]', 'Duncanville', '3', '01')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['[AniMaunt]', 'Duncanville', '3', '01']

		# clean_soundtrack_from_0_value(unique)
		if filelearn[0][0].startswith("["):
			filelearn.remove(filelearn[0])

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[-2][0:]).isnumeric(),
					"".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0" + "".join(filelearn[-2][0:]) + "s"])
					if len(filelearn[-2]) == 1
					else "".join(["".join(filelearn[-2][0:]) + "s"])
				)
				epis = (
					"".join(["0" + "".join(filelearn[-1][0:]) + "e"])
					if len(filelearn[-1]) == 1
					else "".join(["".join(filelearn[-1][0:]) + "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 03s01e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Duncanville_03s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Duncanville_03s01e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Duncanville_03s01e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [23]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [23]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=23
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([\d+]{1,2})\.sezon\.([\d+]{1,2})\.seriya",
			re.I,
		)
		# temp="7f_Zhizn.1.sezon.01.seriya.iz.11.2007.XviD.DVDRip.a1.23.11.12.mp4"
		# temp="7f_Myslit.kak.prestupnik.7.sezon.22.seriya.iz.24.2011.x264.WEB-DL.720pFOX.CRIME.a1.07.05.15.mp4"

		tags = seasonvar_regex.findall(
			temp
		)  # ; print("Tags: %s" % str(tags)) # [('Zhizn.', '1', '01')] # [('Myslit.kak.prestupnik.', '7', '22')]
		# [t for t in tags] # debug/test
		filelearn = [
			w.strip() for t in tags for w in t if w
		]  # ; print("Split data: %s" % str(filelearn)) # ['Zhizn.', '1', '01'] # ['Myslit.kak.prestupnik.', '7', '22']

		seas = epis = ""

		try:
			if all(
				(
					"".join(filelearn[1][0:]).isnumeric(),
					"".join(filelearn[2][0:]).isnumeric(),
					len(filelearn) >= 3,
				)
			):
				seas = (
					"".join(["0", "".join(filelearn[1][0:]), "s"])
					if len("".join(filelearn[1][0:])) == 1
					else "".join(["".join(filelearn[1][0:]), "s"])
				)
				epis = (
					"".join(["0", "".join(filelearn[2][0:]), "e"])
					if len("".join(filelearn[2][0:])) == 1
					else "".join(["".join(filelearn[2][0:]), "e"])
				)
		except:
			seas = epis = ""
		finally:
			swap_seasepis = (
				"".join([seas, epis]).lower() if all((seas, epis)) else ""
			)  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e # 07s22e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Zhizn_01s01e # Myslit_kak_prestupnik_07s22e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(
					".", "_"
				)  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:]
			)  # ; print("Filename: %s" % str(filename)) # Zhizn_01s01e # Myslit_kak_prestupnik_07s22e
			filename += "".join(
				[".", temp.split(".")[-1].lower()]
			)  # ; print("Filename: %s" % str(filename)) # Zhizn_01s01e.mp4 # Myslit_kak_prestupnik_07s22e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "Не могу перевести в обычный вид файл %s [%s] [24]"
				% (copyfile, str(e))
			)
			write_log(
				"debug parse[error]",
				"Не могу перевести в обычный вид файл %s [%s] [24]"
				% (copyfile, str(e)),
				is_error=True,
			)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(
				filename, ff_last=ff_last, ind=24
			)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	write_log(
		"debug end[seasonvar_parse][unknown]",
		"%s [%s]" % (filename, str(datetime.now())),
	)

	# exit() # exit_if_unkown_parse/debug

	return None  # if_not_found_template(None)


def okay_parse(filename, is_log: bool = True):  # convert_parsefile_to_normal_file #1
	return None  # pass


# @optimial_time_for_jobs_by_xml(load)
async def load_timing_from_xml(
	ind: int = 0,
) -> tuple:  # load_last_time # list -> tuple # debug(is_async) #20
	timing = []

	try:
		tree = xml.parse(
			files_base["timing"]
		)  # tree = xml.parse(file=files_base["timing"]) # is_error

		root = tree.getroot()

		for elem in root.iter(
			tag="time"
		):  # <timing><time><hh>1</hh><mm>46</mm></time></timing>
			tim = {}

			for subelem in elem:
				tim[subelem.tag] = subelem.text

			timing.append(tim)
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "Xml load error (time)")
		write_log(
			"debug timing[xml][loaderror][%d]" % ind,
			"Xml load error (time) %s [%s]" % (str(e), str(datetime.now())),
			is_error=True,
		)  # main_xml_error
		return (0, 0)  # error

	if timing:  # logging_if_some_data # ... Xml loaded # dict's_to_list
		print(
			Style.BRIGHT + Fore.WHITE + "%s" % str(timing),
			Style.BRIGHT + Fore.GREEN + "Xml loaded",
		)
		write_log(
			"debug timing[xml][load][%d]" % ind, "load ok [%s]" % str(datetime.now())
		)  # xml_loaded

		hours, minutes = int(timing[0]["hh"]), int(timing[0]["mm"])

		if hours > 24:
			hours %= 24

		if minutes > 60:
			minutes %= 60

		try:
			assert hours or minutes, ""  # is_assert_debug
		except AssertionError as err:  # if_null
			hours, minutes = 3, 30  # +1 hour
			raise err  # logging
		except BaseException:  # if_error
			hours, minutes = 3, 30  # +1 hour

		# return (int(timing[0]["hh"]), int(timing[0]["mm"])) # [{'hh': '1', 'mm': '56'}] # true_calc # old
		return (hours, minutes)  # debug # [{'hh': '1', 'mm': '56'}] # true_calc
	elif not timing:
		return (0, 0)  # ok_but_null


# @log_error # get_time_if_have_ready_jobs_else_null_time
async def save_timing_to_xml(hours: int = 0, minutes: int = 0):  # 3

	if hours > 24:
		hours = hours % 24  # debug # if_more_24hour_find_mod

	if minutes > 60:
		minutes = minutes % 60  # debug # if_more_60minute_find_mod

	try:
		assert hours or minutes, ""  # is_assert_debug
	except AssertionError:  # if_null
		hours, minutes = 3, 30  # +1 hour
		# raise err # logging
	except BaseException:  # if_error
		hours, minutes = 3, 30  # +1 hour

	# timing = [{"hh": hh_time, "mm": mm_time}] # one_record
	timing = [{"hh": int(hours), "mm": int(minutes)}]  # one_record

	# xml_root_name
	root = xml.Element("timing")

	try:
		# xml_fields
		for tim in timing:
			child = xml.Element("time")
			root.append(child)
			hh = xml.SubElement(child, "hh")
			hh.text = str(tim.get("hh"))
			mm = xml.SubElement(child, "mm")
			mm.text = str(tim.get("mm"))

		# put_root_and_data_to_tree
		tree = xml.ElementTree(root)
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "Xml save error (time)")
		write_log(
			"debug timing[xml][saveerror]",
			"Xml save error (time) %s [%s]" % (str(e), str(datetime.now())),
			is_error=True,
		)  # main_xml_error
	else:
		try:
			# save_xml
			with open(
				files_base["timing"], "wb"
			) as vrf:  # "".join([script_path, '\\video_resize.xml'])
				tree.write(vrf)

		except BaseException as e:
			print(Style.BRIGHT + Fore.RED + "Xml save error (time)")
			write_log(
				"debug timing[saveerror]",
				"Xml save error (time) %s [%s]" % (str(e), str(datetime.now())),
				is_error=True,
			)  # some_error_in_save
		else:
			print(Style.BRIGHT + Fore.GREEN + "Xml saved")
			write_log(
				"debug timing[xml][save]", "save ok [%s]" % str(datetime.now())
			)  # xml_saved

		# clear_xml(logic)
		"""
		for country in root.findall('country'):
			# using root.findall() to avoid removal during traversal
			rank = int(country.find('rank').text)
			if rank > 50:
				root.remove(country)

		tree.write('output.xml')
		"""


# update_is_ready_project # pass_x_of_4
# @log_error
async def project_done(
	path_to_done: str = path_to_done, is_debug: bool = False, is_learn: bool = False
):  # 28

	write_log("debug start[project_done]", "%s" % str(datetime.now()))

	# return

	# move_last_files(if_have) # date_of_change(modify)_files # last_files

	# file_time = {} # time_to_delete(min/max)_time

	# load_meta_base(filter) #2
	try:
		with open(some_base, encoding="utf-8") as sbf:
			somebase_dict = json.load(sbf)
	except:
		somebase_dict = {}

		with open(some_base, "w", encoding="utf-8") as sbf:
			json.dump(somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True)

	# filter_current_jobs(is_update)

	# @load_current_jobs
	try:
		with open(filecmd_base, encoding="utf-8") as fbf:
			fcmd = json.load(fbf)
	except:
		fcmd = {}

		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump(fcmd, fbf, ensure_ascii=False, indent=4, sort_keys=False)

	first_len = second_len = 0

	# filter_current_jobs_(in_meta/no_in_meta/only_exists)
	try:
		first_len: int = len(fcmd)
		fcmd = {
			k: v
			for k, v in fcmd.items()
			if os.path.exists(k)
			and any((k.strip() in [*somebase_dict], not [*somebase_dict]))
		}
	except:
		fcmd = {k: v for k, v in fcmd.items() if os.path.exists(k)}
	finally:
		second_len: int = len(fcmd)

	if (
		fcmd
	):  # filter_current_and_not_optimize_jobs # second_len <= first_len # all -> any
		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump(fcmd, fbf, ensure_ascii=False, indent=4, sort_keys=False)

		write_log("debug fcmd[filter]", "%d" % len(fcmd))
	# @load_known_files
	try:
		with open(vr_files, encoding="utf-8") as vff:
			ff_last = json.load(vff)
	except:
		ff_last = {}

	# min_time = max_time = 0 # time_by_hour
	datelist: list = []
	proj_files: list = []

	fcmd_filter: list = []
	proj_filter: list = []
	known_filter: list = []
	proj_and_fcmd_filter: dict = {}

	# original_for_check # pass_1_of_2
	try:
		proj_list = os.listdir(path_to_done)
	except:
		proj_list = []

	try:
		if proj_list:
			proj_files: list = list(
				set(
					[
						"".join([path_to_done, pl])
						for pl in proj_list
						if os.path.exists("".join([path_to_done, pl]))
						and video_ext_regex.findall(pl)
						and all(
							(
								pl.count(".") == 1,
								not pl.split(".")[-1].lower()
								in [
									"dmf",
									"dmfr",
									"filepart",
									"aria2",
									"crdownload",
									"crswap",
								],
							)
						)
					]
				)
			)  # only_normal(files_by_tempate)
	except BaseException as e:
		proj_files: list = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
		write_log("debug proj_files[error]", "%s" % str(e), is_error=True)
	else:
		# need_clear_after_midnight(from_disk)
		if proj_files:
			print(
				Style.BRIGHT
				+ Fore.WHITE
				+ "Последние обновления %d штук(и) [%s]"
				% (len(proj_files), str(datetime.now()))
			)
		write_log(
			"debug updates[yes]",
			"Последние обновления %d штук(и) [%s]"
			% (len(proj_files), str(datetime.now())),
		)

		proj_files.sort(reverse=False)  # sort_by_string
		# proj_files.sort(key=len, reverse=False) # sort_by_length

		# @video_resize.lst

		try:
			# tmp = list(pf_gen()) # new(yes_gen)
			tmp: list = list(
				set(
					[
						pf.strip()
						for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))
						if pf
					]
				)
			)
		except:
			tmp: list = []
		finally:
			tmp.sort(reverse=False)  # sort_by_string
			# tmp.sort(key=len, reverse=False) # sort_by_length

		proj_files = tmp if tmp else []

		cnt: int = 0

		cnt += len(fcmd)
		cnt += len(proj_files)

		MySt = MyString()

		# Надо проверить 22 задач / и 0 "готовых" файл(а,ов) # Надо проверить 270 задач и 0 файлов

		if cnt:
			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ MySt.last2str(
					maintxt="Надо проверить", endtxt="", count=len(fcmd), kw="задач"
				),
				Style.BRIGHT
				+ Fore.CYAN
				+ MySt.last2str(
					maintxt="и", endtxt="", count=len(proj_files), kw="файл"
				),
			)
			write_log(
				"debug jobs[ready][count]",
				"Надо проверить %d задач и %d готовых файлов"
				% (len(fcmd), len(proj_files)),
			)
		elif not cnt:
			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ "Нет задач или готовых файлов для проверки [%s]" % str(datetime.now())
			)
			write_log(
				"debug jobs[ready][null]",
				"Нет задач или готовых файлов для проверки [%s]" % str(datetime.now()),
			)

		# del MySt # clear_mem # debug

	MM = MyMeta()  # 1

	for pf in filter(lambda x: x, tuple(proj_files)):

		try:
			gl = MM.get_length(pf)
		except:
			gl = 0
		else:
			proj_filter.append((pf.strip(), gl))

	proj_filter_status = (
		"Готовые файлы успешно отфильтрованы и добавлены [%d]" % len(proj_filter)
		if len(proj_files) == len(proj_filter)
		else "Какой-то файл не отфильтровался или не добавился [%d]"
		% abs(len(proj_filter) - len(proj_filter))
	)  # is_no_lambda

	write_log("debug proj_filter_status", "%s" % proj_filter_status)

	for k, _ in fcmd.items():

		try:
			assert (
				fcmd
			), "Пустой словарь или нет задач @project_done/fcmd"  # is_assert_debug
		except AssertionError as err:  # if_null
			logging.warning(
				"Пустой словарь или нет задач @project_done/fcmd [%s]"
				% str(datetime.now())
			)
			raise err
			break
		except BaseException as e:  # if_error
			logging.error(
				"Пустой словарь или нет задач @project_done/fcmd [%s] [%s]"
				% (str(e), str(datetime.now()))
			)
			break

		try:
			gl = MM.get_length(k)
		except:
			gl = 0
		else:
			fcmd_filter.append((k.strip(), gl))

	fcmd_filter_status = (
		"Задачи успешно отфильтрованы и добавлены [%d]" % len(fcmd_filter)
		if len(fcmd) == len(fcmd_filter)
		else "Какая-то задача не отфильтровалась или не добавилась [%d]"
		% abs(len(fcmd) - len(fcmd_filter))
	)  # is_no_lambda

	write_log("debug fcmd_filter_status", "%s" % fcmd_filter_status)

	if all((proj_filter, fcmd_filter)):  # ready_jobs / current_jobs # pass_1_of_2
		try:
			proj_and_fcmd_filter = {
				pf[0].strip(): ff[0].strip()
				for pf in proj_filter
				for ff in fcmd_filter
				if all(
					(
						pf[0].split("\\")[-1] == ff[0].split("\\")[-1],
						pf[1] == ff[1],
						pf[0] != ff[0],
					)
				)
			}
		except BaseException as e:
			proj_and_fcmd_filter = {}

			write_log("debug proj_and_fcmd_filter[error]", "%s" % str(e))
		else:
			if len(proj_filter) != len(fcmd_filter):
				write_log(
					"debug diff[proj_filter][fcmd_filter]",
					"Фильтры для обновления или записи разные, %s"
					% "/".join([str(len(proj_filter)), str(len(fcmd_filter))]),
				)  # 1/2
			elif len(proj_filter) == len(fcmd_filter):
				write_log(
					"debug ok[proj_filter][fcmd_filter]",
					"Фильтры для обновления или записи совпадают",
				)

	elif all((proj_filter, not fcmd_filter)):  # ready_jobs / no_current_jobs
		cjob_set = set()

		for pf in proj_filter:
			for k, _ in ff_last.items():

				if (
					os.path.exists(k)
					and all((pf[0].split("\\")[-1] == k.split("\\")[-1], pf[0] != k))
					and not k in cjob_set
				):  # equal_filename

					cjob_set.add(k)

					try:
						ff_last_length = MM.get_length(
							k
						)  # last_length_from_known_files
					except:
						ff_last_length = 0

					if all(
						(pf[1], ff_last_length, pf[1] == ff_last_length)
					):  # equal_length
						known_filter.append((k.strip(), ff_last_length))

	if known_filter:  # known_jobs
		fcmd_filter = known_filter

	if all(
		(proj_filter, fcmd_filter, known_filter)
	):  # ready_jobs / current_jobs / known_jobs # pass_2_of_2

		proj_filter = [
			pf.strip()
			for pf in filter(lambda x: x.endswith("mp4"), tuple(proj_filter))
			if os.path.exists(pf)
		]

		try:
			await redate_files(lst=proj_filter)
		except:
			pass

		try:
			proj_and_fcmd_filter = {
				pf[0].strip(): ff[0].strip()
				for pf in proj_filter
				for ff in fcmd_filter
				if all(
					(
						pf[0].split("\\")[-1] == ff[0].split("\\")[-1],
						pf[1] == ff[1],
						pf[0] != ff[0],
					)
				)
			}
		except BaseException as e:
			proj_and_fcmd_filter = {}

			write_log("debug proj_and_fcmd_filter[error][2]", "%s" % str(e))

	if proj_and_fcmd_filter:
		for k, v in proj_and_fcmd_filter.items():

			if os.path.exists(k):  # is_assert_debug
				print(
					Style.BRIGHT + Fore.CYAN + "Подготовка обработки файла",
					Style.BRIGHT + Fore.YELLOW + "%s" % k,
					Style.BRIGHT + Fore.CYAN + "добавление или обновление файла",
					Style.BRIGHT + Fore.YELLOW + "%s" % full_to_short(v),
				)

				move(k, v)  # no_async_if_"big"

				write_log("debug proj_and_fcmd_filter[move]", "-=>".join([k, v]))

	fcmd_hours: list = []
	fcmd_minutes: list = []

	if fcmd_filter:
		fcmd_hours = [ff[1] % 3600 for ff in fcmd_filter if ff[1] % 3600 > 0]
		fcmd_minutes = [
			(ff[1] // 60) % 60 for ff in fcmd_filter if (ff[1] // 60) % 60 > 0
		]

		hh_time: int = 0
		hh_avg_time: int = 0
		mm_time: int = 0
		mm_avg_time: int = 0

		# @avg_hour / @max_hour
		try:
			fcmd_hours_sum = sum(fcmd_hours)
			fcmd_hours_len = len(fcmd_hours)
			fcmd_hours_avg = (lambda fhs, fhl: fhs / fhl)(
				fcmd_hours_sum, fcmd_hours_len
			)
		except:
			fcmd_hours_avg = 0
		else:
			# hh_time = max(fcmd_hours) if max(fcmd_hours) > fcmd_hours_avg else fcmd_hours_avg # pass_1_of_2
			# hh_time = int(3600 // hh_time) if max(fcmd_hours) < 3600 else int(hh_time // 3600) # pass_2_of_2
			hh_time = (
				int(3600 // fcmd_hours_avg)
				if fcmd_hours_avg < 3600
				else int(fcmd_hours_avg // 3600)
			)  # avg_without_max # is_no_lambda

			hh_avg_time = hh_time  # is_debug

			print("Оптимально время для обработки в часах %d часов(а)" % hh_avg_time)
			write_log(
				"debug fcmd_hours_avg[jobtime]",
				"Оптимально время для обработки в часах %d часов(а)" % hh_avg_time,
			)  # hh

		# @avg_minute / @max_minute

		try:
			fcmd_minutes_sum = sum(fcmd_minutes)
			fcmd_minutes_len = len(fcmd_minutes)
			fcmd_minutes_avg = (lambda fms, fml: fms / fml)(
				fcmd_minutes_sum, fcmd_minutes_len
			)
		except:
			fcmd_minutes_avg = 0
		else:
			# mm_time = max(fcmd_minutes) if max(fcmd_minutes) > fcmd_minutes_avg else fcmd_minutes_avg
			mm_time = fcmd_minutes_avg  # avg_without_max
			mm_avg_time = mm_time

			print("Оптимально время для обработки в минутах %d минут(ы)" % mm_avg_time)
			write_log(
				"debug fcmd_minutes_avg[jobtime]",
				"Оптимально время для обработки в минутах %d минут(ы)" % mm_avg_time,
			)  # mm

		# @optimial_time_for_jobs_by_xml(save) # dict's_in_list # debug(xml)

		await save_timing_to_xml(
			hours=hh_time, minutes=mm_time
		)  # optimize_by_current_projects(is_ready)

		try:
			h, m = await load_timing_from_xml(
				ind=1
			)  # {'hh': '1', 'mm': '56'} # values(str) -> values(int) # 1 # is_hide
		except:
			h, m = 0, 0

		job_timing_status = (
			"Время обработки задания загружено"
			if all((h, m))
			else "Ошибка загрузки времени обработки задания"
		)  # is_no_lambda

		if job_timing_status.startswith("Время"):
			print(Style.BRIGHT + Fore.WHITE + "%s" % job_timing_status)
		elif job_timing_status.startswith("Ошибка"):
			print(Style.BRIGHT + Fore.RED + "%s" % job_timing_status)

		write_log(
			"debug job_timing_status",
			"%s [%s]" % (job_timing_status, str(datetime.now())),
		)

	for pf in filter(lambda x: os.path.exists(x), tuple(proj_files)):  # new(yes_gen)

		try:
			fp, fn = split_filename(pf)
		except:
			fn = pf.split("\\")[-1].strip()  # fp

		try:
			fname = fn
		except:
			fname = ""
			continue

		gl, last_file = 0, ""

		try:
			with open(vr_files, encoding="utf-8") as vff:
				ff_last = json.load(vff)
		except:
			ff_last = {}

		if ff_last:

			try:
				# dub_list = list(dub_list_gen()) # new(yes_gen)
				dub_list: list = [
					t.strip()
					for t in filter(
						lambda x: x.split("\\")[-1] == fname, tuple(ff_last)
					)
					if t
				]
			except:
				dub_list: list = []
			finally:
				dub_list.sort(reverse=False)

				# dub_list = sorted(tmp, reverse=False) # sort_by_string
				# dub_list = sorted(tmp, key=len, reverse=False) # sort_by_length

			len_file_list: list = []

			if len(dub_list) > 1:  # show_more_one
				print(
					Style.BRIGHT
					+ Fore.GREEN
					+ "Найдено несколько файлов с именем %s" % pf
				)
				len_file_list = [
					{"file": dl, "length": MM.get_length(dl)}
					for dl in filter(lambda x: os.path.exists(x), tuple(dub_list))
					if dl
				]
			# elif len(dub_list) == 1:  # hide_one
			# print(Style.BRIGHT + Fore.CYAN + "Найдено один файл с именем %s" % fname)
			# len_file_list = [{"file": dl, "length": MM.get_length(dl)} for dl in filter(lambda x: os.path.exists(x), tuple(dub_list)) if dl]

			if len_file_list:
				for lfl in len_file_list:
					print(
						lfl["file"], hms(lfl["length"]), end="\n"
					)  # logging(filenames/lengths_to_time)

			funique = set()
			try:
				# tmp = list(ff_gen()) # new(yes_gen)
				tmp: list = list(
					set(
						[
							ff.strip()
							for ff in filter(
								lambda x: os.path.exists(x), tuple(ff_last)
							)
							if ff
						]
					)
				)
			except:
				tmp: list = []
			finally:
				tmp.sort(reverse=False)  # sort_by_string
				# tmp.sort(key=len, reverse=False) # sort_by_length

			ff_last = tmp if tmp else []  # sorted/sort

			for ff in tuple(ff_last):

				try:
					assert ff_last, ""  # is_assert_debug
				except AssertionError as err:
					raise err  # logging
					break
				except BaseException:
					break

				try:
					fp, fn = split_filename(ff)
				except:
					fn = ff.split("\\")[-1].strip()  # fp

				try:
					fname = fn
				except:
					fname = ""
					continue
				else:
					if not fname in funique:
						funique.add(fname)

				# (mp4=mp4;any!=mp4)
				if ff.split("\\")[-1] == pf.split("\\")[-1] or all(
					(
						ff.split("\\")[-1].split(".")[0]
						== pf.split("\\")[-1].split(".")[0],
						ff.split(".")[-1] != pf.split(".")[-1],
					)
				):  # (mp4=mp4;any!=mp4)

					try:
						gl = MM.get_length(ff)
					except BaseException as e:
						gl = 0  # if_no_length
						print(
							Style.BRIGHT
							+ Fore.RED
							+ "Ошибка длина файла %s [%s]" % (pf, str(e))
						)
						write_log(
							"debug file[length][error][0]",
							"Ошибка длина файла %s [%s]" % (pf, str(e)),
							is_error=True,
						)
					else:
						if gl:
							last_file = ff  # if_some_length
						# break # stop_if_find_one
				# else:
				# continue

			try:
				fp, fn = split_filename(pf)
			except:
				fn = pf.split("\\")[-1].strip()  # fp

			try:
				fname = fn
			except:
				fname = ""
				continue

			try:
				assert (
					last_file
				), f"Нет выбранного файла @project_done/{last_file}"  # is_assert_debug
			except AssertionError:  # if_null
				logging.warning(f"Нет выбранного файла @project_done/{last_file}")
				# raise err
				continue
			except BaseException as e:  # if_error
				logging.error(
					"Нет выбранного файла @project_done/last_file [%s]" % str(e)
				)
				continue

			dt = datetime.now()

			try:
				fdate, status = await datetime_from_file(pf)
			except:
				fdate, status = datetime.now(), False

			# any_day = any((fdate.day <= dt.day, fdate.month <= dt.month, fdate.year <= dt.year))
			some_day = [
				fdate.day <= dt.day,
				fdate.month <= dt.month,
				fdate.year <= dt.year,
			]  # some_day.count(True) > 0

			# is_merge(datalist += datalist2) # filter(day/time)
			if (
				all((some_day.count(True) > 0, fdate.hour <= dt.hour))
				and os.path.exists(pf)
				and all((fname, status))
			):  # skip(minute/second)
				datelist.append(
					{"file": [pf, fdate.hour, gl, last_file]}
				)  # any_(day/month/year)

			elif not status:  # error_date
				continue

		# elif not proj_files:
		# print(Style.BRIGHT + Fore.WHITE + "В данный момент нет обновлений [%s]" % str(datetime.now()))
		# write_log("debug updates[no]", "В данный момент нет обновлений [%s]" % str(datetime.now()))

	# del MM # clear_mem # debug

	if all((proj_files, datelist)):  # need_automatic_clean

		MM = MyMeta()  # 2

		print(
			Style.BRIGHT
			+ Fore.YELLOW
			+ "Ищу временные файлы для переноса и удаления..."
		)
		print("Найдено [%d] файлов для переноса и удаления" % len(datelist))

		fsizes_list: list = []

		skip_file = set()

		with unique_semaphore:
			for dl in datelist:

				try:
					assert (
						datelist
					), f"Пустой список или нет файлов для справнения @project_done/{dl}"  # datelist # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning(
						"Пустой список или нет файлов для сравнения @project_done/datelist [%s]"
						% str(datetime.now())
					)
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой список или нет файлов для сравнения @project_done/datelist [%s] [%s]"
						% (str(e), str(datetime.now()))
					)
					break

				if not os.path.exists(dl["file"][3]):  # is_assert_debug
					continue

				try:
					fname = dl["file"][3].split("\\")[-1].strip()
				except:
					fname = ""
					continue

				try:
					fnshort = fname.split(".")[0].strip()
				except:
					fnshort = ""
				else:
					if any(
						(
							fnshort.count(".") > 1,
							fname.split(".")[-1].lower()
							in [
								"dmf",
								"dmfr",
								"filepart",
								"aria2",
								"crdownload",
								"crswap",
							],
						)
					) and all(
						(fnshort, fname)
					):  # sep_no_ext/temp_ext
						print(
							Style.BRIGHT
							+ Fore.RED
							+ "Файл %s пропущен, т.к. он закачивается" % dl["file"][3]
						)

						write_log(
							"debug skipfile[debug]",
							"Файл %s пропущен, т.к. включен режим отладки"
							% dl["file"][3],
						)

						if not fnshort in skip_file:
							skip_file.add(fnshort)

		try:
			fsizes_list: list = list(
				set(
					[
						os.path.getsize(dl["file"][0])
						for dl in datelist
						if os.path.exists(dl["file"][0])
					]
				)
			)
		except:
			fsizes_list: list = []
		else:
			fsizes_list.sort(reverse=False)

		try:
			avg_size = await avg_lst(list(set(fsizes_list)))  # async(avg_size)
			assert avg_size, ""  # is_assert_debug
		except AssertionError as err:  # if_null
			avg_size = 0
			raise err  # logging
		except BaseException:  # if_error
			try:
				avg_size = (lambda s, l: s / l)(
					sum(fsizes_list), len(fsizes_list)
				)  # by_lambda
			except:
				avg_size = 0

		# clean_project_from_base: list = []

		processes_ram: list = []
		processes_ram2: list = []

		no_list: list = []

		with unique_semaphore:
			for dl in datelist:

				# print(dl["file"], "1", end="\n")

				try:
					assert (
						datelist
					), f"Пустой список или нет файлов для сравнения @project_done/{dl}"  # datelist # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning(
						"Пустой список или нет файлов для сравнения @project_done/datelist [%s]"
						% str(datetime.now())
					)
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой список или нет файлов для сравнения @project_done/datelist [%s] [%s]"
						% (str(e), str(datetime.now()))
					)
					break

				if not os.path.exists(dl["file"][3]):  # is_assert_debug
					continue

				try:
					fullname = dl["file"][0].strip()  # project
				except:
					fullname = ""

				fname = fname2 = ""

				try:
					if fullname:
						fname = fullname.split("\\")[-1]
				except:
					fname = ""
					continue
				else:
					write_log("debug fullname[fname]", "%s" % fname)

				try:
					fullname2 = dl["file"][3].strip()  # original
				except:
					fullname2 = ""

				try:
					if fullname2:
						fname2 = fullname2.split("\\")[-1]
				except:
					fname2 = ""
					continue
				else:
					write_log("debug fullname2[fname2]", "%s" % fname2)

				# try:
				# filetime = dl["file"][1]
				# except:
				# filetime = 999

				gl1: int = 0

				try:
					gl1 = MM.get_length(fullname)  # project
				except BaseException as e:
					gl1 = 0
					print(
						Style.BRIGHT
						+ Fore.RED
						+ "Ошибка длина файла[1] %s [%s]" % (fullname, str(e))
					)
					write_log(
						"debug file[length][error][1]",
						"Ошибка длина файла %s [%s]" % (fullname, str(e)),
						is_error=True,
					)
				else:
					if not isinstance(gl1, int):
						gl1 = int(gl1)

				gl2: int = 0

				try:
					gl2 = MM.get_length(fullname2)  # original # dl["file"][2]
				except BaseException as e:
					gl2 = 0

					print(
						Style.BRIGHT
						+ Fore.RED
						+ "Ошибка длина файла[2] %s [%s]" % (fullname, str(e))
					)
					write_log(
						"debug file[length][error][2]",
						"Ошибка длина файла %s [%s]" % (fullname, str(e)),
						is_error=True,
					)
				else:
					if not isinstance(gl2, int):
						gl2 = int(gl2)

				try:
					if all((gl2 == dl["file"][2], dl["file"][2], gl2)):
						gl2 = dl["file"][2]  # read_from_dict(equal)
				except:
					gl2 = 0

				if not os.path.exists(fullname) or not os.path.exists(fullname2):
					print(
						Style.BRIGHT
						+ Fore.CYAN
						+ "Файл отсутствует [%s] обработки или переноса" % fullname
					)

					write_log(
						"debug file[skip][1]",
						"Файл отсутствует [%s] обработки или переноса" % fullname,
					)

				if all((isinstance(gl1, int), isinstance(gl2, int))) and os.path.exists(
					fullname
				):

					print(
						Style.BRIGHT
						+ Fore.GREEN
						+ "Длина(час:мин): [%s], файл: [%s]" % (hms(gl1), fullname)
					)

					write_log(
						"debug file[lengths]",
						"Длина(час:мин): [%s], файл: [%s]" % (hms(gl1), fullname),
					)

					if all((gl1, gl2)) and os.path.exists(fullname):  # debug/test
						try:
							fsize: int = os.path.getsize(fullname)
							dsize: int = disk_usage(fullname2[0] + ":\\").free
						except:
							fsize: int = 0
							dsize: int = 0
						else:
							if all((fsize, dsize, int(fsize // (dsize / 100)) <= 100)):
								if all(
									(
										fullname.split("\\")[-1]
										== fullname2.split("\\")[-1],
										fullname != fullname2,
									)
								):  # mp4 # skip_any_logic

									try:
										gl1 = MM.get_length(
											fullname
										)  # mp4_file(project)
									except:
										gl1 = 0

									try:
										gl2 = MM.get_length(fullname2)  # job_file(job)
									except:
										gl2 = 0

									try:
										is_new = os.path.exists(
											fullname
										) and not os.path.exists(fullname2)
									except:
										is_new = False

									try:
										is_update = os.path.exists(
											fullname
										) and os.path.exists(fullname2)
									except:
										is_update = False

									is_clean = all(
										(gl1 in range(gl2, gl2 - 10, -1), gl1, gl2)
									)  # tv_series

									if all(
										(is_clean, fullname2[0] >= fullname[0])
									) and os.path.exists(
										fullname
									):  # move_or_update_by_project(by_base)

										print(
											Style.BRIGHT
											+ Fore.WHITE
											+ "Правильная длина файла %s" % fullname
										)
										write_log(
											"debug destonationfile[mp4]",
											"Правильная длина файла %s" % fullname,
										)

										# load_meta_jobs(filter) #3
										try:
											with open(
												some_base, encoding="utf-8"
											) as sbf:
												somebase_dict = json.load(sbf)
										except:
											somebase_dict = {}

											with open(
												some_base, "w", encoding="utf-8"
											) as sbf:
												json.dump(
													somebase_dict,
													sbf,
													ensure_ascii=False,
													indent=4,
													sort_keys=True,
												)

										first_len: int = len(somebase_dict)

										# clean_project_from_base.append(fullname2)

										somebase_dict = {
											k: v
											for k, v in somebase_dict.items()
											if os.path.exists(k)
										}  # exists_only # pass_1_of_2
										somebase_dict = {
											k: v
											for k, v in somebase_dict.items()
											if k != fullname2
										}  # clear_if_ready(delete)  # tv_series(big_cinema) # pass_2_of_2

										# somebase_dict.pop(fullname2)

										second_len: int = len(somebase_dict)

										if (
											somebase_dict
										):  # delete_ready_jobs # second_len <= first_len # all -> any
											with open(
												some_base, "w", encoding="utf-8"
											) as sbf:
												json.dump(
													somebase_dict,
													sbf,
													ensure_ascii=False,
													indent=4,
													sort_keys=True,
												)

											write_log(
												"debug somebase_dict[delete]",
												"%d" % len(somebase_dict),
											)

											print(
												Style.BRIGHT
												+ Fore.GREEN
												+ "Добавление в очередь файла",
												Style.BRIGHT
												+ Fore.WHITE
												+ "%s" % fullname,
											)  # add_to_all(process_move)

										if all(
											(
												os.path.getsize(fullname) <= avg_size,
												avg_size,
											)
										):

											print(
												Style.BRIGHT
												+ Fore.GREEN
												+ "Добавление в очередь файла",
												Style.BRIGHT
												+ Fore.WHITE
												+ "%s" % fullname,
											)  # add_to_all(process_move)

										# @load_current_jobs
										try:
											with open(
												filecmd_base, encoding="utf-8"
											) as fbf:
												fcmd = json.load(fbf)
										except:
											fcmd = {}

											with open(
												filecmd_base, "w", encoding="utf-8"
											) as fbf:
												json.dump(
													fcmd,
													fbf,
													ensure_ascii=False,
													indent=4,
													sort_keys=False,
												)

										first_len = len(fcmd)

										fcmd = {
											k: v
											for k, v in fcmd.items()
											if os.path.exists(k)
											and any(
												(
													k.strip() in [*somebase_dict],
													not [*somebase_dict],
												)
											)
										}

										second_len = len(fcmd)

										if all(
											(fcmd, second_len <= first_len)
										):  # filter_current_and_not_optimize_jobs
											with open(
												filecmd_base, "w", encoding="utf-8"
											) as fbf:
												json.dump(
													fcmd,
													fbf,
													ensure_ascii=False,
													indent=4,
													sort_keys=False,
												)

											write_log(
												"debug fcmd[filter]", "%d" % len(fcmd)
											)

									try:
										await process_move(
											fullname, fullname2, False, True, avg_size
										)  # no_asyncio.run # async_if_small #1
									except BaseException as e:
										write_log(
											"debug process_move[error][1]",
											";".join([fullname, fullname2, str(e)]),
										)
									else:
										write_log(
											"debug process_move[ok][1]",
											";".join([fullname, fullname2]),
										)

									if not fullname in processes_ram:
										processes_ram.append(fullname)

								elif (
									all(
										(os.path.getsize(fullname) > avg_size, avg_size)
									)
									or not avg_size
								):
									move(fullname, fullname2)  # no_async_if_big

									if is_new:
										print(
											Style.BRIGHT + Fore.GREEN + "Файл",
											Style.BRIGHT
											+ Fore.WHITE
											+ "%s" % full_to_short(fullname),
											Style.BRIGHT
											+ Fore.YELLOW
											+ "надо записать в",
											Style.BRIGHT + Fore.CYAN + "%s" % fullname2,
										)  # is_another_color

										write_log(
											"debug movefile[need][mp4]",
											"Файл %s надо записать в %s"
											% (fullname, fullname2),
										)

									elif is_update:
										print(
											Style.BRIGHT + Fore.YELLOW + "Файл",
											Style.BRIGHT
											+ Fore.WHITE
											+ "%s" % full_to_short(fullname),
											Style.BRIGHT
											+ Fore.YELLOW
											+ "надо обновить в",
											Style.BRIGHT + Fore.CYAN + "%s" % fullname2,
										)  # is_another_color

										write_log(
											"debug movefile[need][mp4]",
											"Файл %s надо обновить в %s"
											% (fullname, fullname2),
										)

							elif not is_clean and os.path.exists(
								fullname
							):  # fullname2[0] >= fullname[0] # delete_error_project(by_base)

								no_list.append(
									dl["file"][3].strip()
								)  # add_not_ready_in_nolist(backup)

								print(
									Style.BRIGHT
									+ Fore.RED
									+ "Неправильная длина файла %s" % fullname
								)
								write_log(
									"debug destonationfile[mp4]",
									"Неправильная длина файла %s" % fullname,
								)

								await process_delete(fullname)

								if not fullname in processes_ram2:
									processes_ram2.append(fullname)

								# os.remove(fullname)

								if os.path.exists(fullname):
									print(
										Style.BRIGHT
										+ Fore.YELLOW
										+ "Удаление файла %s" % fullname
									)

									write_log(
										"debug deletefile!",
										"Удаление файла %s" % fullname,
									)
								elif not os.path.exists(fullname):
									print(
										Style.BRIGHT
										+ Fore.GREEN
										+ "Удаление файла %s" % fullname
									)

									write_log(
										"debug deletefile[mp4]",
										"Удаление файла %s" % fullname,
									)

		# del MM # clear_mem # debug

		# @update_bases
		# '''
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.load(
					somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)

		try:
			with open(filecmd_base, encoding="utf-8") as fbf:
				filecmdbase_dict = json.load(fbf)
		except:
			filecmdbase_dict = {}

			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(
					filecmdbase_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False
				)

		try:
			with open(backup_base, encoding="utf-8") as bbf:
				backupbase_dict = json.load(bbf)
		except:
			backupbase_dict = {}

			with open(backup_base, "w", encoding="utf-8") as bbf:
				json.dump(
					backupbase_dict, bbf, ensure_ascii=False, indent=4, sort_keys=True
				)

		if all((no_list, somebase_dict)):  # not_ready / not_optimized
			no_list = list(
				set([nl.strip() for nl in no_list if nl in [*somebase_dict]])
			)

		if len(no_list) != len(list(set(no_list))):
			no_list = list(set(no_list))  # unique(not_optimize)

		no_list.sort(reverse=False)  # sorted_by_abc

		if all((filecmdbase_dict, somebase_dict)):  # current_jobs / not_optimized
			filecmdbase_dict = {
				k: v for k, v in filecmdbase_dict.items() if k in [*somebase_dict]
			}

		if all((backupbase_dict, somebase_dict)):  # backup_jobs / not_optimized
			backupbase_dict = {
				k: unixtime_to_date(os.path.getmtime(k))
				for k, v in backupbase_dict.items()
				if k in [*somebase_dict]
			}

		write_log(
			"debug optimize[count]",
			"somebase/no_list/filecmdbase/backupbase/datetime %s"
			% ",".join(
				[
					str(len(somebase_dict)),
					str(len(no_list)),
					str(len(filecmdbase_dict)),
					str(len(backupbase_dict)),
					str(datetime.now()),
				]
			),
		)

		backupbase_filter_dict = (
			backupbase_dict if backupbase_dict else {}
		)  # add_backup_jobs_if_not_null
		backupbase_dict.update(backupbase_filter_dict)  # update_backup_jobs_by_filter

		backupbase_dict = {
			k: v for k, v in backupbase_dict.items() if os.path.exists(k)
		}  # check_exists_only / before_save

		# no_list_dict: dict = {}
		# no_list_dict = {nl: str(datetime.now()) for nl in no_list}
		no_list = sorted(
			[*backupbase_dict], reverse=False
		)  # is_not_optimized_jobs(sort_by_abc)

		# pass_3_of_3 # @backup.json
		with open(backup_base, "w", encoding="utf-8") as bbf:
			json.dump(
				backupbase_dict, bbf, ensure_ascii=False, indent=4, sort_keys=True
			)

		with open(files_base["backup"], "w", encoding="utf-8") as fbf:  # @backup.lst
			# fbf.writelines("%s\n" % nl.strip() for nl in filter(lambda x: x[0] == x[0].isalpha(), tuple(no_list))) # current_jobs(drive_letter_filter)
			fbf.writelines(
				"%s\n" % nl.strip()
				for nl in filter(lambda x: os.path.exists(x), tuple(no_list))
			)  # current_jobs(exists_files)

		# @stay_not_optimized_jobs # @lfcd.json
		with open(filecmd_base2, "w", encoding="utf-8") as fbf:
			json.dump(
				filecmdbase_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False
			)

		# @is_clear_current_jobs # @fcd.json
		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump({}, fbf, ensure_ascii=False, indent=4, sort_keys=False)
		# '''

		print()

		len_proc: int = len(processes_ram) + len(processes_ram2)  # is_hide

		if len_proc:
			MySt = MyString()  # MyString("Запускаю:", "[1 из 7]")

			try:
				print(
					Style.BRIGHT
					+ Fore.CYAN
					+ MySt.last2str(
						maintxt="Запускаю:",
						endtxt="[1 из 6]",
						count=len_proc,
						kw="задач",
					)
				)
				# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
			except:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Обновляю или удаляю %d файлы(а,ов) [1 из 6]" % len_proc
				)  # old(is_except)
			else:
				write_log(
					"debug run[task1]",
					MySt.last2str(
						maintxt="Запускаю:",
						endtxt="[1 из 6]",
						count=len_proc,
						kw="задач",
					),
				)

			# del MySt # clear_mem # debug

		if len(proj_files) >= 0:
			temp = [
				True if os.path.exists(pf) else False for pf in proj_files
			]  # is_no_lambda # old
			# temp = [(False, True)[os.path.exists(pf)] for pf in proj_files] # ternary

			if temp.count(True):
				try:
					# proj_files = list(pf_gen()) # new(yes_gen)
					proj_files: list = list(
						set(
							[
								pf.strip()
								for pf in filter(
									lambda x: os.path.exists(x), tuple(proj_files)
								)
								if pf
							]
						)
					)
				except:
					proj_files: list = []
				finally:
					proj_files.sort(reverse=False)  # sort_by_string
					# proj_files.sort(key=len, reverse=False) # sort_by_length

				print(
					Style.BRIGHT
					+ Fore.WHITE
					+ "Осталось %d задачи(и), которые надо очистить" % temp.count(True)
				)
				write_log(
					"debug files[project][count][+]",
					"Осталось %d задач(и), которые надо очистить" % temp.count(True),
				)

				with unique_semaphore:
					for pf in filter(lambda x: x, tuple(proj_files)):

						try:
							fname = pf.split("\\")[-1].strip()
						except:
							fname = ""
							continue

						try:
							if os.path.exists(pf):
								os.remove(pf)
						except:
							continue

		elif temp.count(False):
			print(
				Style.BRIGHT
				+ Fore.WHITE
				+ "Файлов нету или все %d задач(и) обработаны" % temp.count(False)
			)
			write_log(
				"debug files[project][count][-]",
				"Файлов нету или все %d задач(и) обработаны" % temp.count(False),
			)

	# if_stay_files(clear_him) # pass_2_of_2 # debug
	try:
		proj_list = os.listdir(path_to_done)
	except:
		proj_list = []

	try:
		if proj_list:
			proj_files: list = list(
				set(
					[
						"".join([path_to_done, pl])
						for pl in proj_list
						if os.path.exists("".join([path_to_done, pl]))
						and video_ext_regex.findall(pl)
						and all(
							(
								pl.count(".") == 1,
								not pl.split(".")[-1].lower()
								in [
									"dmf",
									"dmfr",
									"filepart",
									"aria2",
									"crdownload",
									"crswap",
								],
							)
						)
					]
				)
			)  # only_normal(files_by_tempate)
	except:
		proj_files: list = []
	finally:
		proj_files.sort(reverse=False)  # sort_by_string
		# proj_files.sort(key=len, reverse=False) # sort_by_length

	if all((len(proj_list) > 0, len(proj_list) <= len(proj_files))):
		cnt = len(proj_list)
		err = 0

		for pl in filter(lambda x: os.path.exists(x), tuple(proj_list)):
			try:
				if os.path.exists(pl):
					os.remove(pl)
					print(
						Style.BRIGHT + Fore.WHITE + "%s [%d]" % (full_to_short(pl), cnt)
					)  # is_color
					write_log("debug proj_list[delete]", "%s [%d]" % (pl, cnt))
					cnt -= 1
			except BaseException as e:
				print(Style.BRIGHT + Fore.RED + "%s [%s]" % (full_to_short(pl), str(e)))
				write_log("debug proj_list[error]", "%s [%s]" % (pl, str(e)))
				err += 1
		if all((len(proj_list) > 0, err >= 0)):
			write_log(
				"debug [projects/error][count]", "%d [%d]" % (len(proj_list), err)
			)

	write_log("debug end[project_done]", "%s" % str(datetime.now()))


# pass_x_of_4
async def project_update(
	is_debug: bool = False, is_copy_update: bool = False, is_skip_project: bool = False
):  # update_downloaded_files(tvseries/cinema) #14
	# copy_src - tvseries(update_folder), copy_src2 - cinema(update_folder), move_dst - @path_for_folder1(local_project)

	path1: str = copy_src
	path2: str = copy_src2
	path3: str = path_for_folder1

	# hidden(skip_check_exist_folder)
	if (
		not os.path.exists(path1)
		or not os.path.exists(path2)
		or not os.path.exists(path3)
	):
		return

	write_log("debug start[project_update]", "%s" % str(datetime.now()))

	print(Style.BRIGHT + Fore.WHITE + "TvSeries: %s" % str(os.path.exists(path1)))
	print(Style.BRIGHT + Fore.WHITE + "Cinema: %s" % str(os.path.exists(path2)))
	print(Style.BRIGHT + Fore.WHITE + "Project: %s" % str(os.path.exists(path3)))

	files: list = []
	files_for_job: list = []
	list_total: list = []
	files2: dict = {}
	skip_copy = set()
	copy_src_list1: list = []

	try:
		for fl in os.listdir(path1):
			if os.path.exists("".join([path1, fl])) and all(
				(fl, fl.count(".") == 1, video_ext_regex.findall(fl))
			):  # os.path.isfile("".join([path1, fl]))
				copy_src_list1.append(
					os.path.join(path1, fl).strip()
				)  # "".join([path1, fl]).strip()
	except BaseException as e:
		copy_src_list1 = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
		write_log("debug copy_src_list1[error]", "%s" % str(e), is_error=True)

	try:
		files += copy_src_list1
	except:
		pass
	else:
		write_log(
			"debug copy_src_list1[files]", "[%d] %d" % (len(copy_src_list1), len(files))
		)

	try:
		# tmp_dict = {crop_filename_regex.sub("", fn).strip(): str(datetime.now()) for csl1 in copy_src_list1 for fp, fn in split_filename(csl1) if all((fn, csl1, fn == csl1.split("\\")[-1]))}  # new_files(project/short)
		tmp_dict = {
			crop_filename_regex.sub("", csl1.split("\\")[-1]).strip(): str(
				datetime.now()
			)
			for csl1 in copy_src_list1
			if csl1
		}  # new_files(project/short)
	except BaseException as e:
		tmp_dict = {}

		write_log("debug copy_src_list1[error]!", "%s" % str(e), is_error=True)
	finally:
		write_log("debug copy_src_list1", ";".join([*tmp_dict]))  # copy_src_list1

	# a = "a.b.c.d"; ".".join(a.split(".")[0:-2]) # a.b.c # with_sep # "".join(a.split(".")[0:-2]) # abc # no_sep
	# ".".join(fl.split(".")[0:-1]).strip()
	try:
		temp = list(
			set(
				[
					fl.split(".")[0].strip()
					for fl in os.listdir(path1)
					if fl.split(".")[-1].lower()
					in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]
				]
			)
		)

		skip_file1 = sorted(temp, reverse=False)  # sort_by_string
		# skip_file1 = sorted(temp, key=len, reverse=False) # sort_by_length
	except:
		skip_file1 = []

	list1: list = []

	try:
		for fl in os.listdir(path1):
			if (
				os.path.exists(os.path.join(path1, fl).strip())
				and fl.count(".") > 1
				and (not fl.split(".")[0].strip() in skip_file1 or not skip_file1)
				and not video_ext_regex.findall(fl)
			):  # os.path.isfile("".join([path1, fl]))
				list1.append(
					os.path.join(path1, fl).strip()
				)  # "".join([path1, fl]).strip()
	except BaseException as e:
		list1 = []

		write_log("debug list1[error]!", "%s" % str(e), is_error=True)

	try:
		list_total += list1
	except:
		pass
	else:
		write_log("debug list1[list_total]", "[%d] %d" % (len(list1), len(list_total)))

	copy_src_list2: list = []

	try:
		for fl in os.listdir(path2):
			if os.path.exists(os.path.join(path2, fl).strip()) and all(
				(fl, fl.count(".") == 1, video_ext_regex.findall(fl))
			):  # os.path.isfile("".join([path2, fl]))
				copy_src_list2.append(
					os.path.join(path2, fl).strip()
				)  # "".join([path2, fl]).strip()
	except BaseException as e:
		copy_src_list2 = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
		write_log("debug copy_src_list2[error]", "%s" % str(e), is_error=True)

	try:
		files += copy_src_list2
	except:
		pass
	else:
		write_log(
			"debug copy_src_list2[files]", "[%d] %d" % (len(copy_src_list2), len(files))
		)

	try:
		# tmp_dict = {crop_filename_regex.sub("", fn).strip(): str(datetime.now()) for csl2 in copy_src_list2 for fp, fn in split_filename(csl2) if all((fn, csl2, fn == csl2.split("\\")[-1]))}  # new_files(project/short)
		tmp_dict = {
			crop_filename_regex.sub("", csl2.split("\\")[-1]).strip(): str(
				datetime.now()
			)
			for csl2 in copy_src_list2
			if csl2
		}  # new_files(project/short)
	except BaseException as e:
		tmp_dict = {}

		write_log("debug copy_src_list2[error]!", "%s" % str(e), is_error=True)
	finally:
		write_log("debug copy_src_list2", ";".join([*tmp_dict]))  # copy_src_list2

	# ".".join(fl.split(".")[0:-1]).strip()
	try:
		temp = list(
			set(
				[
					fl.split(".")[0].strip()
					for fl in os.listdir(path2)
					if fl.split(".")[-1].lower()
					in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]
				]
			)
		)

		skip_file2 = sorted(temp, reverse=False)  # sort_by_string
		# skip_file2 = sorted(temp, key=len, reverse=False) # sort_by_length
	except:
		skip_file2 = []

	list2: list = []

	try:
		for fl in os.listdir(path2):
			if (
				os.path.exists(os.path.join(path2, fl).strip())
				and fl.count(".") > 1
				and (not fl.split(".")[0].strip() in skip_file2 or not skip_file2)
				and not video_ext_regex.findall(fl)
			):  # os.path.isfile("".join([path2, fl]))
				list2.append(
					os.path.join(path2, fl).strip()
				)  # "".join([path2, fl]).strip()
	except BaseException as e:
		list2 = []

		write_log("debug list2[error]!", "%s" % str(e), is_error=True)

	try:
		list_total += list2
	except:
		pass
	else:
		write_log("debug list2[list_total]", "[%d] %d" % (len(list2), len(list_total)))

	# 7f_...
	try:
		temp = list(
			set(
				[
					lt.split("\\")[-1].split(".")[0]
					for lt in list_total
					if lt.split(".")[-1].lower()
					in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]
				]
			)
		)

		skip_copy = sorted(temp, reverse=False)  # sort_by_string
		# skip_copy = sorted(temp, key=len, reverse=False) # sort_by_length
	except:
		skip_copy = []

	# copy_src_list3: list = [] # debug

	try:
		# copy_src_list3 = list(set(["".join([path3, fn]).strip() for fl in files for fp, fn in split_filename(fl) if all((fl, fn, fn == fl.split("\\")[-1], fn.count(".") == 1))])) # os.path.isfile(fl)
		copy_src_list3 = list(
			set(
				[
					"".join([path3, fl.split("\\")[-1]]).strip()
					for fl in files
					if all((fl, fl.split("\\")[-1].count(".") == 1))
				]
			)
		)  # ?
	except BaseException as e:
		copy_src_list3 = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
		write_log("debug copy_src_list3[error]", "%s" % str(e), is_error=True)
	else:
		write_log(
			"debug copy_src_list3[files]", "[%d] %d" % (len(copy_src_list3), len(files))
		)  # move_files_from_downloads / concatinate_files

	try:
		tmp_dict = {
			crop_filename_regex.sub("", csl3.split("\\")[-1]).strip(): str(
				datetime.now()
			)
			for csl3 in copy_src_list3
			if csl3
		}
		# tmp_dict = {crop_filename_regex.sub("", fn).strip(): str(datetime.now()) for csl3 in copy_src_list3 for fp, fn in split_filename(csl3) if all((fn, csl3, fn == csl3.split("\\")[-1]))}  # new_files(project/short)

	except BaseException as e:
		tmp_dict = {}

		write_log("debug copy_src_list3[error]!", "%s" % str(e), is_error=True)
	finally:
		write_log("debug copy_src_list3", ";".join([*tmp_dict]))  # copy_src_list3

	# filter_old_file_for_delete_by_compare

	# @log_error
	async def filter_date_file(lst: list = []):  # 4

		try:
			# lst = list(l_gen()) # new(yes_gen)
			lst: list = list(
				set(
					[
						l.strip()
						for l in filter(lambda x: os.path.exists(x), tuple(lst))
						if l
					]
				)
			)
		except:
			lst: list = []
		finally:
			lst.sort(reverse=False)  # sort_by_string
			# lst.sort(key=len, reverse=False)  # sort_by_length

		for l in tuple(lst):

			if os.path.exists(l) and not is_skip_project:
				os.remove(l)

				print(
					Style.BRIGHT
					+ Fore.CYAN
					+ "Старый файл %s был удалён и оставлен более свежий" % l
				)

				write_log(
					"debug filter_date_file",
					"Старый файл %s был удалён и оставлен более свежий" % l,
				)

	# filter_by_date_if_equal_filename # (path1[update]/path3[project]):(path2[update]/path3[project]) # filter_tvseries(bigfilms)

	# pass_1_of_2

	def csl_date_filter(first=copy_src_list1, second=copy_src_list3):  # 3
		for csl1 in first:
			for csl3 in second:
				if all(
					(
						mdate_by_days(filename=csl1, is_any=True)
						> mdate_by_days(filename=csl3, is_any=True),
						csl1.split("\\")[-1] == csl3.split("\\")[-1],
						all((csl1 < csl3, csl1 != csl3)),
						csl1,
						csl3,
					)
				):
					yield csl3.strip()

	filter_date: list = []

	try:
		# filter_date = [csl3.strip() for csl1 in copy_src_list1 for csl3 in copy_src_list3 if all((mdate_by_days(filename=csl1) > mdate_by_days(filename=csl3), csl1.split("\\")[-1] == csl3.split("\\")[-1], csl1, csl3))]
		filter_date = list(set(csl_date_filter(first=copy_src_list1)))
	except:
		filter_date = []  # if_some_error
	finally:
		if filter_date and not is_skip_project:
			await filter_date_file(filter_date)  # 1>"3" # asyncio.run

	# pass_2_of_2

	try:
		# filter_date = [csl3.strip() for csl2 in copy_src_list2 for csl3 in copy_src_list3 if all((mdate_by_days(filename=csl2) > mdate_by_days(filename=csl3), csl2.split("\\")[-1] == csl3.split("\\")[-1], csl2, csl3))]
		filter_date = list(set(csl_date_filter(first=copy_src_list2)))
	except:
		filter_date = []  # if_some_error
	finally:
		if filter_date and not is_skip_project:
			await filter_date_file(filter_date)  # 2>"3" # asyncio.run

	# print(files, copy_src_list3, "project_update", end="\n")

	# parse_to_normal_file
	if len(list_total) > 0:

		try:
			tmp = len(list_total) // 2 if list_total else 0  # is_no_lambda
		except:
			tmp: int = 0

		# list_total_tmp -> tmp
		print(
			Style.BRIGHT + Fore.YELLOW + "Найдено",
			Style.BRIGHT + Fore.WHITE + "%d" % tmp,
			Style.BRIGHT + Fore.YELLOW + "файлов для преобразования и проверки",
		)
		write_log(
			"debug parse[convert][filter]",
			"Найдено %d файлов для преобразования и проверки" % tmp,
		)

		full_list = moved_list = set()

		move_files: list = []

		try:
			# tmp = list(lt_gen()) # new(yes_gen)
			tmp = list(
				set(
					[
						lt.strip()
						for lt in filter(lambda x: os.path.exists(x), tuple(list_total))
						if lt
					]
				)
			)
		except:
			tmp = []
		finally:
			tmp.sort(reverse=False)  # sort_by_string
			# tmp.sort(key=len, reverse=False) # sort_by_length

		list_total = tmp if tmp else []  # sorted/sort

		for lt in tuple(list_total):

			try:
				fname = lt.split("\\")[-1].strip()
			except:
				fname = ""
				continue

			try:
				fnshort = fname.split(".")[0].strip()
			except:
				fnshort = ""
			else:
				if all((fnshort in skip_copy, skip_copy)):  # skip_downloaded_files
					continue

			if all((not lt in full_list, lt)):
				full_list.add(lt)

			dfile1 = dfile2 = ""

			# parsed = parsed2 = False

			# normal_parse
			try:
				parsefile = await seasonvar_parse(
					lt, is_log=False
				)  # filename=lt(args) -> lt(no_args)
				# asyncio.sleep(0.05) # is_async_debug # debug
			except:
				parsefile = None
				continue  # if_error_skip_current_file # pass_1_of_2

			try:
				if (
					len(parsefile.split("$")) == 2
					and os.path.exists(parsefile.split("$")[0])
					and parsefile != None
				):

					try:
						part1, *part2, part3 = (
							parsefile.split("$")[1].split("\\")[-1].split(".")
						)
					except:
						part1 = part2 = part3 = ""
					else:
						filename_parts = (part1, *part2, part3)
						write_log(
							"debug filename[parsed]",
							"%s [%d]" % (parsefile.split("$")[1], len(filename_parts)),
						)

					# parsefile.split("$")[1] # clear_word_startswith_if_need(rename_main_file)

					# add_to_all(process_move)
					print(
						Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
						Style.BRIGHT + Fore.WHITE + "%s" % parsefile.split("$")[0],
					)

					# hidden_when_debug_parse_code # debug/test
					try:
						await process_move(
							parsefile.split("$")[0],
							parsefile.split("$")[1],
							False,
							False,
							0,
						)  # no_asyncio.run #2
					except BaseException as e:
						write_log(
							"debug process_move[error][2]",
							";".join(
								[
									parsefile.split("$")[0],
									parsefile.split("$")[1],
									str(e),
								]
							),
						)
					else:
						write_log(
							"debug process_move[ok][2]",
							";".join(
								[parsefile.split("$")[0], parsefile.split("$")[1]]
							),
						)

					try:
						if not parsefile.split("$")[0] in move_files:
							move_files.append(parsefile.split("$")[0])
					except BaseException as e:
						write_log(
							"debug move_files[append][error]",
							"%s [%s]" % (parsefile.split("$")[0], str(e)),
							is_error=True,
						)
						pass  # if_error_nothing_to_do
					else:
						write_log(
							"debug move_files[append]", "%s" % parsefile.split("$")[0]
						)

					try:
						if not parsefile.split("$")[0] in moved_list:
							moved_list.add(parsefile.split("$")[0])
					except BaseException as e:
						write_log(
							"debug moved_list[add][error]",
							"%s [%s]" % (parsefile.split("$")[0], str(e)),
							is_error=True,
						)
						pass  # if_error_nothing_to_do
					else:
						write_log(
							"debug moved_list[add]", "%s" % parsefile.split("$")[0]
						)

					# move(parsefile.split("$")[0], parsefile.split("$")[1])

			except BaseException as e:
				# Обработка файла c:\downloads\combine\original\tvseries\hello..world.txt
				# Ошибка парсинга файла ['NoneType' object has no attribute 'split']
				print(
					Style.BRIGHT
					+ Fore.RED
					+ "Ошибка парсинга файла %s [%s]" % (lt, str(e))
				)
				write_log(
					"debug parsefile[error]",
					"Ошибка парсинга файла %s [%s]" % (lt, str(e)),
					is_error=True,
				)
				continue

			try:
				if (
					len(parsefile.split("$")) == 2
					and os.path.exists(parsefile.split("$")[0])
					and parsefile != None
				):
					# full_to_short # drive + short_filename
					try:
						dfile1, dfile2 = (
							parsefile.split("$")[0],
							parsefile.split("$")[1],
						)
					except:
						dfile1 = dfile2 = ""
					else:
						if all((dfile1, dfile2)):
							print(
								Style.BRIGHT
								+ Fore.BLUE
								+ "%s" % "=->".join([full_to_short(dfile1), dfile2])
							)  # parse_filename

							print(
								Style.BRIGHT
								+ Fore.GREEN
								+ "Успешный парсинга файла %s [%s]" % (dfile1, dfile2)
							)
							write_log(
								"debug parsefile[ok]",
								"Успешный парсинга файла %s [%s]"
								% (parsefile.split("$")[0], parsefile.split("$")[1]),
							)
				elif any((len(parsefile.split("$")) != 2, parsefile == None)):
					print(
						Style.BRIGHT
						+ Fore.RED
						+ "Неизвестный парсинга файла %s" % str(parsefile)
					)
					write_log(
						"debug parsefile[unknown]",
						"Неизвестный парсинга файла %s" % str(parsefile),
					)  # some_value
					continue  # if_error_parse_skip_current_file # pass_2_of_2
			except:
				pass  # if_error_nothing_to_do

		if len(list_total) > 0:
			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ "Найдено %d задач(и) для проверки" % len(list_total)
			)
			write_log(
				"debug parser[job][count]",
				"Найдено %d задач(и) для проверки" % len(list_total),
			)

		if abs(len(list_total) - len(moved_list)) > 0:
			print(
				Style.BRIGHT
				+ Fore.WHITE
				+ "Не переименовалось %d файлов(а)"
				% abs(len(list_total) - len(moved_list))
			)
			write_log(
				"debug parser[job][no_update]",
				"Не переименовалось %d файлов(а)"
				% abs(len(list_total) - len(moved_list)),
			)

		# move_files(task_count)
		if len(moved_list) > 0:
			print(
				Style.BRIGHT + Fore.CYAN + "Переименовалось",
				Style.BRIGHT + Fore.WHITE + "%d" % len(moved_list),
				Style.BRIGHT + Fore.CYAN + "файлов(а)",
			)
			write_log(
				"debug parser[job][update]",
				"Переименовалось %d файлов(а)" % len(moved_list),
			)

		# print()

		print(
			Style.BRIGHT
			+ Fore.YELLOW
			+ "Обработанные файлы перенесутся при следующем запуске"
		)

	if copy_src_list3:

		skip_file = set()

		with unique_semaphore:
			for fl in tuple(copy_src_list3):  # new_files(project) # dont_check_exists

				try:
					fname = fl.split("\\")[-1].strip()
				except:
					fname = ""
					continue

				try:
					fnshort = fname.split(".")[0].strip()
				except:
					fnshort = ""
				else:
					if any(
						(
							fnshort.count(".") > 1,
							fname.split(".")[-1].lower()
							in [
								"dmf",
								"dmfr",
								"filepart",
								"aria2",
								"crdownload",
								"crswap",
							],
						)
					) and all(
						(fnshort, fname)
					):  # skip_downloaded(temporary_download)
						print(
							Style.BRIGHT
							+ Fore.RED
							+ "Файл %s пропущен, т.к. он закачивается" % lf
						)
						write_log(
							"debug skipfile[debug]",
							"Файл %s пропущен, т.к. включен режим отладки" % lf,
						)

						if not fnshort in skip_file:
							skip_file.add(fnshort)

					# continue

		with unique_semaphore:
			for fl in tuple(copy_src_list3):  # dont_check_exists

				try:
					fname = fl.split("\\")[-1].strip()
				except:
					fname = ""
					continue

				try:
					fnshort = fname.split(".")[0].strip()
				except:
					fnshort = ""
				else:
					if all((fnshort in skip_file, fnshort, skip_file)):
						continue

				if video_ext_regex.findall(
					fname
				):  # with_short_video_by_template # debug(off)
					if os.path.exists("".join([path3, fl.split("\\")[-1]])):
						files_for_job.append(
							{
								"file": fl.strip(),
								"file2": "".join([path3, fl.split("\\")[-1]]).strip(),
								"status": "update",
								"debug": is_debug,
							}
						)
					elif not os.path.exists("".join([path3, fl.split("\\")[-1]])):
						files_for_job.append(
							{
								"file": fl.strip(),
								"file2": "".join([path3, fl.split("\\")[-1]]).strip(),
								"status": "add",
								"debug": is_debug,
							}
						)

	if all((len(copy_src_list3) > 0, len(files_for_job) > 0)):
		print(
			Style.BRIGHT
			+ Fore.CYAN
			+ "Файлов %d для обновления %d проектов"
			% (len(copy_src_list3), len(files_for_job))
		)
		write_log(
			"debug projects[yes]",
			"Файлов %d для обновления %d проектов"
			% (len(copy_src_list3), len(files_for_job)),
		)
	elif all((len(copy_src_list3) > 0, len(files_for_job) == 0)):
		print(
			Style.BRIGHT + Fore.CYAN + "Файлов %d для обновления" % len(copy_src_list3)
		)
		write_log(
			"debug projects[yes]", "Файлов %d для обновления" % len(copy_src_list3)
		)
	elif all((not copy_src_list3, not files_for_job)):
		print(Style.BRIGHT + Fore.CYAN + "Нет файлов для обновления проектов")
		write_log("debug projects[no]", "Нет файлов для обновления проектов")

		return  # if_no_files(exit_from_function)

	try:
		files2 = {
			fl.strip(): csl3.strip()
			for fl in files
			for csl3 in copy_src_list3
			if all((fl, csl3, fl.split("\\")[-1] == csl3.split("\\")[-1]))
		}  # csl3(new_files(project))
	except:
		files2 = {}

	# print(files2, end="\n") # dict

	processes_ram: list = []
	processes_ram2: list = []

	fsizes_list: list = []

	skip_file = set()

	for ffj in files2:  # for k, v in files2.items() # is_dict

		try:
			assert files2, "Пустой список или нет файлов files2"  # is_assert_debug
		except AssertionError as err:  # if_null
			logging.warning(
				"Пустой список или нет файлов files2 [%s]" % str(datetime.now())
			)
			raise err
			break
		except BaseException as e:  # if_error
			logging.error(
				"Пустой список или нет файлов files2 [%s] [%s]"
				% (str(e), str(datetime.now()))
			)
			break

		try:
			assert ffj and os.path.exists(ffj), ""  # is_assert_debug # ffj
		except AssertionError as err:  # if_null
			raise err
			continue
		except BaseException:  # if_error
			continue

		try:
			fname = ffj.split("\\")[-1].strip()
		except:
			fname = ""
			# continue

		try:
			fnshort = fname.split(".")[0].strip()
		except:
			fnshort = ""
		else:
			if any(
				(
					fnshort.count(".") > 1,
					fname.split(".")[-1].lower()
					in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"],
				)
			) and all(
				(fnshort, fname)
			):  # skip_downloaded(temporary_download)
				print(
					Style.BRIGHT
					+ Fore.RED
					+ "Файл %s пропущен, т.к. он закачивается" % ffj
				)

				write_log(
					"debug skipfile[debug]",
					"Файл %s пропущен, т.к. включен режим отладки" % ffj,
				)

				if all((not fnshort in skip_file, fnshort)):
					skip_file.add(fnshort)

			# continue

	if files2 and not os.path.isfile(path3):  # project_files

		try:
			fsizes_list: list = list(
				set(
					[
						os.path.getsize(ffj)
						for ffj in files2
						if os.path.exists(ffj) and ffj
					]
				)
			)
		except:
			fsizes_list: list = []
		else:
			fsizes_list.sort(reverse=False)  # sort_by_string
			# fsizes_list.sort(key=len, reverse=False) # sort_by_length

		try:
			avg_size = await avg_lst(list(set(fsizes_list)))  # async(avg_size)
			assert avg_size, ""  # is_assert_debug
		except AssertionError as err:  # if_null
			avg_size: int = 0
			raise err  # logging
		except BaseException:  # if_error
			try:
				avg_size = (lambda s, l: s / l)(
					sum(fsizes_list), len(fsizes_list)
				)  # by_lambda
			except:
				avg_size = 0

		for ffj in files2:  # is_dict

			if not files2:  # no _data
				break

			try:
				dfile1, dfile2 = ffj, files2[ffj]
			except:
				dfile1 = dfile2 = ""
			finally:
				if all((dfile1, dfile2)):
					print(
						Style.BRIGHT
						+ Fore.BLUE
						+ "%s" % "=->".join([full_to_short(dfile1), dfile2])
					)  # move_downloads_files

			try:
				fname = ffj.split("\\")[-1].strip()
			except:
				fname = ""
				# continue

			try:
				fnshort = fname.split(".")[0].strip()
			except:
				fnshort = ""
			else:
				if all((fnshort in skip_file, fnshort, skip_file)):
					continue

			try:
				fsize1 = os.path.getsize(ffj)
			except:
				fsize1 = 0

			try:
				fsize2 = os.path.getsize(files2[ffj])
			except:
				fsize2 = 0

			try:
				is_new = os.path.exists(ffj) and not os.path.exists(files2[ffj])
			except:
				is_new = False

			try:
				is_update = os.path.exists(ffj) and os.path.exists(files2[ffj])
			except:
				is_update = False

			try:
				if (
					os.path.exists(ffj)
					and any((is_new, is_update))
					and fspace(ffj, files2[ffj])
				):  # new/update # fspace
					if is_debug == True:
						if all((fsize2, is_update)):
							print(
								Style.BRIGHT + Fore.YELLOW + "Будет обновлено",
								Style.BRIGHT
								+ Fore.WHITE
								+ "%s" % "=>".join([dfile1, dfile2]),
							)
							write_log(
								"debug movefile[update]!",
								"Будет обновлено %s" % "=>".join([ffj, files2[ffj]]),
							)
						elif all((not fsize2, is_new)):
							print(
								Style.BRIGHT + Fore.GREEN + "Будет добавлено",
								Style.BRIGHT
								+ Fore.WHITE
								+ "%s" % "=>".join([dfile1, dfile2]),
							)
							write_log(
								"debug movefile[add]!",
								"Будет добавлено %s" % "=>".join([ffj, files2[ffj]]),
							)
					elif is_debug == False:
						# print(Style.BRIGHT + Fore.CYAN + "Было добавлено или обновлено", Style.BRIGHT + Fore.WHITE + "%s" % "~>".join([dfile1, dfile2]))
						# write_log("debug movefile[update]", "Было добавлено или обновлено %s" % "~>".join([dfile1, dfile2]))

						if all((os.path.getsize(ffj) <= avg_size, avg_size)):
							print(
								Style.BRIGHT
								+ Fore.GREEN
								+ "Добавление в очередь файла",
								Style.BRIGHT + Fore.WHITE + "%s" % ffj,
							)  # add_to_all(process_move)

							try:
								await process_move(
									ffj, files2[ffj], False, True, avg_size
								)  # no_asyncio.run # async_if_small #3
								if is_copy_update:
									await process_move(
										ffj, files2[ffj], True, True, avg_size
									)
							except BaseException as e:
								write_log(
									"debug process_move[error][3]",
									";".join([ffj, files2[ffj], str(e)]),
								)
							else:
								write_log(
									"debug process_move[ok][3]",
									";".join([ffj, files2[ffj]]),
								)

							if not ffj in processes_ram:
								processes_ram.append(ffj)

						elif (
							all((os.path.getsize(ffj) > avg_size, avg_size))
							or not avg_size
						):
							move(ffj, files2[ffj])  # no_async_if_big

							if is_new:
								print(
									Style.BRIGHT + Fore.GREEN + "Файл",
									Style.BRIGHT + Fore.WHITE + "%s" % ffj,
									Style.BRIGHT + Fore.YELLOW + "надо записать в",
									Style.BRIGHT + Fore.CYAN + "%s" % files2[ffj],
								)  # is_another_color # dfile2
								write_log(
									"debug movefile[need]",
									"Файл %s надо записать в %s" % (ffj, files2[ffj]),
								)

							elif is_update:
								print(
									Style.BRIGHT + Fore.YELLOW + "Файл",
									Style.BRIGHT + Fore.WHITE + "%s" % ffj,
									Style.BRIGHT + Fore.YELLOW + "надо обновить в",
									Style.BRIGHT + Fore.CYAN + "%s" % files2[ffj],
								)  # is_another_color # dfile2
								write_log(
									"debug movefile[need]",
									"Файл %s надо обновить в %s" % (ffj, files2[ffj]),
								)

				elif os.path.exists(ffj) and all(
					(fsize1 == fsize2, fsize1, fsize2)
				):  # delete
					if is_debug == True:
						print(
							Style.BRIGHT + Fore.CYAN + "Будет удалено",
							Style.BRIGHT + Fore.WHITE + "%s" % dfile1,
						)
						write_log("debug deletefile[update]!", "Будет удалено %s" % ffj)
					elif is_debug == False:
						# print(Style.BRIGHT + Fore.BLUE + "Было удалено", Style.BRIGHT + Fore.WHITE + "%s" % dfile1)
						# write_log("debug deletefile[update]", "Было удалено %s" % dfile1)

						await process_delete(ffj)  # async_if_delete

						if not ffj in processes_ram2:
							processes_ram2.append(ffj)

					# os.remove(ffj["file"])
			except BaseException as e:
				print(Style.BRIGHT + Fore.RED + "%s" % str(e))

	print()

	len_proc: int = len(processes_ram) + len(processes_ram2)

	if all((len_proc, is_debug == False)):
		MySt = MyString()  # MyString("Запускаю:", "[2 из 6]")

		try:
			print(
				Style.BRIGHT
				+ Fore.CYAN
				+ MySt.last2str(
					maintxt="Запускаю:", endtxt="[2 из 6]", count=len_proc, kw="задач"
				)
			)
			# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
		except:
			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ "Обновляю или удаляю %d файлы(а,ов) [2 из 6]" % len_proc
			)  # old(is_except)
		else:
			write_log(
				"debug run[task2]",
				MySt.last2str(
					maintxt="Запускаю:", endtxt="[2 из 6]", count=len_proc, kw="задач"
				),
			)

		del MySt

	write_log("debug end[project_update]", "%s" % str(datetime.now()))


# update_bigcinema_by_year # pass_x_of_4
async def update_bigcinema():  # 11

	write_log("debug start[update_bigcinema]", "%s" % str(datetime.now()))

	# pass_1_of_2 # update_exists_files # ok

	# move_big_films(lfiles) # need_code # move_project_to_folder1 # update
	# '''

	MM = MyMeta()  # 3

	# standarts (.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf)

	# temp_download (^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^crdownload|^.crswap)

	# subtitles {.srt|.smi|.s2k|.ssa|.ass|.sub|.vtt|.dfxp|.xml|.scc|.itt|.stl|.ogm|.ass|.sub|.csv|.rtf|.psl|.vtt|.stl}

	video_regex = re.compile(
		r"(.*)(\([\d+]{4}\))(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^crdownload|^.crswap|^.srt|.smi|.s2k|.ssa|.ass|.sub|.vtt|.xml|.scc|.itt|.stl|.ogm|.ass|.sub|.csv|.rtf|.psl|.vtt|.stl|.dfxp))$",
		re.M,
	)
	video_big_regex = re.compile(
		r"\([\d+]{4}\)", re.M
	)  # ; filename = r"c:\\downloads\\film(2000).mp4"

	big_cinema: list = []

	file_cinema: str = "d:\\multimedia\\video\\big_films\\"

	try:
		year_range = list(
			set(
				[
					os.path.join(file_cinema, yr).strip()
					for yr in os.listdir(file_cinema)
					if os.path.exists("".join([file_cinema, yr]))
					and not os.path.isfile("".join([file_cinema, yr]))
				]
			)
		)
	except:
		year_range = []
	else:
		if year_range:
			for yr in sorted(year_range, reverse=False):
				try:
					if len(os.listdir(yr)) == 0:  # delete_folder_if_no_files

						try:
							os.rmdir(yr)  # type1 # dos_delete_folder_by_python
						except:
							os.system(
								r"cmd /c rmdir %s" % yr
							)  # type2(error) # dos_delete_folder # cmd /k
						finally:
							if not os.path.exists(yr):
								print(
									Style.BRIGHT
									+ Fore.GREEN
									+ "В папке %s нет больших файлов и была удалена"
									% yr
								)
								write_log(
									"debug delete[folder][big_cinema]",
									"В папке %s нет больших файлов и была удалена" % yr,
								)

				except BaseException as e:
					print(
						Style.BRIGHT
						+ Fore.RED
						+ "Ошибка удаления папки %s [%s]" % (yr, str(e))
					)
					write_log(
						"debug delete[folder][big_cinema][error]",
						"Ошибка удаления папки %s [%s]" % (yr, str(e)),
						is_error=True,
					)

					continue

	# filename = "Some_film(2000).mp4" # debug_filename

	if os.path.exists(file_cinema):  # if_have_nlocal_folder
		with ThreadPoolExecutor(max_workers=ccount) as e:
			nlf = e.submit(
				sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex
			)  # nlocal # filmy

		try:
			big_cinema = nlf.result()
		except:
			big_cinema = []

	elif (
		not os.path.exists(file_cinema) or not big_cinema
	):  # if_no_nlocal_folder(no_files)
		big_cinema = []

	print(Style.BRIGHT + Fore.CYAN + "Перегруппировка файлов начата. Ждите...")

	for bc in filter(lambda x: x, tuple(big_cinema)):
		# change_datetime_at_folder_by_last_(access/modify/create)_date # big_cinema # debug
		#'''
		file_path, file_name = os.path.split(bc)

		maxdate_m = ""  # maxdate_c = maxdate_m = maxdate_a = ""

		try:
			files = [
				os.path.join(file_path, f)
				for f in os.listdir(file_path)
				if os.path.exists(os.path.join(file_path, f))
			]
			files = [f.strip() for f in files if os.path.isfile(f)]
		except:
			files = []

		try:
			maxdate_folder = os.path.getctime(
				file_path
			)  # create(min) # debug # pass_1_of_2
			# maxdate_folder = os.path.getatime(file_path) # access(max) # debug # pass_1_of_2
		except:
			maxdate_folder = None

		# maxdate_c = max(files, key=os.path.getctime) # 'C:\\Python27\\LICENSE.txt' # created
		# maxdate_a = max(files, key=os.path.getatime) # 'C:\\Python27\\LICENSE.txt' # access
		maxdate_m = max(
			files, key=os.path.getmtime
		)  # 'C:\\Python27\\LICENSE.txt' # modify

		try:
			maxdate_file = os.path.getmtime(maxdate_m)  # modify # debug # pass_2_of_2
		except:
			maxdate_file = None

		if all(
			(
				maxdate_folder != None,
				maxdate_file != None,
				maxdate_folder != maxdate_file,
			)
		):
			os.utime(
				file_path, times=(maxdate_folder, maxdate_file)
			)  # is_recovery_datetime # old -> new
		else:
			continue
		# '''

	print(Style.BRIGHT + Fore.YELLOW + "Перегруппировка файлов завершена...")

	print(
		Style.BRIGHT
		+ Fore.CYAN
		+ "Проверка готовых больших и проектов файлов. Ждите..."
	)

	# create_folders_by_years(if_not_exists)

	project_bigcinema: list = []

	try:
		project_bigcinema = list(
			set(
				[
					video_big_regex.findall(pff)[0]
					.replace("(", "")
					.replace(")", "")
					.strip()
					for pff in os.listdir(path_for_folder1)
					if video_big_regex.findall(pff)[0]
					.replace("(", "")
					.replace(")", "")
					.isnumeric()
				]
			)
		)
	except:
		project_bigcinema = []
	finally:
		pb_status = (
			len(project_bigcinema) if len(project_bigcinema) > 0 else 0
		)  # is_no_lambda
		write_log("debug project_bigcinema[count]", "%d" % pb_status)

	for pb in filter(lambda x: x, tuple(project_bigcinema)):

		if not project_bigcinema:
			break

		try:
			clear_year = os.path.join(file_cinema, pb).strip()
		except:
			clear_year = ""

		try:
			if not os.path.exists(clear_year) and all(
				(clear_year, pb.strip().isnumeric())
			):
				try:
					os.mkdir(clear_year)  # type1(try)
				except:
					os.system(r"cmd /c mkdir %s" % clear_year)  # type2(error) # cmd /k
		except BaseException as e:
			write_log(
				"debug bigcinema[folder][error]",
				"%s [%s]" % (clear_year, str(e)),
				is_error=True,
			)
		# continue # skip_if_error
		else:
			bc_status = ""

			try:
				bc_status = (
					f"Папка {clear_year} создана"
					if os.path.exists(clear_year)
					else f"Папка {clear_year} не создана"
				)
			except:
				bc_status = f"Ошибка создания папки {clear_year}"
			finally:
				write_log("debug bigcinema[status]", "%s" % bc_status)
	# move_ready_bigcinema_to_projects

	list1: list = []

	try:
		list1 = os.listdir(path_to_done)
	except:
		list1 = []
	finally:
		if list1:
			move_dict = {
				os.path.join(path_to_done, l1)
				.strip(): os.path.join(path_for_folder1, l1)
				.strip()
				for l1 in list1
				if video_big_regex.findall(l1)
				and os.path.isfile(os.path.join(path_to_done, l1).strip())
			}  # ready/project # is_move_for_pass2
		else:
			move_dict = {}

		rename_count: int = 0

		for k, v in move_dict.items():

			try:
				assert (
					move_dict or big_cinema
				), "Нет файлов для переноса @update_bigcinema/move_dict/big_cinema"  # is_assert_debug
			except AssertionError as err:  # if_null
				logging.warning(
					"Нет файлов для переноса @update_bigcinema/move_dict/big_cinema"
				)
				raise err
				break
			except BaseException as e:  # if_error
				logging.error(
					"Нет файлов для переноса @update_bigcinema/move_dict/big_cinema [%s]"
					% str(e)
				)
				break

			try:
				fname1 = k.split("\\")[-1].strip()  # project(v) -> ready(k)
			except:
				fname1 = ""

			# new_count: int = 0
			move_count: int = 0
			delete_count: int = 0
			rename_count: int = 0

			for bc in tuple(big_cinema):  # os.path.exists(x) -> x # new(yes_gen)

				try:
					assert big_cinema, ""  # is_assert_debug
				except AssertionError as err:  # if_null
					raise err
					break

				try:
					assert bc, ""  # is_assert_debug
				except AssertionError as err:  # if_null
					raise err
					continue

				try:
					fname2 = bc.split("\\")[-1].strip()
				except:
					fname2 = ""

				fext = ""

				if all((fname1 == fname2, fname1, fname2)):
					fext = fname1.split("\\")[-1].split(".")[0].strip() + ".bak"

				# original_error_meta_or_null_size_or_null_length

				is_error = False

				if (
					any(
						(
							MM.get_meta(bc) == False,
							os.path.getsize(bc) == 0,
							MM.get_length(bc) == 0,
						)
					)
					and all((fext, k.split("\\")[-1] == bc.split("\\")[-1]))
					or not os.path.exists(bc)
				):  # meta(error) # null_size(0) # null_length(0) # ready_and_project_equal_shortfilename

					if MM.get_meta(bc) == False:
						logging.warning(
							"get_meta[error] %s [%s]" % (bc, str(datetime.now()))
						)  # error_dict[bc.strip()] = "get_meta[error] [%s]" % str(datetime.now())

					if os.path.getsize(bc) == 0:
						logging.warning(
							"get_size[error] %s [%s]" % (bc, str(datetime.now()))
						)  # error_dict[bc.strip()] = "get_size[error] [%s]" % str(datetime.now())

					if MM.get_length(bc) == 0:
						logging.warning(
							"get_length[error] %s [%s]" % (bc, str(datetime.now()))
						)  # error_dict[bc.strip()] = "get_length[error] [%s]" % str(datetime.now())

					bigcinema_folder = "\\".join(bc.split("\\")[:-1]) + "\\"

					mp4_to_bak = "".join([bigcinema_folder, fext])

					# move(bc, mp4_to_bak) # rename_original_to_bak_if_error_meta

					# write_log("debug mp4_to_back", "%s" % mp4_to_bak)
					write_log("debug mp4_to_back!", "%s" % mp4_to_bak)

					rename_count += 1

					print(
						Style.BRIGHT + Fore.RED + "-(%s)-" % mp4_to_bak,
						"[%d]" % rename_count,
						end="\n",
					)  # rename_by_error_length
					write_log(
						"debug bigcinema[rename]",
						"-(%s)-" % mp4_to_bak,
						"[%d]" % rename_count,
					)  # delete -> rename

					is_error = True

					if all(
						(fname1 == fname2, fname1, fname2, not is_error)
					):  # equal_filename_without_errors

						try:
							gl1 = MM.get_length(k)
						except:
							gl1 = 0

						try:
							gl2 = MM.get_length(bc)
						except:
							gl2 = 0

						is_clean = all(
							(gl1 in range(gl2, gl2 - 10, -1), gl1, gl2)
						)  # big_cinema

						if is_clean and os.path.exists(k):

							# load_meta_jobs(filter) #5
							try:
								with open(some_base, encoding="utf-8") as sbf:
									somebase_dict = json.load(sbf)
							except:
								somebase_dict = {}

								with open(some_base, "w", encoding="utf-8") as sbf:
									json.dump(
										somebase_dict,
										sbf,
										ensure_ascii=False,
										indent=4,
										sort_keys=True,
									)

							first_len: int = len(somebase_dict)

							# clean_project_from_base.append(fullname2)

							somebase_dict = {
								k: v
								for k, v in somebase_dict.items()
								if os.path.exists(k)
							}  # exists_only # pass_1_of_2
							somebase_dict = {
								k: v for k, v in somebase_dict.items() if k != bc
							}  # clear_if_ready(delete)  # big_cinema # pass_2_of_2 # somebase_dict.pop(bc)

							second_len: int = len(somebase_dict)

							if (
								somebase_dict
							):  # delete_ready_jobs # second_len <= first_len # all -> any
								with open(some_base, "w", encoding="utf-8") as sbf:
									json.dump(
										somebase_dict,
										sbf,
										ensure_ascii=False,
										indent=4,
										sort_keys=True,
									)

								write_log(
									"debug somebase_dict[delete]",
									"%d" % len(somebase_dict),
								)

								print(
									Style.BRIGHT
									+ Fore.YELLOW
									+ "Подготовка к переносу файла",
									Style.BRIGHT + Fore.WHITE + "%s" % bc,
								)
								write_log(
									"debug bc[move]",
									"Подготовка к переносу файла %s" % bc,
								)

								try:
									fsize: int = os.path.getsize(k)
									dsize: int = disk_usage(bc[0] + ":\\").free
									try:
										fsize2: int = os.path.getsize(bc)
									except:
										fsize2: int = 0
								except:
									fsize: int = 0
									dsize: int = 0
								else:
									if all(
										(
											fsize,
											dsize,
											int(fsize // (dsize / 100)) <= 100,
											fsize != fsize2,
										)
									):
										move(k, bc)  # update_if_ok_length_by_move

										move_count += 1

										print(
											Style.BRIGHT
											+ Fore.YELLOW
											+ "%s [%d]"
											% ("-=>".join([k, bc]), move_count)
										)  # update_by_length

										write_log(
											"debug bigcinema[move]",
											"%s [%d]"
											% ("-=>".join([k, bc]), move_count),
										)
										MyNotify(
											txt="%s" % full_to_short(bc),
											icon=icons["different"],
										)

									elif (
										all(
											(
												fsize >= 0,
												dsize,
												int(fsize // (dsize / 100)) > 100,
											)
										)
										or not dsize
									):  # fspace(bad) # dspace(bad)
										print(
											Style.BRIGHT
											+ Fore.YELLOW
											+ "debug bigcinema[fspace] '%s'"
											% full_to_short(bc)
										)
										write_log("debug bigcinema[fspace]", "%s" % bc)
										MyNotify(
											txt="%s" % full_to_short(bc),
											icon=icons["error"],
										)
										continue
									elif all((fsize, fsize2, fsize == fsize2)):
										print(
											Style.BRIGHT
											+ Fore.WHITE
											+ "debug bigcinema[equals] '%s'"
											% full_to_short(bc)
										)
										write_log("debug bigcinema[equals]", "%s" % bc)
										# MyNotify(txt="%s" % full_to_short(bc), icon=icons["error"]) # os.remove(k)

										if os.path.exists(bc):
											if (
												k[0] < bc[0]
												and k.split("\\")[-1]
												== bc.split("\\")[-1]
											):
												write_log(
													"debug delete[k/bc]!",
													"%s" % ";".join([k, bc]),
												)  # os.remove(k)
										continue

								# @load_current_jobs
								try:
									with open(filecmd_base, encoding="utf-8") as fbf:
										fcmd = json.load(fbf)
								except:
									fcmd = {}

									with open(
										filecmd_base, "w", encoding="utf-8"
									) as fbf:
										json.dump(
											fcmd,
											fbf,
											ensure_ascii=False,
											indent=4,
											sort_keys=False,
										)

								first_len = len(fcmd)

								if all((fcmd, somebase_dict)):
									fcmd = {
										k: v
										for k, v in fcmd.items()
										if os.path.exists(k)
										and any(
											(
												k.strip() in [*somebase_dict],
												not [*somebase_dict],
											)
										)
									}

								second_len = len(fcmd)

								if all(
									(fcmd, second_len <= first_len)
								):  # filter_current_and_not_optimize_jobs
									with open(
										filecmd_base, "w", encoding="utf-8"
									) as fbf:
										json.dump(
											fcmd,
											fbf,
											ensure_ascii=False,
											indent=4,
											sort_keys=False,
										)

									write_log("debug fcmd[filter]", "%d" % len(fcmd))

						elif not is_clean and os.path.exists(k):
							os.remove(k)  # del_ready_with_error_length

							delete_count += 1

							print(
								Style.BRIGHT
								+ Fore.RED
								+ "-(%s)- [%d]" % (k, rename_count),
								end="\n",
							)
							write_log(
								"debug bigcinema[delete]",
								"-(%s)- [%d]" % (k, rename_count),
							)

	print(
		Style.BRIGHT
		+ Fore.YELLOW
		+ "Проверка готовых больших и проектов файлов завершена..."
	)

	print()

	print(Style.BRIGHT + Fore.CYAN + "Проверка новых больших файлов. Ждите...")

	processes_ram: list = []
	processes_ram2: list = []

	# pass_2_of_2 # new_file_for_move_by_year # debug/test

	# move_big_films(lfiles) # need_code # move_folder1_to_bigfilms # src_to_dst
	try:
		list1 = os.listdir(path_for_folder1)
	except:
		list1 = []
	finally:
		temp = [
			os.path.join(path_for_folder1, l1)
			for l1 in list1
			if os.path.isfile(os.path.join(path_for_folder1, l1).strip())
		]

		list1 = sorted(temp, reverse=False)  # sort_by_string
		# list1 = sorted(temp, key=len, reverse=False) # sort_by_length

		if list1:

			new_count: int = 0
			move_count: int = 0
			delete_count: int = 0

			avg_size: int = 0

			try:
				fsizes = list(
					set(
						[
							os.path.getsize(l1)
							for l1 in filter(lambda x: os.path.exists(x), tuple(list1))
							if l1
						]
					)
				)
			except:
				fsizes = []
			finally:
				fsizes.sort(reverse=False)  # sort_by_string
				# fsizes.sort(key=len, reverse=False) # sort_by_length

			try:
				avg_size = await avg_lst(list(set(fsizes)))  # async(avg_size)
				assert avg_size, ""  # is_assert_debug
			except AssertionError as err:  # if_null
				avg_size: int = 0
				raise err  # logging
			except BaseException:  # if_error
				try:
					avg_size = (lambda s, l: s // l)(
						sum(fsizes), len(fsizes)
					)  # by_lambda
				except:
					avg_size = 0

			with unique_semaphore:
				for l1 in filter(lambda x: x, tuple(list1)):

					try:
						assert list1, "Пустой список list1"  # is_assert_debug
					except AssertionError as err:  # if_null
						logging.warning(
							"Пустой список list1 [%s]" % str(datetime.now())
						)
						raise err
						break
					except BaseException as e:  # if_error
						logging.error(
							"Пустой список list1 [%s] [%s]"
							% (str(e), str(datetime.now()))
						)
						break

					try:
						fname = l1.split("\\")[-1].strip()
					except:
						fname = ""
						continue

					try:
						year_path = "".join(
							[
								file_cinema,
								video_big_regex.findall(fname)[0]
								.replace("(", "")
								.replace(")", ""),
							]
						)

						year_path += "\\" + fname
					except:
						year_path = ""
					finally:

						print(
							Style.BRIGHT
							+ Fore.WHITE
							+ "%s" % "->".join([year_path, fname])
						)  # new
						write_log("debug yearfolder", "->".join([year_path, fname]))

					if all((l1, year_path)) and os.path.exists(
						"".join(
							[
								file_cinema,
								video_big_regex.findall(fname)[0]
								.replace("(", "")
								.replace(")", ""),
							]
						)
					):

						try:
							fsize: int = os.path.getsize(l1)
							dsize: int = disk_usage(year_path[0] + ":\\").free
						except:
							fsize: int = 0
							dsize: int = 0
						else:
							if all((fsize, dsize, int(fsize // (dsize / 100)) <= 100)):
								# move(l1, year_path) # processes_ram

								print(
									Style.BRIGHT
									+ Fore.GREEN
									+ "Добавление в очередь файла",
									Style.BRIGHT + Fore.WHITE + "%s" % l1,
								)  # add_to_all(process_move)

								try:
									await process_move(
										l1, year_path, False, True, avg_size
									)  # no_asyncio.run # async_if_small #4
								except BaseException as e:
									write_log(
										"debug process_move[error][4]",
										";".join([l1, year_path, str(e)]),
									)
								else:
									write_log(
										"debug process_move[ok][4]",
										";".join([l1, year_path]),
									)

								if not l1 in processes_ram:
									processes_ram.append(l1)

								print(
									Style.BRIGHT
									+ Fore.GREEN
									+ "%s[2]" % "==>".join([l1, year_path])
								)  # new
								write_log(
									"debug bigcinema[moved]",
									"%s[2]" % "==>".join([l1, year_path]),
								)

								new_count += 1

							elif (
								all(
									(
										fsize >= 0,
										dsize,
										int(fsize // (dsize / 100)) > 100,
									)
								)
								or not dsize
							):  # fspace(bad) # dspace(bad)
								# os.remove(l1) # processes_ram2

								# await process_delete(l1) # async_if_delete # is_debug

								if not l1 in processes_ram2:
									processes_ram2.append(l1)

								print(
									Style.BRIGHT
									+ Fore.GREEN
									+ "bigcinema[deleted] '-(%s[2])-'"
									% full_to_short(l1),
									end="\n",
								)
								write_log("debug bigcinema[deleted]", "-(%s[2])-" % l1)
								MyNotify(
									txt="-(%s[2])-" % full_to_short(l1),
									icon=icons["error"],
								)

								delete_count += 1

	print()

	len_proc: int = len(processes_ram) + len(processes_ram2)

	if len_proc:
		MySt = MyString()  # MyString("Запускаю:", "[3 из 6]")

		try:
			print(
				Style.BRIGHT
				+ Fore.CYAN
				+ MySt.last2str(
					maintxt="Запускаю:", endtxt="[3 из 6]", count=len_proc, kw="задач"
				)
			)
			# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))#
		except:
			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ "Обновляю или удаляю %d файлы(а,ов) [3 из 6]" % len_proc
			)  # old(is_except)
		else:
			write_log(
				"debug run[task3]",
				MySt.last2str(
					maintxt="Запускаю:", endtxt="[3 из 6]", count=len_proc, kw="задач"
				),
			)

		del MySt

	print(Style.BRIGHT + Fore.YELLOW + "Проверка новых больших файлов завершена...")

	del MM

	write_log("debug end[update_bigcinema]", "%s" % str(datetime.now()))


# pass_x_of_4
async def true_project_rename(
	folder=path_for_folder1, folderlst=vr_folder
):  # what_file_need_rename(try_change_project_folder_to_only_tv_series) # path_for_folder1 -> copy_src #18

	# return

	try:
		assert folder and os.path.exists(
			folder
		), f"Папка отсутствует @true_project_rename/{folder}"  # is_assert_debug # folder
	except AssertionError as err:  # if_null
		logging.warning(
			"Папка отсутствует @true_project_rename/%s [%s]"
			% (folder, str(datetime.now()))
		)
		raise err
		return
	except BaseException as e:  # if_error
		logging.error(
			"Папка отсутствует @true_project_rename/%s [%s] [%s]"
			% (folder, str(e), str(datetime.now()))
		)
		return

	write_log("debug start[true_project_rename]", "%s" % str(datetime.now()))

	# lfiles_filter: list = []

	"""
	@video_resize.dir @vr_folder
	{"d:\\multimedia\\video\\serials_conv\\13_Ghosts_of_Scooby_Doo": "13_Ghosts_of_Scooby_Doo"}
	"""

	# need_convert_current_dict_to_registry_dict
	try:
		with open(vr_folder, encoding="utf-8") as vff:
			filter_dict = json.load(vff)
	except:
		filter_dict = {}

	year_regex = re.compile(r"\([\d+]{4}\)", re.M)

	# list_files_in_"project"_folder # if_true_file_save_fullpath(for_tvseries)
	try:
		lfiles = [
			os.path.join(folder, lf).strip()
			for lf in os.listdir(folder)
			if all((lf.count(".") >= 1, not year_regex.findall(lf)))
		]
	except:
		lfiles = []

	# gen_skip_list(lfiles)
	skip_set = set()

	flist = [
		lf.split("\\")[-1].strip()
		for lf in filter(lambda x: "aria2" in x, tuple(lfiles))
		if os.path.exists(lf)
	]

	flst = [
		f.split("\\")[-1].split(".")[:1] for f in flist if f.count(".") > 2
	]  # skip_filter # ['7f_2'] <class 'list'>
	flst2 = [
		f.split("\\")[-1].split("_")[:1]
		for f in flist
		if all((f.count(".") == 2, f.count("_") == 1))
	]  # skip_filter # ['Afterparty'] <class 'list'>
	flst3 = [
		f.split("\\")[-1].split("_")[:2]
		for f in flist
		if all((f.count(".") == 2, f.count("_") > 1))
	]  # skip_filter # ['2', 'Broke'] <class 'list'>

	fl: list = []

	try:
		fl += flst
		fl += flst2
		fl += flst3
	except:
		fl = []
	else:
		for f in fl:
			if not fl:
				break

			if isinstance(f, list):
				if len(f) == 1:
					skip_set.add(f[0])
				elif len(f) > 1:
					skip_set.add("_".join(f))

		# print(f, type(f), end="\n") # debug

	# print(list(skip_set)) # debug # ['7f_2', 'Afterparty', '2_Broke']

	new_list: list = []

	try:
		new_list = list(
			set(
				[
					lf.strip()
					for ss in filter(lambda x: x, tuple(list(skip_set)))
					for lf in filter(lambda y: y, tuple(lfiles))
					if lf.split("\\")[-1].startswith(ss)
				]
			)
		)  # skip_list_for_lfiles # debug
	except:
		new_list = []
	finally:
		if new_list:
			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ "Найдено %d скачанных файлов и файлы будут пропущены [%s]"
				% (len(new_list), str(datetime.now()))
			)

			# lfiles = sorted(new_list, key=len, reverse=False) # is_need(no_debug)
			# new_list = [] # clear_if_need_rename
			if new_list:
				write_log(
					"debug new_list[yes]!",
					"Найдено %d скачанных файлов и файлы будут пропущены [%s]"
					% (len(new_list), str(datetime.now())),
				)  # debug_length_for_current_jobs(yes)
			# write_log("debug new_list[yes]", "Найдено %d скачанных файлов и файлы будут пропущены [%s]" % (len(new_list), str(datetime.now()))) # length_for_current_jobs(yes)
		elif not new_list:
			print(
				Style.BRIGHT
				+ Fore.GREEN
				+ "Не найдено скачанных файлов и файлы будут переименованы [%s]"
				% str(datetime.now())
			)

			# lfiles = sorted(new_list, key=len, reverse=False) # is_need(no_debug)

			write_log(
				"debug new_list[no]!",
				"Не найдено скачанных файлов и файлы будут переименованы [%s]"
				% str(datetime.now()),
			)  # debug_length_for_current_jobs(no)
		# write_log("debug new_list[no]", "Не найдено скачанных файлов и файлы будут переименованы [%s]" % str(datetime.now())) # length_for_current_jobs(no)

	if all((lfiles, filter_dict, not new_list)):  # rename_if_no_skip_list
		try:
			# filter_dict2 = {v.strip():crop_filename_regex.sub("", lf.split("\\")[-1]).strip() for k, v in filter_dict.items() for lf in filter(lambda x: x, tuple(lfiles)) if all((v.lower().strip() == crop_filename_regex.sub("", lf.split("\\")[-1]).lower().strip(), v.strip() != crop_filename_regex.sub("", lf.split("\\")[-1]).strip()))} # short_and_diff_reg
			# filter_dict2 = {lf.strip():"".join(["\\".join([k, v]), str("".join(crop_filename_regex.findall(lf.split("\\")[-1])[0])).split(".")[0], ".", lf.split("\\")[-1].split(".")[-1]]) for k, v in filter_dict.items() for lf in filter(lambda x: x, tuple(lfiles)) if all((v.lower().strip() == crop_filename_regex.sub("", lf.split("\\")[-1]).lower().strip(), v.strip() != crop_filename_regex.sub("", lf.split("\\")[-1]).strip()))} # two_disk_drive_letters
			filter_dict2 = {
				lf.strip(): "".join(
					[
						"\\".join(["\\".join(lf.split("\\")[:-1]), v]),
						str(
							"".join(crop_filename_regex.findall(lf.split("\\")[-1])[0])
						).split(".")[0],
						".",
						lf.split("\\")[-1].split(".")[-1],
					]
				)
				for k, v in filter_dict.items()
				for lf in filter(lambda x: x, tuple(lfiles))
				if all(
					(
						v.lower().strip()
						== crop_filename_regex.sub("", lf.split("\\")[-1])
						.lower()
						.strip(),
						v.strip()
						!= crop_filename_regex.sub("", lf.split("\\")[-1]).strip(),
					)
				)
			}  # one_disk_drive_letter
		except BaseException as e:
			filter_dict2 = {}

			write_log(
				"debug filter_dict[error]",
				"[%s] [%s]" % (str(e), str(datetime.now())),
				is_error=True,
			)

		if filter_dict2:

			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ "Есть различия в именах файлов или похожие названия, фильтр запущен..."
			)
			write_log(
				"debug different[filter_dict][yes]",
				"Есть различия в именах файлов или похожие названия, фильтр запущен [%s]"
				% str(datetime.now()),
			)

			# filter_by_length # pass_1_of_2

			try:
				for k, v in filter_dict2.items():

					try:
						assert (
							filter_dict2
						), "Пустой словарь filter_dict2"  # is_assert_debug
					except AssertionError as err:  # if_null
						logging.warning("Пустой словарь filter_dict2")
						raise err
						break
					except BaseException as e:  # if_error
						logging.error("Пустой словарь filter_dict2 [%s]" % str(e))
						break

					try:
						fname1 = k.split("\\")[-1].strip()
					except:
						fname1 = ""

					try:
						fname2 = v.split("\\")[-1].strip()
					except:
						fname2 = ""

					diff_dict: dict = {}
					count1: int = 0

					if all((fname1, fname2, len(fname1) == len(fname2))):

						for s1 in range(len(fname1)):  # index_string1
							for s2 in range(len(fname2)):  # index_string2

								if s1 == s2:
									diff_dict[fname1[s1].strip()] = fname2[s2].strip()

						if diff_dict:

							for k2, v2 in diff_dict.items():  # count_equal_symbols

								if k2 == v2:
									count1 += 1

						if all(
							(count1, k, (count1 / len(k)) * 100 > 0, diff_dict)
						):  # if_not_null
							print(
								"Source string: %s" % "".join(list(diff_dict.keys())),
								"Destonation string: %s"
								% "".join(list(diff_dict.values())),
							)
							write_log(
								"debug diff_dict[src]",
								"Source string: %s" % "".join(list(diff_dict.keys())),
							)
							write_log(
								"debug diff_dict[dst]",
								"Destonation string: %s"
								% "".join(list(diff_dict.values())),
							)
							# dst -> src # true_autorename_filter
					else:
						continue
			except BaseException as e:
				write_log("debug diff_dict[pass1]", "%s" % str(e), is_error=True)

			# differense_register # pass_2_of_2

			try:
				for k, v in filter_dict2.items():

					try:
						assert (
							filter_dict2
						), "Пустой словарь filter_dict2"  # is_assert_debug
					except AssertionError as err:  # if_null
						logging.warning(
							"Пустой словарь filter_dict2 [%s]" % str(datetime.now())
						)
						raise err
						break
					except BaseException as e:  # if_error
						logging.error(
							"Пустой словарь filter_dict2 [%s] [%s]"
							% (str(e), str(datetime.now()))
						)
						break

					# Надо заменить c:\downloads\new\Reginald_the_Vampire_01s07e.mp4 на c:\downloads\new\Reginald_The_Vampire_01s07e.mp4 # write_log
					# Надо заменить c:\...\Reginald_the_Vampire_01s07e.mp4 на c:\...\Reginald_The_Vampire_01s07e.mp4 # print

					if (
						fspace(k, v) and k.split("\\")[:-1] == v.split("\\")[:-1]
					):  # fspace(ok) # equal_folder
						try:
							print(
								Style.BRIGHT
								+ Fore.YELLOW
								+ "Надо заменить %s на %s" % (full_to_short(k), v)
							)  # is_color
							move(k, v)  # no_async_if_"big"
						except:
							pass  # continue
						else:
							write_log(
								"debug filter_dict[move]!",
								"Будет заменён %s на %s" % (k, v),
							)  # debug/test # only_here
							MyNotify(
								txt=f"Будет заменён {k} на {v}", icon=icons["moved"]
							)
			except BaseException as e:
				write_log("debug diff_dict[pass2]", "%s" % str(e), is_error=True)

		elif not filter_dict2:
			print(
				Style.BRIGHT
				+ Fore.GREEN
				+ "Нет различий в именах файлов или известных фильтров, фильтр пропущен..."
			)
			write_log(
				"debug different[filter_dict][no]",
				"Нет различий в именах файлов или известных фильтров, фильтр пропущен [%s]"
				% str(datetime.now()),
			)

	write_log("debug end[true_project_rename]", "%s" % str(datetime.now()))


# (2914 // 3600, (2914 // 60) % 60, 2914 % 60) # (0, 48, 34)
async def hh_mm_ss(legth: int = 0) -> str:  # 5

	try:
		assert (
			length
		), f"Не указано сколько время ms надо конвертировать @hh_mm_ss/{length}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(
			"Не указано сколько время ms надо конвертировать @hh_mm_ss/length [%s]"
			% str(datetime.now)
		)
		raise err
		return (0, 0, 0, False)
	except BaseException as e:  # if_error
		logging.error(
			"Ну указано сколько время ms надо конвертировать @hh_mm_ss/length [%s] [%s]"
			% (str(e), str(datetime.now()))
		)
		return (0, 0, 0, False)

	try:
		val1 = length // 3600  # >>> 2914 // 3600 # 0 # hh
	except:
		val1 = 0

	try:
		val2 = (length // 60) % 60  # >>> (2914 // 60) % 60 # 48 # mm
	except:
		val2 = 0

	try:
		val3 = length % 60  # >>> 2914 % 60 # 34 # ss
	except:
		val3 = 0

	if all((not val1, not val2, not val3)):  # if_error_or_null
		return (0, 0, 0, False)

	if any((val1, val2, val3)):
		return (val1, val2, val3, True)  # hour_and_minute_and_seconds


def some_formula(filename, is_log: bool = True):  # 2
	return


# @log_error
async def filter_from_list(lst: list = []) -> list:  # files -> current_files + base #5

	temp: list = []
	some_files: list = []

	try:
		assert lst, "Пустой список @filter_from_list/lst"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(
			"Пустой список @filter_from_list/lst [%s]" % str(datetime.now())
		)
		raise err
		return temp
	except BaseException as e:  # if_error
		logging.error(
			"Пустой список @filter_from_list/lst [%s] [%s]"
			% (str(e), str(datetime.now()))
		)
		return temp

	# load_meta_jobs(filter) #4
	try:
		with open(some_base, encoding="utf-8") as sbf:
			somebase_dict = json.load(sbf)
	except:
		somebase_dict = {}

		with open(some_base, "w", encoding="utf-8") as sbf:
			json.dump(somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True)
	finally:
		some_files = [*somebase_dict] if somebase_dict else []  # is_no_lambda

	some_files = (
		some_files[0:1000] if len(some_files) >= 1000 else some_files
	)  # no_limit(if_hide) # (1)

	short_list: list = []
	keyword_list: list = []

	# need_shorts_to_list(upgrade)
	try:
		# short_list = [crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))] # equal
		# short_list: list = [crop_filename_regex.sub("", sm.split("\\")[-1]).split("_")[0].strip() if sm.split("\\")[-1].count("_") > 0 else crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))]  # match_or_equal # only_first
		for sm in filter(lambda x: os.path.exists(x), tuple(some_files)):
			try:
				keyword_list = sm.split("\\").split("_")[
					0 : sm.count("_")
				]  # is_tv_series_without_seasepis(is_big_cinema_without_year) # is_skip_last_group_tempalte
			except:
				continue
			else:
				if keyword_list:
					short_list += keyword_list[0]
	except:
		short_list: list = []
	else:
		if short_list:
			tmp: list = []

			tmp = list(
				set([sl.strip() for sl in short_list if sl])
			)  # need_only_upper_or_bum #  if len(sl) > 1 # short_by_length
			short_list = sorted(tmp, reverse=False)

	tmp = list(
		set(
			[
				sl.strip()
				for sl in filter(
					lambda x: any((x[0] == x[0].isalpha(), x[0] == x[0].isnumeric())),
					tuple(short_list),
				)
			]
		)
	)

	short_list = sorted(tmp, reverse=False)  # sort_by_string
	# short_list = sorted(tmp, key=len, reverse=False) # sort_by_length

	try:
		filter_list: list = list(
			set(
				[
					l.strip()
					for l in filter(lambda x: os.path.exists(x), tuple(lst))
					for sl in filter(lambda y: y, tuple(short_list))
					if all((l, sl, l.split("\\")[-1].startswith(sl)))
				]
			)
		)  # exists/short_template/start_with_template
	except:
		filter_list: list = []
	finally:
		filter_list.sort(reverse=False)  # sort_by_string
		# filter_list.sort(key=len, reverse=False) # sort_by_length

	return filter_list


def ms_to_time(ms: int = 0, mn: int = 60) -> int:
	try:
		h: int = ms // 3600
		m: int = ms % 3600 // 60
		s: int = ms % 3600 % 60
		assert any(
			(h, m, s)
		), f"Нет какой-то величины времени @hms/{h}/{m}/{s}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Нет какой-то величины времени @hms/%d" % ms)
		raise err

	try:
		assert isinstance(h, int) and isinstance(m, int) and isinstance(s, int), ""
	except AssertionError:
		h, m, s = int(h), int(m), int(s)

	try:
		ms_time = (h * 3600) + (m * 60) + s
	except:
		ms_time = 0

	return ms_time


if __name__ == "__main__":  # debug/test(need_pool/thread/multiprocessing/queue)
	asyncio.run(project_done())  # after_jobs_finish # update_project(some_ready/all)
	asyncio.run(update_bigcinema())  # update_cinema
	asyncio.run(project_update())  # updates(if_downloaded)
	# true_project_rename(folder=copy_src); true_project_rename() # check_and_rename
	asyncio.run(true_project_rename())  # check_and_rename

	# debug
	# exit()
	# '''

	lfiles: list = []

	# recovery/project/args/"last_jobs"(is_optimized) # filter4
	filter1: list = []  # recovery_base(full)
	filter2: list = []  # short_filenames(full)
	filter3: list = []  # args
	filter4: list = []  # ready_projects
	filter5: list = []  # ?desc

	need_find_all: bool = False
	need_find_period: bool = False

	# pass_1_of_4(recovery/is_jobs_backup)
	try:
		with open(
			files_base["backup"], encoding="utf-8"
		) as bjf:  # read_recovery_base(if_new_no_jobs)
			backup_list = bjf.readlines()  # try_read_from_file
	except BaseException as e:
		backup_list: list = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
	finally:

		try:
			filter1: list = list(
				set(
					[
						crop_filename_regex.sub("", f.split("\\")[-1]).strip()
						for f in filter(lambda x: os.path.exists(x), tuple(backup_list))
						if f
					]
				)
			)  # filenames_from_backup # equal(full)
		except:
			filter1 = []
		finally:
			filter1.sort(reverse=False)  # recovery_files # sort_by_string
			# filter1.sort(key=len, reverse=False)  # recovery_files # sort_by_length

		if filter1:
			logging.info("@filter1 %s" % ";".join(filter1))

			print(
				Style.BRIGHT
				+ Fore.CYAN
				+ "Надо обработать файлов: [%d], шаблон: [%s], последнее восстановление: [%s]"
				% (len(filter1), ",".join(filter1), str(datetime.now()))
			)
			write_log(
				"debug recovery[have]",
				"Надо обработать файлов: [%d], шаблон: [%s], последнее восстановление: [%s]"
				% (len(filter1), ",".join(filter1), str(datetime.now())),
			)

			if filter1:
				if len(filter1) >= 20:
					print(
						Style.BRIGHT
						+ Fore.YELLOW
						+ "Проход 1 из 4 [%s]" % ", ".join(filter1[0:20])
					)
					write_log("debug filter1[list]", ",".join(filter1[0:20]))
				elif len(filter1) < 20:
					print(
						Style.BRIGHT
						+ Fore.YELLOW
						+ "Проход 1 из 4 [%s]" % ", ".join(filter1[0 : len(filter1)])
					)
					write_log(
						"debug filter1[list]", ",".join(filter1[0 : len(filter1)])
					)

				# write_log("debug files[filter1]", "Найдены файлы с шаблоном 1 [%d][%s]" % (len(filter1), str(datetime.now())))
				write_log(
					"debug files[filter1]",
					"Найдены файлы с шаблоном 1 [%s][%s]"
					% ("|".join(filter1), str(datetime.now())),
				)
			else:
				write_log(
					"debug files[filter1][null]",
					"Не найдены файлы с шаблоном 1 [%s]" % str(datetime.now()),
				)

		elif not filter1:
			write_log(
				"debug recovery[none]",
				"Нет данных по фильтру 1 [%s]" % str(datetime.now()),
			)

		# @another_time_no_clean_backup
		dt = datetime.now()

		if all(
			(
				mytime["jobtime"][0] <= dt.hour <= mytime["jobtime"][1],
				dt.weekday() <= mytime["jobtime"][2],
			)
		):  # check_and_filter_by_job_time
			if backup_list:  # clear_if_backup_loaded # check_jobs_from_backup
				open(files_base["backup"], "w", encoding="utf-8").close()

	# pass_2_of_4(project/is_new_jobs/is_no_moved) # short_names_in_local_project
	try:
		short_files = os.listdir(path_for_folder1)
	except BaseException as e:
		short_files = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))

	# generate_short_filenames
	try:
		filter2 = [
			crop_filename_regex.sub("", f).strip()
			for f in filter(lambda x: x, tuple(short_files))
		]  # equal
		# filter2 = list(set([crop_filename_regex.sub("", f.split("\\")[-1]).split("_")[0].strip() if f.split("\\")[-1].count(
		# "_") > 0 else crop_filename_regex.sub("", f.split("\\")[-1]).strip() for f in
		# filter(lambda x: x, tuple(short_files))]))  # match_or_equal
	except:
		filter2 = []

	# '''
	# crop_filename_regex.sub("", f).strip()split("_")[0:crop_filename_regex.sub("", f).count("_")]
	# crop_filename_regex.sub("", f).strip().split("_")

	sym_or_num_regex = re.compile(
		r"([A-Z]{1,}|[0-9]{1,})", re.M
	)  # Abc -> [A] # aBc -> [B] # aBC -> [BC] # a1B -> [1, B]
	# sym_regex = re.compile(r"[A-Z]{1,}", re.M) # Abc -> [A] # aBc -> [B] # aBC -> [BC]

	filter_split: list = []

	try:
		for f in filter(
			lambda x: sym_or_num_regex.findall(x), tuple(filter2)
		):  # filter(lambda x: sym_regex.findall(x), tuple(filter2))
			# filter_split.extend(f.strip().split("_")[0:f.count("_")]) # type1
			filter_split.extend(f.strip().split("_"))  # type2
	except:
		filter_split = []
	finally:
		filter2 = list(set(filter_split))
	# '''

	filter2.sort(reverse=False)  # sort_by_string
	# filter2.sort(key=len, reverse=False) # sort_by_length

	if filter2:
		logging.info("@filter2 %s" % ";".join(filter2))

		print(Style.BRIGHT + Fore.GREEN + "Файлы проекта готовы к обработке")
		write_log("debug files[local]", "Файлы проекта готовы к обработке")

		print(Style.BRIGHT + Fore.WHITE + "%s" % ",".join(filter2))

		if filter2:
			if len(filter2) >= 20:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Проход 2 из 4 [%s]" % ", ".join(filter2[0:20])
				)
				write_log("debug filter2[list]", ",".join(filter2[0:20]))
			elif len(filter2) < 20:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Проход 2 из 4 [%s]" % ", ".join(filter2[0 : len(filter2)])
				)
				write_log("debug filter2[list]", ",".join(filter2[0 : len(filter2)]))

			# write_log("debug files[filter2]", "Найдены файлы с шаблоном 2 [%d][%s]" % (len(filter2), str(datetime.now())))
			write_log(
				"debug files[filter2]",
				"Найдены файлы с шаблоном 2 [%s][%s]"
				% ("|".join(filter2), str(datetime.now())),
			)
		else:
			write_log(
				"debug files[filter2][null]",
				"Не найдены файлы с шаблоном 2 [%s]" % str(datetime.now()),
			)

	elif not filter2:
		write_log(
			"debug project[none]", "Нет данных по фильтру 2 [%s]" % str(datetime.now())
		)

	# pass_3_of_4(args)
	try:
		my_arg_filter = asyncio.run(my_args())
	except BaseException as e:
		my_arg_filter = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))

	try:
		filter3 = sorted(
			list(set(my_arg_filter)), reverse=False
		)  # template_from_cmd_args # sort_by_string
		# filter3 = sorted(list(set(my_arg_filter)), key=len, reverse=False)  # template_from_cmd_args # sort_by_length
	except:
		filter3 = []
	else:
		filter_set3 = set()

		# get_all_unique_words # pass_1_of_2
		for maf in filter(lambda x: x, tuple(my_arg_filter)):
			if maf.count("_") > 0:
				filter_set3 = set(
					crop_filename_regex.sub("", maf).split("_")
				)  # have_delims_but_not_sort
			elif maf.count("_") == 0 and all((maf, not maf in filter_set3)):
				filter_set3.add(maf)  # no_delims_but_not_sort

		# try_delete_lang_and_find_sym_or_num(regex) # pass_2_of_2
		# """
		skip_lang_regex = re.compile(
			r"([A-Z]{1}[a-z]{2})$", re.M
		)  # txt = "Hello_Rus"; print(skip_lang_regex.findall(txt)) # [Rus]
		sym_or_num_regex = re.compile(
			r"([A-Z]{1,}|[0-9]{1,})", re.M
		)  # Abc -> [A] # aBc -> [B] # aBC -> [BC] # a1B -> [1, B]

		filter_new = [
			f.strip()
			for f in filter(
				lambda x: not skip_lang_regex.findall(x), tuple(filter_set3)
			)
			if sym_or_num_regex.findall(f)
		]

		if all((filter_new, len(filter_new) < len(filter_set3))):
			filter_set3 = set(filter_new)

		# """

		filter3 = list(filter_set3)

	filter3.sort(reverse=False)  # sort_by_string
	# filter3.sort(key=len, reverse=False) # sort_by_length

	if filter3:
		logging.info("@filter3 %s" % ";".join(filter3))

		if filter3:
			if len(filter3) >= 20:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Проход 3 из 4 [%s]" % ", ".join(filter3[0:20])
				)
				write_log("debug filter3[list]", ",".join(filter3[0:20]))
			elif len(filter3) < 20:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Проход 3 из 4 [%s]" % ", ".join(filter3[0 : len(filter3)])
				)
				write_log("debug filter3[list]", ",".join(filter3[0 : len(filter3)]))

			# write_log("debug files[filter3]", "Найдены файлы с шаблоном 3 [%d][%s]" % (len(filter3), str(datetime.now())))
			write_log(
				"debug files[filter3]",
				"Найдены файлы с шаблоном 3 [%s][%s]"
				% ("|".join(filter3), str(datetime.now())),
			)
		else:
			write_log(
				"debug files[filter3][null]",
				"Не найдены файлы с шаблоном 3 [%s]" % str(datetime.now()),
			)

	# my_arg_filter = [] # clean_if_some_data # debug/test

	elif not filter3:
		write_log(
			"debug args[none]", "Нет данных по фильтру 3 [%s]" % str(datetime.now())
		)

	# pass_4_of_4(is_ready_files)

	proj_files: list = []

	try:
		proj_list = os.listdir(path_to_done)
	except:
		proj_list = []

	try:
		if proj_list:
			proj_files = [
				"".join([path_to_done, pl])
				for pl in proj_list
				if os.path.exists("".join([path_to_done, pl]))
				and video_ext_regex.findall(pl)
				and all(
					(
						pl.count(".") == 1,
						not pl.split(".")[-1].lower()
						in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"],
					)
				)
			]  # only_normal(files_by_tempate)
	except BaseException as e:
		proj_files = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
		write_log("debug proj_files[filter4][error]", "%s" % str(e), is_error=True)

	if proj_files:
		# shorts_in_list(upgrade)
		# tmp = list(set([crop_filename_regex.sub("", pf.split("\\")[-1]).strip() for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))])) # equal
		tmp = list(
			set(
				[
					crop_filename_regex.sub("", pf.split("\\")[-1])
					.split("_")[0]
					.strip()
					if pf.split("\\")[-1].count("_") > 0
					else crop_filename_regex.sub("", pf.split("\\")[-1]).strip()
					for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))
				]
			)
		)  # match_or_equal

		filter4 = sorted(tmp, reverse=False)  # sort_by_string
		# filter4 = sorted(tmp, key=len, reverse=False) # sort_by_length

	filter4.sort(reverse=False)  # sort_by_string
	# filter4.sort(key=len, reverse=False) # sort_by_length

	if filter4:
		logging.info("@filter4 %s" % ";".join(filter4))

		if filter4:
			if len(filter4) >= 20:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Проход 4 из 4 [%s]" % ", ".join(filter4[0:20])
				)
				write_log("debug filter4[list]", ",".join(filter4[0:20]))
			elif len(filter4) < 20:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Проход 4 из 4 [%s]" % ", ".join(filter4[0 : len(filter4)])
				)
				write_log("debug filter4[list]", ",".join(filter4[0 : len(filter4)]))

			# write_log("debug files[filter4]", "Найдены файлы с шаблоном 4 [%d][%s]" % (len(filter4), str(datetime.now())))
			write_log(
				"debug files[filter4]",
				"Найдены файлы с шаблоном 4 [%s][%s]"
				% ("|".join(filter4), str(datetime.now())),
			)
		else:
			write_log(
				"debug files[filter4][null]",
				"Не найдены файлы с шаблоном 4 [%s]" % str(datetime.now()),
			)

	# filter5 # desc

	if any((filter1, filter2, filter3, filter4)):  # filter5

		print(
			Style.BRIGHT
			+ Fore.YELLOW
			+ "Выбран какой-то из шаблонов для обработки файлов"
		)
		write_log(
			"debug filter[1234]", "Выбран какой-то из шаблонов для обработки файлов"
		)

		# add_templates
		if filter1:
			filter_list += filter1  # recovery(add) # is_sort_by_key(1)

		if filter2:
			filter_list += filter2  # project(add) # is_sort_by_key(2)

		if filter3:
			filter_list += filter3  # from_args(add) # is_sort_by_key(3)

		if filter4:
			filter_list += filter4  # from_ready_jobs(add) # is_sort_by_key(4)

		# if filter5:
		# filter_list += filter5  # ? # is_sort_by_key(5)

		true_sym = re.compile(
			r"([^A-ZА-Я\d\-\_])", re.I
		)  # 2_Broke_Girls # 9-1-1_Lone_Star
		new_filter_set = set()
		new_filter: list = []

		try:
			for fl in filter(
				lambda x: len(x) >= 2, tuple(filter_list)
			):  # optimal_length_short_template # default(all)
				st = fl
				for ss in true_sym.findall(fl):
					if all((st, ss, ss in st)):  # skip_syms_in_filter_list
						st = (
							st.replace(" ", "_").replace(ss, "").strip()
						)  # replace_whitespac(other_clean)
						if all((st, not st in new_filter)):  # one_record
							new_filter.append(st)  # if_no_logic_save_with_dublicate
		except BaseException as e:
			new_filter = []
			print(Style.BRIGHT + Fore.RED + "%s" % str(e))  # upgrade(filter_list)
			write_log(
				"debug new_filter[error]", "[%s] [%s]" % (str(e), str(datetime.now()))
			)
		else:
			if all((new_filter, filter_list)):  # add_renamed_filter_data
				filter_list += list(set(new_filter))
			elif all((new_filter, not filter_list)):  # use_renames_filter_data
				filter_list = new_filter

			print("%s" % ";".join(list(set(filter_list))))  # upgrade(filter_list)
			write_log(
				"debug new_filter",
				"%s [%s]" % (";".join(list(set(filter_list))), str(datetime.now())),
			)  # logging_for_debug

		if filter_list:
			temp_list = sorted(filter_list, reverse=False)  # abc # type1
			# temp_list = sorted(filter_list, key=len, reverse=False)  # sort_by_key # type2
			# temp_list = filter_list # no_sort # type3

			filter_list = list(set(temp_list))  # unique_list
		else:
			print(
				"Пустой фильтр или короткий фильтр для обработки [%s]"
				% str(datetime.now())
			)
			write_log(
				"debug filter_list[None]",
				"Пустой фильтр или короткий фильтр для обработки [%s]"
				% str(datetime.now()),
			)
			exit()

		# default_short_names_without_slice
		tmp = [
			fl.strip() for fl in filter_list if all((len(fl) >= 2, fl != "''"))
		]  # skip_null_filter
		filter_list = tmp if tmp else []  # is_no_lambda

		# slice_by_short_names # @filter_list # combine_jobs_filter_by_short_names
		# tmp = ["Hello", "World", "9-1-1", "test", "Test_world"] # ["Hello", "World", "9-1-1", "Test"]

		# shorts_in_list(upgrade)
		temp = list(
			set(
				[
					t.strip().split("_")[0] if len(t.split("_")) > 0 else t.strip()
					for t in tmp
				]
			)
		)  # use_first_word_or_one_word # is_no_lambda
		temp2 = list(
			set(
				[
					t.strip()
					for t in filter(lambda x: x, tuple(temp))
					if any((t.title().startswith(t[0]), t[0].isnumeric()))
				]
			)
		)  # compare_first_symb_by_capitalize

		if temp2:
			filter_list = sorted(temp2, reverse=False)  # sort_by_string
			# filter_list = sorted(temp2, key=len, reverse=False) # sort_by_length

		fl_count = str(len(filter_list)) if filter_list else "All"  # is_no_lambda

		if filter_list:
			if len(filter_list) >= 20:  # first_20_short_templates
				print(fl_count, filter_list[0:20], end="\n")  # length / list(20)
			elif len(filter_list) < 20:
				print(fl_count, filter_list, end="\n")  # length / list(full)

			write_log("debug filter_list", ";".join(filter_list))  # current(1) # full
		else:
			write_log(
				"debug filter_list[null][combine]",
				"Нет фильтра для поиска [%s]" % str(datetime.now()),
			)

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))$", re.M) # _[\d+]{2}p

		# load_meta_jobs(filter) #6
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(
					somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)
		finally:
			some_files = [*somebase_dict] if somebase_dict else []  # is_no_lambda

		some_files = (
			some_files[0:1000] if len(some_files) >= 1000 else some_files
		)  # no_limit(if_hide) # (2)

		if filter_list:  # some_template
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap|^.srt))$"
				% "|".join(filter_list),
				re.M,
			)  # M(atch)/I(gnore)_case # by_filter
			need_find_all = True
		elif not filter_list:  # no_template
			# if not some_files:
			# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M) # M(atch)/I(gnore)_case # season(year) # _[\d+]{2}p
			if some_files:  # elif -> if
				filt = sorted(
					list(
						set(
							[
								crop_filename_regex.sub("", sm.split("\\")[-1]).strip()
								for sm in filter(
									lambda x: os.path.exists(x), tuple(some_files)
								)
							]
						)
					),
					key=len,
					reverse=False,
				)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$"
					% "|".join(filt),
					re.M,
				)  # M(atch)/I(gnore)_case # by_filter_base

			need_find_period = True

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine
				nlf = e.submit(
					sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex
				)  # nlocal # serialy
				nlf2 = e.submit(
					sub_folder, "d:\\multimedia\\video\\serials_europe\\", video_regex
				)  # nlocal # serialy_rus
				nlf3 = e.submit(
					sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex
				)  # nlocal # filmy
				# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
				# nlf5 = e.submit(sub_folder, "d:\\multimedia\\video\\", temp_regex) # temporary_files
				# nlf6 = e.submit(sub_folder, "d:\\multimedia\\video\\documental\\", video_regex) # documental_files

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()
			# lfiles += nlf5.result()
			# lfiles += nlf6.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine

			lfiles = lf.result()

		try:
			# short_files = list(short_files_gen()) # new(yes_gen)
			short_files: list = list(
				set(
					[
						crop_filename_regex.sub("", lf.split("\\")[-1]).strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if all(
							(
								lf,
								lf.count(".") == 1,
								video_regex.findall(lf.split("\\")[-1]),
							)
						)
					]
				)
			)
		except:
			short_files: list = []
		else:
			if short_files:

				short_files.sort(
					reverse=False
				)  # re_sorted_before_save # sort_by_string
				# short_files.sort(key=len, reverse=False) # re_sorted_before_save # sort_by_length

				# a = ["11", "222", "3", "44"]

				# sorted(a, key=len, reverse=False) # ['3', '11', '44', '222'] # abc_by_values
				# sorted(a, key=len, reverse=True) # ['222', '11', '44', '3'] # cbc_by_values

				# sorted(a, reverse=False) # ['11', '222', '3', '44'] # abc_by_string
				# sorted(a, reverse=True) # ['44', '3', '222', '11'] # cbc_by_string

				try:
					with open(short_folders, encoding="utf-8") as sff:
						sfl = sff.readlines()
				except:
					sfl = []

				with unique_semaphore:
					for sf in filter(
						lambda x: len(x.strip()) >= 2, tuple(short_files)
					):  # short_by_length(sf)
						if all((not sf in sfl, sf)):
							sfl.append(sf.strip())

				def short_files_gen(sfl=sfl):  # 3
					for s in filter(lambda x: x, tuple(sfl)):
						yield s.strip()

				if sfl:
					try:
						short_files = list(short_files_gen())  # new(yes_gen)
					# short_files = [s.strip() for s in filter(lambda x: x, tuple(sfl))]
					except:
						short_files = []

				temp = list(set(short_files))

				try:
					short_files: list = sorted(temp, reverse=False)  # sort_by_string
					# short_files: list = sorted(temp, key=len, reverse=False)  # sort_by_key
				except:
					short_files: list = []

				try:
					# tmp = list(temp_gen()) # new(yes_gen)
					tmp: list = list(
						set(
							[
								sf.strip()
								for lf in filter(
									lambda x: os.path.exists(x), tuple(lfiles)
								)
								for sf in tuple(short_files)
								if all((lf, sf, lf.split("\\")[-1].startswith(sf)))
							]
						)
					)
				except:
					tmp: list = []
				finally:
					short_files = (
						sorted(list(set(tmp)), reverse=False) if tmp else []
					)  # re_sorted_before_save(by_string) # is_no_lambda
					# short_files = sorted(tmp2, key=len, reverse=False) if tmp2 else []  # re_sorted_before_save(by_length)

				if short_files:  # save_if_some_list
					with open(short_folders, "w", encoding="utf-8") as sff:
						sff.writelines(
							"%s\n" % sf.strip()
							for sf in filter(lambda x: x, tuple(short_files))
						)  # current_folders(short)

					try:
						copy(short_folders, copy_folders)  # copy_list_to_list
					except:
						open(
							files_base["current"], "w", encoding="utf-8"
						).close()  # if_error_null_list
					else:
						write_log("debug shortfiles[filter]", "|".join(short_files))

				elif not short_files:  # save_if_some_list
					write_log(
						"debug shortfiles[filter]",
						"No_short_files at [%s]" % str(datetime.now()),
					)

			if not short_files:  # stop_if_no_files # temp(debug)
				logging.info("@no short_files[11643]")
				exit()

		filter_list: list = (
			list(set(short_files)) if short_files else []
		)  # is_no_lambda

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			write_log("debug files[filter]", "%s" % "|".join(filter_list))  # current(2)
			need_find_all = True
		elif not filter_list:
			need_find_period = True  # find_all_if_null_filter(period)

		# @clear_after_filter # clear_backup(after_filter/is_need_hidden)
		# open(files_base["backup"], "w", encoding="utf-8").close()

		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump(
				{}, fbf, ensure_ascii=False, indent=4, sort_keys=False
			)  # clear_jobs(after_filter) # is_need_hide(no_clean)

		with open(sfilecmd_base, "w", encoding="utf-8") as sbf:
			json.dump(
				{}, sbf, ensure_ascii=False, indent=4, sort_keys=False
			)  # clear_sort_jobs(after_filter) # is_need_hide(no_clean)

		# open(cfilecmd_base, "w", encoding="utf-8").close()  # clear_combinelist(after_filter) # hide_if_manual_run
		# open(path_for_queue + "another.lst", "w", encoding="utf-8").close() # is_csv(after_filter) # hide_if_not_need_another

	elif all((not filter1, not filter2, not filter3, not filter4)):

		some_files: list = []

		# load_meta_jobs(filter) #7
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(
					somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)
		finally:
			some_files: list = (
				[*somebase_dict] if somebase_dict else []
			)  # list(somebase_dict.keys()) # is_no_lambda

		some_files = (
			some_files[0:1000] if len(some_files) >= 1000 else some_files
		)  # no_limit(if_hide) # (3)

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))", re.M) # _[\d+]{2}p

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$"
				% "|".join(filter_list),
				re.M,
			)  # all_period
			need_find_all = True
		elif not filter_list:  # M(atch)/I(gnore)_case # seas(year)
			# if not some_files:
			# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M) # period_about_x_days # _[\d+]{2}p
			if some_files:  # elif -> if
				filt = sorted(
					list(
						set(
							[
								crop_filename_regex.sub("", sm.split("\\")[-1]).strip()
								for sm in filter(
									lambda x: os.path.exists(x), tuple(some_files)
								)
							]
						)
					),
					key=len,
					reverse=False,
				)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$"
					% "|".join(filt),
					re.M,
				)  # M(atch)/I(gnore)_case # by_filter_base

			need_find_period = True

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine
				nlf = e.submit(
					sub_folder, "e:\\multimedia\\video\\serials_conv\\", video_regex
				)  # nlocal # serialy
				nlf2 = e.submit(
					sub_folder, "e:\\multimedia\\video\\serials_europe\\", video_regex
				)  # nlocal # serialy_rus
				nlf3 = e.submit(
					sub_folder, "e:\\multimedia\\video\\big_films\\", video_regex
				)  # nlocal # filmy
				# nlf4 = e.submit(one_folder, "e:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
				# nlf5 = e.submit(one_folder, "e:\\multimedia\\video\\", temp_regex) # temporary_files # sub_folder -> one_folder
				# nlf6 = e.submit(sub_folder, "e:\\multimedia\\video\\documental\\", video_regex) # documental_files

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()
			# lfiles += nlf5.result()
			# lfiles += nlf6.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine

			lfiles = lf.result()

		try:
			# short_list = list(short_list_gen()) # new(yes_gen)
			short_list = list(
				set(
					[
						crop_filename_regex.sub("", lf.split("\\")[-1]).strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if all(
							(
								lf,
								2,
								lf.count(".") == 1,
								video_regex.findall(lf.split("\\")[-1]),
							)
						)
					]
				)
			)
		except:
			short_list = []

		if not short_list:  # stop_if_not_files # temp(debug)
			logging.info("@no short_list[11740]")
			exit()

		tmp: list = []
		tmp = list(
			set(
				[
					sl.strip()
					for sl in filter(lambda x: len(x.strip()) > 1, tuple(short_list))
				]
			)
		)  # short_by_length(sl)

		short_list = sorted(short_list, reverse=False)  # re_sort_before_by_string
		# short_list = sorted(tmp, key=len, reverse=False) # re_sort_before_by_length

		short_string = (
			"|".join(short_list) if len(short_list) > 1 else short_list[0]
		)  # is_no_lambda

		if short_string:
			short_regex = re.compile(r"^(%s)" % short_string)

			short_exists: list = []
			short_not_exists: list = []

			# delete_strings_when_no_exists_in_find_files(regex) # debug/test

			try:
				with open(short_folders, encoding="utf-8") as sff:
					sfl = sff.readlines()
			except:
				sfl: list = []

			for sl in filter(lambda x: x, tuple(sfl)):
				if all(
					(short_regex.findall(sl), short_string, sl)
				):  # filter_string_by_current_list(file)
					short_exists.append(sl)

			if short_exists:  # if_some
				short_list = [s.strip() for s in short_exists if s]
			elif not short_exists:  # if_null
				try:
					# short_exists = list(sl_gen()) # new(yes_gen)
					short_exists: list = [
						sl.strip()
						for sl in filter(lambda x: x, tuple(short_list))
						if all((short_regex.findall(sl), short_string, sl))
					]
				except:
					short_exists: list = []
				finally:
					short_list = sorted(short_exists, reverse=False)  # sort_by_string
					# short_list = sorted(short_exists, key=len, reverse=False) # sort_by_length

			open(
				short_folders, "w", encoding="utf-8"
			).close()  # clear_for_update # debug/test

			# use_only_include_files # debug/test
			temp = list(set(short_list))

			try:
				short_list = sorted(temp, reverse=False)  # True(cba) # False(abc)
				# short_list = sorted(temp, key=len, reverse=False)  # True(cba) # False(abc)
			except:
				short_list = []

			with open(short_folders, "w", encoding="utf-8") as sff:
				sff.writelines(
					"%s\n" % sf.strip() for sf in filter(lambda x: x, tuple(short_list))
				)  # current_folders(short)

			try:
				copy(short_folders, copy_folders)  # copy_list_to_list
			except:
				open(
					files_base["current"], "w", encoding="utf-8"
				).close()  # if_error_null_list
			else:
				write_log("debug shortfiles[job]", "|".join(short_list))

		filter_list = list(set(short_list)) if short_list else []  # is_no_lambda

		# default_short_names_without_slice
		tmp = [
			fl.strip() for fl in filter_list if all((len(fl) >= 2, fl != "''"))
		]  # skip_null_filter
		filter_list: list = tmp if tmp else []  # is_no_lambda

		# slice_by_short_names # @filter_list # find_jobs_filter_by_short_names
		# tmp = ["Hello", "World", "9-1-1", "test", "Test_world"] # ["Hello", "World", "9-1-1", "Test"]

		# shorts_in_list(upgrade)
		temp = list(
			set(
				[
					t.strip().split("_")[0] if len(t.split("_")) > 0 else t.strip()
					for t in tmp
				]
			)
		)  # use_first_word_or_one_word # is_no_lambda
		temp2 = list(
			set(
				[
					t.strip()
					for t in filter(lambda x: x, tuple(temp))
					if any((t.title().startswith(t[0]), t[0].isnumeric()))
				]
			)
		)  # compare_first_symb_by_capitalize

		if temp2:
			filter_list = sorted(temp2, reverse=False)  # sort_by_string
			# filter_list = sorted(temp2, key=len, reverse=False) # sort_by_length

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			write_log(
				"debug files[filter][-]", "%s" % "|".join(filter_list)
			)  # current(3)
			need_find_all = True
		elif not filter_list:
			need_find_period = True  # find_all_if_null_filter(period)

		fl_count = str(len(filter_list)) if filter_list else "All"  # is_no_lambda

		try:
			if len(filter_list) >= 20:
				print(
					fl_count, filter_list[0:20], end="\n"
				)  # count/filter # first_20_only
			elif all((filter_list, len(filter_list) < 20)):
				print(
					fl_count, filter_list[0 : len(filter_list)], end="\n"
				)  # count/filter # first_20_only
			else:
				write_log(
					"debug filter_list[null]",
					"Нет фильтра для поиска [%s]" % str(datetime.now()),
				)
		except:
			print("no index")

	# --- update_files ---

	try:
		lfiles: list = list(
			set(
				[
					lf.strip()
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
					if lf
				]
			)
		)
	except:
		lfiles: list = []
	finally:
		lfiles.sort(reverse=False)  # sort_by_string
		# lfiles.sort(key=len, reverse=False)  # sort_by_length

	if need_find_all:  # avg_days_to_full_period

		try:
			dbl = asyncio.run(days_by_list(lfiles))  # full_days
		except:
			dbl = 365  # full_year
		finally:
			write_log("debug dbl[need_find_all]", "%s" % str(dbl))

		is_any = True if dbl != 365 else False  # is_no_lambda

		try:
			temp = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if all(
							(
								lf,
								mdate_by_days(filename=lf, period=dbl, is_any=is_any)
								!= None,
							)
						)
					]
				)
			)  # filter_by_period(all_time/avg_time)
		except:
			temp = []
		finally:
			if isinstance(dbl, int) and dbl != None and temp:
				# write_log("debug files[avgdays]", "Дней: %d, найдено: %d" % (dbl, len(temp)))
				write_log("debug files[maxdays]", "Найдено: %d" % len(temp))

			lfiles = sorted(temp, reverse=False)

	elif need_find_period:
		try:
			dbl = asyncio.run(days_by_list(lfiles))  # full_days
		except:
			dbl = 365  # full_year
		finally:
			write_log("debug dbl[need_find_period]", "%s" % str(dbl))

		# every_30days
		try:
			dbl = (
				(dbl // 30) * 30 if dbl // 30 > 0 else 30
			)  # get_period_more_month_or_month # is_no_lambda
		except:
			dbl = 30

		is_any = True if dbl != 30 else False  # is_no_lambda

		try:
			temp = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if all(
							(
								lf,
								mdate_by_days(filename=lf, period=dbl, is_any=is_any)
								!= None,
							)
						)
					]
				)
			)  # filter_by_all_days
		except:
			temp = []
		finally:
			temp.sort(reverse=False)  # sort_by_string
			# temp.sort(key=len, reverse=False) # sort_by_length

		if temp:
			write_log(
				"debug files[allmonth]", "Найдено: %d" % len(temp)
			)  # allmonth(dbl >= 30)
		elif not temp:  # all_days_if_no_files_by_30days
			try:
				dbl = asyncio.run(days_by_list(lfiles))  # full_days
			except:
				dbl = 365  # full_year
			finally:
				write_log("debug dbl", "%d" % dbl)

			is_any = True if dbl != 365 else False  # is_no_lambda

			try:
				temp = list(
					set(
						[
							lf.strip()
							for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
							if all(
								(
									lf,
									mdate_by_days(
										filename=lf, period=dbl, is_any=is_any
									)
									!= None,
								)
							)
						]
					)
				)  # filter_by_all_days
			except:
				temp = []
			finally:
				temp.sort(reverse=False)  # sort_by_string
				# temp.sort(key=len, reverse=False)  # sort_by_length

			if temp:
				write_log(
					"debug files[alldays]", "Найдено: %d" % len(temp)
				)  # alldays(dbl > 0, 0 - current, 1 - other_days)

		tmp = list(set(temp))
		lfiles = sorted(tmp, reverse=False)

	if lfiles and any(
		(need_find_period, need_find_all)
	):  # filter_period(30_days/all_days)
		if need_find_all:
			write_log(
				"debug files[find]", "Найдены за весь период [%s]" % str(datetime.now())
			)
		elif need_find_period:
			write_log(
				"debug files[find]", "Найдены за месяц [%s]" % str(datetime.now())
			)

		date1 = datetime.now()

		unique = full_list = set()
		try:
			tmp: list = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if lf
					]
				)
			)
		except:
			tmp: list = []
		finally:
			lfiles = sorted(tmp, reverse=False)

		cnt: int = 0

		# find_avg_time_by_pass

		MM = MyMeta()  # 4

		length = list(
			set(
				[
					MM.get_length(lf)
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
					if lf
				]
			)
		)

		# async
		try:
			l_avg = asyncio.run(avg_lst(list(set(length))))
		except:
			l_avg = 0
		else:
			if l_avg:
				write_log("debug avgcalc[avg][1]", "%d" % l_avg)

		del MM

		MT = MyTime(seconds=2)

		"""
		try:
			h, m = asyncio.run(load_timing_from_xml(ind=2)) # 2 # h, m = load_timing_from_xml(ind=2)
		except:
			h, m = 0, 0
		"""

		date1 = datetime.now()

		with unique_semaphore:
			for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)):

				try:
					assert (
						lfiles
					), f"Пустой список или нет файлов {lf}"  # lfiles # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning(
						"Пустой список или нет файлов lfiles [%s]" % str(datetime.now())
					)
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой список или нет файлов lfiles [%s] [%s]"
						% (str(e), str(datetime.now()))
					)
					break

				cnt += 1

				date2 = datetime.now()

				hour = divmod(
					int(abs(date1 - date2).total_seconds()), 60
				)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(
						date1, date2
					)  # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				try:
					if len(hour) > 0:
						hour = hour[0] // 60
					assert bool(hour < 4), ""
				except BaseException:
					hour = 4
				except AssertionError:
					hour = 4

				write_log("debug hour[count][1]", "%d [lfiles]" % hh)  # is_index #1

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if (
					all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
				):  # stop_if_more_hour
					write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
					break

				try:
					fname = lf.split("\\")[-1].strip()
				except:
					fname = ""

				try:
					assert lf, ""
				except AssertionError:
					# if not lf:
					continue

				if all((not fname in unique, fname)) and os.path.exists(lf):
					unique.add(fname)  # short_file(first)_by_set
					full_list.add(lf)  # full_filename(first)_by_set

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)

		def files_to_short_by_full(lfiles=lfiles):  # 6
			for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)):
				if all((lf, crop_filename_regex.sub("", lf.split("\\")[-1]))):
					yield lf.strip()
				else:
					yield ""

		try:
			tmp: list = list(files_to_short_by_full())  # new(yes_gen)
		except:
			tmp: list = []
		finally:
			lfiles = sorted(tmp, reverse=False)  # sort_by_string
			# lfiles = sorted(tmp, key=len, reverse=False) # sort_by_length

	elif not lfiles:  # if -> elif

		# load_meta_jobs(filter) #8
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(
					somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)
		finally:
			some_files = (
				[*somebase_dict] if somebase_dict else []
			)  # list(somebase_dict.keys()) # is_no_lambda

		some_files = (
			some_files[0:1000] if len(some_files) >= 1000 else some_files
		)  # no_limit(if_hide) # (4)

		# shorts_in_list(upgrade)
		try:
			# filter_list = [crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))] # equal
			filter_list: list = [
				crop_filename_regex.sub("", sm.split("\\")[-1]).split("_")[0].strip()
				if sm.split("\\")[-1].count("_") > 0
				else crop_filename_regex.sub("", sm.split("\\")[-1]).strip()
				for sm in filter(lambda x: os.path.exists(x), tuple(some_files))
			]  # match_or_equal
		except:
			filter_list: list = []

		temp = list(set([f.strip() for f in filter(lambda x: x, tuple(filter_list))]))

		filter_list = sorted(temp, reverse=False)  # sort_by_string
		# filter_list = sorted(temp, key=len, reverse=False) # sort_by_length

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))", re.M) # _[\d+]{2}p

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$"
				% "|".join(filter_list),
				re.M,
			)
		elif not filter_list:  # M(atch)/I(gnore)_case # seas(year)
			# if not some_files:
			# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M) # _[\d+]{2}p
			if some_files:  # elif -> if
				filt = sorted(
					list(
						set(
							[
								crop_filename_regex.sub("", sm.split("\\")[-1]).strip()
								for sm in filter(
									lambda x: os.path.exists(x), tuple(some_files)
								)
							]
						)
					),
					key=len,
					reverse=False,
				)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$"
					% "|".join(filt),
					re.M,
				)  # M(atch)/I(gnore)_case # by_filter_base

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine
				nlf = e.submit(
					sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex
				)  # nlocal # serialy
				nlf2 = e.submit(
					sub_folder, "d:\\multimedia\\video\\serials_europe\\", video_regex
				)  # nlocal # serialy_rus
				nlf3 = e.submit(
					sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex
				)  # nlocal # filmy
				# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
				# nlf5 = e.submit(one_folder, "d:\\multimedia\\video\\", temp_regex) # temporary_files # sub_folder -> one_folder
				# nlf6 = e.submit(sub_folder, "d:\\multimedia\\video\\documental\\", video_regex) # documental_files

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()
			# lfiles += nlf5.result()
			# lfiles += nlf6.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine

			lfiles = lf.result()

		if not lfiles:  # stop_if_no_files # temp(debug)
			logging.info("@no lfiles[12128]")
			exit()

		if filter_list:
			tfilter_list = list(
				set([f.strip() for f in filter_list if f])
			)  # if len(f) > 1
			filter_list = tfilter_list if tfilter_list else []  # is_no_lambda

			write_log(
				"debug files[filter][reserved]", "%s" % "|".join(filter_list)
			)  # current(4)

		date1 = datetime.now()

		# no_backup(lfiles)
		unique = full_list = set()
		try:
			tmp: list = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if lf
					]
				)
			)
		except:
			tmp: list = []
		finally:
			lfiles = sorted(tmp, reverse=False)  # sort_by_string
			# lfiles = sorted(tmp, key=len, reverse=False) # sort_by_length

		cnt: int = 0

		MT = MyTime(seconds=2)

		"""
		try:
			h, m = asyncio.run(load_timing_from_xml(ind=3)) # 3 # h, m = load_timing_from_xml(ind=3)
		except:
			h, m = 0, 0
		"""

		date1 = datetime.now()

		with unique_semaphore:
			for lf in filter(lambda x: x, tuple(lfiles)):  # new(yes_gen)

				cnt += 1

				date2 = datetime.now()

				hour = divmod(
					int(abs(date1 - date2).total_seconds()), 60
				)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(
						date1, date2
					)  # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				try:
					if len(hour) > 0:
						hour = hour[0] // 60
					assert bool(hour < 4), ""
				except BaseException:
					hour = 4
				except AssertionError:
					hour = 4

				write_log("debug hour[count][2]", "%d [lfiles]" % hh)  # is_index #2

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >=h, mm >= m)) # all((hh > hour, mm >= m))
				if (
					all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
				):  # stop_if_more_hour
					write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
					break

				try:
					fname = lf.split("\\")[-1].strip()
				except:
					fname = ""
					continue

				if all((not fname in unique, fname)):
					unique.add(fname)  # short_file(first)_by_set
					full_list.add(lf)  # full_filename(first)_by_set

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)

		if filter_list:
			temp = [
				flst.strip()
				for fl in filter(lambda y: y, tuple(filter_list))
				for flst in filter(lambda x: os.path.exists(x), tuple(full_list))
				if all((fl, flst, fl in flst))
			]  # +filter
		elif not filter_list:
			temp = [
				flst.strip()
				for flst in filter(lambda x: os.path.exists(x), tuple(full_list))
				if all((flst, crop_filename_regex.sub("", flst.split("\\")[-1])))
			]  # default_filter

		lfiles = sorted(list(set(temp)), reverse=False)

	if not lfiles:  # exit_if_not_found_some_files
		exit()

	# --- (move/update)_files ---

	try:
		temp = list(
			set(
				[
					lf.strip()
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
					if lf
				]
			)
		)
	except:
		temp = []
	finally:
		lfiles = sorted(temp, reverse=False)  # sort_by_string
		# lfiles = sorted(temp, key=len, reverse=False)  # sort_by_length

	# new_or_update_jobs # pass_2_of_2(if_ok_move_and_update)
	lfiles_total: list = []

	if (
		any((len(os.listdir(copy_src)) > 0, len(os.listdir(copy_src2)) > 0))
		and os.path.exists(copy_src)
		and os.path.exists(copy_src2)
	):  # debug

		try:
			lfiles2 = [
				os.path.join(copy_src, lf).strip()
				for lf in os.listdir(copy_src)
				if all((lf, lf.count(".") == 1, crop_filename_regex.sub("", lf)))
			]  # if_short_ok(tv_series)
		except:
			lfiles2 = []
		finally:
			lfiles_total += lfiles2

		try:
			lfiles3 = [
				os.path.join(copy_src2, lf).strip()
				for lf in os.listdir(copy_src2)
				if all((lf, lf.count(".") == 1, crop_filename_regex.sub("", lf)))
			]  # if_short_ok(big_films)
		except:
			lfiles3 = []
		finally:
			lfiles_total += lfiles3

		# lt = ["c:\\downloads\\mytemp\\hello.file"]
		# ["\\".join(["\\".join(ltf.split("\\")[:-1]), ltf.split("\\")[-1]]) for ltf in lt] # ['c:\\downloads\\mytemp\\hello.file']

		try:
			lfiles_move = {
				"\\".join(
					["\\".join(lt.split("\\")[:-1]), lt.split("\\")[-1]]
				): "".join([path_for_folder1, lt.split("\\")[-1]]).strip()
				for lt in filter(lambda x: os.path.exists(x), tuple(lfiles_total))
				if lt
			}
		except:
			lfiles_move = {}
		else:
			if lfiles_move:

				print()

				processes_ram: list = []

				try:
					l = list(
						set(
							[
								os.path.getsize(lm)
								for lm in lfiles_move
								if os.path.exists(lm)
							]
						)
					)
				except:
					l = []

				try:
					s = reduce(lambda x, y: x + y, l)
				except:
					s = 0

				try:
					a = (lambda s, l: s // l)(s, len(l))
				except:
					a = 0

				# move_downloads_to_project
				for k, v in lfiles_move.items():

					if all((fspace(k, v), os.path.getsize(k))):

						if (
							all((os.path.getsize(k) <= a, a)) or not a
						):  # less_or_equal_avg_or_null

							write_log("debug move[files][thread]", ";".join([k, v]))

							print(
								Style.BRIGHT
								+ Fore.GREEN
								+ "Добавление в очередь файла",
								Style.BRIGHT + Fore.WHITE + "%s" % k,
							)  # add_to_all(process_move)

							try:
								asyncio.run(
									process_move(k, v, False, True, a)
								)  # no_await # async_if_small #5
							except BaseException as e:
								write_log(
									"debug process_move[error][5]",
									";".join([k, v, str(e)]),
								)
							else:
								write_log("debug process_move[ok][5]", ";".join([k, v]))

							if not k in processes_ram:
								processes_ram.append(k)

						elif all((os.path.getsize(k) > a, a)):  # more_avg

							move(k, v)  # no_async_if_big

							try:
								is_new = os.path.exists(k) and not os.path.exists(v)
							except:
								is_new = False

							try:
								is_update = os.path.exists(k) and os.path.exists(v)
							except:
								is_update = False

							if all((is_new, not is_update)):
								print(
									Style.BRIGHT + Fore.GREEN + "Файл",
									Style.BRIGHT + Fore.WHITE + "%s" % k,
									Style.BRIGHT
									+ Fore.YELLOW
									+ "надо записать проект в",
									Style.BRIGHT + Fore.CYAN + "%s" % v,
								)  # is_another_color
								write_log(
									"debug movefile[new]",
									"Файл %s надо записать проект в %s" % (k, v),
								)

							elif all((is_update, not is_new)):
								print(
									Style.BRIGHT + Fore.YELLOW + "Файл",
									Style.BRIGHT + Fore.WHITE + "%s" % k,
									Style.BRIGHT
									+ Fore.YELLOW
									+ "надо обновить проект в",
									Style.BRIGHT + Fore.CYAN + "%s" % v,
								)  # is_another_color
								write_log(
									"debug movefile[update]",
									"Файл %s надо обновить проект в %s" % (k, v),
								)

							write_log("debug move[files][normal]", ";".join([k, v]))

				# print(full_to_short(k), os.path.exists(k), full_to_short(v), os.path.exists(v), Style.BRIGHT + Fore.WHITE + "%s -> %s" % (k, v), end="\n")
				# write_log("debug lfiles_move", "%s" % ";".join([k, str(os.path.exists(k)), v, str(os.path.exists(v)), "%s -> %s" % (k, v)] ))

	# debug
	# exit()

	# add_or_update_projects(tv_series/big_cinema)
	try:
		lfiles_total: list = list(
			set(
				[
					os.path.join(path_for_folder1, lf).strip()
					for lf in os.listdir(path_for_folder1)
					if os.path.exists(os.path.join(path_for_folder1, lf).strip()) and lf
				]
			)
		)  # old(no_gen)
	except:
		lfiles_total: list = []

	if lfiles_total:

		# tmp = list(set([lt.strip() for lt in filter(lambda x: x, tuple(lfiles_total))])) # if_yes_gen

		lfiles_total = sorted(lfiles_total, reverse=False)  # re_sort_before_by_string
		# lfiles_total = sorted(lfiles_total, key=len, reverse=False) # re_sort_before_by_length

		try:
			tmp: list = list(
				set(
					[
						crop_filename_regex.sub("", lf.split("\\")[-1].strip())
						for lf in filter(
							lambda x: os.path.exists(x), tuple(lfiles_total)
						)
						if lf
					]
				)
			)
		except:
			tmp: list = []
		else:
			tmp = sorted(tmp, reverse=False)  # sort_by_string
			# tmp = sorted(tmp, key=len, reverse=False) # sort_by_length

			write_log("debug lfiles_total[projects]", "%s" % ";".join(tmp))

	tmp = list(set(lfiles_total))
	lfiles_total = sorted(tmp, reverse=False)

	# check_connect_if_no_users_in_my_smb(for_update) # is_here_overload # smbclient

	# move_tv_series(rus/eng) # ..\\video\\documental\\
	try:
		ff = asyncio.run(
			folders_filter(
				lst=lfiles_total, folder="d:\\multimedia\\video\\serials_conv\\"
			)
		)  # usa(english)
		ff2 = asyncio.run(
			folders_filter(
				lst=lfiles_total,
				folder="d:\\multimedia\\video\\serials_europe\\",
				is_Rus=True,
				is_Ukr=True,
			)
		)  # europe(rus/ukr/...)
	except BaseException as e:
		ff = ff2 = []  # null_if_some_error(no_drive/procedure_error)

		print(
			Style.BRIGHT
			+ Fore.RED
			+ "Нет файлов для переноса. Ошибка в скрипте [%s]" % str(e)
		)
		write_log(
			"debug move[need][error]",
			"Нет файлов для переноса. Ошибка в скрипте [%s]" % str(e),
			is_error=True,
		)
	else:
		temp: list = []
		temp2 = []  # default

		try:
			if ff:
				temp += ff
		except:
			temp = []

		try:
			if ff2:
				temp2 += ff2
		except:
			temp2 = []

		l1 = l2 = ff = []

		if temp:
			l1 = sorted(temp, reverse=False)
		if temp2:
			l2 = sorted(temp2, reverse=False)

		ff += l1
		ff += l2

		lfiles_set = nlfiles_set = set()

		# crop_filename_regex.sub("", lf.split("\\")[-1])

		if ff:
			temp = list(set(ff))
			ff = sorted(ff, reverse=False)

		processes_ram: list = []
		processes_ram2: list = []

		fsizes_list: list = []

		sum_value: int = 0
		avg_value: int = 0
		len_value: int = 0

		job_set = set()

		try:
			fsizes_list: list = list(
				set(
					[
						os.path.getsize(f.split(";")[0])
						for f in ff
						if os.path.exists(f.split(";")[0])
					]
				)
			)
		except:
			fsizes_list: list = []
		else:
			fsizes_list.sort(reverse=False)

		try:
			avg_size = asyncio.run(avg_lst(list(set(fsizes_list))))  # async(avg_value)
			assert avg_size, ""  # is_assert_debug
		except AssertionError as err:  # if_null
			avg_size: int = 0
			raise err  # logging
		except BaseException:
			try:
				avg_size = (lambda s, l: s / l)(
					sum(fsizes_list), len(fsizes_list)
				)  # by_lambda
			except:
				avg_size = 0

		with unique_semaphore:
			for f in ff:

				try:
					assert (
						ff
					), f"Пустой список или нет файлов {f}"  # ff # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning("Пустой список или нет файлов ff")
					raise err
					break
				except BaseException as e:  # if_error
					logging.error("Пустой список или нет файлов ff [%s]" % str(e))
					break

				try:
					assert f, ""  # is_assert_debug # assert os.path.exists(f)
				except AssertionError as err:  # if_null
					raise err
					continue
				except BaseException:  # if_error
					continue

				if not f in job_set:
					job_set.add(f)
				else:
					continue

				try:
					file1, file2 = f.split(";")[0], f.split(";")[-1]
				except:
					file1 = file2 = ""

				try:
					dfile1, dfile2 = file1, file2
				except:
					dfile1 = dfile2 = ""
				finally:
					if all((dfile1, dfile2)):
						print(
							Style.BRIGHT
							+ Fore.BLUE
							+ "%s" % "=->".join([full_to_short(dfile1), dfile2])
						)  # move_files_by_lang

				try:
					is_new = os.path.exists(file1) and not os.path.exists(file2)
				except:
					is_new = False
				try:
					is_update = os.path.exists(file1) and os.path.exists(file2)
				except:
					is_update = False

				if all(
					(
						file1[0] < file2[0],
						file1.split("\\")[-1] == file2.split("\\")[-1],
						file1,
						file2,
					)
				) and any((is_new, is_update)):

					try:
						fsize: int = os.path.getsize(file1)
						dsize: int = disk_usage(file2[0] + ":\\").free

						try:
							fsize2: int = os.path.getsize(file2)
						except:
							fsize2: int = 0
					except:
						fsize: int = 0
						dsize: int = 0
					else:
						if all(
							(fsize, dsize, int(fsize // (dsize / 100)) <= 100)
						):  # fsize != fsize2 # fspace(ok)

							if all(
								(os.path.getsize(file1) <= avg_size, avg_size)
							):  # if_fspace_less_avg_fsize_then_processed_move

								print(
									Style.BRIGHT
									+ Fore.GREEN
									+ "Добавление в очередь файла",
									Style.BRIGHT + Fore.WHITE + "%s" % file1,
								)  # add_to_all(process_move)

								try:
									asyncio.run(
										process_move(
											file1, file2, False, True, avg_size
										)
									)  # no_await # async_if_small #6
								except BaseException as e:
									write_log(
										"debug process_move[error][6]",
										";".join([file1, file2, str(e)]),
									)
								else:
									write_log(
										"debug process_move[ok][6]",
										";".join([file1, file2]),
									)

								if not file1 in processes_ram:
									processes_ram.append(file1)

							elif (
								all((os.path.getsize(file1) > avg_size, avg_size))
								or not avg_size
							):  # if_fspace_more_avg_or_null_then_default_move

								move(file1, file2)  # no_async_if_big

								if is_new:
									print(
										Style.BRIGHT + Fore.GREEN + "Файл",
										Style.BRIGHT + Fore.WHITE + "%s" % file1,
										Style.BRIGHT + Fore.YELLOW + "надо записать в",
										Style.BRIGHT + Fore.CYAN + "%s" % file2,
									)  # is_another_color # dfile2
									write_log(
										"debug movefile[need][mp4]",
										"Файл %s надо записать в %s" % (file1, file2),
									)

								elif is_update:
									print(
										Style.BRIGHT + Fore.YELLOW + "Файл",
										Style.BRIGHT + Fore.WHITE + "%s" % file1,
										Style.BRIGHT + Fore.YELLOW + "надо обновить в",
										Style.BRIGHT + Fore.CYAN + "%s" % file2,
									)  # is_another_color # dfile2
									write_log(
										"debug movefile[need][mp4]",
										"Файл %s надо обновить в %s" % (file1, file2),
									)

						elif (
							all((fsize >= 0, dsize, int(fsize // (dsize / 100)) > 100))
							or not dsize
						):  # fspace(bad) # dspace(bad)

							if not file1 in processes_ram2:
								processes_ram2.append(file1)

							print(
								Style.BRIGHT
								+ Fore.RED
								+ "move[need] 'Нет хватает места для переноса файла %s'"
								% full_to_short(file1)
							)
							write_log(
								"debug move[need]",
								"Нет хватает места для переноса файла %s" % file1,
							)
							MyNotify(
								txt="Нет хватает места для переноса файла %s"
								% full_to_short(file1),
								icon=icons["error"],
							)

							continue  # skip_if_fspace(bad)
						elif any((not fsize, not dsize)):
							continue  # skip_if_another_logic # fspace(bad)
						else:
							print(
								Style.BRIGHT
								+ Fore.YELLOW
								+ "Не могу обработать файлы [%s][%d]Мб и [%s][%d]Мб"
								% (
									dfile1,
									fsize // (1024**2),
									dfile2,
									fsize2 // (1024**2),
								)
							)
							write_log(
								"debug move[logic]",
								"Не могу обработать файлы [%s][%d]Мб и [%s][%d]Мб"
								% (
									file1,
									fsize // (1024**2),
									file2,
									fsize2 // (1024**2),
								),
							)

		print()

		len_proc = len(processes_ram) + len(processes_ram2)

		if len_proc:  # need_count_and_index
			MySt = MyString()  # MyString("Запускаю:", "[4 из 6]")

			try:
				print(
					Style.BRIGHT
					+ Fore.CYAN
					+ MySt.last2str(
						maintxt="Запускаю:",
						endtxt="[4 из 6]",
						count=len_proc,
						kw="задач",
					)
				)
				# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
			except:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Обновляю или удаляю %d файлы(а,ов) [4 из 6]" % len_proc
				)  # old(is_except)
			else:
				write_log(
					"debug run[task4]",
					MySt.last2str(
						maintxt="Запускаю:",
						endtxt="[4 из 6]",
						count=len_proc,
						kw="задач",
					),
				)

			del MySt

	# --- update_files ---

	try:
		temp = list(
			set(
				[
					lf.strip()
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
					if lf
				]
			)
		)
	except:
		temp = []
	finally:
		lfiles = sorted(temp, reverse=False)  # sort_by_string
		# lfiles = sorted(temp, key=len, reverse=False) # sort_by_string

	date1 = datetime.now()

	jcount = len(lfiles)

	short_set = full_list = set()

	slist: list = []
	dub_list: list = []

	cnt: int = 0

	MT = MyTime(seconds=2)

	"""
	try:
		h, m = asyncio.run(load_timing_from_xml(ind=4)) # 4 # h, m = load_timing_from_xml(ind=4)
	except:
		h, m = 0, 0
	"""

	with unique_semaphore:
		for lf in filter(lambda x: x, tuple(lfiles)):

			cnt += 1

			hour = divmod(
				int(abs(date1 - date2).total_seconds()), 60
			)  # 60(min) -> 3600(hours)

			try:
				_, hh, mm, _ = MT.seconds_to_hms(date1, date2)  # days -> _ # ss -> _
			except:
				mm = abs(date1 - date2).seconds
				hh = mm // 3600
				mm //= 60
				# mm %= 60 # sec

			try:
				if len(hour) > 0:
					hour = hour[0] // 60
				assert bool(hour < 4), ""
			except BaseException:
				hour = 4
			except AssertionError:
				hour = 4

			write_log("debug hour[count][3]", "%d [lfiles]" % hh)  # is_index #3

			# time_is_limit_1hour_50min # all((h >= 0, m, hh >=h, mm >= m)) # all((hh > hour, mm >= m))
			if all((hh > hour, hour)):  # stop_if_more_hour
				write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
				break

			try:
				fname = lf.split("\\")[-1]
			except:
				fname = ""
				continue

			if all((not fname in short_set, fname)):
				short_set.add(fname)
				full_list.add(lf)
			elif all((fname in short_set, fname)):
				full_list.add(lf)

	del MT

	# filter_unique_and_dublicate_files
	if full_list:
		dub_list = list(set(full_list))
		dub_list.sort(reverse=False)

	# update_dublicate_only
	if len(dub_list) >= 2:

		is_dublicate = False

		temp: list = []

		# pass_1_of_2 # check_files_for_update(difference_drive)
		for ind1 in range(len(dub_list) - 1):
			for ind2 in range(ind1 + 1, len(dub_list)):
				if (
					dub_list[ind1].split("\\")[-1] == dub_list[ind2].split("\\")[-1]
					and dub_list[ind1][0] < dub_list[ind2][0]
				):

					try:
						fname = dub_list[ind1].split("\\")[-1]
					except:
						fname = ""

					try:
						fsize: int = os.path.getsize(dub_list[ind1])
						dsize: int = disk_usage(dub_list[ind2][0] + ":\\").free
					except:
						fsize: int = 0
						dsize: int = 0
					else:
						if all(
							(fname, fsize, dsize, int(fsize // (dsize / 100)) <= 100)
						):
							if (
								os.path.exists(dub_list[ind1])
								and os.path.exists(dub_list[ind2])
								and os.path.getsize(dub_list[ind1])
								!= os.path.getsize(dub_list[ind2])
							):
								move(dub_list[ind1], dub_list[ind2])

								print(
									Style.BRIGHT
									+ Fore.WHITE
									+ "%s -> %s" % (dub_list[ind1], dub_list[ind2])
								)
								write_log(
									"debug updatedublicate",
									"%s -> %s" % (dub_list[ind1], dub_list[ind2]),
								)

								if os.path.exists(dub_list[ind1]):
									MyNotify(
										txt=f"Файл {fname} будет обновлен",
										icon=icons["complete"],
									)
								elif not os.path.exists(dub_list[ind1]):
									MyNotify(
										txt=f"Файл {fname} был обновлен",
										icon=icons["complete"],
									)

								is_dublicate = True

							elif (
								os.path.exists(dub_list[ind1])
								and os.path.exists(dub_list[ind2])
								and os.path.getsize(dub_list[ind1])
								== os.path.getsize(dub_list[ind2])
							):
								os.remove(dub_list[ind1])

								print(
									Style.BRIGHT
									+ Fore.WHITE
									+ "%s deleted" % dub_list[ind1]
								)

								write_log(
									"debug deletedublicate",
									"%s deleted" % dub_list[ind1],
								)

								if not os.path.exists(dub_list[ind1]):
									MyNotify(
										txt=f"Дубликат {fname} был удален",
										icon=icons["cleaner"],
									)

						elif (
							all(
								(
									fname,
									fsize >= 0,
									dsize,
									int(fsize // (dsize / 100)) > 100,
								)
							)
							or not dsize
						):  # fspace(bad) # dspace(bad)
							print(
								Style.BRIGHT
								+ Fore.YELLOW
								+ "debug fspace 'Не хватает места для обновления файла %s'"
								% full_to_short(dub_list[ind1])
							)
							write_log(
								"debug fspace",
								"Не хватает места для обновления файла %s"
								% dub_list[ind1],
							)
							MyNotify(
								txt="Не хватает места для обновления файла %s"
								% full_to_short(dub_list[ind1]),
								icon=icons["error"],
							)

		if is_dublicate:
			print(Style.BRIGHT + Fore.YELLOW + "Video dublicate found")
			write_log("debug files", "Video dublicate found")

	# --- update_files ---
	try:
		temp = list(
			set(
				[
					lf.strip()
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
					if lf
				]
			)
		)
	except:
		temp = []
	finally:
		lfiles = sorted(temp, reverse=False)  # sort_by_string
		# lfiles = sorted(temp, key=len, reverse=False) # sort_by_length

	filecmdbase_copy: dict = {}

	# delete_last_jobs_if_hidden(try/except)
	try:
		with open(filecmd_base, encoding="utf-8") as fbf:
			filecmdbase_dict = json.load(fbf)
	except:
		filecmdbase_dict = {}

		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump({}, fbf, ensure_ascii=False, indent=4, sort_keys=False)
	else:
		if filecmdbase_dict:  # is_optimize_and_run_by_time
			filecmdbase_copy = filecmdbase_dict

			# Продолжить сравнив длину файлов(пропустить или обработать)

			# @metadata
			"""
			# First extract metadata # ffmpeg -i original.mov -f ffmetadata metadata.txt # import_metadata(1)
			# exiftool original.mov > metadata.txt # import_metadata(2)
			# ffprobe -show_frames "original.mov" > metadata.txt # import_metadata(3) # all_streams(is_Mb)

			# Next, transcode, including extracted metadata # ffmpeg -i original.mov -f ffmetadata -i metadata.txt compressed.mp4 # export_metadata
			"""

			"""
			@metadata.txt(1) @need_fields
			;FFMETADATA1
			major_brand=isom
			minor_version=512
			compatible_brands=isomiso2avc1mp41
			title=С разбитым Хартом
			artist=Крепкий Харт
			album_artist=Крепкий Харт
			album=Крепкий Харт, Сезон 2
			date=2023
			disc=2
			comment=Актер понял, что ему надоело быть персонажем-шутом на побегушках у главного героя.
			genre=Action
			copyright=LostFilm.TV(c)
			show=Крепкий Харт
			episode_id=201
			episode_sort=1
			season_number=2
			media_type=10
			compilation=0
			track=1
			encoder=Lavf60.3.100
			"""

			# filename = r"c:\downloads\mytemp\hello.mp4"
			def extract_metadata(filename: str = ""):  # is_no_async #1

				try:
					assert filename and os.path.exists(filename), ""  # filename
				except AssertionError as err:  # if_null # BaseException
					raise err  # logging
				else:
					cmd_file = (
						"cmd /c "
						+ "".join([path_for_queue, "ffmpeg.exe"])
						+ ' -hide_banner -y -i "%s" -f ffmetadata "%s" '
						% (filename, ".".join([filename.split(".")[0], "txt"]))
					)  # cmd /k
					os.system("%s" % cmd_file)

				return ".".join(
					[filename.split(".")[0], "txt"]
				)  # metadata_by_source_in_folder_where_file

			def import_metadata(
				inputfilename: str = "",
				metafilename: str = "",
				outputfilename: str = "",
			):  # is_no_async #4
				# ffmpeg -i original.mov -f ffmetadata -i metadata.txt compressed.mp4
				# cmd_file = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -f ffmetadata -i \"%s\" "%s" " % (inputfilename, metafilename, outputfilename)

				# if os.path.exists(metafilename):
				# os.remove(metafilename)

				pass

			maxcnt = len(filecmdbase_dict) if filecmdbase_dict else 0  # is_no_lambda

			prc: int = 0
			cnt: int = 0
			prccnt: int = 0

			prc_set = set()

			filter_run: dict = {}
			filter_skip: dict = {}

			date1 = datetime.now()

			processes_ram: list = []
			processes_ram2: list = []

			# need_optimize(scale/profile/level) # skip_other
			filecmdbase_dict = {
				k: v
				for k, v in filecmdbase_dict.items()
				if any(
					(v.count("scale") > 0, v.count("profile") > 0, v.count("level") > 0)
				)
			}

			year_regex = re.compile(r"[\d+]{4}")
			year_filter: list = []

			def filebase_to_year(filecmdbase_dict=filecmdbase_dict):  # 6
				for k, v in filecmdbase_dict.items():
					if year_regex.findall(k):
						yield k.strip()

			# year_filter = [k.strip() for k in [*filecmdbase_dict] if year_regex.findall(k)] # for k, v in filecmdbase_dict.items()
			year_filter = (
				list(filebase_to_year()) if list(filebase_to_year()) else []
			)  # new(yes_gen) # is_no_lambda

			# debug/test

			full_set = set()

			limit_hour = 4 if year_filter else 2  # is_no_lambda

			# avg_sum: int = 0
			# avg_len: int = 0
			# avg_size: int = 0

			try:
				fsizes: list = list(
					set(
						[
							os.path.getsize(fd)
							for fd in filter(
								lambda x: os.path.exists(x), tuple([*filecmdbase_dict])
							)
							if fd
						]
					)
				)
			except:
				fsizes: list = []
			finally:
				fsizes.sort(reverse=False)

			MT = MyTime(seconds=2)

			"""
			try:
				h, m = asyncio.run(load_timing_from_xml(ind=5)) # 5 # h, m = load_timing_from_xml(ind=5)
			except:
				h, m = 0, 0
			"""

			date1 = datetime.now()

			for k, v in filecmdbase_dict.items():

				try:
					assert (
						filecmdbase_dict
					), "Пустой словарь или нет задач filecmdbase_dict"  # skip_maxint # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning("Пустой словарь или нет задач filecmdbase_dict")
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой словарь или нет задач filecmdbase_dict [%s]" % str(e)
					)
					break

				cnt += 1

				if not k in full_set:
					full_set.add(k.strip())  # save_unique_job

				# elif k in full_set:
				# continue  # skip_unique_job

				date2 = datetime.now()

				# hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(
						date1, date2
					)  # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				try:
					if len(hour) > 0:
						hour = hour[0] // 60
					assert bool(hour < 4), ""
				except BaseException:
					hour = 4
				except AssertionError:
					hour = 4

				write_log(
					"debug hour[count][4]", "%d [filecmdbase_dict]" % hh
				)  # is_index #4

				# # time_is_limit_1hour_or_30min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if (
					all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
				):  # stop_if_more_hour
					write_log(
						"debug stop_job[filecmdbase_dict]",
						"Stop: at %s [%d]" % (k, cnt),
					)
					break

				# find_dspace(nlocal)
				try:
					ds2 = disk_usage("d:\\").free
				except:
					ds2 = 0

				try:
					fname1 = k.strip()
				except:
					fname1 = ""

				try:
					fname2 = v.split(" ")[-1].strip()
				except:
					fname2 = ""

				date2 = datetime.now()

				try:
					prc = cnt / maxcnt
					prc *= 100
				except:
					break  # if_percent_calc_error

				if int(prc) != int(prccnt):
					prccnt = int(prc)

					# change_numeric_data_to_percent # if_every_file_run
					if not prccnt in prc_set and (
						not prc_set
						or all((prc_set, prccnt > sorted(list(prc_set))[-1]))
					):  # null_or_more_last
						prc_set.add(prccnt)

				# is_check_ready_project_by_length_files(main)
				try:
					gl1 = MM.get_length(fname1)
				except:
					gl1 = 0

				try:
					gl2 = MM.get_length(fname2)
				except:
					gl2 = 0

				try:
					fstatus = fspace(
						fname2, fname1
					)  # all((fsize, dsize, int(fsize // (dsize / 100)) <= 100))
				except:
					fstatus = False

				is_not_need_run = (
					all((gl2 in range(gl1, gl1 - 5, -1), gl1, gl2))
					if all((gl1, gl2))
					else False
				)  # run_job_filter

				if all(
					(is_not_need_run, fname1.split("\\")[-1] == fname2.split("\\")[-1])
				):  # ready(skip_status_and_move_ready)
					print(
						Style.BRIGHT
						+ Fore.BLUE
						+ "Файл %s будет пропущен для обработки, т.к. длина файла совпала"
						% fname1
					)  # skip_color_is_blue

					write_log(
						"debug backup[skip]",
						"Файл %s будет пропущен для обработки, т.к. длина файла совпала"
						% fname1,
					)

					if os.path.exists(fname1) and os.path.exists(
						fname2
					):  # all_exists # is_green
						print(
							Style.BRIGHT + Fore.GREEN + "Обработалось",
							Style.BRIGHT + Fore.WHITE + "%d из %d" % (cnt, maxcnt),
							Style.BRIGHT + Fore.GREEN + "данных, текущий файл [%s]" % k,
						)  # some_original_filename(short)

						write_log(
							"debug data[percent]",
							"Обработалось %d из %d данных, текущий файл [%s]"
							% (cnt, maxcnt, k),
						)  # some_original_filename(full/job)

					filter_skip[
						k.strip()
					] = v.strip()  # count_skip_by_dict(almost_ready)

					if all((gl1, gl2, fstatus)):  # fspace(ok) # no_errors
						if os.path.exists(fname1) and os.path.exists(
							fname2
						):  # move_ready_project_by_length # project -> original
							# move(fname2, fname1) # "move" -> process_move

							print(
								Style.BRIGHT
								+ Fore.GREEN
								+ "Добавление в очередь файла",
								Style.BRIGHT + Fore.WHITE + "%s" % fname2,
							)  # add_to_all(process_move)

							asyncio.run(
								(fname2, fname1, False, True, avg_size)
							)  # async_if_small

							if not fname2 in processes_ram:
								processes_ram.append(fname2)

							filecmdbase_copy = {
								k2: v2 for k2, v2 in filecmdbase_copy.items() if k2 != k
							}  # clear_for_skip_run(is_ready_ok_by_length)

							write_log(
								"debug move[ended]",
								"Файл %s успешно завершен для переноса в %s [%s]"
								% (v.split(" ")[-1], fname1, str(fstatus)),
							)

					elif all((gl1, gl2 >= 0)) and any(
						(fstatus == False, is_not_need_run == True)
					):  # fspace(bad) # no_need_run(ok)
						write_log(
							"debug move[ended][error]",
							"Файл %s успешно завершен, но нет места или ошибка переноса для %s"
							% (v.split(" ")[-1], fname1),
						)

					print()  # null_line_after_logging
				elif all(
					(
						is_not_need_run == False,
						fname1.split("\\")[-1] == fname2.split("\\")[-1],
					)
				) or not os.path.exists(
					fname2
				):  # not_(ready/exists)(run_status)
					# print(Style.BRIGHT + Fore.CYAN + "Файл %s будет запущен для обработки, т.к. длина файла разная или отсутствует на диске" % fname2.split("\\")[-1]) # is_run

					print(
						Style.BRIGHT
						+ Fore.CYAN
						+ "Возможно длина файла %s разная или отсутствует на диске"
						% v.split(" ")[-1]
					)  # is_delete # delete_color_is_cyan

					# write_log("debug backup[run]", "Файл %s будет запущен для обработки, т.к. длина файла разная или отсутствует на диске" % fname2) # is_run
					write_log(
						"debug backup[run]",
						"Возможно длина файла %s разная или отсутствует на диске"
						% v.split(" ")[-1],
					)  # is_delete

					exist_or_update = (
						os.path.exists(fname1)
						and not os.path.exists(fname2)
						or not os.path.exists(fname1)
						and os.path.exists(fname2)
					)
					not_exists = not os.path.exists(fname1) and not os.path.exists(
						fname2
					)

					if exist_or_update:  # some_exists # some_not_exists # is_yellow
						print(
							Style.BRIGHT + Fore.YELLOW + "Обработалось",
							Style.BRIGHT + Fore.WHITE + "%d" % cnt,
							Style.BRIGHT
							+ Fore.YELLOW
							+ "данных, текущий файл [%s]" % fname1,
						)  # some_original_filename(short)

						write_log(
							"debug data[percent]",
							"Обработалось %d данных, текущий файл [%s]" % (cnt, fname1),
						)  # some_original_filename(full/job)
					elif not_exists:  # all_not_exists # is_red
						print(
							Style.BRIGHT + Fore.RED + "Обработалось",
							Style.BRIGHT + Fore.WHITE + "%d" % cnt,
							Style.BRIGHT
							+ Fore.RED
							+ "данных, текущий файл [%s]" % fname1,
						)  # some_original_filename(short)

						write_log(
							"debug data[percent]",
							"Обработалось %d данных, текущий файл [%s]" % (cnt, fname1),
						)  # some_original_filename(full/job)

					filter_run[k.strip()] = v.strip()  # count_run_by_dict(need_run)

					if os.path.exists(
						fname2
					):  # delete_not_ready_project_by_length # project
						# os.remove(fname2) # remove -> process_delete

						asyncio.run(process_delete(fname2))  # async_if_delete

						if not fname2 in processes_ram2:
							processes_ram2.append(fname2)

					# run_no_complete_file_from_[fcd.json] # debug/test

			del MT

			del MM

			print()

			len_proc = len(processes_ram) + len(processes_ram2)

			MySt = MyString()  # MyString("Запускаю:", "[5 из 6]")

			if len_proc:
				try:
					print(
						Style.BRIGHT
						+ Fore.CYAN
						+ MySt.last2str(
							maintxt="Запускаю:",
							endtxt="[5 из 6]",
							count=len_proc,
							kw="задач",
						)
					)
					# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
				except:
					print(
						Style.BRIGHT
						+ Fore.YELLOW
						+ "Обновляю или удаляю %d файлы(а,ов) [5 из 6]" % len_proc
					)  # old(is_except)
				else:
					write_log(
						"debug run[task6]",
						MySt.last2str(
							maintxt="Запускаю:",
							endtxt="[5 из 6]",
							count=len_proc,
							kw="задач",
						),
					)

			# update_data_if_stay_files(some)_or_all_ready(null)
			if all((filecmdbase_dict, len(filecmdbase_copy) <= len(filecmdbase_dict))):
				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(
						filecmdbase_copy,
						fbf,
						ensure_ascii=False,
						indent=4,
						sort_keys=False,
					)

			if all((filter_run, filter_skip)):
				filter_run = {
					k: v
					for k, v in filter_run.items()
					for k2, v2 in filter_skip.items()
					if all((k, k2, k != k2))
				}  # include_run_delete_skip

				# filter_run.pop(k2) # debug

			filter_run_count = (
				len(filter_run) if filter_run else 0
			)  # count_or_null # is_no_lambda
			filter_skip_count = (
				len(filter_skip) if filter_skip else 0
			)  # count_or_null # is_no_lambda

			# print_counts(run/skip)_and_logging # last2str

			if all(
				(
					filter_skip_count,
					filter_run_count >= 0,
					filter_run_count < filter_skip_count,
				)
			):  # run_logic
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ MySt.last2str(
						maintxt="Было запущено", count=filter_run_count, kw="файл"
					)
				)
				write_log(
					"debug filter[run]", "Было запущено %d файлов(а)" % filter_run_count
				)

			elif all(
				(
					filter_skip_count,
					filter_run_count,
					filter_skip_count == filter_run_count,
				)
			):  # skip_logic
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ MySt.last2str(
						maintxt="Было пропущено", count=filter_skip_count, kw="файл"
					)
				)
				write_log(
					"debug filter[skip]",
					"Было пропущено %d файлов(а)" % filter_skip_count,
				)

			del MySt

			if all(
				(
					filter_run,
					filecmdbase_dict,
					len(filter_skip) == len(filecmdbase_dict),
				)
			):
				# clear_jobsdata_if_skip_count_equal_jobs_count # logic(1_of_2)
				asyncio.run(
					project_done()
				)  # after_jobs_finish # update_project(some_ready/all)
				asyncio.run(update_bigcinema())  # update_cinema
				asyncio.run(project_update())  # updates(if_downloaded)
				# true_project_rename(folder=copy_src); true_project_rename() # check_and_rename
				asyncio.run(true_project_rename())  # check_and_rename

				ctme = datetime.now()

				if not srd:
					asyncio.run(
						shutdown_if_time()
					)  # check_time_after_run(finish) # try_skip # no_date="29.08.2023"

				# filecmdbase_dict = {}  # clean_jobs_list_after_skip # clear_when_done

				# with open(filecmd_base, "w", encoding="utf-8") as fbf:
				# json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False)

			elif (
				all((filecmdbase_dict, not filter_run))
				or all(
					(
						filter_run,
						filecmdbase_dict,
						len(filter_run) < len(filecmdbase_dict),
					)
				)
				and all((cnt, maxcnt, cnt <= maxcnt))
			):
				# update_if_some_jobs_or_run_less_jobs_count # logic(2_of_2)
				asyncio.run(
					project_done()
				)  # after_jobs_finish # update_project(some_ready/all)
				asyncio.run(update_bigcinema())  # update_cinema
				asyncio.run(project_update())  # updates(if_downloaded)
				# true_project_rename(folder=copy_src); true_project_rename() # check_and_rename
				asyncio.run(true_project_rename())  # check_and_rename

				ctme = datetime.now()

				if not srd:
					asyncio.run(
						shutdown_if_time()
					)  # check_time_after_run(finish) # try_skip # no_date="29.08.2023"

				# filecmdbase_dict = {}  # clean_jobs_list_after_update # clear_when_done

				# with open(filecmd_base, "w", encoding="utf-8") as fbf:
				# json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False)

	# @paths_base
	try:
		with open(paths_base, encoding="utf-8") as pbf:
			pathbase_dict = json.load(pbf)
	except:
		pathbase_dict = {}

		with open(paths_base, "w", encoding="utf-8") as pbf:
			json.dump({}, pbf, ensure_ascii=False, indent=4, sort_keys=True)

	else:
		listfiles_dict = {
			lf.strip(): "\\".join(lf.split("\\")[:-1]).strip()
			for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
			if lf
		}  # {fullname:fullfolder} # current_files

		if listfiles_dict:
			pathbase_dict.update(listfiles_dict)  # update_files(dict)

		# {fullname:fullfolder} # exists_files
		pathbase_dict = {k: v for k, v in pathbase_dict.items() if os.path.exists(k)}

		with open(paths_base, "w", encoding="utf-8") as pbf:
			json.dump(pathbase_dict, pbf, ensure_ascii=False, indent=4, sort_keys=True)

	if need_find_all:  # avg_days_to_full_period
		try:
			dbl = asyncio.run(days_by_list(lfiles))  # full_days
		except:
			dbl = 365  # full_year

		is_any = True if dbl != 365 else False  # is_no_lambda

		# filter_by_period(all_time/avg_time)
		try:
			temp = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if all(
							(
								lf,
								mdate_by_days(filename=lf, period=dbl, is_any=is_any)
								!= None,
							)
						)
					]
				)
			)
		except:
			temp = []
		finally:
			if isinstance(dbl, int) and dbl != None:
				# write_log("debug files[avgdays]", "Дней: %d, найдено: %d" % (dbl, len(temp)))
				write_log("debug files[maxdays]", "Найдено: %d" % len(temp))

			lfiles = sorted(temp, reverse=False)

	elif need_find_period:  # find_by_period
		try:
			dbl = asyncio.run(days_by_list(lfiles))  # full_days
		except:
			dbl = 365  # full_year

		# every_30days
		try:
			dbl = (
				(dbl // 30) * 30 if dbl // 30 > 0 else 30
			)  # get_period_more_month_or_month # is_no_lambda
		except:
			dbl = 30

		is_any = True if dbl != 30 else False  # is_no_lambda

		try:
			temp = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if all(
							(
								lf,
								mdate_by_days(filename=lf, period=dbl, is_any=is_any)
								!= None,
							)
						)
					]
				)
			)  # filter_by_all_days
		except:
			temp = []

		if temp:
			write_log(
				"debug files[allmonth]", "Найдено: %d" % len(temp)
			)  # allmonth(dbl >= 30)

		elif not temp:  # all_days_if_no_files_by_30days
			try:
				dbl = asyncio.run(days_by_list(lfiles))  # full_days
			except:
				dbl = 365  # full_year

			is_any = True if dbl != 365 else False  # is_no_lambda

			try:
				temp = list(
					set(
						[
							lf.strip()
							for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
							if all(
								(
									lf,
									mdate_by_days(
										filename=lf, period=dbl, is_any=is_any
									)
									!= None,
								)
							)
						]
					)
				)  # filter_by_all_days
			except:
				temp = []
			else:
				if temp:
					write_log("debug files[alldays]", "Найдено: %d" % len(temp))

		lfiles = sorted(temp, reverse=False)

	if lfiles and any(
		(need_find_period, need_find_all)
	):  # filter_period(30_days/all_days)
		if need_find_all:
			write_log(
				"debug files[find]", "Найдены за весь период [%s]" % str(datetime.now())
			)
		elif need_find_period:
			write_log(
				"debug files[find]", "Найдены за месяц [%s]" % str(datetime.now())
			)

		date1 = datetime.now()

		unique = full_list = set()
		try:
			# tmp = list(lf_gen()) # new(yes_gen)
			tmp: list = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if lf
					]
				)
			)
		except:
			tmp: list = []
		finally:
			lfiles = sorted(tmp, reverse=False)  # sort_by_string
			# lfiles = sorted(tmp, key=len, reverse=False)  # sort_by_length

		cnt: int = 0

		MT = MyTime(seconds=2)

		"""
		try:
			h, m = asyncio.run(load_timing_from_xml(ind=6)) # 6 # h, m = load_timing_from_xml(ind=6)
		except:
			h, m = 0, 0
		"""

		# with unique_semaphore:
		for lf in filter(lambda x: x, tuple(lfiles)):

			cnt += 1

			date2 = datetime.now()

			hour = divmod(
				int(abs(date1 - date2).total_seconds()), 60
			)  # 60(min) -> 3600(hours)

			try:
				_, hh, mm, _ = MT.seconds_to_hms(date1, date2)  # days -> _ # ss -> _
			except:
				mm = abs(date1 - date2).seconds
				hh = mm // 3600
				mm //= 60
				# mm %= 60 # sec

			try:
				if len(hour) > 0:
					hour = hour[0] // 60
				assert bool(hour < 4), ""
			except BaseException:
				hour = 4
			except AssertionError:
				hour = 4

			write_log("debug hour[count][5]", "%d [lfiles]" % hh)  # is_index #5

			# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
			if (
				all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
			):  # stop_if_more_hour
				write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
				break

			try:
				fname = lf.split("\\")[-1].strip()
			except:
				fname = ""
				continue

			if all((not fname in unique, fname)):
				unique.add(fname)  # short_file(first)_by_set
				full_list.add(lf)

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)

		def files_to_short_by_full(lfiles=lfiles):  # 6
			for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)):
				if all((lf, crop_filename_regex.sub("", lf.split("\\")[-1]))):
					if lf:
						yield lf.strip()
					else:
						yield ""
				else:
					yield ""

		try:
			tmp: list = list(files_to_short_by_full())  # new(yes_gen)
		except:
			tmp: list = []
		finally:
			lfiles = sorted(tmp, reverse=False)  # sort_by_string
			# lfiles = sorted(tmp, key=len, reverse=False) # sort_by_length

	elif not lfiles:  # if -> elif
		# read_jobs_from_base(if_no_files_by_template)

		somebase_dict: dict = {}

		# load_meta_jobs(filter) #9
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(
					somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)
		finally:
			some_files = (
				[*somebase_dict] if somebase_dict else []
			)  # list(somebase_dict.keys()) # is_no_lambda

		some_files = (
			some_files[0:1000] if len(some_files) >= 1000 else some_files
		)  # no_limit(if_hide) # (5)

		def files_to_short(some_files=some_files):  # 7
			for sm in filter(lambda x: os.path.exists(x), tuple(some_files)):
				if sm:
					yield crop_filename_regex.sub("", sm.split("\\")[-1]).strip()
				else:
					yield ""

		# shorts_in_list(upgrade)
		try:
			# filter_list = [crop_filename_regex.sub("", lf.split("\\")[-1]) for lf in filter(lambda x: os.path.exists(x), tuple(some_files))] # equal
			filter_list: list = list(
				set(
					[
						crop_filename_regex.sub("", lf.split("\\")[-1])
						.split("_")[0]
						.strip()
						if lf.split("\\")[-1].count("_") > 0
						else crop_filename_regex.sub("", lf.split("\\")[-1]).strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(some_files))
					]
				)
			)  # match_or_equal
		except:
			filter_list: list = []
		finally:
			filter_list = sorted(filter_list, reverse=False)

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))", re.M) # _[\d+]{2}p

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$"
				% "|".join(filter_list),
				re.M,
			)
		elif not filter_list:
			# if not some_files:
			# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M) # _[\d+]{2}p
			if some_files:  # elif -> if
				filt = sorted(
					list(
						set(
							[
								crop_filename_regex.sub("", k.split("\\")[-1]).strip()
								for sm in filter(
									lambda x: os.path.exists(x), tuple(some_files)
								)
							]
						)
					),
					key=len,
					reverse=False,
				)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$"
					% "|".join(filt),
					re.M,
				)  # M(atch)/I(gnore)_case # by_filter_base

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine
				nlf = e.submit(
					sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex
				)  # nlocal # serialy
				nlf2 = e.submit(
					sub_folder, "d:\\multimedia\\video\\serials_europe\\", video_regex
				)  # nlocal # serialy_rus
				nlf3 = e.submit(
					sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex
				)  # nlocal # filmy
				# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
				# nlf5 = e.submit(sub_folder, "d:\\multimedia\\video\\", temp_regex) # temporary_files
				# nlf6 = e.submit(sub_folder, "d:\\multimedia\\video\\documental\\", video_regex) # documental_files

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()
			# lfiles += nlf5.result()
			# lfiles += nlf6.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(
					one_folder, "c:\\downloads\\new\\", video_regex
				)  # local # combine

			lfiles = lf.result()

		if not lfiles:  # stop_if_no_files # temp(debug)
			logging.info("@no lfiles[13489]")
			exit()

		if filter_list:
			tfilter_list = list(
				set([f.strip() for f in filter_list if f])
			)  # if len(f) > 1
			filter_list = tfilter_list if tfilter_list else []  # is_no_lambda

			write_log(
				"debug files[filter][reserved]", "%s" % "|".join(filter_list)
			)  # current(5)

		date1 = datetime.now()

		# no_backup(lfiles)
		unique = full_list = set()
		try:
			# tmp = list(lf_gen()) # new(yes_gen)
			tmp: list = list(
				set(
					[
						lf.strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if lf
					]
				)
			)
		except:
			tmp: list = []
		finally:
			lfiles = sorted(tmp, reverse=False)  # sort_by_string
			# lfiles = sorted(tmp, key=len, reverse=False) # sort_by_length

		cnt: int = 0

		MT = MyTime(seconds=2)

		"""
		try:
			h, m = asyncio.run(load_timing_from_xml(ind=7)) # 7 # h, m = load_timing_from_xml(ind=7)
		except:
			h, m = 0
		"""

		date1 = datetime.now()

		with unique_semaphore:
			for lf in filter(lambda x: x, tuple(lfiles)):

				try:
					fname = lf.strip("\\")[-1]
				except:
					fname = ""
					continue

				if all((not fname in unique, fname)):
					unique.add(fname)  # short_file(first)_by_set
					full_list.add(lf)  # full_filename(first)_by_set

				cnt += 1

				date2 = datetime.now()

				# hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(
						date1, date2
					)  # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				try:
					if len(hour) > 0:
						hour = hour[0] // 60
					assert bool(hour < 4), ""
				except BaseException:
					hour = 4
				except AssertionError:
					hour = 4

				write_log("debug hour[count][6]", "%d [lfiles]" % hh)  # is_index #6

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if (
					all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
				):  # stop_if_more_hour
					write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
					break

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)

		if filter_list:
			temp = list(
				set(
					[
						flst.strip()
						for fl in filter(lambda y: y, tuple(filter_list))
						for flst in filter(
							lambda x: os.path.exists(x), tuple(full_list)
						)
						if all((flst, fl, fl in flst))
					]
				)
			)  # +filter
		elif not filter_list:
			temp = list(
				set(
					[
						flst.strip()
						for flst in filter(
							lambda x: os.path.exists(x), tuple(full_list)
						)
						if all(
							(flst, crop_filename_regex.sub("", flst.split("\\")[-1]))
						)
					]
				)
			)  # default_filter

		# lfiles = sorted(temp, reverse=False) # sort_by_string(default)
		# lfiles = sorted(temp, key=len, reverse=False) # sort_by_length

		if not lfiles:  # exit_if_not_found_some_files
			exit()

	# filesize/...

	try:
		lfiles_dict = {
			lf.strip(): [os.path.getsize(lf)]
			for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
			if all((lf, os.path.getsize(lf)))
		}  # filesize
	except:
		lfiles_dict = {}  # use_all_find_files(if_null_dict)
	else:
		lfiles_sizes = [v[0] for _, v in lfiles_dict.items() if v[0]]  # all_filesizes
		if lfiles_sizes:
			temp = list(set(lfiles_sizes))
			lfiles_sizes = sorted(
				temp, reverse=False
			)  # True = cba(sort) # False = abc(sort)

			def files_by_sizes(lfiles_sizes=lfiles_sizes, lfiles=lfiles):  # 2
				for ls in lfiles_sizes:
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)):
						if all((lf, os.path.getsize(lf) == ls, os.path.getsize(lf))):
							yield lf.strip()
						else:
							yield ""

			try:
				tmp: list = list(files_by_sizes())  # new(yes_gen)
			except:
				tmp: list = []
			finally:
				lfiles = sorted(tmp, reverse=True)  # sort_by_string
				# lfiles = sorted(tmp, key=len, reverse=True) # sort_by_length

	write_log("debug jobsave", "%d" % len(lfiles))  # count_current_jobs(all_find_files)

	another_list: list = []

	MM = MyMeta()  # 6

	prc: int = 0
	cnt: int = 0
	max_cnt: int = len(lfiles)

	# meta_ram = param_list = []

	prc_set = job_set = set()

	fext_dict: dict = {}

	date1 = datetime.now()
	try:
		# tmp = list(lf_gen()) # new(yes_gen)
		tmp: list = list(
			set(
				[
					lf.strip()
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
					if lf
				]
			)
		)
	except:
		tmp: list = []
	finally:
		lfiles = sorted(tmp, reverse=False)  # sort_by_string
		# lfiles = sorted(tmp, key=len, reverse=False) # sort_by_length

	hms_sum: int = 0
	hms_len: int = 0
	hms_avg: int = 0

	cnt: int = 0

	MT = MyTime(seconds=2)

	"""
	try:
		h, m = asyncio.run(load_timing_from_xml(ind=8)) # 8 # h, m = load_timing_from_xml(ind=8)
	except:
		h, m = 0, 0
	"""

	date1 = datetime.now()

	# with unique_semaphore:
	for lf in filter(lambda x: x, tuple(lfiles)):

		cnt += 1

		try:
			fp, fn = split_filename(lf)
		except:
			fn = lf.split("\\")[-1].strip()  # fp

		try:
			fname = fn
		except:
			fname = ""
			continue

		fext = lf.split(".")[-1].lower().strip()

		fext_dict[fext.strip()] = fext_dict.get(fext.strip(), 0) + 1  # add_count

		date2 = datetime.now()

		hour = divmod(
			int(abs(date1 - date2).total_seconds()), 60
		)  # 60(min) -> 3600(hours)

		try:
			_, hh, mm, _ = MT.seconds_to_hms(date1, date2)  # days -> _ # ss -> _
		except:
			mm = abs(date1 - date2).seconds
			hh = mm // 3600
			mm //= 60
			# mm %= 60 # sec

		try:
			if len(hour) > 0:
				hour = hour[0] // 60
			assert bool(hour < 4), ""
		except BaseException:
			hour = 4
		except AssertionError:
			hour = 4

		write_log("debug hour[count][7]", "%d [lfiles]" % hh)  # is_index #7

		# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
		if (
			all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
		):  # stop_if_more_hour
			write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
			break

		if not lf in job_set:
			job_set.add(lf)
		else:
			continue

		if lf != lf.strip() and len(lf.strip()) > 0:
			lf = lf.strip()

		if all(
			(
				lf.split(".")[-1].lower()
				in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"],
				lf[0].lower() != "c",
			)
		):
			os.remove(lf)

			continue

		# some_formula(lf) # debug/test (fps/filesize/destonation)

		# run(pass_1_of_2)

		fname = (
			lf.split("\\")[-1].strip() if os.path.exists(lf) else ""
		)  # filename(no_ext) # is_no_lambda # old
		# fname = ("", lf.split("\\")[-1].strip())[os.path.exists(lf)] # filename(no_ext) # ternary

		fext = (
			lf.split(".")[-1].lower().strip() if os.path.exists(lf) else ""
		)  # extention # is_no_lambda # old
		# fext = ("", lf.split(".")[-1].lower().strip())[os.path.exists(lf)] # extention # ternary

		try:
			assert os.path.exists(lf) and all(
				(lf, fname, fext)
			), ""  # is_assert_debug # is_no_except(no_logging) # lf
		except AssertionError:  # if_null
			# raise err
			continue
		except BaseException:  # if_error
			continue

		ofilename = newfilename = ""

		try:
			fp, fn = split_filename(lf)
		except:
			fn = lf.split("\\")[-1].strip()  # fp

		try:
			dfilename = fn
		except:
			dfilename = ""
			continue

		if fext != "mp4":
			"""
			path_for_folder = "\\".join(lf.split("\\")[:-1]) + "\\"  # "c:\\downloads\\new\\"

			ofilename = lf  # original_file
			fname = lf.split("\\")[-1].split(".")[0] + ".mp4"  # new_short(any_to_mp4)
			# newfilename = "\\".join(ofilename.split(".")[0:-1]) + ".mp4"  # by_source_folder(any_to_mp4)
			project_file = "".join([path_to_done, fname])  # project_file(need_changed)

			# source_folder = path_for_folder # source_folder(for_move/update)
			source_file = path_for_folder + fname  # source_folder(for_move/update)

			# c:\downloads\new\somefile.avi;c:\downloads\somefile.mp4;c:\downloads\new\somefile.mp4 # delete\move->new)\new
			# another_list.append({"file":[ofilename, project_file, source_file]}) # dict_in_list(hidden) # @any_to_mp4

			print(Style.BRIGHT + Fore.WHITE + "%s" % ";".join([ofilename, project_file, source_file]))  # full_setup # is_need_json

			write_log("debug anyfile", "%s [%s]" % (";".join([ofilename, project_file, source_file]), str(datetime.now())))

			"""

			continue  # skip_run_after_mp4

		print(
			Style.BRIGHT + Fore.WHITE + "Получаю мета-данные по файлу:",
			Style.BRIGHT + Fore.YELLOW + "%s" % lf,
		)

		write_log("debug getmeta", "Получаю мета-данные по файлу: %s" % lf)

		try:
			width, height, is_change = MM.get_width_height(
				filename=lf, is_calc=True
			)  # pass_3_of_3 # calc("find_scale_and_true_scale")
		except BaseException as e:
			width = height = 0
			is_change = False

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log(
				"debug get_width_height[error]", "%s [%s]" % (lf, str(e)), is_error=True
			)
			logging.error("@get_width_height[error] %s [%s]" % (lf, str(e)))

			continue  # skip_if_no_scale

		# optimal_hd

		# rescale_any_tv(hd <-> sd) # 1:1
		if all((width >= height, width, height)):
			# 16/9 -> 4/3 # is_run(no_script) # is_zip(no_backup) # is_pad(sd_bars/hd_scale) # when_zip(delete_scaled)
			# is_run(is_zip)[ok] # is_run(is_zip/is_pad) # sd # is_debug
			try:
				hd_sd = MM.hd_to_sd(
					lf, width, height, is_run=False, is_zip=False, is_pad=True
				)
			except BaseException as e:
				hd_sd = ""
				write_log(
					"debug hdtosd[rescale][error]",
					"%s [%s]" % (dfilename, str(e)),
					is_error=True,
				)  # error
				logging.error("@hdtosd[rescale][error] %s [%s]" % (dfilename, str(e)))
			else:
				if hd_sd:
					write_log(
						"debug hdtosd[rescale]",
						"%s [%s] [%s]"
						% (hd_sd, dfilename, str(round(width / height, 2))[0:]),
					)

			# 4/3 -> 16/9 # is_run(no_script) # is_zip=False(no_backup) # is_pad(unknown) # when_zip(delete_scaled)
			# is_run(is_zip)[?] # is_run(is_zip/is_pad) # hd # is_debug
			try:
				sd_hd = MM.sd_to_hd(
					lf, width, height, is_run=True, is_zip=True, is_pad=True
				)
			except BaseException as e:
				sd_hd = ""
				write_log(
					"debug sdtohd[rescale][error]",
					"%s [%s]" % (dfilename, str(e)),
					is_error=True,
				)  # error
				logging.error("@sdtohd[rescale][error] %s [%s]" % (dfilename, str(e)))
			else:
				if sd_hd:
					write_log(
						"debug sdtohd[rescale]",
						"%s [%s] [%s]"
						% (sd_hd, dfilename, str(round(width / height, 2))[0:]),
					)

		if all((width >= height, width, height)):
			write_log(
				"debug get_width_height",
				"%s" % ";".join([lf, str(width), str(height), str(is_change)]),
			)

		elif any((not width, not height)):
			write_log("debug wh[null]", "Нет данных width/height для %s" % lf)
			logging.warning("@wh[null] Нет данных width/height для %s" % lf)

			if os.path.exists(lf) and not os.path.getsize(lf):
				print(
					Style.BRIGHT
					+ Fore.RED
					+ "Файл %s пустой его надо удалить" % dfilename
				)
				write_log("debug file[null]", "Файл %s пустой его надо удалить" % lf)
				logging.warning("@file[null] Файл %s пустой его надо удалить" % lf)

				continue

		try:
			nwidth = height * (width / height)
		except:
			nwidth = 0

		if not isinstance(nwidth, int):
			nwidth = int(nwidth)
		if nwidth % 2 != 0:
			nwidth -= 1

		"""
		is_other_hd: bool = False

		# ar = 1.7777777777777777777777777777778

		# logging(1_to_3)
		try:
			if any((width == 3840, height == 2160)):
				if width != nwidth:
					logging.info("@hd file: %s, quality: 2160p, width: %d, height: %d, fps: 60/30, speed: 20-50/13-34" % (lf, nwidth, height))
				else:
					logging.info("@hd file: %s, quality: 2160p, width: %d, height: %d, fps: 60/30, speed: 20-50/13-34" % (lf, width, height))
			elif any((width == 2560, height == 1440)):
				if width != nwidth:
					logging.info("@hd file: %s quality: 1440p, width: %d, height: %d, fps: 60/30, speed: 9-18/6-13" % (lf, nwidth, height))
				else:
					logging.info("@hd file: %s quality: 1440p, width: %d, height: %d, fps: 60/30, speed: 9-18/6-13" % (lf, width, height))
			elif any((width == 1920, height == 1080)):
				if width != nwidth:
					logging.info("@hd file: %s, quality: 1080p, width: %d, height: %d, fps: 60/30, speed: 4,5-9/3-6" % (lf, nwidth, height))
				else:
					logging.info("@hd file: %s, quality: 1080p, width: %d, height: %d, fps: 60/30, speed: 4,5-9/3-6" % (lf, width, height))
			elif any((width == 1280, height == 720)):
				if width != nwidth:
					logging.info("@hd file: %s, quality: 720p, width: %d, height: %d, fps: 60/30, speed: 2,25-6/1,5-4" % (lf, nwidth, height))
				else:
					logging.info("@hd file: %s, quality: 720p, width: %d, height: %d, fps: 60/30, speed: 2,25-6/1,5-4" % (lf, width, height))

		except BaseException as e:
			logging.warning("[hd] error %s" % ";".join([lf, str(e)]))
		else:
			if all((height, height >= 720)): # height_more_or_equal_720
				logging.info("@hd file: %s, quality: %dp, width: %d, height: %d" % (lf, height, width, height))
				is_other_hd = ((width / height) == 1.7777777777777777777777777777778) # True

		if all((height, (width / height) == (16/9))) or is_other_hd: # not is_other_hd # is_hd
			any_hd_str = "@hd file: %s, quality: %dp, width: %d, height: %d" % (lf, height, width, height)
			logging.info("@any_hd_str %s [hd]" % any_hd_str)

		# sd # block2
		is_other_sd: bool = False

		try:
			nwidth = height * (width / height)
		except:
			nwidth = 0

		if not isinstance(nwidth, int):
			nwidth = int(nwidth)
		if nwidth % 2 != 0:
			nwidth -= 1

		is_other_sd: bool = False

		ar_list = [1.7708333333333333333333333333333, 1.7777777777777777777777777777778, 1.775]

		# logging(1_to_3)
		try:
			if any((width == 850, height == 480)):
				if width != nwidth:
					logging.info("@sd file: %s, quality: 480p, width: %d, height: %d, fps: 30, speed: 0,5-2" % (lf, nwidth, height))
				else:
					logging.info("@sd file: %s, quality: 480p, width: %d, height: %d, fps: 30, speed: 0,5-2" % (lf, width, height))
			elif any((width == 640, height == 360)):
				if width != nwidth:
					logging.info("@sd file: %s, quality: 360p, width: %d, height: %d, fps: 30, speed: 0,4-1" % (lf, nwidth, height))
				else:
					logging.info("@sd file: %s, quality: 360p, width: %d, height: %d, fps: 30, speed: 0,4-1" % (lf, width, height))
			elif any((width == 426, height == 240)):
				if width != nwidth:
					logging.info("@sd file: %s, quality: 240p, width: %d, height: %d, fps: 30, speed: 0,3-0,7" % (lf, nwidth, height))
				else:
					logging.info("@sd file: %s, quality: 240p, width: %d, height: %d, fps: 30, speed: 0,3-0,7" % (lf, width, height))

		except BaseException as e:
			logging.warning("[sd] error %s" % ";".join([lf, str(e)]))
		else:
			if all((height, height <= 480)): # height_less_or_equal_480
				logging.info("@sd file: %s, quality: %dp, width: %d, height: %d" % (lf, height, width, height))
				is_other_sd = ((width / height) in ar_list) # True

		if all((height, (width / height) == (4/3))) or is_other_sd: # not is_other_sd # is_sd
			any_sd_str = "@sd file: %s, quality: %dp, width: %d, height: %d" % (lf, height, width, height)
			if any_hd_str != any_sd_str:
				logging.info("@any_sd_str %s [sd]" % any_sd_str)
		"""

		try:
			vcodec, acodec = MM.get_codecs(lf)
		except BaseException as e:
			vcodec = acodec = ""

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log(
				"debug get_codecs[error]", "%s [%s]" % (lf, str(e)), is_error=True
			)
		else:
			if vcodec != "h264":
				vcodec = "h264"  # mp4(video) # no_copy
			if acodec != "aac":
				acodec = "aac"  # aac(audio) # no_copy

		if all((vcodec, acodec)):
			write_log("debug get_codecs", "%s" % ",".join([lf, vcodec, acodec]))
		elif any((not vcodec, not acodec)):
			write_log(
				"debug codec[null]", "Нет данных codecs для %s" % lf
			)  # save_error_data # json/text

			continue  # skip_if_no_codecs

		try:
			profile, level = MM.get_profile_and_level(lf)
		except BaseException as e:
			profile = level = ""

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log(
				"debug get_profile_and_level[error]",
				"%s [%s]" % (lf, str(e)),
				is_error=True,
			)

		if all((profile, level)):
			# write_log("debug get_profile_and_level", ";".join([full_to_short(lf), profile, level]))
			write_log("debug get_profile_and_level", ";".join([lf, profile, level]))
		elif any((not profile, not level)):
			write_log("debug profilev[null]", "Нет данных profile/level для %s" % lf)

			continue  # skip_if_no_profile(no_level)

		# if "baseline" in profile and profile:  # baseline(low) ~> main(middle)
		# continue

		try:
			duration = MM.get_length(lf)
		except BaseException as e:
			duration = 0

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log("debug get_length[error]", "%s [%s]" % (lf, str(e)), is_error)

		if duration:
			hms_sum += duration
			hms_len += 1
			# write_log("debug duration", ";".join([hms(duration), full_to_short(lf)])) # save_only_with_time(json/is_sort)
			write_log(
				"debug duration", ";".join([hms(duration), lf])
			)  # save_only_with_time(json/is_sort)
		elif not duration:
			write_log(
				"debug duration[null]", "Нет данных duration для %s" % lf
			)  # try_remove_by_logic

			continue  # skip_if_no_duration

		# some_bitrate(self, filename, K: int = 0.25, width: int = 640, height: int = 480, fps: float = 15, ms: int = 1200)
		# (filename, width, height, fps, ms, sb)

		optimial_width: int = 0
		optimal_height: int = 0

		try:
			sb_calc = MM.some_bitrate(
				filename=lf,
				width=width,
				height=height,
				fps=MM.get_fps(lf),
				ms=MM.get_length(lf),
			)
			assert sb_calc, ""  # check_assert # is_assert_debug
		except AssertionError as err:
			sb_calc = ()
			print(Style.BRIGHT + Fore.RED + "%s" % lf)
			raise err
			logging.warning("debug some_bitrate[assert] %s" % lf)
		except BaseException as e:
			sb_calc = ()
			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			logging.error("debug some_bitrate[error] %s [%s]" % (lf, str(e)))
			write_log(
				"debug some_bitrate[error]", "%s [%s]" % (lf, str(e)), is_error=True
			)
		else:
			# debug some_bitrate:c:\downloads\new\Gruz_proshlogo_01s01e.mp4 [('c:\\downloads\\new\\Gruz_proshlogo_01s01e.mp4', 640, 360, 25, 2821, 1406.25)]
			write_log(
				"debug some_bitrate", "%s [%s]" % (lf, str(sb_calc))
			)  # is_vbr_calc # sb_calc[5] = 1406.25 # 1406 -> 1400

			vbr_status: str = ""

			# -b:v 1000K -maxrate 1000K -bufsize 2000K

			output_file = "".join([path_to_done, lf.split("\\")[-1]])
			try:
				if any(
					(width, height, sb_calc, width > sb_calc[1], height > sb_calc[2])
				):  # create_cmd_with_vbr(manual_run)
					cmd_vbr = (
						'cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i "%s" -preset medium -threads 2 -c:v libx264 -b:v %s -maxrate %s -bufsize %s -vf "scale=\'%d:%d\'" -threads 2 -c:a aac "%s"'
						% (
							sb_calc[0],
							"".join([str(int(sb_calc[5])), "k"]),
							"".join([str(int(sb_calc[5])), "k"]),
							"".join([str(int(sb_calc[5]) * 2), "k"]),
							sb_calc[1],
							sb_calc[2],
							output_file,
						)
					)  # cmd /k
					vbr_status = "full"
				elif all(
					(width, height, sb_calc, width == sb_calc[1], height == sb_calc[2])
				):  # skip_vbr
					cmd_vbr = (
						'cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i "%s" -preset medium -threads 2 -c:v libx264 -threads 2 -c:a aac "%s"'
						% (sb_calc[0], output_file)
					)  # cmd /k
					vbr_status = "short"
			except:
				cmd_vbr = ""
			finally:
				if cmd_vbr:
					write_log(
						"debug cmd_vbr[info]",
						"%s [%s] [%s]" % (lf, vbr_status, str(datetime.now())),
					)
					write_log("debug cmd_vbr[cmd]", "%s" % cmd_vbr)
				elif not cmd_vbr:
					write_log(
						"debug cmd_vbr[null]", "%s [%s]" % (lf, str(datetime.now()))
					)

			# hd # sd
			if 1000 >= int(sb_calc[-1]) >= 1500:
				optimal_height = 360
			elif 2500 >= int(sb_calc[-1]) >= 4000:
				optimal_height = 480
			elif 5000 >= int(sb_calc[-1]) >= 7500:
				optimial_height = 720
			elif 8000 >= int(sb_calc[-1]) >= 12000:
				optimal_height = 1080
			else:
				optimal_height = 360  # by_default

			if all((optimal_height, optimal_height != height)):  # logging_if_another
				try:
					optimal_width = (width / height) * optimal_height
					assert (
						width and height
					), f"Высота или ширина указаны не верно @optimal_width/{width}/{height}"  # is_assert_debug
				except AssertionError as err:
					optimal_width = None
					logging.warning(
						f"Высота или ширина указаны не верно @optimal_width/{width}/{height}"
					)
					raise err
				except ZeroDivisionError:
					optimal_width = None

				if not isinstance(optimal_width, int) and optimal_width != None:
					optimal_width = int(optimal_width)

				# debug optimal[filename/width/height/date]:c:\downloads\new\Razorvannije_01s03e.mp4, 677.6470588235294x360 [2023-03-16 20:56:08.271600]
				write_log(
					"debug optimal[filename/width/height/date]",
					"%s, %s [%s]"
					% (
						lf,
						"x".join([str(optimal_width), str(optimal_height)]),
						str(datetime.today()),
					),
				)

			# debug current[filename/width/height/date]:c:\downloads\new\Gruz_proshlogo_01s01e.mp4, 640x360 [2023-03-16 20:55:31.352128]
			write_log(
				"debug current[filename/width/height/date]",
				"%s, %s [%s]"
				% (lf, "x".join([str(width), str(height)]), str(datetime.today())),
			)

		try:
			with open(vbr_base, encoding="utf-8") as vbf:
				vbr_dict = json.load(vbf)
		except:
			vbr_dict = {}

			with open(vbr_base, "w", encoding="utf-8") as vbf:
				json.dump(vbr_dict, vbf, ensure_ascii=False, indent=4)

		try:
			vbr_dict[lf.strip()] = int(sb_calc[-1])  # save_vbr_for_job
		except:
			vbr_dict[lf.strip()] = 0  # if_error_vbr_null

		# update_list_to_int
		try:
			vbr_update = {
				k: int(v[0]) if isinstance(v, list) else int(v)
				for k, v in vbr_dict.items()
			}  # list -> int # is_no_lambda
		except:
			vbr_update = {}

		if vbr_update:
			vbr_dict.update(vbr_update)

		vbr_dict = {k: v for k, v in vbr_dict.items() if os.path.exists(k)}  # exists

		with open(vbr_base, "w", encoding="utf-8") as vbf:
			json.dump(vbr_dict, vbf, ensure_ascii=False, indent=4)

		try:
			vbr = MM.calc_vbr(filename=lf, width=width, height=height)  # -b:v aaaK
		except BaseException as e:
			vbr = 0

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log("debug calc_vbr[error]", "%s [%s]" % (lf, str(e)), is_error=True)
		finally:
			if any((vbr, sb_calc)):
				# write_log("debug calc_vbr", ";".join([full_to_short(lf), str(vbr), str(sb_calc)]))
				write_log(
					"debug calc_vbr", ";".join([lf, str(vbr), str(sb_calc)])
				)  # filename / calc_vbr / calc_vbr2(None)
			elif not vbr:
				write_log("debug calc_vbr[null]", "Нет данных vbr для %s" % lf)

		"""
		Тип;Битрейт видео, стандартная частота кадров (24, 25, 30);Битрейт видео, высокая частота кадров (48, 50, 60);Vbr1;Vbr2
		2160p (4К);35–45 Мбит/с;53–68 Мбит/с;45000;68000
		1440p (2К);16 Мбит/c;24 Мбит/c;16000;24000
		***
		# @csv
		1080p;8 Мбит/c;12 Мбит/c;8000;12000
		720p;5 Мбит/c;7,5 Мбит/c;5000;7500
		480p;2,5 Мбит/c;4 Мбит/c;2500;4000
		360p;1 Мбит/c;1,5 Мбит/c;1000;1500
		"""

		height_to_vbr_sd: dict = {}
		height_to_vbr_hd: dict = {}

		height_to_vbr_sd[360] = 1000
		height_to_vbr_sd[480] = 2500
		height_to_vbr_sd[720] = 5000
		height_to_vbr_sd[1080] = 8000
		height_to_vbr_sd[1440] = 16000
		height_to_vbr_sd[2160] = 45000

		height_to_vbr_hd[360] = 1500
		height_to_vbr_hd[480] = 4000
		height_to_vbr_hd[720] = 7500
		height_to_vbr_hd[1080] = 12000
		height_to_vbr_hd[1440] = 24000
		height_to_vbr_hd[2160] = 68000

		temp_vbr: int = 0

		try:
			fps = MM.get_fps(lf)
		except:
			fps = 0
		else:
			# need_setup_for_fps
			if 23 <= fps <= 30:
				try:
					if all((height, height_to_vbr_sd[height])):  # default/calc(+dict)
						temp_vbr = height_to_vbr_sd[height]
				except:
					temp_vbr = vbr

			elif 48 <= fps <= 60:
				try:
					if all((height, height_to_vbr_hd[height])):  # default/calc(+dict)
						temp_vbr = height_to_vbr_hd[height]
				except:
					temp_vbr = vbr

			if all((vbr < temp_vbr, vbr, temp_vbr)):
				write_log(
					"debug calc_vbr[change]",
					"[%s] [vbr:%s] ~> [vbr:%s]" % (lf, str(vbr), str(temp_vbr)),
				)  # old(vbr) -> new(vbr)
				vbr = temp_vbr

			if all((vbr == temp_vbr, vbr, temp_vbr)):
				write_log(
					"debug calc_vbr[not_change]",
					"[%s] [fps:%s] [vbr:%s]" % (lf, str(fps), str(vbr)),
				)  # not_change_vbr

		try:
			gop = MM.get_gop(filename=lf, fps=fps)
		except:
			gop = 0

		try:
			abr = MM.lossy_audio(filename=lf, audio_format=acodec)
		except:
			abr = 0

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log("debug lossy_audio[error]", "%s [%s]" % (lf, str(e)))

		"""
		Тип(Канал);Битрейт аудио
		Моно;128 кбит/с
		Стерео;384 кбит/с
		5.1;512 кбит/с
		"""

		try:
			with open(abr_base, encoding="utf-8") as abf:
				abr_dict = json.load(abf)
		except:
			abr_dict = {}

			with open(abr_base, "w", encoding="utf-8") as abf:
				json.dump(abr_dict, abf, ensure_ascii=False, indent=4, sort_keys=True)

		temp_abr: int = 0

		try:
			cl = MM.get_channels(lf)
		except:
			cl = 0
		else:
			if cl == 1 and abr < 128:  # mono(<128)
				temp_abr = 128

			elif cl == 2 and abr < 384:  # stereo(<384)
				temp_abr = 384

			elif cl == 5 and abr < 512:  # 5.1(<512)
				temp_abr = 512

			if all((abr != temp_abr, abr, temp_abr)):
				write_log(
					"debug lossy_audio[change]",
					"[abr:%s] ~> [abr:%s]" % (str(abr), str(temp_abr)),
				)  # old(abr) -> new(abr)
				abr = temp_abr

			if all((abr == temp_abr, abr, temp_abr)):
				write_log(
					"debug lossy_audio[not_change]", "[abr:%s]" % str(abr)
				)  # not_change_abr

		if abr:
			# write_log("debug lossy_audio", ";".join([full_to_short(lf), str(abr)]))
			write_log("debug lossy_audio", ";".join([lf, str(abr)]))
			abr_dict[lf.strip()] = abr

			with open(abr_base, "w", encoding="utf-8") as abf:
				json.dump(abr_dict, abf, ensure_ascii=False, indent=4, sort_keys=True)
		elif not abr:
			write_log("debug lossy_audio[null]", "Нет данных abr для %s" % lf)

			continue  # skip_if_no_abr

		try:
			is_meta = MM.get_meta(lf)
		except:
			is_meta = False
		finally:
			if is_meta:
				print(
					Style.BRIGHT + Fore.GREEN + "Получены мета-данные по файлу:",
					Style.BRIGHT + Fore.WHITE + "%s" % lf,
				)
				write_log("debug donemeta", "Получены мета-данные по файлу: %s" % lf)
			elif not is_meta:
				print(
					Style.BRIGHT + Fore.RED + "Ошибка мета-данных по файлу:",
					Style.BRIGHT + Fore.WHITE + "%s" % lf,
				)
				write_log(
					"debug donemeta[error]", "Ошибка мета-данных по файлу: %s" % lf
				)

			# continue

		# Quality of each frame # a = 1.234 # "%s" % str(round(a,2))[0:] # '1.23'
		try:
			fq = MM.get_frame_quality(lf)
		except:
			fq = 0
			print(
				Style.BRIGHT + Fore.RED + "Размер фрейма: не определен, для файла: ",
				Style.BRIGHT + Fore.WHITE + "%s" % fname,
			)
			write_log(
				"debug frame[quality][error]",
				"Размер фрейма файла [%s]: не определен" % fname,
			)
		else:
			if fq:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "Размер фрейма: %s, для файла: " % str(round(fq, 2))[0:],
					Style.BRIGHT + Fore.WHITE + "%s" % fname,
				)
				write_log(
					"debug frame[quality]",
					"Размер фрейма файла [%s]: %s" % (fname, str(round(fq, 2))[0:]),
				)

		cnt += 1

		try:
			prc = int(cnt // (max_cnt / 100))
		except:
			break
		else:
			if all((abs(prc) <= 100, not prc in prc_set, cnt <= max_cnt)):
				prc_set.add(prc)

				if all((fname, cnt)):  # last_shortname/total_count_data
					print(
						Style.BRIGHT
						+ Fore.YELLOW
						+ "Обработанно %d процентов данных." % prc,
						Style.BRIGHT + Fore.WHITE + "[%s/%d]" % (fname, cnt),
					)
					write_log(
						"debug datacount",
						"Обработанно %d процентов данных. [%s/%d]" % (prc, fname, cnt),
					)

		# --- Command line and base and need change (new/update) ---
		# if all((width, height, vcodec, vbr, acodec, profile, level)):  # hide_logic # is_360p

		print(
			Style.BRIGHT + Fore.WHITE + "Файл: %s" % fname,
			Style.BRIGHT
			+ Fore.GREEN
			+ "%s"
			% ";".join(
				[
					str(width),
					str(height),
					vcodec,
					str(vbr),
					acodec,
					str(abr),
					profile,
					level,
					full_to_short(lf),
				]
			),
		)

		# debug metaparam:640;360;h264;1000;aac;384;high;30;d:\multimedia\video\serials_conv\Kvantoviy_skachyok\Kvantoviy_skachyok_01s01e.mp4
		write_log(
			"debug metaparam",
			"%s"
			% ";".join(
				[
					str(width),
					str(height),
					vcodec,
					str(vbr),
					acodec,
					str(abr),
					profile,
					level,
					lf,
				]
			),
		)

		# load_meta_jobs(filter) #10
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(
					somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
				)
		finally:
			some_files: list = (
				[*somebase_dict] if somebase_dict else []
			)  # list(somebase_dict.keys()) # is_no_lambda

		some_files = (
			some_files[0:1000] if len(some_files) >= 1000 else some_files
		)  # no_limit(if_hide) # (6)

		# scale=640:360:flags=lanczos,pad=640:480:0:60 # scale=1440:1080:flags=lanczos,pad=1920:1080:240:0

		scale_regex = re.compile(
			r"(scale=[\d+]\:[\d+]\:flags\=lanczos)", re.I
		)  # hd_to_sd # ,pad=[\d+]\:[\d+]\:0\:[\d+] # skip_pad
		scale_regex2 = re.compile(
			r"(scale=[\d+]\:[\d+]\:flags\=lanczos)", re.I
		)  # sd_to_hd # ,pad=[\d+]\:[\d+]\:[\d+]\:0) # skip_pad

		# sd_scale
		try:
			scale1 = (
				scale_regex.sub("", hd_sd) if scale_regex.sub("", hd_sd) else ""
			)  # sd # cmd # is_no_lambda
		except:
			scale1 = ""

		# hd_scale
		try:
			scale2 = (
				scale_regex2.sub("", sd_hd) if scale_regex2.sub("", sd_hd) else ""
			)  # hd # cmd # is_no_lambda
		except:
			scale2 = ""

		# all_scales/some_scales/no_scales(by_aratio)
		try:
			scales = ":".join([scale1, scale2])  # scales(sd/hd) # cmd:cmd
		except:
			scales = ""
		else:
			write_log("debug scales", "%s [%s]" % (scales, lf))

		# 640;356;h264;None;aac;None;high;30 # check_streams_"and_format"_from_meta # separataros = ["+", ":", "!", "?"] # new # is_new # is_ready # is_error

		try:
			if all((is_change, width == 640)) and any(
				(
					vcodec.lower().strip() != "h264",
					acodec.lower().strip() != "aac",
					any(
						(
							profile.lower().strip() != "main",
							not "main" in profile.lower().strip(),
						)
					),
					int(level) != 30,
				)
			):  # logic(1_of_4)

				# --- is_new ---

				try:
					write_log(
						"debug somebase_dict[1]",
						"%s [%s] [%s]"
						% (
							lf.strip(),
							"+".join(
								[
									str(width),
									str(height),
									vcodec,
									str(vbr),
									acodec,
									str(abr),
									profile,
									level,
									scales,
								]
							),
							str(datetime.now()),
						),
					)  # filename / param / datetime
				except BaseException as e:
					write_log(
						"debug somebase_dict[1][error]",
						"%s [%s] [%s]" % (lf.strip(), str(e), str(datetime.now())),
						is_error=True,
					)  # filename / error / datetime
				else:
					# 640+266+h264+170+aac+384+high+30 # vcodec(!h264) # acodec(!aac) # profile(!main)
					# {filename: [width+height+vcodec+vbr+acodec+abr+profile+level+scales]}
					somebase_dict[lf.strip()] = "+".join(
						[
							str(width),
							str(height),
							vcodec,
							str(vbr),
							acodec,
							str(abr),
							profile,
							level,
							scales,
						]
					)  # new(add)

			elif all((is_change == False, width <= 640)) and all(
				(
					vcodec.lower().strip() == "h264",
					acodec.lower().strip() == "aac",
					any(
						(
							profile.lower().strip() == "main",
							"main" in profile.lower().strip(),
						)
					),
					all((int(level) > 0, int(level) <= 30)),
				)
			):  # logic(2_of_4)

				# --- is_ready ---

				# hide_ready_from_logging
				"""
				try:
						# write_log("debug somebase_dict[2]", "%s [%s] [%s]" % (full_to_short(lf.strip()), "ready", str(datetime.now()))) # filename / is_status / datetime
						write_log("debug somebase_dict[2]", "%s [%s] [%s]" % (lf.strip(), "ready", str(datetime.now()))) # filename / is_status / datetime
				except BaseException as e:
						write_log("debug somebase_dict[2][error]", "%s [%s] [%s]" % (lf.strip(), str(e), str(datetime.now()))) # filename / error / datetime
				else:
						# somebase_dict[lf.strip()] = "!".join([str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, scales])
						# {filename: [width!height!vcodec!vbr!acodec!abr!profile!level!scales]}
				"""

				somebase_dict = {
					k: v for k, v in somebase_dict.items() if os.path.exists(k)
				}  # exists_only # pass_1_of_2
				somebase_dict = {
					k: v
					for k, v in somebase_dict.items()
					if all((k, lf, k.strip() != lf.strip()))
				}  # delete_current(is_ready) # is_ready(clean) # pass_2_of_2
				# somebase_dict.pop(lf)	# debug

				# @load_current_jobs
				try:
					with open(filecmd_base, encoding="utf-8") as fbf:
						fcmd = json.load(fbf)
				except:
					fcmd = {}

					with open(filecmd_base, "w", encoding="utf-8") as fbf:
						json.dump(
							fcmd, fbf, ensure_ascii=False, indent=4, sort_keys=False
						)

				first_len = len(fcmd)

				if all((fcmd, somebase_dict)):
					fcmd = {
						k: v
						for k, v in fcmd.items()
						if os.path.exists(k)
						and any((k.strip() in [*somebase_dict], not [*somebase_dict]))
					}

				second_len = len(fcmd)

				if all(
					(fcmd, second_len <= first_len)
				):  # filter_ready_and_not_optimize_jobs
					with open(filecmd_base, "w", encoding="utf-8") as fbf:
						json.dump(
							fcmd, fbf, ensure_ascii=False, indent=4, sort_keys=False
						)

					write_log("debug fcmd[filter]", "%d" % len(fcmd))

			else:
				# --- (is_unknown) ---

				try:
					write_log(
						"debug somebase_dict[3]",
						"%s [%s] [%s]"
						% (
							lf.strip(),
							":".join(
								[
									str(width),
									str(height),
									vcodec,
									str(vbr),
									acodec,
									str(abr),
									profile,
									level,
									scales,
								]
							),
							str(datetime.now()),
						),
					)  # filename / param / datetime
				except:
					write_log(
						"debug somebase_dict[3][error]",
						"%s [%s] [%s]" % (lf.strip(), str(e), str(datetime.now())),
					)  # filename / error / datetime
				else:
					if any(
						(
							vcodec.lower().strip() != "h264",
							acodec.lower().strip() != "aac",
						)
					) or any(
						(
							profile.lower().strip() != "main",
							not "main" in profile.lower().strip(),
						)
					):  # filter(vcodec/acodec/profile) # logic(3_of_4)

						# 640:360:h264:704:aac:384:high:30 # vcodec(!h264) # acodec(!aac) # profile(!main)
						# {filename: [width:height:vcodec:vbr:acodec:abr:profile:level:scales]}

						somebase_dict[lf.strip()] = ":".join(
							[
								str(width),
								str(height),
								vcodec,
								str(vbr),
								acodec,
								str(abr),
								profile,
								level,
								scales,
							]
						)  # not_optimized(add)
					elif all(
						(
							vcodec.lower().strip() == "h264",
							acodec.lower().strip() == "aac",
							any(
								(
									profile.lower().strip() == "main",
									"main" in profile.lower().strip(),
								)
							),
						)
					):  # filter(vcodec/acodec/profile) # logic(4_of_4)
						somebase_dict = {
							k: v for k, v in somebase_dict.items() if os.path.exists(k)
						}  # exists_only # pass_1_of_2
						somebase_dict = {
							k: v
							for k, v in somebase_dict.items()
							if k.strip() != lf.strip()
						}  # delete_current(is_optimized) # is_optimized(clean) # pass_2_of_2

		except BaseException as e:

			# --- is_error ---

			try:
				write_log(
					"debug somebase_dict[4]",
					"%s [%s] [%s] [%s]"
					% (
						lf.strip(),
						"?".join(
							[
								str(width),
								str(height),
								vcodec,
								str(vbr),
								acodec,
								str(abr),
								profile,
								level,
								scales,
							]
						),
						str(e),
						str(datetime.now()),
					),
					is_error=True,
				)  # error_with_param # filename / param / error / datetime
			except:
				write_log(
					"debug somebase_dict[4][error]",
					"%s [%s] [%s]" % (lf.strip(), str(e), str(datetime.now())),
					is_error=True,
				)  # error_without_param # filename / error / datetime

		with open(some_base, "w", encoding="utf-8") as sbf:
			json.dump(somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True)

		# find_logic(debug/test)

		# skip_only_resized # skip_if_profile(-profile:v main) # skip_any_level(-level 30) # is_ffmpeg(param)

		# (is_resized)&(profile:v main)&(level 30) # is_slow(0 - change_all) # (is_resized)(profile:v high)(level 40) # is_fast(1 - only_resize)
		try:
			if all(
				(
					is_change == False,
					any(
						(
							"main" in profile.lower().strip(),
							profile.lower().strip() == "main",
						)
					),
					int(level) == 30,
				)
			):  # resized/profile/level # no_params
				continue
		except BaseException as e:
			print(
				Style.BRIGHT + Fore.RED + "Ошибка оптимизации файла",
				Style.BRIGHT + Fore.WHITE + "%s [%s]" % (lf, str(e)),
			)

			write_log(
				"debug status[resize/profile/level][error]",
				"Ошибка оптимизации файла %s [%s]" % (lf, str(e)),
				is_error=True,
			)
		else:
			print(
				Style.BRIGHT + Fore.CYAN + "Оптимизация файла",
				Style.BRIGHT + Fore.WHITE + "%s" % lf,
			)

			write_log("debug status[resize/profile/level]", "Оптимизация файла %s" % lf)

		# get_data_for_metadict_and_skip_run_if_resized(pass_2_of_2)

		vfile = "libx264"  # "libx264" if vcodec != "h264" else "copy"  # is_change # mp4(video) # no_copy
		afile = "aac"  # "aac" if acodec != "aac" else "copy"  # is_change # aac(audio) # no_copy

		try:
			is_profile = (
				True
				if any(
					(
						not "main" in profile.lower().strip(),
						profile.lower().strip() != "main",
					)
				)
				else False
			)  # profile.lower().strip() != "main"  # high -> main(middle) / baseline(low) -> main(middle)
		except:
			continue  # "main" in profile.lower()

		try:
			is_level = True if int(level) > 30 else False  # is_no_lambda
		except:
			continue  # level == None

		try:
			svbr = (
				"".join([str(vbr), "K"]) if vbr else ""
			)  # if len(str(cbr)) <= 3 else "".join([str((cbr)), "M"])
		except:
			svbr = ""

		try:
			svbr2 = (
				"".join([str(vbr * 2), "K"]) if vbr else ""
			)  # if len(str(cbr*2)) <= 3 else "".join([str((cbr*2)), "M"])
		except:
			svbr2 = ""

		try:
			sabr = (
				"".join([str(abr), "K"]) if abr else ""
			)  # if len(str(abr)) <= 3 else "".join([str((abr)), "M"])
		except:
			sabr = ""

		bitrate_data = all((svbr, svbr2, sabr))

		project_file = "".join([path_to_done, fname])

		cmd_file = cmd_file2 = ""  # default/with_vbr

		year_regex = re.compile(r"([\d+]{4})")

		# no_change_high_to_main(is_profile)_for_high # optimal_level(is_level)_for_30 # -profile:v high -level 30 # is_manual_run
		# map_metadata -1(hide_metadata) # optimal_hide_all_attributes
		# map_metadata 0(edit_or_hide_tags_by_keys) # ffmpeg -i test.mp4 -map_metadata 0 -metadata creation_time="2020-07-30 12:59:20" -c copy C.mp4
		# map_metadata 1(insert_metadata_attributes(m4a->mp3) #  ffmpeg -i "02 Napali.m4a" -i metadata.txt -map_metadata 1 -c:a libmp3lame -ar 44100 -b:a 192k -id3v2_version 3 -f mp3 "02 Napali.mp3"

		try:
			with open(vbr_base, encoding="utf-8") as vbf:
				vbr_dict = json.load(vbf)
		except:
			vbr_dict = {}

		try:
			with open(abr_base, encoding="utf-8") as abf:
				abr_dict = json.load(abf)
		except:
			abr_dict = {}

		# update_path_base_before_meta_parameters
		pathbase_dict[lf.strip()] = (
			"True" if is_change else "False"
		)  # is_change_status(json)
		pathbase_dict_str = ";".join([pathbase_dict[lf.strip()], lf])  # filename_2types

		is_change_status = (
			("debug is_changed[+]", "%s" % pathbase_dict_str)
			if is_change
			else ("debug is_changed[-]", "%s" % pathbase_dict_str)
		)

		# new # debug
		write_log(is_change_status[0], is_change_status[1])

		# '''
		# run_optimized / is_optimize(is_change == False, ...)
		# optimize_width/not_optimize_width # width*height # vcodec(acodec) # is_bitrate(svbr/svbr2/sabr)
		if all(
			(any((is_change, not is_change)), width, height, vfile, afile, bitrate_data)
		):

			# try_load_video_bitrate(if_ok_vbr_old)
			try:
				if all(
					(lf in [*vbr_dict], vbr_dict[lf] >= int(bitrate_data[0]))
				):  # int(svbr) -> int(bitrate_data[0])
					svbr, svbr2 = str(vbr_dict[lf]), str(vbr_dict[lf] * 2)
			except:
				svbr = svbr2 = ""  # pass

			# try_load_audio_bitrate(if_ok_abr_old)
			try:
				if all(
					(lf in [*abr_dict], abr_dict[lf] >= int(bitrate_data[2]))
				):  # int(sabr) -> int(bitrate_data[2])
					sabr = str(abr_dict[lf])
			except:
				sabr = ""  # pass

			# brightness # eq/pp/...

			# skip_subtitles # ffmpeg input -sn -threads 2 -c:v libx264 -threads 2 -c:a aac output
			# no_skip_subtitles # ffmpeg input -threads 2 -c:v libx264 -threads 2 -c:a aac output # default

			# is_add_meta
			# @generate_parameters_for_job

			# new/update: width/height, h264, vbr, aac/copy, main, 30, $file$
			# vcodec/acodec(by_bitrate)
			# unknown_convert = ";".join([str(width), str(height), vcodec, svbr, acodec, profile, level, lf])

			# logging.warning("debug unknown_parameters_or_is_ready %s" % unknown_convert) #line1
			# write_log("debug unknown_parameters_or_is_ready", "%s" % unknown_convert)  # machine_learning

			# lf, vfile, str(width), str(height), afile, project_file
			# lf, vfile, svbr, svbr, svbr2, str(width), str(height), afile, sabr, project_file

			# @add_meta[is_debug] {'acodec': 'aac', 'afile': 'aac', 'height': '360', 'is_change': True, 'is_level': [True, '31'],
			# 'is_profile': [True, 'high'], 'lf': 'd:\\multimedia\\video\\serials_europe\\Golos_Rus\\Golos_12s02e.mp4',
			# 'project_file': 'c:\\downloads\\Golos_12s02e.mp4', 'sabr': '384K', 'svbr': '1000K', 'svbr2': '2000K',
			# 'vcodec': 'h264', 'vfile': 'libx264', 'width': '640', 'year_regex': []} [2024-01-27 23:53:43.568841]

			param_dict: dict = {}
			param_dict["acodec"] = acodec
			param_dict["afile"] = afile.strip()
			param_dict["height"] = str(height)
			param_dict["is_change"] = is_change
			param_dict["is_level"] = [is_level, level]
			param_dict["is_profile"] = [is_profile, profile]
			param_dict["lf"] = lf.strip()
			param_dict["project_file"] = project_file.strip()

			if sabr:
				param_dict["sabr"] = sabr
			if svbr:
				param_dict["svbr"] = svbr
			if svbr:
				param_dict["svbr2"] = svbr2

			param_dict["vcodec"] = vcodec
			param_dict["vfile"] = vfile.strip()
			param_dict["width"] = str(width)
			param_dict["year_regex"] = year_regex.findall(lf.split("\\")[-1])

			init_ffmpeg = " ".join(
				["cmd /c", "".join([path_for_queue, "ffmpeg.exe"])]
			)  # cmd /k

			"""
			br_dict: dict = {}
			br_record: bool = False
			abr = vbr = 0

			try:
				with open(br_base, encoding="utf-8") as bbf:
					br_dict = json.load(bbf)
			except:
				br_dict = {}
			else:
				if br_dict:
					for k, v in br_dict.items():
						try:
							if k.split("\\")[-1] == param_dict["project_file"].split("\\")[-1]:
								br_record = True
						except:
							br_record = False
						else:
							if br_record:
								vbr, abr = v[0], v[1]
							else:
								continue
			"""

			cmd_line: list = []  # withoutvbr/withoutabr
			# cmd_line2: list = [] # withvbr/withabr

			cmd_line.append(init_ffmpeg)

			# -hide_banner -y -i \"%s\" -map_metadata -1 -preset medium -threads 2 -c:v %s -vf \"scale=%s:%s\" -profile:v main -level 30 -movflags faststart -threads 2 -c:a %s -af \"dynaudnorm\" \"%s\"

			cmd_line.append('-hide_banner -y -i "%s"' % param_dict["lf"])
			cmd_line.append("-map_metadata -1")
			cmd_line.append("-preset medium")  # debug_speed
			cmd_line.append("-threads 2 -c:v %s" % param_dict["vfile"])

			# if vbr:
			# cmd_line2.extend(cmd_line)
			# cmd_line2.append("-b:v %dK" % vbr) # -maxrate / -minrate

			if all((param_dict["is_change"], width == 640, height)):
				cmd_line.append(
					'-vf "scale=%s:%s"' % (param_dict["width"], param_dict["height"])
				)

			if all(
				(
					param_dict["is_profile"][0],
					param_dict["is_profile"][1].lower() != "main",
				)
			):
				if any(
					(
						not "baseline" in param_dict["is_profile"][1].lower(),
						param_dict["is_profile"][1].lower() == "high",
					)
				):  # baseline < main, high > main
					cmd_line.append("-profile:v main")

			if all((param_dict["is_level"][0], int(param_dict["is_level"][1]) > 30)):
				cmd_line.append("-level 30")

			if not param_dict["year_regex"]:  # if_tvseries
				cmd_line.append("-movflags faststart")

			cmd_line.append("-threads 2 -c:a %s" % param_dict["afile"])

			# if abr:
			# cmd_line2.extend(cmd_line)
			# cmd_line2.append("-b:a %dK" % abr)

			cmd_line.append('-af "dynaudnorm"')
			cmd_line.append(
				'"%s"' % param_dict["project_file"]
			)  # try_with_quote(optimal_for_path)

			# movflags <-> is_debug

			if cmd_line:  # cmd_line2
				cmd_file = " ".join(cmd_line)
				# cmd_line2.extend(cmd_line)
				# cmd_file2 = " ".joint(cmd_line2)

			if cmd_file:  # is_command
				write_log(
					"debug need_optimize[is_command]", "%s" % param_dict["project_file"]
				)

				if param_dict["is_change"]:  # need_optimize(is_run) # green/yellow
					if any(
						(
							cmd_file.count("scale") > 0,
							cmd_file.count("profile") > 0,
							cmd_file.count("level") > 0,
						)
					):  # (s)/(p)/(l)
						print(
							Style.BRIGHT + Fore.GREEN + "%s" % cmd_file
						)  # need_optimize(debug) # green_if_new
						write_log("debug cmd_file[need_optimize]", "%s" % cmd_file)

						filecmdbase_dict[param_dict["lf"]] = cmd_file.strip()
					else:  # not_optimized # (no_scale/no_profile/no_level)
						print(
							Style.BRIGHT + Fore.YELLOW + "%s" % cmd_file
						)  # logging(debug)
						write_log("debug cmd_file[logging][1]", "%s" % cmd_file)
				elif not param_dict[
					"is_change"
				]:  # is_optimized(is_skip_but_run) # blue/cyan
					if any(
						(
							cmd_file.count("scale") > 0,
							cmd_file.count("profile") > 0,
							cmd_file.count("level") > 0,
						)
					):  # (s)/(p)/(l)
						print(
							Style.BRIGHT + Fore.BLUE + "%s" % cmd_file
						)  # need_run(debug) # yellow_if_optimized
						write_log("debug cmd_file[need_run]", "%s" % cmd_file)

						filecmdbase_dict[param_dict["lf"]] = cmd_file.strip()
					else:  # ready # (no_scale/no_profile/no_level)
						continue
						## print(Style.BRIGHT + Fore.CYAN + "%s" % cmd_file)
						# write_log("debug cmd_file[logging][2]", "%s" % cmd_file)
			elif not cmd_file:  # no_command
				write_log(
					"debug skip_run[no_command]", "%s" % param_dict["project_file"]
				)
				continue  # skip_run(no_command_line)

			if filecmdbase_dict[param_dict["lf"]]:  # if_add_job_by_optimize_status
				print(
					Style.BRIGHT
					+ Fore.WHITE
					+ "debug add_meta[is_debug] %s [%s]"
					% (str(param_dict), str(datetime.now()))
				)  # yellow_if_another_parameters(no_style)
				logging.warning(
					"@add_meta[is_debug] %s [%s]"
					% (str(param_dict), str(datetime.now()))
				)  # line1
				write_log(
					"debug add_meta[is_debug]",
					"%s [%s]" % (str(param_dict), str(datetime.now())),
				)

		# '''

	if fext_dict:
		write_log("debug jobs[ext]", "%s" % str(fext_dict))  # dict_to_str(ext_count)

	del MT

	# count_avg_by_sum_and_length

	if any((hms_sum, hms_len)):
		try:
			hms_avg: int = hms_sum // hms_len
		except:
			hms_avg: int = 0

		write_log(
			"debug hms_avg",
			"%s [%d] [%s]" % (hms(hms_avg), hms_len, str(datetime.now())),
		)  # avg_size_by_length(avg_framecount/convert_to_time) # length_data # datetime

	# not_mp4_format
	"""
	if another_list:
		try:
			temp = [";".join(al["file"]) for al in another_list if
					os.path.exists(al["file"][0].strip())]  # save_file_from_dict # debug/test
			temp2 = list(set(temp))
		except:
			temp2 = []
		else:
			if temp2:
				another_list = sorted(temp2, reverse=False)

				with open(path_for_queue + "another.lst", "w", encoding="utf-8") as palf:
					palf.writelines("%s\n" % al.strip() for al in another_list)  # write(any/mp4/local)
	"""

	del MM

	if filecmdbase_dict:

		write_log("debug run[mp4]", "%s" % str(datetime.now()))

		ready_and_move: dict = {}

		# filecmdbase_dict = {k:v for k, v in filecmdbase_dict.items() if any((v.count("scale") > 0, v.count("profile") > 0, v.count("level") > 0))}

		# get_short_filenames(findfiles/"jobdata") # debug/test

		# shorts_in_list(upgrade)
		try:
			# short_list = [crop_filename_regex.sub("", lf.split("\\")[-1]) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))] # equal
			short_list = list(
				set(
					[
						crop_filename_regex.sub("", lf.split("\\")[-1])
						.split("_")[0]
						.strip()
						if lf.split("\\")[-1].count("_") > 0
						else crop_filename_regex.sub("", lf.split("\\")[-1]).strip()
						for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
						if lf
					]
				)
			)  # match_or_equal
		except:
			short_list = []
		finally:
			short_list.sort(reverse=False)  # re_sort_before_by_string
			# short_list.sort(key=len, reverse=False) # re_sort_before_by_length

		if short_list:
			write_log("debug short", ";".join(short_list))  # short_files
			write_log("debug shortsave", "%d" % len(short_list))  # count_files

		fcmd_filter: list = []

		MM = MyMeta()  # 7

		for k, _ in filecmdbase_dict.items():

			try:
				assert (
					filecmdbase_dict
				), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
			except AssertionError as err:  # if_null
				logging.warning("Пустой словарь или нет задач filecmdbase_dict")
				raise err
				break
			except BaseException as e:
				logging.error(
					"Пустой словарь или нет задач filecmdbase_dict [%s]" % str(e)
				)
				break

			try:
				fileinfo = (k, MM.get_length(MM))
			except:
				pass  # continue
			else:
				fcmd_filter.append(fileinfo)

		fcmd_sorted_tuple = sorted(fcmd_filter, key=lambda fcmd_filter: fcmd_filter[1])

		if all((fcmd_sorted_tuple, len(fcmd_sorted_tuple) <= len(filecmdbase_dict))):
			filecmdbase_dict = {
				k: v
				for fst in fcmd_sorted_tuple
				for k, v in filecmdbase_dict.items()
				if os.path.exists(k) and fst[0].strip() == k.strip()
			}

		# '640+360+h264+704+aac+384+high+30+c:\\downloads\\mytemp\\ffmpeg -y -i \"d:\\multimedia\\video\\serials_conv\\Interview_With_The_Vampire\\Interview_With_The_Vampire_01s06e.mp4\" -threads 2 -c:v libx264 -vf \"scale=640:360:flags=lanczos,pad=640:480:0:60\" -threads 2 -c:a copy \"c:\\downloads\\Interview_With_The_Vampire_01s06e_360p_sd.mp4\"'
		# (st.count("+"), st.count(":")) # (8, 10)

		# '640:360:h264:704:aac:320:high:30:c:\\downloads\\mytemp\\ffmpeg -y -i \"d:\\multimedia\\video\\serials_conv\\King_of_Queens\\King_of_Queens_03s13e.mp4\" -threads 2 -c:v libx264 -vf \"scale=640:360:flags=lanczos,pad=640:480:0:60\" -threads 2 -c:a copy \"c:\\downloads\\King_of_Queens_03s13e_360p_sd.mp4\"'
		# (st.count("+"), st.count(":")) # (0, 18)

		# need_optimize_current_jobs_by_param
		filecmdbase_dict = {
			k: v
			for k, v in filecmdbase_dict.items()
			if any((v.count("scale") > 0, v.count("profile") > 0, v.count("level") > 0))
		}

		if filecmdbase_dict:  # filesize(optimize)_or_abc(default)_sort
			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(
					filecmdbase_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False
				)

		jobs_list = (
			sorted([*filecmdbase_dict], reverse=False) if [*filecmdbase_dict] else []
		)  # is_no_lambda

		is_rec = False

		new_rec: int = 0
		some_rec: int = 0

		if jobs_list:
			try:
				with open(jobs_base, encoding="utf-8") as fbf:
					files_dict = json.load(fbf)
			except:
				files_dict = {}

				with open(jobs_base, "w", encoding="utf-8") as fbf:
					json.dump(
						files_dict, fbf, ensure_ascii=False, indent=4, sort_keys=True
					)

			else:
				# with unique_semaphore:
				for jl in filter(lambda x: x, tuple(jobs_list)):

					try:
						assert jl and os.path.exists(
							jl
						), f"Файл отсутствует {jl}"  # is_assert_debug # jl
					except AssertionError as err:  # if_null
						logging.warning("Файл отсутствует %s" % jl)
						raise err
						continue
					except BaseException as e:  # if_error
						logging.error("Файл отсутствует %s [%s]" % (jl, str(e)))
						continue

					try:
						fname = jl.split("\\")[-1]
					except:
						fname = ""
						continue

					is_rec = False

					try:
						is_rec = (
							True if files_dict[jl.strip()] else False
						)  # is_no_lambda
					except:
						files_dict[jl.strip()] = str(
							datetime.now()
						)  # if_error(KeyError)
						new_rec += 1
					else:
						if not is_rec:  # if_no_file(update_rec)
							files_dict[jl.strip()] = str(
								datetime.now()
							)  # new_rec(no_error)
							new_rec += 1
						elif is_rec:
							some_rec += 1

			if any((new_rec, some_rec)):
				print(
					"Из %d файлов, новых %d и известных %d файлов"
					% (len(jobs_list), new_rec, some_rec)
				)
				write_log(
					"debug new_rec/some_rec",
					"Из %d файлов, новых %d и известных %d файлов"
					% (len(jobs_list), new_rec, some_rec),
				)

			if files_dict:
				first_len = len(files_dict)

				files_dict = {k: v for k, v in files_dict.items() if os.path.exists(k)}

				second_len = len(files_dict)

				if all((files_dict, second_len <= first_len)):
					with open(jobs_base, "w", encoding="utf-8") as fbf:
						json.dump(
							files_dict,
							fbf,
							ensure_ascii=False,
							indent=4,
							sort_keys=True,
						)

		# null_command_line_script

		open(
			"c:\\downloads\\mytemp\\jresize.cmd", "w"
		).close()  # stay_current_jobs_no_hidden(manual_run)

		# learn_to_count
		scale_count: int = 0
		profile_count: int = 0
		level_count: int = 0

		s_c: int = 0
		p_c: int = 0
		l_c: int = 0

		# nob_dict: dict = {}

		try:
			with open(new_optimize_base, encoding="utf-8") as nobf:
				nob_dict = json.load(nobf)
		except:
			nob_dict = {}

			with open(new_optimize_base, "w", encoding="utf-8") as nobf:
				json.dump(nob_dict, nobf, ensure_ascii=False, indent=4, sort_keys=True)

		# nob_dict = {k:v for k, v in nob_dict.items() if os.path.exists(k) and all((sum(v) > 0, len(v) == 3))} # 1/2/3 # default(length=3) # skip_try_except
		nob_dict = {
			k: v for k, v in nob_dict.items() if os.path.exists(k)
		}  # without_length # skip_try_except

		s_p_l_set = set()  # int -> str

		for k, v in filecmdbase_dict.items():

			try:
				assert (
					filecmdbase_dict
				), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
			except AssertionError as err:  # if_null
				logging.warning("Пустой словарь или нет задач filecmdbase_dict")
				raise err
				break
			except BaseException as e:  # if_error
				logging.error(
					"Пустой словарь или нет задач filecmdbase_dict [%s]" % str(e)
				)
				break

			write_log(
				"debug filecmdbase_dict[job][index]",
				"%s"
				% "x".join(
					[
						k.strip(),
						str(v.count("scale")),
						str(v.count("profile")),
						str(v.count("level")),
					]
				),
			)

			if all((k, v)):

				scale_count = v.count("scale")
				profile_count = v.count("profile")
				level_count = v.count("level")

				if scale_count:
					s_c += 1

				if profile_count:
					p_c += 1

				if level_count:
					l_c += 1

				is_new: bool = False

				if (
					not ";".join([str(s_c), str(p_c), str(l_c)]) in s_p_l_set
				):  # unique_only
					s_p_l_set.add(";".join([str(s_c), str(p_c), str(l_c)]))
					is_new = True
					nob_dict[k.strip()] = "x".join(
						[str(scale_count), str(profile_count), str(level_count)]
					)  # is_optimize(1 found, 0 not_found)
				else:
					continue  # skip_dublicate

				if is_new:
					print(
						Style.BRIGHT
						+ Fore.CYAN
						+ "%s\t(%s, %s, %s)" % (k.strip(), str(s_c), str(p_c), str(l_c))
					)  # scale_count -> s_c ...
					write_log(
						"debug filecmdbase_dict[count]",
						"%s\t(%s, %s, %s)" % (k.strip(), str(s_c), str(p_c), str(l_c)),
					)

		if any((s_c, p_c, l_c)):
			cnt_index = {"scale": s_c, "profile": p_c, "level": l_c}
			write_log("debug filecmdbase_dict[index]", "%s" % str(cnt_index))

		nob_dict = {k: v for k, v in nob_dict.items() if os.path.exists(k)}

		with open(new_optimize_base, "w", encoding="utf-8") as nobf:
			json.dump(nob_dict, nobf, ensure_ascii=False, indent=4, sort_keys=True)

		# with unique_semaphore:
		# for k, v in filecmdbase_dict.items():
		# print(Style.BRIGHT + Fore.WHITE + "Файл %s будет обработан [level=%d]" % (k.strip(), count_level_from_full(k))) # level=6

		# if filecmdbase_dict:
		# print()

		sorted_files = list(filecmdbase_dict.keys())  # sort_current_jobs(pass_1_of_2)

		unique = full_list = set()
		try:
			# tmp = list(sf_gen()) # new(yes_gen)
			tmp: list = list(
				set(
					[
						sf.strip()
						for sf in filter(
							lambda x: os.path.exists(x), tuple(sorted_files)
						)
						if sf
					]
				)
			)
		except:
			tmp: list = []
		finally:
			sorted_files = sorted(tmp, reverse=False)  # sort_by_string
			# sorted_files = sorted(tmp, key=len, reverse=False) # sort_by_length

		for sf in tuple(sorted_files):

			if not sorted_files:  # skip_if_nulllist
				break

			try:
				fp, fn = split_filename(sf)
			except:
				fn = sf.split("\\")[-1].strip()  # fp

			try:
				fname = fn
			except:
				fname = ""
				continue

			if all((not fname in unique, fname)):
				unique.add(fname)  # short_file(first)_by_set
				full_list.add(sf)  # full_filename(first)_by_set
		if full_list:
			temp = list(set(full_list))  # unique_filenames
			sorted_files = sorted(temp, reverse=False)

		def files_to_short_by_full(sorted_files=sorted_files):  # 6
			for sf in filter(lambda x: os.path.exists(x), tuple(sorted_files)):
				if all((sf, crop_filename_regex.sub("", sf.split("\\")[-1]))):
					if sf:
						yield sf.strip()
					else:
						yield ""
				else:
					yield ""

		try:
			tmp: list = list(files_to_short_by_full())  # new(yes_gen)
		except:
			tmp: list = []
		finally:
			sorted_files = sorted(tmp, reverse=False)  # sort_by_string
			# sorted_files = sorted(tmp, key=len, reverse=False) # sort_by_length

		try:
			temp: list = asyncio.run(
				filter_from_list(sorted_files)
			)  # current_jobs + base
		except:
			temp: list = []
		else:
			if temp:
				temp2 = list(set(temp))  # unqiue_no_dublicates
				sorted_files = sorted(temp2, reverse=False)

		# @save_current_jobs(exists)
		if sorted_files:
			sort_dict: dict = {}
			sort_dict = {sf: str(datetime.now()) for sf in sorted_files}

			with open(backup_base, "w", encoding="utf-8") as bbf:
				json.dump(sort_dict, bbf, ensure_ascii=False, indent=4, sort_keys=True)

			with open(files_base["backup"], "w", encoding="utf-8") as bjf:
				bjf.writelines(
					"%s\n" % cmd.strip()
					for cmd in filter(lambda x: x, tuple(sorted_files))
				)

		elif not sorted_files:  # exit_if_not_found_some_files
			exit()

		# save_command_line_script
		with open("c:\\downloads\\mytemp\\jresize.cmd", "a") as jcf:
			jcf.writelines(
				"%s\n" % cmd.strip()
				for cmd in filter(lambda x: x, tuple(filecmdbase_dict.values()))
			)  # save_all_cmd(for_run)

		ready_set = set()

		for k, v in filecmdbase_dict.items():

			try:
				assert (
					filecmdbase_dict
				), "Пустой список или нет задач filecmdbase_dict"  # is_assert_debug
			except AssertionError as err:  # if_null
				logging.warning("Пустой список или нет задач filecmdbase_dict")
				raise err
				break
			except BaseException as e:  # if_error
				logging.error(
					"Пустой список или нет задач filecmdbase_dict [%s]" % str(e)
				)
				break

			try:
				assert k and os.path.exists(
					k
				), f"Файл отсутствует {k}"  # is_assert_debug # k
			except AssertionError as err:  # if_null
				logging.warning("Файл отсутствует %s" % k)
				raise err
				continue
			except BaseException as e:  # if_error
				logging.error("Файл отсутствует %s [%s]" % (k, str(e)))
				continue

			try:
				fname1 = v.split(" ")[-1].split("\\")[-1].strip()
			except:
				fname1 = ""

			try:
				_, fn = split_filename(k)
			except:
				fn = k.split("\\")[-1].strip()  # fp

			try:
				fname2 = fn
			except:
				fname2 = ""

			if all((fname1 == fname2, fname1, fname2)):
				print(
					Style.BRIGHT + Fore.WHITE + "Файл %s" % fname1,
					Style.BRIGHT
					+ Fore.YELLOW
					+ "будет добавлен или обновлён после обработки",
				)
				write_log(
					"debug job[addupdate]",
					"Файл %s будет добавлен или обновлён после обработки" % fname1,
				)

				ready_and_move[v.split(" ")[-1].strip()] = k.strip()

		# run(["cmd", "/c", "c:\\downloads\\mytemp\\jresize.cmd"], shell=False) # command_line_script_to_run # old_script

		hours_set = set()

		# clean_hours_cfg_by_schedule # if_need_hide

		dt = datetime.now()

		if all(
			(dt.weekday() >= 0, dt.hour in range(9, 19))
		):  # any_day_in_job_time(9am-6pm)_to_default
			if os.path.exists(files_base["hours"]):
				os.remove(files_base["hours"])

		try:
			with open(files_base["hours"], encoding="utf-8") as fbhf:
				max_hour_list = fbhf.readlines()
		except:
			max_hour_list = [4]  # default = 4

			with open(files_base["hours"], "w", encoding="utf-8") as fbhf:
				fbhf.writelines(
					"%d\n" % int(mhl)
					for mhl in filter(lambda x: x, tuple(max_hour_list))
				)  # save_total_time_run_by_hour

		if max_hour_list:  # hour_variables
			temp = list(
				set(
					[
						int(mhl)
						for mhl in filter(lambda x: x, tuple(max_hour_list))
						if all((int(mhl) >= 0, mhl != None))
					]
				)
			)  # hours_list(string)
			max_hour_list = sorted(temp, reverse=False)  # abc(by_hours)

		try:
			max_hour = int(max(max_hour_list, key=int))  # get_max_hour(str -> int)
		except:
			max_hour = 0
		else:
			if all((len(hours_set) <= max_hour, max_hour)):  # max_hour > 0 # max(1..x)
				with open(files_base["hours"], "w", encoding="utf-8") as fbhf:
					fbhf.write("%d\n" % max_hour)

			elif all((len(hours_set) > max_hour, hours_set)):  # hour_set > 0 # 1..x
				max_hour = len(hours_set)  # hour_by_length

				with open(files_base["hours"], "w", encoding="utf-8") as fbhf:
					fbhf.write("%d\n" % max_hour)

		prc: int = 0
		cnt: int = 0
		max_cnt: int = len(filecmdbase_dict)

		date1 = datetime.now()

		epis_regex = re.compile(r"([\d+]{2}e)", re.I)
		year_regex = re.compile(r"\(([\d+]{4})\)", re.I)

		epis_filter: list = []
		year_filter: list = []

		try:
			epis_filter: list = list(
				set(
					[
						epis_regex.findall(k.split("\\")[-1])[0].strip()
						for k in [*filecmdbase_dict]
						for fp, fn in split_filename(k)
						if ((fn, k, fn == k.split("\\")[-1], epis_regex.findall(fn)))
					]
				)
			)  # for k, _ in filecmdbase_dict.items()
		except:
			epis_filter: list = []
		finally:
			epis_filter.sort(reverse=False)

		try:
			year_filter: list = list(
				set(
					[
						year_regex.findall(k.split("\\")[-1])[0].strip()
						for k in [*filecmdbase_dict]
						for fp, fn in split_filename(k)
						if all((fn, k, fn == k.split("\\")[-1], year_regex.findall(fn)))
					]
				)
			)  # for k, _ in filecmdbase_dict.items()
		except:
			year_filter: list = []
		finally:
			year_filter.sort(reverse=False)

		error1 = error2 = False

		combine_filter: list = []

		try:
			combine_filter += epis_filter
		except BaseException as e:
			error1 = True
			write_log("debug combine_filter[epis_filter]", "%s" % str(e), is_error=True)

		try:
			combine_filter += year_filter
		except BaseException as e:
			error2 = True
			write_log("debug combine_filter[year_filter]", "%s" % str(e), is_error=True)

		if any((error1, error2)):
			combine_filter = []

		if combine_filter:
			tmp = list(set(combine_filter))

			combine_filter = sorted(tmp, reverse=False)  # sort_by_abc
			# combine_filter = sorted(tmp, key=len, reverse=False) # sort_by_key

			filecmdbase_dict_new = {
				k: v
				for cf in combine_filter
				for k, v in filecmdbase_dict.items()
				if all((cf, k, v, cf in k.split("\\")[-1].strip()))
			}

			if all(
				(
					filecmdbase_dict_new,
					len(filecmdbase_dict_new) <= len(filecmdbase_dict),
				)
			):  # filecmdbase_dict
				filecmdbase_dict.update(filecmdbase_dict_new)

			write_log("debug combine_filter", "%s" % ";".join(combine_filter))

		# debug
		# exit() # is_manual_run(stop)

		if (
			filecmdbase_dict
		):  # seas_year_filter(combine_filter) # jobs # filter_by_base(tmp_combine_jobs)

			cnt: int = 0

			MT = MyTime(seconds=2)

			fsizes: int = 0

			# run_jobs_by_workspace_filesize(gb)
			# """
			count_fsize: int = 0
			default_dspace: int = 8  # use_by_default_dspace

			for k, v in filecmdbase_dict.items():
				try:
					count_fsize += os.path.getsize(k)  # calc_filesize
				except:
					continue  # if_not_exist

			if count_fsize:
				if count_fsize // (1024**3) > 0:
					default_dspace: int = count_fsize // (
						1024**3
					)  # dspace_by_filesize_jobs
				else:
					default_dspace: int = 8  # return_default_dspace

				write_log(
					"debug default_space",
					"%s"
					% "%".join(
						[str(default_dspace), str(count_fsize), str(datetime.now())]
					),
				)
			# """
			# default_dspace: int = 8

			# disk_space_limit: int = 0
			disk_space_limit: int = default_dspace * (1024**3)  # 16Gb -> 8Gb

			lastfile: list = []

			jobs: list = []  # filecmdbase_dict

			# @another_list # @last.xml @src=k/len=length(k)/dst=v.split(" ")[-1] # move_dst_to_src

			# xml(job(src=k/len=length(k)/dst=v.split(" ")[-1])) # save_job_to_xml(mp4)

			# @log_error
			async def save_job_to_xml(
				src: str = "", dst: str = ""
			):  # save_last_job # need_multiple_record #5

				try:
					assert os.path.exists(src), ""
				except AssertionError:  # if_null
					return
				except BaseException:  # if_error
					return

				global jobs

				MM = MyMeta()  # 8

				# jobs = [{"src": k, "leng": MM.get_length(k), "dst": v.split(" ")[-1]}] # one_record
				jobs = [
					{"src": src, "leng": MM.get_length(src), "dst": dst}
				]  # one_record

				del MM

				# xml_root_name
				root = xml.Element("jobs")

				try:
					# xml_fields
					for job in jobs:
						child = xml.Element("job")
						root.append(child)
						src = xml.SubElement(child, "src")
						src.text = str(job.get("src"))
						leng = xml.SubElement(child, "leng")
						leng.text = str(job.get("leng"))
						dst = xml.SubElement(child, "dst")
						dst.text = str(job.get("dst"))

					# put_root_and_data_to_tree
					tree = xml.ElementTree(root)
				except BaseException as e:
					print(Style.BRIGHT + Fore.RED + "Xml save error (job)")
					write_log(
						"debug jobs[xml][saveerror]",
						"Xml save error (job) %s [%s]" % (str(e), str(datetime.now())),
						is_error=True,
					)  # main_xml_error
				else:
					try:
						# save_xml
						with open(
							files_base["lastjob"], "wb"
						) as vrf:  # "".join([script_path, '\\last.xml'])
							tree.write(vrf)

					except BaseException as e:
						print(Style.BRIGHT + Fore.RED + "Xml save error (job)")
						write_log(
							"debug jobs[saveerror]",
							"Xml save error (job) %s [%s]"
							% (str(e), str(datetime.now())),
							is_error=True,
						)  # some_error_in_save
					else:
						print(Style.BRIGHT + Fore.GREEN + "Xml saved")
						write_log(
							"debug jobs[xml][save]",
							"save ok [%s]" % str(datetime.now()),
						)  # xml_saved

					# clear_xml(logic)
					"""
					for country in root.findall('country'):
						# using root.findall() to avoid removal during traversal
						rank = int(country.find('rank').text)
						if rank > 50:
							root.remove(country)

					tree.write('output.xml')
					"""

			# @optimial_job_for_jobs_by_xml(load)
			async def load_job_from_xml() -> list:  # load_last_job # dict_in_list #4
				jobs = []

				try:
					tree = xml.parse(
						files_base["lastjob"]
					)  # tree = xml.parse(file=files_base["lastjob"]) # is_error

					root = tree.getroot()

					for elem in root.iter(
						tag="job"
					):  # <jobs><job><src>d:\multimedia\video\serials_conv\Legacies\Legacies_04s11e.mp4</src><leng>2492</leng><dst>c:\downloads\Legacies_04s11e.mp4</dst></job></jobs>
						job = {}

						for subelem in elem:
							job[subelem.tag] = subelem.text

						jobs.append(job)
				except BaseException as e:
					print(Style.BRIGHT + Fore.RED + "Xml load error (job)")
					write_log(
						"debug jobs[xml][loaderror]",
						"Xml load error (job) %s [%s]" % (str(e), str(datetime.now())),
						is_error=True,
					)  # main_xml_error
				else:
					if jobs:  # logging_if_some_data # ... Xml loaded # dict's_to_list
						print(
							Style.BRIGHT + Fore.WHITE + "%s" % str(jobs),
							Style.BRIGHT + Fore.GREEN + "Xml loaded",
						)
						write_log(
							"debug jobs[xml][load]",
							"load ok [%s]" % str(datetime.now()),
						)  # xml_loaded

					return jobs  # [{"src": "d:\\multimedia\\video\\serials_europe\\Nelichnaya_zhizn_Rus\\Nelichnaya_zhizn_01s04e.mp4", "leng": 5000, "dst": "c:\\downloads\\Nelichnaya_zhizn_01s04e.mp4"}]

			# 5000(src_length) ~ (5000//3600) = 1 hh, (5000//60)%60 = int((mm(1.38)-hh)*100) ~ 38 # sample_calc

			MM = MyMeta()  # 9

			fcmd_filter: list = []

			# short_count: dict = {}
			# seasyear_count: dict = {}

			# combine_job_filter # convert_combine_jobs_to_current_jobs # calc_avg_time_by_combine_jobs

			# load_meta_jobs(filter) #10
			try:
				with open(some_base, encoding="utf-8") as sbf:
					somebase_dict = json.load(sbf)
			except:
				somebase_dict = {}

				with open(some_base, "w", encoding="utf-8") as sbf:
					json.dump(
						somebase_dict, sbf, ensure_ascii=False, indent=4
					)  # -save_current_meta(new)

			# filter_stay_only_exists_jobs(is_meta)
			first_len: int = len(somebase_dict)
			somebase_dict = {
				k: v for k, v in somebase_dict.items() if os.path.exists(k)
			}
			second_len: int = len(somebase_dict)

			if (
				somebase_dict
			):  # update_exists_jobs # second_len <= first_len # all -> any
				with open(some_base, "w", encoding="utf-8") as sbf:
					json.dump(
						somebase_dict, sbf, ensure_ascii=False, indent=4
					)  # -save_current_meta(update)

				write_log(
					"debug somebase_dict[update]", "%d" % len(somebase_dict)
				)  # after_load(meta)

			# current_jobs # is_find_job_in_meta_base
			try:
				with open(filecmd_base, encoding="utf-8") as fbf:
					filecmdbase_dict = json.load(fbf)
			except:
				filecmdbase_dict = {}

				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(
						filecmdbase_dict, fbf, ensure_ascii=False, indent=4
					)  # -save_current_jobs(new)

			# '''
			first_len = second_len = 0

			# filter_current_jobs_(in_meta/no_in_meta/exists_only)
			try:
				first_len: int = len(filecmdbase_dict)
				filecmdbase_dict = {
					k: v
					for k, v in filecmdbase_dict.items()
					if os.path.exists(k)
					and any((k.strip() in [*somebase_dict], not [*somebase_dict]))
				}
			except:
				filecmdbase_dict = {
					k: v for k, v in filecmdbase_dict.items() if os.path.exists(k)
				}
			finally:
				second_len: int = len(filecmdbase_dict)

			if (
				filecmdbase_dict and second_len <= first_len
			):  # filter_current_and_not_optimize_jobs # all -> any
				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(
						filecmdbase_dict, fbf, ensure_ascii=False, indent=4
					)  # -save_current_jobs(update)

				write_log(
					"debug filecmdbase_dict[filter]", "%d" % len(filecmdbase_dict)
				)

			write_log(
				"debug filecmdbase_dict[jcount]", "%d" % len(filecmdbase_dict)
			)  # after_load(current)
			# '''

			# combine_jobs # is_find_job_in_meta_base
			# '''
			cbf_dict: dict = {}

			try:
				with open(cfilecmd_base, encoding="utf-8") as cbf:
					cbf_dict = json.load(cbf)
			except:
				cbf_dict = {}

				with open(cfilecmd_base, "w", encoding="utf-8") as cbf:
					json.dump(
						cbf_dict, cbf, ensure_ascii=False, indent=4
					)  # -save_combine_jobs(new)

			first_len = second_len = 0

			# filter_combine_jobs_(in_meta/no_in_meta/exists_only)
			try:
				first_len: int = len(cbf_dict)
				cbf_dict = {
					k: v
					for k, v in cbf_dict.items()
					if os.path.exists(k)
					and any((k.strip() in [*somebase_dict], not [*somebase_dict]))
				}
			except:
				cbf_dict = {k: v for k, v in cbf_dict.items() if os.path.exists(k)}
			finally:
				second_len: int = len(cbf_dict)

			if (
				cbf_dict
			):  # filter_current_and_not_optimize_jobs # second_len <= first_len # all -> any
				with open(cfilecmd_base, "w", encoding="utf-8") as cbf:
					json.dump(
						cbf_dict, cbf, ensure_ascii=False, indent=4
					)  # -save_combine_jobs(update)

				write_log(
					"debug cbf_dict[filter]", "%d" % len(cbf_dict)
				)  # after_load(combine)
			# '''

			# sorted_current_jobs # type1
			MM = MyMeta()

			fcbd: list = []
			fcbd_sorted: list = []

			short_count: dict = {}

			# count_short_files(tvseries/cinema)
			for k, v in filecmdbase_dict.items():

				if not filecmdbase_dict:
					break

				if not os.path.exists(k) or any((not k, not v)):
					continue

				try:
					fname = k.split("\\")[-1].strip()
				except:
					fname = ""

				if os.path.exists(k) and fname:  # exists_job
					try:
						short = crop_filename_regex.sub("", fname).strip()  # regex
					except:
						short = ""
					else:  # is_hide_count
						if short:
							short_count[short.strip()] = (
								short_count.get(short.strip(), 0) + 1
							)  # short_count(generate)

			# logging_short_names(count)
			for k, v in short_count.items():

				if not short_count:
					break

				if any((not k, not v)):
					continue

				logging.info(
					"Шаблон[1]: %s, количесто найденных элементов %d, время: %s"
					% (k, v, str(datetime.now()))
				)

			sfc: dict = {}

			for k, v in filecmdbase_dict.items():

				try:
					assert (
						filecmdbase_dict
					), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning("Пустой словарь или нет задач filecmdbase_dict")
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой словарь или нет задач filecmdbase_dict [%s]" % str(e)
					)
					break

				try:
					assert k and os.path.exists(
						k
					), f"Файл отсутствует {k}"  # is_assert_debug # k
				except AssertionError as err:  # if_null
					logging.warning("Файл отсутствует %s" % k)
					raise err
					continue
				except BaseException as e:  # if_error
					logging.error("Файл отсутствует %s [%s]" % (k, str(e)))
					continue

				try:
					fname = k.split("\\")[-1].strip()
				except:
					fname = ""

				if os.path.exists(k) and fname:  # exists_job
					try:
						gl = MM.get_length(k)  # int
					except:
						gl = 0

					try:
						fs = os.path.getsize(k)  # int
					except:
						fs = 0

					try:
						seas_or_year = crop_filename_regex.findall(fname)[0][
							0
						].strip()  # regex(short) # type1
						# seas_or_year2 = "".join(crop_filename_regex.findall(fname.split(".")[0])[0]) # .replace("_", "").replace("(", "").replace(")", "") # is_crop_syms # str(short) # type2
					except:
						seas_or_year = ""
					# else: # is_hide_count
					# if seas_or_year:
					# seasyear_count[seas_or_year.strip()] = seasyear_count.get(seas_or_year.strip(), 0) + 1 # seas_or_year_count

					# fname = "hello_world_01s01e" -> "01s01e" # fname = "my_name_is(2000)" -> "2000"

					# is_shorts_in_list(upgrade)
					try:
						keywords = fname.split(".")[0].split("_")[
							0 : fname.count("_")
						]  # short_split / (no_seasepis / no_year) # list(short) # type1
						# keywords = fname.split(".")[0].split("_") # short_split / (seasepis / year) # list(full) # type2
						# keywords = fname.split(".")[0].split("_")[-1:] if not "(" in fname else ? # seasepis / ? # type3
					except:
						keywords = []

					# seasepis(year)

					ssy_first, ssy = fname.split(".")[0].split("_")[-1], ""

					try:
						if all(("(" in ssy_first, ")" in ssy_first)):
							ssy = (
								fname.split(".")[0].split("(")[-1].split(")")[0]
							)  # with_year
					except:
						ssy = fname.split(".")[0].split("_")[
							-1
						]  # with_season_and_episode
					finally:
						if not ssy:
							ssy = fname.split(".")[0].split("_")[-1]

					try:
						moddate = os.path.getmtime(k)
					except:
						moddate = 0
					else:
						write_log(
							"debug moddate",
							";".join([k.strip(), unixtime_to_date(moddate)]),
						)  # filename / unixdate(str)
						# date_to_unixtime()

					# keywords -> ".".join(keywords) # list -> str
					# moddate -> str(datetime.fromtimestamp(moddate)) # time(float) -> datetime(str)
					if all((gl, fs, short, seas_or_year, keywords, ssy, moddate)):
						# fcbd.append((k, gl, fs, short, seas_or_year, ".".join(keywords), ssy, str(datetime.fromtimestamp(moddate)))) # filename / length / filesize / short_filename / (seas/year) / keywords_by_list / seasepis(keywords[-1]) ~ type2 / modifydate # old
						fcbd.append(
							(
								k,
								gl,
								fs,
								short,
								seas_or_year,
								".".join(keywords),
								ssy,
								unixtime_to_date(moddate),
							)
						)  # filename / length / filesize / short_filename / (seas/year) / keywords_by_list / seasepis(keywords[-1]) ~ type2 / modifydate # debug
						# sfc[k.strip()] = str((full_to_short(k), gl, fs, short, seas_or_year, ".".join(keywords), ssy, unixtime_to_date(moddate))) # type1 # step_by_step # list_to_dict # keywords[-1] ~ type2
				elif not os.path.exists(k):  # skip_no_exists_job
					continue

			# select_one_length # debug
			# '''
			fcbd_count: dict = {}  # d[str(i)] = d.get(str(i),0)+1
			fcbd_set = set()

			# is_count_data(tuple_to_list)
			try:
				for f in fcbd:  # fields
					for i in range(1, len(f)):  # index
						if not f[i] in fcbd_set:  # type1
							fcbd_count[str(i)] = fcbd_count.get(str(i), 0) + 1
							fcbd_set.add(f[i])
						# elif f[i] in fcbd_set: # type2
						# fcbd_count[str(i)] = fcbd_count.get(str(i), 0) + 1
			except BaseException as e:
				write_log("debug fcbd_count[error]", "%s" % str(e))  # is_error=True
				logging.error("@fcbd_count[error] %s" % str(e))
			else:
				write_log("debug fcbd_count[sort]", "%s" % str(fcbd_count))  # dict

				optimal_sort: list = []

				try:
					counts = max(list(fcbd_count.values()))
				except:
					counts = 0

				try:
					for k, v in fcbd_count.items():
						if fcbd_count[k] == len(fcbd) and (
							all((counts, len(fcbd) == counts)) or not counts
						):  # debug
							optimal_sort.append(k)  # unique_by_length
							write_log(
								"debug optimal_sort",
								"Оптимальная сортировка по индексу поля %s" % str(k),
							)  # int
				except BaseException as e:
					write_log("debug fcbd_count!", "%s" % str(e))  # is_error=True
					logging.error(
						"@fcbd_count! %s" % str(e)
					)  # exit() # debug(hide_try_except)
				else:
					if optimal_sort:
						optimal_sort.sort(reverse=False)

						print(
							"debug optimal_sort[index] %s [%d] [%d]"
							% (str(optimal_sort), len(fcbd), counts)
						)  # list
						write_log(
							"debug optimal_sort[index]",
							"%s [%d] [%d]" % (str(optimal_sort), len(fcbd), counts),
						)
			# '''

			os_sort_dict: dict = {}
			os_sort_dict[1] = "@os_sort sorted_by_length(int)"
			os_sort_dict[2] = "@os_sort sorted_by_filesize(int)"
			os_sort_dict[3] = "@os_sort sorted_by_short_filename(str)"
			os_sort_dict[4] = "@os_sort sorted_by_seas_or_year(str)"
			os_sort_dict[5] = "@os_sort sorted_keywords(list)"
			os_sort_dict[6] = "@os_sort sorted_by_seas/year(last_in_list)"
			os_sort_dict[7] = "@os_sort sorted_by_modifydate(float))"

			# automatic_sort
			try:
				if all((len(optimal_sort) > 0, optimal_sort[-1])):

					os_sort = int(optimal_sort[-1])

					# random_index(some_sort_index) # try_and_hide
					"""
					try:
						oss = sorted([int(o) for o in optimal_sort], reverse=False)
					except:
						oss = 0
					else:
						if sum(oss) > 0:
							if min(oss) < max(oss) and len(optimal_sort) > 1: # not_equal # min_less_max # length>1
								logging.info("@os_sort %s" % (randint(min(oss), max(oss)))) # os_sort = randint(min(oss), max(oss))
							elif min(oss) == max(oss) and len(optimal_sort) == 1: # select_max # length=1
								logging.info("@os_sort %s" % (max(oss))) # os_sort = max(oss)
					"""
				assert os_sort, ""  # is_assert_debug
			except AssertionError:
				os_sort = 7  # is_null # index=7
			except BaseException:
				os_sort = 7  # is_error # index=7

			try:
				fcbd_sorted = sorted(
					fcbd, key=lambda fcbd: fcbd[os_sort]
				)  # any_index # if_normal_select # index(1..7)
			except:
				fcbd_sorted = sorted(
					fcbd, key=lambda fcbd: fcbd[os_sort]
				)  # sort_by_datetime(if_error) # after_some_error(index=7)
			finally:  # else # if_no_error
				try:
					if os_sort in range(1, 8):
						logging.info(os_sort_dict[os_sort])
				except:
					logging.warning("@os_sort unknown")  # if_was_error

			# dict_sort
			"""
			d = {"a": 2, "c": 3, "b": 1}
			print(sorted(d.items(), key=lambda d: ((d[0], d[1])))) # [('a', 2), ('b', 1), ('c', 3)]
			print(sorted(d.items(), key=lambda d: ((d[1], d[0])))) # [('b', 1), ('a', 2), ('c', 3)]
			print(sorted(d.items(), key=lambda d: d[1])) # [('b', 1), ('a', 2), ('c', 3)]
			print(sorted(d, key=lambda d: d[0])) # ['a', 'b', 'c']
			"""

			# manual_sort
			"""
			# reverse (cba) # no_reverse (abc) - default
			# [filename, length, filesize, short_filename, seas_or_year, split_filename + regex, seasepis_or_year, moddate)} # list(params)
			# {filename: [full_to_short(filename), 2872, 136943819, 'Vorona', '_01s', ['Vorona'], '01s04e', 1703765464.1026971]} # dict(params)
			try:
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[1]) # sorted_by_length(int) # (framecount/length)_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[2]) # sorted_by_filesize(int) # filesizes_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[3]) # sorted_by_short_filename(str) # short+(seas/year)_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[4]) # sorted_by_seas_or_year(str) # short_in_str_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[5]) # sorted_keywords(list) # split_filename_in_list_by_abc # off
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[6]) # sorted_by_seas/year(last_in_list) # (seas/year)_by_abc # off
				fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[7]) # sorted_by_modifydate(float)) # modifydate_by_abc
			except:
				fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[0]) # sorted_by_filename
			"""

			for fs in fcbd_sorted:

				if not fcbd_sorted:
					break

				sfc[fs[0].strip()] = str(
					(full_to_short(fs[0]), fs[1:])
				)  # type2 # sorted # tuple_to_dict

				print(
					Style.BRIGHT
					+ Fore.CYAN
					+ "%s" % ";".join([full_to_short(fs[0]), str(fs[1:])])
				)  # str(fs)
				write_log("debug fcbd_sorted", "%s" % str(fs))

			# if all((fcbd_sorted, len(fcbd_sorted) <= list(set([*fcbd])))):
			# pass

			# and (isinstance(fs[1], str) and any((k.strip().startswith(fs[1]), fs[1] in k.strip())) or isinstance(fs[0], int))
			if all((fcbd_sorted, len(fcbd_sorted) <= len(filecmdbase_dict))):
				filecmdbase_dict = {
					k: v
					for fs in fcbd_sorted
					for k, v in filecmdbase_dict.items()
					if os.path.exists(k) and fs[0].strip() == k.strip()
				}  # for_any_sort_types

			if sfc:  # default_parameters_for_current_job
				with open(sfilecmd_base, "w", encoding="utf-8") as sbf:
					json.dump(sfc, sbf, ensure_ascii=False, indent=4, sort_keys=False)

			del MM

			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(
					filecmdbase_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False
				)  # save_current_jobs

			# is_skip_database

			yes_files: list = []
			no_files: list = []

			# clear_every_time # is_true_jobs_count
			"""
			open("".join([script_path, '\\video_resize.db']), "w").close()
			"""

			# @connect_to_database(start)
			conn = sql.connect(
				"".join([script_path, "\\video_resize.db"])
			)  # conn = sql.connect(":memory:")
			"""
			# conn.row_factory = sqlite3.Row # dict # fields_to_dict_keys
			# for res in conn.execute("SELECT * FROM filebase"):
				# print(res["filename"], res["filesize"]) # dict_data
			"""

			# database_backup_to_sql # is_database_backup
			async def database_backup(file="video_resize.sql"):  # 4
				with open("".join([script_path, "\\%s" % file]), "w") as f:
					for line in conn.iterdump():
						f.write("%s\n" % line)

			# database_recovery_from_sql # is_database_recovery
			"""
			async def database_recovery(file="video_resize.sql"): #4
				sql_script: list = []

				with open("".join([script_path, "\\%s" % file, "r") as f:
					sql_script = f.read()

				curr.executescruot(sql_script)
				conn.commit()
			"""

			asyncio.run(database_backup())
			# asyncio.run(database_recovery())

			cur = conn.cursor()

			"""
			# sql.apilevel # '2.0'
			# sql.sqlite_version # '3.31.1'
			# sql.sqlite_version_info # (3, 31, 1)

			# dir(conn) # @ connect_samples
			# dir(cur) # @ cursor_samples

			# fileid INT PRIMARY KEY, # hide_sql_field
			"""

			# @create_table
			# '''
			with conn:
				cur.execute(
					"""CREATE TABLE IF NOT EXISTS filebase(filename TEXT, filesize INTEGER, daterun TEXT);"""
				)
				conn.commit()
			# '''

			# execute(@insert_one)
			"""
			# @sample_one_record
			fileinfo = (k.strip(), os.path.getsize(k), str(datetime.now())) # file / filesize / daterun

			with conn:
				cur.execute("INSERT INTO filebase VALUES (?, ?, ?);", fileinfo)
				conn.commit()
			"""

			# executemany(@insert_multiple)
			"""
			# @sample_multiple_record
			fileinfo = (k.strip(), os.path.getsize(k), str(datetime.now())) # file / filesize / daterun

			multiple_data.append(fileinfo)

			with conn:
				cur.executemany("INSERT INTO filebase VALUES (?, ?, ?);", multiple_data)
					conn.commit()
			"""

			# @create_function_for_sql(mutiple_data) # is_debug
			"""
			def logging_files(lst=multiple_data): #4

				files_lst = []

				try:
					assert lst and isinstance(lst, list), "" # is_assert_debug
				except AssertionError as err:  # if_null
					raise err # logging
					return files_lst
				except BaseException:  # if_error
					return files_lst

				try:
					for d1, d2, d3 in lst:
						if os.path.exists(d1):
							files_lst.append(d1) # append_exists_files
				except:
					files_lst = [] # if_error_null_list

				return files_lst

			with conn:
				conn.create_function("logging_files", -1, logging_files)
				cur = conn.cursor()
				cur.execute("select logging_files()")
				print(cur.fetchall()) # print(cur.fetchone())[0]
			"""

			for k, v in filecmdbase_dict.items():  # somebase_dict # cbf_dict

				try:
					assert (
						filecmdbase_dict
					), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning("Пустой словарь или нет задач filecmdbase_dict")
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой словарь или нет задач filecmdbase_dict [%s]" % str(e)
					)
					break

				try:
					fileinfo = (
						k.strip(),
						os.path.getsize(k),
						str(datetime.now()),
					)  # file / filesize / daterun
				except:
					fileinfo = ()

				if os.path.exists(k) and fileinfo:

					if all(
						(k, any((not k in yes_files, k in [*somebase_dict])))
					):  # exists / yes_in_metabase
						yes_files.append(k)

					try:
						with conn:
							cur.execute(
								"SELECT * FROM filebase WHERE filename = ?;",
								(fileinfo[0],),
							)  # rowid - номер записи # select rowid, * from filebase
					except:
						with conn:
							cur.execute(
								"SELECT * FROM filebase WHERE filename = :filename;",
								{"filename": fileinfo[0]},
							)  # rowid - номер записи # select rowid, * from filebase
					finally:  # else
						write_log(
							"debug filecmdbase_dict[select][yes_files]",
							"%s [%s]" % (fileinfo[0], str(datetime.now())),
						)

						try:
							sql_count = len(cur.fetchall())
						except:
							sql_count = -1
						else:
							if sql_count == 0:
								with conn:
									cur.execute(
										"INSERT INTO filebase VALUES (?, ?, ?);",
										fileinfo,
									)
									conn.commit()

								write_log(
									"debug filecmdbase_dict[insert]",
									"%s [%s]" % (str(fileinfo), str(datetime.now())),
								)
							elif sql_count == 1:
								try:
									with conn:
										cur.execute(
											"UPDATE filebase set filesize = ? where filename = ?;",
											(fileinfo[1], fileinfo[0]),
										)  # ?
										conn.commit()
								except:
									with conn:
										cur.execute(
											"UPDATE filebase set filesize = :filesize where filename = :filename;",
											{
												"fileize": fileinfo[1],
												"filename": fileinfo[0],
											},
										)  # ?
										conn.commit()

								write_log(
									"debug filecmdbase_dict[update]",
									"%s [%s]" % (str(fileinfo), str(datetime.now())),
								)

							write_log(
								"debug filecmdbase_dict[yes_files]",
								"Файл %s присутствует в базе или списке [%d] [%d]"
								% (fileinfo[0], sql_count, len(yes_files)),
							)  # filename / found_in_database / yes_file

				elif not os.path.exists(k) and fileinfo:

					if all(
						(k, any((not k in no_files, not k in [*somebase_dict])))
					):  # no_exists / no_in_metabase
						no_files.append(k)

					try:
						with conn:
							cur.execute(
								"SELECT * FROM filebase WHERE filename = ?;",
								(fileinfo[0],),
							)  # rowid - номер записи # select rowid, * from filebase
					except:
						with conn:
							cur.execute(
								"SELECT * FROM filebase WHERE filename = :filename;",
								{"filename": fileinfo[0]},
							)  # rowid - номер записи # select rowid, * from filebase
					finally:  # else
						write_log(
							"debug filecmdbase_dict[select][no_files]",
							"%s [%s]" % (fileinfo[0], str(datetime.now())),
						)

						try:
							sql_count = len(cur.fetchall())
						except:
							sql_count = -1
						else:
							if sql_count > 0:
								try:
									with conn:
										cur.execute(
											"DELETE FROM filebase WHERE filename = ?;",
											(fileinfo[0],),
										)  # ?
										conn.commit()
								except:
									with conn:
										cur.execute(
											"DELETE FROM filebase WHERE filename = :filename;",
											{"filename": fileinfo[0]},
										)  # ?
										conn.commit()

								write_log(
									"debug filecmdbase_dict[delete]",
									"%s [%s]" % (str(fileinfo), str(datetime.now())),
								)

							write_log(
								"debug filecmdbase_dict[no_files]",
								"Файл %s отсутствует в базе или списке [%d] [%d]"
								% (fileinfo[0], sql_count, len(no_files)),
							)  # filename / not_found_in_database / no_file

			# @delete_table
			if not somebase_dict:
				with conn:
					cur.execute("DROP TABLE IF EXISTS filebase")

			# @disconnect_from_database(end)
			cur.close()  # cursor_stop
			conn.close()  # sqlite_stop # if conn: conn.close()

			if all((filecmdbase_dict, len(somebase_dict) >= 0)):

				try:
					unique_jobs = list(
						set([*filecmdbase_dict]) & set([*somebase_dict])
					)  # use_unique_jobs(current_and_combine_jobs)
				except:
					unique_jobs = list(
						set([*filecmdbase_dict])
					)  # only_current_jobs # if_error
				finally:
					if all(
						(not unique_jobs, [*filecmdbase_dict])
					):  # if_no_jobs(try_only_current_jobs)
						unique_jobs = list(
							set([*filecmdbase_dict])
						)  # only_current_jobs

			MM = MyMeta()

			async def fcmd_generate():  # 2

				global fcmd_filter

				for k, v in filecmdbase_dict.items():

					try:
						assert (
							filecmdbase_dict
						), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
					except AssertionError as err:  # if_null
						logging.warning("Пустой словарь или нет задач filecmdbase_dict")
						raise err
						break
					except BaseException as e:  # if_error
						logging.error(
							"Пустой словарь или нет задач filecmdbase_dict [%s]"
							% str(e)
						)
						break

					try:
						gl = MM.get_length(k)
					except:
						gl = 0
					else:
						if all(
							(gl, k in [*unique_jobs])
						):  # some_length / find_unique_jobs(k in [*unique_jobs])
							fcmd_filter.append((k.strip(), gl))  # "os.path.getsize(k)"

			asyncio.run(fcmd_generate())

			del MM

			fcmd_hours: list = []
			fcmd_minutes: list = []

			if fcmd_filter:
				fcmd_hours = [ff[1] % 3600 for ff in fcmd_filter if ff[1] % 3600 > 0]
				fcmd_minutes = [
					(ff[1] // 60) % 60 for ff in fcmd_filter if (ff[1] // 60) % 60 > 0
				]

				hh_time: int = 0
				hh_avg_time: int = 0
				mm_time: int = 0
				mm_avg_time: int = 0

				# @avg_hour / @max_hour
				try:
					fcmd_hours_sum = sum(fcmd_hours)
					fcmd_hours_len = len(fcmd_hours)
					fcmd_hours_avg = (lambda fhs, fhl: fhs / fhl)(
						fcmd_hours_sum, fcmd_hours_len
					)
				except:
					fcmd_hours_avg = 0
				else:
					# hh_time = max(fcmd_hours) if max(fcmd_hours) > fcmd_hours_avg else fcmd_hours_avg # pass_1_of_2
					# hh_time = int(3600 // hh_time) if max(fcmd_hours) < 3600 else int(hh_time // 3600) # pass_2_of_2

					hh_avg_time = hh_time  # is_debug

					print(
						"Оптимально время для обработки в часах %d часов(а)"
						% hh_avg_time
					)
					write_log(
						"debug fcmd_hours_avg[jobtime]",
						"Оптимально время для обработки в часах %d часов(а)"
						% hh_avg_time,
					)  # hh

				# @avg_minute / @max_minute

				try:
					fcmd_minutes_sum = sum(fcmd_minutes)
					fcmd_minutes_len = len(fcmd_minutes)
					fcmd_minutes_avg = (lambda fms, fml: fms / fml)(
						fcmd_minutes_sum, fcmd_minutes_len
					)
				except:
					fcmd_minutes_avg = 0
				else:
					# mm_time = max(fcmd_minutes) if max(fcmd_minutes) > fcmd_minutes_avg else fcmd_minutes_avg
					mm_time = fcmd_minutes_avg  # avg_without_max
					mm_avg_time = mm_time

					print(
						"Оптимально время для обработки в минутах %d минут(ы)"
						% mm_avg_time
					)
					write_log(
						"debug fcmd_minutes_avg[jobtime]",
						"Оптимально время для обработки в минутах %d минут(ы)"
						% mm_avg_time,
					)  # mm

				# @optimial_time_for_jobs_by_xml(save) # dict's_in_list # debug(xml)

				asyncio.run(
					save_timing_to_xml(hours=hh_time, minutes=mm_time)
				)  # optimize_by_current_jobs(is_run)

			# '''
			try:
				h, m = asyncio.run(
					load_timing_from_xml(ind=9)
				)  # 9 # h, m = load_timing_from_xml(ind=9)
			except:
				h, m = 0, 0
			# '''

			fsizes: int = 0
			fsizes2: int = 0
			fsizes_max: int = 0

			async def fsizes_generate():  # 2
				global fsizes

				for k, v in filecmdbase_dict.items():

					try:
						assert (
							filecmdbase_dict
						), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
					except AssertionError as err:  # if_null
						logging.warning("Пустой словарь или нет задач filecmdbase_dict")
						raise err
						break
					except BaseException as e:  # if_error
						logging.error(
							"Пустой словарь или нет задач filecmdbase_dict [%s]"
							% str(e)
						)
						break

					try:
						assert k and os.path.exists(
							k
						), f"Файл отсутствует {k}"  # is_assert_debug # k
					except AssertionError as err:  # if_null
						logging.warning("Файл отсутствует %s" % k)
						raise err
						continue
					except BaseException as e:  # if_error
						logging.error("Файл отсутствует %s [%s]" % (k, str(e)))
						continue

					if os.path.exists(k):
						try:
							fsize = os.path.getsize(k)
						except:
							fsize = 0

						fsizes += fsize

			asyncio.run(fsizes_generate())

			if fsizes:
				fsizes_max = fsizes

			ms_set = set()

			std_dict: dict = {}

			try:
				with open(std_base, encoding="utf-8") as sbf:
					std_dict = json.load(sbf)
			except:
				with open(std_base, "w", encoding="utf-8") as sbf:
					json.dump(
						std_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
					)

			if std_dict:  # filter_by_exists_files
				std_dict = {k: v for k, v in std_dict.items() if os.path.exists(k)}

			# count_time # pass_1_of_2
			MM = MyMeta()

			hms_list: list = []

			summ: int = 0
			sum_fsizes: int = 0
			fsizes_lst: list = []
			filecmdbase_pos_dict: dict = {}

			write_log("debug run_jobs[1]", "[%s]" % str(datetime.now()))

			for k, v in filecmdbase_dict.items():

				try:
					assert (
						filecmdbase_dict
					), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning("Пустой словарь или нет задач filecmdbase_dict")
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой словарь или нет задач filecmdbase_dict [%s]" % str(e)
					)
					break

				try:
					assert k and os.path.exists(
						k
					), f"Файл отсутствует {k}"  # is_asssert_debug # k
				except AssertionError as err:  # if_null
					logging.warning("Файл отсутствует %s" % k)
					raise err
					continue
				except BaseException as e:  # if_error
					logging.error("Файл отсутствует %s [%s]" % (k, str(e)))
					continue

				try:
					fname = k.split("\\")[-1]
				except:
					fname = ""

				try:
					fsize = os.path.getsize(k)
				except:
					fsize = 0
				else:
					if fsize:
						summ += fsize
						fsizes_lst.append(fsize)

				try:
					gl = MM.get_length(k)
				except:
					gl = 0
				else:
					hh, mm, ss, status = asyncio.run(hh_mm_ss(gl))

					hms_list.append((hh, mm, ss, status, gl, k))

					chunk_size = gl // 10  # length(gl) # parts
					chunks = range(0, gl, chunk_size)  # range_chunks_current_job
					# dl = {str(chunk): str(chunk + chunk_size) for i, chunk in enumerate(chunks)} # for_sequence(- 1)
					dl = {
						str(chunk): str(chunk_size) for i, chunk in enumerate(chunks)
					}  # for_ffmpeg

					seg_dict: dict = {}
					reg_str: str = ""

					# for i, chunk in enumerate(chunks):
					# start=chunk, end=chunk + chunk_size - 1 # use_to_ffmpeg

					# length / onesegment / segment_count / segments(length) # *dl -> dl[0], "...", dl[-1]
					seg_dict[k.strip()] = {
						"length": str(gl),
						"onesegment": str(chunk_size),
						"segmentsize": str(len(chunks)),
						"segments": "x".join([*dl]),
					}
					reg_str = str(seg_dict[k.strip()])

					# segment_info_for_current_job # file/filesize/onesegment/segmentsize/"start"/"end"
					write_log(
						"debug segmentinfo[full]",
						"file [%s]" % "x".join([k, reg_str, str(datetime.now())]),
					)

					if any((gl == (hh * 3600) + (mm * 60) + ss, gl == hh * mm * ss)):
						print(
							Style.BRIGHT
							+ Fore.CYAN
							+ "%s [%s]" % (str(hms_list[-1]), str(datetime.now()))
						)  # show_last_time_and_file_with_framecount # is_color
						write_log(
							"debug hms_list",
							"%s [%s]" % (str(hms_list[-1]), str(datetime.now())),
						)  # last_record

			del MM

			# @classify(for_all_jobs/is_fast) # is_need_hide(dict) # with_json
			# """
			sum_classify: dict = {}
			fsizes_classify: list = []
			# jobs_count: int = 0
			is_classify: bool = False

			if all((filecmdbase_dict, fsizes_lst)):

				try:
					fsum = sum(fsizes_lst)
					flen = len(fsizes_lst)
				except:
					fsum = flen = 0

				try:
					favg = (lambda s, l: s / l)(fsum / flen)
				except:
					favg = 0

				try:
					sum_classify = {
						fl: 1 if fl - favg > 0 else 0 for fl in fsizes_lst
					}  # is_big(is_small) # is_no_lambda
				except:
					sum_classify = {}

				# jobs_count = len(sum_classify)
				fsizes_classify = [*sum_classify]

				if all(
					(fsizes_classify, len(fsizes_classify) <= len(filecmdbase_dict))
				):
					if len(fsizes_classify) != len(filecmdbase_dict):
						is_classify = True
						write_log(
							"debug sum_classify[fsizes_list][different]",
							"Найдено %d классицированных задач из %d файлов [%s]"
							% (
								len(fsizes_classify),
								len(filecmdbase_dict),
								str(datetime.now()),
							),
						)
					elif len(fsizes_classify) == len(filecmdbase_dict):
						is_classify = True
						write_log(
							"debug sum_classify[fsizes_list][equal]",
							"Найдено %d одинаковых классицированных задач с файлами [%s]"
							% (len(fsizes_classify), str(datetime.now())),
						)
				elif not fsizes_classify:
					is_classify = False
					write_log(
						"debug sum_classify[null]",
						"Не получилось класифицировать размеры файлов для текущих задач [%s]"
						% str(datetime.now()),
					)

			if filecmdbase_dict:

				fcb: dict = {}

				if is_classify:
					try:
						fcb = {
							k: v
							for k, v in filecmdbase_dict.items()
							if os.path.exists(k)
							and os.path.getsize(k) in fsizes_classify
						}
					except:
						fcb = {}

				if all(
					(fcb, len(fcb) <= len(filecmdbase_dict))
				):  # update_jobs_by_classify
					filecmdbase_dict = fcb

				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(
						filecmdbase_dict, fbf, ensure_ascii=False, indent=4
					)  # -save_current_jobs
			# """

			filecmdbase_list = [
				*filecmdbase_dict
			]  # skip_sort(defaul) # is_need_classify
			filecmdbase_pos_dict = {
				jfile.strip(): str(i + 1).strip()
				for i, jfile in enumerate(filecmdbase_list)
			}  # start_at_1

			# percent_position
			prc_pos_set = set()
			prc_pos: int = 0

			fsizes_list: list = []

			for k, v in filecmdbase_dict.items():

				try:
					assert filecmdbase_dict, ""  # is_assert_debug
				except AssertionError as err:  # if_null
					raise err
					break
				except BaseException:  # if_error
					break

				try:
					assert k and os.path.exists(
						k
					), f"Файл отсутствует {k}"  # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning("Файл отсутствует %s" % k)
					raise err
					continue
				except BaseException as e:  # if_error
					logging.error("Файл отсутствует %s [%s]" % (k, str(e)))
					continue

				try:
					fsize = os.path.getsize(k)
					assert (
						fsize
					), f"Файл {k} пустой или не содержит информации"  # is_assert_debug # is_another_except
				except AssertionError as err:  # if_null
					logging.warning("Файл %s пустой или не содержит информации" % k)
					raise err
					# continue
				except BaseException as e:  # if_error
					logging.error(
						"Файл %s пустой или не содержит информации [%s]" % (k, str(e))
					)
				else:
					fsizes_list.append(fsize)  # pass_1_of_2

			"""
			Скользящее среднее число - это статистический показатель, который используется для анализа временных рядов, таких как цены акций, температура или продажи.
			Это среднее значение, которое вычисляется путем усреднения предыдущих значений в заданном периоде времени.

			Формула расчета скользящего среднего числа зависит от выбранного вида скользящего среднего, но одним из наиболее распространенных и простых способов расчета
			является простое скользящее среднее (SMA) число.

			Формула расчета SMA выглядит следующим образом:
			SMA = (Значение1 + Значение2 + Значение3 + ... + ЗначениеN) / N

			Где:
			- Значение1, Значение2, Значение3 и так далее представляют предыдущие значения в заданном периоде времени (например, цены акций за последние несколько дней).
			- N представляет собой количество предыдущих значений, используемых для расчета скользящего среднего числа. Например, если выбран период времени в 7 дней,
			N будет равно 7.

			Для примера, рассмотрим расчет простого скользящего среднего числа цен акций за последние 5 дней:
			Цена акций за пять предыдущих дней: 10, 12, 14, 13, 15
			SMA = (10 + 12 + 14 + 13 + 15) / 5
			SMA = 64 / 5
			SMA = 12.8
			"""

			# {'3': 5, '4': 6, '5': 7, '6': 8, '7': 5, '8': 3}
			def future_filesizes(
				fsizes: list = fsizes_list, ws: int = 3
			) -> tuple:  # debug
				lst = fsizes  # [4, 5, 6, 7, 8, 9]
				cnt_max, cnt = len(lst), 0  # no_double_use_original_length
				analiz_dict: dict = {}  # future_dict # if_not_calced_use_null

				while cnt < cnt_max:
					cnt += 1
					# wind_size = ws # window_size # freeze_avg_step # manual
					wind_size = (
						len(lst) if ws != len(lst) else ws
					)  # window_size_by_list_length(debug) # freeze_avg_step # auto
					analiz_dict: dict = {}  # future_dict

					for i in range(len(lst)):
						if (
							i < len(lst)
							and wind_size
							and sum(lst[i : i + wind_size]) / wind_size > 0
						):
							analiz_dict[str(wind_size + i)] = round(
								sum(lst[i : i + wind_size]) / wind_size, 2
							)
						elif wind_size and sum(lst[i : i + wind_size]) / wind_size == 0:
							continue

					s: int = 0
					a: int = 0

					for k, v in analiz_dict.items():
						if v:  # use_not_null_values
							s += v

					try:
						a = s // len(analiz_dict)
					except:
						a = 0
					else:
						if a:  # add_new_value_at_end
							lst.append(a)  # avg_add_list
							analiz_dict[str(len(lst) + 1)] = a  # avg_add_to_json

					s = l = a = 0

					try:
						s = sum(list(analiz_dict.values()))
						l = len(analiz_dict)
						a = s / l
					except:
						a = 0
					else:
						if a > 0:
							# analiz_dict = {k: v for k, v in analiz_dict.items() if v - a > 0} # is_max

							analiz_dict = {
								k: v if v - a > 0 else -v
								for k, v in analiz_dict.items()
							}  # is_max(plus) # is_min(minus)
							# analiz_dict = {k: v for k, v in analiz_dict.items() if v} # is_max # clear_null

				return analiz_dict

			try:
				fut_fil = future_filesizes()  # find_avg_filesize
			except:
				fut_fil = {}
			else:
				if fut_fil:
					write_log(
						"debug fut_fil",
						"jobs_filesize: %s, [%s]" % (str(fut_fil), str(datetime.now())),
					)

					# plt.plot([0, 1, 2, 3, 4], [0, 2, 4, 8, 16])
					# if os.path.exists("".join([path_for_queue, "video_resize.png"])):
					# os.remove("".join([path_for_queue, "video_resize.png"]))

					# is_need_try_except_insert_for_debug
					plt.plot(list(fut_fil.values()), list(fut_fil.keys()))  # all_sizes

					plt.xlabel("filesize_jobs")
					plt.ylabel("wind_size")
					plt.legend(list(fut_fil.keys()))
					plt.savefig(
						"".join([path_for_queue, "video_resize.png"])
					)  # is_some_name

			cnt_max, cnt = len(filecmdbase_dict), 0

			image = os.path.join(path_for_queue, "pil_text.ico")

			# all_or_select_by_classify
			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(
					filecmdbase_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False
				)  # -save_current_jobs(new)

			write_log(
				"debug run_jobs[2]",
				"Найдено %d для обработки [%s]"
				% (len(filecmdbase_dict), str(datetime.now())),
			)

			date1 = datetime.now()

			# new_script
			for k, v in filecmdbase_dict.items():

				try:
					assert (
						filecmdbase_dict
					), "Пустой словарь или нет задач filecmdbase_dict"  # is_assert_debug
				except AssertionError as err:  # if_null
					logging.warning("Пустой словарь или нет задач filecmdbase_dict")
					raise err
					break
				except BaseException as e:  # if_error
					logging.error(
						"Пустой словарь или нет задач filecmdbase_dict [%s]" % str(e)
					)
					break

				try:
					assert k and os.path.exists(
						k
					), f"Файл отсутствует {k}"  # is_assert_debug # k
				except AssertionError as err:  # if_null
					logging.warning("Файл отсутвтует %s" % k)
					raise err
					continue
				except BaseException as e:  # if_error
					logging.error("Файл отсутвтует %s [%s]" % (k, str(e)))
					continue

				lastfile.append(
					v.split(" ")[-1]
				)  # save_to_xml_for_backup(clear_last) # @last.xml

				asyncio.run(
					save_job_to_xml(src=k, dst=v.split(" ")[-1])
				)  # save_job_for_check(in_run/debug)

				ctme = datetime.now()

				if not srd:
					asyncio.run(shutdown_if_time())  # every_check_time_by_job_run

				# if disk_usage("c:\\").free // (1024 ** 2) <= 500:  # if_fspace_less_500mb_then_stop(local)
				# break

				cnt += 1

				try:
					fp, fn = split_filename(k)
				except:
					fn = k.split("\\")[-1].strip()  # fp

				try:
					fname = fn
				except:
					fname = ""
					# continue

				try:
					fsize: int = os.path.getsize(k)
					dsize: int = disk_usage("c:\\").free
				except:
					fsize: int = 0
					dsize: int = 0

				if all((fsize, dsize)):
					fsizes += fsize

					try:
						disk_space_limit = dsize - fsizes
					except:
						disk_space_limit = 0

					# "debug dspace[mp4][stop]": "..."
					if disk_space_limit <= 0:  # if_less_zero
						print(dsize, fsizes, disk_space_limit, k)  # is_color
						write_log(
							"debug dspace[mp4][stop]",
							";".join(
								[
									str(dsize),
									str(fsizes),
									str(disk_space_limit),
									str(datetime.now()),
								]
							),
						)
						break

					# "debug dspace[mp4][limit]": "139/604/512/768;18/980/154/701;8/589/934/592;2023-04-03 11:03:23.116395",
					if all(
						(
							dsize,
							fsizes,
							(disk_space_limit // (1024**3)) < default_dspace,
							(disk_space_limit // (1024**3)) > 0,
						)
					):  # if_less_limit_job(16Gb)
						print(dsize, fsizes, disk_space_limit, k)  # is_color
						write_log(
							"debug dspace[mp4][limit]",
							";".join(
								[
									str(dsize),
									str(fsizes),
									str(disk_space_limit),
									str(datetime.now()),
								]
							),
						)
						break

				# if all((fname in skip_file, fname, skip_file)) or all((jobs_dict_index, jobs_dict_index[fname] > 1)):  # fname_count_filter(list/dict)
				# continue

				main_count = cnt  # count_mp4

				try:
					prc = (cnt / max_cnt) * 100
					if not isinstance(prc, int):
						prc = int(prc)
				except:
					break
				else:
					if all((prc >= 0, not prc in prc_set, cnt <= max_cnt)):
						prc_set.add(prc)

						try:
							# create image
							img = Image.new(
								"RGBA", (50, 50), color=(255, 255, 255, 90)
							)  # color background =  "white"  with transparency
							d = ImageDraw.Draw(img)
							# d.rectangle([(0, 40), (50, 50)], fill=(39, 112, 229), outline=None)  #  color = "blue" # percent # default

							# 0..50 # red(start) # 51..75 # yellow(middle) # 76..100 # green(almost_ready)
							if 0 <= prc <= 50:
								d.rectangle(
									[(0, 40), (50, 50)], fill=(255, 0, 0), outline=None
								)  #  color = "red" # percent
							elif 51 <= prc <= 75:
								d.rectangle(
									[(0, 40), (50, 50)],
									fill=(255, 216, 0),
									outline=None,
								)  #  color = "yellow" # percent
							elif 76 <= prc <= 100:
								d.rectangle(
									[(0, 40), (50, 50)], fill=(76, 255, 0), outline=None
								)  #  color = "green" # percent

							# add text to the image
							font_type = ImageFont.truetype("arial.ttf", 25)
							try:
								prc_last = ((cnt - 1) / max_cnt) * 100
							except:
								prc_last = 0

							if int(prc_last) < prc:  # different_percent
								d.text(
									(0, 0),
									f"{prc_last}\n{prc}",
									fill=(255, 255, 0),
									font=font_type,
								)
							elif int(prc_last) == prc:  # equal_percent
								d.text(
									(0, 0), f"{prc}", fill=(255, 255, 0), font=font_type
								)

							img.save(image)

							# display image in systray
							systray = SysTrayIcon(image, "Systray")
							systray.start()

							# systray.update(icon=image)

							sleep(5)  # ms ~ 5

							# kill image in systray
							systray.shutdown()
						except:
							pass

				# try_find_max_time_from_jobs # save_after_every_job

				dt = datetime.now()
				date2 = dt

				# before_job_start
				if (
					not dt.hour in hours_set
				):  # and (all((len(hours_set) != max_hour, max_hour >= 2)) or not max_hour):  # add_unique_hour
					hours_set.add(dt.hour)  # {1,2,3,4} # set(no_dict)

				speed_file: float = 0
				time_file: float = 0
				data_file: float = 0

				# file_zise = 1024 # размер файла в байтах # transfer_speed = 1000000 # скорость передачи данных в битах в секунду
				# time = calculate_transfer_time(file_size, transfer_speed); print(f"Время передачи файла: {time} секунд")

				def calculate_transfer_time(file_size, transfer_speed):
					transfer_time = (file_size * 8) / transfer_speed
					return transfer_time

				if os.path.exists(k):
					try:
						fsize = os.path.getsize(k)
					except:
						fsize = 0

					fsizes2 += fsize

					# job_info(speed / time / data) # (one/multiple)_jobs
					# """
					speed_list: list = []
					speed_size: str = ""

					# @speed
					# Вычислите скорость передачи, разделив объем данных на время передачи # скорость передачи(Speed)
					"""
					Например, файл размером 25 МБ передается за 2 минуты.
					Сначала преобразуйте 2 минуты в секунды: 2 х 60 = 120 с. Таким образом, S = 25 МБ ÷ 120 с = 0,208.
					Следовательно, скорость передачи равна 0,208 МБ/с.
					Чтобы конвертировать это значение в килобайты, умножьте 0,208 на 1024: 0,208 x 1024 = 212,9.
					Итак, скорость передачи также равна 212,9 КБ/с.
					"""
					# @speed_file": "d:\\multimedia\\video\\serials_conv\\Rookie\\Rookie_05s01e.mp4, скорость передачи: 11.000 Mb/s [12243010]"
					try:
						speed_file = (
							fsize / abs(date1 - date2).seconds
						)  # S = A / T # скорость передачи # default(one_file)
						speed_list = [
							str((speed_file * (1024**i)))
							for i in range(1, 4)
							if (speed_file * (1024**i)) > 0
						]  # Kb/Mb/Gb
					except BaseException as e:
						speed_file = 0
						write_log("debug speed_file[error]", "%s [%s]" % (k, str(e)))
					else:
						if speed_list:
							# speed_size = "%0.3f Mb/s [%d]" % (speed_list[-1], speed_file) # is_1024(is_float) # is_debug(in_list)
							speed_size = "%s Kb/s(Mb/s) [%d]" % (
								",".join(speed_list),
								speed_file,
							)  # is_1024(is_float) # is_debug(in_list)
							write_log(
								"debug speed_file",
								"%s, скорость передачи: %s" % (k, speed_size),
							)  # [2]
						elif not speed_list:
							speed_size = (
								"%0.3f Mb/s" % speed_file
							)  # is_1024(is_float) # is_debug(default) # 11.000 Mb/s
							write_log(
								"debug speed_file[nolist]",
								"%s, скорость передачи: %s" % (k, speed_size),
							)  # [2]

					# 'debug speed_file: d:\\multimedia\\video\\serials_conv\\Hudson_and_Rex\\Hudson_and_Rex_03s01e.mp4, скорость передачи: 32251694.750 30 Mb/s

					# debug_logging_and_logic # logging!
					try:
						time_calc = calculate_transfer_time(fsize, speed_file)
						min_or_hour = (
							"%d часов" % int(time_calc // 60)
							if time_calc > 60
							else "%d минут" % int(time_calc)
						)  # часов / минут
					except BaseException:  # as e:
						write_log(
							"debug min_or_hour[error]",
							"%s [%s]" % (str(k).strip(), str(datetime.now())),
						)
						logging.error(
							"debug min_or_hour[error] %s [%s]"
							% (str(k).strip(), str(datetime.now()))
						)
					else:
						write_log(
							"debug min_or_hour",
							f"Время передачи файла: {min_or_hour}, имя файла: {k}, сейчас: {str(datetime.now())}",
						)
						logging.info(
							f"debug min_or_hour Время передачи файла: {min_or_hour}, имя файла: {k}, сейчас: {str(datetime.now())}"
						)

					time_list: list = []
					time_size: str = ""

					# @time
					# Вычислите время передачи, разделив объем данных на скорости передачи # время_передачи(Time)
					"""
					Например, файл размером 134 ГБ был передан со скоростью 7 МБ/с.
					Сначала преобразуйте ГБ в МБ, чтобы унифицировать единицы измерения: 134 х 1024 = 137217 МБ.
					Итак, 137217 МБ были переданы со скоростью 7 МБ/с.
					Чтобы найти время передачи (T), разделите 137217 на 7 и получите 19602 секунд.
					Чтобы преобразовать секунды в часы, разделите 19602 на 3600 и получите 5,445 ч.
					Другими словами, чтобы передать 134 ГБ данных со скоростью 7 МБ/с, потребовалось 5,445 часа.
					"""

					nfsize: int = 0
					ntime: int = 0

					is_gb = fsize // (1024**3) > 0

					if is_gb:
						nfsize = (fsize // (1024**3)) * 1024  # gb -> mb
						ntime = nfsize / speed_file  # время передачи (T)

					# time_file": "d:\\multimedia\\video\\serials_conv\\Rookie\\Rookie_05s01e.mp4, время передачи: [10.0, 0.0, 10.0] ?[10.0, 0.0] [10]
					try:
						time_file = (
							nfsize / speed_file if nfsize else fsize / speed_file
						)  # T = A / S # время передачи # default(one_file)
						# time_list = [time_file // i for i in range(60, 3660) if all((time_file // i > 0, i % 60 == 0))]

						# is_hh # is_mm # is_ss
						time_list = (
							[
								str(ntime % 3600),
								str((ntime // 60) % 60),
								str(ntime % 60),
							]
							if ntime
							else [
								str(time_file % 3600),
								str((time_file // 60) % 60),
								str(time_file % 60),
							]
						)
					except BaseException as e:
						time_file = 0
						write_log("debug time_file[error]", "%s [%s]" % (k, str(e)))
					else:
						if time_list:
							# time_size = "%0.3f часов, %0.3f минут, %0.3f секунд [%d]" % (time_list[0], time_list[1], time_list[-1], time_file) # str(time_list2) # from_list's
							time_size = "%s чч/мм/cc [%d]" % (
								",".join(time_list),
								time_file,
							)  # from_list's
							write_log(
								"debug time_file",
								"%s, передано %d со скоростью %d время передачи: %s"
								% (k, fsize, speed_file, time_size),
							)  # [4]
						elif not time_list:
							time_size = "%0.3f мин" % time_file  # #%0.3f # from_value
							write_log(
								"debug time_file[nolist]",
								"%s, передано %d со скоростью %d время передачи: %s"
								% (k, fsize, speed_file, time_size),
							)  # [4]

					# 'debug time_file: d:\\multimedia\\video\\serials_conv\\Firefly_Lane\\Firefly_Lane_02s01e.mp4, время передачи: 66.000 1 сек

					data_list: list = []
					data_size: str = ""

					# @data
					# Вычислите объем данных, умножив время передачи на скорость передачи # объём данных(Data)
					"""
					Например, нужно определить, сколько данных было передано за 1,5 часа со скоростью 200 бит/с.
					Сначала преобразуйте часы в секунды: 1,5 х 3600 = 5400 с. Итак, А = 5400 с х 200 бит/с = 1080000 бит/с.
					Чтобы преобразовать это значение в байты, разделите на 8: 1080000 ÷ 8 = 135000.
					Чтобы конвертировать значение в килобайты, разделите на 1024: 135000 ÷ 1024 = 131,84.
					Таким образом, 131,84 КБ данных было передано за 1,5 часа со скоростью 200 бит/с.
					"""
					# data_file": "d:\\multimedia\\video\\serials_conv\\Rookie\\Rookie_05s01e.mp4, сколько данных было передано: 122430109.000 116.000 Mb [122430109]
					try:
						data_file = (
							(time_file * 3600) * speed_file
							if int(time_list[0]) > 0
							else time_file * speed_file
						)  # A = T * S # сколько данных было передано # for_all
						data_file //= 8  # is_bytes
						data_file //= 1024  # is_kbytes
						data_list = [
							(data_file // (1024**i))
							for i in range(1, 4)
							if (data_file // (1024**i)) > 0
						]  # Kb/Mb/Gb
					except BaseException as e:
						data_file = 0
						write_log("debug data_file[error]", "%s [%s]" % (k, str(e)))
					else:
						if data_list:
							# data_size = "%0.3f Mb <=> %0.3f Mb [%d]" % (data_list[0], data_list[-1], data_file) # is_1024(is_float) # is_debug(in_list)
							data_size = "%s Kb(Mb) [%d]" % (str(data_list), data_file)
							write_log(
								"debug data_file",
								"%s, сколько данных было передано: %0.3f %s за %d со скоростью %d"
								% (
									k,
									round(data_file, 3),
									data_size,
									time_file,
									speed_file,
								),
							)  # [5]
						elif not data_list:
							data_size = (
								"%0.3f Mb" % data_file
							)  # is_1024(is_float) # is_debug(default)
							write_log(
								"debug data_file[nolist]",
								"%s, сколько данных было передано: %0.3f %s за %d со скоростью %d"
								% (
									k,
									round(data_file, 3),
									data_size,
									time_file,
									speed_file,
								),
							)  # [5]

					std_dict[k.strip()] = str(
						{
							"speed": [str(round(speed_file, 3)), speed_size],
							"time": [str(round(time_file, 3)), time_size],
							"data": [str(round(data_file, 3)), data_size],
						}
					)  # speed/time/data

					# 'debug data_file: d:\\multimedia\\video\\serials_conv\\Hudson_and_Rex\\Hudson_and_Rex_03s02e.mp4, сколько данных было передано: 129830249.000 123 Mb
					# """

				if std_dict:
					with open(std_base, "w", encoding="utf-8") as sbf:
						json.dump(
							std_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True
						)

				# if all((len(hours_set) == max_hour, max_hour >= 2)):  # 2_hours_or_more_to_stop(default) # wait_after_2_hours
				# break

				print(
					Style.BRIGHT + Fore.CYAN + "\nФайл %s" % k,
					Style.BRIGHT + Fore.WHITE + "начал обрабатываться",
				)
				write_log(
					"debug run[job][start]",
					"Файл %s начал обрабатываться [%s]" % (k, str(datetime.now())),
				)

				# filecmd_base # if_big_cinema_4_hours # if_tv_series_3_hours # debug(trends)
				# set_or_update(trends)_by_any_video # change_after_finish_job
				try:
					with open(trends_base, encoding="utf-8") as ftf:
						trends_dict = json.load(ftf)
				except:
					trends_dict = {}

					with open(trends_base, "w", encoding="utf-8") as ftf:
						json.dump(
							trends_dict,
							ftf,
							ensure_ascii=False,
							indent=4,
							sort_keys=False,
						)  # save_by_modified

				first_len = len(trends_dict)

				# today_check = str(datetime.today()).split(" ")[0] # year/month/day # default
				# today_check = "-".join(str(datetime.today()).split(" ")[0].split("-")[0:1]) # current_year
				# today_check = "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2]) # current(year/month)
				# today_check = "-".join(str(datetime.today()).split(" ")[0].split("-")[0:3]) # current(year/month/day)
				# dt_check = " ".join(["-".join(str(datetime.today()).split(" ")[0].split("-")[0:3]), ":".join(str(datetime.today()).split(" ")[-1].split(":")[0:3])]) # default

				try:
					assert (
						unixtime_to_date(os.path.getmtime(k))
						in trends_dict[
							crop_filename_regex.sub("", k.split("\\")[-1]).strip()
						]
					), ""
				except AssertionError:  # if_null(not_found)
					trends_dict[
						crop_filename_regex.sub("", k.split("\\")[-1]).strip()
					] = unixtime_to_date(os.path.getmtime(k))
					write_log(
						"debug trend_time[new]",
						"%s" % crop_filename_regex.sub("", fname).strip(),
					)
				except BaseException:  # if_error
					trends_dict[
						crop_filename_regex.sub("", k.split("\\")[-1]).strip()
					] = unixtime_to_date(os.path.getmtime(k))
					write_log(
						"debug trend_time[error]",
						"%s" % crop_filename_regex.sub("", fname).strip(),
					)
				else:  # redate
					trends_dict[
						crop_filename_regex.sub("", k.split("\\")[-1]).strip()
					] = unixtime_to_date(os.path.getmtime(k))
					write_log(
						"debug trend_time[update]",
						"%s" % crop_filename_regex.sub("", fname).strip(),
					)

				maxdate_filter = max(
					list(trends_dict.values())
				)  # maxdate_in_trends(+count)
				trends_filter = {
					k: v
					for k, v in trends_dict.items()
					if all((maxdate_filter, v, maxdate_filter in v))
				}  # trends_filter_by_maxdate
				if len(trends_filter) > 0:
					write_log(
						"debug maxdate_filter",
						"%s"
						% ";".join(
							[
								str(maxdate_filter),
								str(list(trends_dict.values()).count(maxdate_filter)),
								";".join([*trends_filter]),
							]
						),
					)

				trends_dict = {
					k: v
					for k, v in trends_dict.items()
					for s in sorted(
						trends_dict, key=lambda trends: ((trends[1], trends[0]))
					)
					if k == s
				}
				trends_dict = {
					k: v
					for k, v in trends_dict.items()
					if "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2])
					in v.strip()
				}  # stay_only_this_month(other_clear)

				second_len = len(trends_dict)

				if all((trends_dict, second_len)):  # second_len <= first_len
					# save_by_(sort_base/filter_by_date)
					with open(trends_base, "w", encoding="utf-8") as ftf:
						json.dump(trends_dict, ftf, ensure_ascii=False, indent=4)

					with open(files_base["trends"], "w", encoding="utf-8") as fbtf:
						fbtf.writelines("%s\n" % t for t in [*trends_dict])

					write_log(
						"debug trends_dict[save3]",
						"%s"
						% ";".join([";".join([*trends_dict]), str(datetime.now())]),
					)

				# p: int = -999

				date2 = datetime.now()

				hour = divmod(
					int(abs(date1 - date2).total_seconds()), 60
				)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(
						date1, date2
					)  # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				try:
					if len(hour) > 0:
						hour = hour[0] // 60
					assert bool(hour < 4), ""
				except BaseException:
					hour = 4
				except AssertionError:
					hour = 4

				write_log(
					"debug hour[count][8]", "%d [filecmdbase_dict]" % hh
				)  # is_index #8

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if (
					all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
				):  # stop_if_more_hour
					write_log(
						"debug stop_job[filecmdbase_dict]",
						"Stop: at %s [%d]" % (k, cnt),
					)

					break  # stop_if_before_run

				if all((k, k in [*filecmdbase_pos_dict])):
					prc_pos = int((cnt / len(filecmdbase_pos_dict)) * 100)

					if all((not int(prc_pos) in prc_pos_set, prc_pos <= 100)):
						prc_pos_set.add(int(prc_pos))

					print(
						Style.BRIGHT + Fore.BLUE + "Run:",
						Style.BRIGHT + Fore.WHITE + "%s" % v,
						Style.BRIGHT + Fore.YELLOW + "[%d]" % prc_pos,
						end="\n",
					)  # show_all_percent_process # filecmdbase_pos_dict[k] -> prc_pos
					write_log("debug run[mp4][pos]", "%s" % v)

				# @m3u8 # generate_m3u8_by_job(stay_m3u8) # ts_segments

				try:
					is_run, is_cmd, is_comment = asyncio.run(
						mp4_to_m3u8(filename=k, is_run=False, is_stay=True)
					)
				except:
					is_run, is_cmd, is_comment = False, "", ""

				if any((is_run, is_cmd, is_comment)):
					generate_m3u8_by_job = (is_run, is_cmd, is_comment)
					write_log(
						"debug mp4_to_m3u8",
						"%s [%s] [%s]"
						% (str(generate_m3u8_by_job), k, str(datetime.now())),
					)

				# @mp4 # default_auto_run
				"""
				try:
					p = os.system(v) # continue # continue_if_debug / run # mp4
					assert bool(p == 0), ""
				except AssertionError:
					if p != 0:  # skip_if_run_bad
						print(Style.BRIGHT + Fore.RED + "Ошибка обработки файла %s будет пропушен" % k)

						write_log("debug run[job][error]",
								  "Ошибка обработки файла %s будет пропушен [%s]" % (k, str(datetime.now())))
						continue
				else:
					# find_max_job_time
					if p == 0:  # calc_time_if_run_ok
						# clear(null)_xml_if_ready_ok # is_need_or_not

						print(Style.BRIGHT + Fore.GREEN + "Файл %s" % k,
							  Style.BRIGHT + Fore.WHITE + "успешно обработался")  # k -> dfile

						if all((k, not k in ready_set)):
							ready_set.add(k)

							write_log("debug run[job][complete]",
								  "Файл %s успешно обработался [%s]" % (k, str(datetime.now())))  # k -> dfile


				"""
				continue  # skip_run # hide_if_auto_run

				# compare_filesizes
				try:
					glf = os.path.getsize(lastfile[-1])
				except:
					glf = 0
				else:
					glf //= 1024**2

				try:
					fname1 = lastfile[-1].split("\\")[-1]
				except:
					fname1 = ""

				try:
					fname2 = k.split("\\")[-1]
				except:
					fname2 = ""

				# compare_lengths(src=dst) # clear(null)_xml_if_ready_ok # @last.xml

				date2 = datetime.now()

				hour = divmod(
					int(abs(date1 - date2).total_seconds()), 60
				)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(
						date1, date2
					)  # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				try:
					if len(hour) > 0:
						hour = hour[0] // 60
					assert bool(hour < 4), ""
				except BaseException:
					hour = 4
				except AssertionError:
					hour = 4

				write_log(
					"debug hour[count][9]", "%d [filecmdbase_dict]" % hh
				)  # is_index #9

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if (
					all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]
				):  # stop_if_more_hour
					write_log(
						"debug stop_job[filecmdbase_dict]",
						"Stop: at %s [%d]" % (k, cnt),
					)

					try:
						fdate, status = asyncio.run(datetime_from_file(lastfile[-1]))
					except:
						fdate, status = datetime.now(), False
					else:
						if any(
							(
								fdate.hour < mytime["sleeptime"][1],
								all((hh >= h, mm >= m)),
							)
						):
							if os.path.exists(lastfile[-1]):
								os.remove(lastfile[-1])
								lastfile.remove(lastfile[-1])

					break  # stop_after_run

			del MT

			try:
				prc_total = "".join(
					[str(round(cnt / len(filecmdbase_dict), 3) * 100), "%"]
				)
			except:
				prc_total = ""
			finally:
				if prc_total:
					write_log(
						"debug run_jobs[end]",
						"Обработано %s для обработки [%s]"
						% (prc_total, str(datetime.now())),
					)

			async def clear_m3u8():  # clear_old_m3u8_playlists #2
				# current_files(dict)
				try:
					with open(vr_files, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except:
					ff_last = {}

					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(
							ff_last, vff, ensure_ascii=False, indent=4, sort_keys=True
						)

				try:
					segments_list = os.listdir(path_for_segments)
				except:
					segments_list = []

				# combine_jobs_filter_by_segments(m3u8)_filenames
				try:
					ff_last_no_file = {
						os.path.join(path_for_segments, sl).strip(): v
						for k, v in ff_last.items()
						for sl in segments_list
						if all(
							(
								k,
								sl,
								k.split("\\")[-1].split(".")[0]
								== "".join([path_for_segments, sl])
								.split("\\")[-1]
								.split(".")[0],
							)
						)
						and not os.path.exists(k)
					}
				except:
					ff_last_no_file = {}

				if ff_last_no_file:  # what_not_exists
					for k, _ in ff_last_no_file.items():

						if not os.path.exists(k):  # is_assert_debug
							print(
								Style.BRIGHT
								+ Fore.CYAN
								+ "Файл %s не найден и его надо удалить из базы" % k
							)
							write_log(
								"debug ff_last[nofile]",
								"Файл %s не найден и его надо удалить из базы" % k,
							)
							# os.remove(k) # need_delete_m3u8_by_filename

					sleep(0.50)

			async def update_combine_jobs():  # delete_not_exists_job #2
				try:
					with open(vr_files, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except:
					ff_last = {}

					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(
							ff_last, vff, ensure_ascii=False, indent=4, sort_keys=True
						)

				first_len: int = 0
				first_len = len(ff_last)  # without_update_length # pass_1_of_2

				if ff_last:
					ff_last = {k: v for k, v in ff_last.items() if os.path.exists(k)}

				second_len: int = 0
				second_len = len(ff_last)  # is_update(equal)_length # pass_2_of_2

				if all((ff_last, second_len <= first_len)):  # update_exists_files
					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(
							ff_last, vff, ensure_ascii=False, indent=4, sort_keys=True
						)

					write_log("debug ff_last[update]", "%d" % len(ff_last))

			asyncio.run(clear_m3u8())
			asyncio.run(update_combine_jobs())

			# check_jobs_for_forward_update(project(src) -> original(dst)) # debug(xml)

			MM = MyMeta()  # 10

			ok_count: int = 0
			diff_count: int = 0
			err_count: int = 0

			ok_bad_dict: dict = {}

			for k, v in filecmdbase_dict.items():  # fcd.json -> cfcd.json
				asyncio.run(
					save_job_to_xml(src=k, dst=v.split(" ")[-1])
				)  # save_job_for_check(after_run/debug)

				is_ok: bool = False
				is_bad: bool = False

				try:
					check_job = asyncio.run(
						load_job_from_xml()
					)  # check_job_for_check(after_run)
				except:
					check_job = []
				else:
					try:
						for cj in check_job:

							try:
								assert (
									check_job
								), f"Пустой список или нет задач {cj}"  # check_job # is_assert_debug
							except AssertionError as err:  # if_null
								logging.warning(
									f"Пустой список или нет задач {cj}"
								)  # check_job
								raise err
								break
							except BaseException as e:  # if_error
								logging.error(
									"Пустой список или нет задач check_job [%s]"
									% str(e)
								)
								break

							try:
								assert cj and os.path.exists(
									cj
								), ""  # is_assert_debug # cj
							except AssertionError as err:  # if_null # BaseException
								raise err
								# continue

							# src_length
							try:
								gl1 = int(cj["leng"])
							except:
								gl1 = 0

							# dst_length
							try:
								gl2 = MM.get_length(cj["dst"])
							except:
								gl2 = 0

							try:
								is_clean = all(
									(gl2 in range(gl1, gl1 - 10, -1), gl2, gl1)
								)
							except:
								is_clean = False

							if is_clean:
								ok_bad_dict[0] = ok_bad_dict.get(0, 0) + 1  # ok_length
								ok_count += 1
							elif not is_clean:
								ok_bad_dict[1] = ok_bad_dict.get(1, 0) + 1  # ok_length
								diff_count += 1

							if all(
								(
									is_clean == True,
									cj["src"].split("\\")[-1]
									== cj["dst"].split("\\")[-1],
								)
							):  # try_save # int(cj["leng"]) == MM.get_length(cj["dst"])
								print(
									Style.BRIGHT
									+ Fore.CYAN
									+ "Задача %s выполнена успешно, её можно сохранить"
									% full_to_short(cj["dst"])
								)  # is_color
								write_log(
									"debug check_job[equal]",
									"Задача %s выполнена успешно, её можно сохранить"
									% cj["dst"],
								)

								# is_ok, is_bad = True, False

								# ok_bad_dict[0] = ok_bad_dict.get(0, 0) + 1 # ok_length

								if os.path.exists(cj["src"]) and os.path.exists(
									cj["dst"]
								):
									try:
										fsize: int = os.path.getsize(cj["dst"])
										dsize: int = disk_usage(
											cj["src"][0] + ":\\"
										).free
									except:
										fsize: int = 0
										dsize: int = 0
									else:
										try:
											move(cj["dst"], cj["src"])
										except:
											if os.path.exists(
												cj["dst"]
											):  # status_error_from_xml # is_logging(is_red)
												os.remove(
													cj["dst"]
												)  # delete_if_cant_move
												print(
													Style.BRIGHT
													+ Fore.RED
													+ "Файл %s удален, т.к. не получилось перенести готовый файл"
													% full_to_short(cj["dst"])
												)
												write_log(
													"debug dst[save][error]",
													"Файл %s удален, т.к. не получилось перенести готовый файл"
													% cj["dst"],
												)
												logging.error(
													"debug dst[save][error] Файл %s удален, т.к. не получилось перенести готовый файл"
													% cj["dst"]
												)
										else:
											print(
												Style.BRIGHT
												+ Fore.GREEN
												+ "%s"
												% ">=->".join([cj["dst"], cj["src"]])
											)
											write_log(
												"debug dst[save][xml]",
												"%s"
												% ">=->".join([cj["dst"], cj["src"]]),
											)  # status_save_ok_from_xml # is_logging(is_green)

							elif all(
								(
									is_clean == False,
									cj["src"].split("\\")[-1]
									== cj["dst"].split("\\")[-1],
								)
							):  # skip_to_update(check_length) # int(cj["leng"]) != MM.get_length(cj["dst"])

								# diff_save_status(short/full) # debug # dst <= src # src <= dst
								diff_save_short = (
									"Задача %s выполнена с разницей, её нельзя сохранять"
									% full_to_short(cj["dst"])
									if os.path.exists(cj["src"])
									else "Задача %s, файл отсутствует"
									% full_to_short(cj["src"])
								)
								diff_save_full = (
									"Задача %s выполнена с разницей, её нельзя сохранять"
									% cj["dst"]
									if os.path.exists(cj["src"])
									else "Задача %s, файл отсутствует" % cj["src"]
								)

								print(
									Style.BRIGHT + Fore.YELLOW + "%s" % diff_save_short
								)
								write_log(
									"debug check_job[diff]", "%s" % diff_save_full
								)

								# is_ok, is_bad = False, True

								# ok_bad_dict[1] = ok_bad_dict.get(1, 0) + 1 # diff_length

								if os.path.exists(cj["dst"]):
									try:
										os.remove(cj["dst"])
									except:
										print(
											Style.BRIGHT
											+ Fore.RED
											+ "Файл %s не удален"
											% full_to_short(cj["dst"])
										)
										write_log(
											"debug dst[delete][error]",
											"Файл %s не удален" % cj["dst"],
										)  # status_error_from_xml # is_logging(is_red)
										logging.error(
											"debug dst[delete][error] Файл %s не удален"
											% cj["dst"]
										)
									else:
										print(
											Style.BRIGHT
											+ Fore.GREEN
											+ "Файл %s успешно с разным временем удален"
											% full_to_short(cj["dst"])
										)
										write_log(
											"debug dst[delete][xml]",
											"Файл %s успешно с разным временем удален"
											% cj["dst"],
										)  # status_delete_from_xml # is_logging(is_green)
					except BaseException as e:
						write_log(
							"debug check_job[error]", "%s" % str(e), is_error=True
						)
						logging.error("debug check_job[error] %s" % str(e))

						err_count += 1
						ok_bad_dict[2] = ok_bad_dict.get(2, 0) + 1  # error

						continue  # if_none_next_record(eof)
					else:

						if (
							len(ok_bad_dict) >= 0
						):  # filename, (0 - ok/1 - diff/2 - error), datetime
							write_log(
								"debug check_job[some]",
								"%s"
								% ";".join(
									[
										k,
										str(ok_bad_dict),
										str(ok_count),
										str(diff_count),
										str(err_count),
										str(datetime.now()),
									]
								),
							)

						"""
						answer_status: str = ""

						try:
							if ok_bad_dict[2] > 0:
								answer_status = "Данные совпадают [%d]" % len(ok_bad_dict) if ok_bad_dict[0] == len(ok_bad_dict) else "Данные не совпадают [%d]" % ok_bad_dict[2] # is_no_lambda
							elif ok_bad_dict[2] == 0:
								answer_status = "Данные совпадают [%d]" % len(ok_bad_dict) if ok_bad_dict[0] == len(ok_bad_dict) else "Данные не совпадают" # is_no_lambda
							assert answer_status, "" # is_assert_debug
						except AssertionError as err:  # if_null
							raise err # logging
							write_log("debug check_job[null]", "Данные не совпадают") # logging.warning
						except BaseException as e:  # if_error
							write_log("debug check_job[null]", "Данные не совпадают [%s]" % str(e)) # logging.error
						else:
							if answer_status:
								write_log("debug check_job[ok]", "%s" % answer_status)
						"""

			del MM

			sum_count: int = 0

			try:
				sum_count = ok_count + diff_count + err_count
			except:
				sum_count = 0

			if all((sum_count, sum_count < len(filecmdbase_dict))):
				print(
					Style.BRIGHT + Fore.YELLOW + "Возможно есть пропущенные задачи!!!"
				)
				write_log(
					"debug check_job[skiped]", "Возможно есть пропущенные задачи!!!"
				)
			elif all((sum_count, sum_count == len(filecmdbase_dict))):
				print(
					Style.BRIGHT
					+ Fore.GREEN
					+ "Все задачи обработаны, даже если есть ошибки"
				)
				write_log(
					"debug check_job[combine]",
					"Все задачи обработаны, даже если есть ошибки",
				)
			elif not sum_count:
				print(
					Style.BRIGHT
					+ Fore.WHITE
					+ "Возможно нет никаких задач или ошибка счётчика"
				)
				write_log(
					"debug check_job[nojobs]",
					"Возможно нет никаких задач или ошибка счётчика",
				)

			# xml(job(src=k/len=length(k)/dst=v.split(" ")[-1])) # load_job_from_xml(mp4)

			if max_hour < len(hours_set):
				max_hour = len(hours_set)  # update_hours

			with open(files_base["hours"], "w", encoding="utf-8") as fbhf:
				fbhf.write("%d\n" % max_hour)

			# print()

			# open(files_base["backup"], "w", encoding="utf-8").close()  # clean_backup_if_some_jobs_done(is_need_hidden)

			# ip_and_macs_after_every_run_complete

			dt1 = datetime.now()

			if any(
				(dt1.hour > mytime["sleeptime"][1], dt1.hour <= 21)
			):  # is_time_ranges(?am-9pm)
				print(
					"Сбор дполнительной информации об текущих устройствах... Ждите..."
				)

				asyncio.run(ip_config())  # asyncio.run(ipconfig_to_base())

				if isinstance(lanmacs, dict):
					with open(
						"".join([script_path, "\\lanmacs.json"]), "w", encoding="utf-8"
					) as ljf:
						json.dump(
							lanmacs, ljf, ensure_ascii=False, indent=4, sort_keys=True
						)

				dt2 = datetime.now()  # is_debug(time)

				try:
					hh = abs(dt2 - dt1).seconds // 3600
				except:
					hh = 0

				try:
					mm = (abs(dt2 - dt1).seconds // 60) % 60
				except:
					mm = 0

				try:
					ss = abs(dt2 - dt1).seconds % 60
				except:
					ss = 0

				full_time = None

				try:
					assert any(
						(hh, mm, ss)
					), f"Ошибка значения единицы времени {hh}/{mm}/{ss}"  # is_assert_debug
				except AssertionError as err:  # if_null
					full_time = None
					logging.warning(
						"Ошибка значения единицы времени %d/%d/%d" % (hh, mm, ss)
					)
					raise err
				except BaseException as e:  # if_error
					full_time = None
					logging.error(
						"Ошибка значения единицы времени %d/%d/%d [%s]"
						% (hh, mm, ss, str(e))
					)
				else:
					full_time = "%s:%s:%s" % (hh, mm, ss)

				if full_time != None:
					print(
						f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}] [{full_time}]"
					)  # is_color
					write_log(
						"debug get_hardware[lan][time]",
						f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}] [{full_time}]",
					)
				elif full_time == None:
					print(
						f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}]"
					)  # is_color
					write_log(
						"debug get_hardware[lan]",
						f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}]",
					)

	# current_mac_and_ip # online / offline

	try:
		ip_address, _ = asyncio.run(current_ip())  # ip_template
	except:
		ip_address = ""

	ip: str = ""

	if ip_address.count(".") == 3:
		ip = ".".join(ip_address.split(".")[:-1])  # 192.168.1

	# {"mac": "ip"}
	# "00:00:00:00:00:00": "127.0.0.254"
	# "00:06:dc:46:b7:dc": "VENUS;192.168.1.120"
	try:
		with open("".join([script_path, "\\lanmacs.json"]), encoding="utf-8") as ljf:
			lanmacs = json.load(ljf)
	except:
		with open(
			"".join([script_path, "\\lanmacs.json"]), "w", encoding="utf-8"
		) as ljf:
			json.dump(lanmacs, ljf, ensure_ascii=False, indent=4, sort_keys=True)

	end_ip = re.compile(
		r".*#([\d+]{1,3})$", re.I
	)  # s = "acl ip120 arp 00:06:dc:46:b7:dc #120"; print(end_ip.findall(s)[-1])

	# s = "acl ip120 arp 00:06:dc:46:b7:dc #120"; new_ip = ".".join([ip, end_ip.findall(s)[-1]])

	# {"mac": ["squid_rule", "squid_access", "datetime"]}
	# "00:06:dc:46:b7:dc": ["acl ip120 arp 00:06:dc:46:b7:dc #120", "http_access access ip120", "2024-01-07 16:26:12.155609"]
	try:
		with open("".join([script_path, "\\squid.json.acl"]), encoding="utf-8") as sajf:
			acl = json.load(sajf)
	except:
		with open(
			"".join([script_path, "\\squid.json.acl"]), "w", encoding="utf-8"
		) as sajf:
			json.dump(acl, sajf, ensure_ascii=False, indent=4, sort_keys=True)

	lanmacs_copy = lanmacs

	work_set = set()
	skip_set = set()

	try:
		for k, v in lanmacs.items():
			for k2, v2 in acl.items():
				if all((k == k2, ip)) and not k in work_set:
					work_set.add(k)
					s = str(v2[0])  # squid_rule_for_parse
					new_ip = ".".join([ip, end_ip.findall(s)[-1]])  # new_ip_by_lan
					v_new = (
						";".join([v.split(";")[0], new_ip])
						if len(v.split(";")) > 1
						else new_ip
					)  # host(+ip) / ip

					try:
						assert bool(lanmacs_copy[k.strip()] == v_new), ""
					except AssertionError:  # if_unknown_ip
						lanmacs_copy[k.strip()] = v_new
						logging.warning(
							"@lanmacs_copy[null] %s" % str({str(k), str(v_new)})
						)
					except BaseException:  # if_unknown_key
						lanmacs_copy[k.strip()] = v_new
						logging.error(
							"@lanmacs_copy[error] %s" % str({str(k), str(v_new)})
						)
					else:  # if_known_ip_reupdate
						lanmacs_copy[k.strip()] = v_new
						write_log(
							"debug lanmacs_copy[ok]", "%s" % str({str(k), str(v_new)})
						)

					# print(":".join([str(k), v_new]), sep="\t", end="\n") # debug
					write_log("debug ipinfo", "%s" % str({str(k), str(v_new)}))
	except BaseException as e:
		logging.error("%s" % str(e))
		write_log("debug lanmacs/acl/error", "%s" % str(e))
	else:
		for k, v in lanmacs.items():
			if all((not k in work_set, not k in skip_set)):
				skip_set.add(k)

		# lanmacs_copy = {k:v for k, v in lanmacs_copy.items() if k in [*work_set]} # only_known_ip
		lanmacs_copy = {
			k: v if k in [*work_set] else ipv4_to_ipv6(ip=v)
			for k, v in lanmacs_copy.items()
		}  # known_ip / unknown_ip

		# @only_known_ip
		work_count: int = 0  # online_count
		skip_count: int = 0  # offline_count

		for k, v in lanmacs_copy.items():
			if v.lower().strip() != "offline":
				work_count += 1
			elif v.lower().strip() == "offline":
				skip_count += 1

		if any((work_count, skip_count)):  # ip_count
			write_log(
				"debug status/online/offline",
				"online: %d, offline: %d" % (work_count, skip_count),
			)

		if any((work_set, skip_set)):  # set's
			write_log(
				"debug sets/work_set/skip_set",
				"find: %d, skip: %d" % (len(work_set), len(skip_set)),
			)

		if lanmacs_copy:
			lanmacs.update(lanmacs_copy)
			write_log(
				"debug lanmacs_copy", "%s" % str(lanmacs_copy)
			)  # debug_before_save

			with open(
				"".join([script_path, "\\lanmacs.json"]), "w", encoding="utf-8"
			) as ljf:
				json.dump(lanmacs, ljf, ensure_ascii=False, indent=4, sort_keys=True)

	if not jcount:  # no_jobs_but_maybe_combine_jobs_from_base

		# clear_when_null_jobs(is_update)

		print("No data for video template or resolution")
		write_log("debug nofiles", "No data for video template or resolution")

		# print()

		# @hide_clean_backup_by_job_time
		# dt = datetime.now()

		# if all((mytime["jobtime"][0] <= dt.hour <= mytime["jobtime"][1], dt.weekday() <= mytime["jobtime"][2])): # check_and_filter_by_job_time # another_time_no_clean_backup
		# open(files_base["backup"], "w", encoding="utf-8").close()

		# debug
		# exit()

		# any_to_mp4 # hide_for_debug
		'''
		try:
			with open(path_for_queue + "another.lst", encoding="utf-8") as palf:
				another_list = palf.readlines() # read(any/mp4/local)
		except:
			another_list = []

		cnt = 0

		if another_list:

			MM = MyMeta() #11

			processes_ram = processes_ram2 = []

			fsizes_list = []

			sum_value = avg_value = len_value = 0

			# with unique_semaphore:
			for al in filter(lambda x: x, tuple(another_list)):

				if not another_list:
					break

				if not os.path.exists(al.split(";")[0].strip()): # not al:
					continue

				# if al.split(";")[0].split("\\")[-1].count(".") == 1:
					# fsizes_list.append(os.path.getsize(al.split(";")[0].strip()))

			"""
			if fsizes_list:  # sleep_filter_by_avg(5)
				sum_value = (reduce(lambda x, y: x + y, fsizes_list)) # sum_value = sum(fsizes_list)
				len_value = len(fsizes_list)

				try:
					avg_value = (lambda s, l: s // l)(sum_value, len_value)
				except:
					avg_value = 0
			"""

			update_count = clean_count = 0

			max_cnt = len(another_list)
			prc = cnt = 0
			prc_set = set()

			MT = MyTime(seconds=2)

			fsizes: int = 0
			disk_space_limit: int = 16 * (1024**3) # 16Gb
			lastfile: list = []

			# @another_list # @last.xml @src=any_file/len=length(any_file)/dst=mp4_file # move_dst_to_src

			# xml(job(src=any_file/len=length(any_file)/dst=mp4_file)) # save_job_to_xml(any)

			# any_file = al.split(";")[0].strip() # job(any/mp4)
			# mp4_file = al.split(";")[1].strip() # local_project

			try:
				h, m = asyncio.run(load_timing_from_xml(ind=10)) # 10 # h, m = load_timing_from_xml(ind=10)
			except:
				h, m = 0, 0

			date1 = datetime.now()

			# with unique_semaphore:
			for al in another_list:
				date2 = datetime.now()

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60) # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				if hour[0]:
					write_log("debug hour[count][10]", "%d [another_list]" % (hour[0] // 60)) # is_index #10
					hour = hour[0] // 60

				try:
					assert isinstance(hour, int) and bool(hour <= 4), "Меньше установленого лимита по времени hour[10]" # 10 # is_assert_debug # 4 -> 3
				except AssertionError:  # if_null
					# logging.warning("Меньше установленого лимита по времени hour[10]")
					hour = 4 # limit_hour
					# raise err
				except BaseException as e:  # if_error
					logging.error("Меньше установленого лимита по времени hour[10] [%s]" % str(e))
					hour = 4

				# all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if all((all((hh > hour, hour)), int(prc) >= 50)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # mm[0] // 60 >= 1 # stop_if_more_hour_by_percent
					break

				cnt += 1

				try:
					prc = (cnt / max_cnt) * 100
					if not isinstance(prc, int):
						prc = int(prc)
				except:
					break
				else:
					if all((prc >= 0, not prc in prc_set, cnt <= max_cnt)):
						prc_set.add(prc)

				try:
					any_file = al.split(";")[0].strip() # job(any/mp4)
					mp4_file = al.split(";")[1].strip() # local_project
					fname = mp4_file.split("\\")[-1].strip() # short_filename
					move_file = al.split(";")[2].strip() + fname # job_folder + short_filename # any_drive_project
					path_for_folder1 = "c:\\downloads\\new\\"  # local_project
					move_file2 = path_for_folder1 + fname # local_folder + short_filename # local_project
				except BaseException as e:
					print(Style.BRIGHT + Fore.RED + "Ошибка пути [%s]" % str(e))
					write_log("debug paths[error]", "Ошибка пути [%s]" % str(e))
					continue
				else:
					cnt += 1

				lastfile.append(mp4_file) # save_to_xml_for_backup(clear_last) # @last.xml

				if not lastfile:
					continue

				try:
					fsize: int = os.path.getsize(any_file)
					dsize: int = disk_usage("c:\\").free
				except:
					fsize: int = 0
					dsize: int = 0

				if all(((fsize, dsize)):
					fsizes += fsize

					try:
						disk_space_limit = dsize - fsizes
					except:
						disk_space_limit = 0

					# "debug dspace[mp4][stop]": "..."
					if disk_space_limit <= 0: # if_less_zero
						print(dsize, fsizes, disk_space_limit, k) # is_color
						write_log("debug dspace[any][stop]", ";".join([str(dsize), str(fsizes), str(disk_space_limit), str(datetime.now())]))
						break

					# "debug dspace[mp4][limit]": "139/604/512/768;18/980/154/701;8/589/934/592;2023-04-03 11:03:23.116395",
					if all((dsize, fsizes, (disk_space_limit // (1024**3)) < 16, (disk_space_limit // (1024**3)) > 0)): # if_less_limit_job(16Gb)
						print(dsize, fsizes, disk_space_limit, k) # is_color
						write_log("debug dspace[any][limit]", ";".join([str(dsize), str(fsizes), str(disk_space_limit), str(datetime.now())]))
						break

					# d:\multimedia\video\serials_conv\8_Simple_Rules\8_Simple_Rules_01s27e.avi$c:\downloads\8_Simple_Rules_01s27e.mp4$c:\downloads\new\8_Simple_Rules_01s27e.mp4 [2022-04-06 21:40:04.025688]
					if all((any_file, mp4_file, move_file2)):
						print(Style.BRIGHT + Fore.YELLOW + "%s [%s]" % ("$".join([any_file, mp4_file, move_file2]),str(datetime.now()))) # any/project/local
						write_log("debug [paths/date]", "%s [%s]" % ("$".join([any_file, mp4_file, move_file2]),str(datetime.now())))

					if any_file[0] >= mp4_file[0]:  # and any_file.split(".")[-1].lower() != mp4_file.split(".")[-1].lower():  # drive_letter(diff/equal)

						try:
							dfile1, dfile2, dfile3 = any_file, mp4_file, move_file2
						except:
							dfile1 = dfile2 = dfile3 = ""
						finally:
							if all((dfile1, dfile2, dfile3)):
								print(Style.BRIGHT + Fore.BLUE + "%s" % "=-=>".join([dfile1, dfile2, dfile3]))

						try:
							if os.path.exists(any_file):
								codecs_data = MM.get_codecs(any_file)
						except:
							codecs_data = []

						if any((not codecs_data, len(codecs_data) < 2)):
							print(Style.BRIGHT + Fore.RED + "Ошибка чтения кодеков для %s [%d]" % (fname, len(codecs_data)))
							write_log("debug codecs[error]", "Ошибка чтения кодеков для %s [%d]" % (fname, len(codecs_data)))
							continue

						vcodec = "libx264" if codecs_data[0].lower() != "h264" else "copy"  # mp4(video)/copy
						acodec = "aac" if codecs_data[1].lower() != "aac" else "copy"  # aac(audio)/copy

						try:
							if any_file.split(".")[-1].lower() != "mp4":
								convert_cmd = "cmd /c "
								convert_cmd += "".join([path_for_queue,"ffmpeg.exe"])
								convert_cmd += " -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -threads 2 -c:a %s -f mp4 \"%s\" " % (any_file, vcodec, acodec, mp4_file)

							elif any_file.split(".")[-1].lower() == "mp4":
								convert_cmd = "cmd /c "
								convert_cmd += "".join([path_for_queue,"ffmpeg.exe"])
								convert_cmd += " -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -threads 2 -c:a %s \"%s\" " % (any_file, vcodec, acodec, mp4_file)
						except:
							convert_cmd = ""

						write_log("debug convert_cmd", "%s" % convert_cmd)

						if not convert_cmd: # skip_if_null
							continue

						try:
							with files_base["hours"] as fbh:
								mh = fbh.readlines()
						except:
							mh = []

						# filecmd_base # if_big_cinema_4_hours # if_tv_series_2_hours

						try:
							with open(filecmd_base, encoding="utf-8") as fbf:
								fb_dict = json.load(fbf)
						except:
							fb_dict = {}

							with open(filecmd_base, "w", encoding="utf-8") as fbf:
								json.dump(fb_dict, fbf, ensure_ascii=False, indent=4, sort_keys=True)
						# else:
							# if fb_dict:
								# fb_dict = {k:v for k, v in fb_dict.items() if any((v.count("scale") > 0, v.count("profile") > 0, v.count("level") > 0))} # need_optimize(scale/profile/level)

						year_regex = re.compile(r"[\d+]{4}")
						year_filter = []

						def filebase_to_year(fb_dict=fb_dict): #6
							for k, v in fb_dict.items():
								if year_regex.findall(k):
									yield k.strip()

						# year_filter = [k.strip() for k in [*fb_dict] if year_regex.findall(k)] # for k, _ in fb_dict.items()
						year_filter = list(filebase_to_year()) if list(filebase_to_year()) else [] # new(yes_gen)

						try:
							ds2 = disk_usage("d:\\").free
						except:
							ds2 = 0

						date2 = datetime.now()

						hour = divmod(int(abs(date1 - date2).total_seconds()), 60) # 60(min) -> 3600(hours) # update

						try:
							_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
						except:
							mm = abs(date1 - date2).seconds
							hh = mm // 3600
							mm //= 60
							# mm %= 60 # sec

						if hour[0]:
							write_log("debug hour[count][11]", "%d [another_list]" % (hour[0] // 60)) # is_index #11
							hour = hour[0] // 60

						try:
							assert isinstance(hour, int) and bool(hour <= 4), "Меньше установленого лимита по времени hour[11]" # 11 # is_assert_debug # 4 -> 3
						except AssertionError:  # if_null
							# logging.warning("Меньше установленого лимита по времени hour[11]")
							hour = 4 # limit_hour
							# raise err
						except BaseException as e:  # if_error
							logging.error("Меньше установленого лимита по времени hour[11] [%s]" % str(e))
							hour = 4

						# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
						if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_hour
							write_log("debug stop_job[another_list]", "Stop: at %s [%d]" % (any_file, cnt))

							break # stop_if_before_run

						# set_or_update(trends)_by_any_video # hidden(debug)
						try:
							with open(trends_base, encoding="utf-8") as ftf:
								trends_dict = json.load(ftf)

						except:
							trends_dict = {}

							with open(trends_base, "w", encoding="utf-8") as ftf:
								json.dump(trends_dict, ftf, ensure_ascii=False, indent=4, sort_keys=False) # save_by_modified

						fisrt_len = second_len = 0

						first_len = len(trends_dict)

						if len(mp4_file.strip()) > 0:
							try:
								trends_dict[crop_filename_regex.sub("", mp4_file.split("\\")[-1]).strip()] = unit_to_date(os.path.getmtime(mp4_file)) # modify_date
							except:
								trends_dict[crop_filename_regex.sub("", mp4_file.split("\\")[-1]).strip()] = str(datetime.now()) # current_date

						try:
							fdates = [v.strip() for _, v in trends_dict.items()]
						except:
							fdates = []
						else:
							fdates.sort(reverse=False)

						try:
							fdates_dict = {k:v for fd in fdates for k, v in trends_dict.items() if
												fd.strip() == v.strip()}
						except:
							fdates_dict = {}
						else:
							if all((fdates_dict, len(fdates_dict) <= len(trends_dict))): # trends_dict
								trends_dict = fdates_dict # update_without_sort

						trends_dict = {k:v for k, v in trends_dict.items() for s in sorted(trends_dict, key=lambda trends: ((trends[1], trends[0]))) if k == s}
						trends_dict = {k:v for k, v in trends_dict.items() if "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2]) in v.strip()} # stay_only_this_month(other_clear)

						second_len = len(trends_dict)

						if all((trends_dict, second_len)): # second_len <= first_len
							# save_by_(sort_base/filter_by_date)
							with open(trends_base, "w", encoding="utf-8") as ftf:
								json.dump(trends_dict, ftf, ensure_ascii=False, indent=4)

							with open(files_base["trends"], "w", encoding="utf-8") as fbtf:
								fbtf.writelines("%s\n" % t for t in [*trends_dict])

							write_log("debug trends_dict[save4]", "%s" % ";".join([";".join([*trends_dict]), str(datetime.now())]))

						# pccmd: int = -999

						# when_debug_continue / no_debug_run
						print(Style.BRIGHT + Fore.BLUE + "Run:", Style.BRIGHT + Fore.WHITE + "%s" % convert_cmd, end="\n")
						write_log("debug run[any]!", "%s" % convert_cmd)

						continue # pccmd = os.system(convert_cmd) # continue_if_debug / run # any

						# is_update = is_clean = False

						if all((pccmd == 0, convert_cmd)):
							try:
								gl1 = MM.get_length(any_file)
							except:
								gl1 = 0

							try:
								gl2 = MM.get_length(mp4_file)
							except:
								gl2 = 0

							try:
								fstatus = fspace(mp4_file, move_file2) # all((fsize, dsize, int(fsize // (dsize / 100)) <= 100))
							except:
								fstatus = False

							is_move = all((gl2 in range(gl1, gl1-5, -1), gl1, gl2))

							# print(Style.BRIGHT + Fore.CYAN + "Длина видео(ms): %s" % ";".join([str(gl2 >= gl1), str(gl1), str(gl2), dfile1]))
							# write_log("debug duration!", ";".join([str(gl2 >= gl1), str(gl1), str(gl2), dfile1])) # debug/test

							try:
								if all((is_move, fstatus)) and os.path.exists(mp4_file) and os.path.exists(any_file):

									# clear(null)_xml_if_ready_ok # @last.xml

									# is_update = True
									update_count += 1

									print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла", Style.BRIGHT + Fore.WHITE + "%s" % mp4_file) # add_to_all(process_move)

									p = multiprocessing.Process(target=process_move, args=(mp4_file, move_file2, False, True, 0)) # avg_value

									try:
										await process_move(mp4_file, move_file2, False, True, 0) # is_asyncio.run #7
									except BaseException as e:
										write_log("debug process_move[error][7]", ";".join([mp4_file, move_file2, str(e)]))
									else:
										write_log("debug process_move[ok][7]", ";".join([mp4_file, move_file2]))

									if not p in processes_ram:
										p.start()
										processes_ram.append(p)

									"""
									# move(mp4_file, move_file2)

									# if os.path.exists(mp4_file):
										# print(Style.BRIGHT + Fore.YELLOW + "Надо будет переместить файл %s" % dfile2)
										# write_log("debug movefile[any]!", "%s" % "~>".join([dfile2, dfile3]))
									# elif not os.path.exists(mp4_file):
										# print(Style.BRIGHT + Fore.GREEN + "Файл был %s перемещён" % dfile2)
										# write_log("debug movefile", "%s" % "~>".join([dfile2, dfile3]))
									"""

									p2 = multiprocessing.Process(target=process_delete, args=(any_file, ))

									# asyncio.run(process_delete(any_file))

									if not p2 in processes_ram2:
										p2.start()
										processes_ram2.append(p2)

									"""
									# os.remove(any_file)

									# if os.path.exists(any_file):
										# print(Style.BRIGHT + Fore.YELLOW + "Надо будет удалить оригинальный файл %s" % dfile1)
										# write_log("debug deletefile[any]!", "Надо будет удалить оригинальный файл %s" % dfile1)
									# elif not os.path.exists(any_file):
										# print(Style.BRIGHT + Fore.GREEN + "Оригинальный файл был %s удален" % dfile1)
										# write_log("debug deletefile", "Оригинальный файл был %s удален" % dfile1)
									"""

								elif any((not is_move, not fstatus)) and os.path.exists(mp4_file):

									# is_clean = True
									clean_count += 1

									p = multiprocessing.Process(target=process_delete, args=(mp4_file, ))

									# asyncio.run(process_delete(mp4_file))

									if not p in processes_ram2:
										p.start()
										processes_ram2.append(p)

									"""
									# os.remove(mp4_file)

									# if os.path.exists(mp4_file):
										# print(Style.BRIGHT + Fore.RED + "Ошибка длины или нет места для переноса файла %s" % dfile2)
										# write_log("debug deletefile[any]!", "Ошибка длины или нет места для переноса файла %s" % dfile2)
									# elif not os.path.exists(mp4_file):
										# print(Style.BRIGHT + Fore.WHITE + "Файл был %s удален" % dfile2)
										# write_log("debug deletefile", "Файл был %s удален" % dfile2)
									"""

							except BaseException as e:
								# print(Style.BRIGHT + Fore.RED + "Не могу перенести или обновить файл %s [%s]" % (full_to_short(mp4_file), str(e)))
								print(Style.BRIGHT + Fore.RED + "Не могу перенести или обновить файл %s [%s]" % (mp4_file, str(e)))

								write_log("debug cant move/delete", "Не могу перенести или обновить файл %s [%s]" % (mp4_file, str(e)))
								# continue
							else:
								if any((update_count, clean_count)):  # some_count
									print(Style.BRIGHT + Fore.CYAN + "Было обновлено %d и удалено %d фалов(а)" % (update_count, clean_count))
									write_log("debug updateclean", "Было обновлено %d и удалено %d фалов(а)" % (update_count, clean_count))

						# time_is_limit_1hour_50min
						if all((h >= 0, m, hh >= h, mm >= m)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # mm[0] // 60 >= 2:  # stop_if_more_2hour
							write_log("debug stop_job[another_list]", "Stop: at %s [%d]" % (any_file, cnt))

							try:
								fdate, status = asyncio.run(datetime_from_file(lastfile[-1]))
							except:
								fdate, status = datetime.now(), False
							else:
								if any((fdate.hour < mytime["sleeptime"][1], all(( hh >= h, mm >= m)))):
									if os.path.exists(lastfile[-1]):
										os.remove(lastfile[-1])
										lastfile.remove(lastfile[-1])

							break # stop_if_after_run

				print()

				len_proc = len(processes_ram) + len(processes_ram2)

				if len_proc:
					MySt = MyString() # MyString("Запускаю:", "[6 из 6]")

					try:
						print(Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="Запускаю:", endtxt="[6 из 6]", count=len_proc, kw="задач"))
						# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
					except:
						print(Style.BRIGHT + Fore.YELLOW + "Обновляю или удаляю %d файлы(а,ов) [6 из 6]" % len_proc) # old(is_except)
					else:
						write_log("debug run[task7]", MySt.last2str(maintxt="Запускаю:", endtxt="[6 из 6]", count=len_proc, kw="задач"))

					del MySt

				# --- move_block / test / debug ---
				if processes_ram:
					with unique_semaphore:
						for p7 in processes_ram:
							p7.join() # terminate -> join

				# --- delete_block / test / debug ---
				if processes_ram2:
					with unique_semaphore:
						for p7 in processes_ram2:
							p7.join() # terminate -> join

				# clear_when_exit_or_ready(any) / hide_if_not_clear_combine_jobs
				# with open(cfilecmd_base, "w", encoding="utf-8") as cbf:
					# json.dump({}, cbf, ensure_ascii=False, indent=4, sort_keys=False)

			del MT

			del MM

			# xml(job(src=any_file/len=length(any_file)/dst=mp4_file)) # load_job_from_xml(any)
		'''

	if job_count:
		# MT = MyTime(seconds=2)
		# MT.sleep_with_count(ms=MT.seconds)
		# del MT

		asyncio.run(project_done())  # before_jobs_start # update_project
		asyncio.run(update_bigcinema())  # update_cinema
		asyncio.run(project_update())  # updates(if_downloaded)
		# true_project_rename(folder=copy_src); true_project_rename() # check_and_rename
		asyncio.run(true_project_rename())  # check_and_rename

	# open(path_for_queue + "another.lst", "w", encoding="utf-8").close() # is_csv(clean_not_mp4_ext)

	# --- check_and_filter_dicts ---
	# load_meta_jobs(filter) #10 # {"fullname":"meta_params"}
	try:
		with open(some_base, encoding="utf-8") as sbf:
			somebase_dict = json.load(sbf)
	except:
		somebase_dict = {}

		with open(some_base, "w", encoding="utf-8") as sbf:
			json.dump(somebase_dict, sbf, ensure_ascii=False, indent=4, sort_keys=True)

	# jobs_base_load(hidden) # {"fullname":"command_line"}
	try:
		with open(filecmd_base, encoding="utf-8") as fbf:
			fb_dict = json.load(fbf)
	except:
		fb_dict = {}

		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump(fb_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False)

	# last_jobs_by_count # pass_1_of_2

	first_len = second_len = 0

	# filter_current_jobs_(in_meta/no_in_meta/exists_only)
	try:
		first_len = len(fb_dict)
		fb_dict = {
			k: v
			for k, v in fb_dict.items()
			if os.path.exists(k)
			and any((k.strip() in [*somebase_dict], not [*somebase_dict]))
		}
	except:
		fb_dict = {k: v for k, v in fb_dict.items() if os.path.exists(k)}
	finally:
		second_len = len(fb_dict)  # equal/diff

	if all((second_len, second_len < first_len)):
		print(
			Style.BRIGHT
			+ Fore.CYAN
			+ "Количество заданий было %d стало %d [%s]"
			% (first_len, second_len, str(datetime.now()))
		)  # is_color
		write_log(
			"debug filecmdbase_dict[changed]",
			"Количество заданий было %d стало %d [%s]"
			% (first_len, second_len, str(datetime.now())),
		)
	elif all((second_len, second_len == first_len)):
		print(
			Style.BRIGHT
			+ Fore.WHITE
			+ "Количество заданий не изменилось [%s]" % str(datetime.now())
		)  # is_color
		write_log(
			"debug filecmdbase_dict[not_changed]",
			"Количество заданий не изменилось [%s]" % str(datetime.now()),
		)
	elif all((not first_len, first_len != second_len)):
		print(
			Style.BRIGHT
			+ Fore.YELLOW
			+ "На данный момент все задания выполнены или отсуствуют [%s]"
			% str(datetime.now())
		)  # is_color
		write_log(
			"debug filecmdbase_dict[no_jobs]",
			"На данный момент все задания выполнены или отсуствуют [%s]"
			% str(datetime.now()),
		)

	# last_jobs_by_short # pass_2_of_2

	fcl: list = []

	try:
		# fcl: list = list(set([crop_filename_regex.sub("", fd.split("\\")[-1]).strip() for fd in fb_dict if fd]))
		fcl: list = list(
			set(
				[
					crop_filename_regex.sub("", fn).strip()
					for fd in fb_dict
					for fp, fn in split_filename(fd)
					if ((fn, fd, fn == fd.split("\\")[-1]))
				]
			)
		)
	except:
		fcl: list = []
	finally:
		fcl_str = (
			"%s [%s]" % (";".join(list(set(fcl))), str(datetime.now()))
			if fcl
			else "На данный момент все задания выполнены или отсуствуют [%s]"
			% str(datetime.now())
		)  # debug/test

		print(Style.BRIGHT + Fore.YELLOW + "%s" % fcl_str)  # list_jobs
		write_log(
			"debug fcl[short_jobs]", "%s" % fcl_str
		)  # last_jobs_after_filter(without_save)

	if all((second_len, second_len <= first_len)):  # if_stay_some(>0)_or_all_ready(0)
		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump(
				fb_dict, fbf, ensure_ascii=False, indent=4, sort_keys=False
			)  # stay_files_only_in_meta

	# update_trends_by_top
	"""
	try:
		with open(trends_base, encoding="utf-8") as tbf:
			trends_dict = json.load(tbf)
	except:
		trends_dict = {}

	first_len = len(trends_dict)

	if trends_dict: # include_only_days # pass_1_of_2
		try:
			with open(update_days_file, encoding="utf-8") as udff:
				update_days_list = udff.readlines()
		except:
			update_days_list = []

		if update_days_list:
			for udl in update_days_list:
				if not udl.strip() in [*trends_dict]:
					trends_dict[udl.strip()] = str(datetime.now())

		# @update_month_file(update_month_list)
		# @update_year_file(update_year_list)

	if trends_dict: # pass_2_of_2
		# trends_dict = {k:v for k, v in trends_dict.items() if any((not k in update_month_list, not k in update_year_list))} # filter_by_month_and_year
		trends_dict = {k:v for k, v in trends_dict.items()} # filter_by_days

	second_len = len(trends_dict)

	if all((trends_dict, second_len)): # second_len <= first_len
		trends_dict = {k:v for k, v in trends_dict.items() for s in sorted(trends_dict, key=lambda trends: ((trends[1], trends[0]))) if k == s}
		trends_dict = {k:v for k, v in trends_dict.items() if "-".join(str(datetime.today()).split(" ")[0].split("-")[0:2]) in v.strip()} # stay_only_this_month(other_clear)
		
		# save_by_(sort_base/filter_by_date)
		with open(trends_base, "w", encoding="utf-8") as udff:
			json.dump(trends_dict, udff, ensure_ascii=False, indent=4, sort_keys=False) # save_update_trends # save_by_modified

		with open(files_base["trends"], "w", encoding="utf-8") as fbtf:
			fbtf.writelines("%s\n" % t for t in [*trends_dict])

		write_log("debug trends_dict[save5]", "%s" % ";".join([";".join([*trends_dict]), str(datetime.now())]))
	"""

	# jobs_trends_dict = {k: str(datetime.now()) for k, v in trends_dict.items() for k2, v2 in filecmdbase_dict.items() if k.strip() == crop_filename_regex.sub("", k2).strip()}  # k, k2

	asyncio.run(combine_br())  # combine_br_for_unique_filenames # at_end

	# update_"days/month/year"_file(+add_to_trends/sizes_by_top)
	original_days_file: str = os.path.join(path_for_queue, "days_ago.lst")
	update_days_file: str = (
		r"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\days_ago.lst"
	)
	update_days_file2: str = r"c:\\users\\sergey\\videos\\days_ago.lst"

	original_month_file: str = os.path.join(path_for_queue, "month_forward.lst")
	update_month_file: str = (
		r"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\month_forward.lst"
	)
	update_month_file2: str = r"c:\\users\\sergey\\videos\\month_forward.lst"

	original_year_file: str = os.path.join(path_for_queue, "calc_year.lst")
	update_year_file: str = (
		r"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\calc_year.lst"
	)
	update_year_file2: str = r"c:\\users\\sergey\\videos\\calc_year.lst"

	original_trend_file: str = os.path.join(path_for_queue, "trends.lst")
	update_trend_file: str = (
		r"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\trends.lst"
	)
	update_trend_file2: str = r"c:\\users\\sergey\\videos\\trends.lst"

	original_sizes_file: str = os.path.join(path_for_queue, "video_resize.int")
	# update_sizes_file: str = r"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\video_resize.lst"
	update_sizes_file: str = r"c:\\users\\sergey\\videos\\video_resize.lst"

	original_short_file: str = os.path.join(path_for_queue, "short.lst")
	update_short_file: str = r"c:\\users\\sergey\\videos\\short.txt"

	# @days
	# os.system("cmd /c copy nul %s" % update_days_file)
	# os.system("cmd /c copy nul %s" % update_days_file2)

	if os.path.exists(original_days_file) and os.path.getsize(original_days_file):

		# optimize_list # debug
		# '''
		try:
			with open(original_days_file, encoding="utf-8") as odf:  # update_days_file
				days_files = list(set(odf.readlines()))
		except:
			days_files = []
		else:
			if days_files:
				# days_files_filter = list(set([df.strip() for df in days_files for df2 in days_files if all((df != df2, df in df2))]))
				# days_files_filter2 = list(set([dff.strip() for dff in days_files_filter if not dff in days_files_filter]))
				# days_files = list(set(days_files_filter2)) if days_files_filter2 else []

				if days_files:
					with open(update_days_file, "w", encoding="utf-8") as odf:
						odf.writelines(
							"%s" % df for df in filter(lambda x: x, tuple(days_files))
						)

					if os.path.exists(update_days_file) and os.path.getsize(
						original_days_file
					):
						if os.path.exists(update_days_file2) and os.path.getsize(
							update_days_file
						) != os.path.getsize(update_days_file2):
							copy(update_days_file, update_days_file2)
						elif not os.path.exists(update_month_file2):
							copy(update_days_file, update_days_file2)
		# '''

		# @month
		# os.system("cmd /c copy nul %s" % update_month_file)
		# os.system("cmd /c copy nul %s" % update_month_file2)

	if os.path.exists(original_month_file) and os.path.getsize(original_month_file):

		# optimize_list # debug
		# '''
		try:
			with open(
				original_month_file, encoding="utf-8"
			) as omf:  # update_month_file
				month_files = list(set(omf.readlines()))
		except:
			month_files = []
		else:
			if month_files:
				# month_files_filter = list(set([mf.strip() for mf in month_files for mf2 in month_files if all((mf != mf2, mf in mf2))]))
				# month_files_filter2 = list(set([mff.strip() for mff in month_files_filter if not mff in month_files_filter]))
				# month_files = list(set(month_files_filter2)) if month_files_filter2 else []

				if month_files:
					with open(update_month_file, "w", encoding="utf-8") as omf:
						omf.writelines(
							"%s" % mf for mf in filter(lambda x: x, tuple(month_files))
						)

					if os.path.exists(update_month_file) and os.path.getsize(
						original_month_file
					):
						if os.path.exists(update_month_file2) and os.path.getsize(
							update_month_file
						) != os.path.getsize(update_month_file2):
							copy(update_month_file, update_month_file2)
						elif not os.path.exists(update_month_file2):
							copy(update_month_file, update_month_file2)
		# '''

	# @year
	# os.system("cmd /c copy nul %s" % update_year_file)
	# os.system("cmd /c copy nul %s" % update_year_file2)

	if os.path.exists(original_year_file) and os.path.getsize(original_year_file):

		# optimize_list # debug
		# '''
		try:
			with open(original_year_file, encoding="utf-8") as oyf:  # update_year_file
				year_files = list(set(oyf.readlines()))
		except:
			year_files = []
		else:
			if year_files:
				# year_files_filter = list(set([yf.strip() for yf in year_files for yf2 in year_files if all((yf != yf2, yf in yf2))]))
				# year_files_filter2 = list(set([yff.strip() for yff in year_files_filter if not yff in year_files_filter]))
				# year_files = list(set(year_files_filter2)) if year_files_filter2 else []

				if year_files:
					with open(update_year_file, "w", encoding="utf-8") as oyf:
						oyf.writelines(
							"%s" % yf for yf in filter(lambda x: x, tuple(year_files))
						)

					if os.path.exists(update_year_file) and os.path.getsize(
						original_year_file
					):
						if os.path.exists(update_year_file2) and os.path.getsize(
							update_year_file
						) != os.path.getsize(update_year_file2):
							copy(update_year_file, update_year_file2)
						elif not os.path.exists(update_year_file2):
							copy(update_year_file, update_year_file2)
		# '''

	# @trend
	# os.system("cmd /c copy nul %s" % update_trend_file)
	# os.system("cmd /c copy nul %s" % update_trend_file2)

	if os.path.exists(original_trend_file) and os.path.getsize(original_trend_file):

		# optimize_list # debug
		# '''
		try:
			with open(
				original_trend_file, encoding="utf-8"
			) as otf:  # update_trend_file
				trend_files = list(set(otf.readlines()))
		except:
			trend_files = []
		else:
			if trend_files:
				# trend_files_filter = list(set([tf.strip() for tf in trend_files for tf2 in trend_files if all((tf != tf2, tf in tf2))]))
				# trend_files_filter2 = list(set([tff.strip() for tff in trend_files_filter if not tff in trend_files_filter]))
				# trend_files = list(set(trend_files_filter2)) if trend_files_filter2 else []

				if trend_files:
					with open(update_trend_file, "w", encoding="utf-8") as otf:
						otf.writelines(
							"%s" % tf for tf in filter(lambda x: x, tuple(trend_files))
						)

					if os.path.exists(update_trend_file) and os.path.getsize(
						original_trend_file
					):
						if os.path.exists(update_trend_file2) and os.path.getsize(
							update_trend_file
						) != os.path.getsize(update_trend_file2):
							copy(update_trend_file, update_trend_file2)
						elif os.path.exists(update_trend_file2):
							copy(update_trend_file, update_trend_file2)
		# '''

	# @sizes
	# os.system("cmd /c copy nul %s" % update_sizes_file)

	if os.path.exists(original_sizes_file) and os.path.getsize(original_sizes_file):

		# optimize_list # debug
		# '''
		try:
			with open(
				original_sizes_file, encoding="utf-8"
			) as osf:  # update_sizes_file
				sizes_files = list(set(osf.readlines()))
		except:
			sizes_files = []
		else:
			if sizes_files:
				# sizes_files_filter = list(set([sf.strip() for sf in sizes_files for sf2 in sizes_files if all((sf != sf2, sf in sf2))]))
				# sizes_files_filter2 = list(set([sff.strip() for sff in sizes_files_filter if not sff in sizes_files_filter]))
				# sizes_files = list(set(sizes_files_filter2)) if sizes_files_filter2 else []

				if sizes_files and os.path.getsize(original_sizes_file):
					if os.path.exists(update_sizes_file) and os.path.getsize(
						original_sizes_file
					) != os.path.getsize(update_sizes_file):
						with open(update_sizes_file, "w", encoding="utf-8") as osf:
							osf.writelines(
								"%s" % sf
								for sf in filter(lambda x: x, tuple(sizes_files))
							)
					elif not os.path.exists(update_sizes_file):
						with open(update_sizes_file, "w", encoding="utf-8") as osf:
							osf.writelines(
								"%s" % sf
								for sf in filter(lambda x: x, tuple(sizes_files))
							)

					# copy(update_sizes_file, update_sizes_file2)
		# '''

	# @short
	# os.system("cmd /c copy nul %s" % update_short_file)

	if os.path.exists(original_short_file) and os.path.getsize(original_short_file):

		# optimize_list # debug
		# '''
		try:
			with open(
				original_short_file, encoding="utf-8"
			) as osf:  # update_short_file
				short_files = list(set(osf.readlines()))
		except:
			short_files = []
		else:
			if short_files:
				# short_files_filter = list(set([sf.strip() for sf in short_files for sf2 in short_files if all((sf != sf2, sf in sf2))]))
				# short_files_filter2 = list(set([sff.strip() for sff in short_files_filter if not sff in short_files_filter]))
				# short_files = list(set(short_files_filter2)) if short_files_filter2 else []

				if short_files and os.path.getsize(original_short_file):
					if os.path.exists(update_short_file) and os.path.getsize(
						original_short_file
					) != os.path.getsize(update_short_file):
						with open(update_short_file, "w", encoding="utf-8") as osf:
							osf.writelines(
								"%s" % sf
								for sf in filter(lambda x: x, tuple(short_files))
							)
					elif not os.path.exists(update_short_file):
						with open(update_short_file, "w", encoding="utf-8") as osf:
							osf.writelines(
								"%s" % sf
								for sf in filter(lambda x: x, tuple(short_files))
							)

					# copy(update_short_file, update_short_file2)
		# '''

	# check_time_after_run(finish)
	ctme = datetime.now()

	asyncio.run(shutdown_if_time())  # no_date="29.08.2023"

	end = time()

	finish = int(abs(end - start))

	if files_count:
		logging.info(
			"video_resize.py run, time: %d ms, count: %d, time_per_file_list: %s"
			% (
				ms_to_time(finish),
				files_count,
				";".join(
					[
						str(files_count / ms_to_time(finish)),
						str(ms_to_time(finish) / files_count),
					]
				),
			)
		)

	sizes_dict: dict = {}

	sizes_dict[1] = "Kb"
	sizes_dict[2] = "Mb"
	sizes_dict[3] = "Gb"

	try:
		dsize: int = disk_usage("c:\\").free
		assert dsize, ""
	except AssertionError:
		dsize = 0
	finally:
		if os.path.exists(log_file) and os.path.getsize(log_file):
			fsizes_lst = [
				(os.path.getsize(log_file) // (1024**i), sizes_dict[i])
				for i in range(1, 4)
				if os.path.getsize(log_file) // (1024**i) > 0
			]
			logging.info("@dsize logging size: %s" % str(fsizes_lst))

		if dsize:
			fsizes_lst = [
				(dsize // (1024**i), sizes_dict[i])
				for i in range(1, 4)
				if dsize // (1024**i) > 0
			]
			logging.info("@dsize logging dsize: %s" % str(fsizes_lst))

	# if_need_clean_"error"_from_log
	write_log("debug end", f"{str(datetime.now())}")
	MyNotify(txt=f"Программа завершена {str(datetime.now())}", icon=icons["finish"])

	if all(
		(jcount, dt.hour > mytime["jobtime"][1], dt.weekday() <= mytime["jobtime"][2])
	):  # sound_notify_if_some_job_run(after_job_time)
		# sound_notify(text=f"Программа завершена {str(datetime.now())}") # debug/test(date_include)
		sound_notify(text="Программа завершена")  # only_text

	logging.info(f"@finish {str(datetime.now())}")

	# clear_globals
	try:
		glob_dict = vars()
		assert glob_dict, ""
	except AssertionError:
		logging.warning("@glob_dict empty")

	try:
		ext = "".join([".", __file__.split("\\")[-1].split(".")[-1]])
	except:
		ext = ""

	try:
		filename = "\\".join([script_path, __file__.replace(ext, ".glob")])
	except:
		filename = ""
	else:
		if filename:
			try:
				with open(filename, "w", encoding="utf-8") as fj:
					json.dump(
						glob_dict, fj, ensure_ascii=False, indent=4, sort_keys=False
					)
			except:
				with open(filename, "w", encoding="utf-8") as fj:
					json.dump({}, fj, ensure_ascii=False, indent=4, sort_keys=False)

	flist = list(filter(lambda x: x[0] != "_", [*glob_dict]))

	try:
		for k, _ in glob_dict.items():
			try:
				assert k, ""  # bool(k in flist) and flist, ""
			except AssertionError:
				continue
			else:
				logging.info("@vars %s, id: %s" % (k, str(id(k))))
				del k
	except:
		pass
