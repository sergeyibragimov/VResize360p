# -*- coding: utf-8 -*-

# --- semi_automatic(debug) ---

# Полуавтоматическое форматрирование файлов с метаданными(scale/profile/level)
# Целый файл без разрезов(скрыть если не нужно)

# from os import getcwd # cpu_count  # текущая папка # cpu_count
# from psutil import cpu_count  # viirtual_memory # pip install --user psutil
# import gevent.monkey # pip install --user gevent # is_async(debug)
# import psutil
# import tomllib # look like json - parsing TOML (Python 3.11)
from datetime import (
	datetime,
	timedelta,
)  # дата и время
from shutil import (
	disk_usage,
	move,
)  # copy # файлы # usage(total=16388190208, used=16144154624, free=244035584)
from subprocess import run  # TimeoutExpired, check_output, Popen, call, PIPE, STDOUT # Работа с процессами # console shell=["True", "False"]
from time import (
	time,
	sleep,
)
import asyncio  # TaskGroup(Python 3.11+)
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
from colorama import (
	Fore,
	Style,
	init,
)

# from multiprocessing import Process # Process(target=compute_heavy).start() # join # Многопроцессорность: Применимо к вычислительно сложным задачам, позволяет всем менять ограничения GIL, используя несколько CPU 
# from threading import Thread # Thread(target=disk_io_bound).start() # join # Многопоточность: Она оптимальна для задач, связанных с ожиданием I/O и возможностью параллельного выполнения, обусловленной освобождением GIL во время операций I/O. 
# import asyncio # asyncio.run(async_io_operation()) # Asyncio: Лучший инструмент для асинхронных I/O-операций с эффективным переключением между задачами и снижением возможных проблем, связанных с многопоточностью.

# python version requerments?
"""
# import tzdata # pip install --user -U tzdata
import zoneinfo # pip install --user -U zoneinfo 
from datetime import datetime

# print(len(zoneinfo.available_timezones())) # >= 594

timezone1 = zoneinfo.ZoneInfo("US/Pacific")
print(datetime.now(tz=timezone1))
"""

# match case, python 3.10

"""
def switch():  # res(int)
	res = 999

	match res:
		case 0 | 1 | 999:  # some_value_from_case
			return "ok"
		case _:
			return "unknown"

switch()  # ok <-> unknown

point = [2, 5]  # [0, 3]

def switch_list():  # point(list)
	match point:
		case 0, 3:
			return ("No move")
		case x, 3:
			return (f"moved on x-axis - {x} points")
		case 0, y:
			return (f"moved on y-axis - {y} points")
		case x, y:
			return (f"moved along moth axes - {x}:{y} points")

cmd = "quit"
cmd2 = "menu start"
cmd3 = "param go west"

def switch_list2(cmd):
	match cmd.split():
		case ["quit"]:
			print("we quited")
		case ["menu", status]:
			print(f"my status {status}")
		case ["param", *two]:
			print(f"params: {two}")
		case _:
			print("Unknown command")

switch_list2(cmd)  # ?
switch_list2(cmd2)  # ?
switch_list2(cmd3)  # ?

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

class Circle:
	def __init__(self, radius):
		self.radius = radius

def switch_class(shape):  # ?
	match shape:
		case Rectangle(width=w, height=h):
			return w * h
		case Circle(radius=r):
			return 3.14 * r * r
		case _:
			return "Unknwon shape"

result = swith_class(Circle(10))  # ?

print(result)

data = None
data1 = ["bot"]
data2 = ["user"]
data3 = ["user", "Bob", 18]

def switch_logic(data):
	match data:
		case [_, _, age] if age >= 18:
			print("access granted")
		case _:
			print("access denied")

# switch_logic(data1) # switch_logic(data2) # ? # bad
switch_logic(data3) # ? # ok

def switch_dict(dictionary):
    # match case
    match dictionary:
        # pattern 1
        case {"name": n, "age": a}:
            print(f"Name:{n}, Age:{a}")
        # pattern 2
        case {"name": n, "salary": s}:
            print(f"Name:{n}, Salary:{s}")
        # default pattern
        case _ :
            print("Data does not exist")

switch_dict({"name": "Jay", "age": 24})  # ?
switch_dict({"name": "Ed", "salary": 25000})  # ?
switch_dict({"name": "Al", "age": 27})  # ?
switch_dict({})  # ?
"""

# try_except(note), python 3.11

"""
try:
	raise ExceptionGroup("Description exception group", [ValueError("Some bad"), TypeError("Terrable"), ])
exccept* ValueError as eg:  # TypeError, IndexError # Exception(all)
	for exc in eg.exceptions:
		print(f"{exc}")

try:
	var = val
except Exception as e:
	from datetime import datetime
	# add_error_note(for_debug)
	e.add_note(f"Script down at {datetime.now()}")
	print(e.__notes__) # raise
"""

# TaskGroup, python 3.11

"""
import asyncio

async def sleep(seconds: int) -> None:
	await asyncio.sleep(seconds)
	print(f"sleeped {second}s")

async def old_main():
	tasks = []
	for seconds in (3, 1, 2):
		tasks.append(asyncio.create_task(sleep(seconds)))
	await asyncio.gather(*tasks)

async def main():
	async with asyncio.TaskGroup() as tg:
		for seconds in (3, 1, 2):
			tg.create_task(sleep(seconds))

asyncio.run(main())
"""

# optimal_run_timer
"""
from time import time

elapsed_list = []
for i in range(10):
	timer = time()
	# func() # list / dict / str / sum / ...?
	elapsed = time() - timer
	elapsed_list.append(elapsed)

avg_elapsed_time = sum(elapsed_list) // len(elapsed_list)
print(f"%.3f second's" % avg_elapsed_time); sleep(avg_elapsed_time)
"""

# teranar value
"""
status = True

some_value = ("1.0", "2.0")[not status] # 1.0
some_value = ("1.0", "2.0")[status] # 2.0
"""

# pip install --user bpython (interactive_color_terminal) # launch?

# python -m trace --trace scprle.py

# vosk (+Python/Subtitle Edit"Video") # video(audio)_to_text(is_subtitle)

__version__ = "0.1"
__author__ = "Sergey Ibragimov"

# ffmpeg -i blah.vtt blah.srt # manual_convert_subtitle

# debug_moules
# exit()

# mklink /h scale_profile_level.py scprle.py

# qos ~ 1 * 1024 = 1mb, speed ~ (5/8) * 1024 = 1280 kb/s

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
current_folder = "".join(
	[
		os.path.dirname(os.path.realpath(sys.argv[0])),
		"\\"
	])

dletter = "".join(
	[
		basedir.split("\\")[0],
		"\\"
	])  # "".join(script_path[0:5]) if script_path else "".join(os.getcwd()[0:5])

# logging(start)
log_file = "%s\\scprle.log" % script_path  # main_debug(logging)

# --- path's ---
path_for_queue = r"d:\\downloads\\mytemp\\"
path_to_done = "%sdownloads\\list\\" % dletter  # "c:\\downloads\\" # ready_folder
path_for_folder1 = "".join(
	[
		os.getcwd(),
		"\\"
	])  # "c:\\downloads\\new\\"

# list(json)_by_period
all_period_json = "%s\\all_period.json" % script_path  # ?
calc_year_base = "%s\\calc_year.lst" % script_path
cmd_list = "%s\\scprle.cmd" % script_path
combine_base = "%s\\fcd.txt" % script_path
combine_base2 = "%s\\fcd_.txt" % script_path  # regex_filter((\(|_).*\..*)
days_ago_base = "%s\\days_ago.lst" % script_path
days_ago_list = "%s\\days_ago.txt" % script_path
fcd_base = "%s\\fcd.json" % script_path
fcd_lst = "%s\\fcd.lst" % script_path
month_forward_base = "%s\\month_forward.lst" % script_path
period_base = "%s\\period.lst" % script_path
period_json = "%s\\period.json" % script_path

# '''
try:
	dsize = disk_usage(f"{dletter}").free  # "c:\\"
	# assert dsize, ""
except BaseException: # AssertionError:
	logging.basicConfig(
		format="%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s",
		level=logging.INFO,
	)  # no_file # pass
else: # finally -> else
	if (
		dsize // (1024**2) > 0
	):  # any_Mb # debug
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

"""
list_files: list = []
list_files.append(calc_year_base)
list_files.append(cmd_list)
list_files.append(combine_base)
list_files.append(combine_base2)
list_files.append(days_ago_base)
list_files.append(days_ago_list)
list_files.append(fcd_lst)
list_files.append(month_forward_base)
list_files.append(period_base)

for cmd_files in filter(lambda x: os.path.exists(x), tuple(list_files)):
	os.remove(cmd_files)
"""

try:
	assert os.path.exists(path_to_done), ""
except AssertionError:
	try:
		os.mkdir(path_to_done)
	except:
		exit()  # path_to_done = "c:\\downloads\\"

# @regex
# (.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg|^.dmf|^.txt|^.srt|^.vtt|^.dmfr|^.aria2|^.crswap|^.filepart|^.crdownload)
video_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg))$",
	re.M,
)
space_regex = re.compile(
	r"[\s]{2,}"
)  # text = "hello  world" # space_regex.sub(" ", text)
# not_include_regex = re.compile(r"^.*(?!(copy).*)$", re.I) # debug
crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)", re.I)
year_regex = re.compile(r"\([\d+]{4}\)", re.M)
seasyear = re.compile(
	r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))", re.M
)  # MatchCase # season_and_year(findall) # +additional(_[\d+]{2}p)

# a = "test|test2|test30|test40|test999"
# a_regex = re.compile(r"test[\d+]{2,}?", re.M) # a_regex.findall(a) # ['test30', 'test40', 'test99']
# a_regex = re.compile(r"test[\d+]{1,}", re.M) # a_regex.findall(a) # ['test2', 'test30', 'test40', 'test999']
# a_regex = re.compile(r"test[\d+]??", re.M) # a_regex.findall(a) # ['test', 'test', 'test', 'test', 'test']
# a_regex = re.compile(r"test[\d]?", re.M) # a_regex.findall(a) # ['test', 'test2', 'test3', 'test4', 'test9']
# a_regex = re.compile(r"test[\d]", re.M) # a_regex.findall(a) # ['test2', 'test3', 'test4', 'test9']
# a_regex = re.compile(r"test[\d+]{1,}", re.M) # list(set(a_regex.split(a))) # ['test|', '', '|']

start = time()

# files_count = 0

mytime = {
	"jobtime": [9, 18, 5],
	"dinnertime": [12, 14],
	"dnd": [22, 8],
	"sleeptime": [0, 8],
	"anytime": [True],
	"weekindex": 4,
}  # sleep_time_less_hour # debug # weekindex (0 - 4, monday-friday)


# @oop
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


# t = Timer(12987) # max_count_tasks # There are 12987 units in this task

# do some work

# sleep(1) # time.sleep(1)

# after some time passed, or after some units were processed
# eg.  37 units, calculate, and print the remaining time:
# print(t.remains(37)) # current_how_match # let the process continue and once in a while print the remining time.


class Additional:
	def __init__(self):
		pass

	def full_to_short(self, filename) -> str:
		"""change_full_to_short(if_need_or_test_by_logging) # temporary_not_use"""

		self.filename = filename

		try:
			assert self.filename and os.path.exists(
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
				[
					self.filename[0],
					":\\...\\",
					self.filename.split("\\")[-1]
				]).strip()  # is_ok
		except:
			short_filename = self.filename.strip()  # if_error_stay_old_filename

		return short_filename

	def __del__(self):
		print(
			Style.BRIGHT + Fore.WHITE + "%s удалён" % str(self.__class__.__name__)
		)  # del_class


add = Additional()


def check_dict(
	dct: dict, item=["", None]
):  # dict(json) / find_key / find_value # docstring(sample)
	"""
	>>> a = {"a":1, "b":2, "c":3}
	>>> a.get(5,4) # 4 # no_key
	>>> a.get("a",4) # 1 # yes_key
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

	pass

	"""
	create_files = []
	
	create_files.extend([period_base, cmd_list, fcd_lst]) # fcd_base # skip_periods # "log_file"

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
	"""


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
) -> tuple:  # 4

	# calc_number_of_day
	if is_default:
		dt_calc = datetime.now()  # day / month / year

		dt_str = ".".join(
			map(str, (dt_calc.day, dt_calc.month, dt_calc.year))
		)
	elif not is_default:
		dt_str = ".".join(
			map(str, (day, month, year))
		)

	if all(
		(
			sleep_if,
			dt_str == sleep_if,
			not is_default
		)
	):
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
		print(";".join(
			map(str, (c1, c2, c3, c4, dt_str))),
			"from def"
		)

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
	except:
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

# clear_base_and_lists()

logging.info("%s" % ";".join(
	[
		basedir,
		script_path
	])
)

try:
	files_types: list[int] = [
		0 if os.path.isfile(os.path.join(os.getcwd(), f)) else 1
		for f in os.listdir(os.getcwd())
	]  # python 3.9

	assert files_types, ""
except AssertionError:
	logging.warning("@files_types no files or no folders")
else:
	if files_types.count(0) == 0:  # if_no_files_up_dir
		os.chdir("..")

	logging.info("@files_types found %d data" % len(files_types))

test_folders = test_files = []

# 15632076800 # 3687570583552
# """
dspace_list = []
dspace_another_drive = 0.0

# dletter_and_dspace = {}

# add_and_save_to_json(is_linux)
"""
import gio

for mount in volume_monitor.get_mounts():
    print(mount.get_name(), mount.get_icon())
"""

# is_for_portable_devices
"""
import win32api
import win32file
drives = win32api.GetLogicalDriveStrings()
drives =  drives.split('\000')[:-1]

for drive in drives:
	if win32file.GetDriveType(drive)==win32file.DRIVE_REMOVABLE:
		label,fs,serial,c,d = win32api.GetVolumeInformation(drive)
		print(label)
"""

for dl in range(ord("c"), ord("z") + 1):
	du = "".join(
		[
			str(chr(dl)),
			":\\"
		])

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
	print(";".join(
		map(str, ("%s" % du, int(disk_usage("%s" % du).used))))
	)

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

# pass_1_of_2

# @fcd.json; load / create(if_error)
try:
	with open(fcd_base, encoding="utf-8") as fjf:
		fcd = json.load(fjf)
except:
	fcd = {}

	with open(fcd_base, "w", encoding="utf-8") as fjf:
		json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=False)

if fcd:  # @filter_on_dst
	for k, _ in fcd.items():
		if os.path.exists(
			"".join(
				[
					path_to_done,
					k.split("\\")[-1].replace(k.split(".")[-1],	"cmd")
				])
		) and os.path.exists(k.replace(k.split(".")[-1], "cmd")):
			os.remove(
				k.replace(k.split(".")[-1], "cmd")
			)  # if_found_cmd_file_in_dst_clear_in_src
		elif not os.path.exists(
			"".join(
				[
					path_to_done,
					k.split("\\")[-1].replace(k.split(".")[-1], "cmd")
				])
		) and os.path.exists(k.replace(k.split(".")[-1], "cmd")):
			move(
				k.replace(k.split(".")[-1], "cmd"),
				"".join(
					[
						path_to_done,
						k.split("\\")[-1].replace(k.split(".")[-1], "cmd")
					]),
			)  # if_not_found_cmd_file_in_dst

	# remove_or_move(clear_base)
	# """
	with open(fcd_base, "w", encoding="utf-8") as fjf:
		json.dump(
			{}, fjf, ensure_ascii=False, indent=4, sort_keys=False
		)  # clear_after_load
	# """


class VideoProject:
	def __init__(self):
		pass

	def width_and_height(self, filename, is_log: bool = True):
		global job_count

		self.filename = filename

		# ffprobe -v error -show_entries stream=width,height -of csv=p=0:s=x input.m4v
		cmd_wh: list[str] = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=width,height",
			"-of",
			"csv=p=0:s=x",
			self.filename,
		]  # output_format # python 3.9
		wi = "".join(
			[
				current_folder,
				"wh.nfo"
			])  # path_for_queue

		try:
			p = os.system("cmd /c %s > %s" % (" ".join(cmd_wh), wi))  # cmd /k
			assert bool(p == 0), ""
		except AssertionError:
			return (0, 0, False)

		# width_height_str = ""

		width, height = 0, 0

		try:
			with open(wi) as whf:
				width_height_str = whf.readlines()[0].strip()
		except BaseException:
			width_height_str = ""

		if os.path.exists(wi):
			os.remove(wi)

		try:
			if "x" in width_height_str:
				width, height = int(width_height_str.split("x")[0]), int(
					width_height_str.split("x")[-1]
				)

		except BaseException:
			width, height = 0, 0
			if is_log:
				print(
					Style.BRIGHT + Fore.RED + "debug [w/h error]: %s" % self.filename
				)  # error
		finally:
			logging.info(
				"filename: %s, width/height: %s"
				% (add.full_to_short(filename), "x".join(map(str, [width, height])))
			)

			if all(
				(
					width,
					height
				)
			):
				job_count += 1  # need_scale(debug)
				return (int(width), int(height), False)
			elif any(
				(
					not width,
					not height
				)
			):
				return (0, 0, False)

	def get_profile_and_level(self, filename):
		global job_count

		self.filename = filename

		cmd_pl: list[str] = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=profile,level",
			"-of",
			"default=noprint_wrappers=1",
			self.filename,
		]  # output_format # python 3.9
		plf = "".join(
			[
				current_folder,
				"profile_and_level.nfo"
			])  # path_for_queue

		try:
			p = os.system(
				"cmd /c %s > %s" % (" ".join(cmd_pl), plf)
			)  # profile=High # level=50 # cmd /k
			assert bool(p == 0), ""
		except AssertionError:
			return ("", "")

		pl_list = []

		with open(plf, encoding="utf-8") as plff:
			pl_list = plff.readlines()

		if len(pl_list) > 2:
			pl_list = pl_list[0:2]

		logging.info(
			"filename: %s, profile/level: %s"
			% (
				add.full_to_short(filename),
				"x".join(
					map(str, [pl_list[0], pl_list[-1]])),
			)
		)

		if os.path.exists(plf):
			os.remove(plf)

		is_have = False

		try:
			if pl_list:
				is_have = True
		except BaseException:
			return ("", "")
		else:
			if is_have:
				# write_log(
				# "debug profilelevel", ";".join(
				# [
				# pl_list[0].split("=")[-1].lower().strip(), pl_list[1].split("=")[-1].lower().strip(),
				# filename
				# ]
				# ))

				job_count += 1  # need_profile(debug)

				return (
					pl_list[0].split("=")[-1].lower().strip(),
					pl_list[1].split("=")[-1].lower().strip(),
				)  # [main,30]

	def get_length(self, filename):
		self.filename = filename

		cmd_fd: list[str] = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"format=duration",
			"-of",
			"compact=p=0:nk=1",
			self.filename,
		]  # output_format # python 3.9
		fdi = "".join(
			[
				current_folder,
				"duration.nfo"
			])  # path_for_queue

		duration_list = []

		duration_null = 0

		try:
			p = os.system(
				"cmd /c %s > %s" % (" ".join(cmd_fd), fdi)
			)  # 1|und #type1 # cmd /k
			assert bool(p == 0), ""
		except AssertionError:
			return duration_null

		try:
			with open(fdi, encoding="utf-8") as fdif:
				duration_list = fdif.readlines()
		except BaseException:
			duration_list = []

		if os.path.exists(fdi):
			os.remove(fdi)

		try:
			if "." in duration_list[0] and duration_list:
				duration_null = int(duration_list[0].split(".")[0])
			elif not "." in duration_list[0] and duration_list:
				duration_null = int(duration_list[0])
		except BaseException:
			duration_null = 0

		try:
			if "." in duration_list[0] and duration_list:
				logging.info(
					"filename: %s, duration: %s"
					% (
						add.full_to_short(filename),
						str(int(duration_list[0].split(".")[0])),
					)
				)
				duration_null = int(duration_list[0].split(".")[0])
				return duration_null  # int(duration_list[0].split(".")[0])
			assert duration_list, ""
		except BaseException as e:
			duration_list_err = (add.full_to_short(filename), str(e))
			logging.error("filename: %s, duration: error" % duration_list_err)
			return duration_null  # if_error
		except AssertionError:
			logging.warning(
				"filename: %s, duration: null" % add.full_to_short(filename)
			)
			return duration_null

		logging.info(
			"filename: %s, duration: %s"
			% (add.full_to_short(filename), str(int(duration_null)))
		)

		return duration_null

	def get_codecs(self, filename):
		self.filename = filename

		lst = []

		# ffprobe -v error -show_entries stream=codec_name -of csv=p=0:s=x input.m4v
		cmd: list[str] = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=codec_name",
			"-of",
			"csv=p=0:s=x",
			filename,
		]  # output_format # python 3.9
		ci = "".join(
			[
				current_folder,
				"codecs.nfo"
			])  # path_for_queue

		try:
			p = os.system("cmd /c %s > %s" % (" ".join(cmd), ci))  # cmd /k
			assert bool(p == 0), ""
		except AssertionError:
			return lst
		else:
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

						# print(lst) #['h264', 'aac']

			if os.path.exists(ci):
				os.remove(ci)

		try:
			assert bool(len(lst) == 2), ""
		except AssertionError:
			if len(lst) > 2:
				logging.info(
					"@lst filename:%s, is_codecs: %s"
					% (add.full_to_short(filename), str(",".join(lst[2:])))
				)  # str(lst[2:])
				# print(""@lst filename:%s, is_codecs: %s" % (filename, str(",".join(lst[2:])))) # debug
				codecs_filter = lst[0:2]
				lst = codecs_filter
			elif len(lst) == 1:
				logging.info(
					"@lst filename:%s, some_codecs: %s"
					% (add.full_to_short(filename), str(lst[-1]))
				)  # print("@lst filename:%s, some_codecs: %s" % (filename, str(lst[-1]))) # debug
			elif len(lst) == 0:
				logging.info(
					"@lst filename:%s, no_codecs" % add.full_to_short(filename)
				)  # print("@lst filename:%s, no_codecs" % filename) # debug

		return lst

	def __del__(self):
		print(
			Style.BRIGHT + Fore.WHITE + "%s удалён" % str(self.__class__.__name__)
		)  # del_class


vp = VideoProject()


# @procedures
def hms(seconds: int = 0):
	try:
		h, m, s = (
			seconds // 3600, seconds % 3600 // 60, seconds % 3600 % 60
		)

		assert all((h, m, s)), f"Нет какой-то величины времени @hms/{h}/{m}/{s}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Нет какой-то величины времени @hms/%d" % seconds)
		raise err
	except BaseException as e:  # if_error
		h = m = s = 0
		h_m_s_err = (seconds, str(e))
		logging.error("Нет какой-то величины времени @hms/%d [%s]" % h_m_s_err)

	try:
		ms_time = (lambda hh, mm, ss: (hh * 3600) + (mm * 60) + ss)(h, m, s)  # ms
		# hh:mm:ss # '{:02d} час. {:02d} мин. {:02d} сек.'.format(h, m, s) # hh mm ss
		# ms_time = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
	except:
		ms_time = 0  # ms_time = str(ms_time)

	return str(ms_time)


def width_height_profile_level(filename: str = "", ffmpeg: bool = True):
	"""D:\\Multimedia\\Video\\Serials_conv\\Agatha_Christies_Marple\\Agatha_Christies_Marple_01s01e.mp4"""
	w = h = ch = p = l = length = codecs = None

	"""
	setup_dict: dict = {}

	setup_dict["width"] = 640
	setup_dict["profile"] = "main"
	setup_dict["level"] = 30

	setup_dict["cv"] = "libx264"
	setup_dict["ca"] = "aac"
	"""

	try:
		w, h, ch = vp.width_and_height(filename)
		assert all((w, h)), ""
	except AssertionError:
		w, h, ch = 0, 0, False
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "%s" % str(e))  # error
		w, h, ch = 0, 0, False
	finally:
		if all(
			(
				any((w, h)),
				ch
			)
		):
			logging.info("@w @h @ch %s" % str((filename, w, h, ch)))

	try:
		p, l = vp.get_profile_and_level(filename)
		assert all((p, l)), ""
	except AssertionError:
		p = l = ""
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "%s" % str(e))  # error
		p = l = ""
	finally:
		if any(
			(
				p,
				l
			)
		):
			logging.info("@p @l %s" % str((filename, p, l)))

	try:
		length = vp.get_length(filename)
		assert length, ""
	except AssertionError:
		length = -1
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "%s" % str(e))  # error
		length = -1
	finally:
		if abs(length) == length:
			logging.info("@length %s" % str(length))

	try:
		codecs = vp.get_codecs(filename)
		assert codecs, ""
	except AssertionError:
		codecs = []
	except BaseException as e:
		print(Style.BRIGHT + Fore.RED + "%s" % str(e))  # error
		codecs = []
	finally:
		codecs = str(",".join(codecs))
		logging.info("@codecs %s" % codecs)

	# del vp # clear_mem # debug

	try:
		# is_scale = (w > setup_dict["width"]) # 640
		is_scale = bool(w > 640)
	except BaseException:
		is_scale = False
	finally:
		logging.info("@is_scale %s" % str((filename, is_scale)))

	try:
		# is_profile = (not setup_dict["profile"] in p.lower()) # "main"
		is_profile = bool(not "main" in p.lower())
	except BaseException:
		is_profile = False
	finally:
		logging.info("@is_profile %s" % str((filename, is_profile)))

	try:
		# is_level = (int(l) > setup_dict["level"]) # 30
		is_level = bool(int(l) > 30)
	except BaseException:
		is_level = False
	finally:
		logging.info("@is_level %s" % str((filename, is_level)))

	is_optimal = []

	# is_optimal.append({"scale": is_scale, "profile": is_profile, "level": is_level}) # status

	pr_le_sc: list[bool] = [
		is_profile,
		is_level,
		is_scale
	]  # profile / level / scale # python 3.9

	cmd_line = []

	if ffmpeg:
		init_ffmpeg = " ".join(
			[
				"cmd /c",
				"".join([
					path_for_queue,
					"ffmpeg.exe"
				])
			])  # cmd /k
		cmd_line.append(init_ffmpeg)

		cmd_line.append('-hide_banner -y -i "%s"' % filename)
		cmd_line.append("-map_metadata -1")

		cmd_line.append("-preset medium")  # debug_speed

		if (
			pr_le_sc.count(True) != 3
		):  # some_optimized
			cmd_line.append("-threads 2 -c:v %s" % "libx264")  # video_optimize
		elif (
			pr_le_sc.count(True) == 3
		):  # all_optimized
			cmd_line.append("-threads 2 -c:v copy")  # video_copy
	else:
		init_ffplay = " ".join(
			[
				"cmd /c",
				"".join(
					[
						path_for_queue,
						"ffplay.exe"
					])
			])  # cmd /k
		cmd_line.append(init_ffplay)

	nw, nh = 0, 0
	np = nl = ""

	w, h = map(int, (w, h))

	# if not isinstance(w, int):
	# w = int(w)

	# if not isinstance(h, int):
	# h = int(h)

	"""
	w0 - текущая ширина в пикселях, # 1600
	h0 - текущая высота в пикселях, # 900
	w1 - новая ширина в пикселях, # 640
	h1 - новая высота в пикселях. # 360

	w1 = (w0 * h1) / h0 # формула для вычисления новой ширины, если задана новая высота
	h1 = (h0 * w1) / w0 # формула для вычисления новой высоты, если задана новая ширина
	"""

	def ar_calc(h, w, nw=640) -> tuple:  # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
		"""720x406 => (406 / 720) * 640 = 360,8888888888889"""

		ac, is_clc = 0, False

		# pass_1_of_2(if_default_some_null)
		try:
			assert all((w, h)), ""  # if_owidth_or_oheight_is_null
		except AssertionError:
			nw = ac = 0
			return (nw, ac)

		# pass_2_of_2(if_need_optimize)
		try:
			assert bool(w > nw), ""
		except AssertionError:
			nw, ac = w, h  # set_default
			logging.warning(
				"@ar_calc value is normal [%s]" % "x".join(
					map(str, [nw, ac]))
			)
		else:
			try:
				ac = (h / w) * nw  # calc_height(float)
				assert bool(int(ac) % 2 == 0), ""
			except AssertionError:  # if_not_div_2
				is_clc = True
				ac = int(ac)
				ac -= 1
				logging.warning("@ar_calc calc height [%s]" % str(ac))
			except BaseException as e:  # if_error
				nw = ac = 0
				logging.error("@ar_calc error: %s" % str(e))
			else:
				if all(
					(
						ac,
						h,
						ac != h
					)
				):
					is_clc = True

			try:
				assert isinstance(ac, int), ""  # height(int)
			except AssertionError:  # if_not_int
				is_clc = True
				ac = int(ac)
				logging.warning("@ar_calc converted height float to int %s" % str(ac))

			try:
				assert bool(is_clc == True), ""
			except AssertionError:
				logging.warning("@is_clc not changed width and height")
			else:
				logging.info("@is_clc changed width and height")

		return (nw, ac)

	np = nl = ""

	if is_scale:

		# additional(calc)
		try:
			tst_width, tst_height = ar_calc(h, w, 640)
		except:
			tst_width = tst_height = 0
		else:
			width, height = tst_width, tst_height

		try:
			ar_calc_status = "x".join(
				map(str, [width, height])
			)
			assert ar_calc_status, ""
		except AssertionError:
			logging.warning(
				"@ar_calc_status some status is null, current: %s" % filename
			)
		except BaseException as e:
			ar_calc_status_err = (str(e), filename)
			logging.error("@ar_calc_status error: %s, current: %s" % ar_calc_status_err)
		else:
			logging.info("@ar_calc/file %s" % ";".join(
				[
					ar_calc_status,
					filename
				])
			)

		nw, nh = width, height

		changed = bool(w > 640)  # diff_width

		if any(
			(
				nw != w,
				nh != h
			)
		):
			if not {"width": [nw, w], "height": [nh, h]} in is_optimal:
				is_optimal.append(
					{"width": [nw, w], "height": [nh, h]}
				)  # is_optimal.append({"width": [640, w], "height": [second, h]})

		if changed:
			cmd_line.append('-vf "scale=%s:%s"' % (nw, nh))
	elif not ffmpeg:
		nw, nh = w, h
		cmd_line.append('-vf "scale=%s:%s"' % (nw, nh))

	if all(
		(
			is_profile,
			ffmpeg
		)
	):
		if not {"profile": ["main", p]} in is_optimal:
			is_optimal.append({"profile": ["main", p]})

		np = "main"

		cmd_line.append("-profile:v %s" % np)

	if all(
		(
			is_level,
			ffmpeg
		)
	):
		if not {"level": ["30", l]} in is_optimal:
			is_optimal.append({"level": ["30", l]})

		nl = str(30)

		cmd_line.append("-level %s" % nl)

	# if all((not year_regex.findall(filename), ffmpeg)):
	# cmd_line.append("-movflags faststart") # seek(0)

	if ffmpeg:
		if (
			pr_le_sc.count(True) != 3
		):  # some_optimized
			cmd_line.append(
				'-threads 2 -c:a %s -af "dynaudnorm"' % "aac"
			)  # sound_stabilize # ffmpeg release?
		elif (
			pr_le_sc.count(True) == 3
		):  # all_optimized
			cmd_line.append("-threads 2 -c:a copy")  # sound_copy

		project_file = "".join(
			[
				path_to_done,
				filename.split("\\")[-1]
			])
		cmd_line.append('"%s"' % project_file)  # ffmpeg
	else:
		cmd_line.append('"%s"' % filename)  # ffplay

	# @ffmpeg/@ffplay
	cmd_status: list[str] = [
		cl.strip()
		for cl in filter(
			lambda x: any(("scale" in x, "profile" in x, "level" in x)), tuple(cmd_line)
		)
	]  # python 3.9
	cmd = " ".join(cmd_line) if cmd_status else ""

	try:
		assert all((nw, nh)), ""
	except AssertionError:
		nw, nh = w, h  # default

	if (
		cmd 
		and all((nw, nh))
	):  # all((nw, nh, p, l))
		# logging.info(
		# "filename: %s, width/height/profile/level/length/codecs/cmd: %s" % (
		# filename, "x".join(map(str, [nw, nh, p, l, length, codecs, cmd]))
		# ) # ffmpeg
		logging.info(
			"filename: %s, width/height: %s, length: %s, codecs: %s, cmd: %s"
			% (
				add.full_to_short(filename),
				"x".join(
					map(str, [nw, nh, p, l, length, codecs, cmd])),
			)
		)  # ffplay

	# 576/320/high/21/[{'profile': 'main'}]
	# print(filename, w, h, p, l, length, codecs, str(is_optimal), sep="\t", end="\n")

	return (filename, w, h, p, l, length, codecs, str(is_optimal), cmd)


def walk(dr: str = "", files_template: str = ""):  # docstring(description)  # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	"""Рекурсивный поиск файлов в пути"""

	# -- default --
	if not files_template:
		return None
	else:
		ext_regex = files_template

	# check_and_test_this_block
	try:
		for name in os.listdir(dr):
			path = os.path.join(dr, name)
			if all(
				(
					os.path.isfile(path),
					ext_regex.findall(path)
				)
			):
				yield path
			else:
				yield from walk(path, ext_regex)

	except BaseException as e:
		return f"Error as {str(e)}"


def one_folder(folder: str = "") -> list:
	"""
	def one_folder(folder, files_template) -> list:  # for_generator_in
	one_folder("c:\\downloads\\new\\", re.compile(r"(?:(zip))$")) # one_folder
	one_folder("c:\\downloads\\new\\", video_regex)
	"""

	files = []

	try:
		files: list[str] = [
			os.path.join(folder, f)
			for f in os.listdir(folder)
			if os.path.exists(os.path.join(folder, f))
		]  # python 3.9

		assert files, ""
	except AssertionError:
		files = []
	except BaseException:
		files = []
	else:
		files = [
			f.strip() for f in files if video_regex.findall(f.split("\\")[-1])
		]  # f.lower().endswith("mp4")

	return files


def sub_folder(folder, files_template) -> list:
	"""
	sub_folder("c:\\downloads\\combine\\", re.compile(r"(?:(zip))$")) # sub_folder
	sub_folder("c:\\downloads\\combine\\", video_regex) # sub_folder
	"""

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
		files = list(sub_folder_to_files())
	except BaseException:
		files = []

	return files


def ms_to_time(ms: int = 0, mn: int = 60) -> int:  # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	try:
		h, m, s = (
			ms // 3600,
			ms % 3600 // 60,
			ms % 3600 % 60
		)
		h_m_s_str = (
			ms, str(h), str(m), str(s)
		)

		assert all((h, m, s)), (
			"Первоначально %d, время %s:%s:%s" % h_m_s_str
		)  # is_assert_debug
	except AssertionError:  # as err:  # if_null
		logging.warning("Первоначально %d, время %s:%s:%s" % h_m_s_str)
		# raise err
	else:
		h_m_s_str = (
			str(h), str(m), str(s)
		)
		
		logging.info("Подсчет времени %s:%s:%s" % h_m_s_str)

	h, m, s = map(int, (h, m, s))

	# ms_time = None

	try:
		ms_time = (lambda hh, mm, ss: (hh * 3600) + (mm * 60) + ss)(h, m, s)
		# hh:mm:ss # '{:02d} час. {:02d} мин. {:02d} сек.'.format(h, m, s) # hh mm ss
		# ms_time = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
	except:
		ms_time = 0  # ms_time = str(ms_time)

	return ms_time


def fspace(src: str = "", dst: str = "") -> bool:  # 11 # hide # *(pos_or_keyw), ... # ..., /(pos) # pyhon 3.8
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
			(
				fsize,
				dsize,
				int(fsize // (dsize / 100)) <= 100
			)
		)  # fspace(ok-True,bad-False)
	except BaseException:
		fspace_status = False  # fspace(error-False)
	finally:
		return fspace_status


def calcProcessTime(starttime, cur_iter, max_iter, filename, /):  # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
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


def avg_calc(s, l, /):  # *(pos_or_keyw), ... # ..., \(pos) # python 3.8
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


# sp ~ try automatic speed from ips(qos)
def calc_download_time(
	filename, fs: int = 0, sp: int = 10
):  # fs = real_fs // (1024 * 2), sp = (10/8) * 1024
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

	if any(
		(
			not fs,
			not sp
		)
	):
		return (filename, 0, 0)

	return (filename, (fs * 1024 / sp) // 60, (fs * 1024 / sp) % 60)  # mm:ss


async def older_or_newbie(days, filename):  # filename(folder) # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	days_ago = datetime.now() - timedelta(days=days)
	filetime = datetime.fromtimestamp(os.path.getctime(filename))

	if filetime < days_ago:  # newbie
		logging.info(
			"@older_or_newbie Файл %s старше(newbie) %d дней" % (filename, days)
		)
		return True  # print("File is more than ag days old") # "Файл старше(newbie) чем двухдневной(ag) давности
	else:  # older
		logging.info(
			"@older_or_newbie Файл %s старее(older) %d дней" % (filename, days)
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


# python 3.9
"""
'farhad_python'.removeprefix('farhad_')

#возвращает python

'farhad_python'.removesuffix('_python')

#возвращает farhad

# merge_dict
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "a": 2}

dict_new = dict1 | dict2 # look_like_merge_set
dict1 |= dict2 # is_update_dict

(List / Dict / Tuple) ~ no need import for use # is_sample # list[str] # dict[str, "str"] # tuple[int]

def find_default(dct: dict[str, int]) -> int
	return dct["test1"]

items = {
	"test1": 1,
	"test2": 2,
	"test3": 3,
}

print(find_default(items))

alpha - new features, beta - no update prerelease, minor - ?
"""

# case(somekey(+func)+value)
"""
# --1--
# result = {'a': lambda x: x * 5, 'b': lambda x: x + 7, 'c': lambda x: x - 2}.get(value, lambda x: x)(x)  # switch_statement(lambda_func/last_is_some_value)
# result = {'a': lambda x: x * 5, 'b': lambda x: x + 7, 'c': lambda x: x - 2}.get(value, lambda x: x)(666)  # 3330 # switch_statement(lambda_func/last_is_some_value)
result = {'a': lambda x: x * 5, 'b': lambda x: x + 7, 'c': lambda x: x - 2}["a"](666)  # 3330

# --2--
# choices = {'a': 1, 'b': 2}
# result = choices.get(key, 'default')
result = choices.get("a", 'default')  # 1
result = choices.get("c", 'default')  # default
"""


if __name__ == "__main__":  # skip_main(debug)

	dt = datetime.now()

	# """
	main_filter = []

	# @day
	try:
		with open(days_ago_base, encoding="utf-8") as dalf:
			filter1: list[str] = [d.strip() for d in filter(lambda x: x, tuple(dalf.readlines()))]  # python 3.9
	except:
		filter1 = []

		# open(days_ago_base, "w", encoding="utf-8").close()
	else:
		if filter1:
			main_filter += filter1

	# if not main_filter:
	# @month
	# '''
	try:
		with open(month_forward_base, encoding="utf-8") as mflf:
			filter2: list[str] = [m.strip() for m in filter(lambda x: x, tuple(mflf.readlines()))]  # python 3.9
	except:
		filter2 = []

		# open(month_forward_base, "w", encoding="utf-8").close()
	else:
		main_filter += filter2

	# '''

	# if not main_filter:
	# @year
	# '''
	try:
		with open(calc_year_base, encoding="utf-8") as cylf:
			filter3: list[str] = [c.strip() for c in filter(lambda x: x, tuple(cylf.readlines()))]  # python 3.9
	except:
		filter3 = []

		# open(calc_year_base, "w", encoding="utf-8").close()
	else:
		main_filter += filter3
	# '''

	main_filter = (
		list(set(main_filter)) if main_filter else []
	)

	try:
		main_regex = re.compile(
			r"(%s)" % "|".join(main_filter), re.M
		)  # multiple_record
	except:
		main_regex = None

	periods = []

	periods.extend(main_filter)

	periods = list(set(periods))
	periods.sort(reverse=False)

	split_periods: list[str] = [
		p.split("_")[0].strip() if len(p.split("_")) > 0 else p.strip() for p in periods
	]  # choice_first_word # python 3.9

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

	pj_dict: dict[str, str] = {
		k: v if k == v else v for k, v in pj_dict.items()
	}  # python 3.9

	with open(period_json, "w", encoding="utf-8") as pjf:
		json.dump(pj_dict, pjf, ensure_ascii=False, indent=4, sort_keys=True)

	# '''
	# @period.lst(scprle) # update_period_list # save
	try:
		assert pj_dict, ""
	except AssertionError:
		logging.warning("no periods")
	else:
		# @period.lst
		with open(period_base, "w", encoding="utf-8") as pbf:
			# pbf.writelines("%s\n" % k for k, _ in pj_dict.items())  # multicommander
			pbf.writelines(
				"%s\\\n" % k for k, _ in pj_dict.items()
			)  # totalcommander(is_short)
	# '''

	files_count = 0

	sm = ln = ag = cntfiles = sf = files_count = len_files = 0  # int
	all_period_dict = folders_filter = {}  # dict
	files = (
		files2
	) = (
		folders
	) = (
		new_folders
	) = old_folders = some_files_filter = period_files = null_period_files = []  # list
	all_period_set = (
		some_folders
	) = some_subfolders = some_files = set()  # ("", "", 0) / folders / files # set

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
					files: list[str] = [
						os.path.join(os.path.join(a, bf), f)
						for f in os.listdir(os.path.join(a, bf))
						if os.path.isfile(os.path.join(os.path.join(a, bf), f))
					]  # subfolders # python 3.9

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
	except:
		ag = 0  # 0
	else:
		logging.info("@files/@folders/@ag %d %d %d" % (len(files), len(folders), ag))
	"""

	# debug
	# exit()

	mx_set = set()
	mx1 = mx2 = mx3 = 0

	try:
		some_files = sorted(some_files, key=os.path.getctime)  # getmtime -> debug(getctime/optimal)
		assert some_files, ""
	except AssertionError:
		logging.warning("@some_file no files")
	else:
		logging.info(";".join(some_files))  # debug(print)
		logging.info("@some_files count: %d" % len(some_files))  # 0?

	strt, cur_iter, max_iter = (
		time(),
		0,
		len(some_files),
	)  # -> sum(some_files_fsizes) # debug
	filter_max_iter = 0
	filter_some_files = []

	sm = ln = ag = 0  # max_ag

	for sf in filter(
		lambda x: os.path.isfile(x), tuple(some_files)
	):  # folder_scan_full
		period_list_filter = []

		try:
			today = datetime.now()
			fdate = os.path.getctime(sf)  # getmtime -> debug(getctime/optimal)
			ndate = datetime.fromtimestamp(fdate)
		except BaseException as e:
			sf_err = (sf, str(e))
			logging.error("@sf not exist folder %s, error: %s" % sf_err)
			continue  # if_winerror

		# file, days, day = r"F:\Videos\Serials\Serials_Conv\100\100_05s01e.mp4", 30, 86400; N = days # 19.07.23 # fullday = 86400
		# ((time() - os.path.getmtime(sf)) / 3600, 24 * days) # (717.9585948366589, 720)
		# (time() - os.path.getmtime(sf)) / 3600 > 24 * days # days_ago = days # older(a<b)
		# (time() - os.path.getmtime(sf)) / 3600 <= 24 * days # days_ago = days # newbie
		# (os.path.getmtime(sf), (time() - day * N)) # (1721398225.5726972, 1721390945.6259742)
		# os.path.getmtime(sf) > (time() - day * N) # day = (24 * 3600) # newbie
		# os.path.getmtime(sf) <= (time() - day * N) # day = (24 * 3600) # older(>0)
		# ((time() - os.path.getmtime(sf)), days * 24 * 3600) # (2584825.8840749264, 2592000)
		# (time() - os.path.getmtime(sf)) > days * 24 * 3600 # older
		# (time() - os.path.getmtime(sf)) <= days * 24 * 3600 # newbie

		max_days_by_year = 366 if today.year % 4 == 0 else 365

		"""
		period_list_filter = [
			(time() - os.path.getmtime(sf)) / 3600 <= 24 * ag,
			os.path.getmtime(sf) > (time() - 86400 * ag),
			(time() - os.path.getmtime(sf)) <= ag * 24 * 3600
		]  # newbie_folders(+avg_filter) # is_max_days
		"""

		days_count = (30, max_days_by_year)  # manual_days_setup(range_by_days_by_default/range_by_days2) # 

		# @older_or_newbie # days=ag ~ avg(+time) # days=max_days_by_year ~ year(+time)
		try:
			oon = asyncio.run(
				older_or_newbie(days=days_count[0], filename=sf)
			)  # X_days(+time/filter) # True(newbie) / False(older)
			assert oon, ""
		except AssertionError:
			# """
			oon = asyncio.run(
				older_or_newbie(days=days_count[1], filename=sf)
			)  # year(+time/filter) # True(newbie) / False(older) # debug(skip_older)
			logging.warning(
				"@oon try %d to %d days filter file, current: %s" % (days_count[0], days_count[1], sf.split("\\")[-1])
			)  # debug(skip_older)
			# """
			period_list_filter = [oon]  # [False]
		except BaseException as e:
			logging.error("@oon error: %s, current: %s" % (str(e), sf.split("\\")[-1]))
			period_list_filter = [False]  # debug(is_error_by_older)
		else:
			logging.info("@oon %d days filter file, current: %s" % (days_count[0], sf.split("\\")[-1]))
			period_list_filter = [oon]

		oon_status = (
			"@oon newbie file, current: %s" % sf.split("\\")[-1]
			if oon
			else "@oon older file, current: %s" % sf.split("\\")[-1]
		)
		logging.info("%s" % oon_status)

		if period_list_filter.count(True) > 0:  # newbie
			# filter_max_iter += 1

			try:
				assert bool(sf.strip() in period_files), ""
			except AssertionError:
				period_files.append(sf.strip())
			else:
				logging.info("@sf/@filter_some_files %s" % sf)
		elif period_list_filter.count(True) == 0:  # older
			try:
				assert bool(sf.strip() in null_period_files), ""
			except AssertionError:
				null_period_files.append(sf.strip())
			else:
				logging.info("@sf/@null_period_files %s" % sf)
			# logging.info("@period_list_filter skip files %s" % sf)
			# continue

		try:
			fn, hhmm, ss = calc_download_time(sf, fs=os.path.getsize(sf), sp=10)
		except BaseException as e:
			calc_download_time_error = (str(e), sf)
			logging.error(
				"@calc_download_time error %s, current: %s" % calc_download_time_error
			)
		else:
			logging.info(
				"@calc_download_time current: %s, time: %s" % (fn, ":".join(
					[
						hhmm,
						ss
					]))
			)

	else:
		some_files = (
			period_files if period_files else null_period_files
		)  # newbie -> older

		max_iter = len(some_files)  # debug

	try:
		assert bool(all((max_iter, some_files))), ""
	except AssertionError:  # if_null(no_count/no_files)
		exit()

	# debug
	# exit()

	for f in filter(lambda x: os.path.exists(x), tuple(some_files)):

		logging.info("start %s file" % f)  # debug(print)

		# fn, w, h, p, l, length, codecs, i_o, c = width_height_profile_level(filename=f)

		try:
			fn, w, h, p, l, length, codecs, _, c = width_height_profile_level(
				filename=f, ffmpeg=True
			)  # ffmpeg
			assert all((fn, w, h, p, l, length, codecs, c)), ""
		except AssertionError:
			logging.warning("@width_height_profile_level filename: %s [ffmpeg]" % f)
			continue
		except BaseException as e:
			fn_w_h_p_l_length_codecs_c_err = (f, str(e))
			logging.error(
				"@width_height_profile_level filename: %s, error: %s [ffmpeg]"
				% fn_w_h_p_l_length_codecs_c_err
			)
			continue
		else:
			logging.info("@width_height_profile_level filename: %s [ffmpeg]" % f)

			if c:  # with_cmd(new)
				fcd[f.strip()] = c  # add_if_ffmpeg(not_optimized) # ffmpeg

				print(
					"->".join(
						[
							f.split("\\")[-1],
							c
						]),
					str(
						{
							"width": w,
							"height": h,
							"profile": p,
							"level": l,
							"duration": length,
							"codecs": codecs,
						}
					),
					sep="\t",
					end="\n",
				)  # str(i_o)

				param = (f, w, h, p, l, length, codecs, c)
				logging.info("@fcd %s [with_cmd]" % str(param))

			elif not c:  # no_cmd(last)
				try:
					fn, w, h, p, l, length, codecs, _, c = width_height_profile_level(
						filename=f, ffmpeg=False
					)
					assert all((fn, w, h, p, l, length, codecs, c)), ""
				except AssertionError:
					logging.error(
						"@width_height_profile_level filename: %s [ffplay]" % f
					)
					continue
				except BaseException as e:
					fn_w_h_p_l_length_codes_c_err2 = (f, str(e))
					logging.error(
						"@width_height_profile_level filename: %s, error: %s [ffplay]"
						% fn_w_h_p_l_length_codes_c_err2
					)
					continue
				else:
					logging.info(
						"@width_height_profile_level filename: %s [ffplay]" % f
					)

					fcd[f.strip()] = c  # add_if_ffplay(optimized) # ffmpeg -> ffplay

					print(
						"=>".join(
							[
								f.split("\\")[-1],
								c
							]),
						str(
							{
								"width": w,
								"height": h,
								"duration": length,
								"codecs": codecs,
							}
						),
						sep="\t",
						end="\n",
					)  # p, l, str(i_o)

					param = (f, w, h, length, codecs, c)
					logging.info("@fcd %s [no_cmd]" % str(param))

		logging.info("end %s file" % f)  # debug(print)

	fcd_time = []

	logging.info("@fcd count: %d" % len(fcd))

	for k, _ in fcd.items():
		try:
			assert os.path.exists(k), ""
		except AssertionError:  # is_null
			logging.warning("job %s not exists" % k)
			continue
		except BaseException:  # if_error
			logging.error("job %s error" % k)
			continue
		else:
			fcd_time.append((k, os.path.getctime(k)))  # getmtime -> debug(getctime/optimal)

	fcd_sorted = sorted(fcd_time, key=lambda fcd_time: fcd_time[-1])

	fcd_dict_new: dict[str, float] = {
		k: v for k, v in fcd.items() for fn, mt in fcd_sorted if k == fn
	}  # python 3.9

	if all(
		(
			fcd_dict_new,
			len(fcd) == len(fcd_dict_new)
		)
	):
		fcd |= fcd_dict_new  # python 3.9
		# fcd.update(fcd_dict_new) 
		# fcd_new = {**fcd, **fcd_dict_new}
	# """

	fcd_old: dict = {}

	# pass_2_of_2
	# """
	# "E:\\Multimedia\\Video\\Serials_Europe\\Medium_Rus\\Medium_02s03e.mp4": "cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i \"E:\\Multimedia\\Video\\Serials_Europe\\Medium_Rus\\Medium_02s03e.mp4\" -map_metadata -1 -preset medium -threads 2 -c:v libx264 -vf \"scale=640:360.0\" -profile:v main -level 30 -movflags faststart -threads 2 -c:a aac -af \"dynaudnorm\" \"c:\\downloads\\list\\Medium_02s03e.mp4\"",
	if fcd:
		with open(fcd_base, "w", encoding="utf-8") as fjf:
			json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=True)

		fcd_old = fcd

		# @scprle.cmd
		with open(cmd_list, "w", encoding="utf-8") as clf:
			clf.writelines("%s\n" % v for _, v in fcd.items())  # multicommander
			# clf.writelines("%s\\\n" % v for _, v in fcd.items()) # totalcommander

		fcd: dict[str, str] = {
			k: v for k, v in fcd.items() if "ffmpeg" in v.lower()
		}  # python 3.9

		for k, _ in fcd_old.items():
			if k not in [*fcd] and os.path.exists(k.replace(k.split(".")[-1], "cmd")):
				os.remove(k.replace(k.split(".")[-1], "cmd"))

		a, cnt, last_file = len(fcd), 0, ""
		strt, cur_iter, max_iter = time(), 0, len(fcd)
		fcd_set = ms_set = te_set = set()

		t = Timer(max_iter)

		date1 = datetime.now()

		# '''
		# short_files
		short_list: list[str] = list(
			set(
				[crop_filename_regex.sub("", k.split("\\")[-1]).strip() for k, _ in fcd.items()]
			)
		)  # some_jobs # python 3.9
		short_list.sort()

		# @fcd.txt
		with open(combine_base, "w", encoding="utf-8") as cbf:  # fcd.txt
			# cbf.writelines("%s\n" % sl for sl in filter(lambda x: len(x) > 1, tuple(short_list)))  # multicommander(is_short)
			cbf.writelines(
				"%s\\\n" % sl for sl in filter(lambda x: len(x) > 1, tuple(short_list))
			)  # totalcommander(is_short)
		# '''

		sl_regex = re.compile(r"(\(|_).*\..*", re.I)
		# some_files = [
		# os.path.join(os.getcwd(), f) for f in os.listdir(os.getcwd())
		# ] # debug
		file_and_time = sorted(
			[(k.split("\\")[-1].strip(), os.path.getctime(k)) for k, _ in fcd.items()],
			key=lambda some_files: some_files[1],
		)  # getmtime -> debug(getctime/optimal)
		short_list2: list[str] = list(
			set(
				[
					sl_regex.sub("", f.strip())
					if not "_Rus" in sl_regex.sub("", f.strip())
					else sl_regex.sub("", f.strip()).replace("_Rus", "")
					for f, _, _ in file_and_time
				]
			)
		)  # python 3.9

		# @fcd_.txt
		with open(combine_base2, "w", encoding="utf-8") as cbf2:  # fcd_.txt
			cbf2.writelines(
				"%s\n" % sl for sl in filter(lambda x: len(x) > 1, tuple(short_list2))
			)  # multicommander(is_short)
			# cbf2.writelines("%s\\\n" % sl2 for sl2 in filter(lambda x: len(x) > 1, tuple(short_list2)))  # totalcommander(is_short)

		for k, v in fcd.items():  # {filename: cmd}
			try:
				assert os.path.exists(k), ""
			except AssertionError:
				logging.warning("file %s not exists" % k)
			except BaseException as e:
				fcd_err = (k, str(e))
				logging.error("error in file %s [%s]" % fcd_err)

			last_file = k

			if not k in fcd_set:
				fcd_set.add(k)
			else:
				continue

			# sleep(1) # 0.05
			cur_iter += 1

			date2 = datetime.now()

			try:
				sleep(60 - time() + strt)  # pause_for_debug
			except BaseException:
				sleep(0.05)

			"""
			s = "c:\\downloads\\mytemp\\downloads.txt"

			>>> "\\".join(s.split("\\")[::-1]) # 'downloads.txt\\mytemp\\downloads\\c:  # reverse_path
			>>> s.split("\\")[-1::] # ['downloads.txt'] # only_short_name
			>>> "\\".join(s.split("\\")[:-1:]) # 'c:\\downloads\\mytemp'	# only_folder			
			"""

			# if os.path.exists(k.replace(k.split(".")[-1], "cmd")):  # clear_old_cmd
			# os.remove(k.replace(k.split(".")[-1], "cmd"))

			# @save_on_src
			if not os.path.exists(k.replace(k.split(".")[-1], "cmd")):
				with open(
					k.replace(k.split(".")[-1], "cmd"), "w", encoding="utf-8"
				) as mcf:  # save_new_cmd(is_one_line)
					mcf.writelines("%s\n" % v)  # multicommander(str)
					# mcf.writelines("%s\\\n" % v) # totalcommander(str)

			telapsed, tleft, etime, current = calcProcessTime(
				strt, cur_iter, max_iter, add.full_to_short(k)
			)  # prstime
			# print("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % (sec_to_time(telapsed), sec_to_time(tleft), etime, add.full_to_short(current))) # sec_to_time
			# logging.info("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % (sec_to_time(telapsed), sec_to_time(tleft), etime, add.full_to_short(current)))

			try:
				sleep(60 - time() + strt)  # pause_for_debug
			except BaseException:
				sleep(0.05)

			try:
				assert bool(t.remains(cur_iter) in te_set), ""
			except AssertionError:
				prstime = (t.remains(cur_iter), etime, add.full_to_short(k))

				try:
					te_set.add(prstime[0])  # t.remains(cur_iter)
				except BaseException as e:
					te_str = (str(e), k)
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
				te_str = (str(e2), k)
				logging.error("@te_str error: %s, filename: %s" % te_str)
			else:
				prstime = (t.remains(cur_iter), etime, add.full_to_short(k))

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
		else:
			logging.info(
				"@some_dict time_end: %s, current: %s"
				% (str(datetime.now()), last_file)
			)

		with open(fcd_base, "w", encoding="utf-8") as fjf:
			json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=True)
	# """

	fcd_list = []

	try:
		new_list: list[str] = list(
			set(
				[
					"".join(
						[
							crop_filename_regex.sub(
								"", fv.split(" ")[-1].split("\\")[-1]
							),
							"_Rus",
						])
					if "Rus" in fv
					else crop_filename_regex.sub("", fv.split(" ")[-1].split("\\")[-1])
					for fv in filter(lambda x: "ffmpeg" in x, tuple(fcd.values()))
				]
			)
		)  # only_ffmpeg(not_optimized) # python 3.9
	except:
		new_list = []
	else:
		fcd_list += new_list
		logging.info("@new_list count: %d" % len(new_list))  # one_record

	logging.info("@fcd_list lines: %s" % ";".join(fcd_list))  # merge_records

	# seg_filter = list(set(seg2) ^ set(seg1)) # different(two_list) # [1, 3, 4, 6] # type1
	# seg_filter = list(set(seg2) & set(seg1)) # unique(two_list) # [2] # type2
	# seg_filter = list(set(seg1) - set(seg2)) # stay_different(only_first/clear_unique/one_list) # [1, 3] # type3

	# logging.info("string1: %s, string2: %s" % (";".join(ready_list), ";".join(new_list)))

	# @fcd.lst
	with open(fcd_lst, "w", encoding="utf-8") as flf:
		flf.writelines("%s\n" % fl for fl in fcd_list)  # multicommander
		# flf.writelines("%s\\\n" % fl for fl in fcd_list) # totalcommander

	end = time()

	finish = int(abs(end - start))  # in_seconds
	finish_ms = finish * 1000  # in_ms

	try:
		assert bool(finish // 3600 > 0), ""
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
				"scprle.py run, time: %d ms, calc_time: %s, count: %d, time_per_file_list: %s"
				% (
					finish_ms,
					finish_min,
					job_count,
					";".join(
						[
							str(job_count / ms_to_time(finish)),
							str(ms_to_time(finish) / job_count),
						]),
				)
			)
		assert all((finish, job_count)), ""
	except BaseException as e:
		logging.error("@job_count error: %s" % str(e))
	except AssertionError:
		logging.warning(
			"@finish/@job_count %s" % ", ".join(
				map(str, (finish, job_count)))
		)
	else:
		logging.info("@finish/@job_count %s" % ", ".join(
			map(str, (finish, job_count)))
		)

	sizes_dict: dict = {}

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
			fsizes_lst: list[tuple] = [
				(os.path.getsize(log_file) // (1024**i), sizes_dict[i])
				for i in range(1, 4)
				if os.path.getsize(log_file) // (1024**i) > 0
			]  # python 3.9
			logging.info("@dsize logging size: %s" % str(fsizes_lst))

		if dsize:
			fsizes_lst: list[tuple] = [
				(dsize // (1024**i), sizes_dict[i])
				for i in range(1, 4)
				if dsize // (1024**i) > 0
			]  # python 3.9
			logging.info("@dsize logging dsize: %s" % str(fsizes_lst))

	dt = datetime.now()

	no_ms = str(dt).split(".")[0]

	sound_notify(f"@finish {no_ms}")
	logging.info(f"@finish {no_ms}")

	# '''
	# dt.hour < mytime["sleeptime"][1] and dt.weekday() <= mytime["weekindex"] # midnight-7am
	if any(
		(
			dt.hour >= mytime["dnd"][0],
			all((dt.hour < mytime["dnd"][1], dt.weekday() >= 0))
		)
	):  # 10pm-7am
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
		)  # shutdown(15min) (midnight - 7am) + filter_weekday # start_after # if_updates

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
		ext = "".join(
			[
				".",
				__file__.split(".")[-1]
			])
	except BaseException:
		ext = ""

	"""
	try:
		# script_path = os.path.dirname(os.path.realpath(__file__)).lower()
		filename = "\\".join(
			[
				script_path,
				__file__.replace(ext, ".glob")
			])  # ?
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
