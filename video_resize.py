# -*- coding: utf-8 -*-

# --- manual ---

# PyCharm/Spyder(anaconda) (Оптимизировать и уменьшить код, для анализа)
# "удалить" лишние комментарии, чтобы был чистый код

# threadsing vs asyncio

# Проверить процедуры, классы, алгоритмы и т.п. которые можно убрать(почистить)

# import io
from concurrent.futures import ThreadPoolExecutor  # Thread by pool # man+ / youtube
from datetime import datetime  # datetime
from functools import reduce
from os import getcwd  # current_folder
from psutil import cpu_count  # Process # psutil (process and system utilities)
from shutil import disk_usage, copy, move  # файлы
from time import time, sleep  # ctime, perf_counter, strftime, localtime  # время-задержка
from win10toast import ToastNotifier  # An easy-to-use Python library for displaying Windows 10 Toast Notifications
import ctypes
import json
import logging
# import multiprocessing
import os  # система
import psutil
import pyttsx3  # files_dict
import re  # regular_expression
import sys  # system
import zipfile  # zip archive # backup(job)/after(del/if_done) # UserWarning: Duplicate name
# import argparse  # system # sys.argv -> argparse
import sqlite3 as sql  # sqlite db-api
import xml.etree.ElementTree as xml  # ?pip
import asyncio # TaskGroup(3.11+)
from getmac import get_mac_address # pip install -U getmac # mac_tools
import socket # socket_commands
# from mac_vendor_lookup import MacLookup # pip install -U mac_vendor_lookup # MacLookup().lookup("cc:32:e5:59:ae:12")


from threading import (  # Thread # Barrier # работа с потоками # mutli_async
	Semaphore)

from subprocess import (  # Работа с процессами # console shell=["True", "False"]
	run )  # TimeoutExpired, check_output, Popen, call, PIPE, STDOUT

from colorama import (  # Cursor # Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows. # Fore.color, Back.color # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
	Fore, Style, init)  # Back

# go_in_project_folder
os.chdir("c:\\downloads\\mytemp")

script_path: str = os.path.dirname(os.path.realpath(__file__))

# logging.basicConfig(level=logging.INFO)

# with_encoding # utf-8 -> cp1251
logging.basicConfig(handlers=[logging.FileHandler("".join([script_path, "\\videoresize.log"]), "w", "cp1251")],
					format=u'%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s',
					level=logging.INFO)  # filename / lineno / name / levelname / message / asctime # save_logging_manuals

logging.info(f"debug start {str(datetime.now())}")

mytime: dict = {"jobtime": [9, 18, 4], "dinnertime": [12, 13], "sleeptime": [0, 7], "anytime": [True]}

# '''
# 640x360 -> 1280x720 -> 1920x1080 # 16/9(hd)

# @16/9(hd) # 8/16
async def hd_generate(from_w: int = 640, from_h: int = 360, to_max: int = 2500, bit: int = 16) -> list:
	scales: list = []

	try:
		scales = list(set(["x".join([str(w), str(h)]) for w in range(from_w, to_max, bit) for h in range(from_h, to_max, bit) if w/h == (16/9)]))

		assert scales, "Ошибка hd маштабов @hd_generate/scales" # is_assert(debug)
	except AssertionError as err:
		scales = []
		logging.warning("Ошибка hd маштабов @hd_generate/scales")
		raise err
	else:
		scales.sort(reverse=False)
		# print(scales)

	return scales

# 640x360, 896x504, 1152x648, 1408x792, 1664x936, 1920x1080, 2176x1224, 2432x1368

# @4/3(sd) # 8/16
async def sd_generate(from_w: int = 640, from_h: int = 480, to_max: int = 2500, bit: int = 16) -> list:

	scales: list = []

	try:
		scales = list(set(["x".join([str(w), str(h)]) for w in range(from_w, to_max, bit) for h in range(from_h, to_max, bit) if w/h == (4/3)]))

		assert scales, "Ошибка sd маштабов @sd_generate/scales" # is_assert(debug)
	except AssertionError as err:
		scales = []
		logging.warning("Ошибка sd маштабов @sd_generate/scales")
		raise err
	else:
		scales.sort(reverse=False)
		# print(scales)

	return scales

# 640x480, 704x528, 768x576, 832x624, 896x672, 960x720, 1024x768, 1088x816, 1152x864, 1216x912, 1280x960, 1344x1008
# 1408x1056, 1472x1104, 1536x1152, 1600x1200, 1664x1248, 1728x1296, 1792x1344, 1856x1392, 1920x1440, 1984x1488
# 2048x1536, 2112x1584, 2176x1632, 2240x1680, 2304x1728, 2368x1776, 2432x1824, 2496x1872
# '''

# ffmpeg -y -i input -c:v libx264 -vf scale=640:-1 -c:a aac -af dynaudnorm output # stay_profile_high # stay_metadata
# use_by_default_manual(height % 2 == 0) # "720" >= 640

'''
import re

emails = input().split()

res = filter(lambda x: re.findall(r'^[\w]+@[\w]+.[\w]', x), emails)
print(*res)

'''

# ((1682355156 / 1000) // 60) % 60 ~ 19min
# time.time() * 1000 = ?ms (1682355745739.1763) ~ (1682355745739.1763 // 60) % 60 ~ 28min

if not os.path.exists(r"c:\\downloads\\mytemp"):
	os.chdir(r"c:\\downloads\\mytemp")

curdir: str = getcwd()
if not "mytemp" in curdir.split("\\")[-1].lower():
	curdir = r"c:\\downloads\\mytemp"
	os.chdir(curdir)

dt = datetime.now()

# worktime monday-friday(0-4) (00:00 - 18:00) / weekdays saturday-sunday(5-6) (00:00 - 18:00)
# is_zoomtime everyday (22:00 - 24:00)
if any((dt.weekday() <= mytime["jobtime"][2], dt.weekday() > mytime["jobtime"][2])) and dt.minute < 60:
	# ishide_console_on_start

	is_error: bool = False

	kernel32 = ctypes.WinDLL('kernel32')
	user32 = ctypes.WinDLL('user32')

	SW_HIDE, SW_SHOW = 0, 6

	try:
		hWnd = kernel32.GetConsoleWindow()
		# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6) # console_popup_window # samples_for_window # show
		# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) # console_popup_window # samples_for_window # hide
	except BaseException as e:
		is_error = True
		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
	finally:
		if is_error == False:
			if hWnd:
				if mytime["jobtime"][0] <= dt.hour <= mytime["jobtime"][1]:
					user32.ShowWindow(hWnd, SW_HIDE) # new

					# print(f"Приложение успешно свёрнуто в {str(dt)}")
					with open(curdir + "\\minimized_vr.pid", "w", encoding="utf-8") as mpf:
						mpf.write(f"Приложение успешно свёрнуто в {str(dt)}")
				else:
					user32.ShowWindow(hWnd, SW_SHOW) # new

					# print(f"Приложение успешно разсвёрнуто в {str(dt)}")
					with open(curdir + "\\maximized_vr.pid", "w", encoding="utf-8") as mpf:
						mpf.write(f"Приложение успешно разсвёрнуто в {str(dt)}")


init(autoreset=True)  # init text color's

job_count: int = 0

# --- CPU optimize ---
ccount: int = int(cpu_count(logical=True))  # False
unique_semaphore = Semaphore(ccount)

# --- path's ---
path_for_queue: str = "c:\\downloads\\mytemp\\"
path_to_done: str = "c:\\downloads\\"  # mytemp\\temp\\
path_for_folder1: str = "c:\\downloads\\new\\"
path_for_segments: str = "c:\\downloads\\mytemp\\segments\\" # for_m3u8(ts_segments)
copy_src: str = "C:\\Downloads\\Combine\\Original\\TvSeries\\".lower()
copy_src2: str = "C:\\Downloads\\Combine\\Original\\BigFilms\\".lower()

envdict = os.getenv.__globals__ # переменные_среды

userprofile: str = envdict["environ"]["userprofile"].lower() # os.getenv("USERPROFILE") # r"c:\\users\\sergey
programfiles: str = envdict["environ"]["programfiles"].lower() # os.getenv("PROGRAMFILES") # r"c:\\program files

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
copy_folders: str = r"c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\current.lst"  # is_current_short_folders # +copy
error_base: str = "".join([path_for_queue, "error.json"])  # any_error_for_debug
filecmd_base: str = "".join([path_for_queue, "fcd.json"])  # Command line for job file
fps_base: str = "".join([path_for_queue, "fps.json"])  # fps(frame_rates)
jobs_base: str = "".join([path_for_queue, "jobs.json"])  # ?
padeji_base: str = "".join([path_for_queue, "padeji.json"])  # words_ends
paths_base: str = "".join([path_for_queue, "sdpaths.json"])  # short_folder
short_folders: str = "".join([path_for_queue, "short.lst"])  # current_folders # +orig
some_base: str = "".join([path_for_queue, "somebase.json"])  # filename + meta
trends_base: str = "".join([path_for_queue, "trends.json"])  # last_jobs
unique_base: str = "".join([path_for_queue, "unique_data.json"])  # meta_data
vbr_base: str = "".join([path_for_queue, "vbr.json"])  # vbr_calc
vr_files: str = "".join([path_for_queue, "video_resize.lst"])  # files(files_from_video_resize.dir) # txt -> json
vr_folder: str = "".join([path_for_queue, "video_resize.dir"])  # folders_with_files(length > 1) # txt -> json
soundtrack_base: str = "".join([path_for_queue, "soundtrack.json"])  # popular_sound_track
soundtrack_tbase: str = "".join([path_for_queue, "tsoundtrack.json"])  # temp_sound_track(debug_json)
new_optimize_base: str = "".join([path_for_queue, "neop.json"])  # new_or_optimize(is_learn)
cfilecmd_base: str = "".join([path_for_queue, "cfcd.json"])  # Command line for job file + joined
desc_base: str = "".join([path_for_queue, "descriptions.json"])  # descriptions
desc_base_temp: str = "".join([path_for_queue, "descriptions_temp.json"])  # descriptions(is_debug/is_manual)
dar_base: str = "".join([path_for_queue, "dar.json"])  #d(isplay)aspect_ratio
par_base: str = "".join([path_for_queue, "par.json"])  #p(ixel)aspect_ratio
sar_base: str = "".join([path_for_queue, "sar.json"])  #s(cale)aspect_ratio
std_base: str = "".join([path_for_queue, "std.json"])  #s(peed)/t(ime)/d(ata)

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
	"stracks": "".join([path_for_queue, "soundtrack.lst"])
}

open(files_base["soundtrack"], "w", encoding="utf-8").close()

# ctme.hour # ctime.weekday()
mytime: dict = {"jobtime": [9, 18, 4], "dinnertime": [12, 13], "sleeptime": [0, 7], "anytime": [True]}

# --- regex_codes ---
# seasyear = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))", re.M) # MatchCase # season_and_year(findall)
# big_film_regex = re.compile(r"\([\d+]{4}\)", re.M) # MatchCase # cinema(findall)

# IgnoreCase # short_filename_regex # short_year(sub)_regex # default_filter # (57)
crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)", re.I)
# template_for_seasonvar_filter(season_and_episode)(tv_series_only) # (2)
crop_filename_regex2 = re.compile(r"([sS]{1}[\d+]{1,2})\.([eE]{1}[\d+]{1,2})", re.I)

lang_regex = re.compile(r"_[A-Z]{1}[a-z]{2}$", re.M)  # MatchCase # europe_language(find_all) # (6)

# .webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf

# MatchCase # find_files(findall)
video_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$",
	re.M)  # (38)
video_ext_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$",
	re.M)  # (37)

# --- Overload process ---

# 5%
big_process: list = []
pid_process: list = []
skip_process: list = []

open("c:\\downloads\\mytemp\\overload.csv", "w", encoding="utf-8").close()

with open("c:\\downloads\\mytemp\\overload.csv", "a") as ocf:
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


# group_of_data # debug
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


async def dict_filter(dct: dict = {}, sort_index: int = -1) -> dict: # 1

	try:
		assert dct, "Пустой словарь @dict_filter/dct" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Пустой словарь @dict_filter/dct")
		raise err
		return []

	# if not dct:
		# return [] # return_null_if_dict_null

	dct_new: dict = {}
	lst_new: list = [] # default_list

	# for k, v in dct.items():
		# if all((os.path.exists(k), k.split(".")[-1])): # exists / +extension
			# tup = (k, v) # fullfilename / some_data
			# lst_new.append(tup)

	lst_new = [(k, v) for k, v in dct.items() if all((os.path.exists(k), k.split(".")[-1]))]

	if all((lst_new, sort_index != -1)):
		lst_sort: list = [] # sorted_list

		try:
			len_tuple = len(lst_new[0])
		except:
			len_tuple = 0

		try:
			if len_tuple >= sort_index:
				lst_sort = sorted(lst_new, key=lambda lst: lst[sort_index]) # sorted_tuple_list_by_num_field(logic)
		except:
			lst_sort = sorted(lst_new, key=lambda lst: lst[0]) # sorted_tuple_list_by_first_field(error)

		dct_new = {k: v for ls in lst_sort for k, v in dct.items() if all((len(lst_new) > 0, ls[0].strip() == k.strip()))} # sorted_dict_by_tuple(list)

	elif all((lst_new,sort_index == -1)):
		dct_new = {ls[0]: ls[1] for ls in lst_sort if all((len(lst_new) > 0, ls))} # no_sorted_dict_by_tuple

	return dct_new # any_result


# cl_filter = compare_list([1,1,2,3,4,5]) # True # cl_filter = compare_list([]) # False
async def compare_list(lst: list = [], is_le: bool = False, is_ge: bool = False, is_e: bool = False, is_ne: bool = False) -> bool: #1

	try:
		assert lst and isinstance(lst, list), "Пустой список и другой формат списка @compare_list/lst" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Пустой список и другой формат списка @compare_list/lst")
		raise err
		return False

	# try:
		# if any((not lst, not isinstance(lst, list))):
			# return False # False(if_null)
	# except:
		# return False # if_error

	if is_le:
		return len(set(lst)) <= len(lst) # True(if_less_or_equal) # LE
	if is_ge:
		return len(lst) >= len(set(lst)) # True(if_great_or_equal) # GE
	if is_e:
		return len(lst) == len(set(lst)) # True(if_equal) # E
	if is_ne:
		return len(lst) != len(set(lst)) # True(if_not_equal) # NE

	return len(set(lst)) <= len(lst) # True(if_less_or_equal) # LE # default_result


async def calc_number_of_day(is_default: bool = True, day: int = 0, month: int = 0, year: int = 0, sleep_if: str = "", find_c3: int = 0, find_c4: int = 0) -> tuple:

	# calc_number_of_day
	if is_default:
		dt_calc = datetime.now() # day / month / year

		dt_str = ".".join([str(dt_calc.day), str(dt_calc.month), str(dt_calc.year)])
	elif not is_default:
		dt_str = ".".join([str(day), str(month), str(year)])

	if all((sleep_if, dt_str == sleep_if, is_default == False)):
		sleep(2)

	c2, c4 = 0, 0 # c1, c2, c3, c4 = 0, 0, 0, 0

	# 10.09.1994 # 33.6.31.4
	# 1.4.2023 # 12.3.32.5

	sm = []

	for ds in filter(lambda x: x, tuple(dt_str)):
		try:
			if int(ds) > 0:
				sm.append(int(ds))
		except:
			continue
	else: # is_no_break
		if len(sm) >= 0:
			is_day_calc = "Число дня получено!" if sm else "Число дня неизвестно!"
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
	elif c1 < 10: # all((c1 < 10, not calc1)):
		c2 = int(str(c1))
		# print(c2, 2)
		calc2 = True

	c3 = 33 - int(str(dt_str.split(".")[0])[1]) * 2 if dt_str.split(".")[0].startswith("0") else 33 - int(dt_str.split(".")[0])

	if c3 >= 10:
		calc3 = True
		c4 = int(str(c3)[0]) + int(str(c3)[1])
		while c4 > 10:
			c4 = int(str(c3)[0]) + int(str(c3)[1])
			# c3 = int(c4) # str -> int
			# print(c3, c4, 3)
	elif c3 < 10: # all((c3 < 10, not calc3)):
		c4 = int(str(c3))
		# print(c4, 4)
		calc4 = True

	if all((c3, find_c3 == c3)) and all((c4, find_c4 == c4)) and any((calc1, calc2, calc3, calc4)):
		print(c1, c2, c3, c4, dt_str, "from def")

	return (int(c1), int(c2), int(c3), int(c4), dt_str)


async def month_to_seasdays(month: int = 0, year: int = 0) -> tuple:

	try:
		assert 1 <= month <= 12, "Ошибка индекса месяца @month_to_seasdays/month" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Ошибка индекса месяца @month_to_seasdays/month")
		raise err
		return ("", 0)

	# if any((month < 0, month > 12)):
		# return ("", 0) # month_name, days_in_month

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
			days = 28 # short_month
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
			days = 30
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


async def date_to_week() -> dict:
	# Creating an dictionary with the return
	# value as keys and the day as the value
	# This is used to retrieve the day of the
	# week using the return value of the
	# isoweekday() function
	weekdays = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}

	try:
		# Getting current date using today()
		# function of the datetime class
		todays_date = datetime.today()

		try:
			mts = await month_to_seasdays(month=todays_date.month, year=todays_date.year)
		except:
			mts = ("", 0)

		try:
			cnod = await calc_number_of_day(day=todays_date.day, month=todays_date.month, year=todays_date.year)
		except:
			cnod = (0,0,0,0, str(todays_date))

		# Using the isoweekday() function to
		# retrieve the day of the given date
		day = todays_date.isoweekday()
		# print("The date", todays_date, "falls on", weekdays[day])
	except:
		return {"date": "unknown", "weekday": "unknown", "season(days)": "unknown", "number_of_day": "unknown"} # false_date
	else:
		return {"date": todays_date, "weekday": weekdays[day], "season(days)": str(mts), "number_of_day": str(cnod)} # true_date / season(days_in_month)


# gcd_list = gcd_from_numbers([i for i in range(20) if i]) # filter_integers_from_to
async def gcd_from_numbers(lst: list = []) -> list:

	try:
		assert lst, "Пустой список @gcd_from_numbers/lst" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Пустой список @gcd_from_numbers/lst")
		raise err
		return []

	equal_mod: list = []

	tmp = [l for l in filter(lambda x: x, tuple(lst))] # skip_zero_by_filter
	if all((tmp, len(tmp) <= len(lst))):
		lst = tmp # skip_zero

	# wait_to_found_divmod
	if all((min(lst) > 0, min(lst) < max(lst))): # convert_to_generator(refactor)
		for i in range(min(lst), max(lst) + 1):
			for l1 in range(len(lst) - 1):
				for l2 in range(l1 + 1, len(lst)):
					if all((l1 != l2, i > 1)) and all((lst[l1] % i == 0, lst[l2] % i == 0, lst[l1] < lst[l2])):
						equal_mod.append({"l1": lst[l1], "l2": lst[l2], "i": i})

	return equal_mod # result(divmod_in_list/null_list)


def ff_to_days(ff: str = "", period: int = 30, is_dir: bool = False, is_less: bool = True, is_any: bool = False) -> tuple: # count_is_after # default(month)

	try:
		assert os.path.exists(ff), "Файл не существует @ff_to_days/ff" # is_assert(debug)
	except AssertionError: # as err: # stay_or_hide
		logging.warning("Файл не существует @ff_to_days/ff")
		# raise err
		return ("", -1, None)

	# if not ff or not os.path.exists(ff):
		# return ("", -1, None) # null_filename / bad_status / unknown_type

	if is_any:
		is_less = False

	if is_less:
		is_any = False

	try:
		is_dir = (not os.path.isfile(ff))
	except:
		is_dir = False

	try:
		today = datetime.today()  # datetime
		fdate = os.path.getmtime(ff)  # unixdate(file/folder)
		ndate = datetime.fromtimestamp(fdate)  # datetime
	except:
		return ("", -1, is_dir) # null_filename / bad_status / is_dir
	else:
		try:
			assert period >= 0, "Ошибка периода @ff_to_days/period" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Ошибка периода @ff_to_days/%s" % ff)
			raise err
			return ("", -1, is_dir) # default_result / bad_status / is_dir
		else:
			if period >= 0:
				if (is_less and abs(today - ndate).days <= period or not is_less and abs(today - ndate).days >= period) and is_any == False:
					return (ff, abs(today - ndate).days, is_dir) # (file/folder)name / count_days / is_dir
				elif all((is_any == True, abs(today - ndate).days >= 0, period >= 0)):
					return (ff, abs(today - ndate).days, is_dir) # (file/folder)name / count_days / is_dir
			# elif period < 0:
				# return ("", -1, is_dir) # default_result / bad_status / is_dir

	return ("", -1, is_dir) # default_result / bad_status / is_dir


top_folder: str = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\cur_top.lst"
top_folder2: str = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\curr.lst" # eng(+rus).lst_to_update

all_list: list = []
lang_list: list = []

# generate_paths_for_manual_run
async def folders_from_path(is_rus: bool = False, template: list = [], need_clean: bool = False): # -> list:

	global all_list

	folder_scan: list = []
	folder_scan_full: list = []
	folder_desc_files: list = []

	# new

	if is_rus:
		mydir = "d:\\multimedia\\video\\serials_europe\\"
		# efile = ".\\top100_rus.lst" # generate_to_current_folder
		mydir2 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\top100_rus.lst" # folder -> file
		mydir3 = "d:\\multimedia\\video\\serials_europe\\top100_rus.lst" # folder -> file
		mydir4 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\rus.lst" # folder -> file
	elif not is_rus:
		mydir = "d:\\multimedia\\video\\serials_conv\\"
		# efile = ".\\top100_eng.lst" # generate_to_current_folder
		mydir2 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\top100_eng.lst" # folder -> file
		mydir3 = "d:\\multimedia\\video\\serials_conv\\top100_eng.lst" # folder -> file
		mydir4 = "c:\\downloads\\soft\\for_usb_ffmpeg(projects)\\eng.lst" # folder -> file

	rus_regex = re.compile("_Rus", re.M)

	# full_paths # video_regex

	found_list: list = []
	full_list: list = []

	# if_more_one_file_then_save # debug
	try:
		folder_scan_full = list(set(["".join([mydir, df]) for df in os.listdir(mydir) if os.path.exists("".join([mydir, df]))])) # os.listdir("".join([mydir, df])
	except:
		folder_scan_full = []
	else:
		if folder_scan_full:
			folder_scan_full.sort(reverse=False) # sort_by_abc

			is_found: bool = False
			is_not_found: bool = False
			is_two_desc: bool = False

			try:
				with open(desc_base, encoding="utf-8") as dbf:
					desc_dict = json.load(dbf)
			except:
				desc_dict = {}

				with open(desc_base, "w", encoding="utf-8") as dbf:
					json.dump(desc_dict, dbf, ensure_ascii=False, indent=2, sort_keys=True)

			try:
				with open(desc_base_temp, encoding="utf=8") as dbtf:
					desc_dict2 = json.load(dbtf)
			except:
				desc_dict2 = {}

			desc_dict_filter: dict = {}

			# clear_old_desc
			try:
				desc_dict_filter = {k.strip(): v.replace(";(", ";").replace(");", ";").strip() for k, v in desc_dict.items() if
									v != v.replace(";(", ";").replace(");", ";")}
			except:
				desc_dict_filter = {}
			else:
				if all((desc_dict_filter, len(desc_dict_filter) <= len(desc_dict))): # desc_dict

					if len(desc_dict_filter) != len(desc_dict):
						print(Style.BRIGHT + Fore.CYANimport  + "будет обновлено",
							Style.BRIGHT + Fore.WHITE + "%d",
							Style.BRIGHT + Fore.YELLOW + "записей" % abs(len(desc_dict_filter) - len(desc_dict)))

					desc_dict.update(desc_dict_filter)

			# folders_sym: list = []
			# folders_sym = sorted(list(set([fsf[0] for fsf in folder_scan_full if fsf[0]])), reverse=False)

			# true_sym = re.compile(r"([^A-ZА-Я\d\-])", re.I); # sample = "Hello world"; print(list(set(true_sym.findall(sample)))) # need_skip

			for fsf in filter(lambda x: x, tuple(folder_scan_full)):

				try:
					list_files = os.listdir(fsf)
				except:
					list_files = []
				else:
					is_found = (len(list(filter(lambda x: "mp4" in x, tuple(list_files)))) > 0 and len(list(filter(lambda x: "txt" in x, tuple(list_files)))) > 0) # desc(1) / files(1)
					is_not_found = (len(list(filter(lambda x: "mp4" in x, tuple(list_files)))) == 0 and len(list(filter(lambda x: "txt" in x, tuple(list_files)))) == 0) # desc(0) / files(0)
					is_two_desc = (len(list(filter(lambda x: "mp4" in x, tuple(list_files)))) >= 0 and len(list(filter(lambda x: "txt" in x, tuple(list_files)))) == 2) # desc(2) / files(0/1)

				# path_to_description
				try:
					full_list = ["\\".join([fsf, ol]).strip() for ol in filter(lambda x: "txt" in x, tuple(list_files))] #  if os.path.exists("\\".join([fsf, ol]).strip())
				except:
					full_list = []

				# descriptions
				if len(list(filter(lambda x: "txt" in x, tuple(list_files)))) == 1 and full_list:

					# "﻿10 причин моей ненависти": "﻿10 причин моей ненависти;(10 Things I Hate About You);7 Jul 2009"
					# "Адаптация": "Адаптация;6 Feb 2017"

					# 911 (9-1-1) 3 Jan 2018 # 911 (9-1-1) 3.01.2018 # one_info_different_date_types

					desc_regex = re.compile(r"(.*)\s\((.*)\)\s(?:([\d+]{1,2}\s[A-Za-z]{3}\s[\d+]{4}|[\d+]{1,2}\.[\d+]{1,2}\.[\d+]{4}))", re.I) # rus / eng / date
					# se_or_year = re.compile(r"(?:([\d+]{2}s[\d+]e|\([\d+]{4}\)))", re.I)

					for fl in filter(lambda x: x, tuple(full_list)):

						if fl.lower().endswith("txt"):

							dlist: list = []

							try:
								with open(fl, encoding="utf-8") as df:
									dlist = df.readlines()
							except:
								dlist = []

							try:
								if all((dlist, dlist[0])): # add_some_desc(lines/line[1])

									row_data = str(dlist[0]).strip() # first_line

									# if_not_utf-8(is_ansi) # debug
									if all((not row_data[0].isnumeric(), not row_data[0].isalpha())):
										row_data = row_data.replace("\ufeff", "")

									# ("Медленные лошади (Slow Horses) 1 Apr 2022")
									# {"Медленные лошади": "Slow Horses;1 Apr 2022"}

									# ("Алиби () 18 Oct 2021")
									# {'Алиби': '18 Oct 2021'}

									try:
										parse_desc = desc_regex.findall(row_data)
									except:
										parse_desc = []

									# yes_description # desc(1)
									if parse_desc:
										try:
											desc = ";".join(parse_desc[0])

											if any((desc.split(";")[0][0].isnumeric(), desc.split(";")[0][0].isalpha())):
												desc = desc.replace(";;", ";") # clear_double(if_rus)
												desc = desc.replace(";(", ";") # clear_first_quote(is_rus)
												desc = desc.replace(");", ";") # clear_second_quote(is_rus)
										except:
											desc = ""
										else:
											desc_dict[desc.split(";")[0].strip()] = ";".join(desc.split(";")[1:])

										# print(Style.BRIGHT + Fore.CYAN + "Info: %s" % str(parse_desc)) # original_desc
										# print(Style.BRIGHT + Fore.CYAN + "%s" % desc_dict[parse_desc[0].strip()]) # "eng" / date
										# print(Style.BRIGHT + Fore.CYAN + "%s" % ";".join(parse_desc[0])) # string_desc
							except: # skip_desc
								continue

				# '''

				# config = {"ff": None, "period": 30, "is_dir": False} # **config # fsf(default) -> None(debug)

				fold_and_date: list = []

				dt = datetime.now()

				days = 366 if dt.year % 4 == 0 else 365 # by_year

				try:
					ftd = ff_to_days(ff=fsf, period=days, is_dir=False, is_less=False, is_any=True) # period=30(is_month) # period=days(is_year) # is_all
				except:
					ftd = (None, ) # if_error2(None)

				if len(ftd) > 1 and os.path.exists(ftd[0]) and ftd[0] != None: # ftd[1] >= 0:
					try:
						folder_or_file = "Папка: %s" % fsf if ftd[-1] else "Файл: %s " % ftd[0]
						days_ago = "%d месяцев назад" % (ftd[1] // 30) if ftd[1] // 30 > 0 else "%d дней назад" % ftd[1]
					except:
						folder_or_file = "Папка: %s" % fsf if ftd[-1] else "Файл: %s" % ftd[0]
						print(Style.BRIGHT + Fore.YELLOW + "%s [%s]" % (folder_or_file, str(datetime.now()))) # folder(file) / datetime
					else:
						fold_and_date.append((folder_or_file, days_ago, str(datetime.now())))
						# print(Style.BRIGHT + Fore.WHITE + "%s %s [%s]" % (folder_or_file, days_ago, str(datetime.now()))) # folder(file) / days_ago / datetime

				fold_and_date_sorted: list = []

				fold_and_date_sorted = sorted(fold_and_date, key=lambda fold_and_date: fold_and_date[1])

				fad_dict = {fads[0]: fads[1] for fads in fold_and_date_sorted for fad in fold_and_date if fads[0] == fad[0]} # type / days_ago

				for k, v in fad_dict.items():
					if not fad_dict:
						break

					if any((not k, not v)):
						continue

					print(Style.BRIGHT + Fore.WHITE + "%s %s" % (k, v)) # folder(file) / days_ago

				# find_folders_by_month(by_time) # is_all_days
				if all((len(ftd) > 1, ftd[0] != None, ftd[1] >= 0)): # period=30 -> period=days
					if is_found: # desc(0/1), files(1) # some_found

						if template:
							tmp = [lf.strip() for t in template for lf in list_files if all((t, lf, lf.lower().endswith(t.lower())))]

							if tmp: # add_with_template
								folder_desc_files.append(fsf)

						elif not template:
							folder_desc_files.append(fsf) # add_without_template_by_count

						found_list.append(fsf.split("\\")[-1]) # file_or_folder

						# folder_desc_files # parse_soundtracks_from_filename

						# @is_debug
						# '''
						desc_list: list = []
						parse_list: list = []
						# parse_filename: list = []

						def http_trace_to_soundtrack_parse(line: str = ""):

							# global parse_filename

							no_prot_ext: str = ""

							try:
								assert line, "Пустая строка @http_trace_to_soundtrack_parse/line"
							except AssertionError as err:
								logging.warning("Пустая строка @http_trace_to_soundtrack_parse/line")
								raise err
								return no_prot_ext

							# if not line:
								# return no_prot_ext

							parse_regex = re.compile(r"http(.*)\.mp4", re.I)

							filename = line # "http://data11-cdn.datalock.ru/fi2lm/7d2b2f94011f33cd73b7dbf603374c89/7f_The.Hundred.S07E11.720p.rus.LostFilm.TV.a1.14.08.20.mp4"
							try:
								no_prot_ext = parse_regex.findall(filename)[0] # ://data11-cdn.datalock.ru/fi2lm/7d2b2f94011f33cd73b7dbf603374c89/7f_The.Hundred.S07E11.720p.rus.LostFilm.TV.a1.14.08.20
							except:
								no_prot_ext = ""

							if all((no_prot_ext, no_prot_ext.count("/") > 0)):
								no_prot_ext = no_prot_ext.split("/")[-1].replace("7f_", "").replace(".", "_").strip() # The_Hundred_S07E11_720p_rus_LostFilm_TV_a1_14_08_20

								# parse_filename.append(no_prot_ext)

								return no_prot_ext
							else:
								return no_prot_ext

						dt = datetime.now()

						is_backup: bool = False
						is_backup = all((dt.hour % 3 == 0, dt.minute <= 15)) # every_3_hour's_between_in_15min # is_default(?)

						desc_list = [ld.strip() for ld in os.listdir(fsf) if ld.lower().endswith(".txt")]

						if all((len(desc_list) == 1, is_backup)):
							try:
								with open("\\".join([fsf, desc_list[-1]]), encoding="utf-8") as fdf:
									parse_list = fdf.readlines()
							except:
								parse_list = []

							# if_look_like_download_path_change_soundtracks # save_to(soundtrack_base)
							try:
								tmp = ["\\".join(["c:\\downloads\\combine\\original\\tvseries", ".".join([http_trace_to_soundtrack_parse(pl), "mp4"])]) for pl in filter(lambda x: x, tuple(parse_list)) if http_trace_to_soundtrack_parse(pl)] # http(s)...mp4

								assert tmp, "Пустой список файлов @folders_from_path/tmp" # is_assert(debug)
							except AssertionError: # as err:
								tmp = []
								logging.warning("Пустой список файлов @folders_from_path/tmp")
								# raise err
							finally:
								if tmp:
									print("%d downloaded projects" % len(tmp)) #print(";".join(tmp)) #; print() # need_another_comment
									sleep(0.5)

							st_list: list = []

							try:
								with open(files_base["stracks"], encoding="utf-8") as sf:
									st_list = sf.readlines()
							except:
								st_list = []

							try:
								with open(soundtrack_base, encoding="utf-8") as sbf:
									soundtrack_dict = json.load(sbf)
							except: # IOError
								soundtrack_dict = {}

							is_error = False

							# x[0].isalpha() -> x[0] == x[0].upper() # pass_1_of_2
							try:
								soundtrack_filter = {t.strip(): sl.strip() for sl in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(st_list)) for t in tmp if
														any((sl.lower().strip() in t.lower().strip(), sl.strip() in t)) and tmp} # t.replace(sl, "*" * len(sl)).strip() # descrypt/debug
								# soundtrack_filter = {t.replace(sl, "*" * len(sl)).strip(): sl.strip() for sl in filter(lambda x: any((x[0].isalpha(), x[0].isnumeric())), tuple(st_list)) for t in tmp if
								# any((sl.lower().strip() in t.lower().strip(), sl.strip() in t))} # t.replace(sl, "*" * len(sl)).strip() # debug/decrypt/backup
							except:
								soundtrack_filter = {}
								is_error = True
							else:
								is_error = False

							soundtrack_filter_top = {}

							# update_havent_soundtracks(filter) # pass_2_of_2
							soundtrack_filter_top = {k: v for k, v in soundtrack_filter.items() if all((k, not k in [*soundtrack_dict]))} # if_new_soundtrack(filter_current_files)

							if any((not soundtrack_filter, not soundtrack_filter_top)): # if_some_null
								continue # skip_desc_if_no_soundtrack

							if soundtrack_filter_top:
								soundtrack_filter = {}
								soundtrack_filter.update(soundtrack_filter_top)

							if all((soundtrack_filter_top, len(soundtrack_dict) >= 0, is_error == False)): # it_was_new(else_skip) # some_soundtracks(or_newbase) # soundtrack_filter
								soundtrack_dict.update(soundtrack_filter) # update_base_from_filter

								# soundtrack_tbase(decrypt/debug/backup) -> soundtrack_base(original) # file
								# soundtrack_filter(decrypt/debug) # soundtrack_dict(original/backup) # json

								# filter(lambda x: lst.count(x) != list(set(lst)).count(x), tuple(lst)) # search_moda

								# soundtrack_dict -> soundtrack_filter

								try:
									soundtrack_count = [(v.strip(), list(soundtrack_dict.values()).count(v.strip)) for k, v in soundtrack_dict.items() if
												sl.lower().strip() in k.lower().strip()]
								except:
									soundtrack_count = []
								else:
									if soundtrack_count:

										soundtrack_count_sorted = sorted(soundtrack_count, key=lambda soundtrack_count: soundtrack_count[1]) # sorted_by_value
										soundtrack_count = [(scs[0], int(scs[1])) for scs in soundtrack_count_sorted if isinstance(soundtrack_count_sorted, tuple)]

										# print(Style.BRIGHT + Fore.CYAN + "debug soundtrack_count[low] \'%s\'" % str(soundtrack_count)) # is_color
										print(Style.BRIGHT + Fore.CYAN + "debug soundtrack_count[low] \'%d soundtrack count\'" % len(soundtrack_count)) # is_color

								try:
									soundtrack_count = {v.strip(): str(list(soundtrack_dict.values()).count(v.strip())) for k, v in
												soundtrack_dict.items()}
								except:
									soundtrack_count = {}
								else:
									if soundtrack_count:

										soundtrack_count_list = [(k, int(v)) for k, v in soundtrack_count.items()]
										soundtrack_count_sorted = sorted(soundtrack_count_list, key=lambda soundtrack_count_list: soundtrack_count_list[1]) # sorted_by_value
										stc = {scs[0]: scs[1] for scs in soundtrack_count_sorted} # sorted_json
										soundtrack_count = stc if stc else {}

										print(Style.BRIGHT + Fore.WHITE + "debug soundtrack_count[combine] \'%s\'" % str(soundtrack_count)) # is_color
										# print(Style.BRIGHT + Fore.WHITE + "debug soundtrack_count[combine] \'%d soundtrack count\'" % len(soundtrack_count)) # is_color

										try:
											soundtrack_count_new = {k: int(v) for k, v in soundtrack_count.items()}
											s = sum(list(soundtrack_count_new.values()));
											l = len(soundtrack_count_new);
											a = s / l
											class_dict = {k: round((v / s) * 100, 2) for k, v in soundtrack_count_new.items() if v - a > 0}  # 0..100%(popular_classify)
										except BaseException as e:
											class_dict = {}
											print(Style.BRIGHT + Fore.RED + "debug soundtrack_count[error] \'%s %s\'" % (str(None), str(e)))
											# write_log("debug soundtrack_count[error]", "%s %s" % (str(None), str(e)), is_error=True) # is_color
										else:
											try:
												sort_class = {s:v for s in sorted(class_dict, key=class_dict.get, reverse=False) for k, v in class_dict.items() if all((s,k,v, s == k))}
											except:
												sort_class = {}

											if all((sort_class, len(sort_class) <= len(class_dict))): # is_sorted_dict # less_or_equal
												class_dict = sort_class

											class_status = str(class_dict) if class_dict else ""
											if class_status:
												print(Style.BRIGHT + Fore.CYAN + "debug soundtrack_count[popular] \'%s\'" % class_status) # is_color
												# write_log("debug soundtrack_count[popular]", "%s" % class_status)

								with open(soundtrack_base, "w", encoding="utf-8") as sbf:
									json.dump(soundtrack_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True) # is(decrypt/debug)

							# x[0].isalpha() -> x[0] == x[0].upper()

							with open(files_base["soundtrack"], "a", encoding="utf-8") as fbsf:
								fbsf.writelines("%s\n" % t.strip() for t in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(tmp)))

						# '''

						# if all((fsf, fsf[-1])):
							# print(Style.BRIGHT + Fore.WHITE + "Описание и файлы найдены в папке", Style.BRIGHT + Fore.CYAN + "%s" % fsf, end = "\n") # is_color's
							# write_log("debug fsf[is_found][ok]", "%s" % fsf) # is_found

					if is_not_found: # desc(0), files(0) # create_null(any_time)
						try:
							if not os.path.exists("\\".join([fsf, "00s00e.txt"])):
								open("\\".join([fsf, "00s00e.txt"]), "w", encoding="utf-8").close()
						except:
							pass # nothing_to_do_if_error # is_continue
						else:
							print(Style.BRIGHT + Fore.CYAN + "Описание и файлы не найдены в папке", Style.BRIGHT + Fore.WHITE + "%s" % fsf, end = "\n") # is_color's
							# write_log("debug fsf[is_not_found][ok]", "%s" % fsf) # is_create

					if is_two_desc: # desc(2), files(0/1) # delete_null(any_time)
						try:
							if os.path.exists("\\".join([fsf, "00s00e.txt"])):
								os.remove("\\".join([fsf, "00s00e.txt"]))
						except:
							pass # nothing_to_do_if_error # is_continue
						else:
							print(Style.BRIGHT + Fore.YELLOW + "Удаляю лишнее описание в папке", Style.BRIGHT + Fore.WHITE + "%s" % fsf, end = "\n") # is_color's
							# write_log("debug fsf[is_two_desc_found][ok]", "%s" % fsf) # is_delete

			if desc_dict: # some_data # data

				if desc_dict2:
					desc_dict.update(desc_dict2)

					if all((desc_dict2, set([*desc_dict2]) & set([*desc_dict]))): # newbie_in_current_desc_by_json
						with open(desc_base_temp, "w", encoding="utf-8") as dbtf:
							json.dump({}, dbtf, ensure_ascii=False, indent=2, sort_keys=True) # clear_manual_desc_if_some_added

						if os.path.exists(desc_base_temp):
							os.remove(desc_base_temp) # delete_after_update

				with open(desc_base, "w", encoding="utf-8") as dbf:
					json.dump(desc_dict, dbf, ensure_ascii=False, indent=2, sort_keys=True)

			# x[0].isalpha() -> x[0] == x[0].upper()

			with open(mydir4, "w", encoding="utf-8") as mf: # resave # debug # found_by_period
				mf.writelines("%s\n" % fs.strip() for fs in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(found_list))) # int/str # is_all(lang)

	# only_folder_names

	ccmd = r'cmd /c dir /r/b/ad/od- *.*'

	lang_list: list = []
	folder_scan: list = []

	os.chdir(mydir)

	cmd = os.system("%s -> %s" % (ccmd, mydir3)) # is_list_in_current_folder # 0 - ok, 1 - error

	if cmd == 0:
		sleep(30) # if_ok_wait_30ms

	try:
		with open(mydir3) as mdf:
			lang_list = mdf.readlines()
	except:
		lang_list = []
	else:
		if len(lang_list) > 0:
			# is_languages
			folder_scan = [rus_regex.sub("", ll).strip() if rus_regex.sub("", ll) != ll else ll for ll in filter(lambda x: x, tuple(lang_list))] # debug
			folder_scan = folder_scan[::-1] # reverse(newer_to_oldest)
			# folder_scan = folder_scan[0:1000] if len(folder_scan) > 1000 else folder_scan # limit_folders_for_scan

			# x[0].isalpha() -> x[0] == x[0].upper()

			with open(mydir2, "w", encoding="utf-8") as mf: # resave # debug # top_file_by_lang
				mf.writelines("%s\n" % fs.strip() for fs in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(folder_scan))) # int/str # is_by_count(top)

	try:
		if os.path.exists(mydir3) and folder_scan:
			os.remove(mydir3)
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "%s" % str(e))

	# if folder_scan:
		# print(folder_scan)

	try:
		all_list += folder_scan # is_skip_await
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
	task1 = asyncio.create_task(folders_from_path(is_rus = True), name="folders_from_path_rus") # old
	task2 = asyncio.create_task(folders_from_path(is_rus = False), name="folders_from_path_no_rus") # old
	# task1 = tg.create_task(folders_from_path(is_rus = True), name="folders_from_path_rus")
	# task2 = tg.create_task(folders_from_path(is_rus = False), name="folders_from_path_no_rus")

	ffp.append(task1) # old
	ffp.append(task2) # old

	await asyncio.gather(*ffp) # ok_if_runned / debug(is_no_return) # old

asyncio.run(ffp_generate())
# '''

# x[0].isalpha() -> x[0] == x[0].upper()

# current_list(is_full) # is_ok
if all_list:
	try:
		tmp = list(set([al.strip() for al in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(all_list))])) # unique
	except:
		tmp = [] # null_if_error

	all_list = tmp if tmp else []

# 1684 [None, None] Текущий список папок, общий список папок # current_list_length / is_full_list / status's
all_list_status = "Общий список в %d папках" % len(all_list) if all_list else "Общего списка в папках не найдено" # str(debug) -> int(count)

print(Style.BRIGHT + Fore.YELLOW + "%d" % len(all_list), Style.BRIGHT + Fore.WHITE + "%s" % all_list_status)

if not all_list:
	exit() # if_null_exit

abc_or_num_regex = re.compile(r"^[A-Z0-9].*", re.I)

# x[0].isalpha() -> x[0] == x[0].upper()

try:
	# temp = list(set([al.strip() for al in all_list if abc_or_num_regex.findall(al)])) # filter_by_regex
	temp = list(set([al.strip() for al in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(all_list))])) # int/str
except:
	temp = []

if all((temp, len(temp) <= len(all_list))):
	all_list = sorted(temp, reverse=False) # sort_by_abc
	# all_list = sorted(temp, key=len, reverse=False) # sort_by_key

os.chdir(r"c:\\downloads\\mytemp") # is_change_drive_and_folder

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
	tff.writelines("%s\n" % al.strip() for al in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(all_list))) # int/str # is_top

top_list: list = []

# top100(rus+eng)_load # @cur_top.lst # original
with open(top_folder, encoding="utf-8") as tff:
	top_list = tff.readlines()

filter_top_list = [tl.strip() for tl in filter(lambda x: x, tuple(top_list))] # shorts

# load_meta_base(fitler) #1
try:
	with open(some_base, encoding="utf-8") as sbf:
		somebase_dict = json.load(sbf)
except:
	somebase_dict = {}

	with open(some_base, "w", encoding="utf-8") as sbf:
		json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

if all((filter_top_list, len(somebase_dict) >= 0)):

	# old # only_folders / no_backup # is_count_equal_template
	filter_top_by_folders =list(set([ftl.strip() for ftl in filter_top_list for k, v in somebase_dict.items() if
								  len(ftl.strip()) > 0 and k.split("\\")[-1].startswith(ftl)]))

	if not filter_top_by_folders: # stay_filter_short
		filter_top_by_folders =list(set([ftl.strip() for ftl in filter_top_list if len(ftl.strip()) > 0]))

	# filter_for_new_backup = list(set([k.strip() for ftl in filter_top_list for k, v in somebase_dict.items() if len(ftl.strip()) > 0 and k.split("\\")[-1].startswith(ftl)]))

	filter_get1000 = filter_top_by_folders[0:1000] if len(filter_top_by_folders) > 1000 else filter_top_by_folders # only_1000(optimal) # top_1000
	if all((filter_get1000, len(filter_get1000) <= len(filter_top_by_folders))):
		filter_top_by_folders = filter_get1000

	# new # no_folders / only_backup # is_count_equal_template # default(30_days)
	filter_for_new_backup = list(set([k.strip() for k, v in somebase_dict.items() if ff_to_days(ff = k, period = 0, is_dir=False, is_less=False, is_any=True)[0] != None])) # is_all

	filter_get1000 = filter_for_new_backup[0:1000] if len(filter_for_new_backup) > 1000 else filter_for_new_backup # only_1000(for_fast) # top_1000
	if all((filter_get1000, len(filter_get1000) <= len(filter_for_new_backup))):
		filter_for_new_backup = filter_get1000

	# x[0].isaplha() -> x[0] == x[0].upper()

	# top100(rus+eng)_by_template # pass_2_of_4 # pass # @cur_top.lst
	if filter_top_by_folders:
		with open(top_folder, "w", encoding="utf-8") as tff:
			tff.writelines("%s\n" % ftbf.strip() for ftbf in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(filter_top_by_folders))) # int/str # is_top

	if os.path.exists(top_folder): # update_top_file
		# top100(rus+eng)_copy # pass_3_of_4 # pass # cur_top.lst -> curr.lst
		copy(top_folder, top_folder2)

	# ff_to_days(ff=fsf, period=30, is_dir=False, is_less=True, is_any=False)[0] != None # top_folder2 # curr.lst # date_modified_by_less_days

	# check_last_backup

	clb: list = []

	# try_load_last_backup
	try:
		with open(files_base["backup"], encoding="utf-8") as bjf:
			clb = bjf.readlines()
	except:
		clb = []

	# put_files_by_top_and_recovery # pass_4_of_4 # pass # @current.lst
	if all((filter_for_new_backup, not clb)): # if_file_null_try_update # save_by_key(is_short)
		with open(files_base["backup"], "w", encoding="utf-8") as bjf: # try_save_new_backup
			bjf.writelines("%s\n" % ffnb.strip() for ffnb in filter(lambda x: x, tuple(filter_for_new_backup))) # not_null(current_jobs)

# if all((rus_list, eng_list, all_list)): # hide_counters
	# print("%d russian" % len(rus_list), "%d english" % len(eng_list), "%d total" % len(all_list)) # is_color

async def memory_usage_psutil(proc_id) -> any:
	# return the memory usage in percentage like top

	try:
		process = psutil.Process(proc_id)  # os.getpid()
		mem = process.memory_percent()

		assert mem, "Ошибка сохранения значения памяти @memory_usage_psutil/mem" # is_assert(debug)
	except AssertionError as err:
		mem = 0
		logging.warning("Ошибка сохранения значения памяти @memory_usage_psutil/mem")
		raise err

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
			mem: float = asyncio.run(memory_usage_psutil(int(eachProcess.pid)))  # print(eachProcess.pid)

			if int(mem) > 80:  # "80"->85
				print(eachProcess.name(), end="\n")

				if all((not eachProcess.name() in big_process, not eachProcess.name() in skip_process)):
					big_process.append(eachProcess.name())

					if not eachProcess.pid in pid_process:
						pid_process.append(eachProcess.pid)

				with open("c:\\downloads\\mytemp\\overload.csv", "a") as ocf:
					ocf.write(";".join([str(eachProcess.pid), str(eachProcess.name())]) + "\n")

		except:
			mem: float = 0
	else: # is_no_break
		print("Процессы проанализированы")

	# exit

	if any((big_process, pid_process)):
		print(big_process, pid_process, end="\n")

# logging(start)
log_base: str = "c:\\downloads\\mytemp\\video_resize.json"  # unique_logging(test)
log_print: str = "c:\\downloads\\mytemp\\resize.log"

open(log_print, "w", encoding="utf-8").close()

# delete_last_days_log
new_dict: dict = {}

try:
	with open(log_base, encoding="utf-8") as nlf:
		log_dict = json.load(nlf)
except: # IOError
	log_dict = {}

	with open(log_base, "w", encoding="utf-8") as nlf:
		json.dump(log_dict, nlf, ensure_ascii=False, indent=2)
else:
	if log_dict:
		new_dict = log_dict

		try:
			today_check = "-".join([str(dt.year), str(dt.month), str(dt.day)])  # full_paramaters(string)
		except:
			today_check = str(datetime.today()).split(" ")[0]  # date_fitler(string)

		new_dict = {k: v for k, v in new_dict.items() if all((today_check in v, today_check, v))}

	if all((new_dict, len(new_dict) <= len(log_dict))):  # filter(by_data/by_length) + some_data
		# log_dict = new_dict # filter_by_dates_other_clear
		log_dict.update(new_dict)  # update

		with open(log_base, "w", encoding="utf-8") as nlf:
			json.dump(log_dict, nlf, ensure_ascii=False, indent=2)

some_dict: dict = {}

try:
	with open(log_base, encoding="utf-8") as lbf:
		log_dict = json.load(lbf)
except: # IOError
	log_dict = {}

	with open(log_base, "w", encoding="utf-8") as lbf:
		json.dump(log_dict, lbf, ensure_ascii=False, indent=2)

def write_log(desc: str = "", txt: str = "", is_error: bool = False, is_logging: bool = False):  # event_log(is_all)

	try:
		assert desc and txt, "Пустое описание или комментарий @write_log/desc/txt" # is_assert(debug)
	except AssertionError: # as err:
		logging.warning("Пустое описание или комментарий @write_log/%s/%s" % (desc, txt))
		# raise err # have_null
		return

	# if any((not desc, not txt)):
		# return

	global log_dict

	try:
		with open(log_base, encoding="utf-8") as lbf:
			log_dict = json.load(lbf)
	except: # IOError
		log_dict = {}

		with open(log_base, "w", encoding="utf-8") as lbf:
			json.dump(log_dict, lbf, ensure_ascii=False, indent=2)
	finally:
		if all((desc, txt)):
			if any(("error" in txt.lower().strip(), "error" in desc.lower().strip(), is_error == True)):
				logging.error(txt.strip())  # logging_with_error
			if all((txt.strip(), is_logging == True, is_error != True)):
				logging.info(";".join([desc.strip(), txt.strip()])) # logging
			# if str(datetime.today()).split(" ")[0] in txt.lower().strip(): # only_current_date
				# logging.info(txt.strip())  # logging_with_info

			log_dict[desc.strip()] = txt.strip()

		if log_dict:
			with open(log_base, "w", encoding="utf-8") as lbf:
				json.dump(log_dict, lbf, ensure_ascii=False, indent=2, sort_keys=True)

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
				assert len(lp.strip()) > 0
			except AssertionError as err:
				raise err
				continue

			# if len(lp.strip()) == 0:
				# continue

			if not lp in check_log:
				check_log.add(lp)

		if all((check_log, len(check_log) <= len(lprint))):
			lprint = sorted(list(check_log), reverse=False)  # without_abc(set->list) # key=len # debug_by_key

		with open(log_print, "w", encoding="utf-8") as lpf:
			lpf.writelines("%s\n" % lp.strip() for lp in filter(lambda x: x, tuple(lprint))) # not_null(logging)


# check_function_by_error(logging)
def log_error(f):
	def inner(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except BaseException as e:
			write_log("debug error", "%s" % str(e), is_error=True)
			# logging.error("%s" % str(e))
			# raise e

	return inner


async def mp4_to_m3u8(filename: str = "", is_run: bool = False, is_stay: bool = False) -> tuple:

	try:
		assert os.path.exists(filename), "Файл отсутствует @mp4_to_m3u8/filename" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Файл отсутствует @mp4_to_m3u8/%s" % filename)
		raise err
		return (False, "", "no_run")

	# if not filename or not os.path.exists(filename):
		# return (False, "", "no_run")

	try:
		folder = "\\".join(filename.split("\\")[0:-1]).strip()
	except:
		folder = ""

	try:
		fname = filename.split("\\")[-1]
	except:
		fname = ""

	try:
		if not os.path.exists(path_for_segments):
			os.mkdir(path_for_segments)
	except:
		os.system("cmd /c mkdir \"%s\"" % path_for_segments) # create_null_m3u8_by_job

	try:
		m3u8_file = "".join([path_for_segments, ".".join([fname.split(".")[0], "m3u8"])])
	except:
		m3u8_file = ""
	else:
		if not os.path.exists(m3u8_file) and m3u8_file:
			os.system("cmd /c copy nul \"%s\"" % m3u8_file) # create_null_m3u8_by_job

	cmd: str = ""

	# %filename%.m3u8 (main_m3u8_playlist) # %filename%%index%.ts (parts_count)


	async def seg_and_playlist_counts(fname: str = "") -> tuple:

		m3u8_regex = re.compile(r"^(%s)(.*)(?:(m3u8|ts))$" % fname, re.I) # "filename" / is_index / "m3u8(ts)" # IgnoreCase

		some_files = [m3u8_regex.findall(lf) for lf in os.listdir(path_for_segments) if m3u8_regex.findall(lf)] # save_found_tuple_to_list

		playlist_count: int = 0
		index_count: int = 0

		for sf in some_files:
			if len(sf) == 3:
				index_count += 1
			elif len(sf) == 2:
				playlist_count += 1
			else: # <2 # >3
				continue

			# print(sf) # (filename, is_index, is_ext) # (filename, is_ext)

		return (index_count, playlist_count)

	if all((folder, fname, m3u8_file)):
		# ffmpeg -i filename.mp4 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls filename.m3u8 # ffmpeg_script
		cmd = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) +  " -hide_banner -y -i \"%s\" -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls \"%s\"" % (filename, m3u8_file)

		if is_run:
			p = os.system(cmd)

			if p == 0:
				if is_stay == False and os.path.exists(m3u8_file): # delete_if_stay_false
					os.remove(m3u8_file)

				try:
					index_count, playlist_count = await seg_and_playlist_counts(fname=fname)
				except:
					index_count = playlist_count = 0
				else:
					if any((index_count, playlist_count)): # ts_segment_count / playlist_count
						print("Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]" % (index_count, playlist_count, filename, str(datetime.now())))
						write_log("debug counts", "Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]" % (index_count, playlist_count, filename, str(datetime.now())))

				return (True, cmd, "run")

			if p != 0:
				if os.path.exists(m3u8_file): # delete_if_error_run
					os.remove(m3u8_file)

				return (False, cmd, "run")

		elif not is_run:
			if is_stay == False and os.path.exists(m3u8_file): # delete_if_stay_false
				os.remove(m3u8_file)

			try:
				index_count, playlist_count = await seg_and_playlist_counts(fname=fname)
			except:
				index_count = playlist_count = 0
			else:
				if any((index_count, playlist_count)): # ts_segment_count(is_null) / playlist_count
					print("Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]" % (index_count, playlist_count, filename, str(datetime.now())))
					write_log("debug counts", "Найдено %d индексов и %d основных m3u8 списков для файла [%s] [%s]" % (index_count, playlist_count, filename, str(datetime.now())))

			return (True, cmd, "no_run")


# @log_error
async def myboottime() -> tuple:
	# global hbd

	hbd: int = 0 # hours_by_days

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
		ddate: int = int(abs(mdate - dnow).seconds) // 3600 # different_by_hours

		assert ddate >= 0, "Пустое количество часов или только включили PC @myboottime/ddate" # is_assert(debug)
	except AssertionError as err:
		ddate: int = 0
		logging.warning("Пустое количество часов или только включили PC @myboottime/ddate")
		raise err

	try:
		if ddate > 24:  # more_day
			hbd = ddate // 24 # days_by_hours
			write_log("debug daytime", "started %d days ago" % hbd) # debug daytime:"started 4 days 52 hours ago"
			is_hd_status = True
		elif ddate <= 24:  # one_day
			hbd = ddate # hours
			write_log("debug daytime", "started today %d hours ago" % ddate)
			is_hd_status = False
	except:
		write_log("debug daytime", "unknown boottime")
		hbd = 666 # if_error_null_days

	return (hbd, is_hd_status)

dayago, is_hd_status = asyncio.run(myboottime())

try:
	if dayago != 666:
		if is_hd_status:
			print("Days ago %d" % dayago)
		elif is_hd_status == False:
			print("Hours ago %d" % dayago)
except:
	write_log("debug worktime[mac]", "Unknown days/hours")

write_log("debug start", f"{str(datetime.now())}")

lanmacs: dict = {}

try:
	with open("".join([script_path, "\\lanmacs.json"]), encoding="utf-8") as ljf:
		lanmacs = json.load(ljf)
except:
	with open("".join([script_path, "\\lanmacs.json"]), "w", encoding="utf-8") as ljf:
		json.dump(lanmacs, ljf, ensure_ascii=False, indent=2, sort_keys=True)

async def ip_to_mac(ip: str = "") -> tuple: # single_by_async

	try:
		# eth_mac = get_mac_address(interface="eth0")
		# win_mac = get_mac_address(interface="Ethernet 3")
		ip_mac = get_mac_address(ip=ip) # "192.168.0.1" # default
		# ip6_mac = get_mac_address(ip6="::1")
		# host_mac = get_mac_address(hostname="localhost") # is_need
		# updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)
	except:
		ip_mac = ""

	'''
	# Enable debugging
	from getmac import getmac
	getmac.DEBUG = 2  # DEBUG level 2
	print(getmac.get_mac_address(interface="Ethernet 3"))

	# Change the UDP port used for updating the ARP table (UDP packet)
	from getmac import getmac
	getmac.PORT = 44444  # Default is 55555
	print(getmac.get_mac_address(ip="192.168.0.1", network_request=True))
	'''

	if all((ip, ip_mac)):
		print("Получаю сведения ip: %s" % ip)
		print("Сведения ip, mac: %s" % ";".join([ip, ip_mac]))
		write_log("debug ip_to_mac", ";".join([ip, ip_mac, str(datetime.now())])) # only_positive
	elif not ip_mac:
		# print("Нет сведений по ip: %s и он был пропущен" % ip) # no_negative
		write_log("debug ip_to_mac[nomac]", "%s [%s]" % (ip, str(datetime.now())))

	return (ip, ip_mac)


async def hostname_and_ip() -> tuple: # get_hostname_and_ip

	try:
		hostname = socket.gethostname() # default_hostname
	except:
		hostname = ""

	try:
		IPAddr=socket.gethostbyname(hostname) # default_ip
	except:
		IPAddr = ""
	finally:
		if not hostname:
			hostname = socket.getfqdn(IPAddr) #  DESKTOP-L7B4S7M (I'm in a windows machine)

	try:
		assert hostname and IPAddr, "Пустой Host или IP, @hostname_and_ip/hostname/IPAddr" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Пустой Host или IP, @hostname_and_ip/%s/%s" % (hostname, IPAddr))
		raise err
		return ("", "")

	# if any((not hostname, not IPAddr)):
		# return ("", "")

	write_log("debug hostname_and_ip", ";".join([hostname, IPAddr, str(datetime.now())])) # positive

	return (hostname, IPAddr) #('SergeyPC', '192.168.1.109')

	# print("Your Computer Name is:"+hostname)
	# print("Your Computer IP Address is:"+IPAddr)


async def current_ip() -> tuple: # get_ip_by_current_lan

	try:
		host, ip = await hostname_and_ip()
	except:
		host = ip = ""

	try:
		assert ip, "Пустой ip адресс @current_ip/ip" # is_assert(debug)
	except AssertionError as err:
		ip = ""
		logging.warning("Пустой ip адресс @current_ip/ip")
		raise err
	else:
		write_log("debug current_ip", "%s [%s]" % (";".join([ip, host]), str(datetime.now()))) # positive

	return (ip, host)


async def ipconfig_to_base():

	global lanmacs

	try:
		ip_address, _ = await current_ip() # ip_template
	except:
		ip_address = ""

	ip: str = ""

	if ip_address.count(".") == 3:
		ip = ".".join(ip_address.split(".")[:-1]) # 192.168.1

	if ip: #ip_range
		for i in range(1, 255):

			curr_ip = ".".join([ip, str(i)])

			try:
				cip, cmac = await ip_to_mac(ip=curr_ip)
			except:
				cip = cmac = ""
				continue # if_error_skip_ip
			else:
				if all((cmac, cip)): # save_if_all_info
					write_log("debug ipconfig_to_base[mac]", "%s [%s]" % (cmac, str(datetime.now())))
					write_log("debug ipconfig_to_base[ip]", "%s [%s]" % (cip, str(datetime.now())))

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
						combine_info = ";".join([socket.gethostbyaddr(curr_ip)[0].strip(), cip.strip()]) if socket.gethostbyaddr(curr_ip) else cip.strip() # pass_1_of_2
						if not ";" in combine_info:
							combine_info = ";".join([socket.getfqdn(cip.strip()), cip.strip()]) if socket.getfqdn(cip.strip()) else cip.strip() # pass_2_of_2

					except:
						combine_info = cip.strip()

					is_update: bool = all((last_info, combine_info, last_info != combine_info))
					is_new: bool = any((all((not last_info, combine_info)), all((not cmac.strip() in [*lanmacs], cmac))))

					if any((is_new, is_update)): # if_updated(vendor) / if_new(vendor)

						if is_new:
							print("информация по ip %s добавлена в базу" % cip.strip())
						if is_update:
							print("информация по ip %s обновлена в базе" % cip.strip())

						lanmacs[cmac.strip()] = combine_info # host;"ip";mac_to_vendor # "ip";mac_to_vendor
				else:
					continue # if_some_data_null
		else: # is_no_break
			print("Компьютеры с ip адресами начинающимися %s просканированны" % ip) # is_color

async def ip_config():

	# async with asyncio.TaskGroup() as gp:
	task = asyncio.create_task(ipconfig_to_base()) # old
	# task = tg.create_task(ipconfig_to_base())

	await task # old

"""
import scapy.all as scapy # pip install -U scapy # WARNING: No libpcap provider available ! pcap won't be used

def scan(ip)
	scapy.arping(ip)

scan(10.0.2.1/24)
"""

'''
ip_str = "127.0.0.1"

try:
	ip, host = asyncio.run(current_ip()) # ip_str = ".".join(ip.split(".")[0:3]) + ".1"
except:
	ip = host = ""
else:
	if len(ip.split(".")) >= 3:
		ip_str = ".".join(ip.split(".")[0:3]) + ".1"


async def arp_by_ip(ip_router="/".join([ip_str, "24"])): # 192.168.1.1/24
	# RuntimeError: Sniffing and sending packets is not available at layer 2: "winpcap" is not installed. You may use conf.L3socket orconf.L3socket6 to access layer 3
	pass # scapy.arping(ip_router)
'''


def time_to_ms() -> int: # unixtime -> ms

	try:
		tim = int(time() * 1000) # time() - unixtime # * 1000 = ms

		assert tim >= 0, "Ошибка конвертирования времени @time_to_ms/tim" # is_assert(debug)
	except AssertionError as err:
		tim = 0
		logging.warning("Ошибка конвертирования времени @time_to_ms/tim")
		raise err

	return int(tim) # ms # 1681467127489


# change_full_to_short(if_need_or_test_by_logging) # temporary_not_use
def full_to_short(filename) -> str:
	try:
		short_filename = "".join([filename[0], ":\\...\\", filename.split("\\")[-1]]).strip()  # is_ok
	except:
		try:
			short_filename = filename.split("\\")[-1].strip()  # default_short_without_drive
		except:
			short_filename = filename.strip()  # if_error_stay_old_filename

	return short_filename


# count_level_from_full("c:\\mytemp\\downloads\\hello.world") # need_folder_by_level # 4
def count_level_from_full(filename) -> int:

	try:
		assert os.path.exists(filename), "Файл отсуствует @count_level_from_full/filename" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Файл отсуствует @count_level_from_full/%s" % filename)
		raise err
		return 0

	# if not filename or not os.path.exists(filename):
		# return 0

	try:
		level_count: int = len(filename.split("\\")) if filename else 0
	except BaseException as e:
		level_count: int = 0
		write_log("debug level_count[filename][error]", "%s [%s]" % (filename, str(e)), is_error=True)
	else:
		if not os.path.isfile("\\".join(filename.split("\\")[0:level_count-1])): # if_folder(skip_file)
			write_log("debug level_count[filename]", "%s [%d]" % (filename, level_count)) # logging_file_by_level

	return level_count


# slugify("Hello, world") # Hello-world
# slugify("My name is Sergey, my age is 39") # My-name-is-Sergey-my-age-is-39
# slugify("prog-help.ru-Python  KivyKivyMD создание шаблонов для уменьшения кода")
# prog-helpru-Python--KivyKivyMD-создание-шаблонов-для-уменьшения-кода


# @log_error
def slugify(s: str = "") -> str:

	try:
		assert s, "Пустая строка @slugify/s" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Пустая строка @slugify/s")
		raise err
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


# kill_process_by_name(test) # percent?
# @log_error
async def kill_proc_by_name(proc_name: str = ""):
	try:
		os.system("taskkill /f /im %s" % proc_name)
	except:
		PROCNAME = proc_name

		try:
			for proc in psutil.process_iter():
				if proc.name == PROCNAME:
					p = psutil.Process(proc.pid)

					if not 'SYSTEM' in p.username:
						# write_log("debug kill", str(proc.name))
						proc.kill()

		except:
			return


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
	logging.info("Today is: %s, weekday is: %s, season(days): %s, number_of_day: %s" % (dtw["date"], dtw["weekday"], dtw["season(days)"], dtw["number_of_day"]))
	write_log("debug dtw[ok]", "Today is: %s, weekday is: %s, season(days): %s, number_of_day: %s" % (dtw["date"], dtw["weekday"], dtw["season(days)"], dtw["number_of_day"]))

# debug
# sys.exit() # spyder_debug
# exit() # python_debug(no_run) # debug # stop_if_some_error(is_long)

# dsize = dsize2 = 0

try:
	dsize: int = disk_usage("c:\\").free // (1024 ** 2)
except:
	dsize: int = 0

try:
	dsize2: int = disk_usage("d:\\").free // (1024 ** 2)
except:
	dsize2: int = 0

mem: float = psutil.virtual_memory()[2]  # need_less_80(ram)

ctme = datetime.now()

async def utc_time(dt = datetime.now()):

	gmt = datetime.utcnow() # datetime.datetime(2023, 2, 23, 3, 47, 36, 326713)
	cur_gmt = datetime.now() # ?

	try:
		gmt = abs(cur_gmt - gmt).seconds // 3600 # 5

		assert gmt in range(-99, 100), "Ошибка часового пояса или отрицательный часовой пояс @utc_time/gmt" # is_assert(debug)
	except AssertionError as err:
		gmt = 999
		logging.warning("Ошибка часового пояса или отрицательный часовой пояс @utc_time/gmt")
		raise err

	return gmt


utc = asyncio.run(utc_time())


async def shutdown_if_time(utcnow: int = utc):

	global ctme

	# mytime: dict = {"jobtime": [9, 18, 4], "dinnertime": [12, 13], "sleeptime": [0, 7]}

	write_log("debug utctime", "Utc: %s" % str(utcnow)) # time_zone(gmt)

	# if ctime.hour <= mytime["sleeptime"][1] and all((not list(filter(lambda x: "aria2" in x, tuple(os.listdir(copy_src)))), not list(filter(lambda x: "aria2" in x, tuple(os.listdir(copy_src2)))))):  # shutdown_before_7am_or_equal_and_no_download_files
	# if ctme.hour < mytime["sleeptime"][1] and any((not os.listdir(copy_src), not os.listdir(copy_src2))):  # shutdown_before_7am_or_equal_and_some_no_download_files
	if ctme.hour < mytime["sleeptime"][1]:  # utcnow <= ctme.hour < mytime["sleeptime"][1] # shutdown_before_6am_or_equal
		# run(["cmd", "/c", "shutdown", "/a"], shell=False)  # stop_timer(is_need_hide_no_cancel) # kill_proc_by_name("shutdown.exe") # stop_timer_by_app # 1
		# run(["cmd", "/c", "shutdown", "/s", "/t", "3600", "/c", "Чтобы отменить выключение, выполните в командной строке shutdown /a"], shell=False)  # shutdown(1hour) (midnight - 7am) # start_after # if_no_updates #1.1
		run(["cmd", "/c", "shutdown", "/s", "/t", "1800", "/c", "Чтобы отменить выключение, выполните в командной строке shutdown /a"], shell=False)  # shutdown(30min) (midnight - 7am) # start_after
		# run(["cmd", "/c", "shutdown", "/g", "/t", "900", "/c", "Чтобы отменить выключение, выполните в командной строке shutdown /a"], shell=False) # shutdown(15min) (midnight - 7am) # start_after # if_updates

		# """
		try:
			if os.path.exists("d:\\"):
				sleep(900)
		except BaseException as e:
			print("job[timeout] [%s]" % str(e))
			write_log("debug job[timeout]", "%s" % str(e), is_error=True)
		# """

		exit()

	elif ctme.hour >= mytime["sleeptime"][1]:  # ctme.hour % 3 == 0 # every_3_hours_by_divmod # stop_shutdown_by_time
		run(["cmd", "/c", "shutdown", "/a"], shell=False)  # stop_timer_after_7am(more)
		await kill_proc_by_name("shutdown.exe") # stop_timer_by_app # asyncio.run(

	# if_equal_time(mytime["sleeptime"][1])_pass

# min_2status
# dspace's / no_download_files / no_sleep_time(backup_time) / is_skip_overload_cpu_more_80("85")

# cpu_overload(try_stop_SysMain/Superfetch)

# dspace(reserve) # no_projects # midnight - 6am # 1
# is_status: tuple = (any((not dsize2, not os.listdir(path_for_folder1))), ctme.hour < mytime["sleeptime"][1])
# dspace(reserve) # midnight - 6am # skip_overload # 2
is_status: tuple = (not dsize2, ctme.hour < mytime["sleeptime"][1]) # use_default
# skip_dspace(reverve) # midnight - 6am # overload_cpu(80) # 3
# is_status: tuple = (ctme.hour < mytime["sleeptime"][1], mem >= 80) # no_use_for_pycharm(overload)

if is_status.count(True) > 0:
	print("0[1431] %s" % str(is_status), mem)
	# sys.exit()

	try:
		ut = asyncio.run(utc_time())
	except:
		ut = 0

	if any((ut < mytime["sleeptime"][1], ctme.hour < mytime["sleeptime"][1])):
		asyncio.run(shutdown_if_time())

	exit()


# Sound notify

# @log_error
def sound_notify(text: str = ""): #2
	try:
		if text:
			engine = pyttsx3.init()
			engine.say(text)
			engine.runAndWait()
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "Не смог произнести текст! [%s]" % str(e))
		write_log("debug soundnotify[error]", "Не смог произнести текст! [%s]" % str(e), is_error=True)
	else:
		if text:
			print(Style.BRIGHT + Fore.GREEN + "Текст [%s] успешно произнесён" % text)
			write_log("debug soundnotify[ok]", "Текст [%s] успешно произнесён" % text)


# --- Files by template to list ---

filter_list: list = []


# 2
async def my_args() -> list: #2

	tmp: list = []
	# some_list: list = []

	# sys.argv -> "argparse"

	# list_arguments # new_command_line_arguments # manual(-h) # debug/test
	"""
	## python argparse_4.py -h
	usage: argparse_4.py [-h] parent_names parent_names parent_names

	positional arguments:
	  parent_filter

	optional arguments:
	  -h, --help    show this help message and exit
	"""

	"""
	## python argparse_4.py -parent_filter 0e # 0e

	tmp: list = []
	is_error: bool = False
	parrent_filter: str = ""

	parser = argparse.ArgumentParser()
	# nargs for store actions must be > 0; if you have nothing to store, actions such as store true or store const may be more appropriate
	try:
		parser.add_argument("-parent_filter", type=str) # use_"one"_argument_input
	except:
		parent_filter = ""
		is_error = True
	else:
		args = parser.parse_args()
		parent_filter = args.parent_filter

		tmp.append(parent_filter) # add_current_string_from_argument #["0e"]
	"""

	# abc_or_num_regex = re.compile(r"^[A-Z0-9].*", re.I)

	# old_command_line_arguments
	# """
	# if is_error:
	try:
		tmp = [str(sys.argv[i]) for i in range(0, len(sys.argv))]  # old(no_gen) #
	except:
		tmp = []
	else:
		if len(tmp) == 1:
			tmp = []  # no_filter

			print(Style.BRIGHT + Fore.YELLOW + "Не найдено аргументов", Style.BRIGHT + Fore.WHITE + "[%s]" % str(datetime.now()))  # is_color
			write_log("debug sys[noargs]", "Не найдено аргументов [%s]" % str(datetime.now()))
		elif len(tmp) > 1:
			temp = tmp[1:]  # skip_script_name_and_have_filter

			# temp2 = list(set([t.strip() for t in temp if abc_or_num_regex.findall(t)])) # start(abc/123) # is_ok
			temp2 = list(set([f.strip() for f in filter(lambda x: abc_or_num_regex.findall(x), tuple(temp))])) # start(abc/123) # debug

			temp3 = list(set([t2.strip() if len(t2) >= 2 else "".join([t2,"_"]) for t2 in temp2]))  # length=2 # debug
			tmp = sorted(temp3, reverse=False)
			# tmp = sorted(temp3, key=len, reverse=False)

		print(Style.BRIGHT + Fore.CYAN + "Найдено %d аргументов [%s]" % (len(tmp), str(datetime.now())))  # is_color
		write_log("debug sys[args]", "Найдено %d аргументов [%s]" % (len(tmp), str(datetime.now())))
	# """

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
			print(f"Зарядка подключена, заряд батареи: {percent}%")
			write_log("debug battery_info[plugged]", f"Зарядка подключена, заряд батареи: {percent}% [{str(datetime.now())}]")
		elif not plugged:
			print(f"Зарядка отключена, заряд батареи: {percent}%")
			write_log("debug battery_info[unplugged]", f"Зарядка отключена, заряд батареи: {percent}% [{str(datetime.now())}]")

	return (plugged, percent) # battery


# --- Find files by period(max_days) ---


# filename(str)/period(int)/is_select(bool)
def mdate_by_days(filename, period: int = 30, is_select: bool = False, is_dir: bool = False, is_less: bool = False, is_any: bool = False) -> any: # default(month) #14

	try:
		assert os.path.exists(filename), "Файл отсутствует @mdate_by_days/filename" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Файл отсутствует @mdate_by_days/%s" % filename)
		raise err
		return None

	# if not os.path.exists(filename): # not filename
		# return None

	# debug_for_folder
	today = datetime.today()  # datetime
	fdate = os.path.getmtime(filename)  # unixdate(file/folder)
	ndate = datetime.fromtimestamp(fdate)  # datetime

	try:
		is_dir = (not os.path.isfile(filename)) # is_folder_filter(True) / is_file_fitler(False)
	except:
		is_dir = False # if_error_is_not_folder

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
		week_status = f"Week for period: {int(days_period // 7)}" if days_period // 7 > 0 else "Week: None"
	except BaseException as e:
		week_status = "Week [error] [%s]" % str(e)
	finally:
		write_log("debug files[week]", week_status)  # "Week for period: %d" % days_period // 7

	try:
		# default_calendar_month #is_abs
		month_status = f"Month for period: {int(days_period // 30)}" if days_period // 30 > 0 else "Month: None"
	except BaseException as e:
		month_status = "Month [error] [%s]" % str(e)
	finally:
		write_log("debug files[month]", "%s" % month_status)  # "Month for period: %d" % days_period // 30

	# default_calendar_year #is_abs
	dt = datetime.now()

	max_days_by_year: int = 0

	def is_year_leap() -> int:

		try:
			max_days_by_year: int = 366 if dt.year % 4 == 0 else 365
		except:
			max_days_by_year: int = 365

		return max_days_by_year

	max_days_by_year = is_year_leap()

	try:
		year_status = f"Year for period: {int(days_period // max_days_by_year)}" if days_period // max_days_by_year > 0 else "Year: None"
	except BaseException as e:
		year_status = "Year [error] [%s]" % str(e)
	finally:
		write_log("debug files[year]", "%s" % year_status)  # "Year for period: %d" % days_period // 365

	try:
		days_ago: int = abs(today - ndate).days # default=file/folder
	except BaseException as e:
		days_ago: int = 0
		# print("%s. [%s]" % (filename, str(e)))

		if not is_dir:
			write_log("debug file[today]", "%s. [%s]" % (filename, str(e)), is_error=True)
		elif is_dir:
			write_log("debug folder[today]", "%s. [%s]" % (filename, str(e)), is_error=True)
		return days_ago # if_error_use_current_day
	else:
		if (is_less == True and all((period >= 0, days_ago <= period)) or is_less == False and days_ago >= period) and is_any == False:
			if not is_dir:
				write_log("debug file[dayago][file]", "Days ago: %d, last file: %s" % (days_ago, filename))
			elif is_dir:
				write_log("debug file[dayago][dir]", "Days ago: %d, last file: %s" % (days_ago, filename))
		elif all((is_any == True, days_ago >= 0, period >= 0)):
			write_log("debug file[dayago]", "Days ago: %d, last file: %s" % (days_ago, filename))

		return days_ago


async def datetime_from_file(filename) -> tuple: #4
	fdate = os.path.getmtime(filename)  # unixdate # 1648708605.2300806 # <class 'float'>

	try:
		ndate = datetime.fromtimestamp(
			fdate)  # datetime.datetime(2022, 3, 31, 11, 36, 45, 230081) # <class 'datetime.datetime'>
	except:
		ndate = datetime.today()  # current
		return (ndate, False)  # current_date + error_status
	else:
		return (ndate, True)  # current_date + normal_status


# @log_error
async def days_by_list(lst: list = [], is_avg: bool = False): #8

	try:
		assert lst and isinstance(lst, list), "Пустой список или другой формат списка @days_by_list/lst" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Пустой список или другой формат списка @days_by_list/lst")
		raise err
		return None

	# if any((not lst, not isinstance(lst, list))):
		# return None

	avg_list: list = []
	sum_days: int = 0
	len_days: int = 0
	max_days: int = 0

	today = datetime.today()  # datetime
	try:
		# lst = list(days_by_list_gen()) # new(yes_gen)
		lst: list = [l.strip() for l in filter(lambda x: os.path.exists(x), tuple(lst))]
	except:
		lst: list = []  # old(no_gen) # l.strip() for l in filter(lambda x: os.path.exists(x), tuple(lst))

	tmp = list(set([l.strip() for l in filter(lambda x: x, tuple(lst))]))
	lst = sorted(tmp, reverse=False)

	with unique_semaphore:
		for l in filter(lambda x: x, tuple(lst)):

			if not lst:  # no_data
				break

			try:
				fdate = os.path.getmtime(l)  # unixdate
				ndate = datetime.fromtimestamp(fdate)  # datetime
			except:
				continue

			try:
				days_ago = abs(today - ndate).days
			except:
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

		sum_days: int = (reduce(lambda x, y: x + y, avg_list))  # sum_days = sum(avg_list)
		len_days: int = len(avg_list)

		try:
			avg_days: int = (lambda s, l: s // l)(sum_days, len_days)
		except:  # DevideByZero
			avg_days: int = 0
		else:
			if avg_days != None:  # use_avg_days # not_null
				max_days = avg_days

	return max_days


# @log_error
def fspace(src: str = "", dst: str = "", is_Log: bool = False) -> bool: #11

	try:
		assert os.path.exists(src), "Файл отсутствует @fspace/src" # is_assert(debug)
	except AssertionError: # as err:
		logging.warning("Файл отсутствует @fspace/src")
		# raise err
		return False

	# if not os.path.exists(src): # not src
		# return False  # if_not_exists(file/folder)

	try:
		fsize: int = os.path.getsize(src)
		dsize: int = disk_usage(dst[0] + ":\\").free

		assert fsize and dsize, "Нет размера файла или размера диска @fspace/fsize/dsize" # is_assert(debug)
	except AssertionError as err:
		fsize: int = 0
		dsize: int = 0
		logging.warning("Нет размера файла или размера диска @fspace/%s" % src)
		raise err

	fspace_status: bool = False

	try:
		fspace_status = all((fsize, dsize, int(fsize // (dsize / 100)) <= 100))  # fspace(ok-True,bad-False)
	except:
		fspace_status = False  # fspace(error-False)
	finally:
		return fspace_status


# fpath, fname = split_filename('c:\\downloads\\hello.wolrd') # use_filename_from_init
def split_filename(filename) -> tuple: #19

	try:
		assert os.path.exists(filename), "Файл отсутствует @split_filename/filename" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Файл отсутствует @split_filename/%s" % filename)
		raise err
		return ("", "")

	# if not os.path.exists(filename):
		# return ("", "")

	try:
		file_path, file_name = os.path.split(filename)
		assert file_path and file_name, "Имя папки или имя файла не указано @split_filename/file_path/file_name" # is_assert(debug)
	except AssertionError as err:
		file_path = file_name = ""
		logging.warning("Имя папки или имя файла не указано @split_filename/%s" % filename)
		raise err

	return (file_path.strip(), file_name.strip()) # return os.path.split(filename) # ('c:\\downloads', 'hello.wolrd')

# fullname = join_filename(file_path, file_name): # split_filename -> join_filename
def join_filename(file_path, file_name) -> str: #3
	return os.path.join(file_path.strip(), file_name.strip()) # 'c:\\downloads\\hello.wolrd'


# --- Notify center

icons: dict = {"cleaner": "c:\\downloads\\mytemp\\cleaner.ico",
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
			   "work": "c:\\downloads\\mytemp\\work.ico"}


# 9
# @log_error
def MyNotify(txt: str = "", icon: str = "", sec: int = 10): #13
	error: bool = False

	try:
		assert os.path.exists(icon), "Файл отсутствует @MyNotify/icon" # is_assert(debug)
	except AssertionError as err:
		error = True
		logging.warning("Файл отсутствует @MyNotify/%s" % icon)
		raise err

	# if not os.path.exists(icon):
		# error = True

	# ---- init(show) notify ----
	try:
		# отобразить_оповещение_в_трее
		toaster = ToastNotifier()
	except:
		error = True
	# pass
	finally:
		if error == False:
			if all((txt, icon, sec)):
				# threaded - в потоке
				# icon_path - ссылка_на_иконку_для_оповещений(ico)
				# duration - задержка в секундах
				toaster.show_toast("Моя программа", txt, threaded=True, icon_path=icon, duration=sec)

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
		return f'Error as {str(e)}'


# one_folder("c:\\downloads\\", re.compile(r"(?:(zip))$")) # one_folder # hide_regex(test_logic)
# one_folder("c:\\downloads\\new\\", video_regex)
def one_folder(folder, files_template) -> list:
	try:
		if not os.path.exists(folder) and os.listdir(folder):  # disk_usage(folder[0] + ":\\").free:
			print("Создаётся папка %s т.к. она отсуствует" % folder)
			write_log("debug one_folder[create]", "Создаётся папка %s т.к. она отсуствует" % folder)
	except BaseException as e:
		write_log("debug one_folder[error]", "Ошибка создания папки %s [%s]" % (folder, str(e)), is_error=True)
	finally:
		try:
			os.mkdir(folder) # type1
		except BaseException as e:
			os.system(r"cmd /c mkdir %s" % folder) # type2(error)

			write_log("debug one_folder[folder]!",
					  "Папка %s уже создана [%s] [%s]" % (folder, str(e), str(datetime.now())), is_error=True)
		else:
			write_log("debug one_folder[folder]",
					  "Папка %s успешно создана [%s]" % (folder, str(datetime.now())))

	def one_folder_to_files(folder=folder, files_template=files_template):
		for lf in os.listdir(folder):
			if files_template.findall(lf.strip()) and os.path.isfile("".join([folder, lf.strip()])) and any((
					lf.split("\\")[-1].startswith(lf.split("\\")[-1].capitalize()), lf.split("\\")[-1].find(
							lf.split("\\")[-1]) == 0)):
				yield "".join([folder, lf.strip()])

	try:
		files = list(one_folder_to_files())
	except BaseException as e:
		files = []  # if_error_null_list
		write_log("debug error_one_folder", "%s [%s]" % (folder, str(e)), is_error=True)
	finally:
		write_log("debug count_one_folder", "%d" % len(files))

	return list(files)  # ['c:\\downloads\\Current_BacthConverter.zip', ...] # capitalize # Abc... # find ~ findall(regex)


# sub_folder("c:\\downloads\\combine\\", re.compile(r"(?:(zip))$")) # sub_folder # hide_regex(test_logic)
def sub_folder(folder, files_template) -> list:
	try:
		if not os.path.exists(folder) and os.listdir(folder):  # disk_usage(folder[0] + ":\\").free:
			print("Создаётся подпапка %s т.к. она отсуствует" % folder)
			write_log("debug sub_folder[create]", "Создаётся подпапка %s т.к. она отсуствует" % folder)
	except BaseException as e:
		write_log("debug sub_folder[error]", "Ошибка создания подпапки %s [%s]" % (folder, str(e)), is_error=True)

	finally:

		try:
			os.mkdir(folder) # type1
		except BaseException as e:
			os.system(r"cmd /c mkdir %s " % folder) # type2(error)

			write_log("debug sub_folder[folder]!",
					  "Папка %s уже создана [%s] [%s]" % (folder, str(e), str(datetime.now())), is_error=True)
		else:
			write_log("debug sub_folder[folder]",
					  "Папка %s успешно создана [%s]" % (folder, str(datetime.now())))

	def sub_folder_to_files(folder=folder, files_template=files_template):
		for lf in walk(folder, files_template):
			if files_template.findall(lf.split("\\")[-1]) and os.path.isfile(lf) and any((
					lf.split("\\")[-1].startswith(lf.split("\\")[-1].capitalize()),
					lf.split("\\")[-1].find(lf.split("\\")[-1]) == 0)):
				yield lf.strip()

	try:
		files: list = list(sub_folder_to_files())
	except BaseException as e:
		files: list = []  # if_error_null_list
		write_log("debug error_sub_folder", "%s [%s]" % (folder, str(e)), is_error=True)
	finally:
		write_log("debug count_sub_folder", "%d" % len(files))

	return list(files)  # ['c:\\downloads\\combine\\Archive\\Adobe_Photoshop_CC_2019.zip', ...] # capitalize # Abc... # find ~ findall(regex)


# --- Math ---

def most_frequent(list) -> any: # int(str) # None
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
def hms(seconds: int = 0): #37
	try:
		h: int = seconds // 3600
		m: int = seconds % 3600 // 60
		s: int = seconds % 3600 % 60
		assert any((h, m, s)), "Нет какой-то величины времени @hms/h/m/s" # is_assert(debug)
	except AssertionError as err:
		h: int = 0
		m: int = 0
		s: int = 0
		logging.warning("Нет какой-то величины времени @hms/%d" % seconds)
		raise err

	if any((h, m, s)):
		return '{:02d}:{:02d}:{:02d}'.format(
			h, m, s)  # hh:mm:ss # '{:02d} час. {:02d} мин. {:02d} сек.'.format(h, m, s) # hh mm ss
	else:  # logic(another_time)
		return None  # str(None)


# @log_error
async def avg_lst(lst: list = []) -> int:  # default_list / in_arg_is_filesizes_list #4

	'''
	try:
		assert lst and isinstance(lst, list), "Пустой список или другой формат списка @avg_lst/lst" # is_assert(debug)
	except AssertionError: # as err:
		logging.warning("Пустой список или другой формат списка @avg_lst/lst")
		# raise err
		return 0
	'''

	#if any((not lst, not isinstance(lst, list))):
		#return 0

	sum_lst: int = (reduce(lambda x, y: x + y, lst))  # sum_lst = sum(lst)
	len_lst: int = len(lst)

	try:
		avg_size: int = (lambda s, l: s // l)(sum_lst, len_lst)

		assert avg_size, "Пустая сумма или длина списка нулевая @avg_list/avg_size" # is_assert(debug)
	except AssertionError as err:
		avg_size: int = 0
		logging.warning("Пустая сумма или длина списка нулевая @avg_list/avg_size")
		raise err
	finally:
		return avg_size


# @log_error
async def screen_clear():
	# for mac and linux(here, os.name is 'posix')

	if os.name == 'posix':
		os.system('clear')
	else:
		# for windows platfrom
		os.system('cls')


asyncio.run(screen_clear()) # clear_screen
asyncio.run(battery_info()) # battery_info(after_clear_screen)


# print out some text

# wait for 5 seconds to clear screen
# sleep(5)
# now call function we defined above
# screen_clear()

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

"""
from dataclass import dataclass # pip install -U dataclass

@dataclass
class Book:
	title: str = ""
	author: str = ""

book = Book("Fahrenheit 451", "Bradbury")

print(book) # Book(title="Fahrenheit 451", author="Bradbury")
"""

# 2
class Get_AR:

	__slots__ = ["width", "height"]

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def width_to_ar(self, width: int = 0, height: int = 0, owidth: int = 640) -> tuple:  # width=640,height=360

		try:
			assert width and height, "Ширина пустая @width_to_ar/width/height" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Ширина пустая @width_to_ar/%d/%d" % (width, height))
			raise err
			return (0, 0, 0)

		# if any((not width, not height)):
			# return (0, 0, 0)

		"""Specify the Width To Retain the Aspect Ratio"""

		if width > owidth and owidth:  # if_need_optimal_ar
			first = width / owidth  # 640/640=1
			second: float = height / first  # 360/1

			if not isinstance(second, int):
				second = int(second)  # height(float->int)
			if all((second % 2 != 0, second)):
				second -= 1  # height(-1)

			def sh_equal(second=second, owidth=owidth, width=width, height=height):
				for nh in range(second - 16, second, 1):
					if (owidth / nh) == (width / height):
						yield (owidth, nh)

			try:
				# scale_height_equal = [(owidth, nh) for nh in range(second-16, second,1) if (owidth/nh) == (width/height)] # old(no_gen)
				scale_height_equal: list = list(sh_equal())  # new(yes_gen)
			except:
				scale_height_equal: list = []
			else:
				if scale_height_equal:
					with unique_semaphore:
						for she in scale_height_equal:

							try:
								width_calc = she[0] - 1 if she[0] % 2 != 0 else she[0]  # -1
							except:
								width_calc = 0
							else:
								she[0] = width_calc

							try:
								print(Style.BRIGHT + Fore.YELLOW + "Оптимальный маштаб(высота) для маштабируемого файла",
									Style.BRIGHT + Fore.WHITE + "%s" % "x".join([str(she[0]), str(she[1])]))  # is_color
							except:
								continue
							else:
								write_log("debug scale_height_equal!", "%s" % ":".join([str(she[0]), str(she[1])]))
				else:
					print(Style.BRIGHT + Fore.YELLOW + "Оптимальный маштаб(высота) для маштабируемого файла",
						Style.BRIGHT + Fore.WHITE + "%s" % "x".join([str(owidth), str(second)]))  # is_color
					write_log("debug scale_height_equal", "%s" % ":".join([str(owidth), str(second)]))

			return (int(owidth), int(second), round(int(owidth) / int(second), 2))  # 640, 360, 640/360

		# elif width <= owidth and width:  # if_optimal_ar
		# return (width, height, 0))
		else:
			return (0, 0, 0)

	def height_to_ar(self, width: int = 0, height: int = 0,
					 oheight: int = 360) -> tuple:  # width=640,height=360 # islogic=(False, 640)

		try:
			assert width and height, "Высота пустая @height_to_ar/width/height" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Высота пустая @height_to_ar/%d/%d" % (width, height))
			raise err
			return (0, 0, 0)

		# if any((not width, not height)):
			# return (0, 0, 0)

		"""Specify the Height To Retain the Aspect Ratio"""

		if height > oheight and oheight:
			first = height / oheight  # 360 / 360
			second: float = width / first  # 640 / 1

			if not isinstance(second, int):
				second = int(second)  # width(float->int)
			if all((second % 2 != 0, second)):
				second -= 1  # width(-1)

			def sw_equal(second=second, oheight=oheight, width=width, height=height):
				for nw in range(second - 16, second, 1):
					if (nw / oheight) == (width / height):
						yield (nw, oheight)

			try:
				# scale_width_equal = [(nw, oheight) for nw in range(second-16, second,1) if (nw/oheight) == (width/height)] # old(no_gen)
				scale_width_equal: list = list(sw_equal())  # new(yes_gen)
			except:
				scale_width_equal: list = []

			else:
				if scale_width_equal:
					with unique_semaphore:
						for swe in scale_width_equal:

							try:
								height_calc = swe[1] - 1 if swe[1] % 2 != 0 else swe[1]  # -1 or +1
							except:
								height_calc = 0
							else:
								swe[1] = height_calc

							try:
								print(Style.BRIGHT + Fore.YELLOW + "Оптимальный маштаб(длина) для маштабируемого файла",
									Style.BRIGHT + Fore.WHITE + "%s" % "x".join([str(swe[0]), str(swe[1])]))  # is_color
							except:
								continue
							else:
								write_log("debug scale_width_equal!", "%s" % ":".join([str(swe[0]), str(swe[1])]))
				else:
					print(Style.BRIGHT + Fore.YELLOW + "Оптимальный маштаб(длина) для маштабируемого файла",
						Style.BRIGHT + Fore.WHITE + "%s" % "x".join([str(second), str(oheight)]))  # is_color
					write_log("debug scale_width_equal", "%s" % ":".join([str(second), str(oheight)]))

			return (int(second), int(oheight), round(int(second) / int(oheight), 2))  # 640, 360, 640/360
		# elif height <= oheight and height:
		# return (width, height, 0))
		else:
			return (0, 0, 0)

	def spd_ar(self, filename: str = "", width: int = 0, height: int = 0, is_hd: bool = False, is_sd: bool = False) -> tuple:

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename) and width and height, "Файл отствует, высота или ширина пустые @spd_ar/filename/width/height" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отствует, высота или ширина пустые @spd_ar/%s" % self.filename)
			raise err
			return ("", "", "")

		# if not os.path.exists(self.filename) or any((not width, not height)): # not filename
			# return ("", "", "")

		# aspect ratio list(display/scale/pixel)

		dar_list = []; dar_list.extend([4 / 3, 16 / 9]) # is_google # SAR x PAR = DAR
		# dar_list = []; dar_list.append() # dar_by_job(one)

		sar_dict: dict = {}

		try:
			with open(sar_base, encoding="utf-8") as sjf:
				sar_dict = json.load(sjf)
		except:
			with open(sar_base, "w", encoding="utf-8") as sjf:
				json.dump(sar_dict, ensure_ascii=False, indent=2, sort_keys=True)

		# SAR of 640/480 = 4:3
		# sar_list = []; sar_list.extend([1/1, 12/11, 10/11, 16/11, 40/33, 24/11, 20/11, 32/11, 80/33, 72/59, 11/9, 5/4, 22/15, 4/3, 18/11, 15/11, 64/33, 160/99, 3/2, 2/1]) # last
		sar_list = []; sar_list.append(width/height)

		try:
			sar_dict[self.filename] = [self.filename, width, height, width / height] # {sar : (filename, width, height)}
		except:
			sar_dict[self.filename] = [self.filename] # {no_sar : filename}

		if sar_dict:
			with open(sar_base, "w", encoding="utf-8") as sjf:
				json.dump(sar_dict, ensure_ascjii=False, indent=2, sort_keys=True)

		par_dict: dict = {}

		try:
			with open(par_base, encoding="utf-8") as pjf:
				par_dict = json.load(pjf)
		except:
			with open(par_base, "w", encoding="utf-8") as pjf:
				json.dump(par_dict, ensure_ascii=False, indent=2, sort_keys=True)

		# (4/3) / (704/576) = 12/11 # (16/9) / (704/576) = 16/11 # PAR = DAR/SAR
		par_list = [] #; par_list = [float(dl / sl) for dl in dar_list for sl in sar_list if all((dl, sl))]

		try:
			par_list = [float(dl / sl) for dl in dar_list for sl in sar_list if all((dl, sl))] # par_by_job # is_json
		except:
			par_list = [] # no_par

		try:
			par_dict = {self.filename: str(pl) for pl in par_list if pl} # {filename / par(value)}
		except:
			par_dict = {}

		if par_dict:
			with open(par_base, "w", encoding="utf-8") as pjf:
				json.dump(par_dict, ensure_ascii=False, indent=2, sort_keys=True)

		dar_dict: dict = {}

		try:
			with open(dar_base, encoding="utf-8") as djf:
				dar_dict = json.load(djf)
		except:
			with open(dar_base, "w", encoding="utf-8") as djf:
				json.dump(dar_dict, ensure_ascii=False, indent=2, sort_keys=True)

		dar_list = [] #; dar_list = [sl * pl for sl in sar_list for pl in par_list if all((sl, pl))]

		try:
			dar_list = [sl * pl for sl in sar_list for pl in par_list if all((sl, pl))] # dar_by_job
		except:
			dar_list = [] # no_dar

		try:
			dar_dict = {self.filename: str(dl) for dl in dar_list if dl} # {filename : dar(value)}
		except:
			dar_dict = {}

		if dar_dict:
			with open(dar_base, "w", encoding="utf-8") as djf:
				json.dump(dar_dict, ensure_ascii=False, indent=2, sort_keys=True)

		if any((dar_list, sar_list, par_list)):
			print(Style.BRIGHT + Fore.WHITE + "%s" % self.filename,"D(isplay)AR: %s" % str(dar_list), "S(cale)AR: %s" % str(sar_list), "P(ixel)AR: %s" % str(par_list))
			write_log("debug aspect_ratio[list]", "File: %s, DAR: %s, SAR: %s, PAR: %s" % (self.filename, str(dar_list), str(sar_list), str(par_list)))

		is_hd_sd = False  # sd(False), hd(True)

		if width / height in dar_list:
			if width / height == 4 / 3:
				is_hd_sd = False
				print("Scale for %dx%d is sd [%s] [%s]" % (width, height, self.filename, str(is_hd_sd)))
			elif width / height == 16 / 9:
				is_hd_sd = True
				print("Scale for %dx%d is hd [%s] [%s]" % (width, height, self.filename, str(is_hd_sd)))

		# sar_list2: list = []

		try:
			# sar_list2 = list(ar_to_gen(sar_list, w=width, h=height)) # new(yes_gen) # [(640, 480, 1.3333333333333333)]
			sar_list2 = [(width, height, sl) for sl in sar_list if
							width / height == sl]
		except:
			sar_list2 = []  # old(no_gen) # (width, height, l) for l in sar_list if width/height == l

		if sar_list2:
			for sl2 in sar_list2:
				if all((sl2[0], sl2[1])):
					print("x".join([str(sl2[0]), str(sl2[1])]),
						  "SAR [%s]" % self.filename)  # debug/test # 640x480 SAR []
			else:
				print("SAR", sar_list2)

		# par_list2: list = []

		try:
			# par_list2 = list(ar_to_gen(par_list, w=width, h=height)) # new(yes_gen)
			par_list2 = [(width, height, pl) for pl in par_list if
							width / height == pl]
		except:
			par_list2 = []

		# for pl in par_list:  # old(no_gen)
		# if width/height == pl:
		# par_list2.append((w,h,pl))

		if par_list2:
			for pl2 in par_list2:
				if all((pl2[0], pl2[1])):
					print("x".join([str(pl2[0]), str(pl2[1])]), "PAR [%s]" % self.filename)  # debug/test
			else:
				print("PAR", par_list2)

		def wh_to_ar(b, e, ar):
			for w in range(1, b + 1):
				for h in range(1, e + 1):
					if w / h == ar:
						yield (w, h)

		try:
			# ar_list = [(w,h) for w in range(1,32) for h in range(1,32) if w/h == ar] # old(no_gen)
			ar_list = list(wh_to_ar(32, 32, width / height)) # new(yes_gen)
		except:
			ar_list = []

		if ar_list:

			try:
				sar = ":".join([str(ar_list[0][0]), str(ar_list[0][1])])
			except:
				sar = ""

			par = str(round(width / height, 2))[0:]

			if all((is_sd, not is_hd)):
				dar = str("16:9")
			elif all((is_hd, not is_sd)):
				dar = str("4:3")

			"""
			if filename:  # only_with_filename
				print(f"The file %s is %sx%s with SAR = %s , PAR = %s , DAR = %s (G-spot)" % (filename, width, height, sar, par, dar))
				write_log("debug spd[ar]", "%s [%s]" % (filename, ";".join(["sar=" % sar,"par=" % par, "dar=" % dar])))
			"""

			return (sar, par, dar)

		elif not ar_list:
			return ("", "", "")


# 9
class MyMeta:

	def __init__(self):
		pass

	"""@unique_data.json"""

	def get_meta(self, filename) -> bool:

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_meta/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_meta/%s" % self.filename)
			raise err
			return False

		# if not filename or not os.path.exists(self.filename):
			# return False

		metacmd = path_for_queue + "ffprobe.exe -v quiet -print_format json -show_format -show_streams %s > %s" % (
			self.filename, unique_base)

		try:
			p = os.system(metacmd)
		except:
			return False  # skip_if_error
		else:
			if p == 0 and os.path.exists(unique_base):
				# import_need_param(tags) # code
				return True
			elif p != 0 or not os.path.exists(unique_base):
				# error_read_param(tags) # logging
				return False

	def get_mkv_audio(self, filename, is_log: bool = True):

		self.filename: str = filename

		try:
			assert self.filename.split(".").lower() == "mkv", "Выбран другой формат @get_mkv_audio/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Выбран другой формат @get_mkv_audio/%s" % self.filename)
			raise err
			return []

		# if not self.filename.split(".").lower() == "mkv": # not filename
			# return []

		lst: list = []

		cmd: list = [path_for_queue + "ffprobe.exe", "-loglevel", "error", "-select_streams", "-show_streams",
					 "-show_entries", "stream=index,codec_name:tags=:disposition=", "-of", "csv",
					 filename]  # output_format
		ca: str = "".join([path_for_queue, "atracks.nfo"])

		p = os.system("cmd /c %s > %s" % (" ".join(cmd), ca))  # stream,1,vorbis # stream,2,aac # stream,3,mp3

		if p == 0:

			try:
				with open(ca) as f:
					lst = f.readlines()
			except BaseException as e:
				lst: list = []
				if is_log:
					write_log("debug get_audiotracks[error]", "%s [%s]" % (self.filename, str(e)), is_error=True)
			else:
				if lst:
					try:
						lst = [l.split(",")[-1].lower().strip() for l in lst if l]  # audio_codecs(aac)
					except:
						lst = []

					if lst:
						if is_log:
							write_log("debug get_audiotracks[ok]", "%s" % self.filename)

		if os.path.exists(ca):
			os.remove(ca)

	# input.mkv

	def get_codecs(self, filename, is_log: bool = True) -> list:

		self.filename: str = filename

		lst: list = []

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_codecs/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_codecs/%s" % self.filename)
			raise err
			return lst

		# if not os.path.exists(self.filename): # not filename
			# return lst

		# ffprobe -v error -show_entries stream=codec_name -of csv=p=0:s=x input.m4v
		cmd: list = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "stream=codec_name", "-of",
					 "csv=p=0:s=x", filename]  # output_format
		ci: str = "".join([path_for_queue, "codecs.nfo"])

		p = os.system("cmd /c %s > %s" % (" ".join(cmd), ci))

		if p == 0:

			try:
				with open(ci) as f:
					lst = f.readlines()
			except BaseException as e:
				lst: list = []
				if all((is_log, len(lst) < 2)):
					write_log("debug get_codecs[error]", "%s [%s]" % (self.filename, str(e)), is_error=True)
			else:
				if lst:

					def codecs_gen(lst=lst):
						for l in filter(lambda l: l, tuple(lst)):
							yield l.strip()

					try:
						tmp = list(codecs_gen()) # new(yes_gen)
					# tmp = [l.strip() for l in filter(lambda l: l, tuple(lst))]
					except:
						tmp = []  # old(no_gen) # l.strip() for l in filter(lambda l: l, tuple(lst))
					else:  # finally
						lst = [t.strip() for t in filter(lambda x: x, tuple(tmp))]
						lst = lst[0:2]  # vcodec/acodec
						if len(lst) == 2:
							if is_log:
								# print(lst) # ['h264', 'aac']
								write_log("debug get_codecs[ok]", "%s" % self.filename)

			if os.path.exists(ci):
				os.remove(ci)

		return lst

	def get_width_height(self, filename, is_calc: bool = False, is_log: bool = True, is_def: bool = False,
						 maxwidth: int = 640) -> tuple:

		global job_count

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_width_height/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_width_height/%s" % self.filename)
			raise err
			return (0, 0, False)

		# if not filename or not os.path.exists(self.filename):
			# return (0, 0, False)

		# is_owidth = 0 # is_change = False

		# ffprobe -v error -show_entries stream=width,height -of csv=p=0:s=x input.m4v
		cmd_wh: list = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "stream=width,height", "-of",
						"csv=p=0:s=x", self.filename]  # output_format
		wi: str = "".join([path_for_queue, "wh.nfo"])

		os.system("cmd /c %s > %s" % (" ".join(cmd_wh), wi))

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
				width, height = int(width_height_str.split("x")[0]), int(width_height_str.split("x")[-1])

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

		# is_normal, is_all, is_diff = False, False, False

		# aspect ratio block / start
		try:
			is_hd: bool = (ga.width / ga.height == 16 / 9)
		except:
			is_hd: bool = False

		try:
			is_sd: bool = (ga.width / ga.height == 4 / 3)
		except:
			is_sd: bool = False

		sar = par = dar = ""

		if any((is_hd, is_sd)):
			try:
				sar, par, dar = ga.spd_ar(filename=self.filename, width=ga.width, height=ga.height, is_hd=is_hd, is_sd=is_sd) #calc_ar # is_assert(debug)
			except:
				sar = par = dar = "" # skip_null
			finally: # else
				if any((sar, par, dar)): # if_(sd/hd)
					write_log("debug ar[list]", "%s" % "x".join([self.filename, str(sar), str(par), str(dar)])) # filename/aratio_list
				elif all((not sar, not par, not dar)): # if_not_(sd/hd) #
					try:
						fr = ga.width / ga.height
					except:
						fr = 0

					fr_str = str(float("%0.2f" % fr)) if int(fr) != float("%0.2f" % fr) else str(int(fr)) # float(1.234) -> str(1.23) # float(1.00) -> str(1)

					write_log("debug ar[list][some_null]", "%s" % "x".join([self.filename, str(ga.width), str(ga.height), fr_str])) # filename/width/height/aratio

		# aspect ratio block / end

		try:
			w, h, ar = ga.width_to_ar(width=ga.width, height=ga.height, owidth=640)

			assert w and h and ar, "Ошибка высоты, ширины и маштаба видео @get_width_height/w/h/ar" # is_assert(debug)
		except AssertionError: # as err:
			w = h = ar = 0
			logging.warning("Ошибка высоты, ширины и маштаба видео @get_width_height/%s" % self.filename)
			# raise err
		else:
			if all((w >= h, w, h, ar, is_calc)):  # need_resize(rescale) # 1:1_by_stream_scale

				# is_normal = is_all = True
				# is_diff = False

				# if h % 2 != 0:
				# h += 1
				# if not isinstance(h, int):
				# h = int(h)

				if is_log:
					write_log("debug filename[aratio]", f"file:{self.filename}, scale:{w}x{h}x{round(w / h, 2)}")

				try:
					job_status: str = "%s" % str(
						(ga.width, ga.height, self.filename, "ok")) if ga.width <= maxwidth else "%s" % str(
						(ga.width, ga.height, self.filename, "job"))
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

		del ga

		# debug # @get_width_height

		try:
			assert is_nwidth and is_nheight and width, "Нет данных для обновления маштаба @get_width_height/is_nwidth/is_nheight/width" # is_calc(T/F) # is_assert(debug)
		except AssertionError: # as err:
			logging.warning("Нет данных для обновления маштаба @get_width_height/%s" % self.filename)
			# raise err
			return (int(width), int(height), False)  # logic2 # owidth/oheight/error(no_calc)
		else:
			return (int(is_nwidth), int(is_nheight), width > is_nwidth)  # logic1 # nwidth/nheight/calced(vwidth > owidth)

	def get_length(self, filename) -> int:

		duration_list: list = []
		duration_null: int = 0
		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_length/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_length/%s" % self.filename)
			raise err
			return duration_null

		# if not filename or not os.path.exists(self.filename):
			# return duration_null

		cmd_fd: list = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "format=duration", "-of",
						"compact=p=0:nk=1", self.filename]  # output_format
		fdi: str = "".join([path_for_queue, "duration.nfo"])

		os.system("cmd /c %s > %s" % (" ".join(cmd_fd), fdi))  # 1|und # type1

		with open(fdi, encoding="utf-8") as fdif:
			duration_list = fdif.readlines()

		if os.path.exists(fdi):
			os.remove(fdi)

		try:
			duration_null: int = int(duration_list[0].split(".")[0])  # if duration_list # is_assert(debug)
		except:
			duration_null: int = 0
		finally:
			return duration_null

	# """
	# ffprobe -v error -select_streams v:0 -show_entries stream=level -of default=noprint_wrappers=1 <filepath> # level=50
	# ffprobe -v error -select_streams v:0 -show_entries stream=level -of default=noprint_wrappers=1:nokey=1 <filepath> # 50
	# ffprobe -v error -select_streams v:0 -show_entries stream=profile,level -of default=noprint_wrappers=1 <filepath> # ['profile=Main\n', 'level=30\n', 'profile=LC\n']

	# D:\Multimedia\Video\Big_Films\1947\Eta_zamechatelnaya_jizn(1947).mp4

	def get_profile_and_level(self, filename) -> tuple:

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_profile_and_level/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_profile_and_level/%s" % self.filename)
			raise err
			return ("", "")

		# if not filename or not os.path.exists(self.filename):
			# return ("", "")

		cmd_pl: list = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "stream=profile,level", "-of",
						"default=noprint_wrappers=1", self.filename]  # output_format
		plf: str = "".join([path_for_queue, "profile_and_level.nfo"])

		os.system("cmd /c %s > %s" % (" ".join(cmd_pl), plf))  # profile=High # level=50

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
					pl_list[0].split("=")[-1].lower().strip(), pl_list[1].split("=")[-1].lower().strip())  # [main,30]

	# """

	def get_fps(self, filename, is_calc: bool = False, is_log: bool = True):  # -> any

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_fps/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_fps/%s" % self.filename)
			raise err
			return 0

		# if not self.filename or not os.path.exists(self.filename):
			# return 0

		fps_list: list = []

		# default=noprint_wrappers=1:nokey=1 # 24000/1001
		# default=noprint_wrappers=1 # r_frame_rate=24000/1001

		cmd_fps: list = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "stream=r_frame_rate", "-of",
						 "default=noprint_wrappers=1:nokey=1", self.filename]  # output_format
		fpsf: str = "".join([path_for_queue, "framerate.nfo"])

		#ffprobe.exe -v error -show_entries stream=r_frame_rate -of default=noprint_wrappers=1 input

		os.system("cmd /c %s > %s" % (" ".join(cmd_fps), fpsf))

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
						frame_rate: int = int(r_frame_rate_regex.findall(fl)[0].split("/")[0]) # 24000
						some_value: int = int(r_frame_rate_regex.findall(fl)[0].split("/")[1]) # 1001
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
								if 23 <= fps_value <= 60: # calc_from_23_to_60
									fps_value = int(fps_value)

								if all((23 <= frame_rate <= 60, not fps_value)): # fps_is_from_23_to_60
									fps_value = int(frame_rate)

								if not fps_value:
									if 2 <= len(str(frame_rate)) <= 3: # 23..60(XXX)
										fps_value = float(str(frame_rate)[0:2])
									elif len(str(frame_rate)) == 4: # 2397 / 2997
										fps_value = float(".".join([str(frame_rate)[0:2], str(frame_rate)[2:4]]))

								if not fps_value:
									break

		if os.path.exists(fpsf):
			os.remove(fpsf)

		try:
			fps: int = fps_value if fps_value else 0

			assert fps, "Не могу получить скорость кадров @get_fps/fps" # is_assert(debug)
		except AssertionError as err:
			fps: int = 0
			logging.warning("Не могу получить скорость кадров @get_fps/%s" % self.filename)
			raise err

		try:
			with open(fps_base, encoding="utf-8") as fbf:
				fps_dict = json.load(fbf)
		except: # IOError
			fps_dict = {}

			with open(fps_base, "w", encoding="utf-8") as fbf:
				json.dump(fps_dict, fbf, ensure_ascii=False, indent=2, sort_keys=True)

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

		fpsdict[23] = ["Film; High definition video with NTSC Compatibility",
						"This is 24 FPS slowed down by 99.9% (1000/1001) to easily transfer film to NTSC video. Many HD formats (some SD formats) can record at this speed and is usually preferred over true 24 FPS because of NTSC compatibility."]
		fpsdict[24] = ["Film; High Definition Video",
						"This is the universally accepted film frame rate. Movie theaters almost always use this frame rate. Many high definition formats can record and play back video at this rate, though 23.98 is usually chosen instead (see below)."]
		fpsdict[25] = ["PAL; HD video",
						"The European video standard. Film is sometimes shot at 25 FPS when destined for editing or distribution on PAL video."]
		fpsdict[29] = ["NTSC; HD video",
						"This has been the color NTSC video standard since 1953. This number is sometimes inaccurately referred to as 30 FPS.*"]
		fpsdict[30] = ["HD video, early black and white NTSC video",
						"Some HD video cameras can record at 30 FPS, as opposed to 29.97 FPS. Before color was added to NTSC video signals, the frame rate was truly 30 FPS. However, this format is almost never used today.*"]
		fpsdict[47] = ["Unknown(47)", "FPS 47"]
		fpsdict[48] = ["Unknown(48)", "FPS 48"]
		fpsdict[50] = ["PAL; HD video",
						"This refers to the interlaced field rate (double the frame rate) of PAL. Some 1080i HD cameras can record at this frame rate."]
		fpsdict[59] = ["HD video with NTSC compatibility",
						"HD cameras can record at this frame rate, which is compatible with NTSC video. It is also the interlaced field rate of NTSC video. This number is sometimes referred to as 60 FPS but it is best to use 59.94 unless you really mean 60 FPS."]
		fpsdict[60] = ["HD video",
						"High definition equipment can often play and record at this frame rate but 59.94 FPS is much more common because of NTSC compatibility."]
		fpsdict[71] = ["Unknown(71)", "FPS 71"]
		fpsdict[72] = ["Unknown(72)", "FPS 72"]
		fpsdict[92] = ["Unknown(92)", "FPS 92"]
		fpsdict[96] = ["Unknown(96)", "FPS 96"]
		fpsdict[100] = ["Unknown(100)", "FPS 100"]
		fpsdict[120] = ["Unknown(120)", "people running, nature videography, etc."]
		fpsdict[240] = ["Unknown(240)", "balloons exploding, water splashes, etc."]
		fpsdict[480] = ["Unknown(480)", "skateboard tricks, skiing, surfing, etc"]

		try:
			fps_desc: str = ";".join(fpsdict[fps]) if fpsdict[fps][1] else "[Unknown framerate] [%s] [%s]" % (self.filename, str(fps)) # fps_desc(full/unknown) # filename / fps_value
		except:
			fps_desc: str = "[Unknown framerate] [%s] [%s]" % (self.filename, str(fps)) # filename / fps_value

		if any((fps, fps_desc)):
			fps_dict[self.filename.strip()] = [fps, fps_desc, str(type(fps))] # fps_value / fps_desc(full/unknown) / int(float)

		try:
			if fps:
				write_log("debug fps[calc]", "Файл: [%s], FPS: %s" % (self.filename, str(fps))) # filename / fps_value
		except:
			write_log("debug fps[calc][unknown]", "Файл: [%s], FPS: None" % self.filename) # filename

		try:
			if fps_desc:
				write_log("debug get_fps[description]", "[%s] [%s]" % (fps_desc, self.filename)) # fps_description / filename
		except:
			write_log("debug get_fps[description][unknown]", "[None] [%s]" % self.filename) # filenname

		try:
			if all((fps, fpsdict[fps][0])):
				write_log("debug get_fps[type]", "Framerate type for [%s] [%s]" % (fpsdict[fps][0], self.filename)) # framerate_type / filename
		except:
			write_log("debug get_fps[type][unknown]", "Unknown framerate type for [None] [%s]" % self.filename) # filename

		try:
			if all((fps, fpsdict[fps])):
				write_log("debug fps[data]", ";".join([str(fps), str(fpsdict[fps]), self.filename])) # fps_value / fps_description / filename
		except:
			write_log("debug fps[data][unknown]", ";".join([str(fps), self.filename])) # fps_value / filename

		with open(fps_base, "w", encoding="utf-8") as fbf:
			json.dump(fps_dict, fbf, ensure_ascii=False, indent=2, sort_keys=True)

		return fps  # no_fps(null)

	def calc_vbr(self, width: int = 0, height: int = 0, filename: str = "") -> int:  # fps - r_frame_rate

		self.filename: str = filename

		scales_set = filenames_set = set()

		try:
			fname = self.filename.split("\\")[-1]
		except:
			fname = ""

		vbr_var: list = []

		if any((not width, not height)):
			width, height, is_change = self.get_width_height(
				filename=self.filename)  # pass_1_of_3 # no_calc("find_scale_and_status")

		if not os.path.exists(self.filename) or any(
				(not filename, not width, not height)) or not fname:  # not_exists # if_some_null
			return 0

		# old_vbr
		# motion = 4 if all((height > 720, height)) else 2  # motion={Middle motion:2, High motion:4} # baseline(1), main(2), high(4) # look_like_profile

		owidth, oheight = width, height

		fnames_set = set()  # (5) # scales_set # (5)

		try:
			ar = width / height

			assert ar, "Не верное значения ширины или высоты видео @calc_vbr/ar" # is_assert(debug)
		except AssertionError as err:
			ar = 0
			logging.warning("Не верное значения ширины или высоты видео @calc_vbr/%s" % self.filename)
			raise err

		# width(640) # scale # 1:1

		try:
			width: float = 640 if owidth > 640 else owidth  # 640(if_width_more)

			assert width, "Ширина видео не должно быть пустым @calc_vbr/width" # is_assert(debug)
		except AssertionError as err:
			width: float = 0
			logging.warning("Ширина видео не должно быть пустым @calc_vbr/width")
			raise err

		try:
			height: float = width / ar  # 360p

			assert height, "Высота видео не должно быть пустым @calc_vbr/height" # is_assert(debug)
		except AssertionError as err:
			height: float = 0  # 360p
			logging.warning("Высота видео не должно быть пустым @calc_vbr/height")
			raise err

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
				(width >= height, height)):  # oheight != height # filter(width/"height"/ar)

			try:
				oscale, nscale = "x".join([str(owidth), str(oheight)]), "x".join([str(width), str(height)])
			except:
				oscale = nscale = ""

			if all((not fname in fnames_set, fname)):
				fnames_set.add(fname)

			if not filename in filenames_set:
				filenames_set.add(filename)

				if all((not nscale in scales_set, nscale)):
					scales_set.add(nscale)  # new_scale(logging)

				# print(Style.BRIGHT + Fore.BLUE + "Старый маштаб: %s, новый маштаб: %s, файл: %s" % (oscale, nscale, filename) # ~cmd(with_scale)
				write_log("debug rescale", "Старый маштаб: %s, новый маштаб: %s, файл: %s" % (
					oscale, nscale, filename))  # ~cmd(with_scale)

		# height(360p) # scale # 1:1

		try:
			height: float = 360 if oheight > 360 else oheight  # 360(if_height_more)

			assert height, "Пустое значение высоты видео @calc_vbr/height" # is_assert(debug)
		except AssertionError as err:
			height: float = 0
			logging.warning("Пустое значение высоты видео @calc_vbr/height")
			raise err

		try:
			width: float = height * ar  # 640.000

			assert width, "Пустое значение ширины видео @calc_vbr/width" # is_assert(debug)
		except AssertionError as err:
			width: float = 0
			logging.warning("Пустое значение ширины видео @calc_vbr/width")
			raise err

		if not isinstance(height, int):
			height = int(height)  # 360.000
		if all((height % 2 != 0, height)):
			height += 1  # 360

		if not isinstance(width, int):
			width = int(width)  # 640.000
		if all((width % 2 != 0, width)):
			width += 1  # 640

		try:
			sd_scales = asyncio.run(sd_generate())
		except:
			sd_scales = []

		if sd_scales:
			try:
				tmp = [ss.strip() for ss in sd_scales if "x".join([str(owidth), str(oheight)]) == ss]
			except:
				tmp = []
			else:
				if tmp:
					write_log("debug sd_count[found]", "%s" % str(tmp))
				else:
					write_log("debug sd_count[notfound]", "%s" % "x".join([str(owidth), str(oheight)]))

		try:
			hd_scales = asyncio.run(hd_generate())
		except:
			hd_scales = []

		if hd_scales:
			try:
				tmp = [hs.strip() for hs in hd_scales if "x".join([str(owidth), str(oheight)]) == hs]
			except:
				tmp = []
			else:
				if tmp:
					write_log("debug hd_count[found]", "%s" % str(tmp))
				else:
					write_log("debug hd_count[notfound]", "%s" % "x".join([str(owidth), str(oheight)]))

		if any((not width, not height)) and all((owidth, oheight)):
			width, height = owidth, oheight  # restore(width/height)

		if any((oheight != height, owidth / oheight != width / height)) and all(
				(width >= height, height)):  # owidth != width # filter("width"/height/ar)

			try:
				oscale2, nscale2 = "x".join([str(owidth), str(oheight)]), "x".join([str(width), str(height)])
			except:
				oscale2 = nscale2 = ""

			if all((not fname in fnames_set, fname)):
				fnames_set.add(fname)

			if all((not nscale2 in scales_set, nscale2)):
				scales_set.add(nscale2)  # new_scale(logging)

				# print(Style.BRIGHT + Fore.BLUE + "Старый маштаб: %s, новый маштаб: %s, файл: %s" % (oscale2, nscale2, filename)) # ~cmd(with_scale)

				write_log("debug rescale[2]", "Старый маштаб: %s, новый маштаб: %s, файл: %s" % (
					oscale2, nscale2, filename))  # ~cmd(with_scale)

		try:
			fsize = os.path.getsize(self.filename)
			gl = self.get_length(self.filename)
		except:
			fsize = gl = 0
		else:
			if all((fsize, gl)):

				try:
					# vbr_list = list(vbr_gen()) # new(yes_gen)
					vbr_list: list = [i for i in range(1, height * 2) if
								((i * gl) / 8) * 1000 >= fsize and i % 16 == 0 and i >= height]

					assert vbr_list, "Пустой список частоты видео @calc_vbr/vbr_list" # is_assert(debug)
				except AssertionError: # as err:
					vbr_list: list = []  # old(no_gen) # i for i in range(1, height*2) if ((i * gl) / 8) * 1000 >= fsize and i % 16 == 0 and i >= height
					logging.warning("Пустой список частоты видео @calc_vbr/vbr_list")
					# raise err

				tmp = list(set([vl for vl in filter(lambda x: x, tuple(vbr_list))]))
				vbr_list = sorted(tmp, reverse=False)

				if vbr_list:
					vbr_var.append(max(vbr_list))  # first_vbr

		# second_vbr
		'''
		try:
			fps = self.get_fps(filename=self.filename, is_log=False)
		except:
			fps = 0
		else:
			if all((width, height)):
				if all((height < 720, motion <= 2)):
					vbr_var.append(int(width * height + fps + 8) // 1000)
				elif all((height >= 720, motion == 4)):
					vbr_var.append(int(width * height * fps * motion * 0.07) // 1000)
		'''

		try:
			assert vbr_var, "Пустое значение частоты видео @calc_vbr/vbr_var" # find_some_vbr # is_assert(debug)
		except AssertionError: # as err: # null_vbr
			logging.warning("Пустое значение частоты видео @calc_vbr/%s" % self.filename)
			# raise err
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
	def some_bitrate(self, filename, K: int = 0.25, width: int = 640, height: int = 480, fps: float = 15, ms: int = 1200):
		try:
			sb = (K * width * height * fps) // 1024 # ?kbps # is_assert(debug)
		except:
			sb = 0 # if_error

		return (filename, width, height, fps, ms, sb) # bitrate_params(+result)

	def get_gop(self, filename, fps: int = 0, is_log: bool = True) -> int:

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_gop/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_gop/%s" % self.filename)
			raise err
			return 0

		# if not os.path.exists(self.filename): # not filename
			# return 0

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
					write_log("debug get_gop[error]", "%s [%s]" % (self.filename, str(e)), is_error=True)
			else:
				if is_log:
					write_log("debug get_gop", "# ".join([self.filename, str(self.fps), str(self.gop)]))

		return self.gop

	def calc_cbr(self, filename, abitrate: int = 128) -> int:
		"""
		Constant Bit Rate
		You can target a bitrate with -b:v. This is best used with two-pass encoding. Adapting an example from the x264 encoding guide: your video is 10 minutes (600 seconds) long and an output of 50 MB is desired. Since bitrate = file size / duration:

		(50 MB * 8192 [converts MB to kilobits]) / 600 seconds = ~683 kilobits/s total bitrate
		683k - 128k (desired audio bitrate) = 555k video bitrate
		"""

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @calc_cbr/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @calc_cbr/%s" % self.filename)
			raise err
			return 0

		# if not os.path.exists(self.filename): # not filename
			# return 0

		if not abitrate:
			abitrate = 128

		try:
			fsize: int = os.path.getsize(self.filename)

			assert fsize, "Не могу определить размер файла @calc_cbr/fsize" # is_assert(debug)
		except AssertionError as err:
			fsize: int = 0
			logging.warning("Не могу определить размер файла @calc_cbr/%s" % self.filename)
			raise err
		else:
			fsize /= (1024 ** 2)

		try:
			dur: int = self.get_length(filename=filename)

			assert dur, "Не могу определить длину видео @calc_cbr/dur" # is_assert(debug)
		except AssertionError as err:
			dur: int = 0
			logging.warning("Не могу определить длину видео @calc_cbr/%s" % self.filename)
			raise err

		if any((not fsize, not dur)):
			return 0
		elif all((fsize, dur, abitrate)):
			'''
			f, d, a = 120, 300, 128
			c = int(round(f * 8192 / d, 1)) # 3276K
			c -= a # 3148K
			'''

			try:
				cbr = int(round(fsize * 8192 / dur, 1))
				cbr -= abitrate
			except:
				cbr = 0

			return cbr

	def lossy_audio(self, filename, abitrate: int = 128, channels: int = 5, def_channels: int = 2,
					audio_format: str = "aac") -> int:
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
			assert os.path.exists(self.filename), "Файл отсуствует @lossy_audio/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсуствует @lossy_audio/%s" % self.filename)
			raise err
			return 0

		# if not filename or not os.path.exists(self.filename):
			# return 0

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

			assert abr, "Немогу определить частоту аудио @lossy_audio/abr" # is_assert(debug)
		except AssertionError as err:
			abr: int = 0
			logging.warning("Немогу определить частоту аудио @lossy_audio/%s" % self.filename)
			raise err

		return abr  # -b:a XXXk

	def get_channels(self, filename, is_log: bool = True) -> int:

		self.filename: str = filename

		try:
			assert os.path.exists(self.filename), "Файл отсутствует @get_channels/filename" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Файл отсутствует @get_channels/%s" % self.filename)
			raise err
			return 0

		# if not os.path.exists(self.filename): # not filename
			# return 0

		clcmd: list = [path_for_queue + "ffprobe.exe", "-v", "error", "-show_entries", "stream=channels", "-of",
					   "default=noprint_wrappers=1", "%s" % self.filename]
		clf: str = "".join([path_for_queue, "channels.nfo"])

		os.system("cmd /c %s > %s" % (" ".join(clcmd), clf))  # "channels=2"

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
				print(Style.BRIGHT + Fore.RED + "Ошибка аудио канала для файла %s" % self.filename)
				write_log("debug audio_channel[error]", "Ошибка аудио канала для файла %s" % self.filename)
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
					channel_dict["6"] = f"{str(self.channel)};Hexagonal (Back)/Front/(Side)"
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

				try:
					if channel_dict[str(self.channel)]:
						channel_str = channel_dict[str(self.channel)]  # get_channel_description
				except:
					channel_str = str(self.channel)  # use_channel_number

				if is_log:
					print(Style.BRIGHT + Fore.CYAN + "Аудио канал для файла",
						Style.BRIGHT + Fore.WHITE + "%s [%s]" % (full_to_short(self.filename), channel_str))
					write_log("debug audio_channel", "Аудио канал для файла %s [%s]" % (self.filename, channel_str))

		if os.path.exists(clf):
			os.remove(clf)

		return self.channel

	def get_frame_quality(self, filename, is_log: bool = True) -> float:
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

		try:
			owidth, oheight, is_change2 = self.get_width_height(filename=self.filename, is_calc=False, is_log=False,
																is_def=True)  # frame_by_scale("find_scale_and_status")
		except:
			owidth = oheight = 0
		# is_change2 = False

		if not os.path.exists(filename) or any((not filename, not owidth, not oheight)):  # not_exists # if_some_null
			return 0

		try:
			vbr: int = self.calc_vbr(filename=self.filename, width=owidth, height=oheight)
		except BaseException as e:
			vbr: int = 0

			if is_log:
				write_log("debug calc_vbr[fq]", "%s" % ";".join([self.filename, str(e)]), is_error=True)

		try:
			fps: int = self.get_fps(filename=self.filename, is_log=True)
		except BaseException as e:
			fps: int = 0

			if is_log:
				# "debug get_fps[fq]": "d:\\multimedia\\video\\serials_conv\\Better_Call_Saul\\Better_Call_Saul_02s10e.mp4;dump() missing 1 required positional argument: 'fp'",
				write_log("debug get_fps[fq]", "%s" % ";".join([self.filename, str(e)]), is_error=True)

		try:
			if all((vbr, fps)):
				frame_quality: float = float(str(round(vbr / fps, 2))[0:])  # one_frame_video_no_filesize
		except BaseException as e:
			frame_quality: float = 0

			if is_log:
				write_log("debug fq[error]",
						  "Не могу определить Frame Quality для %s" % ";".join([self.filename, str(e)]), is_error=True)
		else:
			if is_log:
				if frame_quality:

					try:
						fq_value = float(round(frame_quality, 2)) if isinstance(frame_quality, float) else int(frame_quality) # round_or_int
					except:
						fq_value = int(frame_quality)

					write_log("debug fq[filesize]", "Блок Frame Quality по размеру файла для %s составляет %s" % (
						self.filename, str(fq_value))) # frameq_quality = vbr / fps
				else:
					write_log("debug fq[filesize][unknown]", "Блок Frame Quality по размеру файла для %s неизвестен" % self.filename)

		return frame_quality

	# calc # is_run(script), is_zip(backup) # is_pad(unknown)
	def sd_to_hd(self, input_file: str = "", swidth: int = 0, sheight: int = 0, is_run: bool = False,
				 is_pad: bool = True, is_zip: bool = False, prefix: str = "_hd") -> str:

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
				padx += 1 # - -> +
			if not isinstance(padx, int):
				padx = int(padx)

		try:
			is_ok: bool = (sheight == pheight and swidth < pwidth and all(
				(swidth, sheight, pwidth, pheight)))  # difference_height
		except:
			is_ok: bool = False

		output_file = ""

		try:
			start_input_file, *middle_input_file, end_input_file = input_file.split(".")
		except:
			start_input_file = middle_input_file = end_input_file = []
		else:
			sml = (start_input_file, *middle_input_file, end_input_file)
			write_log("debug input_file[parts][sth]", "%s" % str(sml) ) # start(filename) / in_side / end(ext)

		try:
			fext = input_file.split(".")[-1] # sml[-1]
			fnshort = input_file.split(".")[0] + "_%sp%s.%s" % (str(sheight), prefix, fext) # sml[0]
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
			if all((int(swidth) != int(pwidth), int(sheight) == int(pheight), swidth, pwidth)):

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
				if sheight % 2 != 0: # need_up(scale.height) # 16:9 -> 4:3 # debug
					sheight += 1

				if pheight % 2 != 0: # need_up(pad.height) # 16:9 -> 4:3 # debug
					pheight += 1

				if padx % 2 != 0: # need_up(x.pad) # 16:9 -> 4:3 # debug
					padx += 1

				if any((swidth, sheight, pwidth, pheight, padx)):
					write_log("debug sth[scale][pad]", ";".join([str(swidth), str(sheight), str(pwidth), str(pheight), str(padx), input_file]))

				sth_cmd = path_for_queue + "ffmpeg -hide_banner -y -i \"%s\" -threads 2 -c:v libx264 -vf \"scale=%s:%s:flags=lanczos,pad=%s:%s:%s:0\" -threads 2 -c:a copy \"%s\"" % (
					input_file,
					str(int(swidth)), str(int(sheight)), str(int(pwidth)), str(int(pheight)), str(int(padx)),
					output_file)

		# elif all((int(swidth) == int(pwidth), int(sheight) == int(pheight))):
		# sth_cmd = path_for_queue + "ffmpeg -hide_banner -y -i \"%s\" -threads 2 -c:v libx264 -vf \"scale=%s:%s:flags=lanczos\" -threads 2 -c:a copy \"%s\"" % (input_file, str(int(swidth)), str(int(sheight)), output_file)

		except:
			sth_cmd = ""
		else:
			if all((is_run, is_zip in [True, False], sth_cmd, is_ok)):  # script_before_job_start(in)
				# """

				# short_01s01e_xxxp.mp4 > short.zip

				# zip(job/test_when_file_added)

				is_error, zip_name = False, ""

				start_time = time()

				try:
					pcmd = os.system(sth_cmd)
				except BaseException as e:
					is_error = True

					print(Style.BRIGHT + Fore.RED + "Ошибка запуска скрипта для файла %s [%s]" % (input_file, str(e)))
					write_log("debug zip[scale][error][sdtohd]",
							  "Ошибка запуска скрипта для файла %s [%s]" % (input_file, str(e)), is_error=True)
				else:
					is_error = False

					zip_name = crop_filename_regex.sub("", input_file.split("\\")[-1]) + ".zip"

					print(Style.BRIGHT + Fore.GREEN + "Скрипт успешно завершён для файла",
						Style.BRIGHT + Fore.WHITE + "%s" % full_to_short(input_file))
					write_log("debug zip[scale][done][sdtohd]", "Скрипт успешно завершён для файла %s" % input_file)

				end_time = time()

				is_minute = False

				try:
					ms_to_min = abs(end_time - start_time).seconds  # ms -> minute(seconds)
					ms_to_min //= 60
					ms_to_min %= 60
				except:
					ms_to_min = 0
				else:
					if ms_to_min > 60:
						ms_to_min %= 60

						is_minute = True

				write_log("debug ms_to_min[sdtohd]", "%s [%s]" % (ms_to_min, str(is_minute)))

				try:
					if all((pcmd == 0, zip_name, not is_error, "." in output_file,
							is_zip)):  # run(ok)/backup(zip_name)/no_error/some_file(output)/normal_length
						zip_backup = zipfile.ZipFile("".join([path_for_queue, zip_name]),
													 mode="w")  # a(append) / # w(rewrite)

						try:
							zipfiles = zip_backup.namelist()
						except:
							zipfiles = []

						try:
							file = os.path.basename(output_file)
						except BaseException as e:
							write_log("debug zip_backup[file][sdtohd][error]",
									  "%s [%s]" % (str(e), str(datetime.now())), is_error=True)
						else:
							try:
								if not file in zipfiles:
									# first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)
									zip_backup.write(output_file, compress_type=zipfile.ZIP_DEFLATED)
							except:
								# first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)
								zip_backup.write(output_file, compress_type=zipfile.ZIP_DEFLATED)

					# process_zip(sth_cmd, input_file, is_zip)
				except BaseException as e:
					write_log("debug zip[error][sdtohd]", "Ошибка архивации файла %s [%s]" % (input_file, str(e)), is_error=True)
				else:
					if os.path.exists("".join([path_for_queue, zip_name])):
						if is_zip:
							zip_backup.close()

					if os.path.exists(output_file) and "." in output_file:
						if is_zip:
							os.remove(output_file)

					if any((is_run, is_zip)):
						print(Style.BRIGHT + Fore.CYAN + "Архив %s готов и файл %s добавлен или обновлён за %d мин." % (
							zip_name, full_to_short(output_file), ms_to_min))
						write_log("debug zip[done][sdtohd]",
								  "Архив %s готов и файл %s добавлен или обновлён за %d мин." % (
									  zip_name, output_file, ms_to_min))

		# backup(delete/if_ok)
		# """

		# @sws_flags %s # -vf flags=%s
		# fast_bilinear / bilinear / bicubic / experimental / neighbor / area / bicublin / gauss / sinc / >lanczos< / spline / "print_info" / accurate_rnd / full_chroma_int / full_chroma_inp / bitexact

		try:
			if sth_cmd:
				write_log("debug sdtohd", "%s [%s]" % (input_file, sth_cmd))
			elif not sth_cmd:  # maybe_ready
				write_log("debug sdtohd[nocmd]", "%s [%s]" % (input_file, str(datetime.now())))

		except:
			sth_cmd = ""


		if not pwidth:  # not pheight / not padx:
			return ""

		return sth_cmd


	# calc # is_run(script), is_zip(backup) # is_pad(.T.=sd_bars/.F.=hd_rescale)
	def hd_to_sd(self, input_file: str = "", swidth: int = 0, sheight: int = 0, is_run: bool = False,
			 is_pad: bool = True, is_zip: bool = False, prefix: str = "_sd") -> str:

		self.filename: str = input_file

		# ffmpeg -y -i input_file -vf "scale=640:360:flags=lanczos,pad=640:480:0:60" -c:a copy output_file

		pwidth = swidth

		# another_aratio(debug/test) # without_all_scales
		# if (swidth / sheight) != (4/3):

		try:
			pheight: float = pwidth / (4 / 3)
		except:
			pheight: float = 0

		if ((pheight % 2 != 0, pheight)):
			pheight -= 1
		if not isinstance(pheight, int):
			pheight = int(pheight)

		try:
			pady: int = abs(pheight - sheight) // 2
		except:
			pady: int = 0
		else:
			if pady % 2 != 0:
				pady += 1 # - -> +
			if not isinstance(pady, int):
				pady = int(pady)

		try:
			is_ok: bool = (swidth == pwidth and sheight <= pheight and all(
			(swidth, sheight, pwidth, pheight)))  # difference_height
		except:
			is_ok: bool = False

		output_file = ""

		try:
			start_input_file, *middle_input_file, end_input_file = input_file.split(".")
		except:
			start_input_file = middle_input_file = end_input_file = []
		else:
			sml = (start_input_file, *middle_input_file, end_input_file)
			write_log("debug input_file[parts][hts]", "%s" % str(sml) ) # start(filename) / in_side / end(ext)

		try:
			fext = input_file.split(".")[-1] # sml[-1]
			fnshort = input_file.split(".")[0] + "_%sp%s.%s" % (str(sheight), prefix, fext) # sml[0]
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
			if all((int(swidth) == int(pwidth), int(pheight) != int(sheight), sheight, pheight)):

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
				if sheight % 2 != 0: # need_up(scale.height) # 4:3 -> 16:9 # debug
					sheight += 1

				if pheight % 2 != 0: # need_up(pad.height) # 4:3 -> 16:9 # debug
					pheight += 1

				if pady % 2 != 0: # need_up(y.pad) # 4:3 -> 16:9 # debug
					pady += 1

				if any((swidth, sheight, pwidth, pheight, pady)):
					write_log("debug hts[scale][pad]", ";".join([str(swidth), str(sheight), str(pwidth), str(pheight), str(pady), input_file]))

				hts_cmd = path_for_queue + "ffmpeg -hide_banner -y -i \"%s\" -threads 2 -c:v libx264 -vf \"scale=%s:%s:flags=lanczos,pad=%s:%s:0:%s\" -threads 2 -c:a copy \"%s\"" % (
					input_file,
					str(int(swidth)), str(int(sheight)), str(int(pwidth)), str(int(pheight)), str(int(pady)),
					output_file)

				# if all((int(swidth) == int(pwidth), int(sheight) == int(pheight))):
					# hts_cmd = path_for_queue + "ffmpeg -hide_banner -y -i \"%s\" -threads 2 -c:v libx264 -vf \"scale=%s:%s:flags=lanczos\" -threads 2 -c:a copy \"%s\"" % (input_file, str(int(swidth)), str(int(sheight)), output_file)
		except:
			hts_cmd = ""
		else:
			if all((is_run, is_zip in [True, False], hts_cmd, is_ok)):  # script_before_job_start(in)
				# """
				# short_01s01e_xxxp.mp4 > short.zip

				# zip(job/test_when_file_added)

				is_error, zip_name = False, ""

				start_time = time()

				try:
					pcmd = os.system(hts_cmd)
				except BaseException as e:
					is_error = True

					print(Style.BRIGHT + Fore.RED + "Ошибка запуска скрипта для файла %s [%s]" % (input_file, str(e)))
					write_log("debug zip[scale][error][hdtosd]",
					  "Ошибка запуска скрипта для файла %s [%s]" % (input_file, str(e)), is_error=True)
				else:
					is_error = False

					zip_name = crop_filename_regex.sub("", input_file.split("\\")[-1]) + ".zip"

					print(Style.BRIGHT + Fore.GREEN + "Скрипт успешно завершён для файла",
						Style.BRIGHT + Fore.WHITE + "%s" % full_to_short(input_file))
					write_log("debug zip[scale][done][hdtosd]", "Скрипт успешно завершён для файла %s" % input_file)

				end_time = time()

				is_minute = False

				try:
					ms_to_min = abs(end_time - start_time).seconds  # ms -> minute(seconds)
					ms_to_min //= 60
					ms_to_min %= 60
				except:
					ms_to_min = 0
				else:
					if ms_to_min > 60:
						ms_to_min %= 60

						is_minute = True
						write_log("debug ms_to_min[hdtosd]", "%s [%s]" % (ms_to_min, str(is_minute)))

				try:
					if all((pcmd == 0, zip_name, not is_error, "." in output_file,
						is_zip)):  # run(ok)/backup(zip_name)/no_error/some_file(output)/normal_length
						zip_backup = zipfile.ZipFile("".join([path_for_queue, zip_name]), mode="w")  # a(append) / # w(rewrite)

						try:
							zipfiles = zip_backup.namelist()
						except:
							zipfiles = []

						try:
							file = os.path.basename(output_file)
						except BaseException as e:
							write_log("debug zip_backup[file][hdtosd][error]",
							  "%s [%s]" % (str(e), str(datetime.now())), is_error=True)
						else:
							try:
								if not file in zipfiles:
									zip_backup.write(output_file,
											 compress_type=zipfile.ZIP_DEFLATED)  # first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)
							except:
								zip_backup.write(output_file,
										 compress_type=zipfile.ZIP_DEFLATED)  # first parameter is filename and second parameter is filename in archive by default filename will taken if not provided # one_file(no_for)

					# process_zip(hts_cmd, input_file, is_zip)
				except BaseException as e:
					write_log("debug zip[error][hdtosd]", "Ошибка архивации файла %s [%s]" % (input_file, str(e)), is_error=True)
				else:
					if os.path.exists("".join([path_for_queue, zip_name])) and is_zip:
						zip_backup.close()

					if os.path.exists(output_file) and "." in output_file and is_zip:
						os.remove(output_file)

					if any((is_run, is_zip)):
						print(Style.BRIGHT + Fore.CYAN + "Архив %s готов и файл %s добавлен или обновлён за %d мин." % (
						zip_name, output_file, ms_to_min))
						write_log("debug zip[done][sdtohd]",
						  "Архив %s готов и файл %s добавлен или обновлён за %d мин." % (
							  zip_name, output_file, ms_to_min))

		# backup(delete/if_ok)
		# """

		# @sws_flags %s # -vf flags=%s
		# fast_bilinear / bilinear / bicubic / experimental / neighbor / area / bicublin / gauss / sinc / >lanczos< / spline / "print_info" / accurate_rnd / full_chroma_int / full_chroma_inp / bitexact

		try:
			if hts_cmd:
				write_log("debug hdtosd", "%s [%s]" % (input_file, hts_cmd))
			elif not hts_cmd:  # maybe_ready
				write_log("debug hdtosd[nocmd]", "%s [%s]" % (input_file, str(datetime.now())))
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

	def __init__(self, seconds: int = 2):
		self.seconds = seconds

	def seconds_to_time(self, seconds: int) -> tuple:

		try:
			assert seconds, "Не указано время в ms для конвертации @seconds_to_time/seconds" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Не указано время в ms для конвертации @seconds_to_time/seconds")
			raise err
			return (0, 0, 0, 0)

		# if not seconds:
			# return (0, 0, 0, 0)

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
			seconds -= (days * seconds_in_day)
			hours = seconds // seconds_in_hour
			seconds -= (hours * seconds_in_hour)
			minutes = seconds // seconds_in_minute
			seconds -= (minutes * seconds_in_minute)
		except:
			days = hours = minutes = seconds = 0
		finally:
			dhms: tuple = (days, hours, minutes, seconds)

			return dhms  # if_normal_then_data

	# diff_date's -> hh:mm:ss

	def seconds_to_hms(self, date1, date2) -> tuple:

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
			assert delta.days >= 0 and delta.seconds >= 0, "Нет количества дней или секунд @seconds_to_hms/delta/*" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Нет количества дней или секунд @seconds_to_hms/delta/*")
			raise err
			return (0, 0, 0, 0)
		else:
			# print(delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60)
			return (delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60)

	def sleep_with_count(self, ms: int = 2, is_log: bool = True): # ms = 2 # is_ms_not_global
		"""Подсчитать сколько времени задержка"""

		# get_default
		try:
			# self.ms = self.seconds if self.seconds else 2 # try_load_seconds_to_puase(default~2ms)
			self.ms = ms if ms else 2 # try_load_seconds_to_puase(default~2ms)
		except:
			self.ms = 2 # if_error_default_only

		stime = datetime.now()

		sleep(self.seconds * 60) # debug

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
				dd, hh, mm, _ = self.seconds_to_time(seconds=total_time) # ss -> _
				if any((dd, hh, mm)):
					if is_log:
						print(Style.BRIGHT + Fore.WHITE + "debug time",
							  "Задержка сработала на : %d дн., %d ч., %d м." % (dd, hh, mm), end="\n")


# 8
class MyString:

	# __slots__ = ["maintext", "endtext", "count", "kw"]

	def __init___(self): # maintext, endtext, count, kw
		# self.maintext = maintext
		# self.endtext = endtext
		# self.count = count
		# self.kw = kw
		pass

	def last2str(self, maintxt: str = "", endtxt: str = "", count: int = 1, kw: str = "") -> str: # hide_args_use_slots
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
		if maintxt: # self.maintext
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
			isDebug: bool = (not e == None or len(e) == 0)
			if isDebug == True:
				write_log("debug padeji", str(e), is_error=True)

			def_dict = {}

			with open(padeji_base, "w", encoding="utf-8") as jf:
				json.dump(def_dict, jf, ensure_ascii=False, indent=4)
		# else:
		# print(Fore.WHITE + "Справочник падежей успешно загружен")

		# save_data
		if not def_dict:
			def_dict = {
				"1": ["файлов", "секунд", "часов", "минут", "процесов", "строк", "записей", "элементов", "сезонов",
					  "процентов", "дисков", "папок", "недель", "дней", "устройств", "задач", "штуки"],
				"2": ["файл", "секунда", "час", "минута", "процес", "строка", "запись", "элемент", "сезон", "процент",
					  "диск", "папка", "неделя", "день", "устройство", "задача", "штука"],
				"3": ["файла", "секунды", "часа", "минуты", "процеса", "строки", "записи", "элемента", "сезона",
					  "процента", "диска", "папки", "недели", "дня", "устройства", "задачи", "штуку"]
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
		keyword_regex = re.compile("(" + kw + ")", re.I) # ?self.kw

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

		self.endtxt = endtxt # self.endtext

		cnt = count # ?self.count
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


# @log_error
def clear_null_data_list(lst: list = []) -> list:
	"""Как удалить пустые строки из массива в python?"""

	temp: list = []

	try:
		assert lst, "Пустой список @clear_null_data_list/lst" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Пустой список @clear_null_data_list/lst")
		raise err
		return temp

	# if not lst:
		# return temp

	try:
		lst = list(filter(len, lst))
	except:
		lst = []
	finally:
		return lst


# --- Filter files ---

# folders_to_move
# @log_error
async def folders_filter(lst=[], folder: str = "", is_Rus: bool = False, is_Ukr: bool = False, is_log: bool = True) -> list:

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
		full_folder: list = ["".join([main_folder, fl]) for fl in folder_list if
							os.path.exists("".join([main_folder, fl]))]
	except BaseException as e:
		full_folder: list = []  # old(no_gen) # "".join([main_folder, fl]) for fl in folder_list if os.path.exists("".join([main_folder, fl]))
		if is_log:
			write_log("debug move[folder][error][1]", "Ошибка генерации списка основных папок [%s]" % str(e), is_error=True)

	if full_folder:
		tmp = list(set([ff.strip() for ff in filter(lambda x: x, tuple(full_folder))]))
		full_folder = sorted(tmp, reverse=False)

		if all((not is_Rus, not is_Ukr)):
			if is_log:
				write_log("debug move[folder][1]", "Найдено %d основных папок [Eng]" % len(full_folder))
		elif any((is_Rus, is_Ukr)):
			if is_log:
				write_log("debug move[folder][1]", "Найдено %d основных папок [Eur]" % len(full_folder))

	# --- save_folders_and_files(text/json) / null_folders / end ---

	try:
		# folder_with_files = list(files_from_folders_gen()) # new(yes_gen)
		folder_with_files: list = [ff.strip() for ff in filter(lambda x: os.path.exists(x), tuple(full_folder)) if
								all((len(os.listdir(ff)) >= 1, ff))]  # 1_description # >1_videos
	except BaseException as e:
		folder_with_files: list = []  # old(no_gen) # ff.strip() for ff in filter(lambda x: os.path.exists(x), tuple(full_folder)) if all((len(os.listdir(ff)) >= 1, ff))
		# Ошибка генерации списка папок с файлами [[WinError 267] Неверно задано имя папки: 'd:\\multimedia\\video\\serials_conv\\01s01e.txt']
		write_log("debug move[folder][error][2]", "Ошибка генерации списка папок с файлами [%s]" % str(e), is_error=True)
	else:
		# if folder_with_files:
		tmp = list(set([fwf.strip() for fwf in filter(lambda x: x, tuple(folder_with_files))]))
		folder_with_files = sorted(tmp, reverse=False)

		# if folder_with_files:
		if all((not is_Rus, not is_Ukr)):
			if is_log:
				write_log("debug move[folder][2]", "Найдено %d папок с файлами [Eng]" % len(folder_with_files))
		elif any((is_Rus, is_Ukr)):
			if is_log:
				write_log("debug move[folder][2]", "Найдено %d папок с файлами [Eur]" % len(folder_with_files))

	try:
		folder_without_files: list = [ff.strip() for ff in filter(lambda x: os.path.exists(x), tuple(full_folder)) if
									all((len(os.listdir(ff)) == 0, ff))]  # no_files
	except BaseException as e:
		folder_without_files: list = []
		write_log("debug move[folder][error][3]", "Ошибка генерации списка папок без файлов [%s]" % str(e), is_error=True)
	else:
		# if folder_without_files:
		tmp = list(set([fwf.strip() for fwf in filter(lambda x: x, tuple(folder_without_files))]))
		folder_without_files = sorted(tmp, reverse=False)

		# if folder_without_files:
		if is_log:
			write_log("debug move[folder][3][no_files]", "Нет файлов в %d папках" % len(folder_without_files))

	# --- save_folders_and_files(text/json) ---

	# @vr_folder / @vr_files / debug/test

	files: list = []

	def folder_gen2(folder_list=folder_list):
		for fl in folder_list:
			if os.path.exists("".join([main_folder, fl])):
				yield "".join([main_folder, fl])

	try:
		# full_folder2 = list(folder_gen2()) # new(yes_gen)
		full_folder2: list = ["".join([main_folder, fl]) for fl in folder_list if
							os.path.exists("".join([main_folder, fl]))]
	except BaseException as e:
		full_folder2: list = []

		if is_log:
			write_log("debug move[folder][error][2]", "Ошибка генерации файлов для фильтрации [%s]" % str(e), is_error=True)

	if full_folder2:
		temp = list(set(full_folder2))
		full_folder2 = sorted(temp, reverse=False)
		try:
			# tmp = list(ff2_gen()) # new(yes_gen)
			tmp: list = [ff2.strip() for ff2 in filter(lambda x: os.path.exists(x), tuple(full_folder2))]
		except:
			tmp: list = []  # old(no_gen) # ff2.strip() for ff2 in filter(lambda x: os.path.exists(x), tuple(full_folder2))

		tmp2 = list(set([ff2.strip() for ff2 in filter(lambda x: x, tuple(full_folder2))]))
		full_folder2 = sorted(tmp2, reverse=False)

		with unique_semaphore:
			for ff2 in full_folder2:

				if not full_folder2:  # no_data
					break

				# try:
					# fname = ff2.split("\\")[-1].strip()
				# except:
					# fname = ""

				if os.path.exists(ff2):
					try:
						myfiles = os.listdir(ff2)
					except:
						myfiles = []
					else:
						try:
							# temp = list(fullname_gen()) # new(yes_gen)
							temp: list = ["\\".join([ff2, mf]).strip() for mf in filter(lambda x: x, tuple(myfiles))]
						except:
							temp: list = []  # old(no_gen) # "\\".join([ff2, mf]).strip() for mf in filter(lambda x: x, tuple(myfiles))

						tmp = list(set([t.strip() for t in filter(lambda x: x, tuple(temp))]))
						files += sorted(tmp, reverse=False)

		try:
			if files:
				temp = list(set(files))  # filter_unique_filenames
				files = sorted(temp, reverse=False)

				# current_files(dict)
				try:
					with open(vr_files, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except: # IOError
					ff_last = {}

					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(ff_last, vff, ensure_ascii=False, indent=2, sort_keys=True)

				# current_jobs(list)
				# ff_dict = {} # debug/test

				try:
					ff_dict = {f.strip(): os.path.getsize(f) for f in filter(lambda x: os.path.exists(x), tuple(files))
							   if all((video_ext_regex.findall(f.split("\\")[-1]), f))}  # {filename: filesize}
				except:
					ff_dict = {}
				else:
					if all((len(ff_dict) >= 0, ff_last)):  # null_or_some # last_files
						ff_dict.update(ff_last)

				if ff_dict:
					ff_dict = {k: v for k, v in ff_dict.items() if os.path.exists(k)}  # check_exist_folder

					with open(vr_files, "w", encoding="utf-8") as vff:
						# vff.writelines("%s\n" % f.strip() for f in files) # save_files(txt) # need_json
						json.dump(ff_dict, vff, ensure_ascii=False, indent=2, sort_keys=True) # save_list_files(exists) # is_files

		except BaseException as e:
			if is_log:
				write_log("debug vr_files[error]", "%s [%s]" % (str(e), str(datetime.now())), is_error=True)
		else:
			if is_log:
				write_log("debug vr_files", "ok [%s]" % str(datetime.now()))

		def folder_gen21(files=files):
			for f in filter(lambda x: os.path.exists("\\".join(x.split("\\")[0:-1])), tuple(files)):
				if all((os.listdir("\\".join(f.split("\\")[0:-1])), f)):
					yield "\\".join(f.split("\\")[0:-1]).strip()

		# if is_Rus:
			# pass # trouble_rus_rename(project_name = r"C:\Downloads\new\13_klinicheskaya_01s01e.mp4", dest_folder = r"D:\Multimedia\Video\Serials_Europe\13_Klinicheskaya_Rus")

		# hidden
		# """
		try:
			# full_folder2 = list(folder_gen21()) # new(yes_gen) # is_all_folders(with/without)_files_for_descriptions
			full_folder2: list = ["\\".join(f.split("\\")[0:-1]).strip() for f in filter(lambda x: os.path.exists("\\".join(x.split("\\")[0:-1])), tuple(files)) if all((len(os.listdir("\\".join(f.split("\\")[0:-1]))) >= 0, f))]
		except:
			full_folder2: list = []  # old(no_gen) # "\\".join(f.split("\\")[0:-1]).strip() for f in filter(lambda x: os.path.exists("\\".join(x.split("\\")[0:-1])), tuple(files)) if all((os.listdir("\\".join(f.split("\\")[0:-1])), f))

		tmp = [ff2.strip() for ff2 in filter(lambda x: x, tuple(full_folder2))]
		full_folder2 = sorted(tmp, reverse=False)

		try:
			if full_folder2:
				temp = list(set(full_folder2))

				full_folder2 = sorted(temp, reverse=False)
				# full_folder2 = sorted(temp, key=len, reverse=False)

				try:
					with open(vr_folder, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except: # IOError
					ff_last = {}

					with open(vr_folder, "w", encoding="utf-8") as vff:
						json.dump(ff_last, vff, ensure_ascii=False, indent=2, sort_keys=True)
				else:
					# pass_1_of_2(not_exists_folders)
					try:
						check_folders: list = [ff_check.strip() for ff_check in
										 filter(lambda x: x, tuple(list(ff_last.keys()))) if
										 not os.path.exists(ff_check)]  # restore_folders(clear_without_desc)
					except:
						check_folders: list = []
					else:
						for cf in check_folders:

							if not check_folders:
								break

							if not cf:
								continue

							if not os.path.exists(cf):
								write_log("debug check_folders", "Папка %s не найдена [%s]" % (
									cf, ff_last[cf]))  # ; ff_last[cf] # fullpath(short_foldername)

					tmp = list(set(check_folders))

					check_folders = sorted(tmp, reverse=False)
					# check_folders = sorted(tmp, key=len, reverse=False)

					check_f_status = ";".join(check_folders) if check_folders else ""

					write_log("debug check_folders", "%s" % check_f_status)

					# pass_2_of_2(need_true_short_rename_is_ignorecase) # get_without_seasepis_and_extension
					try:
						check_files: list = [crop_filename_regex.sub("", f.split("\\")[-1]) for ff_check in filter(lambda x: x, tuple(list(ff_last.values()))) for f in filter(lambda x: os.path.exists(x), tuple(files)) if crop_filename_regex.sub("", f.split("\\")[-1]) in ff_check and crop_filename_regex.sub("", f.split("\\")[-1]).lower() < len(ff_check.lower())]
					except:
						check_files: list = []

					tmp = list(set(check_files))

					check_files = sorted(tmp, reverse=False)
					# check_files = sorted(tmp, key=len, reverse=False)

					check_f_status = ";".join(check_files) if check_files else ""

					write_log("debug check_files", "%s" % check_f_status)

				# ff_dict: dict = {} # debug/test

				# {folder:short_folder(for_filter)}
				try:
					ff_dict = {ff2.strip(): ff2.split("\\")[-1].strip() for ff2 in filter(lambda x: os.path.exists(x), tuple(full_folder2)) if all((os.listdir(ff2), ff2))}
				except:
					ff_dict = {}
				else:
					if all((len(ff_dict) >= 0, ff_last)):  # null_or_some # last_files
						ff_dict.update(ff_last)

				if ff_dict:
					ff_dict = {k: v for k, v in ff_dict.items() if os.path.exists(k)}  # check_exist_files

					with open(vr_folder, "w", encoding="utf-8") as vff:
						# vff.writelines("%s\n" % ff2.strip() for ff2 in full_folder2) # save_folders(txt) # need_json
						json.dump(ff_dict, vff, ensure_ascii=False, indent=2, sort_keys=True) # save_list_files(exists) # is_folder

						# some_shortfolders_or_null_list # no_keys_only_values

						sfolders = sorted(list(set(ff_dict.values())), reverse=False) if temp else []
						# sfolders = sorted(list(set(ff_dict.values())), key=len, reverse=False) if temp else []

				if len(sfolders) <= 20:
					print(sfolders[0:len(sfolders)], "==>", "Папки с описаниями и файлами")
					write_log("debug fullfolders[names]", "%s" % ";".join(sfolders[0:len(sfolders)]))
				elif len(sfolders) > 20:
					print(sfolders[0:20], "==>", "Папки с описаниями и файлами")
					write_log("debug fullfolders[names]", "%s" % ";".join(sfolders[0:20]))
				else:
					write_log("debug fullfolders[null]", "Нет папок с описаниями и файлами")

				# print(sfolders, "==>", "Папки с описаниями и файлами")
				# write_log("debug fullfolders[names]", "%s" % ";".join(sfolders))

				# try_save_from_trends_no_by_current_jobs
				try:
					with open(trends_base, encoding="utf-8") as tbf:
						trends_dict = json.load(tbf)
				except:
					trends_dict = {}

				first_len = second_len = 0

				# filter_trends_by_today
				try:
					first_len: int = len(trends_dict)
					trends_dict = {k: v for k, v in trends_dict.items() if str(datetime.today()).split(" ")[0].strip() >= v.split(" ")[0].strip()} # fitler_by_date(some_trends)
				except:
					trends_dict = {k: v for k, v in trends_dict.items() if all((k, v))} # all_data_exists(all_trends)
				finally:
					second_len: int = len(trends_dict)

				if all((second_len, second_len <= first_len)):  # find_today_jobs(or_skip)
					tmp = list(set([k.strip() for k, v in trends_dict.items() for k2, v2 in trends_dict.items() if
								all((v, v2, v > v2))]))

					sfolders = sorted(tmp, reverse=False)  # sort_no_need(some_data)

				with open(short_folders, "w", encoding="utf-8") as sff:
					sff.writelines("%s\n" % sf.strip() for sf in filter(lambda x: x, tuple(sfolders)))  # current_folders(short)

		except BaseException as e:
			if is_log:
				write_log("debug vr_folder[error]", "%s [%s]" % (str(e), str(datetime.now())), is_error=True)

		else:
			if is_log:
				write_log("debug vr_folder", "ok [%s]" % str(datetime.now()))
	# """

	# need_check_full_folder_by_short(re.compile)
	folders_to_move: list = []

	job_file_set = set()

	prc: int = 0
	prc_brf: int = 0
	cnt: int = 0
	max_cnt: int = len(lst)

	# pass_1_of_2
	for l in lst:
		for ff in full_folder:

			try:
				fname = l.split("\\")[-1].strip()  # short_job(src)
				short_file = crop_filename_regex.sub("", fname)  # short_job(src)
				folder = ff.split("\\")[-1].strip()  # folder_only

				new_file = short_folder = ""

				if lang_regex.findall(folder) and any((is_Rus, is_Ukr)):  # crop_lang_from_folder
					short_folder = lang_regex.sub("", folder)

				# len(short_folder) < len(full_folder) # eur(filter) # Igry < Igry_Rus
				try:
					is_Rus_filter = (folder[0:len(short_folder)] == short_file and all(
					(len(folder[0:len(short_folder)]) < len(folder), folder, short_folder, short_file)))
				except:
					is_Rus_filter = False

				# len(full_folder) == len(short_folder) # eng(filter) # Games == Games
				try:
					is_Eng_filter = (folder[0:len(short_file)] == short_file and all(
					(len(folder) == len(folder[0:len(short_file)]), folder, short_file)))
				except:
					is_Eng_filter = False

				# other_file = "\\".join([ff, fname])

				if any((is_Rus_filter,
					is_Eng_filter)):  # and other_file.split("\\")[-2] == fname[0:len(other_file.split("\\")[-2])] # Rus/Eng # Compare_short_filename
					try:
						if all((not is_Rus, not is_Ukr, not short_folder)) and os.path.exists(ff):  # english
							new_file = "\\".join([ff, fname])
						elif any((is_Rus, is_Ukr)) and os.path.exists(ff):  # europe
							if all((short_folder, len(short_folder) < len(folder))):
								new_file = "\\".join([ff, fname])
					except BaseException as e:
						new_file = ""  # if_unknown_logic

						if os.path.exists(ff):  # all_languages(error)
							if is_log:
								print(Style.BRIGHT + Fore.RED + "Файл %s прочитан с ошибкой %s" % (l, str(e)))
								write_log("debug folder[short][error]",
									  "%s [%s]" % ("\\".join([ff, fname]), str(e)), is_error=True)

					else:
						if new_file and os.path.exists(ff):  # all_languages(no_error)
							if is_log:
								print(Style.BRIGHT + Fore.CYAN + "Файл",
									Style.BRIGHT + Fore.WHITE + "%s" % full_to_short(new_file),
									Style.BRIGHT + Fore.CYAN + "успешно прочитан")
								write_log("debug folder[short]", "%s" % "\\".join([ff, fname]))

				# elif all((not is_Rus_filter, not is_Eng_filter)):

				# write_log("debug folder[nolang]", "Нет языка для %s" % "\\".join([ff, fname]))

				if new_file:
					fname2 = new_file.split("\\")[-1].strip()  # short_job(dst)
					short_file2 = crop_filename_regex.sub("", fname2)  # short_job(dst)

			except BaseException as e:
				fname = fname2 = short_file = short_file2 = folder = new_file = ""

				if is_log:
					write_log("debug param[error]", "Файл: %s, ошибка: %s" % (l, str(e)), is_error=True)

			else:
				try:
					equal_short_filenames = (fname == fname2 and all((fname, fname2)))
				except:
					equal_short_filenames = False

				try:
					equal_short_template = (short_file == short_file2 and all((short_file, short_file2)))
				except:
					equal_short_template = False

				try:
					filter_path_by_length = (folder[0:len(short_file)] == short_file and all((len(folder) == len(
					folder[0:len(short_file)]), folder, short_file, not short_folder)))  # if_english
				except:
					filter_path_by_length = False
				else:
					if not filter_path_by_length:
						filter_path_by_length = (folder[0:len(short_folder)] == short_file and all((
								len(folder[0:len(short_folder)]) < len(folder), folder, short_file, short_folder)))  # if_europe

			# local(exists) / equal_short_filenames / equal_short_template / filter_path_by_length(template)
			if os.path.exists(l):
				if all((equal_short_filenames, equal_short_template, filter_path_by_length)):
					if all((not new_file in job_file_set, new_file)):

						cnt += 1

						prc = cnt / max_cnt
						prc *= 100

						if prc == prc_brf:
							if is_log:
								print(Style.BRIGHT + Fore.WHITE + "Обработанно %d процента данных. [%s]" % (
									int(prc), fname2))

							prc_brf = int(prc)

						job_file_set.add(new_file)

						try:
							filename_by_template = (
									fname[0:len(short_file) + 1] == fname2[0:len(short_file2) + 1])
						except:
							filename_by_template = False

						# ["_", "("] # tv_series/cinema # l[0] <= new_file[0] # all_drives
						if all((l[0] < new_file[0], filename_by_template)):  # difference_drive
							full_path = ff + "\\" + short_file

							# "\\".join(new_file.split("\\")[0:-1]) # path_without_file

							# debug/test
							season_regex = re.compile(r"_[\d+]{2,4}s", re.M)  # M(atchCase)
							folder_regex = re.compile(r"\([\d+]{4}\)")

							# ff(full_folder_path_no_filename) -> fname(short_filename_without_path) # debug/test

							try:
								if season_regex.findall(fname):
									write_log("debug folder[season]",
											  "%s [%s]" % (l, ",".join(season_regex.findall(fname))))
								if folder_regex.findall(fname):
									write_log("debug folder[cinema]",
											  "%s [%s]" % (l, ",".join(folder_regex.findall(fname))))
							except BaseException as e:
								write_log("debug folder[error]", "Ошибка обработки папки [%s]" % str(e), is_error=True)

							try:
								scan_files: list = ["\\".join([ff, ld]).strip() for ld in os.listdir(ff) if
														os.path.exists("\\".join([ff, ld]))]  # video_regex.findall(ld)
							except BaseException as e:
								scan_files: list = []
								write_log("debug scanfiles[error]", "%s" % str(e), is_error=True)

							if "txt" in scan_files:  # have_description

								# @description.json # (.*)\s\(.*\)\s([\d+]{1,2}\s[A-Za-z]{3}\s[\d+]{4}) # "rus" (0) / eng (1) / "date" (2)

								desc_regex = re.compile(r"(.*)\s\(.*\)\s([\d+]{1,2}\s[A-Za-z]{3}\s[\d+]{4})")

								try:
									desc_filter: list = [(desc_regex.findall(sf)[0], desc_regex.findall(sf)[1],
															desc_regex.findall(sf)[2]) for sf in scan_files if
															sf.count("txt") > 0 and desc_regex.findall(sf) and
															len(desc_regex.findall(sf)) >= 2]
								except:
									desc_filter: list = []
								finally:
									if sf:
										write_log("debug desc_filter!", "Parse description for %s" % sf)

								if desc_filter:
									for df in desc_filter:  # tuple -> str
										print(Style.BRIGHT + Fore.WHITE + "%s" % str(df))  # print_for_json_data_from_tuple
										write_log("debug desc_filter", "%s" % str(df))  # logging_for_json_data_from_tuple

								tmp = list(set([sf.strip() for sf in
									   filter(lambda x: video_regex.findall(sf.split("\\")[-1]),
											  tuple(scan_files))]))

								scan_files = sorted(tmp, reverse=False)

								write_log("debug scanfiles", ";".join(scan_files))  # only_video_files


							# compare_registry_and_rename_if_need # find_some_in_base_for_is_equal_status(local/nlocal)(os_listdir)

							# debug/test

							def diffreg(local_file: str = "",
										nlocal_file: str = ""):  # local_shortfile(for_check) # nlocal_file(for_path)

								local_equal: list = []
								nlocal_equal: list = []

								try:
									fpath = "\\".join(
										nlocal_file.split("\\")[0:-1])  # folder_for_rename_nlocal_to_local_file
								except:
									fpath = ""

								try:

									try:
										local_equal.append(local_file.strip())  # local
									except:
										local_equal = []

									try:
										nlocal_equal = [nf.strip() for nf in os.listdir(fpath) if all((
											local_equal[0].lower().strip() == nf.lower().strip(),
											local_equal[0].strip() != nf.strip(),
											fpath))]  # nlocal(filter)
									except:
										nlocal_equal = []

								except:
									return False  # if_some_error(get_param/list)
								else:
									try:
										if all((local_equal[0].lower().strip() == nlocal_equal[
											0].lower().strip(), local_equal[0].strip() != nlocal_equal[
											0].strip())):  # equal_by_one_registry # diff_by_filename
											return True  # found
										else:
											return False  # not_found
									except:
										return False  # if_some_error(logic)


							# +asyncio
							if diffreg(l.split("\\")[-1], new_file) and l[0] < new_file[0] and is_log:
								print(Style.BRIGHT + Fore.WHITE + "Разные регистры, но один файл %s" %
									  l)
								write_log("debug diffreg",
										  "Разные регистры, но один файл %s" % l.split("\\")[-1])

							# need_rename_new_file_to_l_for_one_registry

							# Надо ...: d:\multimedia\video\serials_europe\Zveroboy_Rus\Zveroboy c:\...\Zveroboy_01s09e.mp4=>d:\...\Zveroboy_01s09e.mp4

							if os.path.exists(new_file):
								if is_log and all((l, new_file)):
									# full_path # difference

									print(Style.BRIGHT + Fore.CYAN + "Надо обновить:",
										Style.BRIGHT + Fore.YELLOW + "%s" % full_path,
										Style.BRIGHT + Fore.WHITE + "%s" % "~>".join([full_to_short(l), new_file]))
									write_log("debug isupdate", "%s" % "~>".join([l, new_file]))

							elif not os.path.exists(new_file):
								if is_log and all((l, new_file)):
									# full_path # difference

									print(Style.BRIGHT + Fore.GREEN + "Надо записать:",
										Style.BRIGHT + Fore.YELLOW + "%s" % full_path,
										Style.BRIGHT + Fore.WHITE + "%s" % "=>".join([full_to_short(l), new_file]))
									write_log("debug isnew", "%s" % "~>".join([l, new_file]))

							if is_log:
								write_log("debug folder[file]", ";".join([l, new_file]))  # difference

							folders_to_move.append(";".join([l, new_file]))  # difference # hidden_when_debug

	# sleep(2) # end_logging(debug)

	# pass_2_of_2
	if folders_to_move:
		temp = list(set(folders_to_move))

		folders_to_move = sorted(temp, reverse=False)

		with unique_semaphore:
			for ftm in folders_to_move:

				if is_log:
					print(Style.BRIGHT + Fore.GREEN + "%s" % ftm.split(";")[0],
						Style.BRIGHT + Fore.WHITE + "->",
						Style.BRIGHT + Fore.GREEN + "%s" % ftm.split(";")[-1])  # src_to_dst
					write_log("debug folder[filemove]",
						";".join([ftm.split(";")[0], ftm.split(";")[-1]]))  # logging(local_to_nlocal)

		sleep(2)  # end(set_and_sorted)

	return folders_to_move


move_files_list: list = []


# @log_error
async def process_move(file1: str = "", file2: str = "", is_copy: bool = False, is_eq: bool = True, avg_size: int = 0): # 27

	global move_files_list

	try:
		assert file1 and file2 and os.path.exists(file1), "Не указан один из файлов или нет откуда копировать @process_move/file1/file2" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Не указан один из файлов или нет откуда копировать @process_move/%s/%s" % (file1, file2))
		raise err
		return

	# if any((not file1, not file2)) or not os.path.exists(file1):
		# return

	if os.path.exists(file1):
		move_files_list.append((file1, file2, is_copy, is_eq, avg_size))

	# normal_fname = False

	try:
		normal_fname: bool = (file1.split("\\")[-1] == file2.split("\\")[-1])
		# assert normal_fname, "Имя файла при копировании или переносе уникально @process_move/normal_fname" # is_assert(debug)
	except: # AssertionError: # as err:
		normal_fname: bool = False
		logging.warning("Имя файла при копировании или переносе уникально @process_move/%s/%s" % (file1.split("\\")[-1], file2.split("\\")[-1]))
		# raise err
	finally:
		try:
			fname = file1.split("\\")[-1].strip()  # if_ok_use_short
		except:
			fname = file1  # if_error_use_full

		try:
			# fast_move: bool = (os.path.exists(file1) and any((os.path.getsize(file1) <= avg_size, not avg_size))) # exist_is_avg_null(is_avg)
			fast_move: bool = (os.path.exists(file1) and os.path.getsize(file1) <= avg_size) # exist_is_avg_null(is_avg)
		except:
			fast_move: bool = False

		try:
			fast_move_status: str = "Быстрый перенос %s" % file1 if fast_move else "Обычный перенос %s" % file1
		except BaseException as e:
			fast_move_status: str = "Неизвестный перенос %s [%s]" % (file1, str(e))

		write_log("debug process_move!", "%s %s [%d]" % (
			fname, fast_move_status, avg_size))  # Star_Wars_The_Bad_Batch_02s03e.mp4, True, 133138825

	try:
		fname1: str = full_to_short(file1) if file1.split("\\")[-1] else file1
	except:
		fname1: str = file1

	try:
		fname2: str = full_to_short(file2) if file2.split("\\")[-1] else file2
	except:
		fname2: str = file2
	try:
		is_new: bool = (os.path.exists(file1) and not os.path.exists(file2))
	except:
		is_new: bool = False

	try:
		is_update: bool = (os.path.exists(file1) and os.path.exists(file2))
	except:
		is_update: bool = False

	try:
		equal_fsize = all((is_update, os.path.getsize(file1) == os.path.getsize(file2)))
	except:
		equal_fsize = False

	try:
		if is_eq:
			is_eqdi: bool = (normal_fname == True)  # equals_filenames
		elif not is_eq:
			is_eqdi: bool = any((normal_fname, not normal_fname))  # diff_filenames
	except:
		is_eqdi: bool = (normal_fname == True)  # equals_filenames_by_error

	try:
		if any((is_new, is_update)) and all((fspace(file1, file2), any((file1[0] < file2[0], file2[0] >= file1[0])), file1 != file2)) and all(
				(is_eqdi, equal_fsize == False)): # file2[0] >= file1[0]
			try:
				if not is_copy:
					move(file1, file2)
				elif is_copy:
					copy(file1, file2)
			except:
				pass  # return # exit_procedure_if_error
			else:
				if all((is_new, not is_update)):
					print(Style.BRIGHT + Fore.WHITE + "%s ~> %s" % (fname1.strip(), fname2.strip()))  # file1, file2
				elif all((is_update, not is_new)):
					print(Style.BRIGHT + Fore.BLUE + "%s ~> %s" % (fname1.strip(), fname2.strip()))  # file1, file2

				write_log("debug readyfile", "%s ~> %s" % (file1, file2))

		elif all((file1.split("\\")[-1] == file2.split("\\")[-1], any((file1[0] < file2[0], file2[0] >= file1[0])), file1 != file2, is_copy == False)) and equal_fsize == True:
			os.remove(file1)
			write_log("debug need_delete[equal]", ";".join([file1, file2, str(equal_fsize)]))

		'''
		else:
			status = any((is_new, is_update))

			if all((file1, file2)):
				print("Файл(ы): %s. Статус: %s. Имя файла верно: %s. Диск: %s" % (
					"|".join([file1, file2]), str(status), str(normal_fname), str(file2[0]))) # Место для обработки: %s. # str(fspace(file1, file2))

				write_log("debug readyfile[unknown]",
						  "Файл(ы): %s. Статус: %s. Имя файла верно: %s. Диск: %s" % (
							  "|".join([file1, file2]), str(status), str(normal_fname), str(file2[0]))) # Место для обработки: %s. # str(fspace(file1, file2))
		'''
	except BaseException as e:
		if str(e): # not fspace(file1, file2) # skip_if_fspace_bad
			print(Style.BRIGHT + Fore.RED + "Ошибка обработки файла %s или нет места на %s [%s]" % (file1, file2[0], str(e)))
	finally:
		if fspace(file1, file2):  # reserve(dspace)(ok)
			if equal_fsize == False:
				if os.path.exists(file1):
					MyNotify(txt=f"Файл {file2} будет обновлен", icon=icons["moved"])
				elif not os.path.exists(file1):
					MyNotify(txt=f"Файл {file2} был обновлен", icon=icons["moved"])
			elif equal_fsize == True:
				if any((file1[0] < file2[0], file2[0] >= file1[0])) and file1 != file2:
					MyNotify(txt=f"Файл {full_to_short(file1)} будет удален, т.к. файл уже существует",
							 icon=icons["skip"])
					write_log("debug [dspace][equal][file1]", f"Файл {file1} будет удален, т.к. файл уже существует")
					# os.remove(file1)
		# elif fspace(file1, file2) == False: # reserve(dspace)(bad)
			# MyNotify(txt=f"Ошибка записи файла {full_to_short(file1)} нет места", icon=icons["error"])
			# write_log("debug [dspace][error][file1]", f"Ошибка записи файла {file1} нет места")

# @log_error
async def process_delete(file1: str = ""): #17

	try:
		assert os.path.exists(file1), "Файл отсутствует @process_delete/file1" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Файл отсутствует @process_delete/%s" % file1)
		raise err
		return

	# if not os.path.exists(file1): # not file1
		# return

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
			print(Style.BRIGHT + Fore.RED + "Ошибка обработки файла %s [%s]" % (file1, str(e)))
	finally:
		if os.path.exists(file1):
			MyNotify(txt=f"Файл {file1} будет удалён", icon=icons["cleaner"])
		elif not os.path.exists(file1):
			MyNotify(txt=f"Файл {file1} был удалён", icon=icons["cleaner"])

	# MT = MyTime(seconds=2)
	# MT.sleep_with_count(ms=MT.seconds)
	# del MT


# @log_error
def process_zip(cmd, filename):
	pass


async def seasonvar_parse(filename, is_log: bool = True) -> any: # convert_parsefile_to_normal_file

	write_log("debug start[seasonvar_parse]", "%s [%s]" % (filename, str(datetime.now())))

	try:
		assert os.path.exists(filename), "Файл отсутствует @seasonvar_parse/filename" # is_assert(debug)
	except AssertionError as err:
		logging.warning("Файл отсутствует @seasonvar_parse/%s" % filename)
		raise err
		return None

	# if not os.path.exists(filename): # not filename
		# return None # str -> None

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

	print(Style.BRIGHT + Fore.YELLOW + "Обработка файла", Style.BRIGHT + Fore.WHITE + "%s" % filename)

	try:
		part1, *part2, part3 = filename.split("\\")[-1].split(".")
	except:
		part1 = part2 = part3 = ""
	else:
		filename_parts = (part1, *part2, part3)
		write_log("debug filename[original]", "%s [%d]" % (filename, len(filename_parts)))

	# 7f_Avenue.5.S02.E03.2022.WEB-DL.1080p.ExKinoRay.a1.25.10.22.mp4
	# 7f_Nadvoe.S01.E06.2022.WEB-DL.1080p.a1.31.10.22.mp4
	# 7f_The.White.Lotus.S02.E01.2022.WEB-DL.1080p.ExKinoRay.a1.31.10.22.mp4

	# S01.E01 -> 01s01e # debug_by_some_name # debug/test # trouble_autorename -> parse_autorename
	def trouble_autorename(filename):
		# clear_seasonvar_prefix_first

		write_log("debug start[trouble_autorename]", "%s" % str(datetime.now()))

		old_filename = filename if os.path.exists(filename) else ""

		try:
			assert old_filename, "Возможно файл отсутствует @trouble_autorename/old_filename" # is_assert(debug)
		except AssertionError: # as err:
			logging.warning("Возможно файл отсутствует @trouble_autorename/old_filename")
			# raise err
			return # return None

		# if not old_filename:  # exit_if_nullname
			# return None

		# filename = "c:\\temp\\7f_The.White.Lotus.S02.E01.2022.WEB-DL.1080p.ExKinoRay.a1.31.10.22.mp4"
		seep_regex = re.compile(r".*([sS]{1}[\d+]{1,2})\.([eE]{1}[\d+]{1,2}).*", re.I)
		crop_filename_regex3 = re.compile(r"7f_(.*)\.[sS]{1}[\d+]{1,2}\.[eE]{1}[\d+]{1,2}", re.I)

		def gen_to_list(filename=filename):
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

			write_log("debug seep_str[error]",
					  "%s [%s] [%s]" % (filename, str(e), str(datetime.now())), is_error=True)  # filename/error/datetime

			return None

		try:
			with open(vr_folder, encoding="utf-8") as vff:
				vf = json.load(vff)
		except:
			vf = {}

		# 'The_White_Lotus_S02E01.mp4' # need_examples
		try:
			seep_str: str = "\\".join(filename.split("\\")[:-1]) + "\\" + "_".join([crop_filename_regex3.findall(filename.split("\\")[-1])[0].replace(".", "_"), seep_str]) + "".join([".", filename.split("\\")[-1].split(".")[-1]])  # ; print(seep_str)
		except BaseException as e:
			seep_str: str = ""

			write_log("debug seep_str[notemp]!", "Not found same filenames [%s] [%s]" % (filename, str(e)), is_error=True)

			return None

		# (filename_by_template, short_by_base)
		tmp = list(set([(seep_str.strip(), v) for k, v in vf.items() if	all((v, seep_str, v in seep_str))]))

		if tmp:
			write_log("debug seep_str[temp]", "[%s] %s" % (filename, str(tmp)))  # print(filename_and_same)
		else:
			write_log("debug seep_str[notemp]", "Not found same filenames [%s]" % filename)

		write_log("debug seep_str[move]", "%s -> %s [%s]" % (filename, seep_str, str(datetime.now())))  # filename/list/datetime

		# os.move(filename, seep_str)

		write_log("debug end[trouble_autorename]", "%s" % str(datetime.now()))

		return seep_str

	async def soundtrack_save():
		# вытащить_все_озвучки(поиграть_с_регистром)_из_списка_файлов(сохранить_их_в_логи)# debug/test

		# @soundtrack.json(base) # @soundtrack.lst(only_soundtracks_seasonvar_311022) # logging_known_soundtrack_by_file # {filename:soundtrack}

		# if_list_changed(big)_try_load_from(soundtrack.lst) # english(latin)_only

		# ручной поиск, из имени файла при записи или скачивании
		'''
		'''

		# @files_base["soundtrack"] # manual_parse

		soundtrack: list = ['СТС', 'ДТВ', 'Swe', 'KvK', 'FOX', '2x2', 'ТНТ', 'MTV', 'Ukr', 'NTb', 'SET', 'Ozz', 'SNK', 'НТВ', 'ТВ3',
							'Kyle', 'DDP5', 'Diva', 'AMZN', '3xRus', 'RenTV', 'Getty', '2xRus', 'RuDub', 'Gravi', 'Kerob', 'FiliZa',
							'Cuba77', 'RusTVC', 'lunkin', 'Amedia', 'Goblin', 'Котова', 'AniDub', 'qqss44', 'Jetvis', 'Kravec',
							'Disney', 'SHURSH', 'Ancord', 'ylnian', '7turza', 'AltPro', 'HDCLUB', 'SATRip', 'Sci-Fi', 'Кравец',
							'JimmyJ', 'Kinozal', 'Hamster', '1 канал', 'HDREZKA', 'AniFilm', 'Сыендук', 'RiperAM', 'HDRezka',
							'Пифагор', 'Files-x', 'TVShows', 'To4kaTV', 'GraviTV', 'Nicodem', 'BaibaKo', 'SoftBox', 'ColdFilm',
							'DexterTV', 'Alehandr', 'Оригинал', 'LostFilm', 'Субтитры', 'Домашний', 'STEPonee', 'CrazyCat', 'Ultradox',
							'filmgate', 'novafilm', 'gravi-tv', 'AlexFilm', 'FilmGate', 'GreenTea', 'AniMedia', 'GoldTeam', 'AniLibria',
							'Axn SciFi', 'CasStudio', 'seasonvar', 'MediaClub', 'Невафильм', 'Aleksan55', 'Шадинский', 'Novamedia',
							'turok1990', 'NewStudio', 'Nikolspup', 'CBS Drama', 'Universal', 'MrMittens', 'cinemaset', 'Seryy1779',
							'SDI Media', 'Paramount', 'Nataleksa', '25Kuzmich', 'ExKinoRay', 'Persona99', 'Sony Turbo', 'ZoneVision',
							'WarHead.ru', 'films.club', 'East Dream', '1001cinema', 'Shachiburi', 'BenderBEST', 'Sony Sci-Fi',
							'Zone Vision', 'SAFARISOUND', 'GeneralFilm', 'Nickelodeon', 'AngelOfTrue', 'Субтитры VP', 'Studio Band',
							'RG_Paravozik', 'SHIZAProject', 'Кураж-Бамбей', 'RG.Paravozik', 'www.Riper.AM', 'TEPES TeamHD', 'scarfilm.org',
							'AnimeReactor', 'DreamRecords', 'by_761OPiter', 'Kuraj-Bambey', 'кубик в кубе', 'VO-production', 'ViruseProject',
							'DIVA Universal', 'www.riperam.org', 'Wentworth Miller', 'TVHUB', 'LineFilm', 'DUB', 'MrMittens']

		with open(files_base["stracks"], "w", encoding="utf-8") as sf:
			sf.writelines("%s\n" % st.strip() for st in filter(lambda x: x, tuple(soundtrack)))

		try:
			# soundtrack_list = sorted(soundtrack, reverse=True) # cba_by_index
			# soundtrack_list = sorted(soundtrack, reverse=False) # abc_by_index

			soundtrack_list = sorted(soundtrack, key=len, reverse=True)  # cba_by_string
			# soundtrack_list = sorted(soundtrack, key=len, reverse=False) # abc_by_string
		except:
			soundtrack_list = []

		try:
			with open(soundtrack_base, encoding="utf-8") as sbf:
				soundtrack_dict = json.load(sbf)
		except: # IOError
			soundtrack_dict = {}

			with open(soundtrack_base, "w", encoding="utf-8") as sbf:
				json.dump(soundtrack_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)
		else:
			# soundtrack_in_filename_by_low_string
			try:
				soundtrack_filter = {filename.strip(): sl.strip() for sl in filter(lambda x: x, tuple(soundtrack_list)) if
							any((sl.lower().strip() in filename.lower().strip(), sl.strip() in filename))}
			except:
				soundtrack_filter = {}

			if soundtrack_filter:
				soundtrack_dict.update(soundtrack_filter)

		if len(soundtrack_dict) >= 0:

			# filter(lambda x: lst.count(x) != list(set(lst)).count(x), tuple(lst)) # search_moda

			try:
				soundtrack_count = [(v.strip(), list(soundtrack_dict.values()).count(v.strip)) for k, v in soundtrack_dict.items() if
							sl.lower().strip() in k.lower().strip()]
			except:
				soundtrack_count = []
			else:
				if soundtrack_count:

					soundtrack_count_sorted = sorted(soundtrack_count, key=lambda soundtrack_count: soundtrack_count[1]) # sorted_by_value
					soundtrack_count = [(scs[0], int(scs[1])) for scs in soundtrack_count_sorted if isinstance(soundtrack_count_sorted, tuple)]

					# write_log("debug soundtrack_count[low]", "%s" % str(soundtrack_count))
					write_log("debug soundtrack_count[low]", "%d soundtrack count" % len(soundtrack_count))

			try:
				soundtrack_count = {v.strip(): str(list(soundtrack_dict.values()).count(v.strip())) for k, v in	soundtrack_dict.items()}
			except:
				soundtrack_count = {}
			else:
				if soundtrack_count:

					soundtrack_count_list = [(k, int(v)) for k, v in soundtrack_count.items()]
					soundtrack_count_sorted = sorted(soundtrack_count_list, key=lambda soundtrack_count_list: soundtrack_count_list[1]) # sorted_by_value
					stc = {scs[0]: scs[1] for scs in soundtrack_count_sorted} # sorted_json
					soundtrack_count = stc if stc else {}

					write_log("debug soundtrack_count[combine]", "%s" % str(soundtrack_count))
					# write_log("debug soundtrack_count[combine]", "%d soundtracks count" % len(soundtrack_count))

					try:
						soundtrack_count_new = {k: int(v) for k, v in soundtrack_count.items()}
						s = sum(list(soundtrack_count_new.values()));
						l = len(soundtrack_count_new);
						a = s / l
						class_dict = {k: round((v / s) * 100, 2) for k, v in soundtrack_count_new.items() if v - a > 0}  # 0..100%(popular_classify)
					except BaseException as e:
						class_dict = {}
						write_log("debug soundtrack_count[error]", "%s [%s]" % (str(None), str(e)), is_error=True)
					else:
						try:
							sort_class = {s:v for s in sorted(class_dict, key=class_dict.get, reverse=False) for k, v in class_dict.items() if all((s, k, v, s == k))}
						except:
							sort_class = {}

						if all((sort_class, len(sort_class) <= len(class_dict))): # is_sorted_dict # less_or_equal
							class_dict = sort_class

						class_status = str(class_dict) if class_dict else ""
						if class_status:
							write_log("debug soundtrack_count[popular]", "%s" % class_status)

			with open(soundtrack_base, "w", encoding="utf-8") as sbf:
				json.dump(soundtrack_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

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
	clear_start_regex = re.compile(r"^(?:(\[Anistar\.org\][\.\_]{1}|The_|Marvels_|Marvel\'s_|DC_|DC\'s_|Tom_Clancys_))", re.I)

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
			st = "".join(["_","|".join(tmp)]).replace("|", "|_").replace(" ", "_")
	# '''

	if not stl:
		# _[\d+]{4}(tvseries_with_year/include) # is_template
		# _US|_UK(tvseries_with_city/include) # is_template
		# clear_words(ignore -> match) # debug/test # [\_\.]{1}[S]{1}[\d+]{2}[\_\.]{1} # manual # debug/test
		clear_words_regex = re.compile(r"(?:(_Sezon_|\[[AZaz\.]{1,}\]_|\_\-|_TVShows|_LV|_KB|_WEB-DL|_[\d+]{4}))", re.I) # is_clear_soundtrack(regex/in_list)
	elif stl and st:
		clear_words_regex = re.compile(r"(?:(_Sezon_|\[[AZaz\.]{1,}\]_|\_\-|%s|_[\d+]{4}))" % st, re.I) # is_clear_soundtrack(regex/in_list)

	# clear_double(ignore -> match) # Alone__Arctic__06s11e ~> Alone_Arctic_06s11e # manual # debug/test
	clear_double_regex = re.compile(r"([_]{2,})", re.M)

	# unique_filename_regex = re.compile(r"([^A-Za-zА-Яа-я0-9\-\.\(\)\[\]]{1,}|[nbsp]{4}|[\-]{2,})", re.I) # ([^A-Za-zА-Яа-я0-9\-\.\(\)\[\]]{1,}|[nbsp]{4}|[\-]{2,})) -> - # is_sep
	# fname = unique_filename_regex.sub("", fname) ?-> fname = slugify(fname)

	def parse_autorename(filename, ff_last: list = [], ind: int = 0) -> str:  # short/full/fullpath/listfiles # is_log=True

		write_log("debug start[parse_autorename]", "%s" % str(datetime.now()))

		if all((trouble_autorename(filename) != None, filename)):  # != None
			print(Style.BRIGHT + Fore.CYAN + "%s" % trouble_autorename(filename))  # true_autorename_if_not_none # debug/test

		# print(Style.BRIGHT + Fore.YELLOW + "%s" % filename)

		global temp2

		# """
		# all((test.count(".") != filename.count("."), fullpath)) # converted_file # normal_file(filter)
		if all((video_ext_regex.findall(filename), filename)) and not is_log:

			# new_file = "\\".join([fullpath, filename.replace("..", ".")]) # replace_by_string

			dot_regex = re.compile(r"[\.]{2,}")
			new_file = "\\".join([fullpath, dot_regex.sub(".", filename)]) # replace_by_regex

			# move(copyfile, "\\".join([fullpath, fullname]))
			if is_log and all((copyfile, new_file)):
				print(Style.BRIGHT + Fore.WHITE + "%s" % "~~>".join([copyfile, new_file]))
				write_log("debug parse[files]", "%s" % "~~>".join([copyfile, new_file]))

			if all((filename != clear_start_regex.sub("", filename),
					len(clear_start_regex.sub("", filename)) < len(filename), clear_start_regex.sub("", filename))) and \
					os.path.exists(copyfile):  # clear_start_regex.findall(filename):
				filename = clear_start_regex.sub("", filename)

			if all((filename != clear_words_regex.sub("", filename),
					len(clear_words_regex.sub("", filename)) < len(filename), clear_words_regex.sub("", filename))) and \
					os.path.exists(copyfile):  # clear_words_regex.findall(filename):
				filename = clear_words_regex.sub("", filename)

			if all((filename != clear_double_regex.sub("_", filename),
					len(clear_double_regex.sub("_", filename)) < len(filename),
					clear_double_regex.sub("_", filename))) and \
					os.path.exists(copyfile):  # clear_double.findall(filename):
				filename = clear_double_regex.sub("_", filename)

			orig_filename = copyfile
			new_filename = "\\".join([fullpath, filename])  # default_rename_by_fullpath

			clear_punc_regex = re.compile(r"[\!\# \$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?]{1,}", re.M)
			if all((filename != clear_punc_regex.sub("", filename), filename, clear_punc_regex.sub("", filename))):
				write_log("debug parse_autorename[punc]", "%s [%s]" % (
					clear_punc_regex.sub("", filename), str(ind)))  # filename = clear_punc_regex.sub("", filename)
			# new_filename = "\\".join([fullpath, filename]) # rename_without_punc_by_fullpath

			try:
				change_filename = "$".join([orig_filename, new_filename])
			except:
				change_filename = ""
			else:
				temp = {}
				temp2 = change_filename

				# check_short_fullname_in_lowercase # pass_1_of_2
				temp = {orig_filename.strip(): new_filename.strip() for ff in ff_last if all((crop_filename_regex.sub("", ff.split("\\")[-1]).lower().strip() == crop_filename_regex.sub("", new_filename.split("\\")[-1]).lower().strip(), change_filename))}
				# temp = {orig_filename.strip():new_filename.strip() for ff in ff_last if all((crop_filename_regex.sub("", ff.split("\\")[-1]).lower().strip() == crop_filename_regex.sub("", change_filename.split("$")[-1].split("\\")[-1]).lower().strip(), change_filename))}

				# if_equal_shortfilenames # debug/test(logic)
				# '''
				if crop_filename_regex.sub("", new_filename.split("\\")[-1]).lower().strip() == crop_filename_regex.sub("", change_filename.split("$")[-1].split("\\")[-1]).lower().strip():
					write_log("debug crop_filename_regex!",
							  "%s" % crop_filename_regex.sub("", new_filename.split("\\")[-1]).lower().strip())
				# '''

				if temp and is_log:
					print(temp, "Найден(о) %d файл(а, ов) для добавления или обновления" % len(temp), "[%s]" % str(ind),
						  end="\n")  # message_console2
					write_log("debug parsefound[%s]" % str(ind),
							  "Найден(о) %d файл(а, ов) для добавления или обновления [%s]" % (len(temp), new_filename))

				write_log("debug end[parse_autorename]", "%s" % str(datetime.now()))

				return temp2  # return(result)

		write_log("debug end[parse_autorename][unknown]", "%s" % str(datetime.now()))

		return "" # if_not_autorename(null_string)

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
			ff_last = {k: v for k, v in ff_last.items() if os.path.exists(k)} # stay_only_exists(or_null)
		except:
			ff_last = {} # skip_with_error
		else:
			with open(vr_files, "w", encoding="utf-8") as vff:
				json.dump(ff_last, vff, ensure_ascii=False, indent=2, sort_keys=True) # save_without_error

	# convert_fullname_to_(fullpath / shortfilename)
	try:
		fp, fn = split_filename(filename)
	except:
		fn = filename.split("\\")[-1].strip() # fp
	finally:
		temp = fn

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})",
									 re.I)  # [('Hudson.and.Rex.', 's04', 'e01')] # length=3

		# temp = "7f_Hudson.and.Rex.s04e01.HD1080p.WEBRip.Rus.BaibaKo.tv.a1.10.10.21.mp4"  # 1

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Hudson.and.Rex.', 's04', 'e01')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Hudson.and.Rex.', 's04', 'e01'] # len(filelearn) >= 3

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
			if all((filelearn[-2][0].lower() == "s", "".join(filelearn[-2][1:]).isnumeric())):  # 04s
				if all((filelearn[-1][0].lower() == "e", "".join(filelearn[-1][1:]).isnumeric())):  # 01e
					if len(filelearn) >= 3:
						seas = "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]]).lower()
						epis = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 03s02e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Hudson_and_Rex_04s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Hudson_and_Rex_04s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Hudson_and_Rex_04s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [1]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [1]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=1)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})x([\d+]{2})",
									 re.I)  # [('Ordinator.', '3', '02')] # length=3
		# temp = "7f_Ordinator.3x02-FleshofMyFlesh.a2.27.05.20.mp4"  # 2

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # Tags: [('Ordinator.', '3', '02')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Ordinator.', '3', '02'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2], "s"]) if len(str(filelearn[-2])) == 1 else "".join([filelearn[-2], "s"])
				epis = "".join(["0", filelearn[-1], "e"]) if len(str(filelearn[-1])) == 1 else "".join([filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 03s02e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True
			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Ordinator_03s02e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Ordinator_03s02e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Ordinator_03s02e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [2]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [2]" % (copyfile, str(e)), is_error=True)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=2)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([\d+]{2})-([A-Za-z\.\-\d+]{1,}).*([\d+]{1}[sS]{1})ezon",
									 re.I)  # [('10', 'Borgia.', '2s')] # length=3
		# temp = "7f_10-Borgia.2sezon.2012.720p.BDRip.AVC-Srg6161.a1.03.11.16.mp4"  # 3

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('10', 'Borgia.', '2s')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['10', 'Borgia.', '2s'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[0][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-1]]) if len(filelearn[-1]) == 2 else filelearn[-1]
				epis = "".join(["0", filelearn[0], "e"]) if len(filelearn[0]) == 1 else "".join([filelearn[0], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 02s10e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Borgia_02s10e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Borgia_02s10e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Borgia_02s10e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [3]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [3]" % (copyfile, str(e)), is_error=True)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=3)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([\d+]{2}).*[\.]{1,}([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})",
									 re.I)  # [('15', 'Grand.', 's05')] # length=3
		# temp = "7f_15..Grand.s05.2021.WEB-DLRip.Files-x.a1.18.09.21.mp4"  # 4

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('15', 'Grand.', 's05')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['15', 'Grand.', 's05'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[0][0:]).isnumeric(), "".join(filelearn[-1][1:]).isnumeric(),len(filelearn) >= 3)):
				seas = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
				epis = "".join(["0", filelearn[0], "e"]) if len(filelearn[0]) == 1 else "".join([filelearn[0], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 05s15e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Grand_05s15e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(
				filelearn[0:])  # ; print("Filename: %s" % str(filename)) # ; filename = filename[1:] # Grand_05s15e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Grand_05s15e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [4]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [4]" % (copyfile, str(e)), is_error=True)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=4)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# unique(check_for_rus)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,})\.([\d+]{2})\.seriya\.iz\.([\d+]{2})",
									 re.I)  # [('Emili', '02', '20')]
		# temp = "7f_Emili.02.seriya.iz.20.1990.XviD.TVRip.a1.09.03.14.mp4"  # 5

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Emili', '02', '20')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Emili', '02', '20'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][0:]).isnumeric(), "".join(filelearn[-2][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = "01s"
				epis = "".join(["0", filelearn[-2], "e"]) if len(filelearn[-2]) == 1 else "".join([filelearn[-2], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s02e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_epis

			# Emili_01s02e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Emili_01s02e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Emili_01s02e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [5]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [5]" % (copyfile, str(e)), is_error=True)
	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=5)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[\b0-9]f_([A-Za-z\.\-\d+]{1,}).*\[([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})",
									 re.I)  # [('House.of.Cards.', 'S04', 'E01')] # length=3
		# temp = "7f_House.of.Cards.[S04E01].720p.1kanal.[qqss44].a1.19.03.16.mp4"  # 6

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('House.of.Cards.', 'S04', 'E01')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['House.of.Cards.', 'S04', 'E01'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][1:]).isnumeric(), "".join(filelearn[-1][1:]).isnumeric(),	len(filelearn) >= 3)):
				seas = "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]]).lower()
				epis += "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 04s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# House_of_Cards_04s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # House_of_Cards_04s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # House_of_Cards_04s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [6]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [6]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=6)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\d+]{1,}|[A-Za-z\.\d+]{1,})).*([sS]{1}[\d+]{1}).*([\d+]{2})",
			re.I)  # [('How.to.Get.Away.with.Murder.', 'S2', '10')] # length=3 # debug/test # delete '-'
		# temp = "7f_How.to.Get.Away.with.Murder.-.S2.10.,.a1.23.10.18.mp4"  # 7

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('How.to.Get.Away.with.Murder.', 'S2', '18')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['How.to.Get.Away.with.Murder.', 'S2', '10'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][0:]).isnumeric(), "".join(filelearn[-2][1:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2][-1], filelearn[-2][0]]) if len(filelearn[-2]) == 2 else "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]])
				epis = "".join(["0", filelearn[-1], "e"]) if len(filelearn[-1]) == 1 else "".join([filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 02s10e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# How_to_Get_Away_with_Murder_02s10e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # How_to_Get_Away_with_Murder_02s10e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # How_to_Get_Away_with_Murder_02s10e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [7]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [7]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=7)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# unique(check_for_rus)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([eE]{1}[\d+]{2})",
									 re.I)  # [('The.Lost.Tomb.', 'E11')] # length=2 # .* -> \. # debug/test
		# temp = "7f_The.Lost.Tomb.E11.HDTVRip.BTT-TEAM.a1.08.07.16.mp4"  # 8

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('The.Lost.Tomb.', 'E11')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['The.Lost.Tomb.', 'E11'] # len(filelearn) >= 2

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][1:]).isnumeric(), len(filelearn) >= 2)):
				seas = "01s"
				epis = "".join(["0", "".join(filelearn[-1][1:]), filelearn[-1][0]]) if len(filelearn[-1]) == 2 else "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s11e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis

			# The_Lost_Tomb_01s11e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # The_Lost_Tomb_01s11e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # The_Lost_Tomb_01s11e.mp

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [8]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [8]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=8)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# unique(check)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})x([\d+]{2})",
									 re.I)  # [('BirdsofPrey', '1', '13')] # length=3
		# temp = "7f_BirdsofPrey1x13-Rus.a1.19.03.13.mp4"  # 9

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('BirdsofPrey', '1', '13')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['BirdsofPrey', '1', '13'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2], "s"]) if len(filelearn[-2]) == 1 else "".join([filelearn[-2], "s"])
				epis = "".join(["0", filelearn[-1], "e"]) if len(filelearn[-1]) == 1 else "".join([filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s13e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# BirdsofPrey_01s13e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # BirdsofPrey_01s13e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # BirdsofPrey_01s13e.mp4 # uniq

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [9]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [9]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=9)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[\b0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.([\d+]{2})\.serija",
									 re.I)  # [('Korolj.Kvinsa.', '1', '06')] # length=3
		# temp = "7f_Korolj.Kvinsa.1.sezon.06.serija.iz.25.1998-1999.XviD.DVDRip.a1.18.09.12.mp4"  # 10

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Korolj.Kvinsa.', '1', '06')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Korolj.Kvinsa.', '1', '06'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2], "s"]) if len(filelearn[-2]) == 1 else "".join([filelearn[-2], "s"])
				epis = "".join(["0", filelearn[-1], "e"]) if len(filelearn[-1]) == 1 else "".join([filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s06e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Korolj_Kvinsa_01s06e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Korolj_Kvinsa_01s06e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Korolj_Kvinsa_01s06e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [10]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [10]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=10)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([sS]{1}\.[\d+]{1}).*([\d+]{2})",
			re.I)  # [('The.King.of.Queens.', 's.6', '01')] # length=3 # debug/test
		# temp = "7f_The.King.of.Queens.s.6.01.DougLessPart1[Ezekiel2517].a1.21.12.12.mp4"  # 11

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('The.King.of.Queens.', 's.6', '01')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['The.King.of.Queens.', 's.6', '01'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2].split(".")[-1], filelearn[-2].split(".")[0]]) if len(filelearn[-2].split(".")[-1]) == 1 else "".join([filelearn[-2].split(".")[-1], filelearn[-2].split(".")[0]])
				epis = "".join(["0", filelearn[-1], "e"]) if len(filelearn[-1]) == 1 else "".join([filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 06s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# The_King_of_Queens_06s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # The_King_of_Queens_06s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # The_King_of_Queens_06s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [11]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [11]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=11)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([\d+]{2})\-([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})",
									 re.I)  # [('01', 'Vlast.v.nochnom.gorode.', 's05')] # length=3
		# temp = "7f_01-Vlast.v.nochnom.gorode.s05-2018.720p.WEB-DLRip.AVC-Srg6161.a1.24.09.18.mp4"  # 12

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('01', 'Vlast.v.nochnom.gorode.', 's05')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['01', 'Vlast.v.nochnom.gorode.', 's05'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all((filelearn[-1][0].lower() == "s", "".join(filelearn[-1][1:]).isnumeric(), "".join(filelearn[0][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]])
				epis = "".join([filelearn[0], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 05s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Vlast_v_nochnom_gorode_05s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Vlast_v_nochnom_gorode_05s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Vlast_v_nochnom_gorode_05s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [12]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [12]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=12)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[sS]{1}([\d+]{2})[x]([\d+]{2})",
									 re.I)  # [('Bridzhertony', '02', '01')] # length=3
		# temp = "7f_BridzhertonyS02x01.a1.29.03.22.mp4"  # 13

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Bridzhertony', '02', '01')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Bridzhertony', '02', '01']
		filelearn.insert(1, ".")  # ; print("Split data(# 2): %s" % str(filelearn)) # ['Bridzhertony', '.', '02', '01'] # len(filelearn) >= 4

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 4)):
				seas = "".join(["".join(filelearn[-2][0:]), "s"])
				epis = "".join(["".join(filelearn[-1][0:]), "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 02s01e

		if all((swap_seasepis, len(filelearn) >= 4)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Bridzhertony_02s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Bridzhertony_02s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Bridzhertony_02s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [13]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [13]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=13)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})",
									 re.I)  # [('InTheDark', 'S02', 'E01')] # length=3
		# temp = "7f_InTheDarkS02E01.a1.25.06.21.mp4"  # 14

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('InTheDark', 'S02', 'E01')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['InTheDark', 'S02', 'E01']
		filelearn.insert(1, ".")  # ; print("Split data(# 2): %s" % str(filelearn)) # ['InTheDark', '.', 'S02', 'E01'] # len(filelearn) >= 4

		try:
			if all((filelearn[-2][0].lower() == "s", "".join(filelearn[-2][1:]).isnumeric(), len(filelearn) >= 4)):
				if all((filelearn[-1][0].lower() == "e", "".join(filelearn[-1][1:]).isnumeric())):
					seas = "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]]).lower()
					epis = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()

		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 02s01e

		if all((swap_seasepis, len(filelearn) >= 4)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# InTheDark_02s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # InTheDark_02s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # InTheDark_02s01e.mp4 # debug/test

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [14]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [14]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=14)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})\.sezon\.([\d+]{2})\.seria",
									 re.I)  # [('Bratja.po.oruzhiju.', '1', '04')] # length=3
		# temp = "7f_Bratja.po.oruzhiju.1.sezon.04.seria.iz.10.2001.x264.BDRip.720p.MediaClub.a6.02.08.20.mp4"  # 15

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Bratja.po.oruzhiju.', '1', '04')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Bratja.po.oruzhiju.', '1', '04'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2], "s"]) if len(filelearn[-2]) == 1 else "".join([filelearn[-2], "s"])
				epis = "".join(["0", filelearn[-1], "e"]) if len(filelearn[-1]) == 1 else "".join([filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s04e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Bratja_po_oruzhiju_01s04e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Bratja_po_oruzhiju_01s04e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Bratja_po_oruzhiju_01s04e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [15]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [15]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=15)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# check_for_rus

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,})-([\d+]{3}).*", re.I)
		# temp = "7f_Bleach-001.a1.10.07.12.mp4"  # ([\w+\.]{1,}\.)-([\d+]{3}.*) # 16

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Bleach', '001')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Bleach', '001'] # len(filelearn) >= 2

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][0:]).isnumeric(), len(filelearn) >= 2)):
				seas = "01s"
				epis = "".join([filelearn[-1], "e"]) if len(filelearn[-1]) in [2, 3] else "".join(["0", filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s001e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis

			# Bleach_01s001e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Nu-ka_vse_vmeste_04s01e # Bleach_01s001e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Bleach_01s001e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [16]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [16]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			# parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath
			# print(Style.BRIGHT + Fore.YELLOW + "%s [16]" % filename); write_log("debug parse_autorename[16]", f"{filename}") # debug(is_color)

			temp2 = parse_autorename(filename, ff_last=ff_last, ind=16)
			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.Vypusk-([\d+]{2})",
									 re.I)  # [('Nu-ka.vse.vmeste.', '4', '01')] # length=3
		# temp="7f_Nu-ka.vse.vmeste.4.sezon.Vypusk-01.ot.2022.09.02.a1.06.09.22.mp4"  # ([\w+\.\-]{1,})\.([\d+]{1})\.sezon\.Vypusk-([\d+]{2}).* # 17

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Nu-ka.vse.vmeste.', '4', '01')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Nu-ka.vse.vmeste.', '4', '01'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2].split(".")[0], "s"]) if len(filelearn[-2].split(".")[0]) == 1 else "".join([filelearn[-2].split(".")[0], "s"])
				epis = "".join(["0", filelearn[-1].split(".")[0], "e"]) if len(filelearn[-1].split(".")[0]) == 1 else "".join([filelearn[-1].split(".")[0], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 04s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Nu-ka_vse_vmeste_04s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Nu-ka_vse_vmeste_04s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Nu-ka_vse_vmeste_04s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [17]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [17]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			# parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath
			# print(Style.BRIGHT + Fore.YELLOW + "%s [17]" % filename); write_log("debug parse_autorename[17]", f"{filename}") # debug(is_color)

			temp2 = parse_autorename(filename, ff_last=ff_last, ind=17)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[\.]{1,}([\d+]{1})\.s-n\.([\d+]{1,2})\.s",
									 re.I)  # [('Voyna.mirov.', '1', '1')]
		# temp="7f_Voyna.mirov..1.s-n.1.s..-.[FOX].a1.19.11.19.mp4"  # season/series # 18

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Voyna.mirov.', '1', '1')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Voyna.mirov.', '1', '1'] # len(filelearn) >= 3

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2], "s"]) if len(filelearn[-2]) == 1 else "".join([filelearn[-2], "s"])
				epis = "".join(["0", filelearn[-1], "e"]) if len(filelearn[-1]) == 1 else "".join([filelearn[-1], "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e

		# Voyna_mirov_01s01e # addition_logic
		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Voyna_mirov_01s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Voyna_mirov_01s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Voyna_mirov_01s01e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [18]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [18]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=18)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# check_for_rus

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([eE]{1}[\d+]{2})",
									 re.I)  # [('Sobor.', 'E04')] # \. -> .* # debug/test
		# temp="7f_Sobor.E04.2021.WEB-DL.720p.a1.23.12.21.mp4"
		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Sobor.', 'E04')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Sobor.', 'E04']

		seas = epis = ""

		try:
			if all((filelearn[-1][0].lower() == "e", "".join(filelearn[-1][1:]).isnumeric(), len(filelearn) >= 2)):
				seas = "01s"
				epis = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s04e

		# Sobor_01s04e # addition_logic
		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis

			# Sobor_01s04e
			if filelearn[0].count(".") > 0:
				filelearn = "".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join([filelearn[0], swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Sobor_01s04e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Sobor_01s04e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [19]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [19]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=19)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

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
			re.I)  # [('Zhizn.po.vyzovu.', 'S01', 'E07')] # debug/test
		# temp="7f_Zhizn.po.vyzovu.S01.E07.2022.WEBRip.1080p.a1.29.09.22.mp4"

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Zhizn.po.vyzovu.', 'S01', 'E07')] # [('Himera.', 's01', 'e01')] # [('Staya.', 'S01', 'E06')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Zhizn.po.vyzovu.', 'S01', 'E07'] # ['Himera.', 's01', 'e01'] # ['Staya.', 'S01', 'E06']

		# seas = epis = ""  # hide_if_try_except_no_logic # debug/test

		try:
			if all((filelearn[-1][0].lower() == "e", "".join(filelearn[-1][1:]).isnumeric(),
					filelearn[-2][0].lower() == "s", "".join(filelearn[-2][1:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["".join(filelearn[-2][1:]), filelearn[-2][0]]).lower()
				epis = "".join(["".join(filelearn[-1][1:]), filelearn[-1][0]]).lower()
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s07e # 01s01e # 01s06e

		# Zhizn_po_vyzovu_01s07e # Himera_01s01e # addition_logic
		if all((swap_seasepis, len(filelearn) >= 3)):  # length=4 ~> length=3
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Zhizn_po_vyzovu_01s07e # Himera_01s01e # Staya_01s06e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Zhizn_po_vyzovu_01s07e # Himera_01s01e # Staya_01s06e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Zhizn_po_vyzovu_01s07e.mp4 # Himera_01s01e.mp4 # Staya_01s06e.mp4

		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [20]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [20]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=20)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2
	# '''

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*(S[1,2])\.ep([\d+]{1,2})",
									 re.I)  # [('Ice.Age.Scrat.Tales.TVShows.', 'S1', 'ep1')]
		# temp="7f_Ice.Age.Scrat.Tales.TVShows.S1.ep1.a1.08.10.22.mp4"

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Ice.Age.Scrat.Tales.TVShows.', 'S1', '1')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Ice.Age.Scrat.Tales.TVShows.', 'S1', '1']

		seas = epis = ""

		try:
			if all(("".join(filelearn[-1][0:]).isnumeric(), filelearn[-2][0].lower() == "s",
					"".join(filelearn[-2][1:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["0", filelearn[-2][1], filelearn[-2][0]]) if len(filelearn[-2]) == 2 else "".join(
					["".join(filelearn[-2][1:]), filelearn[-2][0]])
				epis = "".join(["0", filelearn[-1], "e"]) if len(filelearn[-1]) == 1 else "".join(
					["".join(filelearn[-1][0:]), "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Ice_Age_Scrat_Tales_TVShows_01s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Ice_Age_Scrat_Tales_TVShows_01s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Ice_Age_Scrat_Tales_TVShows_01s01e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [21]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [21]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=21)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_([\d+]{1,2})[\.]{1,}(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*[\d+]{4}",
			re.I)  # [('01', 'Avatar.')]
		# temp="7f_01..Avatar.2022.WEB-DL.720p.Files-x.a1.12.09.22.mp4"

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('01', 'Avatar.')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['01', 'Avatar.']

		seas = epis = ""

		try:
			if all(("".join(filelearn[0][0:]).isnumeric(), len(filelearn[0]) in range(1, 3), len(filelearn) >= 2)):
				seas = "01s"  # debug/is_skip(season)
				epis = "".join(["0", "".join(filelearn[0][0:]), "e"]) if len(filelearn[0]) == 1 else "".join(["".join(filelearn[0][0:]), "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[0])  # no_epis

			# Avatar_01s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Avatar_01s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Avatar_01s01e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [22]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [22]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=22)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	# with_soundtrack(unique)

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(\[.*\]).*\.(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,}))\.([\d+]{1,2})\.\-\.([\d+]{1,2})",
			re.I)  # [('[AniMaunt]', 'Duncanville', '3', '01')]
		# temp="7f_[AniMaunt].Duncanville.3.-.01.a1.22.10.22.mp4"

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('[AniMaunt]', 'Duncanville', '3', '01')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['[AniMaunt]', 'Duncanville', '3', '01']

		# clean_soundtrack_from_0_value(unique)
		if filelearn[0][0].startswith("["):
			filelearn.remove(filelearn[0])

		seas = epis = ""

		try:
			if all(("".join(filelearn[-2][0:]).isnumeric(), "".join(filelearn[-1][0:]).isnumeric(),
					len(filelearn) >= 3)):
				seas = "".join(["0" + "".join(filelearn[-2][0:]) + "s"]) if len(filelearn[-2]) == 1 else "".join(["".join(filelearn[-2][0:]) + "s"])
				epis = "".join(["0" + "".join(filelearn[-1][0:]) + "e"]) if len(filelearn[-1]) == 1 else "".join(["".join(filelearn[-1][0:]) + "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all((seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 03s01e

		if all((swap_seasepis, len(filelearn) >= 2)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Duncanville_03s01e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Duncanville_03s01e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Duncanville_03s01e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [23]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [23]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=23)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	is_need_change, swap_seasepis = False, ""

	try:
		seasonvar_regex = re.compile(
			r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([\d+]{1,2})\.sezon\.([\d+]{1,2})\.seriya", re.I)
		# temp="7f_Zhizn.1.sezon.01.seriya.iz.11.2007.XviD.DVDRip.a1.23.11.12.mp4"
		# temp="7f_Myslit.kak.prestupnik.7.sezon.22.seriya.iz.24.2011.x264.WEB-DL.720pFOX.CRIME.a1.07.05.15.mp4"

		tags = seasonvar_regex.findall(temp)  # ; print("Tags: %s" % str(tags)) # [('Zhizn.', '1', '01')] # [('Myslit.kak.prestupnik.', '7', '22')]
		# [t for t in tags] # debug/test
		filelearn = [w.strip() for t in tags for w in t if w]  # ; print("Split data: %s" % str(filelearn)) # ['Zhizn.', '1', '01'] # ['Myslit.kak.prestupnik.', '7', '22']

		seas = epis = ""

		try:
			if all(("".join(filelearn[1][0:]).isnumeric(), "".join(filelearn[2][0:]).isnumeric(), len(filelearn) >= 3)):
				seas = "".join(["0", "".join(filelearn[1][0:]), "s"]) if len("".join(filelearn[1][0:])) == 1 else "".join(["".join(filelearn[1][0:]), "s"])
				epis = "".join(["0", "".join(filelearn[2][0:]), "e"]) if len("".join(filelearn[2][0:])) == 1 else "".join(["".join(filelearn[2][0:]), "e"])
		except:
			seas = epis = ""
		finally:
			swap_seasepis = "".join([seas, epis]).lower() if all(
				(seas, epis)) else ""  # ; print("Template: %s" % str(swap_seasepis)) # 01s01e # 07s22e

		if all((swap_seasepis, len(filelearn) >= 3)):
			is_need_change = True

			filelearn.remove(filelearn[-1])  # no_epis
			filelearn.remove(filelearn[-1])  # no_seas

			# Zhizn_01s01e # Myslit_kak_prestupnik_07s22e
			if filelearn[0].count(".") > 0:
				filelearn = "".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))
			elif filelearn[0].count(".") == 0:
				filelearn = "_".join(["".join(filelearn[0:]), swap_seasepis]).replace(".", "_")  # ; print("Split data: %s" % str(filelearn))

			filename = "".join(filelearn[0:])  # ; print("Filename: %s" % str(filename)) # Zhizn_01s01e # Myslit_kak_prestupnik_07s22e
			filename += "".join([".", temp.split(".")[-1].lower()])  # ; print("Filename: %s" % str(filename)) # Zhizn_01s01e.mp4 # Myslit_kak_prestupnik_07s22e.mp4
		elif not swap_seasepis:
			filename = ""

	except BaseException as e:

		if is_log:
			print(Style.BRIGHT + Fore.RED + "Не могу перевести в обычный вид файл %s [%s] [24]" % (copyfile, str(e)))
			write_log("debug parse[error]", "Не могу перевести в обычный вид файл %s [%s] [24]" % (copyfile, str(e)), is_error=True)

	else:
		if video_ext_regex.findall(filename) and is_need_change:
			temp2 = parse_autorename(filename, ff_last=ff_last, ind=24)  # parse_autorename(filename, copyfile, fullpath):  # short/full/fullpath

			if temp2:
				return temp2

	write_log("debug end[seasonvar_parse][unknown]", "%s [%s]" % (filename, str(datetime.now())))

	# exit() # exit_if_unkown_parse/debug

	return None  # if_not_found_template(None)


def okay_parse(filename, is_log: bool = True):  # convert_parsefile_to_normal_file # debug/test

	return None  # pass


# try_to_find_file_by_time(time >= midnight)

"""
@modified
some_file = "C:\\Downloads\\Books\\2022-03-26_16h55_42.png".lower().strip()

# from datetime import datetime as dt
# from os.path import getctime, getmtime
# @csv
# 2022-03-26_16h55_42.png;91494;31.03.22;11:36

# print(dt.fromtimestamp(getctime(some_file)).strftime('%Y-%m-%dT%H:%M')) # 2022-03-31T11:36 # <class 'str'>

# today = dt.today() # datetime # datetime.datetime(2022, 4, 6, 7, 39, 20, 536132) # <class 'datetime.datetime'>
# fdate = getmtime(some_file) # unixdate # 1648708605.2300806 # <class 'float'>
# ndate = datetime.fromtimestamp(fdate) # datetime.datetime(2022, 3, 31, 11, 36, 45, 230081) # <class 'datetime.datetime'>
# print(abs(today - ndate)) # 5 days, 20:02:35.306051 # <class 'datetime.timedelta'>
# print(abs(today - ndate).days) # 5 # <class 'int'>

# difference strftime vs fromtimestamp

@change_time
# from datetime import datetime, timedelta
# clock_in_half_hour = datetime.now() + timedelta(minutes=30)
# print(clock_in_half_hour) # datetime.datetime(2023, 1, 27, 19, 34, 55, 530315)
"""

if __name__ == "__main__":  # debug/test(need_pool/thread/multiprocessing/queue)

	# @optimial_time_for_jobs_by_xml(load)
	async def load_timing_from_xml(ind: int = 0) -> tuple: # load_last_time # list -> tuple # debug(is_async)
		timing = []

		try:
			tree = xml.parse(files_base["timing"]) # xml.ElementTree(file=files_base["timing"])

			root = tree.getroot()

			for elem in root.iter(tag="time"): # <timing><time><hh>1</hh><mm>46</mm></time></timing>
				tim = {}

				for subelem in elem:
					tim[subelem.tag] = subelem.text

				timing.append(tim)
		except BaseException as e:
			print(Style.BRIGHT + Fore.RED + "Xml load error (time)")
			write_log("debug timing[xml][loaderror][%d]" % ind, "Xml load error (time) %s [%s]" % (str(e), str(datetime.now())), is_error=True) # main_xml_error
			return (0, 0) # error

		if timing: # logging_if_some_data # ... Xml loaded # dict's_to_list
			print(Style.BRIGHT + Fore.WHITE + "%s" % str(timing), Style.BRIGHT + Fore.GREEN + "Xml loaded")
			write_log("debug timing[xml][load][%d]" % ind, "load ok [%s]" % str(datetime.now())) # xml_loaded

			return (int(timing[0]["hh"]), int(timing[0]["mm"])) # [{'hh': '1', 'mm': '56'}] # true_calc
		elif not timing:
			return (0, 0) # ok_but_null

	# @log_error # get_time_if_have_ready_jobs_else_null_time
	async def save_timing_to_xml(hours: int = 0, minutes: int = 0):

		# timing = [{"hh": hh_time, "mm": mm_time}] # one_record
		timing = [{"hh": int(hours), "mm": int(minutes)}] # one_record

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
			write_log("debug timing[xml][saveerror]", "Xml save error (time) %s [%s]" % (str(e), str(datetime.now())), is_error=True) # main_xml_error
		else:
			try:
				# save_xml
				with open(files_base["timing"], "wb") as vrf: # "".join([script_path, '\\video_resize.xml'])
					tree.write(vrf)

			except BaseException as e:
				print(Style.BRIGHT + Fore.RED + "Xml save error (time)")
				write_log("debug timing[saveerror]", "Xml save error (time) %s [%s]" % (str(e), str(datetime.now())), is_error=True) # some_error_in_save
			else:
				print(Style.BRIGHT + Fore.GREEN + "Xml saved")
				write_log("debug timing[xml][save]", "save ok [%s]" % str(datetime.now())) # xml_saved

			# clear_xml(logic)
			'''
			for country in root.findall('country'):
				# using root.findall() to avoid removal during traversal
				rank = int(country.find('rank').text)
				if rank > 50:
					root.remove(country)

			tree.write('output.xml')
			'''

	# update_is_ready_project # pass_x_of_4
	# @log_error
	async def project_done(path_to_done: str = path_to_done, is_debug: bool = False, is_learn: bool = False): # debug/test

		write_log("debug start[project_done]", "%s" % str(datetime.now()))

		# return

		# move_last_files(if_have)
		# datelist = datelist2 = [] # date_of_change(modify)_files # last_files

		# file_time = {} # time_to_delete(min/max)_time

		# load_meta_base(filter) #2
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

		# filter_current_jobs(is_update)
		# fcmd: dict = {}

		# @load_current_jobs
		try:
			with open(filecmd_base, encoding="utf-8") as fbf:
				fcmd = json.load(fbf)
		except: # IOError
			fcmd = {}

			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)

		first_len = second_len = 0

		# filter_current_jobs_(in_meta/no_in_meta/only_exists)
		try:
			first_len: int = len(fcmd)
			fcmd = {k: v for k, v in fcmd.items() if os.path.exists(k) and any((k.strip() in [*somebase_dict], not [*somebase_dict]))}
		except:
			fcmd = {k: v for k, v in fcmd.items() if os.path.exists(k)}
		finally:
			second_len: int = len(fcmd)

		if all((second_len, second_len <= first_len)):
			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)
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
				proj_files: list = ["".join([path_to_done, pl]) for pl in proj_list if os.path.exists("".join([path_to_done, pl])) and video_ext_regex.findall(pl) and all((
								pl.count(".") == 1, not pl.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]))]  # only_normal(files_by_tempate)
		except BaseException as e:
			proj_files: list = []

			print(Style.BRIGHT + Fore.RED + "%s" % str(e))
			write_log("debug proj_files[error]", "%s" % str(e), is_error=True)
		else:
			# need_clear_after_midnight(from_disk)
			if proj_files:
				print(Style.BRIGHT + Fore.WHITE + "Последние обновления %d штук(и) [%s]" % (
					len(proj_files), str(datetime.now())))
			write_log("debug updates[yes]",
					  "Последние обновления %d штук(и) [%s]" % (len(proj_files), str(datetime.now())))

			temp = list(set(proj_files))
			proj_files = sorted(temp, reverse=False)

			# @video_resize.lst

			# mntime: int = 0
			# mxtime: int = 0

			# renamed_list = []
			try:
				# tmp = list(pf_gen()) # new(yes_gen)
				tmp: list = [pf.strip() for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))]
			except:
				tmp: list = []  # old(no_gen) # pf.strip() for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))

			tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
			proj_files = sorted(tmp2, reverse=False)

			cnt: int = 0

			cnt += len(fcmd)
			cnt += len(proj_files)

			MySt = MyString()

			# Надо проверить 22 задач / и 0 "готовых" файл(а,ов) # Надо проверить 270 задач и 0 файлов

			if cnt:
				print(Style.BRIGHT + Fore.YELLOW + MySt.last2str(maintxt="Надо проверить", endtxt="", count=len(fcmd), kw="задач"),
					Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="и", endtxt="", count=len(proj_files), kw="файл"))
				write_log("debug jobs[ready][count]", "Надо проверить %d задач и %d готовых файлов" % (len(fcmd), len(proj_files) ))
			elif not cnt:
				print(Style.BRIGHT + Fore.YELLOW + "Нет задач или готовых файлов для проверки [%s]" % str(datetime.now()))
				write_log("debug jobs[ready][null]", "Нет задач или готовых файлов для проверки [%s]" % str(datetime.now()))

			del MySt

		MM = MyMeta() #1

		for pf in proj_files:

			if not proj_files:
				break

			if not os.path.exists(pf):
				continue

			try:
				gl = MM.get_length(pf)
			except:
				gl = 0
			else:
				proj_filter.append((pf.strip(), gl))

		proj_filter_status = "Готовые файлы успешно отфильтрованы и добавлены [%d]" % len(proj_filter) if len(proj_files) == len(proj_filter) else "Какой-то файл не отфильтровался или не добавился [%d]" % abs(len(proj_filter) - len(proj_filter))

		write_log("debug proj_filter_status", "%s" % proj_filter_status)

		for k, v in fcmd.items():

			if not fcmd: # no_data
				break

			if not os.path.exists(k): # if_not_exists
				continue

			try:
				gl = MM.get_length(k)
			except:
				gl = 0
			else:
				fcmd_filter.append((k.strip(), gl))

		fcmd_filter_status = "Задачи успешно отфильтрованы и добавлены [%d]" % len(fcmd_filter) if len(fcmd) == len(fcmd_filter) else "Какая-то задача не отфильтровалась или не добавилась [%d]" % abs(len(fcmd) - len(fcmd_filter))

		write_log("debug fcmd_filter_status", "%s" % fcmd_filter_status)

		if all((proj_filter, fcmd_filter)): # ready_jobs / current_jobs # pass_1_of_2
			try:
				proj_and_fcmd_filter = {pf[0].strip(): ff[0].strip() for pf in proj_filter for ff in fcmd_filter if all((
							pf[0].split("\\")[-1] == ff[0].split("\\")[-1], pf[1] == ff[1], pf[0] != ff[0]))}
			except BaseException as e:
				proj_and_fcmd_filter = {}

				write_log("debug proj_and_fcmd_filter[error]", "%s" % str(e))
			else:
				if len(proj_filter) != len(fcmd_filter):
					write_log("debug diff[proj_filter][fcmd_filter]", "Фильтры для обновления или записи разные, %s" % "/".join([str(len(proj_filter)), str(len(fcmd_filter))])) # 1/2
				elif len(proj_filter) == len(fcmd_filter):
					write_log("debug ok[proj_filter][fcmd_filter]", "Фильтры для обновления или записи совпадают")

		elif all((proj_filter, not fcmd_filter)): # ready_jobs / no_current_jobs
			cjob_set = set()

			for pf in proj_filter:
				for k, v in ff_last.items():

					if os.path.exists(k) and all((pf[0].split("\\")[-1] == k.split("\\")[-1], pf[0] != k)) and not k in cjob_set: # equal_filename

						cjob_set.add(k)

						try:
							ff_last_length = MM.get_length(k) # last_length_from_known_files
						except:
							ff_last_length = 0

						if all((pf[1], ff_last_length, pf[1] == ff_last_length)): # equal_length
							known_filter.append((k.strip(), ff_last_length))

		if known_filter: # known_jobs
			fcmd_filter = known_filter

		if all((proj_filter, fcmd_filter, known_filter)): # ready_jobs / current_jobs / known_jobs # pass_2_of_2
			try:
				proj_and_fcmd_filter = {pf[0].strip(): ff[0].strip() for pf in proj_filter for ff in fcmd_filter if all((
							pf[0].split("\\")[-1] == ff[0].split("\\")[-1], pf[1] == ff[1], pf[0] != ff[0]))}
			except BaseException as e:
				proj_and_fcmd_filter = {}

				write_log("debug proj_and_fcmd_filter[error][2]", "%s" % str(e))

		if proj_and_fcmd_filter:
			for k, v in proj_and_fcmd_filter.items():
				if os.path.exists(k):
					print(Style.BRIGHT + Fore.CYAN + "Подготовка обработки файла", Style.BRIGHT + Fore.YELLOW + "%s" % k,
							Style.BRIGHT + Fore.CYAN + "добавление или обновление файла", Style.BRIGHT + Fore.YELLOW + "%s" % full_to_short(v))

					move(k, v) # no_async_if_"big"

					write_log("debug proj_and_fcmd_filter[move]", "-=>".join([k, v]))

		fcmd_hours: list = []
		fcmd_minutes: list = []

		if fcmd_filter:
			fcmd_hours = [ff[1] % 3600 for ff in fcmd_filter if ff[1] % 3600 > 0]
			fcmd_minutes = [(ff[1] // 60) % 60 for ff in fcmd_filter if (ff[1] // 60) % 60 > 0]

			hh_time: int = 0
			hh_avg_time: int = 0
			mm_time: int = 0
			mm_avg_time: int = 0

			# @avg_hour / @max_hour
			try:
				fcmd_hours_sum = sum(fcmd_hours)
				fcmd_hours_len = len(fcmd_hours)
				fcmd_hours_avg = (lambda fhs, fhl: fhs / fhl)(fcmd_hours_sum, fcmd_hours_len)
			except:
				fcmd_hours_avg = 0
			else:
				# hh_time = max(fcmd_hours) if max(fcmd_hours) > fcmd_hours_avg else fcmd_hours_avg # pass_1_of_2
				# hh_time = int(3600 // hh_time) if max(fcmd_hours) < 3600 else int(hh_time // 3600) # pass_2_of_2
				hh_time = int(3600 // fcmd_hours_avg) if fcmd_hours_avg < 3600 else int(fcmd_hours_avg // 3600) # avg_without_max

				hh_avg_time = hh_time # is_debug

				print("Оптимально время для обработки в часах %d часов(а)" % hh_avg_time)
				write_log("debug fcmd_hours_avg[jobtime]", "Оптимально время для обработки в часах %d часов(а)" % hh_avg_time) # hh

			# @avg_minute / @max_minute

			try:
				fcmd_minutes_sum = sum(fcmd_minutes)
				fcmd_minutes_len = len(fcmd_minutes)
				fcmd_minutes_avg = (lambda fms, fml: fms / fml)(fcmd_minutes_sum, fcmd_minutes_len)
			except:
				fcmd_minutes_avg = 0
			else:
				# mm_time = max(fcmd_minutes) if max(fcmd_minutes) > fcmd_minutes_avg else fcmd_minutes_avg
				mm_time = fcmd_minutes_avg # avg_without_max
				mm_avg_time = mm_time

				print("Оптимально время для обработки в минутах %d минут(ы)" % mm_avg_time)
				write_log("debug fcmd_minutes_avg[jobtime]", "Оптимально время для обработки в минутах %d минут(ы)" % mm_avg_time) # mm

			# @optimial_time_for_jobs_by_xml(save) # dict's_in_list # debug(xml)

			await save_timing_to_xml(hours = hh_time, minutes = mm_time) # optimize_by_current_projects(is_ready)

			# '''
			try:
				h, m = await load_timing_from_xml(ind=1) #{'hh': '1', 'mm': '56'} # values(str) -> values(int) # 1 # is_hide
			except:
				h, m = 0, 0

			job_timing_status = "Время обработки задания загружено" if all((h, m)) else "Ошибка загрузки времени обработки задания"

			if job_timing_status.startswith("Время"):
				print(Style.BRIGHT + Fore.WHITE + "%s" % job_timing_status)
			elif job_timing_status.startswith("Ошибка"):
				print(Style.BRIGHT + Fore.RED + "%s" % job_timing_status)

			write_log("debug job_timing_status", "%s [%s]" % (job_timing_status, str(datetime.now())))
			# '''

		for pf in filter(lambda x: os.path.exists(x), tuple(proj_files)): # new(yes_gen)

			try:
				fp, fn = split_filename(pf)
			except:
				fn = pf.split("\\")[-1].strip() # fp

			try:
				fname = fn
			except:
				fname = ""

			# if not proj_files:  # skip_if_nulllist
				# break

			gl, last_file = 0, ""

			try:
				with open(vr_files, encoding="utf-8") as vff:
					ff_last = json.load(vff)
			except:
				ff_last = {}

			if ff_last:

				try:
					# dub_list = list(dub_list_gen()) # new(yes_gen)
					dub_list: list = [t.strip() for t in filter(lambda x: x.split("\\")[-1] == fname, tuple(ff_last))]
				except:
					dub_list: list = []  # old(no_gen) # t.strip() for t in filter(lambda x: x.split("\\")[-1] == fname, tuple(ff_last))

				tmp = list(set([dl.strip() for dl in filter(lambda x: x, tuple(dub_list))]))
				dub_list = sorted(tmp, reverse=False)

				len_file_list: list = []

				if len(dub_list) > 1:  # show_more_one
					print(Style.BRIGHT + Fore.GREEN + "Найдено несколько файлов с именем %s" % pf)
					len_file_list = [{"file": dl, "length": MM.get_length(dl)} for dl in
									 filter(lambda x: os.path.exists(x), tuple(dub_list)) if dl]
				# elif len(dub_list) == 1:  # hide_one
					# print(Style.BRIGHT + Fore.CYAN + "Найдено один файл с именем %s" % fname)
					# len_file_list = [{"file": dl, "length": MM.get_length(dl)} for dl in filter(lambda x: os.path.exists(x), tuple(dub_list)) if dl]

				if len_file_list:
					for lfl in len_file_list:
						print(lfl["file"], hms(lfl["length"]), end="\n")  # logging(filenames/lengths_to_time)

				funique = set()
				try:
					# tmp = list(ff_gen()) # new(yes_gen)
					tmp: list = [ff.strip() for ff in filter(lambda x: os.path.exists(x), tuple(ff_last))]
				except:
					tmp: list = []  # old(no_gen) # ff.strip() for ff in filter(lambda x: os.path.exists(x), tuple(ff_last))

				tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
				ff_last = sorted(tmp2, reverse=False)

				for ff in ff_last:  # filter(lambda x: os.path.exists(x), tuple(ff_last)):  # new(yes_gen)

					try:
						fp, fn = split_filename(ff)
					except:
						fn = ff.split("\\")[-1].strip() # fp

					try:
						fname = fn
					except:
						fname = ""
					else:
						if not fname in funique:
							funique.add(fname)

					# (mp4=mp4;any!=mp4)
					if ff.split("\\")[-1] == pf.split("\\")[-1] or \
							all((ff.split("\\")[-1].split(".")[0] == pf.split("\\")[-1].split(".")[0],
								 ff.split(".")[-1] != pf.split(".")[-1])):  # (mp4=mp4;any!=mp4)

						try:
							gl = MM.get_length(ff)
						except BaseException as e:
							gl = 0  # if_no_length
							print(Style.BRIGHT + Fore.RED + "Ошибка длина файла %s [%s]" % (pf, str(e)))
							write_log("debug file[length][error][0]",
									  "Ошибка длина файла %s [%s]" % (pf, str(e)), is_error=True)
						else:
							if gl:
								last_file = ff  # if_some_length
							# break # stop_if_find_one
					# else:
						# continue

				try:
					fp, fn = split_filename(pf)
				except:
					fn = pf.split("\\")[-1].strip() # fp

				try:
					fname = fn
				except:
					fname = ""

				if not last_file:  # skip(not_exists/no_file) # not os.path.exists(pf)
					continue

				dt = datetime.now()

				try:
					fdate, status = await datetime_from_file(pf)
				except:
					fdate, status = datetime.now(), False

				# is_merge(datalist += datalist2)
				if all((dt.day >= fdate.day, dt.month >= fdate.month, dt.year >= fdate.year)) \
						and os.path.exists(pf) and all((fname, status)):
					datelist.append({"file": [pf, fdate.hour, gl, last_file]})  # any_(day/month/year)

				elif not status:  # error_date
					continue

			# elif not proj_files:
				# print(Style.BRIGHT + Fore.WHITE + "В данный момент нет обновлений [%s]" % str(datetime.now()))
				# write_log("debug updates[no]", "В данный момент нет обновлений [%s]" % str(datetime.now()))

		del MM

		if all((proj_files, datelist)):  # need_automatic_clean

			MM = MyMeta() #2

			print(Style.BRIGHT + Fore.YELLOW + "Ищу временные файлы для переноса и удаления...")
			print("Найдено [%d] файлов для переноса и удаления" % len(datelist))

			# processes_ram: list = []
			# processes_ram2: list = []

			fsizes_list: list = []

			# sum_value = avg_value = len_value = 0

			skip_file = set()

			with unique_semaphore:
				for dl in datelist:

					if not datelist:  # no_data
						break

					if not os.path.exists(dl["file"][3]):
						continue

					try:
						fname = dl["file"][3].split("\\")[-1].strip()
					except:
						fname = ""

					try:
						fnshort = fname.split(".")[0].strip()
					except:
						fnshort = ""
					else:
						if any((fnshort.count(".") > 1,
								fname.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"])) and all(
							(fnshort, fname)):  # sep_no_ext/temp_ext
							print(Style.BRIGHT + Fore.RED + "Файл %s пропущен, т.к. он закачивается" % dl["file"][3])

							write_log("debug skipfile[debug]",
									"Файл %s пропущен, т.к. включен режим отладки" % dl["file"][3])

							if not fnshort in skip_file:
								skip_file.add(fnshort)

			try:
				fsizes_list: list = [os.path.getsize(dl["file"][0]) for dl in datelist if
									os.path.exists(dl["file"][0])]
			except:
				fsizes_list: list = []
			else:
				fsizes_list.sort(reverse=False)

			try:
				avg_size = await avg_lst(list(set(fsizes_list))) # asyncio.run(
			except:
				try:
					avg_size = sum(fsizes_list) // len(fsizes_list)
				except:
					avg_size = 0

			# clean_project_from_base: list = []

			with unique_semaphore:
				for dl in datelist:

					# print(dl["file"], "1", end="\n")

					if not datelist:  # no_data
						break

					if not os.path.exists(dl["file"][3]):
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
						print(Style.BRIGHT + Fore.RED + "Ошибка длина файла[1] %s [%s]" % (fullname, str(e)))
						write_log("debug file[length][error][1]", "Ошибка длина файла %s [%s]" % (fullname, str(e)), is_error=True)
					else:
						if not isinstance(gl1, int):
							gl1 = int(gl1)

					gl2: int = 0

					try:
						# if os.path.exists(fullname2):
						gl2 = MM.get_length(fullname2)  # original # dl["file"][2]
					except BaseException as e:
						gl2 = 0

						print(Style.BRIGHT + Fore.RED + "Ошибка длина файла[2] %s [%s]" % (fullname, str(e)))
						write_log("debug file[length][error][2]", "Ошибка длина файла %s [%s]" % (fullname, str(e)), is_error=True)
					else:
						if not isinstance(gl2, int):
							gl2 = int(gl2)

					try:
						if all((gl2 == dl["file"][2], dl["file"][2], gl2)):
							gl2 = dl["file"][2]  # read_from_dict(equal)
					except:
						gl2 = 0

					if (not os.path.exists(fullname) or not os.path.exists(fullname2)):
						print(Style.BRIGHT + Fore.CYAN + "Нет файла [%s] обработки или переноса" % fullname)

						write_log("debug file[skip][1]", "Нет файла [%s] обработки или переноса" % fullname)

					if all((isinstance(gl1, int), isinstance(gl2, int))) and os.path.exists(fullname):

						print(Style.BRIGHT + Fore.GREEN + "Длина(час:мин): [%s], файл: [%s]" % (hms(gl1), fullname))

						write_log("debug file[lengths]", "Длина(час:мин): [%s], файл: [%s]" % (hms(gl1), fullname))

						if all((gl1, gl2)) and os.path.exists(fullname):  # debug/test
							try:
								fsize: int = os.path.getsize(fullname)
								dsize: int = disk_usage(fullname2[0] + ":\\").free
							except:
								fsize: int = 0
								dsize: int = 0
							else:
								if all((fsize, dsize, int(fsize // (dsize / 100)) <= 100)):
									if all((fullname.split("\\")[-1] == fullname2.split("\\")[-1],
											fullname != fullname2)):  # mp4 # skip_any_logic

										try:
											gl1 = MM.get_length(fullname)  # mp4_file(project)
										except:
											gl1 = 0

										try:
											# if os.path.exists(fullname2):
											gl2 = MM.get_length(fullname2)  # job_file(job)
										except:
											gl2 = 0

										try:
											is_new = (os.path.exists(fullname) and not os.path.exists(fullname2))
										except:
											is_new = False

										try:
											is_update = (os.path.exists(fullname) and os.path.exists(fullname2))
										except:
											is_update = False

										is_clean = all((gl1 in range(gl2, gl2 - 5, -1), gl1, gl2))  # tv_series

										if all((is_clean, fullname2[0] >= fullname[0])) and os.path.exists(
												fullname):  # move_or_update_by_project(by_base)
											print(Style.BRIGHT + Fore.WHITE + "Правильная длина файла %s" % fullname)

											write_log("debug destonationfile[mp4]",
													"Правильная длина файла %s" % fullname)

											# load_meta_jobs(filter) #3
											try:
												with open(some_base, encoding="utf-8") as sbf:
													somebase_dict = json.load(sbf)
											except:
												somebase_dict = {}

												with open(some_base, "w", encoding="utf-8") as sbf:
													json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

											first_len: int = len(somebase_dict)

											# clean_project_from_base.append(fullname2)

											somebase_dict = {k: v for k, v in somebase_dict.items() if os.path.exists(k)}  # exists_only # pass_1_of_2
											somebase_dict = {k: v for k, v in somebase_dict.items() if k != fullname2}  # clear_if_ready(delete)  # tv_series(big_cinema) # pass_2_of_2

											second_len: int = len(somebase_dict)

											if all((second_len, second_len <= first_len)):  # clear_ready(optimized_file)
												with open(some_base, "w", encoding="utf-8") as sbf:
													json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

												print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
												Style.BRIGHT + Fore.WHITE + "%s" % fullname)  # add_to_all(process_move)

											if all((os.path.getsize(fullname) <= avg_size, avg_size)):

												print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
											Style.BRIGHT + Fore.WHITE + "%s" % fullname)  # add_to_all(process_move)

											# @load_current_jobs
											try:
												with open(filecmd_base, encoding="utf-8") as fbf:
													fcmd = json.load(fbf)
											except: # IOError
												fcmd = {}

												with open(filecmd_base, "w", encoding="utf-8") as fbf:
													json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)

											first_len = len(fcmd)

											fcmd = {k: v for k, v in fcmd.items() if os.path.exists(k) and any((k.strip() in [*somebase_dict], not [*somebase_dict]))}

											second_len = len(fcmd)

											if all((second_len, second_len <= first_len)):
												with open(filecmd_base, "w", encoding="utf-8") as fbf:
													json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)

										# p = multiprocessing.Process(target=process_move, args=(fullname, fullname2, False, True, avg_size))  # avg_value

										try:
											await process_move(fullname, fullname2, False, True, avg_size) # no_asyncio.run # async_if_small #1
										except BaseException as e:
											write_log("debug process_move[error][1]", ";".join([fullname, fullname2, str(e)]))
										else:
											write_log("debug process_move[ok][1]", ";".join([fullname, fullname2]))


										if not fullname in processes_ram:
											processes_ram.append(fullname)

										'''
										if not p in processes_ram and os.path.exists(
												fullname) and os.path.exists(fullname2) and \
												fullname.split("\\")[-1].lower() == fullname2.split("\\")[
											-1].lower():
											p.start()
											processes_ram.append(p)
										'''

									elif all((os.path.getsize(fullname) > avg_size, avg_size)) or not avg_size:
										move(fullname, fullname2) # no_async_if_big

										if is_new:
											print(Style.BRIGHT + Fore.GREEN + "Файл",
												Style.BRIGHT + Fore.WHITE + "%s" % full_to_short(fullname),
												Style.BRIGHT + Fore.YELLOW + "надо записать в",
												Style.BRIGHT + Fore.CYAN + "%s" % fullname2)  # is_another_color

											write_log("debug movefile[need][mp4]",
													"Файл %s надо записать в %s" % (fullname, fullname2))

										elif is_update:
											print(Style.BRIGHT + Fore.YELLOW + "Файл",
												Style.BRIGHT + Fore.WHITE + "%s" % full_to_short(fullname),
												Style.BRIGHT + Fore.YELLOW + "надо обновить в",
												Style.BRIGHT + Fore.CYAN + "%s" % fullname2)  # is_another_color

											write_log("debug movefile[need][mp4]",
													"Файл %s надо обновить в %s" % (fullname, fullname2))

								elif not is_clean and os.path.exists(
										fullname):  # fullname2[0] >= fullname[0] # delete_error_project(by_base)

									print(Style.BRIGHT + Fore.RED + "Неправильная длина файла %s" % fullname)

									write_log("debug destonationfile[mp4]",
											"Неправильная длина файла %s" % fullname)

									# p = multiprocessing.Process(target=process_delete, args=(fullname,))

									await process_delete(fullname)

									if not fullname in processes_ram2:
										processes_ram2.append(fullname)

									'''
									if not p in processes_ram2 and os.path.exists(fullname):
										p.start()
										processes_ram2.append(p)
									'''

									# os.remove(fullname)

									if os.path.exists(fullname):
										print(Style.BRIGHT + Fore.YELLOW + "Удаление файла %s" % fullname)

										write_log("debug deletefile!", "Удаление файла %s" % fullname)
									elif not os.path.exists(fullname):
										print(Style.BRIGHT + Fore.GREEN + "Удаление файла %s" % fullname)

										write_log("debug deletefile[mp4]", "Удаление файла %s" % fullname)

			del MM

			print()

			len_proc: int = len(processes_ram) + len(processes_ram2) # is_hide

			if len_proc:
				MySt = MyString() # MyString("Запускаю:", "[1 из 7]")

				try:
					print(Style.BRIGHT + Fore.CYAN + MySt.last2str(
						maintxt="Запускаю:", endtxt="[1 из 7]", count=len_proc, kw="задач"))
					# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
				except:
					print(Style.BRIGHT + Fore.YELLOW + "Обновляю или удаляю %d файлы(а,ов) [1 из 7]" % len_proc)  # old(is_except)
				else:
					write_log("debug run[task1]", MySt.last2str(
						maintxt="Запускаю:", endtxt="[1 из 7]", count=len_proc, kw="задач"))

				del MySt

			if len(proj_files) >= 0:
				temp = [True if os.path.exists(pf) else False for pf in proj_files]

				if temp.count(True):
					try:
						# temp2 = list(pf_gen()) # new(yes_gen)
						temp2: list = [pf.strip() for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))]
					except:
						temp2: list = []  # old(no_gen) # pf.strip() for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))

					tmp = list(set([t2.strip() for t2 in filter(lambda x: x, tuple(temp2))]))
					proj_files = sorted(tmp, reverse=False)

					print(Style.BRIGHT + Fore.WHITE + "Осталось %d задачи(и), которые надо очистить" % temp.count(True))
					write_log("debug files[project][count][+]",
					  "Осталось %d задач(и), которые надо очистить" % temp.count(True))

					with unique_semaphore:
						for pf in proj_files:  # filter(lambda x: x, tuple(temp2))

							if not proj_files: # no_data
								break

							try:
								fname = pf.split("\\")[-1].strip()
							except:
								fname = ""

							try:
								if os.path.exists(pf):
									os.remove(pf)
							except:
								continue

			elif temp.count(False):
				print(Style.BRIGHT + Fore.WHITE + "Файлов нету или все %d задач(и) обработаны" % temp.count(False))
				write_log("debug files[project][count][-]",
					  "Файлов нету или все %d задач(и) обработаны" % temp.count(False))

		# if_stay_files(clear_him) # pass_2_of_2 # debug
		try:
			proj_list = os.listdir(path_to_done)
		except:
			proj_list = []

		try:
			if proj_list:
				proj_files: list = ["".join([path_to_done, pl]) for pl in proj_list if os.path.exists("".join([path_to_done, pl])) and video_ext_regex.findall(pl) and all((
										pl.count(".") == 1, not pl.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]))]  # only_normal(files_by_tempate)
		except:
			proj_files: list = []

		if all((len(proj_list) > 0, len(proj_list) <= len(proj_files))):
			cnt = len(proj_list)
			err = 0

			for pl in filter(lambda x: os.path.exists(x), tuple(proj_list)):
				try:
					if os.path.exists(pl):
						os.remove(pl)
						print(Style.BRIGHT + Fore.WHITE + "%s [%d]" % (full_to_short(pl), cnt)) # is_color
						write_log("debug proj_list[delete]", "%s [%d]" % (pl, cnt))
						cnt -= 1
				except BaseException as e:
					print(Style.BRIGHT + Fore.RED + "%s [%s]" % (full_to_short(pl), str(e)))
					write_log("debug proj_list[error]", "%s [%s]" % (pl, str(e)))
					err += 1
			if all((len(proj_list) > 0, err >= 0)):
				write_log("debug [projects/error][count]", "%d [%d]" % (len(proj_list), err))

		write_log("debug end[project_done]", "%s" % str(datetime.now()))

	# (2914 // 3600, (2914 // 60) % 60, 2914 % 60) # (0, 48, 34)
	async def hh_mm_ss(legth: int = 0) -> str:

		try:
			assert length, "Ну указано сколько время ms надо конвертировать @hh_mm_ss/length" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Ну указано сколько время ms надо конвертировать @hh_mm_ss/length")
			raise err
			return (0, 0, 0, False)

		# if not length:
			# return (0, 0, 0, False) # if_no_data

		try:
			val1 = length // 3600 # >>> 2914 // 3600 # 0 # hh
		except:
			val1 = 0

		try:
			val2 = (length // 60) % 60 # >>> (2914 // 60) % 60 # 48 # mm
		except:
			val2 = 0

		try:
			val3 = length % 60 # >>> 2914 % 60 # 34 # ss
		except:
			val3 = 0

		if all((not val1, not val2, not val3)): # if_error_or_null
			return (0, 0, 0, False)

		if any((val1, val2, val3)):
			return (val1, val2, val3, True) # hour_and_minute_and_seconds


	# pass_x_of_4
	async def project_update(is_debug: bool = False):  # update_downloaded_files(tvseries/cinema) # debug
		# copy_src - tvseries(update_folder), copy_src2 - cinema(update_folder), move_dst - @path_for_folder1(local_project)

		path1: str = copy_src
		path2: str = copy_src2
		path3: str = path_for_folder1

		# return

		# hidden(skip_check_exist_folder)
		if not os.path.exists(path1) or not os.path.exists(path2) or not os.path.exists(path3):
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
				if os.path.exists("".join([path1, fl])) and all((fl, fl.count(".") == 1, video_ext_regex.findall(fl))): # os.path.isfile("".join([path1, fl]))
					copy_src_list1.append("".join([path1, fl]).strip())
		except BaseException as e:
			copy_src_list1 = []

			print(Style.BRIGHT + Fore.RED + "%s" % str(e))
			write_log("debug copy_src_list1[error]", "%s" % str(e), is_error=True)

		try:
			files += copy_src_list1
		except:
			pass
		else:
			write_log("debug copy_src_list1[files]","[%d] %d" % (len(copy_src_list1), len(files)))

		try:
			# tmp_dict = {crop_filename_regex.sub("", fn).strip(): str(datetime.now()) for csl1 in copy_src_list1 for fp, fn in split_filename(csl1) if all((fn, csl1, fn == csl1.split("\\")[-1]))}  # new_files(project/short)
			tmp_dict = {crop_filename_regex.sub("", csl1.split("\\")[-1]).strip(): str(datetime.now()) for csl1 in copy_src_list1 if csl1} # new_files(project/short)
		except BaseException as e:
			tmp_dict = {}

			write_log("debug copy_src_list1[error]!", "%s" % str(e), is_error=True)
		finally:
			write_log("debug copy_src_list1", ";".join([*tmp_dict]))  # copy_src_list1

		# skip_file1: list = []  # skip_files2

		# a = "a.b.c.d"; ".".join(a.split(".")[0:-2]) # a.b.c # with_sep # "".join(a.split(".")[0:-2]) # abc # no_sep
		# ".".join(fl.split(".")[0:-1]).strip()
		try:
			temp = list(set([fl.split(".")[0].strip() for fl in os.listdir(path1) if fl.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]]))

			skip_file1 = sorted(temp, reverse=False)
			# skip_file1 = sorted(temp, key=len, reverse=False)
		except:
			skip_file1 = []

		list1: list = []
		# lst1: list = [] # is_debug

		try:
			for fl in os.listdir(path1):
				if os.path.exists("".join([path1, fl])) and fl.count(".") > 1 and (not fl.split(".")[0].strip() in skip_file1 or not skip_file1) and not video_ext_regex.findall(fl): # os.path.isfile("".join([path1, fl]))
					list1.append("".join([path1, fl]).strip())
		except BaseException as e:
			list1 = []

			write_log("debug list1[error]!", "%s" % str(e), is_error=True)
		# else:
			# if os.listdir(path1):
				# for fn in os.listdir(path1):
					# lst1.append(fn.split(".")) # filename_in_path1

				# if lst1:
					# pass

		try:
			list_total += list1
		except:
			pass
		else:
			write_log("debug list1[list_total]","[%d] %d" % (len(list1), len(list_total)))

		copy_src_list2: list = []

		try:
			for fl in os.listdir(path2):
				if os.path.exists("".join([path2, fl])) and all((fl, fl.count(".") == 1, video_ext_regex.findall(fl))): # os.path.isfile("".join([path2, fl]))
					copy_src_list2.append("".join([path2, fl]).strip())
		except BaseException as e:
			copy_src_list2 = []

			print(Style.BRIGHT + Fore.RED + "%s" % str(e))
			write_log("debug copy_src_list2[error]", "%s" % str(e), is_error=True)

		try:
			files += copy_src_list2
		except:
			pass
		else:
			write_log("debug copy_src_list2[files]","[%d] %d" % (len(copy_src_list2), len(files)))

		try:
			# tmp_dict = {crop_filename_regex.sub("", fn).strip(): str(datetime.now()) for csl2 in copy_src_list2 for fp, fn in split_filename(csl2) if all((fn, csl2, fn == csl2.split("\\")[-1]))}  # new_files(project/short)
			tmp_dict = {crop_filename_regex.sub("", csl2.split("\\")[-1]).strip(): str(datetime.now()) for csl2 in copy_src_list2 if csl2} # new_files(project/short)
		except BaseException as e:
			tmp_dict = {}

			write_log("debug copy_src_list2[error]!", "%s" % str(e), is_error=True)
		finally:
			write_log("debug copy_src_list2", ";".join([*tmp_dict]))  # copy_src_list2

		# ".".join(fl.split(".")[0:-1]).strip()
		try:
			temp = list(set([fl.split(".")[0].strip() for fl in os.listdir(path2) if fl.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]]))

			skip_file2 = sorted(temp, reverse=False)
			# skip_file2 = sorted(temp, key=len, reverse=False)
		except:
			skip_file2 = []

		list2: list = []

		try:
			for fl in os.listdir(path2):
				if os.path.exists("".join([path2, fl])) and fl.count(".") > 1 and (not fl.split(".")[0].strip() in skip_file2 or not skip_file2) and not video_ext_regex.findall(fl): # os.path.isfile("".join([path2, fl]))
					list2.append("".join([path2, fl]).strip())
		except BaseException as e:
			list2 = []

			write_log("debug list2[error]!", "%s" % str(e), is_error=True)

		try:
			list_total += list2
		except:
			pass
		else:
			write_log("debug list2[list_total]","[%d] %d" % (len(list2), len(list_total)))

		# 7f_...
		try:
			temp = list(set([lt.split("\\")[-1].split(".")[0] for lt in list_total if lt.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]]))

			skip_copy = sorted(temp, reverse=False)
			# skip_copy = sorted(temp, key=len, reverse=False)
		except:
			skip_copy = []

		copy_src_list3: list = []

		try:
			# copy_src_list3 = list(set(["".join([path3, fn]).strip() for fl in files for fp, fn in split_filename(fl) if all((fl, fn, fn == fl.split("\\")[-1], fn.count(".") == 1))])) # os.path.isfile(fl)
			copy_src_list3 = list(set(["".join([path3, fl.split("\\")[-1]]).strip() for fl in files if all((fl, fl.split("\\")[-1].count(".") == 1))])) # ?
		except BaseException as e:
			copy_src_list3 = []

			print(Style.BRIGHT + Fore.RED + "%s" % str(e))
			write_log("debug copy_src_list3[error]", "%s" % str(e), is_error=True)
		else:
			write_log("debug copy_src_list3[files]","[%d] %d" % (len(copy_src_list3), len(files))) # move_files_from_downloads / concatinate_files

		try:
			tmp_dict = {crop_filename_regex.sub("", csl3.split("\\")[-1]).strip(): str(datetime.now()) for csl3 in copy_src_list3 if csl3}
			# tmp_dict = {crop_filename_regex.sub("", fn).strip(): str(datetime.now()) for csl3 in copy_src_list3 for fp, fn in split_filename(csl3) if all((fn, csl3, fn == csl3.split("\\")[-1]))}  # new_files(project/short)

		except BaseException as e:
			tmp_dict = {}

			write_log("debug copy_src_list3[error]!", "%s" % str(e), is_error=True)
		finally:
			write_log("debug copy_src_list3", ";".join([*tmp_dict]))  # copy_src_list3

		# filter_old_file_for_delete_by_compare

		# @log_error
		async def filter_date_file(lst: list = []):

			try:
				# tmp = list(l_gen()) # new(yes_gen)
				tmp: list = [l.strip() for l in filter(lambda x: os.path.exists(x), tuple(lst))]
			except:
				tmp: list = []  # old(no_gen) # l.strip() for l in filter(lambda x: os.path.exists(x), tuple(lst))

			tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
			lst = sorted(tmp2, reverse=False)

			for l in lst:  # filter(lambda x: os.path.exists(x), tuple(lst)):  # new(yes_gen)

				if not lst:  # skip_if_nulllist
					break

				if os.path.exists(l):
					os.remove(l)

					print(Style.BRIGHT + Fore.CYAN + "Старый файл %s был удалён и оставлен более свежий" % l)

					write_log("debug filter_date_file", "Старый файл %s был удалён и оставлен более свежий" % l)

		# filter_by_date_if_equal_filename # (path1[update]/path3[project]):(path2[update]/path3[project]) # filter_tvseries(bigfilms)

		# pass_1_of_2

		def csl_date_filter(first=copy_src_list1, second=copy_src_list3):
			for csl1 in first:
				for csl3 in second:
					if all((mdate_by_days(filename=csl1,is_any=True) > mdate_by_days(filename=csl3, is_any=True), csl1.split("\\")[-1] == csl3.split("\\")[-1], all((csl1 < csl3, csl1 != csl3)), csl1, csl3)):
						yield csl3.strip()

		filter_date: list = []

		try:
			# filter_date = [csl3.strip() for csl1 in copy_src_list1 for csl3 in copy_src_list3 if all((mdate_by_days(filename=csl1) > mdate_by_days(filename=csl3), csl1.split("\\")[-1] == csl3.split("\\")[-1], csl1, csl3))]
			filter_date = list(set(csl_date_filter(first=copy_src_list1)))
		except:
			filter_date = []  # if_some_error
		finally:
			if filter_date:
				await filter_date_file(filter_date)  # 1>"3" # asyncio.run

		# pass_2_of_2

		try:
			# filter_date = [csl3.strip() for csl2 in copy_src_list2 for csl3 in copy_src_list3 if all((mdate_by_days(filename=csl2) > mdate_by_days(filename=csl3), csl2.split("\\")[-1] == csl3.split("\\")[-1], csl2, csl3))]
			filter_date = list(set(csl_date_filter(first=copy_src_list2)))
		except:
			filter_date = []  # if_some_error
		finally:
			if filter_date:
				await filter_date_file(filter_date)  # 2>"3" # asyncio.run

		# print(files, copy_src_list3, "project_update", end="\n")

		# parse_to_normal_file
		# """
		if len(list_total) > 0:

			try:
				tmp = len(list_total) // 2 if list_total else 0
			except:
				tmp = 0

			# list_total_tmp -> tmp
			print(Style.BRIGHT + Fore.YELLOW + "Найдено", Style.BRIGHT + Fore.WHITE + "%d" % tmp,
				Style.BRIGHT + Fore.YELLOW + "файлов для преобразования и проверки")
			write_log("debug parse[convert][filter]", "Найдено %d файлов для преобразования и проверки" % tmp)

			full_list = moved_list = set()

			move_files: list = []

			try:
				# tmp = list(lt_gen()) # new(yes_gen)
				tmp = [lt.strip() for lt in filter(lambda x: os.path.exists(x), tuple(list_total))]
			except:
				tmp = []  # old(no_gen) # lt.strip() for lt in filter(lambda x: os.path.exists(x), tuple(list_total))

			tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
			list_total = sorted(tmp2, reverse=False)

			for lt in list_total:  # filter(lambda x: os.path.exists(x), tuple(list_total)):  # new(yes_gen)

				# if not list_total:  # no_data
					# break

				try:
					fname = lt.split("\\")[-1].strip()
				except:
					fname = ""

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
					parsefile = await seasonvar_parse(lt, is_log=False) # filename=lt(args) -> lt(no_args)
				except:
					parsefile = None
					continue # if_error_skip_current_file # pass_1_of_2

				try:
					if len(parsefile.split("$")) == 2 and os.path.exists(parsefile.split("$")[0]) and parsefile != None:

						try:
							part1, *part2, part3 = parsefile.split("$")[1].split("\\")[-1].split(".")
						except:
							part1 = part2 = part3 = ""
						else:
							filename_parts = (part1, *part2, part3)
							write_log("debug filename[parsed]", "%s [%d]" % (parsefile.split("$")[1], len(filename_parts)))

						# parsefile.split("$")[1] # clear_word_startswith_if_need(rename_main_file)

						# add_to_all(process_move)
						print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
							Style.BRIGHT + Fore.WHITE + "%s" % parsefile.split("$")[0])

						# hidden_when_debug_parse_code # debug/test
						# """
						# p = multiprocessing.Process(target=process_move, args=(parsefile.split("$")[0], parsefile.split("$")[1], False, False, 0)) # src/dst/move(False)/diff(False)

						try:
							await process_move(parsefile.split("$")[0], parsefile.split("$")[1], False, False, 0) # no_asyncio.run #2
						except BaseException as e:
							write_log("debug process_move[error][2]", ";".join([parsefile.split("$")[0], parsefile.split("$")[1], str(e)]))
						else:
							write_log("debug process_move[ok][2]", ";".join([parsefile.split("$")[0], parsefile.split("$")[1]]))

						try:
							if not parsefile.split("$")[0] in move_files:
								move_files.append(parsefile.split("$")[0])
						except BaseException as e:
							write_log("debug move_files[append][error]", "%s [%s]" % (parsefile.split("$")[0], str(e)), is_error=True)
							pass # if_error_nothing_to_do
						else:
							write_log("debug move_files[append]", "%s" % parsefile.split("$")[0])

						try:
							if not parsefile.split("$")[0] in moved_list:
								moved_list.add(parsefile.split("$")[0])
						except BaseException as e:
							write_log("debug moved_list[add][error]", "%s [%s]" % (parsefile.split("$")[0], str(e)), is_error=True)
							pass # if_error_nothing_to_do
						else:
							write_log("debug moved_list[add]", "%s" % parsefile.split("$")[0])

						# move(parsefile.split("$")[0], parsefile.split("$")[1])
						# """

				except BaseException as e:
					# Обработка файла c:\downloads\combine\original\tvseries\hello..world.txt
					# Ошибка парсинга файла ['NoneType' object has no attribute 'split']
					print(Style.BRIGHT + Fore.RED + "Ошибка парсинга файла %s [%s]" % (lt, str(e)))
					write_log("debug parsefile[error]", "Ошибка парсинга файла %s [%s]" % (lt, str(e)), is_error=True)
					continue

				try:
					if len(parsefile.split("$")) == 2 and os.path.exists(parsefile.split("$")[0]) and parsefile != None:
						# full_to_short # drive + short_filename
						try:
							dfile1, dfile2 = parsefile.split("$")[0], parsefile.split("$")[1]
						except:
							dfile1 = dfile2 = ""
						else:
							if all((dfile1, dfile2)):
								print(Style.BRIGHT + Fore.BLUE + "%s" % "=->".join([full_to_short(dfile1), dfile2])) # parse_filename

								print(Style.BRIGHT + Fore.GREEN + "Успешный парсинга файла %s [%s]" % (dfile1, dfile2))
								write_log("debug parsefile[ok]", "Успешный парсинга файла %s [%s]" % (parsefile.split("$")[0], parsefile.split("$")[1]))
					elif any((len(parsefile.split("$")) != 2, parsefile == None)):
						print(Style.BRIGHT + Fore.RED + "Неизвестный парсинга файла %s" % str(parsefile))
						write_log("debug parsefile[unknown]", "Неизвестный парсинга файла %s" % str(parsefile)) # some_value
						continue # if_error_parse_skip_current_file # pass_2_of_2
				except:
					pass # if_error_nothing_to_do

			if len(list_total) > 0:
				print(Style.BRIGHT + Fore.YELLOW + "Найдено %d задач(и) для проверки" % len(list_total))
				write_log("debug parser[job][count]", "Найдено %d задач(и) для проверки" % len(list_total))

			if abs(len(list_total) - len(moved_list)) > 0:
				print(Style.BRIGHT + Fore.WHITE + "Не переименовалось %d файлов(а)" % abs(len(list_total) - len(moved_list)))
				write_log("debug parser[job][no_update]",
						  "Не переименовалось %d файлов(а)" % abs(len(list_total) - len(moved_list)))

			# move_files(task_count)
			if len(moved_list) > 0:
				print(Style.BRIGHT + Fore.CYAN + "Переименовалось",
					Style.BRIGHT + Fore.WHITE + "%d" % len(moved_list),
					Style.BRIGHT + Fore.CYAN + "файлов(а)")
				write_log("debug parser[job][update]", "Переименовалось %d файлов(а)" % len(moved_list))

			# print()

			print(Style.BRIGHT + Fore.YELLOW + "Обработанные файлы перенесутся при следующем запуске")

		# """

		if copy_src_list3:

			skip_file = set()

			with unique_semaphore:
				for fl in copy_src_list3:  # new_files(project) # dont_check_exists

					if not copy_src_list3:  # no_data
						break

					try:
						fname = fl.split("\\")[-1].strip()
					except:
						fname = ""

					try:
						fnshort = fname.split(".")[0].strip()
					except:
						fnshort = ""
					else:
						if any((fnshort.count(".") > 1,	fname.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"])) and all((fnshort, fname)):  # skip_downloaded(temporary_download)
							print(Style.BRIGHT + Fore.RED + "Файл %s пропущен, т.к. он закачивается" % lf)
							write_log("debug skipfile[debug]", "Файл %s пропущен, т.к. включен режим отладки" % lf)

							if not fnshort in skip_file:
								skip_file.add(fnshort)

						# continue

			with unique_semaphore:
				for fl in copy_src_list3:  # dont_check_exists

					if not copy_src_list3:  # no_data
						break

					try:
						fname = fl.split("\\")[-1].strip()
					except:
						fname = ""

					try:
						fnshort = fname.split(".")[0].strip()
					except:
						fnshort = ""
					else:
						if all((fnshort in skip_file, fnshort, skip_file)):
							continue

					if video_ext_regex.findall(fname):  # with_short_video_by_template # debug(off)
						if os.path.exists("".join([path3, fl.split("\\")[-1]])):
							files_for_job.append({"file": fl.strip(), "file2": "".join([path3, fl.split("\\")[-1]]).strip(), "status": "update", "debug": is_debug})
						elif not os.path.exists("".join([path3, fl.split("\\")[-1]])):
							files_for_job.append({"file": fl.strip(), "file2": "".join([path3, fl.split("\\")[-1]]).strip(), "status": "add", "debug": is_debug})

		if all((len(copy_src_list3) > 0, len(files_for_job) > 0)):
			print(Style.BRIGHT + Fore.CYAN + "Файлов %d для обновления %d проектов" % (len(copy_src_list3), len(files_for_job)))
			write_log("debug projects[yes]",
					  "Файлов %d для обновления %d проектов" % (len(copy_src_list3), len(files_for_job)))
		elif all((len(copy_src_list3) > 0, len(files_for_job) == 0)):
			print(Style.BRIGHT + Fore.CYAN + "Файлов %d для обновления" % len(copy_src_list3))
			write_log("debug projects[yes]", "Файлов %d для обновления" % len(copy_src_list3))
		elif all((not copy_src_list3, not files_for_job)):
			print(Style.BRIGHT + Fore.CYAN + "Нет файлов для обновления проектов")
			write_log("debug projects[no]", "Нет файлов для обновления проектов")

			return # if_no_files(exit_from_function)

		try:
			files2 = {fl.strip(): csl3.strip() for fl in files for csl3 in copy_src_list3 if all((fl, csl3, fl.split("\\")[-1] == csl3.split("\\")[-1]))}  # csl3(new_files(project))
		except:
			files2 = {}

		# print(files2, end="\n") # dict

		processes_ram: list = []
		processes_ram2: list = []

		fsizes_list: list = []

		# sum_value = avg_value = len_value = 0

		skip_file = set()

		for ffj in files2:  # is_dict

			if not files2:  # no_data
				break

			try:
				fname = ffj.split("\\")[-1].strip()
			except:
				fname = ""

			try:
				fnshort = fname.split(".")[0].strip()
			except:
				fnshort = ""
			else:
				if any((fnshort.count(".") > 1, fname.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"])) and all((fnshort, fname)):  # skip_downloaded(temporary_download)
					print(Style.BRIGHT + Fore.RED + "Файл %s пропущен, т.к. он закачивается" % ffj)

					write_log("debug skipfile[debug]", "Файл %s пропущен, т.к. включен режим отладки" % ffj)

					if all((not fnshort in skip_file, fnshort)):
						skip_file.add(fnshort)

				# continue

		if files2 and not os.path.isfile(path3):  # project_files

			try:
				fsizes_list: list = list(set([os.path.getsize(ffj) for ffj in files2 if os.path.exists(ffj)]))
			except:
				fsizes_list: list = []
			else:
				fsizes_list.sort(reverse=False)

			try:
				avg_size = await avg_lst(list(set(fsizes_list))) # asyncio.run
			except:
				try:
					avg_size = sum(fsizes_list) // len(fsizes_list)
				except:
					avg_size = 0

			for ffj in files2:  # is_dict

				if not files2: # no _data
					break

				try:
					dfile1, dfile2 = ffj, files2[ffj]
				except:
					dfile1 = dfile2 = ""
				finally:
					if all((dfile1, dfile2)):
						print(Style.BRIGHT + Fore.BLUE + "%s" % "=->".join([full_to_short(dfile1), dfile2])) # move_downloads_files

				try:
					fname = ffj.split("\\")[-1].strip()
				except:
					fname = ""

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
					is_new = (os.path.exists(ffj) and not os.path.exists(files2[ffj]))
				except:
					is_new = False

				try:
					is_update = (os.path.exists(ffj) and os.path.exists(files2[ffj]))
				except:
					is_update = False

				try:
					if os.path.exists(ffj) and any((is_new, is_update)) and fspace(ffj, files2[ffj]):  # new/update # fspace
						if is_debug == True:
							if all((fsize2, is_update)):
								print(Style.BRIGHT + Fore.YELLOW + "Будет обновлено",
									  Style.BRIGHT + Fore.WHITE + "%s" % "=>".join([dfile1, dfile2]))
								write_log("debug movefile[update]!",
										  "Будет обновлено %s" % "=>".join([ffj, files2[ffj]]))
							elif all((not fsize2, is_new)):
								print(Style.BRIGHT + Fore.GREEN + "Будет добавлено",
									  Style.BRIGHT + Fore.WHITE + "%s" % "=>".join([dfile1, dfile2]))
								write_log("debug movefile[add]!",
										  "Будет добавлено %s" % "=>".join([ffj, files2[ffj]]))
						elif is_debug == False:
							# print(Style.BRIGHT + Fore.CYAN + "Было добавлено или обновлено", Style.BRIGHT + Fore.WHITE + "%s" % "~>".join([dfile1, dfile2]))
							# write_log("debug movefile[update]", "Было добавлено или обновлено %s" % "~>".join([dfile1, dfile2]))

							if all((os.path.getsize(ffj) <= avg_size, avg_size)):
								print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
									  Style.BRIGHT + Fore.WHITE + "%s" % ffj)  # add_to_all(process_move)

								# p = multiprocessing.Process(target=process_move, args=(ffj, files2[ffj], False, True, avg_size))  # avg_value

								try:
									await process_move(ffj, files2[ffj], False, True, avg_size) # no_asyncio.run # async_if_small #3
								except BaseException as e:
									write_log("debug process_move[error][3]", ";".join([ffj, files2[ffj], str(e)]))
								else:
									write_log("debug process_move[ok][3]", ";".join([ffj, files2[ffj]]))

								if not ffj in processes_ram:
									processes_ram.append(ffj)

								'''
								if not p in processes_ram:
									p.start()
									processes_ram.append(p)
								'''

							elif all((os.path.getsize(ffj) > avg_size, avg_size)) or not avg_size:
								move(ffj, files2[ffj]) # no_async_if_big

								if is_new:
									print(Style.BRIGHT + Fore.GREEN + "Файл",
										  Style.BRIGHT + Fore.WHITE + "%s" % ffj,
										  Style.BRIGHT + Fore.YELLOW + "надо записать в",
										  Style.BRIGHT + Fore.CYAN + "%s" % files2[ffj])  # is_another_color # dfile2
									write_log("debug movefile[need]",
											  "Файл %s надо записать в %s" % (ffj, files2[ffj]))

								elif is_update:
									print(Style.BRIGHT + Fore.YELLOW + "Файл",
										  Style.BRIGHT + Fore.WHITE + "%s" % ffj,
										  Style.BRIGHT + Fore.YELLOW + "надо обновить в",
										  Style.BRIGHT + Fore.CYAN + "%s" % files2[ffj])  # is_another_color # dfile2
									write_log("debug movefile[need]",
											  "Файл %s надо обновить в %s" % (ffj, files2[ffj]))

					elif os.path.exists(ffj) and all((fsize1 == fsize2, fsize1, fsize2)):  # delete
						if is_debug == True:
							print(Style.BRIGHT + Fore.CYAN + "Будет удалено",
								  Style.BRIGHT + Fore.WHITE + "%s" % dfile1)
							write_log("debug deletefile[update]!", "Будет удалено %s" % ffj)
						elif is_debug == False:
							# print(Style.BRIGHT + Fore.BLUE + "Было удалено", Style.BRIGHT + Fore.WHITE + "%s" % dfile1)
							# write_log("debug deletefile[update]", "Было удалено %s" % dfile1)

							# p = multiprocessing.Process(target=process_delete, args=(ffj,))

							await process_delete(ffj) # async_if_delete

							if not ffj in processes_ram2:
								processes_ram2.append(ffj)

							'''
							if not p in processes_ram2:
								p.start()
								processes_ram2.append(p)
							'''

						# os.remove(ffj["file"])
				except BaseException as e:
					print(Style.BRIGHT + Fore.RED + "%s" % str(e))

		print()

		len_proc: int = len(processes_ram) + len(processes_ram2)

		if all((len_proc, is_debug == False)):
			MySt = MyString() # MyString("Запускаю:", "[2 из 7]")

			try:
				print(Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="Запускаю:", endtxt="[2 из 7]", count=len_proc,	kw="задач"))
				# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
			except:
				print(Style.BRIGHT + Fore.YELLOW + "Обновляю или удаляю %d файлы(а,ов) [2 из 7]" % len_proc)  # old(is_except)
			else:
				write_log("debug run[task2]", MySt.last2str(maintxt="Запускаю:", endtxt="[2 из 7]", count=len_proc, kw="задач"))

			del MySt

		write_log("debug end[project_update]", "%s" % str(datetime.now()))

	def some_formula(filename, is_log: bool = True):
		return

	# @log_error
	async def filter_from_list(lst: list = []) -> list:  # files -> current_files + base

		temp: list = []
		some_files: list = []

		try:
			assert lst, "Пустой список @filter_from_list/lst" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Пустой список @filter_from_list/lst")
			raise err
			return temp

		# if not lst:
			# return temp

		# load_meta_jobs(filter) #4
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)
		finally:
			some_files = [*somebase_dict] if somebase_dict else []

		# some_files = some_files[0:1000] if len(some_files) >= 1000 else some_files # no_limit

		short_list: list = []
		keyword_list: list = []

		# need_shorts_to_list(upgrade)
		try:
			# short_list = [crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))] # equal
			# short_list: list = [crop_filename_regex.sub("", sm.split("\\")[-1]).split("_")[0].strip() if sm.split("\\")[-1].count("_") > 0 else crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))]  # match_or_equal # only_first
			for sm in filter(lambda x: os.path.exists(x), tuple(some_files)):
				try:
					keyword_list = sm.split("\\").split("_")[0:sm.count("_")] # is_tv_series_without_seasepis(is_big_cinema_without_year) # is_skip_last_group_tempalte
				except:
					continue
				else:
					if keyword_list:
						short_list += keyword_list[0]
		except:
			short_list: list = []  # old(no_gen) # crop_filename_regex.sub("", f.split("\\")[-1]).strip() for f in filter(lambda x: os.path.exists(x), tuple(some_files))
		else:
			if short_list:
				tmp: list = []

				tmp = list(set([sl.strip() for sl in short_list if len(sl) >= 2])) # need_only_upper_or_bum
				short_list = sorted(tmp, reverse=False)

		tmp = list(set([sl.strip() for sl in filter(lambda x: any((x[0] == x[0].upper(), x[0].isnumeric())), tuple(short_list))]))

		short_list = sorted(tmp, reverse=False)
		# short_list = sorted(tmp, key=len, reverse=False)

		try:
			filter_list: list = [l.strip() for l in filter(lambda x: os.path.exists(x), tuple(lst)) for sl in filter(lambda y: y, tuple(short_list)) if all((l, sl, l.split("\\")[-1].startswith(sl)))]  # exists/short_template/start_with_template
		except:
			filter_list: list = []

		temp = list(set(filter_list))

		filter_list = sorted(temp, reverse=False)
		# filter_list = sorted(temp, key=len, reverse=False)

		return filter_list

	# update_bigcinema_by_year # pass_x_of_4
	async def update_bigcinema():

		write_log("debug start[update_bigcinema]", "%s" % str(datetime.now()))

		# return

		# pass_1_of_2 # update_exists_files # ok

		# move_big_films(lfiles) # need_code # move_project_to_folder1 # update
		# '''

		MM = MyMeta() #3

		video_regex = re.compile(
			r"(.*)(\([\d+]{4}\))(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^crdownload|^.crswap))$",
			re.M)
		video_big_regex = re.compile(r"\([\d+]{4}\)", re.M)  # ; filename = r"c:\\downloads\\film(2000).mp4"

		big_cinema: list = []

		file_cinema: str = "d:\\multimedia\\video\\big_films\\"

		try:
			year_range = list(set(["".join([file_cinema, yr]).strip() for yr in os.listdir(file_cinema) if os.path.exists("".join([file_cinema, yr])) and not os.path.isfile("".join([file_cinema, yr]))]))
		except:
			year_range = []
		else:
			if year_range:
				for yr in sorted(year_range, reverse=False):
					try:
						if len(os.listdir(yr)) == 0: # delete_folder_if_no_files

							try:
								os.rmdir(yr) # type1 # dos_delete_folder_by_python
							except:
								os.system(r"cmd /c rmdir %s" % yr) # type2(error) # dos_delete_folder
							finally:
								if not os.path.exists(yr):
									print(Style.BRIGHT + Fore.GREEN + "В папке %s нет больших файлов и была удалена" % yr)
									write_log("debug delete[folder][big_cinema]", "В папке %s нет больших файлов и была удалена" % yr)

					except BaseException as e:
						print(Style.BRIGHT + Fore.RED + "Ошибка удаления папки %s [%s]" % (yr, str(e)))
						write_log("debug delete[folder][big_cinema][error]", "Ошибка удаления папки %s [%s]" % (yr, str(e)), is_error=True)

						continue

		# filename = "Some_film(2000).mp4"

		if os.path.exists(file_cinema):  # if_have_nlocal_folder
			with ThreadPoolExecutor(max_workers=ccount) as e:
				nlf = e.submit(sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex)  # nlocal # filmy

			try:
				big_cinema = nlf.result()
			except:
				big_cinema = []

		elif not os.path.exists(file_cinema):  # if_no_nlocal_folder
			big_cinema = []

		print(Style.BRIGHT + Fore.CYAN + "Проверка готовых больших и проектов файлов. Ждите...")

		# create_folders_by_years(if_not_exists)

		project_bigcinema: list = []

		try:
			project_bigcinema = list(set([video_big_regex.findall(pff)[0].replace("(", "").replace(")", "").strip() for pff in os.listdir(path_for_folder1) if video_big_regex.findall(pff)[0].replace("(", "").replace(")", "").isnumeric()]))
		except:
			project_bigcinema = []
		finally:
			pb_status = len(project_bigcinema) if len(project_bigcinema) > 0 else 0
			write_log("debug project_bigcinema[count]", "%d" % pb_status)

		for pb in project_bigcinema:

			if not project_bigcinema:
				break

			if not pb:
				continue

			try:
				clear_year = "".join([file_cinema, pb]).strip()
			except:
				clear_year = ""

			try:
				if not os.path.exists(clear_year) and all((clear_year, pb.strip().isnumeric())):
					try:
						os.mkdir(clear_year)  # type1(try)
					except:
						os.system(r"cmd /c mkdir %s" % clear_year) # type2(error)
			except BaseException as e:
				write_log("debug bigcinema[folder][error]", "%s [%s]" % (clear_year, str(e)), is_error=True)
			# continue # skip_if_error
			else:
				bc_status = ""

				try:
					bc_status = f"Папка {clear_year} создана" if os.path.exists(
						clear_year) else f"Папка {clear_year} не создана"
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
				move_dict = {"".join([path_to_done, l1]).strip(): "".join([path_for_folder1, l1]).strip() for l1 in list1 if video_big_regex.findall(l1) and os.path.isfile("".join([path_to_done, l1]).strip())}  # ready/project # is_move_for_pass2
			else:
				move_dict = {}

			rename_count: int = 0

			error_dict: dict = {}

			try:
				with open(error_base, encoding="utf-8") as ebf:
					error_dict = json.load(ebf)
			except:
				with open(error_base, "w", encoding="utf-8") as ebf:
					json.dump(error_dict, ebf, ensure_ascii=False, indent=2, sort_keys=True)

			for k, v in move_dict.items():

				if any((not move_dict, not big_cinema)):  # if_no_move_files # "if_no_big_cinema_files"
					break

				if not os.path.exists(k) or not k:  # not_exists_or_null_filename
					continue

				try:
					fname1 = k.split("\\")[-1].strip()  # project(v) -> ready(k)
				except:
					fname1 = ""

				# new_count: int = 0
				move_count: int = 0
				delete_count: int = 0
				rename_count: int = 0

				def bc_gen(big_cinema=big_cinema):
					for bc in filter(lambda x: x, tuple(big_cinema)):
						yield bc.strip()

				try:
					tmp = list(bc_gen())  # new(yes_gen)
				# tmp = [bc.strip() for bc in filter(lambda x: x, tuple(big_cinema))]
				except:
					tmp = []  # old(no_gen) # bc.strip() for bc in filter(lambda x: x, tuple(big_cinema))

				big_cinema = tmp
				if big_cinema:

					for bc in big_cinema:  # filter(lambda x: x, tuple(big_cinema)):  # os.path.exists(x) -> x # new(yes_gen)

						try:
							fname2 = bc.split("\\")[-1].strip()
						except:
							fname2 = ""

						fext = ""

						if all((fname1 == fname2, fname1, fname2)):
							fext = fname1.split("\\")[-1].split(".")[0].strip() + ".bak"

						# original_error_meta_or_null_size_or_null_length

						is_error = False

						if any((MM.get_meta(bc) == False, os.path.getsize(bc) == 0, MM.get_length(bc) == 0)) and all((fext, k.split("\\")[-1] == bc.split("\\")[-1])) or not os.path.exists(bc):  # meta(error) # null_size(0) # null_length(0) # ready_and_project_equal_shortfilename

							if MM.get_meta(bc) == False:
								error_dict[bc.strip()] = "get_meta[error] [%s]" % str(datetime.now())

							if os.path.getsize(bc) == 0:
								error_dict[bc.strip()] = "get_size[error] [%s]" % str(datetime.now())

							if MM.get_length(bc) == 0:
								error_dict[bc.strip()] = "get_length[error] [%s]" % str(datetime.now())

							bigcinema_folder = "\\".join(bc.split("\\")[:-1]) + "\\"

							mp4_to_bak = "".join([bigcinema_folder, fext])

							# move(bc, mp4_to_bak) # rename_original_to_bak_if_error_meta

							# write_log("debug mp4_to_back", "%s" % mp4_to_bak)
							write_log("debug mp4_to_back!", "%s" % mp4_to_bak)

							rename_count += 1

							print(Style.BRIGHT + Fore.RED + "-(%s)-" % mp4_to_bak, "[%d]" % rename_count,
								  end="\n")  # rename_by_error_length
							write_log("debug bigcinema[rename]", "-(%s)-" % mp4_to_bak,
									  "[%d]" % rename_count)  # delete -> rename

							is_error = True

							if all((fname1 == fname2, fname1, fname2, not is_error)):  # equal_filename_without_errors

								try:
									gl1 = MM.get_length(k)
								except:
									gl1 = 0

								try:
									gl2 = MM.get_length(bc)
								except:
									gl2 = 0

								is_clean = all((gl1 in range(gl2, gl2 - 5, -1), gl1, gl2))  # big_cinema

								if is_clean and os.path.exists(k):

									# load_meta_jobs(filter) #5
									try:
										with open(some_base, encoding="utf-8") as sbf:
											somebase_dict = json.load(sbf)
									except:
										somebase_dict = {}

										with open(some_base, "w", encoding="utf-8") as sbf:
											json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

									first_len: int = len(somebase_dict)

									# clean_project_from_base.append(fullname2)

									somebase_dict = {k: v for k, v in somebase_dict.items() if os.path.exists(k)}  # exists_only # pass_1_of_2
									somebase_dict = {k: v for k, v in somebase_dict.items() if k != bc}  # clear_if_ready(delete)  # big_cinema # pass_2_of_2

									second_len: int = len(somebase_dict)

									if all((second_len, second_len <= first_len)):  # clear_ready(big_cinema)
										with open(some_base, "w", encoding="utf-8") as sbf:
											json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

										print(Style.BRIGHT + Fore.YELLOW + "Подготовка к переносу файла",
											Style.BRIGHT + Fore.WHITE + "%s" % bc)
										write_log("debug bc[move]", "Подготовка к переносу файла %s" % bc)

										try:
											fsize: int = os.path.getsize(k)
											dsize: int = disk_usage(bc[0] + ":\\").free
										except:
											fsize: int = 0
											dsize: int = 0
										else:
											if all((fsize, dsize, int(fsize // (dsize / 100)) <= 100)):
												move(k, bc)  # update_if_ok_length_by_move

												move_count += 1

												print(Style.BRIGHT + Fore.YELLOW +
													"%s [%d]" % ("-=>".join([k, bc]), move_count))  # update_by_length

												write_log("debug bigcinema[move]", "%s [%d]" % ("-=>".join([k, bc]), move_count))

											elif all((fsize >= 0, dsize, int(fsize // (dsize / 100)) > 100)) or not dsize: # fspace(bad) # dspace(bad)
												print(Style.BRIGHT + Fore.YELLOW + "debug bigcinema[fspace] \'%s\'" % full_to_short(bc))
												write_log("debug bigcinema[fspace]", "%s" % bc)
												MyNotify(txt="%s" % full_to_short(bc), icon=icons["error"])
												continue

										# @load_current_jobs
										try:
											with open(filecmd_base, encoding="utf-8") as fbf:
												fcmd = json.load(fbf)
										except: # IOError
											fcmd = {}

											with open(filecmd_base, "w", encoding="utf-8") as fbf:
												json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)

										first_len = len(fcmd)

										if all((fcmd, somebase_dict)):
											fcmd = {k:v for k, v in fcmd.items() if os.path.exists(k) and any((k.strip() in [*somebase_dict], not [*somebase_dict]))}

										second_len = len(fcmd)

										if all((second_len, second_len <= first_len)):
											with open(filecmd_base, "w", encoding="utf-8") as fbf:
												json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)

								elif not is_clean and os.path.exists(k):
									os.remove(k)  # del_ready_with_error_length

									delete_count += 1

									print(Style.BRIGHT + Fore.RED + "-(%s)- [%d]" % (k, rename_count), end="\n")
									write_log("debug bigcinema[delete]", "-(%s)- [%d]" % (k, rename_count))

			if error_dict: # some_errors
				error_dict = {k: v for k, v in error_dict.items() if os.path.exists(k)} # exists_only

			with open(error_base, "w", encoding="utf-8") as ebf:
				json.dump(error_dict, ebf, ensure_ascii=False, indent=2, sort_keys=True) # errors(+exists)


		print(Style.BRIGHT + Fore.YELLOW + "Проверка готовых больших и проектов файлов завершена...")

		print()

		print(Style.BRIGHT + Fore.CYAN + "Проверка новых больших файлов. Ждите...")

		processes_ram: list = []
		processes_ram2: list = []

		# pass_2_of_2 # new_file_for_move_by_year # debug/test

		# move_big_films(lfiles) # need_code # move_folder1_to_bigfilms # src_to_dst
		# """
		try:
			list1 = os.listdir(path_for_folder1)
		except:
			list1 = []
		finally:
			temp = ["".join([path_for_folder1, l1]) for l1 in list1 if os.path.isfile("".join([path_for_folder1, l1]).strip())]

			list1 = sorted(temp, reverse=False)
			# list1 = sorted(temp, key=len, reverse=False)

			if list1:

				new_count: int = 0
				move_count: int = 0
				delete_count: int = 0

				# avg_sum: int = 0
				# avg_len: int = 0
				avg_size: int = 0

				try:
					fsizes = list(set([os.path.getsize(l1) for l1 in list1 if os.path.exists(l1)]))
				except:
					fsizes = []
				finally:
					fsizes.sort(reverse=False)

				try:
					avg_size = await avg_lst(list(set(fsizes)))
				except:
					try:
						avg_size = (lambda s, l: s // l)(sum(fsizes), len(fsizes))
					except:
						avg_size = 0

				with unique_semaphore:
					for l1 in list1:

						if not list1: # no_data
							break

						try:
							fname = l1.split("\\")[-1].strip()
						except:
							fname = ""

						if not list1:  # skip_if_nulllist
							break

						try:
							year_path = "".join([file_cinema, video_big_regex.findall(fname)[0].replace("(", "").replace(")", "")])

							year_path += "\\" + fname
						except:
							year_path = ""
						finally:

							print(Style.BRIGHT + Fore.WHITE + "%s" % "->".join([year_path, fname]))  # new
							write_log("debug yearfolder", "->".join([year_path, fname]))

						if all((l1, year_path)) and os.path.exists("".join([file_cinema,
																		video_big_regex.findall(fname)[0].replace(
																			"(", "").replace(")", "")])):

							try:
								fsize: int = os.path.getsize(l1)
								dsize: int = disk_usage(year_path[0] + ":\\").free
							except:
								fsize: int = 0
								dsize: int = 0
							else:
								if all((fsize, dsize, int(fsize // (dsize / 100)) <= 100)):
									# move(l1, year_path) # processes_ram

									print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
									Style.BRIGHT + Fore.WHITE + "%s" % l1)  # add_to_all(process_move)

									# p = multiprocessing.Process(target=process_move, args=(l1, year_path, False, True, avg_size))

									try:
										await process_move(l1, year_path, False, True, avg_size) # no_asyncio.run # async_if_small #4
									except BaseException as e:
										write_log("debug process_move[error][4]", ";".join([l1, year_path, str(e)]))
									else:
										write_log("debug process_move[ok][4]", ";".join([l1, year_path]))

									if not l1 in processes_ram:
										processes_ram.append(l1)

									'''
									if not p in processes_ram:
										p.start()
										processes_ram.append(p)
									'''

									print(Style.BRIGHT + Fore.GREEN + "%s[2]" % "==>".join([l1, year_path]))  # new
									write_log("debug bigcinema[moved]", "%s[2]" % "==>".join([l1, year_path]))

									new_count += 1

								elif all((fsize >= 0, dsize, int(fsize // (dsize / 100)) > 100)) or not dsize: # fspace(bad) # dspace(bad)
									# os.remove(l1) # processes_ram2

									# p = multiprocessing.Process(target=process_delete, args=(l1,))

									# await process_delete(l1) # async_if_delete # is_debug

									if not l1 in processes_ram2:
										processes_ram2.append(l1)

									'''
									if not p in processes_ram2:
										p.start()
										processes_ram2.append(p)
									'''

									print(Style.BRIGHT + Fore.GREEN + "bigcinema[deleted] \'-(%s[2])-\'" % full_to_short(l1), end="\n")
									write_log("debug bigcinema[deleted]", "-(%s[2])-" % l1)
									MyNotify(txt="-(%s[2])-" % full_to_short(l1), icon=icons["error"])

									delete_count += 1
		# """

		print()

		len_proc: int = len(processes_ram) + len(processes_ram2)

		if len_proc:
			MySt = MyString() # MyString("Запускаю:", "[3 из 7]")

			try:
				print(Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="Запускаю:", endtxt="[3 из 7]", count=len_proc,	kw="задач"))
				# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))#
			except:
				print(Style.BRIGHT + Fore.YELLOW + "Обновляю или удаляю %d файлы(а,ов) [3 из 7]" % len_proc)  # old(is_except)
			else:
				write_log("debug run[task3]", MySt.last2str(maintxt="Запускаю:", endtxt="[3 из 7]", count=len_proc, kw="задач"))

			del MySt

		print(Style.BRIGHT + Fore.YELLOW + "Проверка новых больших файлов завершена...")

		del MM

		write_log("debug end[update_bigcinema]", "%s" % str(datetime.now()))

	# pass_x_of_4
	async def true_project_rename(folder=path_for_folder1, folderlst=vr_folder):  # what_file_need_rename(try_change_project_folder_to_only_tv_series) # path_for_folder1 -> copy_src

		# return

		try:
			assert os.path.exists(folder), "Папка отсутствует @true_project_rename/folder" # is_assert(debug)
		except AssertionError as err:
			logging.warning("Папка отсутствует @true_project_rename/%s" % folder)
			raise err
			return

		# if not os.path.exists(folder):  # not folder
			# return

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
			lfiles = ["".join([folder, lf]).strip() for lf in os.listdir(folder) if all((lf.count(".") >= 1, not year_regex.findall(lf)))]
		except:
			lfiles = []

		# gen_skip_list(lfiles)
		skip_set = set()

		flist = [lf.split("\\")[-1].strip() for lf in filter(lambda x: "aria2" in x, tuple(lfiles)) if os.path.exists(lf)]

		flst = [f.split("\\")[-1].split(".")[:1] for f in flist if f.count(".") > 2]  # skip_filter # ['7f_2'] <class 'list'>
		flst2 = [f.split("\\")[-1].split("_")[:1] for f in flist if all((f.count(".") == 2, f.count("_") == 1))]  # skip_filter # ['Afterparty'] <class 'list'>
		flst3 = [f.split("\\")[-1].split("_")[:2] for f in flist if all((f.count(".") == 2, f.count("_") > 1))]  # skip_filter # ['2', 'Broke'] <class 'list'>

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
			new_list = list(set([lf.strip() for ss in filter(lambda x: x, tuple(list(skip_set))) for lf in filter(lambda y: y, tuple(lfiles)) if lf.split("\\")[-1].startswith(ss)]))  # skip_list_for_lfiles # debug
		except:
			new_list = []
		finally:
			if new_list:
				print(Style.BRIGHT + Fore.YELLOW + "Найдено %d скачанных файлов и файлы будут пропущены [%s]" % (
					len(new_list), str(datetime.now())))

				# lfiles = sorted(new_list, key=len, reverse=False) # is_need(no_debug)
				# new_list = [] # clear_if_need_rename
				if new_list:
					write_log("debug new_list[yes]!", "Найдено %d скачанных файлов и файлы будут пропущены [%s]" % (
						len(new_list), str(datetime.now())))  # debug_length_for_current_jobs(yes)
				# write_log("debug new_list[yes]", "Найдено %d скачанных файлов и файлы будут пропущены [%s]" % (len(new_list), str(datetime.now()))) # length_for_current_jobs(yes)
			elif not new_list:
				print(Style.BRIGHT + Fore.GREEN + "Не найдено скачанных файлов и файлы будут переименованы [%s]" % str(
					datetime.now()))

				# lfiles = sorted(new_list, key=len, reverse=False) # is_need(no_debug)

				write_log("debug new_list[no]!", "Не найдено скачанных файлов и файлы будут переименованы [%s]" % str(
					datetime.now()))  # debug_length_for_current_jobs(no)
			# write_log("debug new_list[no]", "Не найдено скачанных файлов и файлы будут переименованы [%s]" % str(datetime.now())) # length_for_current_jobs(no)

		if all((lfiles, filter_dict, not new_list)):  # rename_if_no_skip_list
			try:
				# filter_dict2 = {v.strip():crop_filename_regex.sub("", lf.split("\\")[-1]).strip() for k, v in filter_dict.items() for lf in filter(lambda x: x, tuple(lfiles)) if all((v.lower().strip() == crop_filename_regex.sub("", lf.split("\\")[-1]).lower().strip(), v.strip() != crop_filename_regex.sub("", lf.split("\\")[-1]).strip()))} # short_and_diff_reg
				# filter_dict2 = {lf.strip():"".join(["\\".join([k, v]), str("".join(crop_filename_regex.findall(lf.split("\\")[-1])[0])).split(".")[0], ".", lf.split("\\")[-1].split(".")[-1]]) for k, v in filter_dict.items() for lf in filter(lambda x: x, tuple(lfiles)) if all((v.lower().strip() == crop_filename_regex.sub("", lf.split("\\")[-1]).lower().strip(), v.strip() != crop_filename_regex.sub("", lf.split("\\")[-1]).strip()))} # two_disk_drive_letters
				filter_dict2 = {lf.strip(): "".join(["\\".join(["\\".join(lf.split("\\")[:-1]), v]), str("".join(crop_filename_regex.findall(lf.split("\\")[-1])[0])).split(".")[0], ".", lf.split("\\")[-1].split(".")[-1]]) for k, v in filter_dict.items() for lf in filter(lambda x: x, tuple(lfiles)) if all((v.lower().strip() == crop_filename_regex.sub("", lf.split("\\")[-1]).lower().strip(), v.strip() != crop_filename_regex.sub("", lf.split("\\")[-1]).strip()))}  # one_disk_drive_letter
			except BaseException as e:
				filter_dict2 = {}

				write_log("debug filter_dict[error]", "[%s] [%s]" % (str(e), str(datetime.now())), is_error=True)

			if filter_dict2:

				print(Style.BRIGHT + Fore.YELLOW + "Есть различия в именах файлов или похожие названия, фильтр запущен...")
				write_log("debug different[filter_dict][yes]", "Есть различия в именах файлов или похожие названия, фильтр запущен [%s]" % str(datetime.now()))

				# filter_by_length # pass_1_of_2

				try:
					for k, v in filter_dict2.items():

						if not filter_dict2: # no_data
							break

						if any((not k, not v)): # no_string's
							continue

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

							for s1 in range(len(fname1)): # index_string1
								for s2 in range(len(fname2)): # index_string2

									if s1 == s2:
										diff_dict[fname1[s1].strip()] = fname2[s2].strip()

							if diff_dict:

								for k2, v2 in diff_dict.items(): # count_equal_symbols

									if k2 == v2:
										count1 += 1

							if all((count1, k, (count1 / len(k)) * 100 > 0, diff_dict)): # if_not_null
								print("Source string: %s" % "".join(list(diff_dict.keys())), "Destonation string: %s" % "".join(list(diff_dict.values())))
								write_log("debug diff_dict[src]", "Source string: %s" % "".join(list(diff_dict.keys())))
								write_log("debug diff_dict[dst]", "Destonation string: %s" % "".join(list(diff_dict.values())))
								# dst -> src # true_autorename_filter
						else:
							continue
				except BaseException as e:
					write_log("debug diff_dict[pass1]", "%s" % str(e), is_error=True)

				# differense_register # pass_2_of_2

				try:
					for k, v in filter_dict2.items():

						if not filter_dict2: # no_data
							break

						if any((not k, not v)): # no_string's
							continue

						# Надо заменить c:\downloads\new\Reginald_the_Vampire_01s07e.mp4 на c:\downloads\new\Reginald_The_Vampire_01s07e.mp4 # write_log
						# Надо заменить c:\...\Reginald_the_Vampire_01s07e.mp4 на c:\...\Reginald_The_Vampire_01s07e.mp4 # print

						if fspace(k, v) and k.split("\\")[:-1] == v.split("\\")[:-1]:  # fspace(ok) # equal_folder
							try:
								print(Style.BRIGHT + Fore.YELLOW + "Надо заменить %s на %s" % (
									full_to_short(k), v))  # is_color
								move(k, v)  # no_async_if_"big"
							except:
								continue
							else:
								write_log("debug filter_dict[move]!",
									  "Будет заменён %s на %s" % (k, v))  # debug/test # only_here
								MyNotify(txt=f"Будет заменён {k} на {v}", icon=icons["moved"])
				except BaseException as e:
					write_log("debug diff_dict[pass2]", "%s" % str(e), is_error=True)

			elif not filter_dict2:
				print(Style.BRIGHT + Fore.GREEN + "Нет различий в именах файлов или известных фильтров, фильтр пропущен...")
				write_log("debug different[filter_dict][no]",
						  "Нет различий в именах файлов или известных фильтров, фильтр пропущен [%s]" % str(
							  datetime.now()))

		write_log("debug end[true_project_rename]", "%s" % str(datetime.now()))

	# print()

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
	filter1: list = [] # recovery_base
	filter2: list = [] # short_filenames
	filter3: list = [] # args
	filter4: list = [] # ready_projects
	filter5: list = [] # ?desc

	need_find_all: bool = False
	need_find_period: bool = False

	# pass_1_of_4(recovery/is_jobs_backup)
	try:
		with open(files_base["backup"], encoding="utf-8") as bjf:  # read_recovery_base(if_new_no_jobs)
			backup_list = bjf.readlines()  # try_read_from_file
	except BaseException as e:
		backup_list: list = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
	finally:

		try:
			filter1: list = [crop_filename_regex.sub("", f.split("\\")[-1]).strip() for f in filter(lambda x: os.path.exists(x), tuple(backup_list)) if f]  # filenames_from_backup # equal(full)
		except:
			filter1 = []

		temp = list(set(filter1))

		filter1 = sorted(temp, reverse=False)  # recovery_files
		# filter1 = sorted(temp, key=len, reverse=False)  # recovery_files

		if filter1:
			print(
				Style.BRIGHT + Fore.CYAN + "Надо обработать файлов: [%d], шаблон: [%s], последнее восстановление: [%s]" % (
					len(filter1), ",".join(filter1), str(datetime.now())))
			write_log("debug recovery[have]",
					  "Надо обработать файлов: [%d], шаблон: [%s], последнее восстановление: [%s]" % (
						  len(filter1), ",".join(filter1), str(datetime.now())))

			try:
				with open(trends_base, encoding="utf-8") as tbf:
					copy_dict = json.load(tbf)
			except: # IOError
				copy_dict = {}

				with open(trends_base, "w", encoding="utf-8") as ftf:
					json.dump(copy_dict, ftf, ensure_ascii=False, indent=2, sort_keys=False)

			filter_temp: list = []

			try:
				filter_temp = sorted(filter1, reverse=False) # sort_by_abc
				# filter_temp = sorted(filter1, key=len, reverse=False)  # sort_by_keys
			except:
				filter_temp = []
			finally:
				filter1 = filter_temp

			if filter1:
				if len(filter1) >= 20:
					print(Style.BRIGHT + Fore.YELLOW + "Проход 1 из 4 [%s]" % ", ".join(filter1[0:20]))
					write_log("debug filter1[list]", ",".join(filter1[0:20]))
				elif len(filter1) < 20:
					print(Style.BRIGHT + Fore.YELLOW + "Проход 1 из 4 [%s]" % ", ".join(filter1[0:len(filter1)]))
					write_log("debug filter1[list]", ",".join(filter1[0:len(filter1)]))

				write_log("debug files[filter1]",
						  "Найдены файлы с шаблоном 1 [%d][%s]" % (len(filter1), str(datetime.now())))
			else:
				write_log("debug files[filter1][null]", "Не найдены файлы с шаблоном 1 [%s]" % str(datetime.now()))

			# copy_dict1 = {f1.strip(): str(datetime.now()) for f1 in filter(lambda x: x, tuple(filter1)) for k, v in copy_dict.items() if all((f1, k, f1.strip() == k.strip()))} #equal
			copy_dict1 = {k.strip(): str(datetime.now()) for f1 in filter(lambda x: x, tuple(filter1)) for k, v in
						  copy_dict.items() if all((f1, k, f1.strip() in k.strip()))}  # match_or_equal

			if copy_dict1:
				copy_dict.update(copy_dict1)

			with open(trends_base, "w", encoding="utf-8") as tbf:
				json.dump(copy_dict, tbf, ensure_ascii=False, indent=2, sort_keys=False)

		# open(files_base["backup"], "w", encoding="utf-8").close() # clean_if_some_data # debug/test

		elif not filter1:
			write_log("debug recovery[none]", "Нет данных по фильтру 1 [%s]" % str(datetime.now()))

		dt = datetime.now()

		if mytime["jobtime"][0] <= dt.hour <= mytime["jobtime"][1]:  # check_and_filter_by_job_time # another_time_no_clean_backup
			if backup_list:  # clear_if_backup_loaded # check_jobs_from_backup
				open(files_base["backup"], "w", encoding="utf-8").close()

	# pass_2_of_4(project/is_new_jobs/is_no_moved)
	try:
		short_files = os.listdir(path_for_folder1)
	except BaseException as e:
		short_files = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))

	try:
		filter2 = [crop_filename_regex.sub("", f).strip() for f in filter(lambda x: x, tuple(short_files))] # equal
		# filter2 = list(set([crop_filename_regex.sub("", f.split("\\")[-1]).split("_")[0].strip() if f.split("\\")[-1].count(
			# "_") > 0 else crop_filename_regex.sub("", f.split("\\")[-1]).strip() for f in
				# filter(lambda x: x, tuple(short_files))]))  # match_or_equal
	except:
		filter2 = []  # old(no_gen) # crop_filename_regex.sub("", f).strip() for f in filter(lambda x: x, tuple(short_files))

	temp = list(set(filter2))

	filter2 = sorted(temp, reverse=False)  # project_files
	# filter2 = sorted(temp, key=len, reverse=False)  # project_files

	if filter2:
		print(Style.BRIGHT + Fore.GREEN + "Файлы проекта готовы к обработке")
		write_log("debug files[local]", "Файлы проекта готовы к обработке")

		print(Style.BRIGHT + Fore.WHITE + "%s" % ",".join(filter2))

		try:
			with open(trends_base, encoding="utf-8") as tbf:
				copy_dict = json.load(tbf)

		except: # IOError
			copy_dict = {}

			with open(trends_base, "w", encoding="utf-8") as ftf:
				json.dump(copy_dict, ftf, ensure_ascii=False, indent=2, sort_keys=False)

		filter_temp2: list = []

		try:
			filter_temp2 = sorted(filter2, reverse=False) # sort_by_abc
			# filter_temp2 = sorted(filter2, key=len, reverse=False)  # sort_by_keys
		except:
			filter_temp2 = []
		finally:
			filter2 = filter_temp2

		if filter2:
			if len(filter2) >= 20:
				print(Style.BRIGHT + Fore.YELLOW + "Проход 2 из 4 [%s]" % ", ".join(filter2[0:20]))
				write_log("debug filter2[list]", ",".join(filter2[0:20]))
			elif len(filter2) < 20:
				print(Style.BRIGHT + Fore.YELLOW + "Проход 2 из 4 [%s]" % ", ".join(filter2[0:len(filter2)]))
				write_log("debug filter2[list]", ",".join(filter2[0:len(filter2)]))

			write_log("debug files[filter2]",
					  "Найдены файлы с шаблоном 2 [%d][%s]" % (len(filter2), str(datetime.now())))
		else:
			write_log("debug files[filter2][null]", "Не найдены файлы с шаблоном 2 [%s]" % str(datetime.now()))

		# copy_dict2 = {f2.strip():str(datetime.now()) for f2 in filter(lambda x: x, tuple(filter2)) for k, v in copy_dict.items() if all((f2, k, f2.strip() == k.strip()))} #equal
		copy_dict2 = {k.strip(): str(datetime.now()) for f2 in filter(lambda x: x, tuple(filter2)) for k, v in
					  copy_dict.items() if all((f2, k, f2.strip() in k.strip()))}  # match_or_equal

		if copy_dict2:
			copy_dict.update(copy_dict2)

		with open(trends_base, "w", encoding="utf-8") as tbf:
			json.dump(copy_dict, tbf, ensure_ascii=False, indent=2, sort_keys=False)

	elif not filter2:
		write_log("debug project[none]", "Нет данных по фильтру 2 [%s]" % str(datetime.now()))

	# pass_3_of_4(args)
	try:
		my_arg_filter = asyncio.run(my_args())
	except BaseException as e:
		my_arg_filter = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))

	try:
		filter3 = sorted(list(set(my_arg_filter)), reverse=False)  # template_from_cmd_args
		# filter3 = sorted(list(set(my_arg_filter)), key=len, reverse=False)  # template_from_cmd_args
	except:
		filter3 = []
	else:
		# shorts_in_list(upgrade) # maf.split("_")[0:maf.count("_")] for maf in filter(lambda x: x, tuple(my_arg_filter))
		try:
			filter_new3 = list(set([crop_filename_regex.sub("", maf).split("_")[0].strip() if maf.count(
				"_") > 0 else crop_filename_regex.sub("", maf).strip() for maf in
									filter(lambda x: x, tuple(my_arg_filter))]))  # match_or_equal
		except:
			filter_new3 = []
		else:
			filter3 = filter_new3

	if filter3:
		filter_temp3: list = []

		try:
			filter_temp3 = sorted(filter3, reverse=False) # sort_by_abc
			# filter_temp3 = sorted(filter3, key=len, reverse=False)
		except:
			filter_temp3 = []

		try:
			filter3 = filter_temp3 if filter_temp3 else []
		except:
			filter3 = sorted(filter_temp3, reverse=False)
			# filter3 = sorted(filter_temp3, key=len, reverse=False)

		if filter3:
			if len(filter3) >= 20:
				print(Style.BRIGHT + Fore.YELLOW + "Проход 3 из 4 [%s]" % ", ".join(filter3[0:20]))
				write_log("debug filter3[list]", ",".join(filter3[0:20]))
			elif len(filter3) < 20:
				print(Style.BRIGHT + Fore.YELLOW + "Проход 3 из 4 [%s]" % ", ".join(filter3[0:len(filter3)]))
				write_log("debug filter3[list]", ",".join(filter3[0:len(filter3)]))

			write_log("debug files[filter3]",
					  "Найдены файлы с шаблоном 3 [%d][%s]" % (len(filter3), str(datetime.now())))
		else:
			write_log("debug files[filter3][null]", "Не найдены файлы с шаблоном 3 [%s]" % str(datetime.now()))

	# my_arg_filter = [] # clean_if_some_data # debug/test

	elif not filter3:
		write_log("debug args[none]", "Нет данных по фильтру 3 [%s]" % str(datetime.now()))

	# pass_4_of_4(is_ready_files)

	proj_files: list = []

	try:
		proj_list = os.listdir(path_to_done)
	except:
		proj_list = []

	try:
		if proj_list:
			proj_files = ["".join([path_to_done, pl]) for pl in proj_list if os.path.exists("".join([path_to_done, pl])) and video_ext_regex.findall(pl) and all((pl.count(".") == 1, not pl.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"]))]  # only_normal(files_by_tempate)
	except BaseException as e:
		proj_files = []

		print(Style.BRIGHT + Fore.RED + "%s" % str(e))
		write_log("debug proj_files[filter4][error]", "%s" % str(e), is_error=True)

	if proj_files:
		# shorts_in_list(upgrade)
		# tmp = list(set([crop_filename_regex.sub("", pf.split("\\")[-1]).strip() for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))])) # equal
		tmp = list(set([crop_filename_regex.sub("", pf.split("\\")[-1]).split("_")[0].strip() if
						  pf.split("\\")[-1].count("_") > 0 else crop_filename_regex.sub("", pf.split("\\")[-1]).strip() for pf in filter(lambda x: os.path.exists(x), tuple(proj_files))]))  # match_or_equal

		filter4 = sorted(tmp, reverse=False)
		# filter4 = sorted(tmp, key=len, reverse=False)

	if filter4:
		filter_temp4: list = []

		try:
			filter_temp4 = sorted(filter4, reverse=False) # sort_by_abc
			# filter_temp4 = sorted(filter4, key=len, reverse=False)
		except:
			filter_temp4 = []

		try:
			filter4 = filter_temp4 if filter_temp4 else []
		except:
			filter4 = sorted(filter_temp4, reverse=False)
			# filter4 = sorted(filter_temp4, key=len, reverse=False)

		if filter3:
			if len(filter4) >= 20:
				print(Style.BRIGHT + Fore.YELLOW + "Проход 4 из 4 [%s]" % ", ".join(filter4[0:20]))
				write_log("debug filter4[list]", ",".join(filter4[0:20]))
			elif len(filter4) < 20:
				print(Style.BRIGHT + Fore.YELLOW + "Проход 4 из 4 [%s]" % ", ".join(filter4[0:len(filter4)]))
				write_log("debug filter4[list]", ",".join(filter4[0:len(filter4)]))

			write_log("debug files[filter4]",
					  "Найдены файлы с шаблоном 4 [%d][%s]" % (len(filter4), str(datetime.now())))
		else:
			write_log("debug files[filter4][null]", "Не найдены файлы с шаблоном 4 [%s]" % str(datetime.now()))

	# filter5 # desc

	if any((filter1, filter2, filter3, filter4)):

		print(Style.BRIGHT + Fore.YELLOW + "Выбран какой-то из шаблонов для обработки файлов")
		write_log("debug filter[1234]", "Выбран какой-то из шаблонов для обработки файлов")

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
			# filter_list += filter4  # ? # is_sort_by_key(5)

		# is_debug
		# '''
		true_sym = re.compile(r"([^A-ZА-Я\d\-\_])", re.I) # 2_Broke_Girls # 9-1-1_Lone_Star
		new_filter_set = set()
		new_filter: list = []

		try:
			for fl in filter_list:
				st = fl
				for ss in true_sym.findall(fl):
					if all((st, ss, ss in st)): # skip_syms_in_filter_list
						st = st.replace(" ","_").replace(ss, "").strip() # replace_whitespac(other_clean)
						if all((st, not st in new_filter)): # one_record
							new_filter.append(st) # if_no_logic_save_with_dublicate
		except BaseException as e:
			new_filter = []
			print(Style.BRIGHT + Fore.RED + "%s" % str(e)) # upgrade(filter_list)
			write_log("debug new_filter[error]", "[%s] [%s]" % (str(e), str(datetime.now())))
		else:
			if all((new_filter, filter_list)): # add_renamed_filter_data
				filter_list += list(set(new_filter))
			elif all((new_filter, not filter_list)): # use_renames_filter_data
				filter_list = new_filter

			print("%s" % ";".join(list(set(filter_list)))) # upgrade(filter_list)
			write_log("debug new_filter", "%s [%s]" % (";".join(list(set(filter_list))), str(datetime.now()))) # logging_for_debug
		# '''

		if filter_list:
			temp_list = sorted(filter_list, reverse=False) # abc # type1
			# temp_list = sorted(filter_list, key=len, reverse=False)  # sort_by_key # type2
			# temp_list = filter_list # no_sort # type3

			filter_list = list(set(temp_list))  # unique_list

		# default_short_names_without_slice
		tmp = [fl.strip() for fl in filter_list if all((len(fl) >= 2, fl != "''"))]  # skip_null_filter
		filter_list = tmp if tmp else []

		# slice_by_short_names # @filter_list # combine_jobs_filter_by_short_names
		# '''
		# tmp = ["Hello", "World", "9-1-1", "test", "Test_world"] # ["Hello", "World", "9-1-1", "Test"]

		# shorts_in_list(upgrade)
		temp = list(set([t.strip().split("_")[0] if len(t.split("_")) > 0 else t.strip() for t in tmp])) # use_first_word_or_one_word
		temp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(temp)) if any((t.title().startswith(t[0]), t[0].isnumeric()))])) # compare_first_symb_by_capitalize

		if temp2:
			filter_list = sorted(temp2, reverse=False) # list_by_abc
			# filter_list = sorted(temp2, key=len, reverse=False) # list_by_key

		# '''
		fl_count = str(len(filter_list)) if filter_list else "All"

		if filter_list:
			if len(filter_list) >= 20:  # first_20_short_templates
				print(fl_count, filter_list[0:20], end="\n")  # length / list(20)
			elif len(filter_list) < 20:
				print(fl_count, filter_list, end="\n")  # length / list(full)

			write_log("debug filter_list", ";".join(filter_list))  # current(1) # full
		else:
			write_log("debug filter_list[null][combine]", "Нет фильтра для поиска [%s]" % str(datetime.now()))

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))$", re.M)

		# load_meta_jobs(filter) #6
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)
		finally:
			some_files = [*somebase_dict] if somebase_dict else []

		# some_files = some_files[0:1000] if len(some_files) >= 1000 else some_files # no_limit

		if filter_list:  # some_template
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
					filter_list), re.M)  # M(atch)/I(gnore)_case # by_filter
			need_find_all = True
		elif not filter_list:  # no_template
			# if not some_files:
				# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M) # M(atch)/I(gnore)_case # season(year)
			if some_files: # elif -> if
				filt = sorted(list(set([crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))])), key=len, reverse=False)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
						filt), re.M)  # M(atch)/I(gnore)_case # by_filter_base

			need_find_period = True

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine
				nlf = e.submit(sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex)  # nlocal # serialy
				nlf2 = e.submit(sub_folder, "d:\\multimedia\\video\\serials_europe\\",
								video_regex)  # nlocal # serialy_rus
				nlf3 = e.submit(sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex)  # nlocal # filmy
			# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
			# nlf4 = e.submit(sub_folder, "d:\\multimedia\\video\\", temp_regex) # temporary_files

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine

			lfiles = lf.result()

		try:
			# short_files = list(short_files_gen()) # new(yes_gen)
			short_files: list = list(set([crop_filename_regex.sub("", lf.split("\\")[-1]).strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if all((lf, lf.count(".") == 1, video_regex.findall(lf.split("\\")[-1])))]))
		except:
			short_files: list = []  # old(no_gen) # crop_filename_regex.sub("",lf.split("\\")[-1]).strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if all((lf, lf.count(".") == 1, video_regex.findall(lf.split("\\")[-1])))
		else:
			if short_files:

				tmp = list(set([sf.strip() for sf in filter(lambda x: x, tuple(short_files))]))
				short_files = sorted(tmp, reverse=False)

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
					for sf in short_files:
						if all((not sf in sfl, sf)):
							sfl.append(sf.strip())

				def short_files_gen(sfl=sfl):
					for s in filter(lambda x: x, tuple(sfl)):
						yield s.strip()


				if sfl:
					try:
						short_files = list(short_files_gen()) # new(yes_gen)
					# short_files = [s.strip() for s in filter(lambda x: x, tuple(sfl))]
					except:
						short_files = []  # old(no_gen) # s.strip() for s in filter(lambda x: x, tuple(sfl))

				temp = list(set(short_files))

				try:
					short_files: list = sorted(temp, key=len, reverse=False)  # True(cba) # False(abc)
				except:
					short_files: list = []

				if short_files:  # try_update_before_save # debug/test
					try:
						# tmp = list(temp_gen()) # new(yes_gen)
						tmp: list = [sf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) for sf in
							   tuple(short_files) if all((lf, sf, lf.split("\\")[-1].startswith(sf)))]
					except:
						tmp: list = []  # old(no_gen) # sf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) for sf in tuple(short_files) if all((lf, sf, lf.split("\\")[-1].startswith(sf)))

					tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))

					short_files = sorted(tmp2, reverse=False) if tmp2 else []  # if_some_file_add_else_null_list_by_set(sort_by_length)
					# short_files = sorted(tmp2, key=len, reverse=False) if tmp2 else []  # if_some_file_add_else_null_list_by_set(sort_by_length)

				if short_files:  # save_if_some_list
					with open(short_folders, "w", encoding="utf-8") as sff:
						sff.writelines("%s\n" % sf.strip() for sf in filter(lambda x: x, tuple(short_files)))  # current_folders(short)

					try:
						copy(short_folders, copy_folders)  # copy_list_to_list
					except:
						open(files_base["current"], "w", encoding="utf-8").close()  # if_error_null_list
					else:
						write_log("debug shortfiles[filter]", "|".join(short_files))

				elif not short_files:  # save_if_some_list
					write_log("debug shortfiles[filter]", "No_short_files at [%s]" % str(datetime.now()))

		filter_list = list(set(short_files)) if short_files else []

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			write_log("debug files[filter]", "%s" % "|".join(filter_list))  # current(2)
			need_find_all = True
		elif not filter_list:
			need_find_period = True  # find_all_if_null_filter(period)

		# clear_after_filter
		open(files_base["backup"], "w", encoding="utf-8").close()  # clear_backup(after_filter) # is_need_hide

		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump({}, fbf, ensure_ascii=False, indent=2, sort_keys=False) # clear_list(after_filter) # is_need_hide

		# open(cfilecmd_base, "w", encoding="utf-8").close()  # clear_combinelist(after_filter) # hide_if_manual_run
		# open(path_for_queue + "another.lst", "w", encoding="utf-8").close() # is_csv(after_filter) # hide_if_not_need_another

	elif all((not filter1, not filter2, not filter3, not filter4)):

		# load_meta_jobs(filter) #7
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)
		finally:
			some_files = [*somebase_dict] if somebase_dict else []  # list(somebase_dict.keys())

		# some_files = some_files[0:1000] if len(some_files) >= 1000 else some_files # no_limit

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))", re.M)

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
					filter_list), re.M)  # all_period
			need_find_all = True
		elif not filter_list:  # M(atch)/I(gnore)_case # seas(year)
			# if not some_files:
				# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M) # period_about_x_days
			if some_files: # elif -> if
				filt = sorted(list(set([crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))])), key=len, reverse=False)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
						filt), re.M)  # M(atch)/I(gnore)_case # by_filter_base

			need_find_period = True

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine
				nlf = e.submit(sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex)  # nlocal # serialy
				nlf2 = e.submit(sub_folder, "d:\\multimedia\\video\\serials_europe\\",
								video_regex)  # nlocal # serialy_rus
				nlf3 = e.submit(sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex)  # nlocal # filmy
			# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
			# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\", temp_regex) # temporary_files # sub_folder -> one_folder

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine

			lfiles = lf.result()

		try:
			# short_list = list(short_list_gen()) # new(yes_gen)
			short_list = [crop_filename_regex.sub("", lf.split("\\")[-1]).strip() for lf in
						  filter(lambda x: os.path.exists(x), tuple(lfiles)) if
						  all((lf, lf.count(".") == 1, video_regex.findall(lf.split("\\")[-1])))]
		except:
			short_list = []  # old(no_gen) # crop_filename_regex.sub("", lf.split("\\")[-1]).strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if all((lf, lf.count(".") == 1, video_regex.findall(lf.split("\\")[-1])))
		else:
			if short_list:
				tmp: list = []

				tmp = list(set([sl.strip() for sl in short_list if len(sl) >= 2]))
				short_list = sorted(tmp, reverse=False)

		tmp = list(set([sl.strip() for sl in filter(lambda x: x, tuple(short_list))]))

		short_list = sorted(tmp, reverse=False)
		# short_list = sorted(tmp, key=len, reverse=False)

		short_string = "|".join(short_list) if len(short_list) > 1 else short_list[0]

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
				if all((short_regex.findall(sl), short_string, sl)):  # filter_string_by_current_list(file)
					short_exists.append(sl)

			if short_exists:  # if_some
				short_list = [s.strip() for s in short_exists if s]
			elif not short_exists:  # if_null
				try:
					# short_exists = list(sl_gen()) # new(yes_gen)
					short_exists: list = [sl.strip() for sl in filter(lambda x: x, tuple(short_list)) if
										all((short_regex.findall(sl), short_string))]
				except:
					short_exists: list = []  # old(no_gen) # sl.strip() for sl in filter(lambda x: x, tuple(short_list)) if all((short_regex.findall(sl), short_string))

				tmp = list(set([se.strip() for se in filter(lambda x: x, tuple(short_exists))]))

				short_list = sorted(tmp, reverse=False)
				# short_list = sorted(tmp, key=len, reverse=False)

			open(short_folders, "w", encoding="utf-8").close()  # clear_for_update # debug/test

			# use_only_include_files # debug/test
			temp = list(set(short_list))

			try:
				short_list = sorted(temp, reverse=False)  # True(cba) # False(abc)
				# short_list = sorted(temp, key=len, reverse=False)  # True(cba) # False(abc)
			except:
				short_list = []

			with open(short_folders, "w", encoding="utf-8") as sff:
				sff.writelines("%s\n" % sf.strip() for sf in filter(lambda x: x, tuple(short_list)))  # current_folders(short)

			try:
				copy(short_folders, copy_folders)  # copy_list_to_list
			except:
				open(files_base["current"], "w", encoding="utf-8").close()  # if_error_null_list
			else:
				write_log("debug shortfiles[job]", "|".join(short_list))

		filter_list = list(set(short_list)) if short_list else []

		# default_short_names_without_slice
		tmp = [fl.strip() for fl in filter_list if all((len(fl) >= 2, fl != "''"))]  # skip_null_filter
		filter_list = tmp if tmp else []

		# slice_by_short_names # @filter_list # find_jobs_filter_by_short_names
		# '''
		# tmp = ["Hello", "World", "9-1-1", "test", "Test_world"] # ["Hello", "World", "9-1-1", "Test"]

		# shorts_in_list(upgrade)
		temp = list(set([t.strip().split("_")[0] if len(t.split("_")) > 0 else t.strip() for t in tmp])) # use_first_word_or_one_word
		temp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(temp)) if any((t.title().startswith(t[0]), t[0].isnumeric()))])) # compare_first_symb_by_capitalize

		if temp2:
			filter_list = sorted(temp2, reverse=False) # sort_by_abc
			# filter_list = sorted(temp2, key=len, reverse=False) # sort_by_key

		# '''

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			write_log("debug files[filter][-]", "%s" % "|".join(filter_list))  # current(3)
			need_find_all = True
		elif not filter_list:
			need_find_period = True  # find_all_if_null_filter(period)

		fl_count = str(len(filter_list)) if filter_list else "All"

		try:
			if len(filter_list) >= 20:
				print(fl_count, filter_list[0:20], end="\n")  # count/filter # first_20_only
			elif all((filter_list, len(filter_list) < 20)):
				print(fl_count, filter_list[0:len(filter_list)], end="\n")  # count/filter # first_20_only
			else:
				write_log("debug filter_list[null]", "Нет фильтра для поиска [%s]" % str(datetime.now()))
		except:
			print("no index")


	# --- update_files ---

	try:
		# tmp = list(update_files_gen()) # new(yes_gen)
		tmp: list = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
	except:
		tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))

	tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
	lfiles = sorted(tmp2, reverse=False)

	if need_find_all:  # avg_days_to_full_period

		try:
			dbl = asyncio.run(days_by_list(lfiles)) # full_days
		except:
			dbl = 365  # full_year
		finally:
			write_log("debug dbl[need_find_all]", "%s" % str(dbl))

		is_any = True if dbl != 365 else False

		try:
			temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
						all((lf, mdate_by_days(filename=lf, period=dbl, is_any=is_any) != None))]  # filter_by_period(all_time/avg_time)
		except:
			temp = []
		else:
			if isinstance(dbl, int) and dbl != None:
				# write_log("debug files[avgdays]", "Дней: %d, найдено: %d" % (dbl, len(temp)))
				write_log("debug files[maxdays]", "Найдено: %d" % len(temp))

		if temp:
			tmp = list(set(temp))
			lfiles = sorted(tmp, reverse=False)

	elif need_find_period:
		try:
			dbl = asyncio.run(days_by_list(lfiles)) # full_days
		except:
			dbl = 365 # full_year
		finally:
			write_log("debug dbl[need_find_period]", "%s" % str(dbl))

		# every_30days
		try:
			dbl = (dbl // 30) * 30 if dbl // 30 > 0 else 30  # get_period_more_month_or_month
		except:
			dbl = 30

		is_any = True if dbl != 30 else False

		temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
					all((lf, mdate_by_days(filename=lf, period=dbl, is_any=is_any) != None))]  # fitler_by_all_days

		if temp:
			write_log("debug files[allmonth]", "Найдено: %d" % len(temp))  # allmonth(dbl >= 30)

		if not temp:  # all_days_if_no_files_by_30days
			try:
				dbl = asyncio.run(days_by_list(lfiles))  # full_days
			except:
				dbl = 365  # full_year
			finally:
				write_log("debug dbl", "%d" % dbl)

			is_any = True if dbl != 365 else False

			temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
						all((lf, mdate_by_days(filename=lf, period=dbl, is_any=is_any) != None))]  # fitler_by_all_days

			if temp:
				write_log("debug files[alldays]",
						  "Найдено: %d" % len(temp))  # alldays(dbl > 0, 0 - current, 1 - other_days)

		tmp = list(set(temp))
		lfiles = sorted(tmp, reverse=False)

	if lfiles and any((need_find_period, need_find_all)):  # filter_period(30_days/all_days)
		if need_find_all:
			write_log("debug files[find]", "Найдены за весь период [%s]" % str(datetime.now()))
		elif need_find_period:
			write_log("debug files[find]", "Найдены за месяц [%s]" % str(datetime.now()))

		date1 = datetime.now()

		unique = full_list = set()
		try:
			tmp: list = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
		except:
			tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		lfiles = sorted(tmp2, reverse=False)

		cnt: int = 0

		# find_avg_time_by_pass

		MM = MyMeta() #4

		length = [MM.get_length(lf) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]

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

		try:
			h, m = asyncio.run(load_timing_from_xml(ind=2)) # 2 # h, m = load_timing_from_xml(ind=2)
		except:
			h, m = 0, 0

		date1 = datetime.now()

		with unique_semaphore:
			for lf in filter(lambda x: x, tuple(lfiles)):  # filter(lambda x: os.path.exists(x), tuple(lfiles)):  # new(yes_gen)

				if not lfiles: # no_data
					break

				cnt += 1

				# if not lfiles:  # skip_if_nulllist
					# break

				date2 = datetime.now()

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				if hour:
					write_log("debug hour[count][1]", "%d" % (hour[0] // 60)) # is_index #1
					hour = hour[0] // 60

				# '''
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[1]" # 1
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[1]")
					hour = 2 # limit_hour
					# raise err
				# '''

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # all((mm >= l_avg, l_avg >= 30)): # stop_if_more_30min # mm[0] // 60 >= 1:  # stop_if_more_hour
					write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
					break

				if not os.path.exists(lf):
					continue

				try:
					fname = lf.split("\\")[-1].strip()
				except:
					fname = ""

				if all((not fname in unique, fname)) and os.path.exists(lf):
					unique.add(fname)  # short_file(first)_by_set
					full_list.add(lf)  # full_filename(first)_by_set

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)

		def files_to_short_by_full(lfiles=lfiles):
			for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)):
				if all((lf, crop_filename_regex.sub("", lf.split("\\")[-1]))):
					yield lf.strip()
				else:
					yield ""

		try:
			tmp: list = list(files_to_short_by_full()) # new(yes_gen)
		except:
			tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if all((lf, crop_filename_regex.sub("", lf.split("\\")[-1])))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		lfiles = sorted(tmp2, reverse=False)

	elif not lfiles: # if -> elif

		# load_meta_jobs(filter) #8
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)
		finally:
			some_files = [*somebase_dict] if somebase_dict else []  # list(somebase_dict.keys())

		# some_files = some_files[0:1000] if len(some_files) >= 1000 else some_files # no_limit

		# shorts_in_list(upgrade)
		try:
			# filter_list = [crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))] # equal
			filter_list: list = [
				crop_filename_regex.sub("", sm.split("\\")[-1]).split("_")[0].strip() if sm.split("\\")[-1].count(
					"_") > 0 else crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in
				filter(lambda x: os.path.exists(x), tuple(some_files))]  # match_or_equal
		except:
			filter_list: list = []  # old(no_gen) # crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))

		temp = list(set([f.strip() for f in filter(lambda x: x, tuple(filter_list))]))

		filter_list = sorted(temp, reverse=False)
		# filter_list = sorted(temp, key=len, reverse=False)

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))", re.M)

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
					filter_list), re.M)
		elif not filter_list:  # M(atch)/I(gnore)_case # seas(year)
			# if not some_files:
				# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M)
			if some_files: # elif -> if
				filt = sorted(list(set([crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in
										filter(lambda x: os.path.exists(x), tuple(some_files))])), key=len,
							  reverse=False)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
						filt), re.M)  # M(atch)/I(gnore)_case # by_filter_base

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine
				nlf = e.submit(sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex)  # nlocal # serialy
				nlf2 = e.submit(sub_folder, "d:\\multimedia\\video\\serials_europe\\",
								video_regex)  # nlocal # serialy_rus
				nlf3 = e.submit(sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex)  # nlocal # filmy
			# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
			# nlf4 = e.submit(sub_folder, "d:\\multimedia\\video\\", temp_regex) # temporary_files

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine

			lfiles = lf.result()

		if filter_list:
			tfilter_list = [f.strip() for f in filter_list if len(f) > 1]
			filter_list = tfilter_list if tfilter_list else []

			write_log("debug files[filter][reserved]", "%s" % "|".join(filter_list))  # current(4)

		date1 = datetime.now()

		# no_backup(lfiles)
		unique = full_list = set()
		try:
			tmp: list = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
		except:
			tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		lfiles = sorted(tmp2, reverse=False)

		cnt: int = 0

		MT = MyTime(seconds=2)

		try:
			h, m = asyncio.run(load_timing_from_xml(ind=3)) # 3 # h, m = load_timing_from_xml(ind=3)
		except:
			h, m = 0, 0

		date1 = datetime.now()

		with unique_semaphore:
			for lf in filter(lambda x: x, tuple(lfiles)):  # filter(lambda x: os.path.exists(x), tuple(lfiles)):  # new(yes_gen)

				if not lfiles: # no_data
					break

				cnt += 1

				# if not lfiles:  # skip_if_nulllist
					# break

				date2 = datetime.now()

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					#mm %= 60 # sec

				if hour:
					write_log("debug hour[count][2]", "%d" % (hour[0] // 60)) # is_index #2
					hour = hour[0] // 60

				# '''
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[2]" # 2
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[2]")
					hour = 2 # limit_hour
					# raise err
				# '''

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >=h, mm >= m)) # all((hh > hour, mm >= m))
				if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # mm[0] // 60 >= 1:  # stop_if_more_hour
					write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
					break

				if not os.path.exists(lf):
					continue

					try:
						fname = lf.split("\\")[-1].strip()
					except:
						fname = ""

					if all((not fname in unique, fname)):
						unique.add(fname)  # short_file(first)_by_set
						full_list.add(lf)  # full_filename(first)_by_set

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)

		if filter_list:
			temp = [flst.strip() for fl in filter(lambda y: y, tuple(filter_list)) for flst in
					filter(lambda x: os.path.exists(x), tuple(full_list)) if all((fl, flst, fl in flst))]  # +filter
		elif not filter_list:
			temp = [flst.strip() for flst in filter(lambda x: os.path.exists(x), tuple(full_list)) if
						all((flst, crop_filename_regex.sub("", flst.split("\\")[-1])))]  # default_filter

		lfiles = sorted(list(set(temp)), reverse=False)

	# with open(files_base["backup"], "w", encoding="utf-8") as bjf:
	# bjf.writelines("%s\n" % cmd.strip() for cmd in lfiles) # save_for(short_filenames) # save_jobs

	if not lfiles:  # exit_if_not_found_some_files
		exit()

	# --- (move/update)_files ---

	try:
		temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
	except:
		temp = []

	if temp:
		lfiles = sorted(temp, reverse=False)

	# new_or_update_jobs # pass_2_of_2(if_ok_move_and_update)
	lfiles_total: list = []

	if any((os.listdir(copy_src), os.listdir(copy_src2))):

		try:
			lfiles2 = ["".join([copy_src, lf]).strip() for lf in os.listdir(copy_src) if
							all((lf, lf.count(".") == 1, crop_filename_regex.sub("", lf)))]  # if_short_ok(tv_series)
		except:
			lfiles2 = []
		finally:
			lfiles_total += lfiles2

		try:
			lfiles3 = ["".join([copy_src2, lf]).strip() for lf in os.listdir(copy_src2) if
							all((lf, lf.count(".") == 1, crop_filename_regex.sub("", lf)))]  # if_short_ok(big_films)
		except:
			lfiles3 = []
		finally:
			lfiles_total += lfiles3

		# lt = ["c:\\downloads\\mytemp\\hello.file"]
		# ["\\".join(["\\".join(ltf.split("\\")[:-1]), ltf.split("\\")[-1]]) for ltf in lt] # ['c:\\downloads\\mytemp\\hello.file']

		try:
			lfiles_move = {"\\".join(["\\".join(lt.split("\\")[:-1]), lt.split("\\")[-1]]): "".join(
				[path_for_folder1, lt.split("\\")[-1]]).strip() for lt in
						   filter(lambda x: os.path.exists(x), tuple(lfiles_total)) if lt}
		except:
			lfiles_move = {}
		else:
			if lfiles_move:

				print()

				processes_ram: list = []

				try:
					l = list(set([os.path.getsize(lm) for lm in lfiles_move if
								os.path.exists(lm)]))
				except:
					l = []

				try:
					s = (reduce(lambda x, y: x + y, l))
				except:
					s = 0

				try:
					a = (lambda s, l: s // l)(s, len(l))
				except:
					a = 0

				# move_downloads_to_project
				# """
				for k, v in lfiles_move.items():

					if all((fspace(k, v), os.path.getsize(k))):

						if all((os.path.getsize(k) <= a, a)) or not a:  # less_or_equal_avg_or_null

							write_log("debug move[files][thread]", ";".join([k, v]))

							print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
								  Style.BRIGHT + Fore.WHITE + "%s" % k)  # add_to_all(process_move)

							# p = multiprocessing.Process(target=process_move, args=(k, v, False, True, a))  # avg_value

							try:
								asyncio.run(process_move(k, v, False, True, a)) # no_await # async_if_small #5
							except BaseException as e:
								write_log("debug process_move[error][5]", ";".join([k, v, str(e)]))
							else:
								write_log("debug process_move[ok][5]", ";".join([k, v]))

							if not k in processes_ram:
								processes_ram.append(k)

							'''
							if not p in processes_ram:
								p.start()
								processes_ram.append(p)
							'''

						elif all((os.path.getsize(k) > a, a)):  # more_avg

							move(k, v) # no_async_if_big

							try:
								is_new = (os.path.exists(k) and not os.path.exists(v))
							except:
								is_new = False

							try:
								is_update = (os.path.exists(k) and os.path.exists(v))
							except:
								is_update = False

							if all((is_new, not is_update)):
								print(Style.BRIGHT + Fore.GREEN + "Файл",
									  Style.BRIGHT + Fore.WHITE + "%s" % k,
									  Style.BRIGHT + Fore.YELLOW + "надо записать проект в",
									  Style.BRIGHT + Fore.CYAN + "%s" % v)  # is_another_color
								write_log("debug movefile[new]", "Файл %s надо записать проект в %s" % (k, v))

							elif all((is_update, not is_new)):
								print(Style.BRIGHT + Fore.YELLOW + "Файл",
									  Style.BRIGHT + Fore.WHITE + "%s" % k,
									  Style.BRIGHT + Fore.YELLOW + "надо обновить проект в",
									  Style.BRIGHT + Fore.CYAN + "%s" % v)  # is_another_color
								write_log("debug movefile[update]", "Файл %s надо обновить проект в %s" % (k, v))

							write_log("debug move[files][normal]", ";".join([k, v]))

				# print(full_to_short(k), os.path.exists(k), full_to_short(v), os.path.exists(v), Style.BRIGHT + Fore.WHITE + "%s -> %s" % (k, v), end="\n")
				# write_log("debug lfiles_move", "%s" % ";".join([k, str(os.path.exists(k)), v, str(os.path.exists(v)), "%s -> %s" % (k, v)] ))
				# """

	# debug
	# exit()

	# add_or_update_projects(tv_series/big_cinema)
	try:
		lfiles_total: list = ["".join([path_for_folder1, lf.strip()]).strip() for lf in os.listdir(path_for_folder1) if
							os.path.exists("".join([path_for_folder1, lf.strip()]))]  # old(no_gen)
	except:
		lfiles_total: list = []

	if lfiles_total:

		tmp = list(set([lt.strip() for lt in filter(lambda x: x, tuple(lfiles_total))]))
		lfiles_total = sorted(tmp, reverse=False)

		try:
			tmp: list = [crop_filename_regex.sub("", lf.split("\\")[-1].strip()) for lf in
				   filter(lambda x: os.path.exists(x), tuple(lfiles_total)) if lf]
			tmp2 = list(set(tmp))

			tmp = sorted(tmp2, reverse=False)
			# tmp = sorted(tmp2, key=len, reverse=False)
		except:
			tmp: list = []
		else:
			write_log("debug lfiles_total[projects]", "%s" % ";".join(tmp))

	tmp = list(set(lfiles_total))
	lfiles_total = sorted(tmp, reverse=False)

	# check_connect_if_no_users_in_my_smb(for_update) # is_here_overload # smbclient

	# move_tv_series(rus/eng)
	try:
		ff = asyncio.run(folders_filter(lst=lfiles_total, folder="d:\\multimedia\\video\\serials_conv\\"))  # usa(english)
		ff2 = asyncio.run(folders_filter(lst=lfiles_total, folder="d:\\multimedia\\video\\serials_europe\\", is_Rus=True,
							 is_Ukr=True))  # europe(rus/ukr/...)
	except BaseException as e:
		ff = ff2 = []  # null_if_some_error(no_drive/procedure_error)

		print(Style.BRIGHT + Fore.RED + "Нет файлов для переноса. Ошибка в скрипте [%s]" % str(e))
		write_log("debug move[need][error]", "Нет файлов для переноса. Ошибка в скрипте [%s]" % str(e), is_error=True)
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
			fsizes_list: list = list(set([os.path.getsize(f.split(";")[0]) for f in ff if
								os.path.exists(f.split(";")[0])]))
		except:
			fsizes_list: list = []
		else:
			fsizes_list.sort(reverse=False)

		# hidden # debug
		'''
		try:
			gcd_list = asyncio.run(gcd_from_numbers(fsizes_list)) # equal_mod_filesizes
		except:
			gcd_list = []
		finally:
			if gcd_list:
				print("equal_mod_filesizes (current_move_files)", "found %d files" % len(gcd_list))
				write_log("debug gcd_from_numbers[current_move_files]", "equal_mod_filesizes: found %d files" % len(gcd_list))
			elif not gcd_list:
				print("equal_mod_filesizes (current_move_files)", "not found files")
				write_log("debug gcd_from_numbers[current_move_files][null]", "equal_mod_filesizes: not found files")
		'''

		try:
			avg_size = asyncio.run(avg_lst(list(set(fsizes_list)))) # avg_value
		except:
			try:
				avg_size = sum(fsizes_list) // len(fsizes_list)
			except:
				avg_size = 0

		with unique_semaphore:
			for f in ff:

				if not ff: # no_data
					break

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
						print(Style.BRIGHT + Fore.BLUE + "%s" % "=->".join([full_to_short(dfile1), dfile2])) # move_files_by_lang

				try:
					is_new = (os.path.exists(file1) and not os.path.exists(file2))
				except:
					is_new = False
				try:
					is_update = (os.path.exists(file1) and os.path.exists(file2))
				except:
					is_update = False

				if all((file1[0] < file2[0], file1.split("\\")[-1] == file2.split("\\")[-1], file1, file2)) and any(
						(is_new, is_update)):

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
						if all((fsize, dsize, int(fsize // (dsize / 100)) <= 100)):  # fsize != fsize2 # fspace(ok)

							if all((os.path.getsize(file1) <= avg_size,
									avg_size)):  # if_fspace_less_avg_fsize_then_processed_move

								print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
									Style.BRIGHT + Fore.WHITE + "%s" % file1)  # add_to_all(process_move)

								# p = multiprocessing.Process(target=process_move, args=(file1, file2, False, True, avg_size))  # avg_value

								try:
									asyncio.run(process_move(file1, file2, False, True, avg_size)) # no_await # async_if_small #6
								except BaseException as e:
									write_log("debug process_move[error][6]", ";".join([file1, file2, str(e)]))
								else:
									write_log("debug process_move[ok][6]", ";".join([file1, file2]))

								if not file1 in processes_ram:
									processes_ram.append(file1)

								'''
								if not p in processes_ram:
									p.start()
									processes_ram.append(p)
								'''

							elif all((os.path.getsize(file1) > avg_size,
									avg_size)) or not avg_size:  # if_fspace_more_avg_or_null_then_default_move

								move(file1, file2) # no_async_if_big

								if is_new:
									print(Style.BRIGHT + Fore.GREEN + "Файл",
										Style.BRIGHT + Fore.WHITE + "%s" % file1,
										Style.BRIGHT + Fore.YELLOW + "надо записать в",
										Style.BRIGHT + Fore.CYAN + "%s" % file2)  # is_another_color # dfile2
									write_log("debug movefile[need][mp4]",
											"Файл %s надо записать в %s" % (file1, file2))

								elif is_update:
									print(Style.BRIGHT + Fore.YELLOW + "Файл",
										Style.BRIGHT + Fore.WHITE + "%s" % file1,
										Style.BRIGHT + Fore.YELLOW + "надо обновить в",
										Style.BRIGHT + Fore.CYAN + "%s" % file2)  # is_another_color # dfile2
									write_log("debug movefile[need][mp4]",
											"Файл %s надо обновить в %s" % (file1, file2))

						elif all((fsize >= 0, dsize, int(fsize // (dsize / 100)) > 100)) or not dsize: # fspace(bad) # dspace(bad)

							# p = multiprocessing.Process(target=process_delete, args=(file1,))

							# asyncio.run(process_delete(file1)) # async_if_delete # is_debug

							if not file1 in processes_ram2:
								processes_ram2.append(file1)

							'''
							if not p in processes_ram2:
								p.start()
								processes_ram2.append(p)
							'''

							print(Style.BRIGHT + Fore.RED + "move[need] \'Нет хватает места для переноса файла %s\'" % full_to_short(file1))
							write_log("debug move[need]", "Нет хватает места для переноса файла %s" % file1)
							MyNotify(txt="Нет хватает места для переноса файла %s" % full_to_short(file1), icon=icons["error"])

							continue  # skip_if_fspace(bad)
						elif any((not fsize, not dsize)):
							continue  # skip_if_another_logic # fspace(bad)
						else:
							print(Style.BRIGHT + Fore.YELLOW + "Не могу обработать файлы [%s][%d]Мб и [%s][%d]Мб" % (
								dfile1, fsize // (1024 ** 2), dfile2, fsize2 // (1024 ** 2)))
							write_log("debug move[logic]", "Не могу обработать файлы [%s][%d]Мб и [%s][%d]Мб" % (
								file1, fsize // (1024 ** 2), file2, fsize2 // (1024 ** 2)))

		print()

		len_proc = len(processes_ram) + len(processes_ram2)

		if len_proc: # need_count_and_index
			MySt = MyString() # MyString("Запускаю:", "[4 из 7]")

			try:
				print(Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="Запускаю:", endtxt="[4 из 7]", count=len_proc, kw="задач"))
				# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
			except:
				print(
					Style.BRIGHT + Fore.YELLOW + "Обновляю или удаляю %d файлы(а,ов) [4 из 7]" % len_proc)  # old(is_except)
			else:
				write_log("debug run[task4]",
						  MySt.last2str(maintxt="Запускаю:", endtxt="[4 из 7]", count=len_proc, kw="задач"))

			del MySt

	# --- update_files ---

	try:
		temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
	except:
		temp = []

	if temp:
		lfiles = sorted(temp, reverse=False)

	date1 = datetime.now()

	jcount = len(lfiles)

	short_set = full_list = set()

	slist: list = []
	dub_list: list = []

	try:
		# tmp = list(lf_gen()) # new(yes_gen)
		tmp: list = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
	except:
		tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))

	tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
	lfiles = sorted(tmp2, reverse=False)

	# if_skip_limit
	"""
	try:
		fsizes = list(set([os.path.getsize(lf) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]))
	except:
		fsizes = []
	else:
		fsizes.sort(reverse=False)

	try:
		tmp = list(set([lf.strip() for fs in fsizes for lf in lfiles if os.path.exists(lf) and os.path.getsize(lf) == fs]))
	except:
		tmp = []
	else:
		tmp.sort(reverse=False)

	# lfiles = tmp[0:1000] if len(tmp) > 1000 else tmp

	# if len(tmp) > 1000:  # limit_1000_jobs
		# lfiles = tmp[0:1000]
	"""

	cnt: int = 0

	MT = MyTime(seconds=2)

	try:
		h, m = asyncio.run(load_timing_from_xml(ind=4)) # 4 # h, m = load_timing_from_xml(ind=4)
	except:
		h, m = 0, 0

	with unique_semaphore:
		for lf in filter(lambda x: x, tuple(lfiles)):  # filter(lambda x: os.path.exists(x), tuple(lfiles)):

			if not lfiles: # no_data
				break

			cnt += 1

			# if not lfiles:  # skip_if_nulllist
				# break

			hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

			try:
				_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
			except:
				mm = abs(date1 - date2).seconds
				hh = mm // 3600
				mm //= 60
				# mm %= 60 # sec

			if hour:
				write_log("debug hour[count][3]", "%d" % (hour[0] // 60)) # is_index #3
				hour = hour[0] // 60

			# '''
			try:
				assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[3]" # 3
			except AssertionError: # as err:
				logging.warning("Меньше установленого лимита по времени hour[3]")
				hour = 2 # limit_hour
				# raise err
			# '''

			# time_is_limit_1hour_50min # all((h >= 0, m, hh >=h, mm >= m)) # all((hh > hour, mm >= m))
			if all((hh > hour, hour)): # stop_if_more_30min # mm[0] // 60 >= 1:  # stop_if_more_hour
				write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
				break

			if not os.path.exists(lf):
				continue

			try:
				fname = lf.split("\\")[-1]
			except:
				fname = ""

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
				if dub_list[ind1].split("\\")[-1] == dub_list[ind2].split("\\")[-1] and dub_list[ind1][0] < \
						dub_list[ind2][0]:

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
						if all((fname, fsize, dsize, int(fsize // (dsize / 100)) <= 100)):
							if os.path.exists(dub_list[ind1]) and os.path.exists(dub_list[ind2]) and \
									os.path.getsize(dub_list[ind1]) != os.path.getsize(dub_list[ind2]):
								move(dub_list[ind1], dub_list[ind2])

								print(Style.BRIGHT + Fore.WHITE + "%s -> %s" % (dub_list[ind1], dub_list[ind2]))

								write_log("debug updatedublicate", "%s -> %s" % (dub_list[ind1], dub_list[ind2]))

								if os.path.exists(dub_list[ind1]):
									MyNotify(txt=f"Файл {fname} будет обновлен", icon=icons["complete"])
								elif not os.path.exists(dub_list[ind1]):
									MyNotify(txt=f"Файл {fname} был обновлен", icon=icons["complete"])

								is_dublicate = True

							elif os.path.exists(dub_list[ind1]) and os.path.exists(dub_list[ind2]) and \
									os.path.getsize(dub_list[ind1]) == os.path.getsize(dub_list[ind2]):
								os.remove(dub_list[ind1])

								print(Style.BRIGHT + Fore.WHITE + "%s deleted" % dub_list[ind1])

								write_log("debug deletedublicate", "%s deleted" % dub_list[ind1])

								if not os.path.exists(dub_list[ind1]):
									MyNotify(txt=f"Дубликат {fname} был удален", icon=icons["cleaner"])

						elif all((fname, fsize >= 0, dsize, int(fsize // (dsize / 100)) > 100)) or not dsize: # fspace(bad) # dspace(bad)
							print(Style.BRIGHT + Fore.YELLOW + "debug fspace \'Не хватает места для обновления файла %s\'" % full_to_short(dub_list[ind1]))
							write_log("debug fspace", "Не хватает места для обновления файла %s" % dub_list[ind1])
							MyNotify(txt="Не хватает места для обновления файла %s" % full_to_short(dub_list[ind1]), icon=icons["error"])

		if is_dublicate:
			print(Style.BRIGHT + Fore.YELLOW + "Video dublicate found")
			write_log("debug files", "Video dublicate found")

	# --- update_files ---

	try:
		temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
	except:
		temp = []

	if temp:
		lfiles = sorted(temp, reverse=False)

	# --- Frequency files by filter or all files ---

	fsizes_freq = fnames_freq = []  # sizes/filenames # fnames_freq_copy

	if lfiles:
		try:
			# tmp = list(lf_gen()) # new(yes_gen)
			tmp: list = [os.path.getsize(lf) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
						os.path.getsize(lf) and not os.path.getsize(lf) in fsizes_freq]
		except:
			tmp: list = []  # old(no_gen) # os.path.getsize(lf) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if os.path.getsize(lf) and not os.path.getsize(lf) in fsizes_freq

		tmp2 = list(set([t for t in filter(lambda x: x, tuple(tmp))]))
		fsizes_freq = sorted(tmp2, reverse=False)

		try:
			mf = most_frequent(fsizes_freq)  # fsizes_freq(one) # ff(all) # freq_filesize(list) # freq_videos
		except:
			mf = None

		"""
		try:
			avg_size = asyncio.run(avg_lst(list(set(fsizes_freq))))
		except:
			avg_size = 0
		"""

		if all((mf != None, fsizes_freq)):
			try:
				fext_freq = [l.split(".")[-1].lower().strip() for l in
							 filter(lambda x: os.path.exists(x), tuple(lfiles)) if
							 os.path.getsize(l) == mf and all((mf, l))]
			except:
				fext_freq = []
			try:
				# fnames_freq = list(fnames_freq_gen()) # new(yes_gen)
				fnames_freq: list = list(set([l.strip() for l in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
									os.path.getsize(l) == mf and all((mf, l))]))
			except:
				fnames_freq: list = []  # old(no_gen) # l.strip() for l in filter(lambda x: os.path.exists(x), tuple(lfiles)) if os.path.getsize(l) == mf and all((mf, l))

			tmp = list(set([ff.strip() for ff in filter(lambda x: x, tuple(fnames_freq))]))
			fnames_freq = sorted(tmp, reverse=False)

			if fnames_freq and all((fext_freq, fext_freq.count(fext_freq[-1]) >= 1)):  # min(2)
				print(Style.BRIGHT + Fore.WHITE + "Найдено %d уникальных файлов" % len(fnames_freq))

				if len(fnames_freq) > 1:
					crec = fnames_freq[-1]
					fnames_freq.remove(crec)

				for ff in sorted(fnames_freq, reverse=False): # sorted(fnames_freq, key=len, reverse=False)
					print(Style.BRIGHT + Fore.CYAN + "%s" % ff)
					write_log("debug ff", "%s" % ff)

		print()

		len_proc = len(processes_ram2)

		if len_proc:
			MySt = MyString() # MyString("Запускаю:", "[5 из 7]")

			try:
				print(Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="Запускаю:", endtxt="[5 из 7]", count=len_proc, kw="задач"))
				# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
			except:
				print(Style.BRIGHT + Fore.YELLOW + "Удаляю %d файлы(а,ов) [5 из 7]" % len_proc)  # old(is_except)
			else:
				write_log("debug run[task5]",
						  MySt.last2str(maintxt="Запускаю:", endtxt="[5 из 7]", count=len_proc, kw="задач"))

			del MySt

		# debug
		# exit()

	filecmdbase_copy: dict = {}

	# delete_last_jobs_if_hidden(try/except)
	try:
		with open(filecmd_base, encoding="utf-8") as fbf:
			filecmdbase_dict = json.load(fbf)
	except: # IOError
		filecmdbase_dict = {}

		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump({}, fbf, ensure_ascii=False, indent=2, sort_keys=False)
	else:
		if filecmdbase_dict:  # is_optimize_and_run_by_time
			filecmdbase_copy = filecmdbase_dict

			MM = MyMeta() #5

			fsum: int = 0
			flen: int = 0
			favg: int = 0

			try:
				flength: list = list(set([MM.get_length(fd) for fd in filter(lambda x: os.path.exists(x), tuple([*filecmdbase_dict]))]))
			except:
				flength: list = []
			else:
				try:
					fsum = sum(flength)
					flen = len(flength)
					favg = (lambda fs, fl: fs / fl)(fsum, flen)  # generate_average_time_for_job
				except BaseException as e:
					fsum = flen = favg = 0
					write_log("debug flength[error]", "%s" % str(e), is_error=True)  # error_calc
				else:
					if favg:
						write_log("debug flength[calc]", "Sum: %d, length: %d, avg_time: %d" % (
							fsum, flen, favg))  # logging_average_time_from_job #framecount

						try:
							favg_classify = [1 if favg - fl > 0 else 0 for fl in flength]
						except:
							favg_classify = []
						else:
							if favg_classify:
								write_log("debug favg_classify", "%s" % str(
									{"big": favg_classify.count(1), "small": favg_classify.count(0)}))

			# Продолжить сравнив длину файлов(пропустить или обработать)

			# --- Example ---

			# "c:\\downloads\\new\\Gangs_Of_London_02s02e.mp4": "cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -y -i
			# \"c:\\downloads\\new\\Gangs_Of_London_02s02e.mp4\" -map_metadata -1 -threads 2 -c:v libx264 -vf
			# \"scale=640:360\" -profile:v main -movflags faststart -threads 2 -c:a aac -af \"dynaudnorm\"
			# c:\\downloads\\Gangs_Of_London_02s02e.mp4"

			maxcnt = len(filecmdbase_dict) if filecmdbase_dict else 0

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
			filecmdbase_dict = {k: v for k, v in filecmdbase_dict.items() if
									any(("scale" in v.lower(), "profile" in v.lower(), "level" in v.lower()))}

			year_regex = re.compile(r"[\d+]{4}")
			year_filter: list = []


			def filebase_to_year(filecmdbase_dict=filecmdbase_dict):
				for k, v in filecmdbase_dict.items():
					if year_regex.findall(k):
						yield k.strip()

			# year_filter = [k.strip() for k, v in filecmdbase_dict.items() if year_regex.findall(k)] # any(("scale" in v.lower(), "profile" in v.lower(), "level" in v.lower())) # old(no_gen)
			year_filter = list(filebase_to_year()) if list(filebase_to_year()) else []  # new(yes_gen)

			# debug/test

			full_set = set()

			limit_hour: int = 4 if year_filter else 2 # ?debug

			avg_sum: int = 0
			avg_len: int = 0
			avg_size: int = 0

			try:
				fsizes: list = list(set([os.path.getsize(fd) for fd in [*filecmdbase_dict] if
								os.path.exists(fd)]))
			except:
				fsizes: list = []
			finally:
				fsizes.sort(reverse=False)

			try:
				avg_size = asyncio.run(avg_lst(list(set(fsizes))))
			except:
				avg_size = 0

			MT = MyTime(seconds=2)

			try:
				h, m = asyncio.run(load_timing_from_xml(ind=5)) # 5 # h, m = load_timing_from_xml(ind=5)
			except:
				h, m = 0, 0

			date1 = datetime.now()

			for k, v in filecmdbase_dict.items():

				if any((not filecmdbase_dict, not maxcnt)): # no_data / no_max
					break

				cnt += 1

				if not k in full_set:
					full_set.add(k.strip())  # save_unique_job

				elif k in full_set:
					continue  # skip_unique_job

				date2 = datetime.now()

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					#mm %= 60 # sec

				if hour > 0:
					write_log("debug hour[count][4]", "%d" % (hour[0] // 60)) # is_index #4
					hour = hour[0] // 60

				# '''
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[4]" # 4
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[4]")
					hour = 2 # limit_hour
					# raise err
				# '''

				# # time_is_limit_1hour_or_30min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if all((hh > hour, hour)): # stop_if_more_30min # mm[0] // 60 >= limit_hour:  # stop_if_more_"2"hour
					write_log("debug stop_job[filecmdbase_dict]", "Stop: at %s [%d]" % (k, cnt))
					break

				if not os.path.exists(k):  # any((not k, not v))
					continue

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
					prc = (cnt / maxcnt)
					prc *= 100
				except:
					break  # if_percent_calc_error

				if int(prc) != int(prccnt):
					prccnt = int(prc)

					# change_numeric_data_to_percent # if_every_file_run
					if not prccnt in prc_set and (
							not prc_set or all((prc_set, prccnt > sorted(list(prc_set))[-1]))):  # null_or_more_last
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
					fstatus = fspace(fname2, fname1)  # all((fsize, dsize, int(fsize // (dsize / 100)) <= 100))
				except:
					fstatus = False

				is_not_need_run = all((gl2 in range(gl1, gl1 - 5, -1), gl1, gl2)) if all(
					(gl1, gl2)) else False  # run_job_filter

				if all((is_not_need_run, fname1.split("\\")[-1] == fname2.split("\\")[-1])):  # ready(skip_status_and_move_ready)
					print(Style.BRIGHT + Fore.BLUE + "Файл %s будет пропущен для обработки, т.к. длина файла совпала" % fname1)  # skip_color_is_blue

					write_log("debug backup[skip]",
							  "Файл %s будет пропущен для обработки, т.к. длина файла совпала" % fname1)

					if os.path.exists(fname1) and os.path.exists(fname2):  # all_exists # is_green
						print(Style.BRIGHT + Fore.GREEN + "Обработалось",
							  Style.BRIGHT + Fore.WHITE + "%d из %d" % (cnt, maxcnt),
							  Style.BRIGHT + Fore.GREEN + "данных, текущий файл [%s]" % k)  # some_original_filename(short)

						write_log("debug data[percent]", "Обработалось %d из %d данных, текущий файл [%s]" % (
							cnt, maxcnt, k))  # some_original_filename(full/job)

					filter_skip[k.strip()] = v.strip()  # count_skip_by_dict(almost_ready)

					if all((gl1, gl2, fstatus)):  # fspace(ok) # no_errors
						if os.path.exists(fname1) and os.path.exists(
								fname2):  # move_ready_project_by_length # project -> original
							# move(fname2, fname1) # "move" -> process_move

							print(Style.BRIGHT + Fore.GREEN + "Добавление в очередь файла",
								  Style.BRIGHT + Fore.WHITE + "%s" % fname2)  # add_to_all(process_move)

							# p = multiprocessing.Process(target=process_move, args=(fname2, fname1, False, True, avg_size))  # avg_value

							asyncio.run((fname2, fname1, False, True, avg_size)) # async_if_small

							if not fname2 in processes_ram:
								processes_ram.append(fname2)

							'''
							if not p in processes_ram:
								p.start()
								processes_ram.append(p)
							'''

							filecmdbase_copy = {k2: v2 for k2, v2 in filecmdbase_copy.items() if
												k2 != k}  # clear_for_skip_run(is_ready_ok_by_length)

							write_log("debug move[ended]", "Файл %s успешно завершен для переноса в %s [%s]" % (
								v.split(" ")[-1], fname1, str(fstatus)))

					elif all((gl1, gl2 >= 0)) and any(
							(fstatus == False, is_not_need_run == True)):  # fspace(bad) # no_need_run(ok)
						write_log("debug move[ended][error]",
								  "Файл %s успешно завершен, но нет места или ошибка переноса для %s" % (
									  v.split(" ")[-1], fname1))

					print()  # null_line_after_logging
				elif all((is_not_need_run == False,
						  fname1.split("\\")[-1] == fname2.split("\\")[-1])) or not os.path.exists(
					fname2):  # not_(ready/exists)(run_status)
					# print(Style.BRIGHT + Fore.CYAN + "Файл %s будет запущен для обработки, т.к. длина файла разная или отсутствует на диске" % fname2.split("\\")[-1]) # is_run

					print(Style.BRIGHT + Fore.CYAN + "Возможно длина файла %s разная или отсутствует на диске" %
						  v.split(" ")[-1])  # is_delete # delete_color_is_cyan

					# write_log("debug backup[run]", "Файл %s будет запущен для обработки, т.к. длина файла разная или отсутствует на диске" % fname2) # is_run
					write_log("debug backup[run]",
							  "Возможно длина файла %s разная или отсутствует на диске" % v.split(" ")[
								  -1])  # is_delete

					exist_or_update = (os.path.exists(fname1) and not os.path.exists(fname2) or not os.path.exists(fname1) and os.path.exists(fname2))
					not_exists = (not os.path.exists(fname1) and not os.path.exists(fname2))

					if exist_or_update:  # some_exists # some_not_exists # is_yellow
						print(Style.BRIGHT + Fore.YELLOW + "Обработалось", Style.BRIGHT + Fore.WHITE + "%d" % cnt,
							  Style.BRIGHT + Fore.YELLOW + "данных, текущий файл [%s]" % fname1)  # some_original_filename(short)

						write_log("debug data[percent]", "Обработалось %d данных, текущий файл [%s]" % (
							cnt, fname1))  # some_original_filename(full/job)
					elif not_exists:  # all_not_exists # is_red
						print(Style.BRIGHT + Fore.RED + "Обработалось", Style.BRIGHT + Fore.WHITE + "%d" % cnt,
							  Style.BRIGHT + Fore.RED + "данных, текущий файл [%s]" % fname1)  # some_original_filename(short)

						write_log("debug data[percent]", "Обработалось %d данных, текущий файл [%s]" % (
							cnt, fname1))  # some_original_filename(full/job)

					filter_run[k.strip()] = v.strip()  # count_run_by_dict(need_run)

					if os.path.exists(fname2):  # delete_not_ready_project_by_length # project
						# os.remove(fname2) # remove -> process_delete

						# p = multiprocessing.Process(target=process_delete, args=(fname2,))  # avg_value

						asyncio.run(process_delete(fname2)) # async_if_delete

						if not fname2 in processes_ram2:
							processes_ram2.append(fname2)

						'''
						if not p in processes_ram2:
							p.start()
							processes_ram2.append(p)
						'''

					# run_no_complete_file_from_[fcd.json] # debug/test

			del MT

			del MM

			print()

			len_proc = len(processes_ram) + len(processes_ram2)

			MySt = MyString() # MyString("Запускаю:", "[6 из 7]")

			if len_proc:
				try:
					print(Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="Запускаю:", endtxt="[6 из 7]", count=len_proc, kw="задач"))
					# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
				except:
					print(
						Style.BRIGHT + Fore.YELLOW + "Обновляю или удаляю %d файлы(а,ов) [6 из 7]" % len_proc)  # old(is_except)
				else:
					write_log("debug run[task6]",
							  MySt.last2str(maintxt="Запускаю:", endtxt="[6 из 7]", count=len_proc, kw="задач"))

			# update_data_if_stay_files(some)_or_all_ready(null)
			if all((len(filecmdbase_copy) >= 0, filecmdbase_dict, len(filecmdbase_copy) < len(filecmdbase_dict))):
				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(filecmdbase_copy, fbf, ensure_ascii=False, indent=2, sort_keys=False)

			if all((filter_run, filter_skip)):
				filter_run = {k: v for k, v in filter_run.items() for k2, v2 in filter_skip.items() if
								all((k, k2, k != k2))}  # include_run_delete_skip

			filter_run_count = len(filter_run) if filter_run else 0  # count_or_null
			filter_skip_count = len(filter_skip) if filter_skip else 0  # count_or_null

			# print_counts(run/skip)_and_logging # last2str

			if all((filter_skip_count, filter_run_count >= 0, filter_run_count < filter_skip_count)):  # run_logic
				print(Style.BRIGHT + Fore.YELLOW + MySt.last2str(
					maintxt="Было запущено", count=filter_run_count, kw="файл"))
				write_log("debug filter[run]", "Было запущено %d файлов(а)" % filter_run_count)

			elif all((filter_skip_count, filter_run_count, filter_skip_count == filter_run_count)):  # skip_logic
				print(Style.BRIGHT + Fore.YELLOW + MySt.last2str(
					maintxt="Было пропущено", count=filter_skip_count, kw="файл"))
				write_log("debug filter[skip]", "Было пропущено %d файлов(а)" % filter_skip_count)

			del MySt

			if all((filter_run, filecmdbase_dict, len(filter_skip) == len(filecmdbase_dict))):
				# clear_jobsdata_if_skip_count_equal_jobs_count # logic(1_of_2)
				asyncio.run(project_done())  # after_jobs_finish # update_project(some_ready/all)
				asyncio.run(update_bigcinema())  # update_cinema
				asyncio.run(project_update())  # updates(if_downloaded)
				# true_project_rename(folder=copy_src); true_project_rename() # check_and_rename
				asyncio.run(true_project_rename())  # check_and_rename

				ctme = datetime.now()

				asyncio.run(shutdown_if_time())  # check_time_after_run(finish) # try_skip

				filecmdbase_dict = {}  # clean_jobs_list_after_skip # clear_when_done

				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False)

			elif all((filecmdbase_dict, not filter_run)) or all((filter_run, filecmdbase_dict, len(filter_run) < len(filecmdbase_dict))) and all((cnt, maxcnt, cnt <= maxcnt)):
				# update_if_some_jobs_or_run_less_jobs_count # logic(2_of_2)
				asyncio.run(project_done())  # after_jobs_finish # update_project(some_ready/all)
				asyncio.run(update_bigcinema())  # update_cinema
				asyncio.run(project_update())  # updates(if_downloaded)
				# true_project_rename(folder=copy_src); true_project_rename() # check_and_rename
				asyncio.run(true_project_rename())  # check_and_rename

				ctme = datetime.now()

				asyncio.run(shutdown_if_time())  # check_time_after_run(finish) # try_skip

				filecmdbase_dict = {}  # clean_jobs_list_after_update # clear_when_done

				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False)

	# @paths_base
	try:
		with open(paths_base, encoding="utf-8") as pbf:
			pathbase_dict = json.load(pbf)
	except: # IOError
		pathbase_dict = {}

		with open(paths_base, "w", encoding="utf-8") as pbf:
			json.dump({}, pbf, ensure_ascii=False, indent=2, sort_keys=True)

	else:
		listfiles_dict = {lf.strip(): "\\".join(lf.split("\\")[:-1]).strip() for lf in
						  filter(lambda x: os.path.exists(x), tuple(lfiles)) if
						  lf}  # {fullname:fullfolder} # current_files

		if listfiles_dict:
			pathbase_dict.update(listfiles_dict)  # update_files(dict)

		# {fullname:fullfolder} # exists_files
		pathbase_dict = {k: v for k, v in pathbase_dict.items() if os.path.exists(k)}

		with open(paths_base, "w", encoding="utf-8") as pbf:
			json.dump(pathbase_dict, pbf, ensure_ascii=False, indent=2, sort_keys=True)

	if need_find_all:  # avg_days_to_full_period
		try:
			dbl = asyncio.run(days_by_list(lfiles))  # full_days
		except:
			dbl = 365  # full_year

		is_any = True if dbl != 365 else False

		# filter_by_period(all_time/avg_time)
		try:
			temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
						all((lf, mdate_by_days(filename=lf, period=dbl, is_any=is_any) != None))]
		except:
			temp = []
		else:
			if isinstance(dbl, int) and dbl != None:
				# write_log("debug files[avgdays]", "Дней: %d, найдено: %d" % (dbl, len(temp)))
				write_log("debug files[maxdays]", "Найдено: %d" % len(temp))

		# if not temp:
		# dbl = asyncio.run(days_by_list(lfiles)) # full_days

		# temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if all((lf, mdate_by_days(filename=lf, period=dbl) != None))] # fitler_by_all_days
		# write_log("debug files[maxdays]", "Найдено: %d" % len(temp))

		tmp = list(set(temp))
		lfiles = sorted(tmp, reverse=False)

	elif need_find_period:  # find_by_period
		try:
			dbl = asyncio.run(days_by_list(lfiles))  # full_days
		except:
			dbl = 365  # full_year

		# every_30days
		try:
			dbl = (dbl // 30) * 30 if dbl // 30 > 0 else 30  # get_period_more_month_or_month
		except:
			dbl = 30

		is_any = True if dbl != 30 else False

		temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
					all((lf, mdate_by_days(filename=lf, period=dbl, is_any=is_any) != None))]  # fitler_by_all_days
		if temp:
			write_log("debug files[allmonth]", "Найдено: %d" % len(temp))  # allmonth(dbl >= 30)

		if not temp:  # all_days_if_no_files_by_30days
			try:
				dbl = asyncio.run(days_by_list(lfiles)) # full_days
			except:
				dbl = 365  # full_year

			is_any = True if dbl != 365 else False

			temp = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if
						all((lf, mdate_by_days(filename=lf, period=dbl, is_any=is_any) != None))]  # filter_by_all_days
			write_log("debug files[alldays]", "Найдено: %d" % len(temp))

		tmp = list(set(temp))
		lfiles = sorted(tmp, reverse=False)

	if lfiles and any((need_find_period, need_find_all)):  # filter_period(30_days/all_days)
		if need_find_all:
			write_log("debug files[find]", "Найдены за весь период [%s]" % str(datetime.now()))
		elif need_find_period:
			write_log("debug files[find]", "Найдены за месяц [%s]" % str(datetime.now()))

		date1 = datetime.now()

		unique = full_list = set()
		try:
			# tmp = list(lf_gen()) # new(yes_gen)
			tmp: list = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
		except:
			tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		lfiles = sorted(tmp2, reverse=False)

		cnt: int = 0

		MT = MyTime(seconds=2)

		try:
			h, m = asyncio.run(load_timing_from_xml(ind=6)) # 6 # h, m = load_timing_from_xml(ind=6)
		except:
			h, m = 0, 0

		with unique_semaphore:
			for lf in filter(lambda x: x, tuple(lfiles)):  # filter(lambda x: os.path.exists(x), tuple(lfiles))

				if not lfiles: # no_data
					break

				cnt += 1

				# if not lfiles:  # skip_if_nulllist
					# break

				date2 = datetime.now()

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				if hour:
					write_log("debug hour[count][5]", "%d" % (hour[0] // 60)) # is_index #5
					hour = hour[0] // 60

				# '''
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[5]" # 5
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[5]")
					hour = 2 # limit_hour
					# raise err
				# '''

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if all((hh > hour, hour)): # stop_if_more_30min # mm[0] // 60 >= 1:  # stop_if_more_hour
					write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
					break

				if not os.path.exists(lf):
					continue

				try:
					fname = lf.split("\\")[-1].strip()
				except:
					fname = ""

				if all((not fname in unique, fname)):
					unique.add(fname)  # short_file(first)_by_set
					full_list.add(lf)

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)


		def files_to_short_by_full(lfiles=lfiles):
			for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)):
				if all((lf, crop_filename_regex.sub("", lf.split("\\")[-1]))):
					if lf:
						yield lf.strip()
					else:
						yield ""
				else:
					yield ""

		try:
			tmp: list = list(files_to_short_by_full()) # new(yes_gen)
		except:
			tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if all((lf, crop_filename_regex.sub("", lf.split("\\")[-1])))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		lfiles = sorted(tmp2, reverse=False)

	elif not lfiles: # if -> elif
		# read_jobs_from_base(if_no_files_by_template)

		somebase_dict: dict = {}

		# load_meta_jobs(filter) #9
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)
		finally:
			some_files = [*somebase_dict] if somebase_dict else []  # list(somebase_dict.keys())

		# some_files = some_files[0:1000] if len(some_files) >= 1000 else some_files # no_limit

		def files_to_short(some_files=some_files):
			for sm in filter(lambda x: os.path.exists(x), tuple(some_files)):
				if sm:
					yield crop_filename_regex.sub("", sm.split("\\")[-1]).strip()
				else:
					yield ""

		# shorts_in_list(upgrade)
		try:
			# filter_list = [crop_filename_regex.sub("", sm.split("\\")[-1]) for lf in filter(lambda x: os.path.exists(x), tuple(some_files))] # equal
			filter_list: list = [
				crop_filename_regex.sub("", lf.split("\\")[-1]).split("_")[0].strip() if lf.split("\\")[-1].count(
					"_") > 0 else crop_filename_regex.sub("", lf.split("\\")[-1]).strip() for lf in
				filter(lambda x: os.path.exists(x), tuple(some_files))]  # match_or_equal
		except:
			filter_lis: list = []  # old(no_gen) # crop_filename_regex.sub("", sm.split("\\")[-1]).strip() for sm in filter(lambda x: os.path.exists(x), tuple(some_files))

		temp = list(set([fl for fl in filter(lambda x: x, tuple(filter_list))]))
		filter_list = sorted(temp, reverse=False)

		# temp_regex = re.compile("(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.dmf|.dmfr|.filepart|.aria2|.crdownload|.crswap))", re.M)

		if filter_list:  # M(atch)/I(gnore)_case # by_filter
			video_regex = re.compile(
				r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
					filter_list), re.M)
		elif not filter_list:
			# if not some_files:
				# exit()  # exit_if_no_jobs(debug/test) # video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(^.avi|.mkv|.mov|.flv|.vob|.webm|.wmv|.mp4|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$", re.M)
			if some_files: # elif -> if
				filt = sorted(list(set([crop_filename_regex.sub("", k.split("\\")[-1]).strip() for sm in
										filter(lambda x: os.path.exists(x), tuple(some_files))])), key=len,
							  reverse=False)  # filenames_from_base # equal
				video_regex = re.compile(
					r"(.*)(%s)(.*)(?:(.webm|.mpg|.mp2|.mpeg|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|^.avi|.wmv|.mov|.qt|.flv|.f4v|.swf|^.dmf|^.dmfr|^.filepart|^.aria2|^.txt|^.crdownload|^.crswap))$" % "|".join(
						filt), re.M)  # M(atch)/I(gnore)_case # by_filter_base

		temp: list = []

		try:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine
				nlf = e.submit(sub_folder, "d:\\multimedia\\video\\serials_conv\\", video_regex)  # nlocal # serialy
				nlf2 = e.submit(sub_folder, "d:\\multimedia\\video\\serials_europe\\",
								video_regex)  # nlocal # serialy_rus
				nlf3 = e.submit(sub_folder, "d:\\multimedia\\video\\big_films\\", video_regex)  # nlocal # filmy
				# nlf4 = e.submit(one_folder, "d:\\multimedia\\video\\cartoons_europe\\", video_regex) # nlocal
				# nlf4 = e.submit(sub_folder, "d:\\multimedia\\video\\", temp_regex) # temporary_files

			lfiles = lf.result()
			lfiles += nlf.result()
			lfiles += nlf2.result()
			lfiles += nlf3.result()
			# lfiles += nlf4.result()

			# temp = nlf4.result()

		except:
			with ThreadPoolExecutor(max_workers=ccount) as e:
				lf = e.submit(one_folder, "c:\\downloads\\new\\", video_regex)  # local # combine

			lfiles = lf.result()

		if filter_list:
			tfilter_list = [f.strip() for f in filter_list if len(f) > 1]
			filter_list = tfilter_list if tfilter_list else []

			write_log("debug files[filter][reserved]", "%s" % "|".join(filter_list))  # current(5)

		date1 = datetime.now()

		# no_backup(lfiles)
		unique = full_list = set()
		try:
			# tmp = list(lf_gen()) # new(yes_gen)
			tmp: list = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
		except:
			tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		lfiles = sorted(tmp2, reverse=False)

		# if_skip_limit
		"""
		try:
			fsizes = list(set([os.path.getsize(lf) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]))
		except:
			fsizes = []
		else:
			fsizes.sort(reverse=False)

		try:
			tmp = list(set([lf.strip() for fs in fsizes for lf in lfiles if os.path.exists(lf) and os.path.getsize(lf) == fs]))
		except:
			tmp = []
		else:
			tmp.sort(reverse=False)

		# lfiles = tmp[0:1000] if len(tmp) > 1000 else tmp

		# if len(tmp) > 1000:  # limit_1000_jobs
			# lfiles = tmp[0:1000]
		"""

		cnt: int = 0

		MT = MyTime(seconds=2)

		try:
			h, m = asyncio.run(load_timing_from_xml(ind=7)) # 7 # h, m = load_timing_from_xml(ind=7)
		except:
			h, m = 0

		date1 = datetime.now()

		with unique_semaphore:
			for lf in filter(lambda x: x, tuple(lfiles)):  # filter(lambda x: os.path.exists(x), tuple(lfiles)):

				if not lfiles: # no_data
					break

				try:
					fname = lf.strip("\\")[-1]
				except:
					fname = ""

				if not fname or not os.path.exists(lf):
					continue

				if all((not fname in unique, fname)):
					unique.add(fname)  # short_file(first)_by_set
					full_list.add(lf)  # full_filename(first)_by_set

				cnt += 1

				# if not lfiles:  # skip_if_nulllist
					# break

				date2 = datetime.now()

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				if hour:
					write_log("debug hour[count][6]", "%d" % (hour[0] // 60)) # is_index #6
					hour = hour[0] // 60

				# '''
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[6]" # 6
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[6]")
					hour = 2 # limit_hour
					# raise err
				# '''

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # mm[0] // 60 >= 1:  # stop_if_more_hour
					write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
					break

		del MT

		if full_list:
			temp = list(set(full_list))
			lfiles = sorted(temp, reverse=False)

		if filter_list:
			temp = [flst.strip() for fl in filter(lambda y: y, tuple(filter_list)) for flst in
					filter(lambda x: os.path.exists(x), tuple(full_list)) if
					all((flst, fl, fl in flst))]  # +filter
		elif not filter_list:
			temp = [flst.strip() for flst in filter(lambda x: os.path.exists(x), tuple(full_list)) if
						all((flst, crop_filename_regex.sub("", flst.split("\\")[-1])))]  # default_filter

		lfiles = sorted(list(set(temp)), reverse=False)

		# with open(files_base["backup"], "w", encoding="utf-8") as bjf:
		# bjf.writelines("%s\n" % cmd.strip() for cmd in lfiles) # save_for(short_filenames) # save_jobs

		if not lfiles:  # exit_if_not_found_some_files
			exit()

	# filesize/...

	try:
		lfiles_dict = {lf.strip(): [os.path.getsize(lf)] for lf in
					   filter(lambda x: os.path.exists(x), tuple(lfiles)) if
					   all((lf, os.path.getsize(lf)))}  # filesize
	except:
		lfiles_dict = {}  # use_all_find_files(if_null_dict)
	else:
		lfiles_sizes = [v[0] for k, v in lfiles_dict.items() if v[0]]  # all_filesizes
		if lfiles_sizes:
			temp = list(set(lfiles_sizes))
			lfiles_sizes = sorted(temp, reverse=False)  # True = cba(sort) # False = abc(sort)

			def files_by_sizes(lfiles_sizes=lfiles_sizes, lfiles=lfiles):
				for ls in lfiles_sizes:
					for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)):
						if all((lf, os.path.getsize(lf) == ls, os.path.getsize(lf))):
							yield lf.strip()
						else:
							yield ""

			try:
				tmp: list = list(files_by_sizes()) # new(yes_gen)
			except:
				tmp: list = []  # old(no_gen) # lf.strip() for ls in lfiles_sizes for lf in filter(lambda x: os.path.exists(x), tuple(lfiles)) if all((lf, os.path.getsize(lf) == ls, os.path.getsize(lf)))

			tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
			lfiles = sorted(tmp2, reverse=True)  # True=cba(sort) # False=abc(sort)

	write_log("debug jobsave", "%d" % len(lfiles))  # count_current_jobs(all_find_files)

	another_list: list = []

	MM = MyMeta() #6

	prc: int = 0
	cnt: int = 0
	max_cnt: int = len(lfiles)

	# meta_ram = param_list = []

	prc_set = job_set = set()

	fext_dict: dict = {}

	date1 = datetime.now()
	try:
		# tmp = list(lf_gen()) # new(yes_gen)
		tmp: list = [lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))]
	except:
		tmp: list = []  # old(no_gen) # lf.strip() for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))

	tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
	lfiles = sorted(tmp2, reverse=False)

	hms_sum: int = 0
	hms_len: int = 0
	hms_avg: int = 0

	cnt: int = 0

	MT = MyTime(seconds=2)

	try:
		h, m = asyncio.run(load_timing_from_xml(ind=8)) # 8 # h, m = load_timing_from_xml(ind=8)
	except:
		h, m = 0, 0

	date1 = datetime.now()

	# with unique_semaphore:
	for lf in filter(lambda x: x, tuple(lfiles)):  # filter(lambda x: os.path.exists(x), tuple(lfiles))

		if not lfiles: # no_data
			break

		cnt += 1

		# if not lfiles:  # skip_if_nulllist
			# break

		try:
			fp, fn = split_filename(lf)
		except:
			fn = lf.split("\\")[-1].strip() # fp

		try:
			fname = fn
		except:
			fname = ""

		fext = lf.split(".")[-1].lower().strip()

		fext_dict[fext.strip()] = fext_dict.get(fext.strip(), 0) + 1  # add_count

		date2 = datetime.now()

		hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

		try:
			_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
		except:
			mm = abs(date1 - date2).seconds
			hh = mm // 3600
			mm //= 60
			# mm %= 60 # sec

		if hour:
			write_log("debug hour[count][7]", "%d" % (hour[0] // 60)) # is_index #7
			hour = hour[0] // 60

		# '''
		try:
			assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[7]" # 7
		except AssertionError: # as err:
			logging.warning("Меньше установленого лимита по времени hour[7]")
			hour = 2 # limit_hour
			# raise err
		# '''

		# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
		if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # mm[0] // 60 >= 1:  # stop_if_more_hour
			write_log("debug stop_job[lfiles]", "Stop: at %s [%d]" % (lf, cnt))
			break

		if not os.path.exists(lf):
			continue

		if not lf in job_set:
			job_set.add(lf)
		else:
			continue

		if lf != lf.strip() and len(lf.strip()) > 0:
			lf = lf.strip()

		if all((lf.split(".")[-1].lower() in ["dmf", "dmfr", "filepart", "aria2", "crdownload", "crswap"],
				lf[0].lower() != "c")):
			os.remove(lf)

			continue

		# some_formula(lf) # debug/test (fps/filesize/destonation)

		# run(pass_1_of_2)

		fname = lf.split("\\")[-1].strip() if os.path.exists(lf) else ""  # filename(no_ext)
		fext = lf.split(".")[-1].lower().strip() if os.path.exists(lf) else ""  # extention

		if not os.path.exists(lf) or any((not fname, not fext)):  # skip_if(not_exists/no_short_filename/no_extention)
			continue

		ofilename = newfilename = ""

		try:
			fp, fn = split_filename(lf)
		except:
			fn = lf.split("\\")[-1].strip() # fp

		try:
			dfilename = fn
		except:
			dfilename = ""

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

		print(Style.BRIGHT + Fore.WHITE + "Получаю мета-данные по файлу:",
			  Style.BRIGHT + Fore.YELLOW + "%s" % lf)

		write_log("debug getmeta", "Получаю мета-данные по файлу: %s" % lf)

		try:
			width, height, is_change = MM.get_width_height(filename=lf, is_calc=True)  # pass_3_of_3 # calc("find_scale_and_true_scale")
		except BaseException as e:
			width = height = 0
			is_change = False

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))

			write_log("debug get_width_height[error]", "%s [%s]" % (lf, str(e)), is_error=True)
			continue  # skip_if_no_scale

		# optimal_hd

		# rescale_any_tv(hd <-> sd) # 1:1
		if all((width >= height, width, height)):
			# 16/9 -> 4/3 # is_run(no_script) # is_zip(no_backup) # is_pad(sd_bars/hd_scale) # when_zip(delete_scaled)
			# is_run(is_zip)[ok] # is_run(is_zip/is_pad) # sd # is_debug
			try:
				hd_sd = MM.hd_to_sd(lf, width, height, is_run=False, is_zip=False, is_pad=True)
			except BaseException as e:
				hd_sd = ""
				write_log("debug hdtosd[rescale][error]", "%s [%s]" % (dfilename, str(e)), is_error=True)  # error
			else:
				if hd_sd:
					write_log("debug hdtosd[rescale]", "%s [%s] [%s]" % (hd_sd, dfilename, str(round(width / height, 2))[0:]))

			# 4/3 -> 16/9 # is_run(no_script) # is_zip=False(no_backup) # is_pad(unknown) # when_zip(delete_scaled)
			# is_run(is_zip)[?] # is_run(is_zip/is_pad) # hd # is_debug
			try:
				sd_hd = MM.sd_to_hd(lf, width, height, is_run=True, is_zip=True, is_pad=True)
			except BaseException as e:
				sd_hd = ""
				write_log("debug sdtohd[rescale][error]", "%s [%s]" % (dfilename, str(e)), is_error=True)  # error
			else:
				if sd_hd:
					write_log("debug sdtohd[rescale]", "%s [%s] [%s]" % (sd_hd, dfilename, str(round(width / height, 2))[0:]))

		if all((width >= height, width, height)):
			write_log("debug get_width_height", "%s" % ";".join([lf, str(width), str(height), str(is_change)]))

		elif any((not width, not height)):
			write_log("debug wh[null]", "Нет данных width/height для %s" % lf)

			if os.path.exists(lf) and not os.path.getsize(lf):
				print(Style.BRIGHT + Fore.RED + "Файл %s пустой его надо удалить" % dfilename)
				write_log("debug file[null]", "Файл %s пустой его надо удалить" % lf)

				continue

		try:
			vcodec, acodec = MM.get_codecs(lf)
		except BaseException as e:
			vcodec = acodec = ""

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log("debug get_codecs[error]", "%s [%s]" % (lf, str(e)), is_error=True)
		else:
			if vcodec != "h264":
				vcodec = "h264"  # mp4(video) # no_copy
			if acodec != "aac":
				acodec = "aac"  # aac(audio) # no_copy

		if all((vcodec, acodec)):
			write_log("debug get_codecs", "%s" % ";".join([lf, vcodec, acodec]))
		elif any((not vcodec, not acodec)):
			write_log("debug codec[null]", "Нет данных codecs для %s" % lf)  # save_error_data # json/text

			continue  # skip_if_no_codecs

		try:
			profile, level = MM.get_profile_and_level(lf)
		except BaseException as e:
			profile = level = ""

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log("debug get_profile_and_level[error]", "%s [%s]" % (lf, str(e)), is_error=True)

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
			write_log("debug duration", ";".join([hms(duration), lf]))  # save_only_with_time(json/is_sort)
		elif not duration:
			write_log("debug duration[null]", "Нет данных duration для %s" % lf)  # try_remove_by_logic

			continue  # skip_if_no_duration

		# some_bitrate(self, filename, K: int = 0.25, width: int = 640, height: int = 480, fps: float = 15, ms: int = 1200)
		# (filename, width, height, fps, ms, sb)

		optimial_width: int = 0
		optimal_height: int = 0

		try:
			sb_calc = MM.some_bitrate(filename=lf, width=width, height=height, fps=MM.get_fps(lf), ms=MM.get_length(lf)) # check_assert # is_assert(debug)
		except BaseException as e:
			sb_calc = ()

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log("debug some_bitrate[error]", "%s [%s]" % (lf, str(e)), is_error=True)
		else:
			# debug some_bitrate:c:\downloads\new\Gruz_proshlogo_01s01e.mp4 [('c:\\downloads\\new\\Gruz_proshlogo_01s01e.mp4', 640, 360, 25, 2821, 1406.25)]
			write_log("debug some_bitrate", "%s [%s]" % (lf, str(sb_calc))) # is_vbr_calc # sb_calc[5] = 1406.25 # 1406 -> 1400

			vbr_status: str = ""

			# -b:v 1000K -maxrate 1000K -bufsize 2000K

			output_file = "".join([path_to_done, lf.split("\\")[-1]])
			try:
				if any((width, height, sb_calc, width > sb_calc[1], height > sb_calc[2])): # create_cmd_with_vbr(manual_run)
					cmd_vbr = "cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i \"%s\" -threads 2 -c:v libx264 -b:v %s -maxrate %s -bufsize %s -vf \"scale=\'%d:%d\'\" -threads 2 -c:a aac \"%s\"" % (sb_calc[0], "".join([str(int(sb_calc[5])), "k"]), "".join([str(int(sb_calc[5])), "k"]), "".join([str(int(sb_calc[5])*2), "k"]), sb_calc[1], sb_calc[2], output_file)
					vbr_status = "full"
				elif all((width, height, sb_calc, width == sb_calc[1], height == sb_calc[2])): # skip_vbr
					cmd_vbr = "cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i \"%s\" -threads 2 -c:v libx264 -threads 2 -c:a aac \"%s\"" % (sb_calc[0], output_file)
					vbr_status = "short"
			except:
				cmd_vbr = ""
			finally:
				if cmd_vbr:
					write_log("debug cmd_vbr[info]", "%s [%s] [%s]" % (lf, vbr_status, str(datetime.now())))
					write_log("debug cmd_vbr[cmd]", "%s" % cmd_vbr)
				elif not cmd_vbr:
					write_log("debug cmd_vbr[null]", "%s [%s]" % (lf, str(datetime.now())))

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
				optimal_height = 360 # by_default

			if all((optimal_height, optimal_height != height)): # logging_if_another
				try:
					optimal_width = (width / height) * optimal_height
				except ZeroDivisionError:
					optimal_width = None

				if not isinstance(optimal_width, int) and optimal_width != None:
					optimal_width = int(optimal_width)

				# debug optimal[filename/width/height/date]:c:\downloads\new\Razorvannije_01s03e.mp4, 677.6470588235294x360 [2023-03-16 20:56:08.271600]
				write_log("debug optimal[filename/width/height/date]", "%s, %s [%s]" % (lf, "x".join([str(optimal_width), str(optimal_height)]), str(datetime.today())))

			# debug current[filename/width/height/date]:c:\downloads\new\Gruz_proshlogo_01s01e.mp4, 640x360 [2023-03-16 20:55:31.352128]
			write_log("debug current[filename/width/height/date]", "%s, %s [%s]" % (lf, "x".join([str(width), str(height)]), str(datetime.today())))

		try:
			with open(vbr_base, encoding="utf-8") as vbf:
				vbr_dict = json.load(vbf)
		except: # IOError
			vbr_dict = {}

			with open(vbr_base, "w", encoding="utf-8") as vbf:
				json.dump(vbr_dict, vbf, ensure_ascii=False, indent=2)

		try:
			vbr_dict[lf.strip()] = int(sb_calc[-1])  # save_vbr_for_job
		except:
			vbr_dict[lf.strip()] = 0 # if_error_vbr_null

		# update_list_to_int
		try:
			vbr_update = {k: int(v[0]) if isinstance(v, list) else int(v) for k, v in vbr_dict.items()} # list -> int
		except:
			vbr_update = {}

		if vbr_update:
			vbr_dict.update(vbr_update)

		vbr_dict = {k: v for k, v in vbr_dict.items() if os.path.exists(k)}  # exists

		with open(vbr_base, "w", encoding="utf-8") as vbf:
			json.dump(vbr_dict, vbf, ensure_ascii=False, indent=2)

		try:
			vbr = MM.calc_vbr(filename=lf, width=width, height=height)  # -b:v aaaK
		except BaseException as e:
			vbr = 0

			print(Style.BRIGHT + Fore.RED + "%s [%s]" % (lf, str(e)))
			write_log("debug calc_vbr[error]", "%s [%s]" % (lf, str(e)), is_error=True)
		finally:
			if any((vbr, sb_calc)):
				# write_log("debug calc_vbr", ";".join([full_to_short(lf), str(vbr), str(sb_calc)]))
				write_log("debug calc_vbr", ";".join([lf, str(vbr), str(sb_calc)])) # filename / calc_vbr / calc_vbr2(None)
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
				write_log("debug calc_vbr[change]", "[%s] [vbr:%s] ~> [vbr:%s]" % (lf, str(vbr), str(temp_vbr)))  # old(vbr) -> new(vbr)
				vbr = temp_vbr

			if all((vbr == temp_vbr, vbr, temp_vbr)):
				write_log("debug calc_vbr[not_change]", "[%s] [fps:%s] [vbr:%s]" % (lf, str(fps), str(vbr)))  # not_change_vbr

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

			# elif all((cl, 128 <= abr <= 512)):
			# temp_abr = abr

			if all((abr != temp_abr, abr, temp_abr)):
				write_log("debug lossy_audio[change]",
						  "[abr:%s] ~> [abr:%s]" % (str(abr), str(temp_abr)))  # old(abr) -> new(abr)
				abr = temp_abr

			if all((abr == temp_abr, abr, temp_abr)):
				write_log("debug lossy_audio[not_change]", "[abr:%s]" % str(abr))  # not_change_abr

		if abr:
			# write_log("debug lossy_audio", ";".join([full_to_short(lf), str(abr)]))
			write_log("debug lossy_audio", ";".join([lf, str(abr)]))
		elif not abr:
			write_log("debug lossy_audio[null]", "Нет данных abr для %s" % lf)

			continue  # skip_if_no_abr

		try:
			is_meta = MM.get_meta(lf)
		except:
			is_meta = False
		finally:
			if is_meta:
				print(Style.BRIGHT + Fore.GREEN + "Получены мета-данные по файлу:",
					  Style.BRIGHT + Fore.WHITE + "%s" % lf)
				write_log("debug donemeta", "Получены мета-данные по файлу: %s" % lf)
			elif not is_meta:
				print(Style.BRIGHT + Fore.RED + "Ошибка мета-данных по файлу:",
					  Style.BRIGHT + Fore.WHITE + "%s" % lf)
				write_log("debug donemeta[error]", "Ошибка мета-данных по файлу: %s" % lf)

			# continue

		# Quality of each frame # a = 1.234 # "%s" % str(round(a,2))[0:] # '1.23'
		try:
			fq = MM.get_frame_quality(lf)
		except:
			fq = 0
			print(Style.BRIGHT + Fore.RED + "Размер фрейма: не определен, для файла: ",
				  Style.BRIGHT + Fore.WHITE + "%s" % fname)
			write_log("debug frame[quality][error]", "Размер фрейма файла [%s]: не определен" % fname)
		else:
			if fq:
				print(Style.BRIGHT + Fore.YELLOW + "Размер фрейма: %s, для файла: " % str(round(fq, 2))[0:],
					  Style.BRIGHT + Fore.WHITE + "%s" % fname)
				write_log("debug frame[quality]",
						  "Размер фрейма файла [%s]: %s" % (fname, str(round(fq, 2))[0:]))

		cnt += 1

		try:
			prc = int(cnt // (max_cnt / 100))
		except:
			break
		else:
			if all((abs(prc) <= 100, not prc in prc_set, cnt <= max_cnt)):
				prc_set.add(prc)

				if all((fname, cnt)):  # last_shortname/total_count_data
					print(Style.BRIGHT + Fore.YELLOW + "Обработанно %d процентов данных." % prc,
						  Style.BRIGHT + Fore.WHITE + "[%s/%d]" % (fname, cnt))
					write_log("debug datacount", "Обработанно %d процентов данных. [%s/%d]" % (prc, fname, cnt))

		# --- Command line and base and need change (new/update) ---
		# if all((width, height, vcodec, vbr, acodec, profile, level)):  # hide_logic # is_360p

		print(Style.BRIGHT + Fore.WHITE + "Файл: %s" % fname, Style.BRIGHT + Fore.GREEN + "%s" % ";".join(
			[str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, full_to_short(lf)]))

		# debug metaparam:640;360;h264;1000;aac;384;high;30;d:\multimedia\video\serials_conv\Kvantoviy_skachyok\Kvantoviy_skachyok_01s01e.mp4
		write_log("debug metaparam", "%s" % ";".join([str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, lf]))

		# load_meta_jobs(filter) #10
		try:
			with open(some_base, encoding="utf-8") as sbf:
				somebase_dict = json.load(sbf)
		except:
			somebase_dict = {}

			with open(some_base, "w", encoding="utf-8") as sbf:
				json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)
		finally:
			some_files = [*somebase_dict] if somebase_dict else []  # list(somebase_dict.keys())

		# some_files = some_files[0:1000] if len(some_files) > 1000 else some_files # no_limit

		# scale=640:360:flags=lanczos,pad=640:480:0:60 # scale=1440:1080:flags=lanczos,pad=1920:1080:240:0

		scale_regex = re.compile(r"(scale=[\d+]\:[\d+]\:flags\=lanczos)",
								 re.I)  # hd_to_sd # ,pad=[\d+]\:[\d+]\:0\:[\d+] # skip_pad
		scale_regex2 = re.compile(r"(scale=[\d+]\:[\d+]\:flags\=lanczos)",
								  re.I)  # sd_to_hd # ,pad=[\d+]\:[\d+]\:[\d+]\:0) # skip_pad

		# sd_scale
		try:
			scale1 = scale_regex.sub("", hd_sd) if scale_regex.sub("", hd_sd) else ""  # sd # cmd
		except:
			scale1 = ""

		# hd_scale
		try:
			scale2 = scale_regex2.sub("", sd_hd) if scale_regex2.sub("", sd_hd) else ""  # hd # cmd
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
			if all((is_change, width == 640)) and any((vcodec.lower().strip() != "h264", acodec.lower().strip() != "aac", any((
					profile.lower().strip() != "main", not "main" in profile.lower().strip())), int(level) != 30)):  # logic(1_of_4)

				# --- is_new ---

				try:
					write_log("debug somebase_dict[1]", "%s [%s] [%s]" % (lf.strip(), "+".join(
						[str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, scales]), str(datetime.now())))  # filename / param / datetime
				except BaseException as e:
					write_log("debug somebase_dict[1][error]", "%s [%s] [%s]" % (
						lf.strip(), str(e), str(datetime.now())), is_error=True)  # filename / error / datetime
				else:
					# 640+266+h264+170+aac+384+high+30 # vcodec(!h264) # acodec(!aac) # profile(!main)
					# {filename: [width+height+vcodec+vbr+acodec+abr+profile+level+scales]}
					somebase_dict[lf.strip()] = "+".join([str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, scales])  # new(add)

			elif all((is_change == False, width <= 640)) and all((vcodec.lower().strip() == "h264", acodec.lower().strip() == "aac", any((
					profile.lower().strip() == "main", "main" in profile.lower().strip())), all((int(level) > 0, int(level) <= 30)))):  # logic(2_of_4)

				# --- is_ready ---

				# hide_ready_from_logging
				'''
					try:
						# write_log("debug somebase_dict[2]", "%s [%s] [%s]" % (full_to_short(lf.strip()), "ready", str(datetime.now()))) # filename / is_status / datetime
						write_log("debug somebase_dict[2]", "%s [%s] [%s]" % (lf.strip(), "ready", str(datetime.now()))) # filename / is_status / datetime
					except BaseException as e:
						write_log("debug somebase_dict[2][error]", "%s [%s] [%s]" % (lf.strip(), str(e), str(datetime.now()))) # filename / error / datetime
					else:
						# somebase_dict[lf.strip()] = "!".join([str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, scales])
						# {filename: [width!height!vcodec!vbr!acodec!abr!profile!level!scales]}
				'''

				somebase_dict = {k: v for k, v in somebase_dict.items() if os.path.exists(k)}  # exists_only # pass_1_of_2
				somebase_dict = {k: v for k, v in somebase_dict.items() if
							all((k, lf, k.strip() != lf.strip()))}  # delete_current(is_ready) # is_ready(clean) # pass_2_of_2

				# @load_current_jobs
				try:
					with open(filecmd_base, encoding="utf-8") as fbf:
						fcmd = json.load(fbf)
				except: # IOError
					fcmd = {}

					with open(filecmd_base, "w", encoding="utf-8") as fbf:
						json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)

				first_len = len(fcmd)

				if all((fcmd, somebase_dict)):
					fcmd = {k: v for k, v in fcmd.items() if os.path.exists(k) and any((k.strip() in [*somebase_dict], not [*somebase_dict]))}

				second_len = len(fcmd)

				if all((second_len, second_len <= first_len)):
					with open(filecmd_base, "w", encoding="utf-8") as fbf:
						json.dump(fcmd, fbf, ensure_ascii=False, indent=2, sort_keys=False)

			else:
				# --- (is_not_optimized/is_optimized) ---

				try:
					write_log("debug somebase_dict[3]", "%s [%s] [%s]" % (lf.strip(), ":".join(
						[str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, scales]), str(datetime.now()))) # filename / param / datetime
				except:
					write_log("debug somebase_dict[3][error]", "%s [%s] [%s]" % (
						lf.strip(), str(e), str(datetime.now())))  # filename / error / datetime
				else:
					if any((vcodec.lower().strip() != "h264", acodec.lower().strip() != "aac")) or any((
							profile.lower().strip() != "main", not "main" in profile.lower().strip())): # filter(vcodec/acodec/profile) # logic(3_of_4)

						# 640:360:h264:704:aac:384:high:30 # vcodec(!h264) # acodec(!aac) # profile(!main)
						# {filename: [width:height:vcodec:vbr:acodec:abr:profile:level:scales]}

						somebase_dict[lf.strip()] = ":".join(
							[str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level,
							 scales])  # not_optimized(add)
					elif all((vcodec.lower().strip() == "h264", acodec.lower().strip() == "aac", any((
							profile.lower().strip() == "main", "main" in profile.lower().strip())))):  # filter(vcodec/acodec/profile) # logic(4_of_4)
						somebase_dict = {k: v for k, v in somebase_dict.items() if
										 os.path.exists(k)}  # exists_only # pass_1_of_2
						somebase_dict = {k: v for k, v in somebase_dict.items() if
										 k.strip() != lf.strip()}  # delete_current(is_optimized) # is_optimized(clean) # pass_2_of_2

		except BaseException as e:

			# --- is_error ---

			try:
				write_log("debug somebase_dict[4]", "%s [%s] [%s] [%s]" % (lf.strip(), "?".join(
					[str(width), str(height), vcodec, str(vbr), acodec, str(abr), profile, level, scales]), str(e), str(datetime.now())), is_error=True)  # error_with_param # filename / param / error / datetime
			except:
				write_log("debug somebase_dict[4][error]", "%s [%s] [%s]" % (
					lf.strip(), str(e), str(datetime.now())), is_error=True)  # error_without_param # filename / error / datetime

		with open(some_base, "w", encoding="utf-8") as sbf:
			json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

		# find_logic(debug/test)

		# skip_only_resized # skip_if_profile(-profile:v main) # skip_any_level(-level 30) # is_ffmpeg(param)

		# (is_resized)&(profile:v main)&(level 30) # is_slow(0 - change_all) # (is_resized)(profile:v high)(level 40) # is_fast(1 - only_resize)
		try:
			if all((is_change == False,
					any(("main" in profile.lower().strip(), profile.lower().strip() == "main")),
					int(level) == 30)):  # resized/profile/level # no_params
				continue
		except BaseException as e:
			print(Style.BRIGHT + Fore.RED + "Ошибка оптимизации файла",
				Style.BRIGHT + Fore.WHITE + "%s [%s]" % (lf, str(e)))

			write_log("debug status[resize/profile/level][error]",
					  "Ошибка оптимизации файла %s [%s]" % (lf, str(e)), is_error=True)
		else:
			print(Style.BRIGHT + Fore.CYAN + "Оптимизация файла",
				Style.BRIGHT + Fore.WHITE + "%s" % lf)

			write_log("debug status[resize/profile/level]", "Оптимизация файла %s" % lf)

		# get_data_for_metadict_and_skip_run_if_resized(pass_2_of_2)

		vfile = "libx264"  # "libx264" if vcodec != "h264" else "copy"  # is_change # mp4(video) # no_copy
		afile = "aac"  # "aac" if acodec != "aac" else "copy"  # is_change # aac(audio) # no_copy

		try:
			is_profile = True if any((not "main" in profile.lower().strip(),
									  profile.lower().strip() != "main")) else False  # profile.lower().strip() != "main"  # high -> main(middle) / baseline(low) -> main(middle)
		except:
			continue  # "main" in profile.lower()

		try:
			is_level = True if int(level) > 30 else False
		except:
			continue  # level == None

		try:
			svbr = "".join(
				[str(vbr), "K"]) if vbr else ""  # if len(str(cbr)) <= 3 else "".join([str((cbr)), "M"])
		except:
			svbr = ""

		try:
			svbr2 = "".join(
				[str(vbr * 2), "K"]) if vbr else ""  # if len(str(cbr*2)) <= 3 else "".join([str((cbr*2)), "M"])
		except:
			svbr2 = ""

		try:
			sabr = "".join(
				[str(abr), "K"]) if abr else ""  # if len(str(abr)) <= 3 else "".join([str((abr)), "M"])
		except:
			sabr = ""

		bitrate_data = all((svbr, svbr2, sabr))  # sabr

		project_file = "".join([path_to_done, fname])

		cmd_file = cmd_file2 = ""  # default/with_vbr

		# no_change_high_to_main(is_profile)_for_high # optimal_level(is_level)_for_30 # -profile:v high -level 30 # is_manual_run

		if all((is_change, width, height, vfile, afile,
				bitrate_data)):  # optimize_width # width*height # vcodec(acodec) # is_bitrate
			if all((is_profile, is_level)):
				cmd_file = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -vf \"scale=%s:%s\" -profile:v main -level 30 -movflags faststart -threads 2 -c:a %s -af \"dynaudnorm\" %s " % (
							   lf, vfile, str(width), str(height), afile, project_file)
				cmd_file2 = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -b:v %s -maxrate %s -bufsize %s -vf \"scale=%s:%s\" -profile:v main -level 30 -movflags faststart -threads 2 -c:a %s -b:a %s -af \"dynaudnorm\" %s " % (
								lf, vfile, svbr, svbr, svbr2, str(width), str(height), afile, sabr, project_file)
			elif all((is_profile, not is_level)):
				cmd_file = "cmd /c " + "".join([path_for_queue,	"ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -vf \"scale=%s:%s\" -profile:v main -movflags faststart -threads 2 -c:a %s -af \"dynaudnorm\" %s " % (
							   lf, vfile, str(width), str(height), afile, project_file)
				cmd_file2 = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -b:v %s -maxrate %s -bufsize %s -vf  \"scale=%s:%s\" -profile:v main -movflags faststart -threads 2 -c:a %s -b:a %s -af \"dynaudnorm\" %s " % (
								lf, vfile, svbr, svbr, svbr2, str(width), str(height), afile, sabr, project_file)
			elif all((not is_profile, is_level)):
				cmd_file = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -vf \"scale=%s:%s\" -level 30 -movflags faststart -threads 2 -c:a %s -af \"dynaudnorm\" %s " % (
							   lf, vfile, str(width), str(height), afile, project_file)
				cmd_file2 = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -b:v %s -maxrate %s -bufsize %s -vf \"scale=%s:%s\" -level 30 -movflags faststart -threads 2 -c:a %s -b:a %s -af \"dynaudnorm\" %s " % (
								lf, vfile, svbr, svbr, svbr2, str(width), str(height), afile, sabr, project_file)
			elif all((not is_profile, not is_level)):
				cmd_file = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -vf \"scale=%s:%s\" -movflags faststart -threads 2 -c:a %s -af \"dynaudnorm\" %s " % (
							   lf, vfile, str(width), str(height), afile, project_file)
				cmd_file2 = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -b:v %s -maxrate %s -bufsize %s -vf \"scale=%s:%s\" -movflags faststart -threads 2 -c:a %s -b:a %s -af \"dynaudnorm\" %s " % (
								lf, vfile, svbr, svbr, svbr2, str(width), str(height), afile, sabr, project_file)

		elif all((is_change == False, vfile, afile,
				  bitrate_data)):  # optimized_width # width*height # vcodec(acodec) # is_bitrate
			if all((is_profile, is_level)):
				cmd_file = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -profile:v main -level 30 -movflags faststart -threads 2 -c:a %s %s " % (
							   lf, vfile, afile, project_file)
				cmd_file2 = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -b:v %s -maxrate %s -bufsize %s -profile:v main -level 30 -movflags faststart -threads 2 -c:a %s -b:a %s %s " % (
								lf, vfile, svbr, svbr, svbr2, afile, sabr, project_file)
			elif all((is_profile, not is_level)):
				cmd_file = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -profile:v main -movflags faststart -threads 2 -c:a %s %s " % (
							   lf, vfile, afile, project_file)
				cmd_file2 = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -b:v %s -maxrate %s -bufsize %s -profile:v main -movflags faststart -threads 2 -c:a %s -b:a %s %s " % (
								lf, vfile, svbr, svbr, svbr2, afile, sabr, project_file)
			elif all((not is_profile, is_level)):
				cmd_file = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -level 30 -movflags faststart -threads 2 -c:a %s %s " % (
							   lf, vfile, afile, project_file)
				cmd_file2 = "cmd /c " + "".join([path_for_queue, "ffmpeg.exe"]) + " -hide_banner -y -i \"%s\" -map_metadata -1 -threads 2 -c:v %s -b:v %s -maxrate %s -bufsize %s -level 30 -movflags faststart -threads 2 -c:a %s -b:a %s %s " % (
								lf, vfile, svbr, svbr, svbr2, afile, sabr, project_file)

		else:
			# new/update: width/height, h264, vbr, aac/copy, main, 30, $file$
			unknown_convert = ";".join([str(width), str(height), vcodec, svbr, acodec, profile, level,
										lf])  # vcodec/acodec(by_bitrate)

			write_log("debug unknown_parameters", "%s" % unknown_convert)  # machine_learning

		if cmd_file:
			filecmdbase_dict[lf.strip()] = cmd_file.strip() ### debug ###

			write_log("debug withoutvbr/withoutabr", "%s" % cmd_file)

		if cmd_file2:
			write_log("debug withvbr/withabr", "%s" % cmd_file2)

		pathbase_dict[lf.strip()] = "True" if is_change else "False"

		write_log("debug is_changed[+]", "%s [%s]" % (pathbase_dict[lf.strip()], lf))

	if fext_dict:
		write_log("debug jobs[ext]", "%s" % str(fext_dict))  # dict_to_str(ext_count)

	del MT

	# count_avg_by_sum_and_length

	if any((hms_sum, hms_len)):
		try:
			hms_avg: int = hms_sum // hms_len
		except:
			hms_avg: int = 0

		write_log("debug hms_avg", "%d [%d] [%s]" % (
			hms_avg, hms_len, str(datetime.now())))  # avg_size_by_length # length_data # datetime

	#not_mp4_format
	'''
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
	'''

	del MM


	if filecmdbase_dict:

		write_log("debug run[mp4]", "%s" % str(datetime.now()))

		ready_and_move: dict = {}

		# filecmdbase_dict = {k:v for k, v in filecmdbase_dict.items() if any(("scale" in v.lower(), "profile" in v.lower(), "level" in v.lower()))}

		# get_short_filenames(findfiles/"jobdata") # debug/test

		# shorts_in_list(upgrade)
		try:
			# short_list = [crop_filename_regex.sub("", lf.split("\\")[-1]) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))] # equal
			short_list = [
				crop_filename_regex.sub("", lf.split("\\")[-1]).split("_")[0].strip() if lf.split("\\")[-1].count(
					"_") > 0 else crop_filename_regex.sub("", lf.split("\\")[-1]).strip() for lf in
				filter(lambda x: os.path.exists(x), tuple(lfiles))]  # match_or_equal
		except:
			short_list = []  # old(no_gen) # crop_filename_regex.sub("", lf.split("\\")[-1]) for lf in filter(lambda x: os.path.exists(x), tuple(lfiles))
		else:
			if short_list:
				tmp: list = []

				tmp = list(set([sl.strip() for sl in short_list if len(sl) >= 2]))
				short_list = sorted(tmp, reverse=False)

		tmp = list(set([sl.strip() for sl in filter(lambda x: x, tuple(short_list))]))

		short_list = sorted(tmp, reverse=False)
		# short_list = sorted(tmp, key=len, reverse=False)

		if short_list:
			write_log("debug short", ";".join(short_list))  # short_files
			write_log("debug shortsave", "%d" % len(short_list))  # count_files

		fcmd_filter: list = []

		MM = MyMeta() #7

		for k, v in filecmdbase_dict.items():

			if not filecmdbase_dict:
				break

			if any((not k, not v)):
				continue

			try:
				fileinfo = (k, MM.get_length(MM))
			except:
				continue
			else:
				fcmd_filter.append(fileinfo)

		fcmd_sorted_tuple = sorted(fcmd_filter, key=lambda fcmd_filter: fcmd_filter[1])

		if all((fcmd_sorted_tuple, len(fcmd_sorted_tuple) <= len(filecmdbase_dict))):
			filecmdbase_dict = {k:v for fst in fcmd_sorted_tuple for k, v in filecmdbase_dict.items() if
								   os.path.exists(k) and fst[0].strip() == k.strip()}

		# '640+360+h264+704+aac+384+high+30+c:\\downloads\\mytemp\\ffmpeg -y -i \"d:\\multimedia\\video\\serials_conv\\Interview_With_The_Vampire\\Interview_With_The_Vampire_01s06e.mp4\" -threads 2 -c:v libx264 -vf \"scale=640:360:flags=lanczos,pad=640:480:0:60\" -threads 2 -c:a copy \"c:\\downloads\\Interview_With_The_Vampire_01s06e_360p_sd.mp4\"'
		# (st.count("+"), st.count(":")) # (8, 10)

		# '640:360:h264:704:aac:320:high:30:c:\\downloads\\mytemp\\ffmpeg -y -i \"d:\\multimedia\\video\\serials_conv\\King_of_Queens\\King_of_Queens_03s13e.mp4\" -threads 2 -c:v libx264 -vf \"scale=640:360:flags=lanczos,pad=640:480:0:60\" -threads 2 -c:a copy \"c:\\downloads\\King_of_Queens_03s13e_360p_sd.mp4\"'
		# (st.count("+"), st.count(":")) # (0, 18)

		# need_optimize_current_jobs_by_param
		filecmdbase_dict = {k: v for k, v in filecmdbase_dict.items() if
					any(("scale" in v.lower(), "profile" in v.lower(), "level" in v.lower()))}

		if filecmdbase_dict: # filesize(optimize)_or_abc(default)_sort
			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False)

		jobs_list = sorted([*filecmdbase_dict], reverse=False) if [*filecmdbase_dict] else []

		is_rec = False

		if jobs_list:
			try:
				with open(jobs_base, encoding="utf-8") as fbf:
					files_dict = json.load(fbf)
			except: # IOError
				files_dict = {}

				with open(jobs_base, "w", encoding="utf-8") as fbf:
					json.dump(files_dict, fbf, ensure_ascii=False, indent=2, sort_keys=True)

			else:
				# with unique_semaphore:
				for jl in jobs_list:

					if not jobs_list: # no_data
						break

					try:
						fname = jl.split("\\")[-1]
					except:
						fname = ""

					if not fname or not os.path.exists(jl):
						continue

					is_rec = False

					try:
						is_rec = True if files_dict[jl.strip()] else False
					except:
						files_dict[jl.strip()] = str(datetime.now())  # if_error(KeyError)
					else:
						files_dict[jl.strip()] = str(datetime.now())  # any_rec(no_error)

			if files_dict:
				files_dict = {k: v for k, v in files_dict.items() if
								os.path.exists(k)}

				with open(jobs_base, "w", encoding="utf-8") as fbf:
					json.dump(files_dict, fbf, ensure_ascii=False, indent=2, sort_keys=True)

		# null_command_line_script

		open("c:\\downloads\\mytemp\\jresize.cmd", "w").close()  # stay_current_jobs_no_hidden(manual_run)

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
		except: # IOError
			nob_dict = {}

			with open(new_optimize_base, "w", encoding="utf-8") as nobf:
				json.dump(nob_dict, nobf, ensure_ascii=False, indent=2, sort_keys=True)

		# nob_dict = {k:v for k, v in nob_dict.items() if os.path.exists(k) and all((sum(v) > 0, len(v) == 3))} # 1/2/3 # default(length=3) # skip_try_except
		nob_dict = {k: v for k, v in nob_dict.items() if
						os.path.exists(k)}  # without_length # skip_try_except

		for k, v in filecmdbase_dict.items():

			write_log("debug filecmdbase_dict[job][index]", "%s" % "x".join(
				[k.strip(), str(v.count("scale")), str(v.count("profile")), str(v.count("level"))]))

			if all((k, v)):

				scale_count = v.count("scale");
				profile_count = v.count("profile");
				level_count = v.count("level")

				if scale_count:
					s_c += 1

				if profile_count:
					p_c += 1

				if level_count:
					l_c += 1

				nob_dict[k.strip()] = (
					str(scale_count), str(profile_count), str(level_count))  # is_optimize(1 found, 0 not_found)

				print(Style.BRIGHT + Fore.CYAN + "%s\t(%s, %s, %s)" % (
					k.strip(), str(s_c), str(p_c), str(l_c)))  # scale_count -> s_c ...
				write_log("debug filecmdbase_dict[count]",
						  "%s\t(%s, %s, %s)" % (k.strip(), str(s_c), str(p_c), str(l_c)))

		if any((s_c, p_c, l_c)):
			cnt_index = {"scale": s_c, "profile": p_c, "level": l_c}
			write_log("debug filecmdbase_dict[index]", "%s" % str(cnt_index))

		nob_dict = {k: v for k, v in nob_dict.items() if
						os.path.exists(k)}

		with open(new_optimize_base, "w", encoding="utf-8") as nobf:
			json.dump(nob_dict, nobf, ensure_ascii=False, indent=2, sort_keys=True)
		# filter(filecmdbase_dict/trends_dict) # debug/test

		# set_or_update(trends)_by_any_video # hidden(debug)
		trends_dict: dict = {}
		try:
			with open(trends_base, encoding="utf-8") as ftf:
				trends_dict = json.load(ftf)
		except: # IOError
			trends_dict = {}

			with open(trends_base, "w", encoding="utf-8") as ftf:
				json.dump(trends_dict, ftf, ensure_ascii=False, indent=2, sort_keys=False)

		else:
			try:
				jobs_trends_dict = {k: str(datetime.now()) for k, v in trends_dict.items() for k2, v2 in
									filecmdbase_dict.items() if
									k.strip() == crop_filename_regex.sub("", k2).strip()}  # k, k2
			except:
				jobs_trends_dict = {}

			if jobs_trends_dict:
				trends_dict.update(jobs_trends_dict)

			try:
				fdates: list = list(set([v.strip() for k, v in trends_dict.items() if str(datetime.today()).split(" ")[0] in v])) # only_current_day
			except:
				fdates: list = []
			else:
				fdates.sort(reverse=False)

			try:
				fdates_dict = {k: v for fd in fdates for k, v in trends_dict.items() if
									v.strip() == fd.strip()}
			except:
				fdates_dict = {}
			else:
				if all((fdates_dict, len(fdates_dict) <= len(trends_dict))): # trends_dict
					trends_dict = fdates_dict  # update_without_sort

			with open(trends_base, "w", encoding="utf-8") as ftf:
				json.dump(trends_dict, ftf, ensure_ascii=False,
						  indent=2)  # update_trends(short)_if_mp4 # sort_keys=False

		# with unique_semaphore:
		# for k, v in filecmdbase_dict.items():
		# print(Style.BRIGHT + Fore.WHITE + "Файл %s будет обработан [level=%d]" % (k.strip(), count_level_from_full(k))) # level=6

		# if filecmdbase_dict:
		# print()

		sorted_files = list(filecmdbase_dict.keys())  # sort_current_jobs(pass_1_of_2)

		unique = full_list = set()
		try:
			# tmp = list(sf_gen()) # new(yes_gen)
			tmp: list = [sf.strip() for sf in filter(lambda x: os.path.exists(x), tuple(sorted_files))]
		except:
			tmp: list = []  # old(no_gen) # sf.strip() for sf in filter(lambda x: os.path.exists(x) , tuple(sorted_files))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		sorted_files = sorted(tmp2, reverse=False)

		for sf in sorted_files:  # filter(lambda x: x, tuple(tmp))

			if not sorted_files:  # skip_if_nulllist
				break

			try:
				fp, fn = split_filename(sf)
			except:
				fn = sf.split("\\")[-1].strip() # fp

			try:
				fname = fn
			except:
				fname = ""

			if all((not fname in unique, fname)):
				unique.add(fname)  # short_file(first)_by_set
				full_list.add(sf)  # full_filename(first)_by_set
		if full_list:
			temp = list(set(full_list))  # unique_filenames
			sorted_files = sorted(temp, reverse=False)

		def files_to_short_by_full(sorted_files=sorted_files):
			for sf in filter(lambda x: os.path.exists(x), tuple(sorted_files)):
				if all((sf, crop_filename_regex.sub("", sf.split("\\")[-1]))):
					if sf:
						yield sf.strip()
					else:
						yield ""
				else:
					yield ""

		try:
			tmp: list = list(files_to_short_by_full()) # new(yes_gen)
		except:
			tmp: list = []  # old(no_gen) # sf.strip() for sf in filter(lambda x: os.path.exists(x), tuple(sorted_files)) if all((sf, crop_filename_regex.sub("", sf.split("\\")[-1])))

		tmp2 = list(set([t.strip() for t in filter(lambda x: x, tuple(tmp))]))
		sorted_files = sorted(tmp2, reverse=False)

		try:
			temp: list = asyncio.run(filter_from_list(sorted_files))  # current_jobs + base
		except:
			temp: list = []
		else:
			if temp:
				temp2 = list(set(temp))  # unqiue_no_dublicates
				sorted_files = sorted(temp2, reverse=False)

		if sorted_files:
			with open(files_base["backup"], "w", encoding="utf-8") as bjf:
				bjf.writelines("%s\n" % cmd.strip() for cmd in filter(lambda x: x, tuple(sorted_files)))  # save_current_jobs(exists)

		elif not sorted_files:  # exit_if_not_found_some_files
			exit()

		# save_command_line_script
		with open("c:\\downloads\\mytemp\\jresize.cmd", "a") as jcf:
			jcf.writelines("%s\n" % cmd.strip() for cmd in filter(lambda x: x, tuple(filecmdbase_dict.values())))  # save_all_cmd(for_run)

		ready_set = set()

		for k, v in filecmdbase_dict.items():

			if not filecmdbase_dict: # no_data
				break

			if not os.path.exists(k): # no_exists
				continue

			try:
				fname1 = v.split(" ")[-1].split("\\")[-1].strip()
			except:
				fname1 = ""

			try:
				fp, fn = split_filename(k)
			except:
				fn = k.split("\\")[-1].strip() # fp

			try:
				fname2 = fn
			except:
				fname2 = ""

			if all((fname1 == fname2, fname1, fname2)):
				print(Style.BRIGHT + Fore.WHITE + "Файл %s" % fname1,
					  Style.BRIGHT + Fore.YELLOW + "будет добавлен или обновлён после обработки")
				write_log("debug job[addupdate]", "Файл %s будет добавлен или обновлён после обработки" % fname1)

				ready_and_move[v.split(" ")[-1].strip()] = k.strip()

		# run(["cmd", "/c", "c:\\downloads\\mytemp\\jresize.cmd"], shell=False) # command_line_script_to_run # old_script

		hours_set = set()

		try:
			with open(files_base["hours"], encoding="utf-8") as fbhf:
				max_hour_list = fbhf.readlines()
		except: # IOError
			max_hour_list = [2] # default = 2

			with open(files_base["hours"], "w", encoding="utf-8") as fbhf:
				fbhf.writelines("%d\n" % int(mhl) for mhl in filter(lambda x: x, tuple(max_hour_list))) # save_total_time_run_by_hour

		if max_hour_list:  # hour_variables
			temp = list(set([mhl.strip() for mhl in filter(lambda x: x, tuple(max_hour_list)) if
							all((int(mhl) >= 0, mhl != None))]))  # hours_list(string)
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
			epis_filter: list = list(set([epis_regex.findall(k.split("\\")[-1])[0].strip() for k, v in filecmdbase_dict.items() for fp, fn in split_filename(k) if ((fn, k, fn == k.split("\\")[-1], epis_regex.findall(fn)))]))
		except:
			epis_filter: list = []
		finally:
			epis_filter.sort(reverse=False)

		try:
			year_filter: list = list(set([year_regex.findall(k.split("\\")[-1])[0].strip() for k, v in filecmdbase_dict.items() for fp, fn in split_filename(k) if all((fn, k, fn == k.split("\\")[-1], year_regex.findall(fn)))]))
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

			combine_filter = sorted(tmp, reverse=False) # sort_by_abc
			# combine_filter = sorted(tmp, key=len, reverse=False) # sort_by_key

			filecmdbase_dict_new = {k: v for cf in combine_filter for k, v in filecmdbase_dict.items() if
									all((cf, k, v, cf in k.split("\\")[-1].strip()))}

			if all((filecmdbase_dict_new, len(filecmdbase_dict_new) <= len(filecmdbase_dict))): # filecmdbase_dict
				filecmdbase_dict.update(filecmdbase_dict_new)

			write_log("debug combine_filter", "%s" % ";".join(combine_filter))

		# debug
		# exit() # is_manual_run(stop)

		if filecmdbase_dict:  # seas_year_filter(combine_filter) # jobs # filter_by_base(tmp_combine_jobs)

			cnt: int = 0

			MT = MyTime(seconds=2)

			fsizes: int = 0

			disk_space_limit: int = 0
			# disk_space_limit: int = 16 * (1024**3) # 16Gb


			lastfile: list = []

			jobs: list = [] # filecmdbase_dict

			# @another_list # @last.xml @src=k/len=length(k)/dst=v.split(" ")[-1] # move_dst_to_src

			# xml(job(src=k/len=length(k)/dst=v.split(" ")[-1])) # save_job_to_xml(mp4)
			# '''
			# @log_error
			async def save_job_to_xml(src: str = "", dst: str = ""): # save_last_job # need_multiple_record

				if src and not os.path.exists(src): # any((not src, not dst)) # null_path # not dst # no_dst # no_assert
					return

				global jobs

				MM = MyMeta() #8

				# jobs = [{"src": k, "leng": MM.get_length(k), "dst": v.split(" ")[-1]}] # one_record
				jobs = [{"src": src, "leng": MM.get_length(src), "dst": dst}] # one_record

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
					write_log("debug jobs[xml][saveerror]", "Xml save error (job) %s [%s]" % (str(e), str(datetime.now())), is_error=True) # main_xml_error
				else:
					try:
						# save_xml
						with open(files_base["lastjob"], "wb") as vrf: # "".join([script_path, '\\last.xml'])
							tree.write(vrf)

					except BaseException as e:
						print(Style.BRIGHT + Fore.RED + "Xml save error (job)")
						write_log("debug jobs[saveerror]", "Xml save error (job) %s [%s]" % (str(e), str(datetime.now())), is_error=True) # some_error_in_save
					else:
						print(Style.BRIGHT + Fore.GREEN + "Xml saved")
						write_log("debug jobs[xml][save]", "save ok [%s]" % str(datetime.now())) # xml_saved

					# clear_xml(logic)
					'''
					for country in root.findall('country'):
						# using root.findall() to avoid removal during traversal
						rank = int(country.find('rank').text)
						if rank > 50:
							root.remove(country)

					tree.write('output.xml')
					'''

			# '''

			# '''
			# @optimial_job_for_jobs_by_xml(load)
			async def load_job_from_xml() -> list: # load_last_job # dict_in_list
				jobs = []

				try:
					tree = xml.parse(file=files_base["lastjob"]) # xml.ElementTree(file=files_base["lastjob"])

					root = tree.getroot()

					for elem in root.iter(tag="job"): # <jobs><job><src>d:\multimedia\video\serials_conv\Legacies\Legacies_04s11e.mp4</src><leng>2492</leng><dst>c:\downloads\Legacies_04s11e.mp4</dst></job></jobs>
						job = {}

						for subelem in elem:
							job[subelem.tag] = subelem.text

						jobs.append(job)
				except BaseException as e:
					print(Style.BRIGHT + Fore.RED + "Xml load error (job)")
					write_log("debug jobs[xml][loaderror]", "Xml load error (job) %s [%s]" % (str(e), str(datetime.now())), is_error=True) # main_xml_error
				else:
					if jobs: # logging_if_some_data # ... Xml loaded # dict's_to_list
						print(Style.BRIGHT + Fore.WHITE + "%s" % str(jobs), Style.BRIGHT + Fore.GREEN + "Xml loaded")
						write_log("debug jobs[xml][load]", "load ok [%s]" % str(datetime.now())) # xml_loaded

					return jobs # [{"src": "d:\\multimedia\\video\\serials_europe\\Nelichnaya_zhizn_Rus\\Nelichnaya_zhizn_01s04e.mp4", "leng": 5000, "dst": "c:\\downloads\\Nelichnaya_zhizn_01s04e.mp4"}]

			# 5000(src_length) ~ (5000//3600) = 1 hh, (5000//60)%60 = int((mm(1.38)-hh)*100) ~ 38 # sample_calc
			# '''

			MM = MyMeta() #9

			fcmd_filter: list = []

			# short_count: dict = {}
			# seasyear_count: dict = {}

			# combine_job_filter # convert_combine_jobs_to_current_jobs # calc_avg_time_by_combine_jobs
			# '''
			# load_meta_jobs(filter) #10
			try:
				with open(some_base, encoding="utf-8") as sbf:
					somebase_dict = json.load(sbf)
			except:
				somebase_dict = {}

				with open(some_base, "w", encoding="utf-8") as sbf:
					json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sork_keys=True) #1-save_current_meta(new)

			# filter_stay_only_exists_jobs(is_meta)
			first_len: int = len(somebase_dict)
			somebase_dict = {k:v for k, v in somebase_dict.items() if os.path.exists(k)}
			second_len: int = len(somebase_dict)

			if all((second_len, second_len <= first_len)):
				with open(some_base, "w", encoding="utf-8") as sbf:
					json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True) #1-save_current_meta(update)

			write_log("debug somebase_dict[mcount]", "%d" % len(somebase_dict)) # after_load(meta)

			# current_jobs # is_find_job_in_meta_base
			try:
				with open(filecmd_base, encoding="utf-8") as fbf:
					filecmdbase_dict = json.load(fbf)
			except: # IOError
				filecmdbase_dict = {}

				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False) #2-save_current_jobs(new)

			first_len = second_len = 0

			# filter_current_jobs_(in_meta/no_in_meta/exists_only)
			try:
				first_len: int = len(filecmdbase_dict)
				filecmdbase_dict = {k:v for k, v in filecmdbase_dict.items() if	os.path.exists(k) and any((k.strip() in [*somebase_dict], not [*somebase_dict]))}
			except:
				filecmdbase_dict = {k:v for k, v in filecmdbase_dict.items() if os.path.exists(k)}
			finally:
				second_len: int = len(filecmdbase_dict)

			if all((second_len, second_len <= first_len)):
				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False) #2-save_current_jobs(update)

			write_log("debug filecmdbase_dict[jcount]", "%d" % len(filecmdbase_dict)) # after_load(current)

			# combine_jobs # is_find_job_in_meta_base
			cbf_dict: dict = {}

			try:
				with open(cfilecmd_base, encoding="utf-8") as cbf:
					cbf_dict = json.load(cbf)
			except: # IOError
				cbf_dict = {}

				with open(cfilecmd_base, "w", encoding="utf-8") as cbf:
					json.dump(cbf_dict, cbf, ensure_ascii=False, indent=2, sort_keys=False) #3-save_combine_jobs(new)

			first_len = second_len = 0

			# filter_combine_jobs_(in_meta/no_in_meta/exists_only)
			try:
				first_len: int = len(cbf_dict)
				cbf_dict = {k:v for k, v in cbf_dict.items() if os.path.exists(k) and any((k.strip() in [*somebase_dict], not [*somebase_dict]))}
			except:
				cbf_dict = {k: v for k, v in cbf_dict.items() if os.path.exists(k)}
			finally:
				second_len: int = len(cbf_dict)

			write_log("debug cbf_dict[cjcount]", "%d" % len(cbf_dict)) # after_load(combine)

			if all((second_len, second_len <= first_len)):
				with open(cfilecmd_base, "w", encoding="utf-8") as cbf:
					json.dump(cbf_dict, cbf, ensure_ascii=False, indent=2, sort_keys=False) #3-save_combine_jobs(update)

			# sorted_current_jobs # type1
			# '''
			MM = MyMeta()

			fcbd: list = []
			fcbd_sorted: list = []

			for k, v in filecmdbase_dict.items():

				if not filecmdbase_dict: # no_data
					break

				try:
					fname = k.split("\\")[-1].strip()
				except:
					fname = ""

				if os.path.exists(k) and fname: # exists_job
					try:
						gl = MM.get_length(k) # int
					except:
						gl = 0

					try:
						fs = os.path.getsize(k) # int
					except:
						fs = 0

					try:
						short = crop_filename_regex.sub("", fname).strip() # regex
					except:
						short = ""
					# else: # hide_count
						# if short:
							# try:
								# short_count[short.strip()] = short_count.get(short, 0) + 1 # short_count
							# except:
								# continue # skip_if_some_error

					try:
						seas_or_year = crop_filename_regex.findall(fname)[0][0].strip() # regex(short) # type1
						# seas_or_year2 = "".join(crop_filename_regex.findall(fname.split(".")[0])[0]) # .replace("_", "").replace("(", "").replace(")", "") # is_crop_syms # str(short) # type2
					except:
						seas_or_year = ""
					# else: # hide_count
						# if seas_or_year:
							# try:
								# seasyear_count[seas_or_year.strip()] = seasyear_count.get(seas_or_year.strip(), 0) + 1 # seas_or_year_count
							# except:
								# continue # skip_if_some_error

					# fname = "hello_world_01s01e" -> "01s01e" # fname = "my_name_is(2000)" -> "2000"

					# is_shorts_in_list(upgrade)
					try:

						# keywords = fname.split(".")[0].split("_")[0:fname.count("_")] # short / (no_seasepis / no_year) # list(short)
						keywords = fname.split(".")[0].split("_") # short / (seasepis / year) # list(full)
						# keywords = fname.split(".")[0].split("_")[-1:] if not "(" in fname else ? # seasepis / ?
					except:
						keywords = []

					if all((gl, fs, short, seas_or_year, keywords, keywords[-1])):
						fcbd.append((k, gl, fs, short, seas_or_year, keywords, keywords[-1])) # filename / length / filesize / short_filename / (seas/year) / keywords_by_list / seasepis
				elif not os.path.exists(k): # skip_no_exists_job
					continue

			#{filename: (filename, length, filesize, short_filename, seas_or_year, by_words)}
			try:
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[1]) # sorted_by_length(int) # (framecount/length)_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[2]) # sorted_by_filesize(int) # filesizes_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[3]) # sorted_by_short_filename(str) # short+(seas/year)_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[4]) # sorted_by_seas_or_year(str) # short_in_str_by_abc
				# fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[5]) # sorted_keywords(list) # short_in_list_by_abc
				fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[6]) # sorted_by_seas_epis(last_in_list) # (seasepis/year)_by_abc
			except:
				fcbd_sorted = sorted(fcbd, key=lambda fcbd: fcbd[0]) # sorted_by_filename

			for fs in fcbd_sorted:

				if not fcbd_sorted:
					break

				print(Style.BRIGHT + Fore.CYAN + "%s" % ";".join([full_to_short(fs[0]), str(fs[1:])])) # str(fs)
				write_log("debug fcbd_sorted", "%s" % str(fs))

			# if all((fcbd_sorted, len(fcbd_sorted) <= list(set([*fcbd])))):
				# pass

			# and (isinstance(fs[1], str) and any((k.strip().startswith(fs[1]), fs[1] in k.strip())) or isinstance(fs[0], int))
			if all((fcbd_sorted, len(fcbd_sorted) <= len(filecmdbase_dict))):
				filecmdbase_dict = {k: v for fs in fcbd_sorted for k, v in filecmdbase_dict.items() if
							os.path.exists(k) and fs[0].strip() == k.strip()} # for_any_sort_types

			del MM
			# '''

			with open(filecmd_base, "w", encoding="utf-8") as fbf:
				json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False) # save_current_jobs

			# is_skip_database

			yes_files: list = []
			no_files: list = []

			# clear_every_time # is_true_jobs_count
			'''
			open("".join([script_path, '\\video_resize.db']), "w").close()
			'''

			# @connect_to_database(start)
			# '''
			conn = sql.connect("".join([script_path, '\\video_resize.db'])) # conn = sql.connect(":memory:")
			'''
			# conn.row_factory = sqlite3.Row # dict # fields_to_dict_keys
			# for res in conn.execute("SELECT * FROM filebase"):
				# print(res["filename"], res["filesize"]) # dict_data
			'''

			# database_backup_to_sql # is_database_backup
			async def database_backup(file="video_resize.sql"):
				with open("".join([script_path, "\\%s" % file]), "w") as f:
					for line in conn.iterdump():
						f.write("%s\n" % line)

			# database_recovery_from_sql # is_database_recovery
			'''
			async def database_recovery(file="video_resize.sql"):
				sql_script: list = []

				with open("".join([script_path, "\\%s" % file, "r") as f:
					sql_script = f.read()

				curr.executescruot(sql_script)
				conn.commit()
			'''

			asyncio.run(database_backup())
			# asyncio.run(database_recovery())

			cur = conn.cursor()

			'''
			# sql.apilevel # '2.0'
			# sql.sqlite_version # '3.31.1'
			# sql.sqlite_version_info # (3, 31, 1)

			# dir(conn) # @ connect_samples
			# dir(cur) # @ cursor_samples

			# fileid INT PRIMARY KEY, # hide_sql_field
			'''

			# @create_table
			# '''
			with conn:
				cur.execute("""CREATE TABLE IF NOT EXISTS filebase(filename TEXT, filesize INTEGER, daterun TEXT);""")
				conn.commit()
			# '''

			# execute(@insert_one)
			'''
			# @sample_one_record
			fileinfo = (k.strip(), os.path.getsize(k), str(datetime.now())) # file / filesize / daterun

			with conn:
				cur.execute("INSERT INTO filebase VALUES (?, ?, ?);", fileinfo)
				conn.commit()
			'''

			# executemany(@insert_multiple)
			'''
			# @sample_multiple_record
			fileinfo = (k.strip(), os.path.getsize(k), str(datetime.now())) # file / filesize / daterun

			multiple_data.append(fileinfo)

			with conn:
				cur.executemany("INSERT INTO filebase VALUES (?, ?, ?);", multiple_data)
					conn.commit()
			'''

			# avg / classify / is_max / count_jobs(max/20)
			'''
			fsize_sum: int = 0
			fsize_len: int = 0
			fsize_avg: int = 0
			fcount: int = 0

			fsize_list: list = []
			fsize_classify: list = []

			for k, v in filecmdbase_dict.items():

				try:
					fsize = os.path.getsize(k)
				except:
					fsize = 0

				if fsize:
					fcount += 1
					fsize_list.append(fsize)

			if fsize_list:
				fsize_sum = sum(fsize_list)
				fsize_len = fcount if fcount == len(fsize_list) else len(fsize_list) # any_equal_result
				fsize_avg = fsize_sum // fsize_len

			if all((fsize_avg, fsize_list)):
				try:
					fsize_classify = [(0, fl) if fl - fsize_avg > 0 else (1, fl) for fl in fsize_list] # if_some_classify_by_filesize
				except:
					fsize_classify = [] # null_if_no_classify

			if fsize_classify: # what_max
				is_max1, is_count1 = 0, 0
				is_max2, is_count2 = 0, 0

				for fc in fsize_classify:
					if fc[0] == 0 and fc[1] > is_max1: # classify(0)
						is_max1 = fc[1]
						is_count1 += 1
					elif fc[0] == 1 and fc[1] > is_max2: # classify(1)
						is_max2 = fc[1]
						is_count2 += 1

			default_jobs = max(is_count1, is_count2) # max_filesize(current_jobs)
			write_log("debug default_jobs[1]", "%d" % default_jobs) # if_zero_no_logic / if_not_zero_ok

			if any((not default_jobs, default_jobs > 20)): # if_null_or_more_20_jobs
				default_jobs = 20 # default(10)
				write_log("debug default_jobs[null]", "%d" % default_jobs)

			gcl_error: bool = False

			# select_jobs_by_range(default_jobs)
			try:
				# get_count_list = [*filecmdbase_dict][len(filecmdbase_dict)-default_jobs: len(filecmdbase_dict)] if len(filecmdbase_dict) > default_jobs else [*filecmdbase_dict] # last_jobs
				get_count_list = [*filecmdbase_dict][0:default_jobs] if len(filecmdbase_dict) > default_jobs else [*filecmdbase_dict] # first_jobs # is_debug
			except:
				get_count_list = [*filecmdbase_dict] # if_error_select_all_jobs # is_debug
				gcl_error = True
			else:
				gcl_error = False

			if get_count_list:
				write_log("debug get_count_list", "Run count: %d [%s]" % (len(get_count_list), str(gcl_error))) # run_jobs_by_count / is_error
			'''

			for k, v in filecmdbase_dict.items(): # somebase_dict # cbf_dict

				if not filecmdbase_dict: # no_current_jobs
					break

				if any((not k, not v)): # skip_if_some_null # all((not k in get_count_list, get_count_list)) # skip_job_if_not_in_list
					continue

				try:
					fileinfo = (k.strip(), os.path.getsize(k), str(datetime.now())) # file / filesize / daterun
				except:
					fileinfo = ()

				if os.path.exists(k) and fileinfo:

					if all((k, any((not k in yes_files, k in [*somebase_dict])))): # exists / yes_in_metabase
						yes_files.append(k)

					try:
						with conn:
							cur.execute("SELECT * FROM filebase WHERE filename = ?;", (fileinfo[0],)) # rowid - номер записи # select rowid, * from filebase
					except:
						with conn:
							cur.execute("SELECT * FROM filebase WHERE filename = :filename;", {"filename": fileinfo[0]}) # rowid - номер записи # select rowid, * from filebase
					finally: # else
						write_log("debug filecmdbase_dict[select][yes_files]", "%s [%s]" % (fileinfo[0], str(datetime.now())))

						try:
							sql_count = len(cur.fetchall())
						except:
							sql_count = -1
						else:
							if sql_count == 0:
								with conn:
									cur.execute("INSERT INTO filebase VALUES (?, ?, ?);", fileinfo)
									conn.commit()

								write_log("debug filecmdbase_dict[insert]", "%s [%s]" % (str(fileinfo), str(datetime.now())))
							elif sql_count == 1:
								try:
									with conn:
										cur.execute("UPDATE filebase set filesize = ? where filename = ?;", (fileinfo[1], fileinfo[0])) # ?
										conn.commit()
								except:
									with conn:
										cur.execute("UPDATE filebase set filesize = :filesize where filename = :filename;", {"fileize": fileinfo[1], "filename": fileinfo[0]}) # ?
										conn.commit()

								write_log("debug filecmdbase_dict[update]", "%s [%s]" % (str(fileinfo), str(datetime.now())))

							write_log("debug filecmdbase_dict[yes_files]", "Файл %s присутствует в базе или списке [%d] [%d]" % (fileinfo[0],
										 sql_count, len(yes_files))) # filename / found_in_database / yes_file

				elif not os.path.exists(k) and fileinfo:

					if all((k, any((not k in no_files, not k in [*somebase_dict])))): # no_exists / no_in_metabase
						no_files.append(k)

					try:
						with conn:
							cur.execute("SELECT * FROM filebase WHERE filename = ?;", (fileinfo[0],)) # rowid - номер записи # select rowid, * from filebase
					except:
						with conn:
							cur.execute("SELECT * FROM filebase WHERE filename = :filename;", {"filename": fileinfo[0]}) # rowid - номер записи # select rowid, * from filebase
					finally: # else
						write_log("debug filecmdbase_dict[select][no_files]", "%s [%s]" % (fileinfo[0], str(datetime.now())))

						try:
							sql_count = len(cur.fetchall())
						except:
							sql_count = -1
						else:
							if sql_count > 0:
								try:
									with conn:
										cur.execute("DELETE FROM filebase WHERE filename = ?;", (fileinfo[0],)) # ?
										conn.commit()
								except:
									with conn:
										cur.execute("DELETE FROM filebase WHERE filename = :filename;", {"filename": fileinfo[0]}) # ?
										conn.commit()

								write_log("debug filecmdbase_dict[delete]", "%s [%s]" % (str(fileinfo), str(datetime.now())))

							write_log("debug filecmdbase_dict[no_files]", "Файл %s отсутствует в базе или списке [%d] [%d]" % (fileinfo[0],
										 sql_count, len(no_files))) # filename / not_found_in_database / no_file


			# @delete_table
			# '''
			if not somebase_dict:
				with conn:
					cur.execute("DROP TABLE IF EXISTS filebase")
			# '''

			# @disconnect_from_database(end)
			# '''
			cur.close() # cursor_stop
			conn.close() # sqlite_stop # if conn: conn.close()
			# '''

			# '''
			if all((filecmdbase_dict, len(somebase_dict) >= 0)):

				try:
					unique_jobs = list(set([*filecmdbase_dict]) & set([*somebase_dict])) # use_unique_jobs(current_and_combine_jobs)
				except:
					unique_jobs = list(set([*filecmdbase_dict])) # only_current_jobs # if_error
				finally:
					if all((not unique_jobs, [*filecmdbase_dict])): # if_no_jobs(try_only_current_jobs)
						unique_jobs = list(set([*filecmdbase_dict])) # only_current_jobs

			MM = MyMeta()

			async def fcmd_generate():

				global fcmd_filter

				for k, v in filecmdbase_dict.items():

					if not filecmdbase_dict: # no_data
						break

					if not os.path.exists(k): # no_exists / null_data's(any((not k, not v)))
						continue

					try:
						gl = MM.get_length(k)
					except:
						gl = 0
					else:
						if all((gl, k in [*unique_jobs])): # some_length / find_unique_jobs(k in [*unique_jobs])
							fcmd_filter.append((k.strip(), gl)) # "os.path.getsize(k)"

			asyncio.run(fcmd_generate())

			# if all((fcmd_filter, cbf_dict)):
				# listed_sort = sorted(fcmd_filter, key=lambda lst: lst[1])

				# filecmdbase_dict = {k:v for ls in listed_sort for k, v in cbf_dict.items() if os.path.exists(k) and ls[0].strip() == k.strip()} # compare_current_and_combine_jobs

				# with open(filecmd_base, "w", encoding="utf-8") as fbf:
					# json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False)

			del MM
			# '''

			fcmd_hours: list = []
			fcmd_minutes: list = []

			if fcmd_filter:
				fcmd_hours = [ff[1] % 3600 for ff in fcmd_filter if ff[1] % 3600 > 0]
				fcmd_minutes = [(ff[1] // 60) % 60 for ff in fcmd_filter if (ff[1] // 60) % 60 > 0]

				hh_time: int = 0
				hh_avg_time: int = 0
				mm_time: int = 0
				mm_avg_time: int = 0

				# @avg_hour / @max_hour
				try:
					fcmd_hours_sum = sum(fcmd_hours)
					fcmd_hours_len = len(fcmd_hours)
					fcmd_hours_avg = (lambda fhs, fhl: fhs / fhl)(fcmd_hours_sum, fcmd_hours_len)
				except:
					fcmd_hours_avg = 0
				else:
					# hh_time = max(fcmd_hours) if max(fcmd_hours) > fcmd_hours_avg else fcmd_hours_avg # pass_1_of_2
					# hh_time = int(3600 // hh_time) if max(fcmd_hours) < 3600 else int(hh_time // 3600) # pass_2_of_2


					hh_avg_time = hh_time # is_debug

					print("Оптимально время для обработки в часах %d часов(а)" % hh_avg_time)
					write_log("debug fcmd_hours_avg[jobtime]", "Оптимально время для обработки в часах %d часов(а)" % hh_avg_time) # hh

				# @avg_minute / @max_minute

				try:
					fcmd_minutes_sum = sum(fcmd_minutes)
					fcmd_minutes_len = len(fcmd_minutes)
					fcmd_minutes_avg = (lambda fms, fml: fms / fml)(fcmd_minutes_sum, fcmd_minutes_len)
				except:
					fcmd_minutes_avg = 0
				else:
					# mm_time = max(fcmd_minutes) if max(fcmd_minutes) > fcmd_minutes_avg else fcmd_minutes_avg
					mm_time = fcmd_minutes_avg # avg_without_max
					mm_avg_time = mm_time

					print("Оптимально время для обработки в минутах %d минут(ы)" % mm_avg_time)
					write_log("debug fcmd_minutes_avg[jobtime]", "Оптимально время для обработки в минутах %d минут(ы)" % mm_avg_time) # mm

				# @optimial_time_for_jobs_by_xml(save) # dict's_in_list # debug(xml)

				asyncio.run(save_timing_to_xml(hours = hh_time, minutes = mm_time)) # optimize_by_current_jobs(is_run)

			try:
				h, m = asyncio.run(load_timing_from_xml(ind=9)) # 9 # h, m = load_timing_from_xml(ind=9)
			except:
				h, m = 0, 0

			fsizes : int = 0
			fsizes2: int = 0
			fsizes_max: int = 0

			async def fsizes_generate():
				global fsizes

				for k, v in filecmdbase_dict.items():

					if not filecmdbase_dict: # no_data
						break

					if os.path.exists(k):
						try:
							fsize = os.path.getsize(k)
						except:
							fsize = 0

						fsizes += fsize

			asyncio.run(fsizes_generate())

			if fsizes:
				fsizes_max = fsizes

			date1 = datetime.now()

			ms_set = set()

			std_dict: dict = {}

			try:
				with open(std_base, encoding="utf-8") as sbf:
					std_dict = json.load(sbf)
			except:
				with open(std_base, "w", encoding="utf-8") as sbf:
					json.dump(std_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

			if std_dict: # filter_by_exists_files
				std_dict = {k: v for k, v in std_dict.items() if os.path.exists(k)}

			# count_time # pass_1_of_2
			MM = MyMeta()

			hms_list: list = []

			summ: int = 0
			sum_fsizes: int = 0
			fsizes_lst: list = []
			filecmdbase_pos_dict: dict = {}

			for k, v in filecmdbase_dict.items():

				if not filecmdbase_dict:  # no_data
					break

				try:
					fname = k.split("\\")[-1]
				except:
					fname = ""

				if not fname or not os.path.exists(k):
					continue

				try:
					fsize = os.path.getsize(k)
				except:
					fsize = 0

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

					if any((gl == (hh * 3600) + (mm * 60) + ss, gl == hh * mm * ss)):
						print(Style.BRIGHT + Fore.CYAN + "%s [%s]" % (str(hms_list[-1]), str(datetime.now()))) # show_last_time_and_file_with_framecount # is_color
						write_log("debug hms_list", "%s [%s]" % (str(hms_list[-1]), str(datetime.now()))) # last_record

			del MM

			# current_jobs # update_by_classify # user_load # pass_2_of_2
			'''
			try:
				with open(filecmd_base, encoding="utf-8") as fbf:
					filecmdbase_dict = json.load(fbf)
			except: # IOError
				filecmdbase_dict = {}

				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False) #2-save_current_jobs(new)
			'''

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
					favg = (lambda s,l: s/l)(fsum / flen)
				except:
					favg = 0

				try:
					sum_classify = {fl: 1 if fl - favg > 0 else 0 for fl in fsizes_lst} # is_big(is_small)
				except:
					sum_classify = {}

				# jobs_count = len(sum_classify)
				fsizes_classify = [*sum_classify]

				if all((fsizes_classify, len(fsizes_classify) <= len(filecmdbase_dict))):
					if len(fsizes_classify) != len(filecmdbase_dict):
						is_classify = True
						write_log("debug sum_classify[fsizes_list][different]", "Найдено %d классицированных задач из %d файлов [%s]" % (len(fsizes_classify), len(filecmdbase_dict), str(datetime.now())))
					elif len(fsizes_classify) == len(filecmdbase_dict):
						is_classify = True
						write_log("debug sum_classify[fsizes_list][equal]", "Найдено %d одинаковых классицированных задач с файлами [%s]" % (len(fsizes_classify), str(datetime.now())))
				elif not fsizes_classify:
					is_classify = False
					write_log("debug sum_classify[null]", "Не получилось класифицировать размеры файлов для текущих задач [%s]" % str(datetime.now()))

			if filecmdbase_dict:

				fcb: dict = {}

				if is_classify:
					try:
						fcb = {k:v for k, v in filecmdbase_dict.items() if os.path.exists(k) and os.path.getsize(k) in fsizes_classify}
					except:
						fcb = {}

				if all((fcb, len(fcb) <= len(filecmdbase_dict))): # update_jobs_by_classify
					filecmdbase_dict = fcb

				with open(filecmd_base, "w", encoding="utf-8") as fbf:
					json.dump(filecmdbase_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False) #2-save_current_jobs(new)

			filecmdbase_list = [*filecmdbase_dict] # skip_sort(defaul)
			filecmdbase_pos_dict = {jfile.strip(): str(i+1).strip() for i, jfile in enumerate(filecmdbase_list)} # start_at_1

			prc_pos_set = set()
			prc_pos: int = 0

			# new_script
			for k, v in filecmdbase_dict.items():

				if not filecmdbase_dict:  # no_data
					break

				'''
				write_log("debug classify_files[skip]", "Файл %s был пропущен т.к. он не классифицирован [%s]" % (k, str(datetime.now()))) # logging_if_not_classify
				MyNotify(txt="debug classify_files[skip] \"Файл %s был пропущен т.к. он не классифицирован [%s]\"" % (full_to_short(k), str(datetime.now())) , icon=icons["skip"])

				write_log("debug classify_files[ok]", "Файл %s классифицирован [%s]" % (k, str(datetime.now()))) # logging_if_classify
				MyNotify(txt="debug classify_files[ok] \"Файл %s классифицирован [%s]\"" % (full_to_short(k), str(datetime.now())) , icon=icons["work"])

				write_log("debug classify_files[null]", "Нет классификаций для текущих задач [%s]" % str(datetime.now())) # logging_if_classify
				MyNotify(txt="debug classify_files[null] \"Нет классификаций для текущих задач [%s]\"" % str(datetime.now()) , icon=icons["work"])
				'''

				lastfile.append(v.split(" ")[-1]) # save_to_xml_for_backup(clear_last) # @last.xml

				asyncio.run(save_job_to_xml(src=k, dst=v.split(" ")[-1])) # save_job_for_check(in_run/debug)

				ctme = datetime.now()

				asyncio.run(shutdown_if_time()) # every_check_time_by_job_run

				# if disk_usage("c:\\").free // (1024 ** 2) <= 500:  # if_fspace_less_500mb_then_stop(local)
					# break

				cnt += 1

				try:
					fp, fn = split_filename(k)
				except:
					fn = k.split("\\")[-1].strip() # fp

				try:
					fname = fn
				except:
					fname = ""

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
					if disk_space_limit <= 0: # if_less_zero
						print(dsize, fsizes, disk_space_limit, k) # is_color
						write_log("debug dspace[mp4][stop]", ";".join([str(dsize), str(fsizes), str(disk_space_limit), str(datetime.now())]))
						break

					# "debug dspace[mp4][limit]": "139/604/512/768;18/980/154/701;8/589/934/592;2023-04-03 11:03:23.116395",
					if all((dsize, fsizes, (disk_space_limit // (1024**3)) < 16, (disk_space_limit // (1024**3)) > 0)): # if_less_limit_job(16Gb)
						print(dsize, fsizes, disk_space_limit, k) # is_color
						write_log("debug dspace[mp4][limit]", ";".join([str(dsize), str(fsizes), str(disk_space_limit), str(datetime.now())]))
						break

				# if all((fname in skip_file, fname, skip_file)) or all((jobs_dict_index, jobs_dict_index[fname] > 1)):  # fname_count_filter(list/dict)
				# continue

				if not os.path.exists(k):
					continue

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

				# try_find_max_time_from_jobs # save_after_every_job

				dt = datetime.now()

				# before_job_start
				if not dt.hour in hours_set:  # and (all((len(hours_set) != max_hour, max_hour >= 2)) or not max_hour):  # add_unique_hour
					hours_set.add(dt.hour)  # {1,2,3,4} # set(no_dict)

				speed_file: float = 0
				time_file: float = 0
				data_file: float = 0

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

					# Вычислите скорость передачи, разделив объем данных на время передачи # скорость передачи(Speed)
					'''
					Например, файл размером 25 МБ передается за 2 минуты.
					Сначала преобразуйте 2 минуты в секунды: 2 х 60 = 120 с. Таким образом, S = 25 МБ ÷ 120 с = 0,208.
					Следовательно, скорость передачи равна 0,208 МБ/с.
					Чтобы конвертировать это значение в килобайты, умножьте 0,208 на 1024: 0,208 x 1024 = 212,9.
					Итак, скорость передачи также равна 212,9 КБ/с.
					'''
					try:
						speed_file = fsize / abs(dt - date2).seconds # S = A / T # скорость передачи # default(one_file)
						speed_list = [(speed_file // (1024**i)) for i in range(1, 4) if (speed_file // (1024**i)) > 0]
					except BaseException as e:
						speed_file = 0
						write_log("debug speed_file[error]", "%s [%s]" % (k, str(e)))
					else:
						if speed_list:
							speed_size = "%0.3f Mb/s [%d]" % (speed_list[-1], speed_file) # is_1024(is_float) # is_debug(in_list)
							write_log("debug speed_file", "%s, скорость передачи: %s" % (k, speed_size)) # speed_size -> str(speed_list[-1])
						elif not speed_list:
							speed_size = "%0.3f Mb/s" % speed_file # is_1024(is_float) # is_debug(default)
							write_log("debug speed_file[nolist]", "%s, скорость передачи: %s" % (k, speed_size)) # speed_size -> str(speed_list[-1])

					# 'debug speed_file: d:\\multimedia\\video\\serials_conv\\Hudson_and_Rex\\Hudson_and_Rex_03s01e.mp4, скорость передачи: 32251694.750 30 Mb/s

					time_list: list = []
					time_list2: list = [] # is_debug_time
					time_size: str = ""

					# Вычислите время передачи, разделив объем данных на скорости передачи # время_передачи(Time)
					'''
					Например, файл размером 134 ГБ был передан со скоростью 7 МБ/с.
					Сначала преобразуйте ГБ в МБ, чтобы унифицировать единицы измерения: 134 х 1024 = 137217 МБ.
					Итак, 137217 МБ были переданы со скоростью 7 МБ/с.
					Чтобы найти время передачи (T), разделите 137217 на 7 и получите 19602 секунд.
					Чтобы преобразовать секунды в часы, разделите 19602 на 3600 и получите 5,445 ч.
					Другими словами, чтобы передать 134 ГБ данных со скоростью 7 МБ/с, потребовалось 5,445 часа.
					'''
					try:
						time_file = fsize / speed_file # T = A / S # время передачи # default(one_file)
						# time_list = [time_file // i for i in range(60, 3660) if all((time_file // i > 0, i % 60 == 0))]
						time_list = [time_file % 3600, (time_file // 60) % 60, time_file % 60] # is_hh # is_mm # is_ss
						time_list2 =[time_file % 60, time_file // 60 ]
					except BaseException as e:
						time_file = 0
						write_log("debug time_file[error]", "%s [%s]" % (k, str(e)))
					else:
						if any((time_list, time_list2)):
							time_size = "%s %s [%d]" % (str(time_list), str(time_list2), time_file) # from_list's
							write_log("debug time_file", "%s, время передачи: %s" % (k, time_size))
						elif not time_list:
							time_size = "%0.3f мин" % time_file # #%0.3f # from_value
							write_log("debug time_file[nolist]", "%s, время передачи: %s" % (k, time_size))

					# 'debug time_file: d:\\multimedia\\video\\serials_conv\\Firefly_Lane\\Firefly_Lane_02s01e.mp4, время передачи: 66.000 1 сек

					data_list: list = []
					data_size: str = ""

					# Вычислите объем данных, умножив время передачи на скорость передачи # объём данных(Data)
					'''
					Например, нужно определить, сколько данных было передано за 1,5 часа со скоростью 200 бит/с.
					Сначала преобразуйте часы в секунды: 1,5 х 3600 = 5400 с. Итак, А = 5400 с х 200 бит/с = 1080000 бит/с.
					Чтобы преобразовать это значение в байты, разделите на 8: 1080000 ÷ 8 = 135000.
					Чтобы конвертировать значение в килобайты, разделите на 1024: 135000 ÷ 1024 = 131,84.
					Таким образом, 131,84 КБ данных было передано за 1,5 часа со скоростью 200 бит/с.
					'''
					try:
						data_file = time_file * speed_file # A = T * S # сколько данных было передано # for_all
						data_list = [(data_file // (1024**i)) for i in range(1, 4) if (data_file // (1024**i)) > 0]
					except BaseException as e:
						data_file = 0
						write_log("debug data_file[error]", "%s [%s]" % (k, str(e)))
					else:
						if data_list:
							data_size = "%0.3f Mb [%d]" % (data_list[-1], data_file) # is_1024(is_float) # is_debug(in_list)
							write_log("debug data_file", "%s, сколько данных было передано: %0.3f %s" % (k, round(data_file, 3), data_size)) # data_size -> str(data_list[-1])
						elif not data_list:
							data_size = "%0.3f Mb" % data_file # is_1024(is_float) # is_debug(default)
							write_log("debug data_file[nolist]", "%s, сколько данных было передано: %0.3f %s" % (k, round(data_file, 3), data_size)) # data_size -> str(data_list[-1])

					std_dict[k.strip()] = str({"speed": [round(speed_file,3), speed_size], "time": [round(time_file,3), time_size], "data": [round(data_file,3), data_size]}) # speed/time/data

					# 'debug data_file: d:\\multimedia\\video\\serials_conv\\Hudson_and_Rex\\Hudson_and_Rex_03s02e.mp4, сколько данных было передано: 129830249.000 123 Mb
					# """

				if std_dict:
					with open(std_base, "w", encoding="utf-8") as sbf:
						json.dump(std_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

				# if all((len(hours_set) == max_hour, max_hour >= 2)):  # 2_hours_or_more_to_stop(default) # wait_after_2_hours
				# break

				print(Style.BRIGHT + Fore.CYAN + "\nФайл %s" % k, Style.BRIGHT + Fore.WHITE + "начал обрабатываться")
				write_log("debug run[job][start]", "Файл %s начал обрабатываться [%s]" % (k, str(datetime.now())))

				# filecmd_base # if_big_cinema_4_hours # if_tv_series_3_hours
				# set_or_update(trends)_by_any_video # hidden(debug)
				try:
					with open(trends_base, encoding="utf-8") as ftf:
						trends_dict = json.load(ftf)
				except: # IOError
					trends_dict = {}

					with open(trends_base, "w", encoding="utf-8") as ftf:
						json.dump(trends_dict, ftf, ensure_ascii=False, indent=2, sort_keys=False)

				else:
					if len(fname.strip()) > 0:
						trends_dict[crop_filename_regex.sub("", fname).strip()] = str(datetime.now())

				with open(trends_base, "w", encoding="utf-8") as ftf:
					json.dump(trends_dict, ftf, ensure_ascii=False, indent=2, sort_keys=False)  # update_trends(short)_if_mp4

				# p: int = -999

				date2 = datetime.now()

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)

				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				if hour:
					write_log("debug hour[count][8]", "%d" % (hour[0] // 60)) # is_index #8
					hour = hour[0] // 60

				# '''
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[8]" # 8
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[8]")
					hour = 2 # limit_hour
					# raise err
				# '''

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # mm[0] // 60 >= 2:  # stop_if_more_2hour
					write_log("debug stop_job[filecmdbase_dict]", "Stop: at %s [%d]" % (k, cnt))

					break # stop_if_before_run

				if all((k, k in [*filecmdbase_pos_dict])):
					prc_pos = int((cnt / len(filecmdbase_pos_dict))*100)

					if all((not int(prc_pos) in prc_pos_set, prc_pos <= 100)):
						prc_pos_set.add(int(prc_pos))

					print(Style.BRIGHT + Fore.BLUE + "Run:",
					Style.BRIGHT + Fore.WHITE + "%s" % v,
					Style.BRIGHT + Fore.YELLOW + "[%d]" % prc_pos, end="\n") # show_all_percent_process # filecmdbase_pos_dict[k] -> prc_pos
					write_log("debug run[mp4][pos]", "%s" % v)

				# @m3u8 # generate_m3u8_by_job(stay_m3u8) # ts_segments

				try:
					is_run, is_cmd, is_comment = asyncio.run(mp4_to_m3u8(filename=k, is_run=False, is_stay=True))
				except:
					is_run, is_cmd, is_comment = False, "", ""

				if any((is_run, is_cmd, is_comment)):
					generate_m3u8_by_job = (is_run, is_cmd, is_comment)
					write_log("debug mp4_to_m3u8", "%s [%s] [%s]" % (str(generate_m3u8_by_job), k, str(datetime.now())))

				# @mp4

				p = os.system(v) # continue # continue_if_debug / run # mp4

				# find_max_job_time
				if p == 0:  # calc_time_if_run_ok
					# clear(null)_xml_if_ready_ok # is_need_or_not

					print(Style.BRIGHT + Fore.GREEN + "Файл %s" % k,
						  Style.BRIGHT + Fore.WHITE + "успешно обработался")  # k -> dfile

					write_log("debug run[job][complete]",
							  "Файл %s успешно обработался [%s]" % (k, str(datetime.now())))  # k -> dfile

					if all((k, not k in ready_set)):
						ready_set.add(k)

				elif p != 0:  # skip_if_run_bad
					print(Style.BRIGHT + Fore.RED + "Ошибка обработки файла %s будет пропушен" % k)

					write_log("debug run[job][error]",
							  "Ошибка обработки файла %s будет пропушен [%s]" % (k, str(datetime.now())))
					continue

				# compare_filesizes
				try:
					glf = os.path.getsize(lastfile[-1])
				except:
					glf = 0
				else:
					glf //= (1024**2)

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

				hour = divmod(int(abs(date1 - date2).total_seconds()), 60)  # 60(min) -> 3600(hours)


				try:
					_, hh, mm, _ = MT.seconds_to_hms(date1, date2) # days -> _ # ss -> _
				except:
					mm = abs(date1 - date2).seconds
					hh = mm // 3600
					mm //= 60
					# mm %= 60 # sec

				if hour:
					write_log("debug hour[count][9]", "%d" % (hour[0] // 60)) # is_index #9
					hour = hour[0] // 60

				# '''
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[9]" # 9
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[9]")
					hour = 2 # limit_hour
					# raise err
				# '''

				# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
				if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # prc >= 75 # stop_by_progress(1/3) ~ 75% (debug)
					write_log("debug stop_job[filecmdbase_dict]", "Stop: at %s [%d]" % (k, cnt))

					try:
						fdate, status = asyncio.run(datetime_from_file(lastfile[-1]))
					except:
						fdate, status = datetime.now(), False
					else:
						if any((fdate.hour < mytime["sleeptime"][1], all((hh >= h, mm >= m)))):
							if os.path.exists(lastfile[-1]):
								os.remove(lastfile[-1])
								lastfile.remove(lastfile[-1])

					break # stop_after_run

			del MT


			async def clear_m3u8(): # clear_old_m3u8_playlists
				# current_files(dict)
				try:
					with open(vr_files, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except: # IOError
					ff_last = {}

					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(ff_last, vff, ensure_ascii=False, indent=2, sort_keys=True)

				try:
					segments_list = os.listdir(path_for_segments)
				except:
					segments_list = []

				# combine_jobs_filter_by_segments(m3u8)_filenames
				try:
					ff_last_no_file = {"".join([path_for_segments, sl]).strip():v for k, v in ff_last.items() for sl in segments_list if all((k, sl, k.split("\\")[-1].split(".")[0] == "".join([path_for_segments, sl]).split("\\")[-1].split(".")[0])) and not os.path.exists(k)}
				except:
					ff_last_no_file = {}

				if ff_last_no_file: # what_not_exists
					for k, _ in ff_last_no_file.items():

						if not os.path.exists(k):
							print(Style.BRIGHT + Fore.CYAN + "Файл %s не найден и его надо удалить из базы" % k)
							write_log("debug ff_last[nofile]", "Файл %s не найден и его надо удалить из базы" % k)
							# os.remove(k) # need_delete_m3u8_by_filename

					sleep(0.50)

			async def update_combine_jobs(): # delete_not_exists_job
				try:
					with open(vr_files, encoding="utf-8") as vff:
						ff_last = json.load(vff)
				except: # IOError
					ff_last = {}

					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(ff_last, vff, ensure_ascii=False, indent=2, sort_keys=True)

				first_len: int = 0
				first_len = len(ff_last) # without_update_length # pass_1_of_2

				if ff_last:
					ff_last = {k:v for k, v in ff_last.items() if os.path.exists(k)}

				second_len: int = 0
				second_len = len(ff_last) # is_update(equal)_length # pass_2_of_2

				if all((second_len, second_len <= first_len)):
					with open(vr_files, "w", encoding="utf-8") as vff:
						json.dump(ff_last, vff, ensure_ascii=False, indent=2, sort_keys=True)

			asyncio.run(clear_m3u8())
			asyncio.run(update_combine_jobs())

			# check_jobs_for_forward_update(project(src) -> original(dst)) # debug(xml)

			MM = MyMeta() #10

			ok_count: int = 0
			diff_count: int = 0
			err_count: int = 0

			for k, v in filecmdbase_dict.items(): # fcd.json -> cfcd.json
				asyncio.run(save_job_to_xml(src=k, dst=v.split(" ")[-1])) # save_job_for_check(after_run/debug)

				is_ok: bool = False
				is_bad: bool = False

				try:
					check_job = asyncio.run(load_job_from_xml()) # check_job_for_check(after_run)
				except:
					check_job = []
				else:
					try:
						for cj in check_job:

							if not check_job: # no_data
								break

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
								is_clean = all((gl2 in range(gl1, gl1 - 5, -1), gl2, gl1))
							except:
								is_clean = False

							if all((is_clean == True, cj["src"].split("\\")[-1] == cj["dst"].split("\\")[-1])): # try_save # int(cj["leng"]) == MM.get_length(cj["dst"])
								print(Style.BRIGHT + Fore.GREEN + "Задача %s выполнена успешно, её можно сохранить" % full_to_short(cj["dst"]))
								write_log("debug check_job[equal]", "Задача %s выполнена успешно, её можно сохранить" % cj["dst"])

								is_ok, is_bad = True, False

								ok_count += 1

								if os.path.exists(cj["src"]) and os.path.exists(cj["dst"]):
									try:
										fsize: int = os.path.getsize(cj["dst"])
										dsize: int = disk_usage(cj["src"][0] + ":\\").free
									except:
										fsize: int = 0
										dsize: int = 0
									else:
										try:
											move(cj["dst"], cj["src"])
										except:
											if os.path.exists(cj["dst"]): # status_error_from_xml # is_logging(is_red)
												os.remove(cj["dst"]) # delete_if_cant_move
												print(Style.BRIGHT + Fore.RED + "Файл %s удален, т.к. не получилось перенести готовый файл" % full_to_short(cj["dst"]))
												write_log("debug dst[save][error]", "Файл %s удален, т.к. не получилось перенести готовый файл" % cj["dst"])
										else:
											print(Style.BRIGHT + Fore.GREEN + "%s" % ">=->".join([cj["dst"], cj["src"]]))
											write_log("debug dst[save][xml]", "%s" % ">=->".join([cj["dst"], cj["src"]])) # status_save_ok_from_xml # is_logging(is_green)

							elif all((is_clean == False, cj["src"].split("\\")[-1] == cj["dst"].split("\\")[-1])): # skip_to_update(check_length) # int(cj["leng"]) != MM.get_length(cj["dst"])
								print(Style.BRIGHT + Fore.YELLOW + "Задача %s выполнена с разницей, её нельзя сохранять" % full_to_short(cj["dst"]))
								write_log("debug check_job[diff]", "Задача %s выполнена с разницей, её нельзя сохранять" % cj["dst"])

								is_ok, is_bad = False, True

								diff_count += 1

								if os.path.exists(cj["dst"]):
									try:
										os.remove(cj["dst"])
									except:
										print(Style.BRIGHT + Fore.RED + "Файл %s не удален" % full_to_short(cj["dst"]))
										write_log("debug dst[delete][error]", "Файл %s не удален" % cj["dst"]) # status_error_from_xml # is_logging(is_red)
									else:
										print(Style.BRIGHT + Fore.GREEN + "Файл %s успешно с разным временем удален" % full_to_short(cj["dst"]))
										write_log("debug dst[delete][xml]", "Файл %s успешно с разным временем удален" % cj["dst"]) # status_delete_from_xml # is_logging(is_green)
					except BaseException as e:
						write_log("debug check_job[error]", "%s" % str(e), is_error=True)

						err_count += 1

						continue # if_none_next_record(eof)
					else:
						answer_status = "Данные совпадают" if is_ok else "Данные не совпадают"
						write_log("debug check_job[ok]", "%s" % answer_status)

			del MM

			sum_count: int = 0

			try:
				sum_count = ok_count + diff_count + err_count
			except:
				sum_count = 0

			if all((sum_count, sum_count < len(filecmdbase_dict))):
				print(Style.BRIGHT + Fore.YELLOW + "Возможно есть пропущенные задачи!!!")
				write_log("debug check_job[skiped]", "Возможно есть пропущенные задачи!!!")
			elif all((sum_count, sum_count == len(filecmdbase_dict))):
				print(Style.BRIGHT + Fore.GREEN + "Все задачи обработаны, даже если есть ошибки")
				write_log("debug check_job[combine]", "Все задачи обработаны, даже если есть ошибки")
			elif not sum_count:
				print(Style.BRIGHT + Fore.WHITE + "Возможно нет никаких задач или ошибка счётчика")
				write_log("debug check_job[nojobs]", "Возможно нет никаких задач или ошибка счётчика")

			# xml(job(src=k/len=length(k)/dst=v.split(" ")[-1])) # load_job_from_xml(mp4)

			if max_hour < len(hours_set):
				max_hour = len(hours_set)  # update_hours

			with open(files_base["hours"], "w", encoding="utf-8") as fbhf:
				fbhf.write("%d\n" % max_hour)

			# print()

			open(files_base["backup"], "w", encoding="utf-8").close()  # clean_backup_if_some_jobs_done

			# ip_and_macs_after_every_run_complete

			dt1 = datetime.now()

			if any((dt1.hour > mytime["sleeptime"][1], dt1.hour <= 21)): # is_time_ranges(?am-9pm)
				print("Сбор дполнительной информации об текущих устройствах... Ждите...")

				asyncio.run(ip_config()) # asyncio.run(ipconfig_to_base())

				if isinstance(lanmacs, dict):
					with open("".join([script_path, "\\lanmacs.json"]), "w", encoding="utf-8") as ljf:
						json.dump(lanmacs, ljf, ensure_ascii=False, indent=2, sort_keys=True)

				dt2 = datetime.now() # is_debug(time)

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
					# if any((hh, mm, ss)): # limit_scan_time
					assert any((hh, mm, ss)), "Ошибка значения единицы времени hh/mm/ss" # is_assert(debug)
				except AssertionError as err:
					full_time = None
					logging.warning("Ошибка значения единицы времени %d/%d/%d" % (hh, mm, ss))
					raise err
				else:
					full_time = "{hh}:{mm}:{ss}" % (hh, mm, ss)

				if full_time != None:
					print(f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}] [{full_time}]") # is_color
					write_log("debug get_hardware[lan][time]", f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}] [{full_time}]")
				elif full_time == None:
					print(f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}]") # is_color
					write_log("debug get_hardware[lan]", f"Сбор дполнительной информации об текущих устройствах... Готово!!! Найдено [{len(lanmacs)}]")

	if not jcount:  # no_jobs_but_maybe_combine_jobs_from_base

		# clear_when_null_jobs(is_update)

		print("No data for video template or resolution")
		write_log("debug nofiles", "No data for video template or resolution")

		# print()

		dt = datetime.now()

		if mytime["jobtime"][0] <= dt.hour <= mytime["jobtime"][1]: # check_and_filter_by_job_time # another_time_no_clean_backup
			open(files_base["backup"], "w", encoding="utf-8").close()

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

				if hour > 0:
					write_log("debug hour[count][10]", "%d" % (hour[0] // 60)) # is_index #10
					hour = hour[0] // 60

				# """
				try:
					assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[10]" # 10
				except AssertionError: # as err:
					logging.warning("Меньше установленого лимита по времени hour[10]")
					hour = 2 # limit_hour
					# raise err
				# """

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
								json.dump(fb_dict, fbf, ensure_ascii=False, indent=2, sort_keys=True)
						# else:
							# if fb_dict:
								# fb_dict = {k:v for k, v in fb_dict.items() if any(("scale" in v.lower(), "profile" in v.lower(), "level" in v.lower()))} # need_optimize(scale/profile/level) # skip_other

						year_regex = re.compile(r"[\d+]{4}")
						year_filter = []

						def filebase_to_year(fb_dict=fb_dict):
							for k, v in fb_dict.items():
								if year_regex.findall(k):
									yield k.strip()

						# year_filter = [k.strip() for k, v in fb_dict.items() if year_regex.findall(k)] # any(("scale" in v.lower(), "profile" in v.lower(), "level" in v.lower())) # old(no_gen)
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

						if hour > 0:
							write_log("debug hour[count][11]", "%d" % (hour[0] // 60)) # is_index #11
							hour = hour[0] // 60

						# """
						try:
							assert isinstance(hour, int) and hour >= 2, "Меньше установленого лимита по времени hour[11]" # 11
						except AssertionError: # as err:
							logging.warning("Меньше установленого лимита по времени hour[11]")
							hour = 2 # limit_hour
							# raise err
						# """

						# time_is_limit_1hour_50min # all((h >= 0, m, hh >= h, mm >= m)) # all((hh > hour, mm >= m))
						if all((hh > hour, hour)) or date2.hour < mytime["sleeptime"][1]: # stop_if_more_30min # mm[0] // 60 >= 2:  # stop_if_more_2hour
							write_log("debug stop_job[another_list]", "Stop: at %s [%d]" % (any_file, cnt))

							break # stop_if_before_run

						# set_or_update(trends)_by_any_video # hidden(debug)
						try:
							with open(trends_base, encoding="utf-8") as ftf:
								trends_dict = json.load(ftf)

						except:
							trends_dict = {}

							with open(trends_base, "w", encoding="utf-8") as ftf:
								json.dump(trends_dict, ftf, ensure_ascii=False, indent=2, sort_keys=False)

						finally:
							if len(mp4_file.strip()) > 0:
								trends_dict[crop_filename_regex.sub("", mp4_file.split("\\")[-1]).strip()] = str(datetime.now())

							try:
								fdates = [v.strip() for k, v in trends_dict.items()]
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

							with open(trends_base, "w", encoding="utf-8") as ftf:

								json.dump(trends_dict, ftf, ensure_ascii=False, indent=2, sort_keys=False) # update_trends(short)_if_not_mp4

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
					MySt = MyString() # MyString("Запускаю:", "[7 из 7]")

					try:
						print(Style.BRIGHT + Fore.CYAN + MySt.last2str(maintxt="Запускаю:", endtxt="[7 из 7]", count=len_proc, kw="задач"))
						# print(Style.BRIGHT + Fore.WHITE + MySt.last2str(maintxt=MySt.maintext, endtxt=MySt.endtext, count=len_proc, kw="задач"))
					except:
						print(Style.BRIGHT + Fore.YELLOW + "Обновляю или удаляю %d файлы(а,ов) [7 из 7]" % len_proc) # old(is_except)
					else:
						write_log("debug run[task7]", MySt.last2str(maintxt="Запускаю:", endtxt="[7 из 7]", count=len_proc, kw="задач"))

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
					# json.dump({}, cbf, ensure_ascii=False, indent=2, sort_keys=False)

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
			json.dump(somebase_dict, sbf, ensure_ascii=False, indent=2, sort_keys=True)

	# trends_base_load(hidden) # {"short":"%date%"}
	try:
		with open(trends_base, encoding="utf-8") as tbf:  # dict(some_trends_for_run) # debug/test
			trends_dict = json.load(tbf)
	except:
		trends_dict = {}
	else:
		trends_temp = {k: str(datetime.now()) for k, v in trends_dict.items() for k2, v2 in somebase_dict.items() if
							all((k, k2, k.strip() == crop_filename_regex.sub("", k2.split("\\")[-1])))}

		if trends_temp:
			trends_dict.update(trends_temp)

		try:
			fdates = [v.strip() for k, v in trends_dict.items()]
		except:
			fdates = []
		else:
			fdates.sort(reverse=False)

		try:
			fdates_dict = {k: v for fd in fdates for k, v in trends_dict.items() if
								fd.strip() == v.strip()}
		except:
			fdates_dict = {}
		else:
			if all((fdates_dict, len(fdates_dict) <= len(trends_dict))): # trends_dict
				trends_dict = fdates_dict  # update_wothout_sort

		if len(trends_dict) >= 0:  # save_if_null_or_some_data

			today_check = str(datetime.today()).split(" ")[0] # only_current_date

			trends_first = len(trends_dict) # default
			trends_dict = {k:v for k, v in trends_dict.items() if today_check in v} # stay_only_today
			trends_second = len(trends_dict) # equal/diff

			if all((trends_second, trends_second <= trends_first)):
				with open(trends_base, "w", encoding="utf-8") as tbf:  # dict(some_trends_for_run) # update_or_cleaned
					json.dump(trends_dict, tbf, ensure_ascii=False, indent=2, sort_keys=True)

	# jobs_base_load(hidden) # {"fullname":"command_line"}
	try:
		with open(filecmd_base, encoding="utf-8") as fbf:
			fb_dict = json.load(fbf)
	except: # IOError
		fb_dict = {}

		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump(fb_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False)

	# last_jobs_by_count # pass_1_of_2

	first_len = second_len = 0

	# filter_current_jobs_(in_meta/no_in_meta/exists_only)
	try:
		first_len = len(fb_dict)
		fb_dict = {k: v for k, v in fb_dict.items() if os.path.exists(k) and any((k.strip() in [*somebase_dict], not [*somebase_dict]))}
	except:
		fb_dict = {k: v for k, v in fb_dict.items() if os.path.exists(k)}
	finally:
		second_len = len(fb_dict) # equal/diff

	if all((second_len, second_len < first_len)):
		print(Style.BRIGHT + Fore.CYAN + "Количество заданий было %d стало %d [%s]" % (first_len, second_len, str(datetime.now()))) # is_color
		write_log("debug filecmdbase_dict[changed]", "Количество заданий было %d стало %d [%s]" % (first_len, second_len, str(datetime.now())))
	elif all((second_len, second_len == first_len)):
		print(Style.BRIGHT + Fore.WHITE + "Количество заданий не изменилось [%s]" % str(datetime.now()))  # is_color
		write_log("debug filecmdbase_dict[not_changed]", "Количество заданий не изменилось [%s]" % str(datetime.now()))
	elif all((not first_len, first_len != second_len)):
		print(Style.BRIGHT + Fore.YELLOW + "На данный момент все задания выполнены или отсуствуют [%s]" % str(datetime.now()))  # is_color
		write_log("debug filecmdbase_dict[no_jobs]", "На данный момент все задания выполнены или отсуствуют [%s]" % str(datetime.now()))

	# last_jobs_by_short # pass_2_of_2

	fcl: list = []

	try:
		# fcl: list = list(set([crop_filename_regex.sub("", fd.split("\\")[-1]).strip() for fd in fb_dict if fd]))
		fcl: list = list(set([crop_filename_regex.sub("", fn).strip() for fd in fb_dict for fp, fn in split_filename(fd) if ((fn, fd, fn == fd.split("\\")[-1]))]))
	except:
		fcl: list = []
	finally:
		fcl_str = "%s [%s]" % (";".join(list(set(fcl))),
			str(datetime.now())) if fcl else "На данный момент все задания выполнены или отсуствуют [%s]" % str(
				datetime.now())  # debug/test

		print(Style.BRIGHT + Fore.YELLOW + "%s" % fcl_str) # list_jobs
		write_log("debug fcl[short_jobs]", "%s" % fcl_str)  # last_jobs_after_filter(without_save)

	if all((second_len, second_len <= first_len)): # if_stay_some(>0)_or_all_ready(0)
		with open(filecmd_base, "w", encoding="utf-8") as fbf:
			json.dump(fb_dict, fbf, ensure_ascii=False, indent=2, sort_keys=False)  # stay_files_only_in_meta

	# if_need_clean_"error"_from_log
	write_log("debug end", f"{str(datetime.now())}")
	logging.info(f"debug end {str(datetime.now())}")
	MyNotify(txt=f"Программа завершена {str(datetime.now())}", icon=icons["finish"])
	# sound_notify(text=f"Программа завершена {str(datetime.now())}") # debug/test

	# check_time_after_run(finish)
	ctme = datetime.now()

	asyncio.run(shutdown_if_time())
