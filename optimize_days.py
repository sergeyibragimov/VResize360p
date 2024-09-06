# -*- coding: utf-8 -*-

# --- semi_automatic(debug) ---

# Полуавтоматическое форматрирование файлов с проектами по периоду(datetime)

# from os import getcwd # cpu_count  # текущая папка # cpu_count
# from psutil import cpu_count  # viirtual_memory # pip install --user psutil
# from scprle import *
# from video_trimmer2 import *
# import gevent.monkey # pip install --user gevent # is_async(debug)
# import psutil
from datetime import datetime, timedelta  # дата и время
from shutil import (
	disk_usage,
)  # copy, move # файлы # usage(total=16388190208, used=16144154624, free=244035584)
from subprocess import (
	run,
)  # TimeoutExpired, check_output, Popen, call, PIPE, STDOUT # Работа с процессами # console shell=["True", "False"]
from time import time, sleep
import asyncio
import json  # JSON (словарь)
import logging  # журналирование и отладка
import os  # система
import re  # реуглярные выражения/regular expression # .*(\?|$)
import sys
import pyttsx3

# pip install --user bpython (interactive_color_terminal) # launch?
# pip install --user youtube-dl # youtube-dl --hls-prefer-native "http://host/folder/file.m3u8" # youtube-dl -o "%%(title)s.%%(resolution)s.%%(ext)s" --all-formats "https://v.redd.it/8f063bzbdx621/HLSPlaylist.m3u8"

# Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.
# Back, Cursor # Fore.color, Back.color # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE # pip install --user colorama
from colorama import Fore, Style, init

# python -m trace --trace optimize_days.py

# vosk (+Python/Subtitle Edit"Video") # video(audio)_to_text(is_subtitle)

__version__ = "0.1"
__author__ = "Sergey Ibragimov"

# ffmpeg -i blah.vtt blah.srt # manual_convert_subtitle

# debug_moules
# exit()

# mklink /h optimizedays.py optimize_days.py

"""
numbers = [1,2,3]
another_numbers = numbers[:]  # diff_lists(copy)
another_numbers.append(100)
print(another_numbers, numbers) # [1, 2, 3, 100] [1, 2, 3]
"""

"""
# equal_arguments_by_class
class User:
		def __init__(self, group):
			self.group = group

user = User(group="admin")

group_to_process_method = {
	"admin": process_admin_requests,
	"manager": process_manager_requests,
	"client": process_client_requests,
	"anon": process_anon_requests
}

group_to_process_method[user.group](user, request)
"""

# @share local web-service to internet
# python -m http.server
# ngrok http http://localhost:8000 # ngrok http --domain domain-name.ngrok-free.app http://localhost:8000 # https
# @github(localtunnel) # lt --port 8000 --subdomain domain-name # need_share_password # https
# serveo.net # ssh -R 80:localhost:8000 serveo.net # ssh -R wow-my-server:80:localhost:8000 serveo.net # github/google
# @github(expose) # ?

# def / async def # docstring

# abcdef, ghijkl, mnopqr, stuvxy, wz

init(autoreset=True)

# abspath_or_realpath
basedir = os.path.dirname(os.path.abspath(__file__)).lower()  # folder_where_run_script
script_path = os.path.dirname(os.path.realpath(__file__)).lower()  # is_system_older
current_folder = "".join([
	os.path.dirname(os.path.realpath(sys.argv[0])), "\\"
])

dletter = "".join(
	[basedir.split("\\")[0], "\\"]
)  # "".join(script_path[0:5]) if script_path else "".join(os.getcwd()[0:5])

# logging(start)
log_file = "%s\\debug.log" % script_path  # main_debug(logging

# --- path's ---
path_for_queue = r"d:\\downloads\\mytemp\\"
path_to_done = "%sdownloads\\list\\" % dletter  # "c:\\downloads\\" # ready_folder
path_for_folder1 = "".join([os.getcwd(), "\\"])  # "c:\\downloads\\new\\")

# list(json)_by_period
all_period_base = "%s\\all_period.lst" % script_path
all_period_json = "%s\\all_period.json" % script_path
calc_year_base = "%s\\calc_year.lst" % script_path
calc_year_json = "%s\\calc_year.json" % script_path
combine_base = "%s\\fcd.txt" % script_path
combine_base2 = "%s\\fcd_.txt" % script_path  # regex_filter((\(|_).*\..*)
days_ago_base = "%s\\days_ago.lst" % script_path
days_ago_json = "%s\\days_ago.json" % script_path
month_forward_base = "%s\\month_forward.lst" % script_path
month_forward_json = "%s\\month_forward.json" % script_path
period_base = "%s\\period.lst" % script_path  # combine_base
period_json = "%s\\period.json" % script_path

# '''
try:
	dsize = disk_usage(f"{dletter}").free  # "c:\\"
	# assert dsize, ""
except BaseException: # AssertionError
	logging.basicConfig(
		format="%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s",
		level=logging.INFO,
	)  # no_file
else: # finally -> else
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
# logging.basicConfig(
# format=u'%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s',
# level=logging.INFO
# ) # no_file # debug

list_files: list = []
list_files.append(all_period_base)
list_files.append(all_period_json)
list_files.append(calc_year_base)
list_files.append(calc_year_json)
list_files.append(combine_base)
list_files.append(combine_base2)
list_files.append(days_ago_base)
list_files.append(days_ago_json)
list_files.append(month_forward_base)
list_files.append(month_forward_json)
list_files.append(period_base)
list_files.append(period_json)

for cmd_files in filter(lambda x: os.path.exists(x), tuple(list_files)):
	os.remove(cmd_files)

try:
	assert os.path.exists(combine_base), ""
except AssertionError:
	logging.warning("@combine_base is null")
else:
	os.remove(combine_base)

try:
	assert os.path.exists(period_base), ""
except AssertionError:
	logging.warning("@period_base is null")
else:
	os.remove(period_base)

try:
	assert os.path.exists(period_json), ""
except AssertionError:
	logging.warning("@period_json is null")
else:
	os.remove(period_json)

try:
	assert os.path.exists(path_to_done), ""
except AssertionError:
	try:
		os.mkdir(path_to_done)
	except BaseException:
		exit()  # path_to_done = "c:\\downloads\\"

# @regex
# not_include_regex = re.compile(r"^.*(?!(copy).*)$", re.I) # debug
# (.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg|^.dmf|^.txt|^.srt|^.vtt|^.dmfr|^.aria2|^.crswap|^.filepart|^.crdownload)
video_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg))$",
	re.M,
)
space_regex = re.compile(
	r"[\s]{2,}"
)  # text = "hello  world" # space_regex.sub(" ", text)

file_regex = re.compile(r"([0-9]f_.*)", re.M)
seasyear = re.compile(
	r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))", re.M
)  # MatchCase # season_and_year(findall) # +additional(_[\d+]{2}p)
crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)", re.I)

start = time()

files_count = 0
folder_scan_full = []

mytime = {
	"jobtime": [9, 18, 5],
	"dinnertime": [12, 14],
	"sleeptime": [0, 8],
	"anytime": [True],
}  # sleep_time_less_hour # debug


class Timer(object):
	def __init__(self, total):
		self.start = datetime.now()  # datetime.datetime.now()
		self.total = total

	def remains(self, done):
		now = datetime.now()
		left = (self.total - done) * (now - self.start) / done
		sec = int(left.total_seconds())
		logging.info("@now/@left/@sec %s" % str((now, left, sec)))
		if sec < 60:
			return "{} seconds".format(sec)
		else:
			if int(sec / 60) < 60:
				return "{} minutes".format(int(sec / 60))
			elif int(sec / 60) >= 60:
				return "{} hours, {} minutes".format(
					int(sec / 60) // 60, int(sec / 60) % 60
				)  # debug_time


# @ oop
class Additional:
	def __init__(self):
		pass

	def full_to_short(self, filename) -> str:
		"""change_full_to_short(if_need_or_test_by_logging) # temporary_not_use"""
		self.filename = filename

		try:
			assert os.path.exists(
				self.filename
			), f"Файл отсутствует @full_to_short/{self.filename}"
		except AssertionError:  # as err:
			logging.warning("Файл отсутствует @full_to_short/%s" % self.filename)
			# raise err
			# return filename # skip_result
		except BaseException as e:
			full_to_short_err = (self.filename, str(e))
			logging.error("Файл отсутствует @full_to_short/%s [%s]" % full_to_short_err)

		# noinspection PyBroadException # c:\folder\...\filename
		try:
			short_filename = "".join(
				[self.filename[0], ":\\...\\", self.filename.split("\\")[-1]]
			).strip()  # is_ok
		except:
			short_filename = self.filename.strip()  # if_error_stay_old_filename

		return short_filename

	"""
	def parse_file(self, filename):  # full_name
		self.filename = filename

		try:
			filename = file_regex.findall(self.filename)[
				0
			]  # ; print(file_regex.findall(filename), end="\t\n") # short_filename
		except BaseException:
			return (0, [], [])

		# filename = "7f_Aktrisy.S01.E01.2023.WEB-DL.1080p.v1a1.30.03.23.mp4" # is_rus(2)
		# filename = "7f_30.Monedas.S01E06.Guerra.Santa.1080p.HBO.WEB-DL.Rus.Spa.Eng.BenderBEST.a1.09.01.21.mp4" # is_eng(11)

		try:
			assert filename.lower().startswith("http"), ""
		except AssertionError:
			return []

		try:
			short_filename = filename.split("\\")[-1]
		except:
			short_filename = ""

		# global parse_text

		parse_template = parse_text = parse_list = []

		parse_template.append(re.compile(r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([\d+]{1,2})\.sezon\.([\d+]{1,2})\.seriya"))
		parse_template.append(re.compile(r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([eE]{1}[\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([sS]{1}[\d+]{2})\.([eE]{1}[\d+]{2})")) # is_rus
		parse_template.append(re.compile(r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([sS]{1}\.[\d+]{1}).*([\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_(?:([A-Z][a-z\.\d+]{1,}|[A-Za-z\.\d+]{1,})).*([sS]{1}[\d+]{1}).*([\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,})-([\d+]{3}).*"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*(S[1,2])\.ep([\d+]{1,2})"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.Vypusk-([\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})x([\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})\.sezon\.([\d+]{2})\.seria"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})x([\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})")) # is_eng
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[\.]{1,}([\d+]{1})\.s-n\.([\d+]{1,2})\.s"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[sS]{1}([\d+]{2})[x]([\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,})\.([\d+]{2})\.seriya\.iz\.([\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_([\d+]{1,2})[\.]{1,}(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*[\d+]{4}"))
		parse_template.append(re.compile(r"^[0-9]f_([\d+]{2})-([A-Za-z\.\-\d+]{1,}).*([\d+]{1}[sS]{1})ezon"))
		parse_template.append(re.compile(r"^[0-9]f_([\d+]{2}).*[\.]{1,}([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_([\d+]{2})\-([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})"))
		parse_template.append(re.compile(r"^[0-9]f_(\[.*\]).*\.(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,}))\.([\d+]{1,2})\.\-\.([\d+]{1,2})"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.([\d+]{2})\.serija"))
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*\[([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})"))

		try:
			parse_list = list(
				set(
					[
						(tuple(pt.findall(short_filename)), pt)
						for pt in parse_template
						if pt.findall(short_filename)
					]
				)
			)  # try_unique
			assert parse_list, ""
		except AssertionError:
			parse_list = []
		else:
			print()

			for ps in parse_list:
				try:
					assert ps and parse_list, ""  # some_data(tuple) / some_list
				except AssertionError:
					logging.warning("@parse_list template not found for %s" % filename)
					continue
				except BaseException as e:
					parse_list_err = (str(e), filename)
					logging.error("@parse_list error: %s, current: %s" % parse_list_err)
					continue
				else:
					parse_text.append("%s" % str(ps))  # debug_for_join
					logging.info('@parse_text %s for "%s"' % (parse_text[-1], filename))

		return (len(parse_template), parse_list, parse_text)

	"""

	def __del__(self):
		print(
			Style.BRIGHT + Fore.WHITE + "%s удалён" % str(self.__class__.__name__)
		)  # del_class
		# logging.info("%s удалён" % str(self.__class__.__name__))


add = Additional()


# t = Timer(12987) # max_count_tasks # There are 12987 units in this task

# do some work

# sleep(1) # time.sleep(1)

# after some time passed, or after some units were processed
# eg.  37 units, calculate, and print the remaining time:
# print(t.remains(37)) # current_how_match # let the process continue and once in a while print the remining time.


def check_dict(
	dct: dict, item=["", None]
):  # dict(json) / find_key / find_value # docstring(sample)
	"""
	>>> a = {"a":1, "b":2, "c":3}
	>>> a.get(5, 4) # 4 # no_key
	>>> a.get("a", 4) # 1 # yes_key
	"""

	try:
		assert dct, ""
	except AssertionError:  # if_null
		return item[1]  # use_value(None -> no_value)
	else:
		try:
			return dct.get(
				item[0], item[1]
			)  # filter_by_key / use_value(None -> no_value)
		except BaseException:  # if_error
			return item[1]  # use_value(None -> no_value)


def clear_base_and_lists():  # docstring
	"""@clear_log_and_bases"""

	# pass

	# '''
	create_files = []

	# automatic(is_no_semiautomatic)
	create_files.extend(
		[
			period_base,
			days_ago_base,
			days_ago_json,
			month_forward_base,
			month_forward_json,
			calc_year_base,
			calc_year_json,
			all_period_json,
			all_period_base,
		]
	)  # clear_all_data # "log_file"

	try:
		for cf in filter(lambda x: os.path.exists(x), tuple(create_files)):
			os.remove(cf)
	except BaseException as err:
		logging.error("%s" % str(err))

	try:
		for cf in filter(lambda x: os.path.getsize(x), tuple(create_files)):
			open(cf, "w", encoding="utf-8").close()
	except BaseException as err:
		logging.error("%s" % str(err))
	# '''


# logging.basicConfig(level=logging.INFO)

# @logging
# with_encoding # utf-8 -> cp1251
# filename / lineno / name / levelname / message / asctime # save_logging_manuals


# @math


async def calc_number_of_day(
	is_default: bool = True,
	day: int = 0,
	month: int = 0,
	year: int = 0,
	sleep_if: str = "",
	find_c3: int = 0,
	find_c4: int = 0,
) -> tuple:  # 4 # docstring
	"""@calc_number_of_day"""

	if is_default:
		dt_calc = datetime.now()  # day / month / year

		dt_str = ".".join(map(str, (dt_calc.day, dt_calc.month, dt_calc.year)))
	elif not is_default:
		dt_str = ".".join(map(str, (day, month, year)))

	if all((sleep_if, dt_str == sleep_if, not is_default)):
		sleep(2)

	c1, c2, c3, c4 = 0, 0, 0, 0

	# 10.09.1994 # 33.6.31.4
	# 1.4.2023 # 12.3.32.5

	sm = []

	for ds in range(len(dt_str)):  # filter(lambda x: x, tuple(dt_str)):
		try:
			assert bool(dt_str[ds].isnumeric()), ""
		except AssertionError:
			continue
		else:
			sm.append(int(dt_str[ds]))
	else:  # is_no_break
		if len(sm) >= 0:
			is_day_calc = (
				"Число дня получено!" if sm else "Число дня неизвестно!"
			)  # is_no_lambda
			print(Style.BRIGHT + Fore.GREEN + "%s" % is_day_calc)  # day_calc

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
		print(";".join(map(str, (c1, c2, c3, c4, dt_str))), "from def")

	return (int(c1), int(c2), int(c3), int(c4), dt_str)


async def month_to_seasdays(month: int = 0, year: int = 0) -> tuple:  # 5
	try:
		assert (
			1 <= month <= 12
		), f"Неверный индекс месяца @month_to_seasdays/{month}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning(f"Неверный индекс месяца @month_to_seasdays/{month}")
		raise err
		return ("", 0)
	else:
		logging.info("@month индекс месяца: %d" % month)

	# is_calc_number_of_day

	seas, days = "", 0

	if month in [12, 1, 2]:
		if month == 12:
			days = 31
		elif month == 1:
			days = 31
		elif all((month == 2, year)):
			days = 29 if year % 4 == 0 else 28
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
	except BaseException:
		return ""
	else:
		return f"До нового года осталось {d.days} дней, {hh} час. {mm} мин. {ss} сек."
		# return last2str(maintxt="До нового года осталось", endtxt=f"{hh} час. {mm} мин. {ss} сек.", count=d.days, kw="ден")


async def date_to_week() -> dict:  # 2 # docstring(description)
	"""
	Creating an dictionary with the return
	value as keys and the day as the value
	This is used to retrieve the day of the
	week using the return value of the
	isoweekday() function
	"""

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
		except BaseException:
			mts = ("", 0)

		try:
			cnod = await calc_number_of_day(
				day=todays_date.day, month=todays_date.month, year=todays_date.year
			)
		except BaseException:
			cnod = (0, 0, 0, 0, str(todays_date))

		# Using the isoweekday() function to
		# retrieve the day of the given date
		day = todays_date.isoweekday()
		# print("The date", todays_date, "falls on", weekdays[day])

		try:
			fdth = await fromdaytohny()
		except BaseException:
			fdth = ""

	except BaseException:
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


logging.info(f"@start {str(datetime.now())}")

try:
	dtw = asyncio.run(date_to_week())
except BaseException as e:
	logging.error("Ошибка даты [%s]" % str(e))
	# write_log("debug dtw[error]", "Ошибка даты [%s]" % str(e), is_error=True)
else:
	d_w_s_n_d_str = (
		dtw["date"],
		dtw["weekday"],
		dtw["season(days)"],
		dtw["number_of_day"],
		dtw["days_to_ny"],
	)
	logging.info(
		"@dtw[ok] Today is: %s, weekday is: %s, season(days): %s, number_of_day: %s, days_to_ny: %s"
		% d_w_s_n_d_str
	)
	# write_log(
	# "debug dtw[ok]",
	# "Today is: %s, weekday is: %s, season(days): %s, number_of_day: %s, days_to_ny: %s" % d_w_s_n_d_str)

clear_base_and_lists()

logging.info("%s" % ";".join(map(str, (basedir, script_path))))

try:
	files_types = [
		0 if os.path.isfile(os.path.join(os.getcwd(), f)) else 1
		for f in os.listdir(os.getcwd())
	]
	assert files_types, ""
except AssertionError:
	logging.warning("@files_types no files or no folders")
else:
	if files_types.count(0) == 0:  # if_no_files_up_dir
		os.chdir("..")

	logging.info("@files_types found %d data" % len(files_types))

# 15632076800 # 3687570583552
# """
dspace_list = []
dspace_another_drive = 0.0

# dletter_and_dspace = {}

for dl in range(ord("c"), ord("z") + 1):
	du = "".join([str(chr(dl)), ":\\"])

	try:
		optimal_total = int(disk_usage("%s" % du).total) // (1024 ** 3) # 10% free for faster (hdd/ssd)
		optimal_free = int(optimal_total * 0.10)
		optimal_used = int(disk_usage("%s" % du).used) // (1024 ** 3)

		# assert bool(optimal_used > optimal_free), ""
	# except AssertionError:
		# logging.warning(f"@optimal_total/@optimal_free/@optimal_used less 10% space on drive {du}, size: {optimal_free}!")
	except BaseException as e:
		logging.error("@optimal_total/@optimal_free/@optimal_used error: %s" % str(e))
		continue
	else:
		# dletter_and_dspace[str(du)] = ";",join(map(str, (du, optimal_used, optimal_free, bool(optimal_used > optimal_free)))) # value_by_logic
		logging.info(f"@optimal_total/@optimal_free/@optimal_used optimal space on {du}, free: {optimal_free}, used: {optimal_used}")  # "optimal space on du='c:\\\\', free: optimal_free=9, used: optimal_used=46"

	# logging.info("@du %s" % ";".join(map(str, ("%s" % du, int(disk_usage(r"%s" % du).used))))
	print(";".join(map(str, ("%s" % du, int(disk_usage("%s" % du).used)))))

	dspace_list.append(int(disk_usage(r"%s" % du).used))

try:
	dspace_another_drive = (
		((sum(dspace_list) * 0.30) / (1024**3), "Gb")
		if (sum(dspace_list) * 0.30) / (1024**3) < 1000
		else ((sum(dspace_list) * 0.30) / (1024**4), "Tb")
	)
except BaseException as e:
	dspace_another_drive = (0, str(e))
	logging.error(
		"@dspace_another_drive не получилось получить размер резервного пространства [%s]"
		% str(dspace_another_drive)
	)
else:
	logging.info(
		"@dspace_another_drive на данный момент нужно %s" % str(dspace_another_drive)
	)  # print(dspace_another_drive)
# """

job_count = 0

test_folders = test_files = []


def unixtime_to_date(
	unixtime: float = 0.0,
) -> str:  # os.path.getmtime(file) # async # docstring(sample)
	"""# datetime.fromtimestamp(1707646971.451722).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # '2024-02-11 15:22:51.451'"""
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


def ms_to_time(ms: int = 0, mn: int = 60) -> int:
	try:
		h, m, s = ms // 3600, ms % 3600 // 60, ms % 3600 % 60
		h_m_s_str = (ms, str(h), str(m), str(s))
		assert all((h, m, s)), (
			"Первоначально %d, время %s:%s:%s" % h_m_s_str
		)  # is_assert_debug
	except AssertionError:  # as err:  # if_null
		logging.warning("Первоначально %d, время %s:%s:%s" % h_m_s_str)
		# raise err
	else:
		h_m_s_str = (str(h), str(m), str(s))
		logging.info("Подсчет времени %s:%s:%s" % h_m_s_str)

	h, m, s = map(int, (h, m, s))  # int(h), int(m), int(s)

	# ms_time = None

	try:
		ms_time = (lambda hh, mm, ss: (hh * 3600) + (mm * 60) + ss)(h, m, s)
		# hh:mm:ss # '{:02d} час. {:02d} мин. {:02d} сек.'.format(h, m, s) # hh mm ss
		# ms_time = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
	except:
		ms_time = 0  # ms_time = str(ms_time)

	return ms_time


def fspace(src: str = "", dst: str = "") -> bool:  # 11
	try:
		assert src and os.path.exists(
			src
		), f"Файл отсутствует @fspace/{src}"  # is_assert_debug # src
	except AssertionError:  # if_null
		logging.warning("Файл отсутствует @fspace/%s" % src)
		# raise err
		return False
	except BaseException as e:  # if_error
		fspace_err = (src, str(e))
		logging.error("Файл отсутствует @fspace/%s [%s]" % fspace_err)
		return False

	try:
		fsize, dsize = os.path.getsize(src), disk_usage(dst[0] + ":\\").free
	except BaseException as e:  # if_error
		fsize = dsize = 0
		fsize_dsize_err = (src, str(e))
		logging.error(
			"Нет размера файла или размера диска @fspace/%s [%s]" % fsize_dsize_err
		)

	fspace_status = False

	try:
		fspace_status = all(
			(fsize, dsize, int(fsize // (dsize / 100)) <= 100)
		)  # fspace(ok-True,bad-False)
	except:
		fspace_status = False  # fspace(error-False)
	finally:
		return fspace_status


def calcProcessTime(starttime, cur_iter, max_iter, filename):
	telapsed = time() - starttime  # diff_time
	testimated = (telapsed / cur_iter) * (max_iter)  # is in percent

	finishtime = starttime + testimated
	finishtime = datetime.fromtimestamp(finishtime).strftime("%H:%M:%S")  # in time

	lefttime = testimated - telapsed  # in seconds

	return (int(telapsed), int(lefttime), finishtime, filename)


def sec_to_time(sec: int = 0) -> str:
	if sec < 60:
		return "{} seconds".format(sec)
	else:
		if int(sec / 60) < 60:
			return "{} minutes".format(int(sec / 60))
		elif int(sec / 60) >= 60:
			return "{} hours, {} minutes".format(
				int(sec / 60) // 60, int(sec / 60) % 60
			)


def avg_calc(s, l):
	try:
		ag = lambda s, l: s // l
		assert l, ""
	except AssertionError:  # BaseException as e10
		ag = 0
		logging.warning("@ag divide by zero")
	except BaseException as e:
		ag = 0
		logging.error("@ag error: %s" % str(e))
	else:
		avg = ag(s, l)
		ag = avg if avg else 0
		logging.info("@ag" % ag)

	return ag


def calc_download_time(
	filename, fs: int = 0, sp: int = 10
):  # fs = real_fs // (1024*2), sp = (10/8)*1024
	"""
	>>> fs, sp = 865, 1280
	>>> fs / sp # 0.67578125
	>>> (fs * 1024) / sp # 692.0
	>>> ((fs * 1024) / sp) // 60 # 	11.0
	>>> ((fs * 1024) / sp) % 60 # 32.0
	"""
	try:
		fs = os.path.getsize(filename) // (1024**2)
	except:  # if_not_exists
		fs = 0

	try:
		sp = (sp / 8) * 1024
	except:  # value_error
		sp = 0

	if any((not fs, not sp)):
		return (filename, 0, 0)

	return (filename, (fs * 1024 / sp) // 60, (fs * 1024 / sp) % 60)  # mm:ss


async def older_or_newbie(days, filename):  # filename(folder)
	days_ago = datetime.now() - timedelta(days=days)
	filetime = datetime.fromtimestamp(os.path.getctime(filename))

	if filetime < days_ago:  # newbie
		logging.info(
			"@older_or_newbie Папка %s старше(newbie) %d дней" % (filename, days)
		)
		return True  # print("File is more than ag days old") # "Файл старше(newbie) чем двухдневной(ag) давности
	else:  # older
		logging.info(
			"@older_or_newbie Папка %s старее(older) %d дней" % (filename, days)
		)
		return False


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
		# write_log("debug soundnotify[error]",	"Не смог произнести текст! [%s]" % str(e),	is_error=True, )
	else:
		if text:
			print(Style.BRIGHT + Fore.GREEN + "Текст [%s] успешно произнесён" % text)
			# write_log("debug soundnotify[ok]", "Текст [%s] успешно произнесён" % text)


if __name__ == "__main__":

	dt = datetime.now()

	sm = ln = ag = cntfiles = sf = files_count = len_files = 0  # int
	all_period_dict = folders_filter = {}  # dict
	files = (
		files2
	) = (
		folders
	) = (
		new_folders
	) = old_folders = some_files_filter = period_files = []  # list # fsizes
	all_period_set = (
		some_folders
	) = some_subfolders = some_files = set()  # ("", "", 0) / folders / files # set

	with open(all_period_json, "w", encoding="utf-8") as apjf:
		json.dump(
			all_period_dict, apjf, ensure_ascii=False, indent=4, sort_keys=False
		)  # clear_periods

	seasyear_count = {}

	# @sorted_by_filter
	"""
	file_and_filter = ()
	faf = faf_sorted_tuple = []

	for f in os.listdir(path_to_done):
		try:
			assert seasyear.findall(f), ""
		except AssertionError:
			continue
		else:
			file_and_filter = (f, seasyear.findall(f)[0])
			faf.append(file_and_filter)
			faf_sorted_tuple = sorted(faf, key=lambda faf: faf[1])
	"""

	# need_read_subfolder_from_current_folder
	try:
		*fileparam, _ = os.walk(os.getcwd())  # folder/[subfolder]/[files]
	except BaseException:
		fileparam = ("", [], [])
	# else:
	# need_sort_by_regex

	# type(fileparam) # list(full_path=%s,?=list,short_file=list)
	# ('D:\\Multimedia\\Video\\Serials_Europe\\Zolotaya_kletka_Rus', [], ['01s01e.txt'])

	# filter_files = []

	for a, b, c in fileparam:  # (folder)str / (subfolder)list / (files)list
		try:
			assert bool(os.path.isdir(a) and a in some_subfolders), ""
		except AssertionError:
			some_subfolders.add(a)
			folders.append(a)
			logging.info("@folders %s" % a)

		try:
			assert bool(os.path.isdir(a) and len(b) > 0), ""
		except AssertionError:
			continue
		else:
			try:
				len_files += len(b)
				assert len_files, ""
			except AssertionError:
				logging.warning("@len_files skip %s" % a)
			else:
				sm += len_files
				ln += 1

			for bf in filter(lambda x: len(x) > 0, tuple(b)):
				try:
					assert bf, ""
				except AssertionError:
					continue
				else:
					files = [
						os.path.join(os.path.join(a, bf), f)
						for f in os.listdir(os.path.join(a, bf))
						if os.path.isfile(os.path.join(os.path.join(a, bf), f))
					]  # subfolders

					for f in filter(lambda x: os.path.isfile(x), tuple(files)):
						try:
							assert bool(f in some_files), ""
						except AssertionError:
							some_files.add(f)  # any_file
							if video_regex.findall(
								f.split("\\")[-1]
							):  # files_by_format
								files.append(f)
								logging.info("@files %s" % f)

	"""
	try:
		ag = avg_calc(sm, ln)  # avg_calc(100, 2) # 50
	except BaseException:
		ag = 0  # 0
	else:
		logging.info("@files/@folders/@ag %d %d %d" % (len(files), len(folders), ag))
	"""

	open(period_base, "w", encoding="utf-8").close()
	open(all_period_base, "w", encoding="utf-8").close()

	nt = 0
	days = months = years = []
	strt, cur_iter, max_iter = time(), 0, len(some_folders)
	mx_set = te_set = set()
	mx1 = mx2 = mx3 = 0
	last_folder = ""
	days = months = years = []
	filter_max_iter = 0
	filter_some_folders = filter_null_folders = []
	sm = ln = ag = 0  # max_ag

	for fsf in filter(
		lambda x: os.path.isdir(x), tuple(some_subfolders)
	):  # pass_1_of_3
		# @period
		try:
			today = datetime.now()
			fdate = os.path.getctime(fsf)  # getmtime -> debug(getctime/optimal)
			ndate = datetime.fromtimestamp(fdate)
		except BaseException as e:
			fsf_err = (fsf, str(e))
			logging.error("@fsf not exist folder %s, error: %s" % fsf_err)
			continue  # if_winerror

		# hide_avg
		"""
		try:
			days_ago = abs(today - ndate).days
			assert bool(days_ago >= 0), ""
		except AssertionError:  # if_none(today)
			days_ago = 0
		else:
			sm += days_ago
			ln += 1

			try:
				ag = (lambda s, l: s // l)(sm, ln)
				assert bool(ag > 0), ""
			except AssertionError:
				logging.warning("@ag current day, folder: %s" % fsf)
			else:
				logging.info("@ag %d days ago, folder: %s" % (ag, fsf))

				# max_ag = (
					# ag if max_ag < ag else max_ag
				# )
		"""

	# ag = (
	# max_ag if max_ag else ag
	# )

	for fsf in filter(
		lambda x: os.path.isdir(x), tuple(some_subfolders)
	):  # pass_2_of_3
		period_list_filter = []

		try:
			today = datetime.now()
			fdate = os.path.getctime(fsf)  # getmtime -> debug(getctime/optimal)
			ndate = datetime.fromtimestamp(fdate)
		except BaseException as e:
			fsf_err = (fsf, str(e))
			logging.error("@fsf not exist folder %s, error: %s" % fsf_err)
			continue  # if_winerror

		try:
			days_ago = abs(today - ndate).days
			assert bool(days_ago >= 0), ""
		except AssertionError:  # if_none(today)
			continue  # days_ago = 0

		# folder, days, day = r"F:\Videos\Serials\Serials_Conv\100", 30, 86400; N = days # 17.08.24 # fullday = 86400
		# ((time() - os.path.getmtime(fsf)) / 3600, 24 * days) # (26.338929861717755, 720)
		# (time() - os.path.getmtime(fsf)) / 3600 > 24 * days # days_ago = days # older(a<b)
		# (time() - os.path.getmtime(fsf)) / 3600 <= 24 * days # days_ago = days # newbie
		# (os.path.getmtime(fsf), (time() - day * N)) # (1723887503.6333315, 1721390357.1499963)
		# os.path.getmtime(fsf) > (time() - day * N) # day = (24 * 3600) # newbie
		# os.path.getmtime(fsf) <= (time() - day * N) # day = (24 * 3600) # older(>0)
		# ((time() - os.path.getmtime(fsf)), days * 24 * 3600) # (94939.88339042664, 2592000)
		# (time() - os.path.getmtime(fsf)) > days * 24 * 3600 # older
		# (time() - os.path.getmtime(fsf)) <= days * 24 * 3600 # newbie

		max_days_by_year = 366 if today.year % 4 == 0 else 365

		"""
		period_list_filter = [
			(time() - os.path.getmtime(fsf)) / 3600 <= 24 * ag,
			os.path.getmtime(fsf) > (time() - 86400 * ag),
			(time() - os.path.getmtime(fsf)) <= ag * 24 * 3600
		]  # newbie_folders(+avg_filter) # is_max_days
		"""

		# @older_or_newbie # days=ag ~ avg(+time) # days=max_days_by_year ~ year(+time)
		try:
			oon = asyncio.run(
				older_or_newbie(days=30, filename=fsf)
			)  # 30_days(+time/filter) # True(newbie) / False(older)
			assert oon, ""
		except AssertionError:
			oon = asyncio.run(
				older_or_newbie(days=90, filename=fsf)
			)  # 90_days(+time/filter) # True(newbie) / False(older) # debug(skip_older)
			logging.warning(
				"@oon try 30 to 90 days filter folder, current: %s"
				% fsf.split("\\")[-1]
			)  # debug(skip_older)
			period_list_filter = [oon]  # filter(90_days)
		except BaseException as e:
			logging.error("@oon error: %s, current: %s" % (str(e), fsf.split("\\")[-1]))
			period_list_filter = [False]  # debug(is_error_by_older)
		else:
			logging.info(
				"@oon 30 days filter folder, current: %s" % fsf.split("\\")[-1]
			)
			period_list_filter = [oon]  # filter(30_days)

		oon_status = (
			"@oon newbie folder, current: %s" % fsf.split("\\")[-1]
			if oon
			else "@oon older folder, current: %s" % fsf.split("\\")[-1]
		)
		logging.info("%s" % oon_status)

		if period_list_filter.count(True) > 0:  # newbie
			# filter_max_iter += 1

			try:
				assert bool(fsf.strip() in filter_some_folders), ""
			except AssertionError:
				filter_some_folders.append(fsf.strip())
			else:
				logging.info("@fsf/@filter_some_folders %s" % fsf)
		elif period_list_filter.count(True) == 0:  # older
			try:
				assert bool(fsf.strip() in filter_null_folders), ""
			except AssertionError:
				filter_null_folders.append(fsf.strip())
			else:
				logging.info("@fsf/@filter_null_folders %s" % fsf)
			# logging.info("@period_list_filter skip folder %s" % fsf)
			# continue
	else:
		some_subfolders = (
			filter_some_folders if filter_some_folders else filter_null_folders
		)  # newbie -> older

		max_iter = len(some_subfolders)  # debug

	try:
		assert bool(all((max_iter, some_subfolders))), ""
	except AssertionError:  # if_null(no_count/no_folders)
		exit()

	# debug
	# exit()

	t = Timer(max_iter)

	# '''
	# short_folders
	short_list = list(
		set([ss.split("\\")[-1].strip() for ss in some_subfolders])
	)  # only_folders

	# @fcd.txt
	with open(combine_base, "w", encoding="utf-8") as cbf:  # fcd.txt
		# cbf.writelines("%s\n" % sl for sl in filter(lambda x: len(x) > 1, tuple(short_list)))  # multicommander(is_short)
		cbf.writelines(
			"%s\\\n" % sl for sl in filter(lambda x: len(x) > 1, tuple(short_list))
		)  # totalcommander(is_short)
	# '''

	for fsf in filter(
		lambda x: os.path.isdir(x), tuple(some_subfolders)
	):  # pass_3_of_3
		last_folder = fsf

		is_day = is_month = is_year = False

		period_list_filter = []

		# @period
		try:
			today = datetime.now()
			fdate = os.path.getctime(fsf)  # getmtime -> debug(getctime/optimal)
			ndate = datetime.fromtimestamp(fdate)
		except BaseException as e:
			fsf_err = (fsf, str(e))
			logging.error("@fsf not exist folder %s, error: %s" % fsf_err)
			continue  # if_winerror

		try:
			days_ago = abs(today - ndate).days
			assert bool(days_ago >= 0), ""
		except AssertionError:  # if_none(today)
			days_ago = 0
		else:
			logging.info("@days_ago %d days ago, folder: %s" % (days_ago, fsf))

		max_days_by_year = 366 if today.year % 4 == 0 else 365

		if all((fsf, days_ago >= 0)):
			job_count += 1

			if days_ago % 7 <= 4:  # period_list_filter[0] # week
				is_day = True
				week_status = (
					"%d недель назад" % (days_ago % 7)
					if days_ago % 7 > 0
					else "эта неделя"
				)  # недель/это неделя

				try:
					assert bool(fsf.split("\\")[-1] in days), ""
				except AssertionError:
					days.append(fsf.split("\\")[-1])

				mx1 = days_ago % 7 if mx1 < days_ago % 7 else mx1

			elif days_ago % 30 <= 12:  # period_list_filter[1] # month
				is_month = True
				week_status = (
					"%d месяцев назад" % (days_ago % 30)
					if days_ago % 30 > 0
					else "этот месяц"
				)  # месяцев/этот ме

				try:
					assert bool(fsf.split("\\")[-1] in months), ""
				except AssertionError:
					months.append(fsf.split("\\")[-1])

				mx2 = days_ago % 30 if mx2 < days_ago % 30 else mx2

			elif (
				days_ago % max_days_by_year <= max_days_by_year + 1
			):  # period_list_filter[-1] # year
				is_year = True
				week_status = (
					"%d дней назад" % (days_ago % max_days_by_year)
					if days_ago % max_days_by_year > 0
					else "этот год"
				)  # дней/этот год

				try:
					assert bool(fsf.split("\\")[-1] in years), ""
				except AssertionError:
					years.append(fsf.split("\\")[-1])

				mx3 = (
					days_ago % max_days_by_year
					if mx3 < days_ago % max_days_by_year
					else mx3
				)

			if any((is_day, is_month, is_year)):  # some_period
				week_status = "%d дней назад" % days_ago
				all_period_dict[week_status.strip()] = [
					fsf.split("\\")[-1],
					fsf,
					len_files,
					week_status,
				]  # any_periods
			else:  # another_period
				week_status = "%d дней назад!" % days_ago

			logging.info(
				"@mx1/@mx2/@mx3/@fsf %s" % str((mx1, mx2, mx3, fsf))
			)  # folder_by_periods

			all_period = (fsf.split("\\")[-1], days_ago, len_files)

			week_status_str = (all_period[0], week_status, all_period[2])

			logging.info(
				"@datetime [period] folder: %s, days_ago: %s, count_files: %d"
				% week_status_str
			)  # folder / days_ago / count_files

			with open(
				period_base, "a", encoding="utf-8", buffering=1
			) as pbf:  # buffering
				pbf.writelines(
					"%s\n" % all_period[0]
				)  # multicommander # fsf.split("\\")[-1]
				# pbf.writelines("%s\\\n" % all_period[0]) # totalcommander # fsf.split("\\")[-1]

		# sleep(1) # 0.05
		cur_iter += 1

		list_files = []  # list_files_old

		try:
			list_files = [
				os.path.join(fsf, f)
				for f in os.listdir(fsf)
				if os.path.isfile(os.path.join(fsf, f)) and video_regex.findall(f)
			]
			assert list_files, ""
		except AssertionError:  # is_null_jobs
			logging.warning(
				"@list_files в папке %s нет файлов по фильтру" % fsf.split("\\")[-1]
			)
			continue  # skip_folder(no_files)

		# @count
		try:
			len_files = len(
				list(
					filter(
						lambda x: video_regex.findall(x.split("\\")[-1]),
						tuple(list_files),
					)
				)
			)  # all_types
		except BaseException as e:
			len_files_err = (str(e), fsf)
			logging.error("@len_files error: %s, current: %s" % len_files_err)

		all_period = ("", "", 0)

		try:
			assert all((fsf, len_files)), ""
		except AssertionError:  # no_folder / no_count
			continue
		else:
			try:
				all_period = (fsf.split("\\")[-1], fsf, len_files)
				assert bool(all_period in all_period_set), ""
			except AssertionError:  # no_folder / no_count
				all_period_set.add(all_period)
				logging.warning("@all_period add new %s" % str(all_period))
			else:
				logging.info("@all_period %s exists" % all_period[0])

		# group_files_by_date
		if len(list_files) > 1: # sort_by_modify_date
			create_time_list = sorted(
				[os.path.getmtime(f) for f in list_files], reverse=False
			)  # list # +getmtime
			old_time_list = [os.path.getmtime(f) for f in list_files]  # list
			new_time_list = zip(
				create_time_list, old_time_list, list_files
			)  # generator(one_time)

			try:
				create_and_old_time_list = [
					i
					for i in len(create_time_list)
					if create_time_list[i] != old_time_list[i]
				]
			except BaseException:
				create_and_old_time_list = []

			if create_and_old_time_list:
				for ctl, otl, pf in new_time_list:
					try:
						assert all((otl, ctl, pf)), ""
					except AssertionError:  # if_null(date/project_file)
						continue

					if all((ctl, otl, ctl != otl)):  # if_diff_time
						logging.info(
							"@project_file[utime][description] %s"
							% ";".join(
								[unixtime_to_date(ctl), unixtime_to_date(otl), pf]
							)
						)
						os.utime(
							pf, times=(otl, ctl)
						)  # sort_and_update_some_date # old -> new
					else:
						continue
		else:  # if_no_projects
			week_status = "%d дней назад!" % days_ago  # is_another_period
			week_status_str = (all_period[0], week_status, all_period[2])

			logging.info(
				"@datetime [another_period] folder: %s, days_ago: %s, count_files: %d"
				% week_status_str
			)  # folder / days_ago / count_files

			with open(
				all_period_base, "a", encoding="utf-8", buffering=1
			) as apbf:  # buffering
				apbf.writelines(
					"%s\n" % all_period[0]
				)  # multicommander # fsf.split("\\")[-1]
				# apbf.writelines("%s\\\n" % all_period[0]) # totalcommander # fsf.split("\\")[-1]

		telapsed, tleft, etime, current = calcProcessTime(
			strt, cur_iter, max_iter, add.full_to_short(fsf)
		)  # prstime
		# print("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % (sec_to_time(telapsed), sec_to_time(tleft), etime, add.full_to_short(current))) # sec_to_time
		# logging.info("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % (sec_to_time(telapsed), sec_to_time(tleft), etime, add.full_to_short(current)))

		try:
			sleep(60 - time() + strt)
		except BaseException:
			sleep(0.05)

		try:
			assert bool(t.remains(cur_iter) in te_set), ""
		except AssertionError:
			prstime = (t.remains(cur_iter), etime, add.full_to_short(fsf))

			try:
				te_set.add(prstime[0])  # t.remains(cur_iter)
			except BaseException as e:
				te_str = (str(e), fsf.split("\\")[-1])
				logging.error("@te_str add error: %s, current: %s" % te_str)
			else:
				print(
					Style.BRIGHT
					+ Fore.YELLOW
					+ "@prstime left: %s(s), estimated finish time: %s, current: %s"
					% prstime
				)  # t.remains(cur_iter)
				logging.info(
					"@prstime left: %s(s), estimated finish time: %s, current: %s"
					% prstime
				)
		except BaseException as e2:
			te_str = (str(e2), fsf.split("\\")[-1])
			logging.error("@te_str error: %s, filename: %s" % te_str)
		else:
			prstime = (t.remains(cur_iter), etime, add.full_to_short(fsf))

			print(
				Style.BRIGHT
				+ Fore.YELLOW
				+ "@prstime left: %s(s), estimated finish time: %s, current: %s"
				% prstime
			)  # t.remains(cur_iter)
			logging.info(
				"@prstime left: %s(s), estimated finish time: %s, current: %s" % prstime
			)
	else:
		logging.info(
			"@fsf time_end: %s, current: %s" % (str(datetime.now()), last_folder)
		)

	if sf:
		sf_calc, sf_calc_status = 0, ""

		sizes_dict = {}

		sizes_dict[1] = "Kb"
		sizes_dict[2] = "Mb"
		sizes_dict[3] = "Gb"
		sizes_dict[4] = "Tb"

		try:
			for i in range(1, 5):
				try:
					sf_calc = (lambda sf_index, size: sf_index // (1024**size))(sf, i)
					assert bool(sf_calc > 0), ""
				except AssertionError:
					continue
				else:
					sf_calc_status = "".join([str(sf_calc), sizes_dict[i]])
		except BaseException as e:
			sf_calc, sf_calc_status = 0, ""
			sf_calc_str = (fsf, str(e))
			logging.error("@sf_calc [%s] [%s]" % sf_calc_str)
		else:
			sf_calc_str = (fsf, sf_calc_status)
			logging.info("@sf_calc [%s] [%s]" % sf_calc_str)

	all_period_copy_dict = all_period_dict if all_period_dict else {}

	try:
		# all_period_dict = {k:v for k, v in all_period_dict.items() if all((v[2], v[2] - cntfiles > 0))} # ?(is_small_classify)
		# all_period_dict = {k:v for k, v in all_period_dict.items() if all((v[2], v[2] - cntfiles < 0))} # ?(is_big_classify)
		all_period_dict = {
			k: v for k, v in all_period_dict.items() if all((v[2], v[2] in range(ag)))
		}  # all_jobs(+avg)
		assert all_period_dict, ""
	except AssertionError:
		all_period_dict = {
			k: v for k, v in all_period_copy_dict.items() if v[2]
		}  # default_period(in_range)
	finally:
		# {"250 лет назад": ["Animal_Kingdom", "E:\\Multimedia\\Video\\Serials_conv\\Animal_Kingdom", 35]}
		with open(all_period_json, "w", encoding="utf-8") as apjf:
			json.dump(
				all_period_dict, apjf, ensure_ascii=False, indent=4, sort_keys=False
			)  # save_periods

	fcd_folders = [v[0].strip() for _, v in all_period_dict.items()]

	periods = []

	periods += days
	periods += months
	periods += years

	periods = list(set(periods))
	periods.sort(reverse=False)

	split_periods = [
		p.split("_")[0].strip() if len(p.split("_")) > 0 else p.strip() for p in periods
	]  # choice_first_word

	two_periods = zip(split_periods, periods)

	# with open()

	pj_dict = {}

	# @periods.json(video_trimmer2)
	with open(period_json, "w", encoding="utf-8") as pjf:
		json.dump({}, pjf, ensure_ascii=False, indent=4, sort_keys=True)

	for a, b in two_periods:
		if len(a) == len(b):
			logging.info("@two_periods equal: %s" % str(a))
			pj_dict[a.strip()] = "%s" % a
		elif len(a) != len(b):
			logging.info("@two_periods/@a/@b diff: %s" % str((a, b)))
			pj_dict[a.strip()] = "%s" % b

	pj_dict = {k: k if k == v else v for k, v in pj_dict.items()}  # debug

	with open(period_json, "w", encoding="utf-8") as pjf:
		json.dump(pj_dict, pjf, ensure_ascii=False, indent=4, sort_keys=True)

	"""
	# @period.lst(optimize_days) # update_period_list # skip
	try:
		assert pj_dict, ""
	except AssertionError:
		logging.warning("no periods")
	else:
		# @period.lst
		with open(period_base, "w", encoding="utf-8") as pbf:
			# pbf.writelines("%s\n" % k for k, _ in pj_dict.items())  # multicommander
			pbf.writelines("%s\\\n" % k for k, _ in pj_dict.items())  # totalcommander(is_short)
	"""

	# days_ago_base
	try:
		assert days, ""
	except AssertionError:
		logging.error("no days")
	else:
		with open(days_ago_base, "w", encoding="utf-8") as dabf:
			dabf.writelines(
				"%s\n" % d for d in filter(lambda x: x in fcd_folders, tuple(days))
			)  # filter_by_day(week)
			# dabf.writelines("%s\\\n" % d for d in days) # totalcommander

	# month_forward_base
	try:
		assert months, ""
	except AssertionError:
		logging.error("no months")
	else:
		with open(month_forward_base, "w", encoding="utf-8") as mfbf:
			mfbf.writelines(
				"%s\n" % m for m in filter(lambda x: x in fcd_folders, tuple(months))
			)  # filter_by_month
			# mfbf.writelines("%s\\\n" % m for m in months) # totalcommander

	# calc_year_base
	try:
		assert years, ""
	except AssertionError:
		logging.error("no years")
	else:
		with open(calc_year_base, "w", encoding="utf-8") as cybf:
			cybf.writelines(
				"%s\n" % y for y in filter(lambda x: x in fcd_folders, tuple(years))
			)  # filter_by_year
			# cybf.writelines("%s\\\n" % y for y in years) # totalcommander

	with open(all_period_base, "w", encoding="utf-8") as apbf:
		apbf.writelines("%s\n" % v[0] for _, v in all_period_dict.items())
		# apbf.writelines("%s\\\n" % v[0] for _, v in all_period_dict.items()) # totalcommander

	logging.info("@all_period_dict %d" % len(all_period_dict))

	end = time()

	finish = int(abs(end - start))  # in_seconds
	finish_ms = finish * 1000  # in_ms

	try:
		assert bool((finish // 3600) > 0), ""
	except AssertionError:
		finish_min = (
			"minutes: %d" % (finish // 60)
			if finish // 60 > 0
			else "seconds: %d " % finish
		)
	else:
		finish_min = (
			"hours: %d" % (finish_ms // 3600)
			if finish // 3600 > 0
			else "minutes: %d " % finish
		)

	try:
		if job_count:  # files_count
			logging.info(
				"optimize_days.py run, time: %d ms, calc_time: %s, count: %d, time_per_file_list: %s"
				% (
					finish_ms,
					finish_min,
					job_count,
					";".join(
						[
							str(job_count / ms_to_time(finish)),
							str(ms_to_time(finish) / job_count),
						]
					),
				)
			)
		assert all((finish, job_count)), ""
	except BaseException as e:
		logging.error("@job_count error: %s" % str(e))
	except AssertionError:
		logging.warning(
			"@finish/@job_count %s" % ", ".join(map(str, (finish, job_count)))
		)
	else:
		logging.info("@finish/@job_count %s" % ", ".join(map(str, (finish, job_count))))

	sizes_dict = {}

	sizes_dict[1] = "Kb"
	sizes_dict[2] = "Mb"
	sizes_dict[3] = "Gb"

	try:
		dsize = disk_usage(f"{dletter}").free  # "c:\\"
		assert dsize, ""
	except AssertionError:
		logging.warning("@dsize null %s" % dletter)
	else:
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

	dt = datetime.now()

	no_ms = str(dt).split(".")[0]

	sound_notify(f"@finish {no_ms}")
	logging.info(f"@finish {no_ms}")

	# '''
	if dt.hour < mytime["sleeptime"][1]:
		run(
			[
				"cmd",
				"/c",
				"shutdown",
				"/s",
				"/t",
				"900",
				"/c",
				"Чтобы отменить выключение, выполните в командной строке shutdown /a",
			],
			shell=False,
		)  # shutdown(15min) (midnight - 7am) # start_after # if_updates

		sound_notify(
			r"Чтобы отменить выключение, выполните в командной строке shutdown /a"
		)
	# '''

	# string = "hello world"
	# splited_regex = re.compile(r"(\w+|\d+|^\s+)", re.I)
	# splited = ";".join(splited_regex.split(string)); print(splited)

	# clear_globals
	try:
		glob_dict = vars()
		assert glob_dict, ""
	except AssertionError:
		logging.warning("@glob_dict empty")

	try:
		ext = "".join([".", __file__.split(".")[-1]])
	except BaseException:
		ext = ""

	"""
	try:
		# script_path = os.path.dirname(os.path.realpath(__file__)).lower()
		filename = "\\".join([script_path, __file__.replace(ext, ".glob")])  # ?
	except BaseException:
		filename = ""
	else:
		if filename:
			with open(filename, "w", encoding="utf-8") as fj:
				json.dump(
					glob_dict, fj, ensure_ascii=False, indent=4, sort_keys=False
				)  # debug
	"""

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
	except BaseException:
		pass
