# -*- coding: utf-8 -*-

# --- semi_automatic(debug) ---

# Полуавтоматическое форматрирование файлов для разделения(trim) и сбора(concat)
# Файл с разрезами и одной частью если небольшой("оптимально"" для любого компьютера)
# почистить основые примеры, чтобы не было мусора в описании и коде

# from itertools import product  # use_more_1for
# from math import sqrt
# from os import getcwd # cpu_count  # текущая папка # cpu_count
# import gevent.monkey # pip install --user gevent # is_async(debug)
# import psutil
# import tomllib # look like json - parsing TOML (Python 3.11)
from psutil import cpu_count  # viirtual_memory # pip install --user psutil
from subprocess import run  # TimeoutExpired, check_output, Popen, call, PIPE, STDOUT # Работа с процессами # console shell=["True", "False"]
from threading import Semaphore  # Thread, Barrier # работа с потоками # mutli_async
import asyncio  # TaskGroup(Python 3.11+)
import jmespath #  search # compile  # pip install --user -U jmespath # debug
import json  # JSON (словарь)
import logging  # журналирование и отладка
import os  # система
import pyttsx3
import re  # реуглярные выражения/regular expression # .*(\?|$)
import sys

# pip install --user bpython (interactive_color_terminal) # launch?
# pip install --user youtube-dl # youtube-dl --hls-prefer-native "http://host/folder/file.m3u8" # youtube-dl -o "%%(title)s.%%(resolution)s.%%(ext)s" --all-formats "https://v.redd.it/8f063bzbdx621/HLSPlaylist.m3u8"

from datetime import (
	datetime,
	timedelta,
)  # дата и время

from shutil import (
	disk_usage,
	move,
)  # copy # файлы # usage(total=16388190208, used=16144154624, free=244035584)

from time import (
	time,
	sleep,
)

# Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.
# Back, Cursor # Fore.color, Back.color # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE # pip install --user colorama
from colorama import (
	Fore,
	Style,
	init,
)

# python -> exe(+ico) # pip install --user -U pyinstaller # +icon.ico
# pyinstaller -F -i "icon\icon.ico" video_trimmer2.py # dist\video_trimmer2.exe

# pip install --user bpython (interactive_color_terminal) # launch?

# python -m trace --trace video_trimmer2.py

# vosk (+Python/Subtitle Edit"Video") # video(audio)_to_text(is_subtitle)

__version__ = "0.1"
__author__ = "Sergey Ibragimov"

# ffmpeg -i blah.vtt blah.srt # manual_convert_subtitle

# debug_moules
# exit()

# mklink /h videotrimmer.py video_trimmer2.py

# qos ~ 1 * 1024 = 1mb, speed ~ (5/8) * 1024 = 1280 kb/s

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
	[
		basedir.split("\\")[0],
		"\\"
	])  # "".join(script_path[0:5]) if script_path else "".join(os.getcwd()[0:5])

# logging(start)
log_base = "%s\\trimmer_job.json" % script_path  # main_debug(json)
log_file = "%s\\trim.log" % script_path  # main_debug(logging)

# --- path's ---
path_for_queue = r"d:\\downloads\\mytemp\\"
path_to_done = "%sdownloads\\list\\" % dletter  # "c:\\downloads\\" # ready_folder
path_for_folder1 = "".join(
	[
		os.getcwd(),
		"\\"
	])

cmd_list = "%s\\video_trimmer2.cmd" % script_path  # command_line_for_trim
sequence_list = "%s\\sequence_list.cmd" % script_path  # mp4
sequence_list2 = "%s\\sequence_list2.cmd" % script_path  # m3u8
sequence_list3 = "%s\\sequence_list3.cmd" % script_path  # seg
# sequence_list4 = "%s\\sequence_list4.cmd" % script_path  # paded

# list(json)_by_period
all_period_json = "%s\\all_period.json" % script_path  # ?
calc_year_base = "%s\\calc_year.lst" % script_path
combine_base = "%s\\fcd.txt" % script_path
combine_base2 = "%s\\fcd_.txt" % script_path  # regex_filter((\(|_).*\..*)
days_ago_base = "%s\\days_ago.lst" % script_path
days_ago_list = "%s\\days_ago.txt" % script_path  # ?
filename_length_json = "%s\\filename_length.json" % script_path
month_forward_base = "%s\\month_forward.lst" % script_path
period_base = "%s\\period.lst" % script_path  # combine_base
period_json = "%s\\period.json" % script_path
current_json = "%s\\current.json" % script_path
current_base = "%s\\current.lst" % script_path
displayar_base = "%s\\dar.json" % script_path
segments_base = "%s\\segments.json" % script_path

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
list_files.append(month_forward_base)
list_files.append(period_base)
list_files.append(current_base)

for cmd_files in filter(lambda x: os.path.exists(x), tuple(list_files)):
	os.remove(cmd_files)
"""

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
crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)", re.I)
file_regex = re.compile(r"([0-9]f_.*)", re.M)
space_regex = re.compile(r"[\s]{2,}")
cmd_whitespace = re.compile(
	r"[\s]{2,}"
)  # text = "hello  world" # space_regex.sub(" ", text)

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

job_count = 0
some_dict = {}

mytime: dict = {
	"jobtime": [9, 18, 5],
	"dinnertime": [12, 14],
	"dnd": [22, 8],
	"sleeptime": [0, 8],
	"anytime": [True],
	"weekindex": 4,
}  # sleep_time_less_hour # debug # weekindex (0 - 4, monday-friday)


class Timer(object):
	def __init__(self, total):
		self.start = datetime.now()  # datetime.datetime.now()
		self.total = total

	def remains(self, done):
		now = datetime.now()
		left = (self.total - done) * (now - self.start) / done
		sec = int(left.total_seconds())
		logging.info("@now/@left/@sec %s" % ";".join(
			map(str, [now, left, sec]))
		)
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
		except:  # if_error
			return item[1]  # use_value(None -> no_value)


def clear_base_and_lists():  # docstring
	"""@clear_log_and_bases"""

	pass

	"""
	create_files = []

	create_files.extend([period_base, cmd_list, filename_length_json]) # log_base # skip_periods # "log_file"

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

# @file_to_m3u8
"""
#EXTM3U
#EXTINF: 0,1x16 (Девочки Гилмор). jazorw
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Linux; Android 7.1.2; X96mini Build/NHG47L; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36
http://data05-cdn.datalock.ru/fi2lm/7d2b2f94011f33cd73b7dbf603374c89/7f_GilmoreGirls.S01x16.Star-CrossedLoversAndOtherStrangersrusbyJW.a1.18.08.12.mp4
"""

# ffmpeg -protocol_whitelist file,https,tcp,tls -i master.m3u8 -c copy -bsf:a aac_adtstoasc video.mp4 # ffmpeg m3u8 aac_adtstoasc mp4

"""
g://Concat MP4 files without transcoding to mpeg
Use the h264_mp4toannexb bitstream filter to convert the mp4s (video steam only) into the AnnexB bitstream format

ffmpeg -i input1.mp4 -vcodec copy -bsf:v h264_mp4toannexb -acodec copy part1.ts
# repeat for up to inputN
Concat the files using cat

cat part1.ts part2.ts > parts.ts
Remux the files into a complete mp4

ffmpeg -y -i parts.ts -acodec copy -bsf:a aac_adtstoasc parts.mp4
"""

# --- CPU optimize / debug ---
try:
	assert cpu_count(), ""
except AssertionError:
	unique_semaphore = Semaphore(2)
	# bar = Barrier(2, timeout=15)
else:
	unique_semaphore = Semaphore(cpu_count())
	# bar = Barrier(cpu_count(), timeout=15)

open(sequence_list, "w", encoding="utf-8").close()
open(sequence_list2, "w", encoding="utf-8").close()
open(sequence_list3, "w", encoding="utf-8").close()

# @math


async def calc_number_of_day(
	is_default: bool = True,
	day: int = 0,
	month: int = 0,
	year: int = 0,
	sleep_if: str = "",
	find_c3: int = 0,
	find_c4: int = 0,
) -> tuple:  # 4 # docstring # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	"""@calc_number_of_day"""
	if is_default:
		dt_calc = datetime.now()  # day / month / year

		dt_str = ".".join([str(dt_calc.day), str(dt_calc.month), str(dt_calc.year)])
	elif not is_default:
		dt_str = ".".join([str(day), str(month), str(year)])

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
		print(c1, c2, c3, c4, dt_str, "from def")

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
	]  # python 3.9(-hide/debug)

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
# free_dspace = []
# for i in range(10, 26):
	# free_dspace.append(i/100)
# av = 0
# av = sum(free_dspace) / len(free_dspace)

for dl in range(ord("c"), ord("z") + 1):
	du = "".join(
		[
			str(chr(dl)),
			":\\"
		])

	try:
		optimal_total = int(disk_usage("%s" % du).total) // (1024 ** 3) # 10% free for faster (hdd/ssd)
		optimal_free = int(optimal_total * 0.15)  # 0.10 - 0.20 # 0.15
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

trimer_base = log_base
not_ready_base = "%s\\new_job.json" % script_path # job_cmd
ready_base = "%s\\ready_job.json" % script_path # only_parts

# @pass_1_of_2

# @trimmer_base; load / create(if_error)
try:
	with open(trimer_base, encoding="utf-8") as tbf:
		some_dict = json.load(tbf)
except BaseException:
	some_dict = {}

	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)

try:
	assert some_dict, ""
except:
	some_dict = {}
else:
	some_dict = {
		k: v for k, v in some_dict.items() if os.path.exists(k) and v
	}

# @trimmer_base; create(clear)
"""
some_dict = {}

with open(trimer_base, "w", encoding="utf-8") as tbf:
	json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)
"""


# @oop
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

	"""
	def parse_file(self, filename):  # full_name
		try:
			filename = file_regex.findall(filename)[0] #; print(file_regex.findall(filename), end="\t\n") # short_filename
		except:
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
			parse_list = list(set(
				[(tuple(pt.findall(short_filename)), pt) for pt in parse_template if pt.findall(short_filename)]
			)) # try_unique
		except:
			parse_list = []
		else:
			# parse_list.sort(reverse=False)
			
			print()

			for ps in parse_list:
				try:
					assert ps and parse_list, "" # some_data(tuple) / some_list
				except AssertionError:
					logging.warning("@parse_list template not found for %s" % filename)
					continue
				except BaseException as e:
					parse_list_err = (str(e), filename)
					logging.error("@parse_list error: %s, current: %s" % parse_list_err)
					continue
				else:
					parse_text.append("%s" % str(ps)) # debug_for_join
					logging.info("@parse_text %s for \"%s\"" % (parse_text[-1], filename))

		return (len(parse_template), parse_list, parse_text)
	"""

	def __del__(self):
		print(
			Style.BRIGHT + Fore.WHITE + "%s удалён" % str(self.__class__.__name__)
		)  # delete_class
		# logging.info("%s удалён" % str(self.__class__.__name__))


sequence_set = set()

add = Additional()


class width_height:
	def __init__(self, filename):
		self.filename = filename

	def get_width_height(self, filename, is_calc=False, maxwidth=640):
		global job_count

		self.filename = filename

		is_owidth = 0  # is_change = False

		if not self.filename:
			return None

		# ffprobe -v error -show_entries stream=width,height -of csv=p=0:s=x input.m4v
		cmd_wh: list[str] = [
			"".join(
				[
					path_for_queue,
					"ffprobe.exe"
				]),
			"-v",
			"error",
			"-show_entries",
			"stream=width,height",
			"-of",
			"csv=p=0:s=x",
			self.filename,
		]  # output_format # python 3.9(-hide/debug)
		wi = "".join(
			[
				current_folder,
				"wh.nfo"
			])  # path_for_queue

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
				width, height = int(width_height_str.split("x")[0]), int(
					width_height_str.split("x")[-1]
				)

				# is_owidth = width # debug

				# job_status = ""

				try:
					job_status = (
						"%s" % str((width, height, self.filename, "ok"))
						if width <= maxwidth
						else "%s" % str((width, height, self.filename, "job"))
					)
				except BaseException:
					job_status = ""
				finally:
					if job_status:
						print(
							Style.BRIGHT + Fore.GREEN + "%s" % job_status
						)  # ready_or_new
						logging.info(
							job_status
						)

				try:
					assert all((width > 0, maxwidth > 0, height > 0)), ""
				except AssertionError:
					logging.warning(
						"@width/@maxwidth/@height another value, current: %s"
						% self.filename
					)
				else:
					if all(
						(
							width > maxwidth,
							height,
							width >= height
						)
					):
						print(
							Style.BRIGHT
							+ Fore.YELLOW
							+ "debug [w/h/$file$]: %s" % job_status
						)  # new
						job_count += 1

						logging.info(
							"@width/@maxwidth/@height/@file %s"
							% ";".join(
								map(str, [width, maxwidth, height, self.filename])
							)
						)
					else:  # elif any((width == None, maxwidth == None, height == None)):
						logging.info(
							"@width/@maxwidth/@height some value, current: %s"
							% self.filename
						)
		except BaseException:  # as e
			width, height = 0, 0
			# print("@width/@height/@error current: %s" % add.full_to_short(self.filename))
			print(
				Style.BRIGHT
				+ Fore.RED
				+ "@width/@height/@error current: %s" % self.filename
			)  # error
			logging.error("@width/@height/@error current: %s" % self.filename)

		is_owidth, changed, ar_find = (
			width,
			False,
			(width >= height),
		)  # old_width? / optimized? / width => height -> some_aratio

		def ar_calc(h, w, nw=640) -> tuple:
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
				nw = ac = 0  # nw, ac = w, h  # set_default
				logging.warning(
					"@nw/@ac value is null [%s]" % "x".join(map(str, [nw, ac]))
				)
			else:
				try:
					ac = (h / w) * nw  # calc_height(float)
				except BaseException as e:  # if_error(do_default)
					nw, ac = w, h
					logging.error("@ac error: %s" % str(e))
				else:  # if_ok
					# pass_2_of_2
					try:
						assert isinstance(ac, int), ""  # not_int(auto)
					except AssertionError:
						ac = int(ac)  # float -> int(auto)

					try:
						assert bool(ac % 2 == 0), ""  # mod(auto)
					except AssertionError:
						ac -= 1

					logging.info(
						"@nw/@ac value is calced [%s]" % "x".join(map(str, [nw, ac]))
					)

					if all(
						(
							ac,
							h,
							ac != h
						)
					):
						is_clc = True

				try:
					assert bool(is_clc == True), ""
				except AssertionError:
					logging.warning("@is_clc not changed width and height")
				else:
					logging.info("@is_clc changed width and height")

			return (nw, ac)

		if all(
			(
				is_calc == True,
				width > maxwidth,
				height,
				width >= height,
				ar_find
			)
		):  # True;True;h;w >= h("any" -> 1:1);calc_ar(False-error ar, True-normal ar)

			# additional(calc)
			try:
				tst_width, tst_height = ar_calc(height, width, maxwidth)
				assert all((tst_width, tst_height)), ""
			except AssertionError:  # if_null_no_default
				tst_width = (
					tst_height
				) = 0  # tst_width, tst_height = width, height # if_null_default
				logging.warning("@tst_width/@tst_height is null")
			except BaseException as e:  # if_error_null
				tst_width = tst_height = 0
				logging.error("@tst_width/@tst_height error %s" % str(e))
			else:
				width, height = tst_width, tst_height
				logging.info(
					"@width/@height %s" % "x".join(map(str, [tst_width, tst_height]))
				)

			try:
				ar_calc_status = "x".join(map(str, [width, height]))
				assert ar_calc_status, ""
			except AssertionError:
				logging.warning(
					"@ar_calc_status some status is null, current: %s" % filename
				)
			except BaseException as e:
				ar_calc_status_err = (str(e), filename)
				logging.error(
					"@ar_calc_status error: %s, current: %s" % ar_calc_status_err
				)
			else:
				logging.info("@ar_calc/file %s" % ";".join(
					[
						ar_calc_status,
						filename
					])
				)

			changed = bool(
				is_owidth > maxwidth
			)  # ; print(width, height, changed) # diff_width

			wh_status = (
				"x".join(map(str, [width, height])) + " resized"
				if changed
				else "x".join(map(str, [width, height])) + " no resized"
			)

			if all(
				(
					width,
					height,
					wh_status
				)
			):
				logging.info(
					"@width/@height %s, filename: %s" % (wh_status, self.filename)
				)

				# print(wh_status)

		# return (int(width), int(height), is_owidth != width)
		return (int(width), int(height), changed)  # width <= maxwidth

	def get_profile_and_level(self, filename) -> tuple:
		self.filename = filename

		cmd_pl: list[str] = [
			"".join([path_for_queue, "ffprobe.exe"]),
			"-v",
			"error",
			"-show_entries",
			"stream=profile,level",
			"-of",
			"default=noprint_wrappers=1",
			self.filename,
		]  # output_format # python 3.9(-hide/debug)
		plf = "".join([current_folder, "profile_and_level.nfo"])  # path_for_queue

		try:
			p = os.system(
				"cmd /c %s > %s" % (" ".join(cmd_pl), plf)
			)  # profile=High # level=50
			assert bool(p == 0), ""
		except AssertionError:
			return ("", "")

		pl_list = []

		with open(plf, encoding="utf-8") as plff:
			pl_list = plff.readlines()

		if len(pl_list) > 2:
			pl_list = pl_list[0:2]

		# logging.info(
		# "filename: %s, profile/level: %s"
		# % (add.full_to_short(filename), "x".join([str(pl_list[0]), str(pl_list[-1])]))
		# )
		logging.info(
			"filename: %s, profile/level: %s"
			% (filename, "x".join(map(str, [pl_list[0], pl_list[-1]])))
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
				# logging(";".join(["debug profilelevel", pl_list[0].split("=")[-1].lower().strip(), pl_list[1].split("=")[-1].lower().strip(), filename]))

				return (
					pl_list[0].split("=")[-1].lower().strip(),
					pl_list[1].split("=")[-1].lower().strip(),
				)  # [main,30]

	def get_length(self, filename) -> int:
		self.filename = filename

		cmd_fd: list[str] = [
			"".join([path_for_queue, "ffprobe.exe"]),
			"-v",
			"error",
			"-show_entries",
			"format=duration",
			"-of",
			"compact=p=0:nk=1",
			self.filename,
		]  # output_format # python 3.9(-hide/debug)
		fdi = "".join([current_folder, "duration.nfo"])  # path_for_queue

		duration_list = []

		duration_null = 0

		try:
			p = os.system("cmd /c %s > %s" % (" ".join(cmd_fd), fdi))  # 1|und #type1
			assert bool(p == 0), ""
		except AssertionError:
			return duration_null

		with open(fdi, encoding="utf-8") as fdif:
			duration_list = fdif.readlines()

		if os.path.exists(fdi):
			os.remove(fdi)

		try:
			if "." in duration_list[0] and duration_list:
				return int(duration_list[0].split(".")[0])
		except BaseException:
			return duration_null  # if_null_or_error

		print(
			Style.BRIGHT + Fore.BLUE + "Duration time is %d" % int(duration_null)
		)  # some_duration

		return duration_null

	def length_to_framecount(self, filename, fcnt, hh, mm, ss, is_manual: bool = False):
		h = m = s = 0

		fc: int = 0  # ; ln: int = 0

		try:
			h, m, s = (
				fcnt // 3600, fcnt % 3600 // 60, fcnt % 3600 % 60
			)

			assert all((h, m, s)), "Первоначально %d, время %s:%s:%s, current: %s" % (
				fcnt,
				str(h),
				str(m),
				str(s),
				filename,
			)  # is_assert_debug
		except AssertionError:  # as err:  # if_null
			logging.warning(
				"Первоначально %d, время %s:%s:%s, current: %s"
				% (fcnt, str(h), str(m), str(s), filename)
			)
			# raise err
		except BaseException as e:
			h = m = s = 0
			h_m_s_err = (filename, str(e))
			logging.error("Ошибка подсчета времени, current: %s, error: %s" % h_m_s_err)
		else:
			h_m_s_str = (str(h), str(m), str(s), filename)
			logging.info("Подсчет времени %s:%s:%s, current: %s" % h_m_s_str)

		try:
			h1 = max(h, hh)  # hour
		except BaseException:
			h1 = 0

		try:
			m1 = max(m, mm)  # minute
		except BaseException:
			m1 = 0

		try:
			s1 = max(s, ss)  # second
		except BaseException:
			s1 = 0

		h1, m1, s1 = map(int, (h1, m1, s1))

		try:
			fc = (lambda hr, mn, sc: (hr * 3600) + (mn * 60) + sc)(h1, m1, s1)

			assert fc, ""
		except AssertionError:
			fc = (
				self.get_length(filename) if not fcnt else fcnt
			)  # time_from_file / time_from_arg
			logging.warning("@ln full[semiautomatic] framecount: %d" % fc)
		else:
			logging.info("@ln full framecount: %d" % fc)

		return fc

	def get_codecs(self, filename) -> list:
		lst = []

		self.filename = filename

		# ffprobe -v error -show_entries stream=codec_name -of csv=p=0:s=x input.m4v
		cmd: list[str] = [
			"".join([path_for_queue, "ffprobe.exe"]),
			"-v",
			"error",
			"-show_entries",
			"stream=codec_name",
			"-of",
			"csv=p=0:s=x",
			self.filename,
		]  # output_format # python 3.9(-hide/debug)
		ci = "".join([current_folder, "codecs.nfo"])  # path_for_queue

		try:
			p = os.system("cmd /c %s > %s" % (" ".join(cmd), ci))
			assert bool(p == 0), ""
		except AssertionError:
			return lst
		else:
			if p == 0:

				try:
					with open(ci) as f:
						lst = f.readlines()
				except BaseException:
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
					% (filename, str(",".join(lst[2:])))
				)
				# print("@lst filename:%s, is_codecs: %s" % (filename, str(",".join(lst[2:])))) # debug
				codecs_filter = lst[0:2]
				lst = codecs_filter
			elif len(lst) == 1:
				logging.info(
					"@lst filename:%s, some_codecs: %s" % (filename, str(lst[-1]))
				)  # print("@lst filename:%s, some_codecs: %s" % (filename, str(lst[-1]))) # debug
			elif len(lst) == 0:
				logging.info(
					"@lst filename:%s, no_codecs" % filename
				)  # print("@lst filename:%s, no_codecs" % filename) # debug

		return lst

	def __del__(self):
		print(
			Style.BRIGHT + Fore.WHITE + "%s удалён" % str(self.__class__.__name__)
		)  # delete_class



# '''
def screenshot_cut(slide, framecount, /):  # docstring # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	"""@slide_from_job;	Необходимо изменить -r n. К примеру 1 кадр раз в 4 секунды будет как -r 0.25, а 1 кадр каждые 9 секунд - -r 0.1"""

	try:
		assert slide, ""
	except AssertionError:
		slide = 20

	try:
		assert bool(framecount < 2), ""
	except AssertionError:
		framcecount = 2

	return slide / framecount  # 1 / 4 = 0.25 # 1kadr_v_4sekundy(slide / framecount)


def save_slide(slide, framecount, filename, width, height, /):  # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	"""@save_slide; ffmpeg -hide_banner -y -i input -vf scale=-1:480:flags=lanczos -r 0.25 output_%02d.jpg"""

	try:
		assert slide, ""
	except AssertionError:
		slide = 20

	# filename, slide, framecount = r"D:\Downloads\Temp\Download\Agatha_All_Along\Agatha_All_Along_01s02e.mp4", 20, 2568 # 0,00778816199376947040498442367601 # debug
	try:
		sc = screenshot_cut(slide, framecount)
		assert sc, ""
	except AssertionError:
		logging.warning("@sc can't run screenshot_cut is some null")
		return None
	except BaseException as e:
		logging.error("@sc can't run screenshot_cut error: %s" % str(e))
		return None

	try:
		assert os.path.exists(filename), ""
	except AssertionError:
		fname = filename
	else:
		fname = filename.split("\\")[-1]

	# short_filename = None

	if sc > 0:
		# short_filename = crop_filename_regex.sub("", filename.split("\\")[-1])

		# ffmpeg -hide_banner -y -i input -vf scale=-1:480:flags=lanczos -r 20/2899 -f image2 output_%02d.jpg # old
		# ffmpeg -hide_banner -y -i input -vf scale=-1:480:flags=lanczos -r 0.25 output_%02d.jpg # debug

		init_ffmpeg = " ".join(["cmd /c", "".join([path_for_queue, "ffmpeg.exe"])])
		init_file = " ".join(["-hide_banner", "-y", "-i"])  # hide_banner_and_input_file
		init_file += "".join([" ", '"', filename, '"'])  # full_name
		split_stream = os.path.join(
			path_to_done,
			"".join(
				[
					filename.split("\\")[-1].split(".")[0],
					"".join(["_", "%02d"]),
					"".join([".", "jpg"]),
				]
			),
		)  # 03d -> 02d

		try:
			# init_cmd_convert_video_to_slide
			assert all((width, height, sc, split_stream)), ""
		except AssertionError:
			screenshot_video = []
			logging.warning(
				"@screenshot_video/width/height/sc/split_stream %s"
				% ";".join(map(str, [width, height, sc, split_stream]))
			)
		else:
			screenshot_video: list[str] = [
				init_ffmpeg,
				init_file,
				"-vf",
				"scale=%s:%s:flags=lanczos" % (str(width), str(height)),
				"-r",
				str(sc),
				"".join(['"', split_stream, '"']),
			]  # python 3.9(-hide/debug)

		try:
			assert screenshot_video, ""
		except AssertionError:
			logging.warning("@screenshot_video command is null or read err, current: %s" % filename)
		except BaseException as e:
			screenshot_video_err = (str(e), filename)
			logging.error("@screenshot_video error: %s, current: %s" % screenshot_video_err)
		else:
			if screenshot_video:
				try:
					p = run(" ".join(screenshot_video), shell=True)
					assert bool(p == 0), ""
				except AssertionError:
					logging.warning("@screenshot_video error run, current: %s" % filename)
				except BaseException as e:
					screenshot_video_err = (fname, str(e))
					logging.error(
						"@screenshot_video error: can't save image for %s, error: %s"
						% screenshot_video_err
					)
				else:
					logging.info(
						"@screenshot_video command: %s" % " ".join(screenshot_video)
					)
			else:
				logging.info(
					"@screenshot_video no command, current: %s" % filename
				)
# '''

def one_to_double(cnt, mx: int = 3) -> str:  # debug_by_length  # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	"""a = "0"*3 -> '000'"""

	# cnt_len = len(str(cnt))

	if cnt in range(0, 10):  # 9
		return "".join(["0" * (mx - 1), str(cnt)])  # one
	elif cnt in range(10, 100):  # 99
		return "".join(["0" * (mx - 2), str(cnt)])  # double
	elif cnt in range(100, 1000):  # 999
		return "".join(["0" * (mx - 3), str(cnt)])  # triple
	elif cnt > 999:
		return str(cnt)  # four


# save_last: list[bool] = [] # python 3.9
def calc_parts(
	filename: str = "",
	framecount: int = 0,
	parts: int = 10,
	is_trim: bool = True,
	is_scale: bool = True,
	is_update: bool = False,
	skip_rus: bool = True,
	skip_trim: bool = False,
	ext: str = "mp4",
	is_run: bool = False,
	save_last: list = [False],
) -> list:

	logging.info("start calc_parts %s" % str(datetime.now()))

	try:
		assert os.path.exists(
			filename
		), ""  # video_regex.findall(filename.split("\\")[-1])
	except AssertionError:
		logging.warning("@filename %s not video" % filename)
		return []

	mp4, old = "mp4", filename.split(".")[-1]  # for_job(any)

	try:
		assert bool(mp4 == old), ""
	except AssertionError:
		old = filename.split(".")[-1]
		ext = "".join([".", "mp4"])  # another_ext
	else:
		old = ext = "".join([".", "mp4"])  # default_ext

	logging.info("@old/@ext %s" % ";".join(
		map(str, [old, ext]))
	)

	some_dict = {}

	# @trimmer_base; load / create(if_error)
	try:
		with open(trimer_base, encoding="utf-8") as tbf:
			some_dict = json.load(tbf)
	except BaseException:
		some_dict = {}

		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)

	try:
		assert some_dict, ""
	except:
		some_dict = {}
	else:
		some_dict: dict[str, list] = {
			k: v for k, v in some_dict.items() if os.path.exists(k) and v
		}  # python 3.9(-hide/debug)

	try:
		with open(filename_length_json, encoding="utf-8") as flj:
			fl = json.load(flj)
	except:
		fl = {}

	logging.info(
		"@length(some_dict/fl) %s" % ";".join(map(str, [len(some_dict), len(fl)]))
	)

	wh = width_height(filename)

	try:
		fl = {
			k: v for k, v in fl.items() if os.path.exists(k)
		}  # python 3.9(hide/debug!)

		assert fl, ""
	except AssertionError:  # if_no_exists_files
		logging.warning("@fl no exist files")
	except BaseException as e:
		fl_err = (str(e), filename)
		logging.error("@fl error: %s, current: %s" % fl_err)
	else:
		logging.info("@fl length: %s" % str(len(fl)))

	fc = 0

	hc = mc = sc = 0

	try:
		framecount = wh.get_length(filename)  # ms_to_time(framecount) # 2553 # debug
	except BaseException:
		return []
	else:
		try:
			fc = wh.length_to_framecount(filename, framecount, 0, 0, 0, is_manual=False)
		except:
			fc = 0
		else:
			hc, mc, sc = (
				framecount // 3600,
				framecount % 3600 // 60,
				framecount % 3600 % 60,
			)

	try:
		vbr = (os.path.getsize(filename) * framecount) / (
			(hc * 3600) + (mc * 60) + sc
		)  # ~%d(kBit/s total bitrate)
		vbr -= 128  # dynaudnorm ~ 128(kBit/s video bitrate)
		vbr //= 1024**2
	except BaseException as e:
		vbr, vbr_err = 0, (str(e), filename)
		logging.error("@vbr error: %s, current: %s" % vbr_err)
	else:
		vbr_str = (str(vbr), filename)
		logging.info("@vbr vbr: %s, current: %s" % vbr_str)

	"""
	try:
		vbr2 = os.path.getsize(filename) / framecount  # bitrate = file size / duration # test(572416 / 5820 ~ 0,68-0,87)
	except BaseException as e2:
		vbr2, vbr_err = 0, (str(e2), filename)
		logging.error("@vbr2 error: %s, current: %s" % vbr_err)
	else:
		vbr_str = (str(vbr2), filename)
		logging.info("@vbr2 vbr: %s, current: %s" % vbr_str)
	"""

	logging.info("@fc %d" % fc)

	def_fc = framecount  # ; def_p = parts

	try:
		time_by_cpu = int(cpu_count())  # cpu # min_by_cpu(int) # 2
		assert isinstance(time_by_cpu, int), ""
	except AssertionError:
		time_by_cpu = int(time_by_cpu)
	else:
		logging.info("@time_by_cpu %d" % time_by_cpu)

	parts = tp = ag = 0
	tp_diff: float = 0  # tp_float: float = 0
	tp_list: list = []	

	# need_framecount_convert_to_parts

	# -- default(last) --
	# """
	# def_fc = 4800 / parts ~ 40! # def_fc = 2100 / parts - 35! # def_fc = 3700 / parts - 50!

	parts_list = [def_fc // 60, def_fc % 60]

	parts = (sum(parts_list) // len(parts_list), sum(parts_list))[sum(parts_list) <= 60]

	# logging.info("@part_list/@framecount/@parts/@tp/sparts_list/@filename %s" % ";".join(map(str, (parts_list, def_fc, parts, (def_fc // parts), sum(parts_list), filename))))
	logging.info("@framecount/@parts/@tp/@filename %s" % ";".join(map(str, (def_fc, parts, (def_fc // parts), filename))))

	# debug(calc/+switch_statement)	
	"""
	for i in range(1, 4):
		try:
			parts_result = {
				"1": lambda x: (max(x) % min(x)) if (max(x) % min(x)) > 0 else (max(x) // min(x)), 
				"2": lambda x: abs(x[0] - x[1]),
				"3": lambda x: sum(x) // len(x), 
			}.get(str(i), 0)(parts_list)

			assert parts_result, ""
		except AssertionError:
			parts = def_fc // (60 * time_by_cpu)  # parts_by_seconds(+cpu/div) # no_change
			# parts = def_fc % (60 * time_by_cpu)  # parts_by_seconds(+cpu/mod) # no_change
			tp_list.append((parts, i, (def_fc // parts)))
			logging.warning("@parts/error%d/parts" % (i, parts))
		except BaseException:
			continue  # skip_if_error
		else:
			# parts -> parts_result
			tp_list.append((parts_result, i, (def_fc // parts_result)))
			logging.info("@parts/type%d/parts %d" % (i, parts_result))
	"""

	"""
	max_parts = min_parts = 0

	for part, index, t in tp_list:  # part, index, tp
		try:
			if part > max_parts:
				max_parts = part
			if part < max_parts:  # elif -> if
				min_parts = part
		except BaseException as e:
			logging.error("@part/@index/@t/@min_parts/@max_parts/@error %s!" % ";".join(
				map(str, (part, index, t, min_parts, max_parts, str(e))))
			)
		else:
			logging.info("@part/@index/@t/@min_parts/@max_parts %s" % ";".join(
				map(str, (part, index, t, min_parts, max_parts)))
			)

	parts = min_parts if not max_parts else max_parts  # filter(max/min)
	"""

	"""
	logging.info(
		"@parts_list/@tp_list/@filename %s" % str((";".join(map(str, (len(parts_list), tp_list, filename)))))
	) # parts_list -> len(parts_list) # tp_list(+calc)
	"""

	split_stream = split_stream2 = split_stream3 = split_stream4 = ""

	mx_str = len(str(parts)) + 1  # ; print(f"%0{mx_str}d")

	# @one_time(any_format) # one_line(one_cmd)
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c copy -f segment -segment_time {tp} \"{split_stream}\"" # copy_streams #is_ok
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=0:0:flags=lanczos\" -profile:v main -level 30 -threads 2 -c:a aac -af \"dynaudnorm\" -f segment -segment_time {tp} \"{split_stream}\"" # full(is_debug)
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale=0:0:flags=lanczos\" -profile:v main -level 30 -threads 2 -c:a copy -f segment -segment_time {tp} \"{split_stream}\"" # only_video
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" -f segment -segment_time {tp} \"{split_stream}\"" # only_audio

	# @one_filesize(only_mkv)
	# mkvmerge -o "output.mkv" --split 100M "input.mkv"

	framecount = def_fc  # tp * parts # 2860

	try:
		tp = framecount // parts  # calc_one_part
	except:
		return []

	# @save({filename: [framecount/parts/tp]})_in_json

	segments_dict = {}

	try:
		with open(segments_base, encoding="utf-8") as sbf:
			segments_dict = json.load(sbf)
	except:
		with open(segments_base, "w", encoding="utf-8") as sbf:
			json.dump(segments_dict, sbf, ensure_ascii=False, indent=4, sort_keys=False)


	try:
		segments_dict[filename.strip()] = [{"framecount": framecount, "parts": parts, "tp": tp}]
	except:
		segments_dict[filename.strip()] = [{"framecount": 0, "parts": 0, "tp": 0}]

	try:
		assert segments_dict, ""
	except AssertionError:
		logging.warning("@segments_dict no data for save")
	else:
		segments_dict = {k:v for k, v in segments_dict.items() if os.path.exists(k) and all((v[0]["framecount"], v[0]["parts"], v[0]["tp"]))}  # fitler(only_exists_files/param_not_null)

		with open(segments_base, "w", encoding="utf-8") as sbf:
			json.dump(segments_dict, sbf, ensure_ascii=False, indent=4, sort_keys=False)

	try:
		tp_seg = range(0, def_fc, tp)  # generate_slices
	except:
		return []

	tt_list = []

	try:
		# two_times = (tp // 60, tp % 60)  # slice_size(hh-mm, ss) # default
		for i in range(1, 3):
			try:
				two_times = {"1": lambda x: x // 60, "2": lambda x: x % 60}.get(str(i), 0)(tp)
			except BaseException: # if_error(skip_null)
				continue
			else:
				tt_list.append(two_times)
	except BaseException as e:
		two_times = (tp, str(e))
		logging.error("@tp part_size: %d, error: %s" % two_times)
	else:
		# two_times = tuple(tt_list)  # debug(logging)
		# two_times_str = (tp, str(two_times)) # default
		two_times_str = (tp, str(tt_list) if tt_list else "")  # two_times -> tt_list(hh-mm/ms) ~ (tp~70, tt_list~'[1, 10]')

		logging.info("@tp part_size: %d, part_per_time: %s" % two_times_str)

	filter_framecount = 0
	tp_diff = 0.0
	framecount_diff = 0.0
	parts_diff = 0.0

	# h: int = ms // 3600
	# m: int = ms % 3600 // 60
	# s: int = ms % 3600 % 60

	# test(30962) ~ 8:36:2
	try:
		maybe_hour = tp * parts
		maybe_hour //= 3600  # 8
	except:
		maybe_hour = 0

	try:
		maybe_min = tp * parts
		maybe_min %= 3600  # ?
		maybe_min //= 60  # 36
	except:
		maybe_min = 0

	try:
		maybe_sec = tp * parts
		maybe_sec %= 3600
		maybe_sec %= 60  # 2
	except:
		maybe_sec = 0

	filter_framecount = (lambda h, m, s: (h * 3600) + (m * 60) + s)(
		maybe_hour, maybe_min, maybe_sec
	)  # 8, 36, 2 # 88737(calc=30962)

	try:
		tp_diff = round(
			(lambda fp, t: fp / t)(framecount / parts, tp) * 100, 2
		)  # less / max # <= 100 # float
		assert tp_diff, ""
	except AssertionError:
		logging.warning("@tp_diff is null, current: %s" % filename)
	except BaseException as e:
		tp_diff, tp_diff_str = 0, (filename, str(e))
		logging.error("@tp_diff current: %s, error: %s" % tp_diff_str)
	else:
		tp_diff_status = (
			"equal" if tp_diff == 100 else "diff"
		)
		logging.info("@tp_diff %s" % ";".join(
			map(str, [tp_diff, tp_diff_status, filename]))
		)

	try:
		framecount_diff = round(
			(lambda ff, f: ff / f)(filter_framecount, framecount) * 100, 2
		)  # less / max # <= 100 # float
		assert framecount_diff, ""
	except AssertionError:
		logging.warning("@framecount_diff is null, current: %s" % filename)
	except BaseException as e:
		framecount_diff, framecount_diff_err = 0, (filename, str(e))
		logging.error("@framecount_diff current: %s, error: %s" % framecount_diff_err)
	else:
		framecount_diff_status = (
			"equal" if framecount_diff == 100 else "diff"
		)
		logging.info("@framecount_diff %s" % ";".join(
			map(str, [framecount_diff, framecount_diff_status, filename]))
		)

	try:
		parts_diff = round(
			(lambda ft, p: ft / p)(framecount / tp, parts) * 100, 2
		)  # less / max # <= 100 # float
		assert parts_diff, ""
	except AssertionError:
		logging.warning("@parts_diff is null, current: %s" % filename)
	except BaseException as e:
		parts_diff, parts_diff_err = 0, (filename, str(e))
		logging.error("@parts_diff current: %s, error: %s" % parts_diff_err)
	else:
		parts_diff_status = (
			"equal" if framecount_diff == parts_diff else "diff"
		)
		logging.info("@parts_diff %s" % ";".join(
			map(str, [parts_diff, parts_diff_status, filename]))
		)

	# tp_seg = range(0, def_fc, tp)

	try:
		# dl = {str(chunk): str(chunk + tp) for i, chunk in enumerate(chunks)} # for_sequence(- 1)
		dl = {str(chunk): str(tp) for item, chunk in enumerate(tp_seg)}  # for_ffmpeg

		assert dl, ""
	except AssertionError:
		return []
	else:
		logging.info("@dl length: %s" % str(len(dl)))

	# {'0': '124', '124': '124', '248': '124', '372': '124', '496': '124', '620': '124', '744': '124', '868': '124', '992': '124', '1116': '124', '1240': '124', '1364': '124', '1488': '124', '1612': '124', '1736': '124', '1860': '124', '1984': '124', '2108': '124', '2232': '124', '2356': '124', '2480': '124', '2604': '124', '2728': '124', '2852': '124', '2976': '124', '3100': '124'} # not_full
	# {'0': '124', '124': '124', '248': '124', '372': '124', '496': '124', '620': '124', '744': '124', '868': '124', '992': '124', '1116': '124', '1240': '124', '1364': '124', '1488': '124', '1612': '124', '1736': '124', '1860': '124', '1984': '124', '2108': '124', '2232': '124', '2356': '124', '2480': '124', '2604': '124', '2728': '124', '2852': '124', '2976': '124', '3100': '128'} # is_full

	# """
	# (3100, 124, 128) # (last_key, last_value, new_value)
	last_key, last_value = int([*dl][-1]), int(
		list(dl.values())[-1]
	)  # ; new_value = last_value + (def_fc - last_key)

	try:
		new_value = def_fc - last_key if def_fc - last_key > 0 else 0  # is_true
		assert new_value, "@new_value ошибка смещения кадров, current: %s" % filename
	except AssertionError:  # if_null
		logging.warning("@new_value ошибка смещения кадров, current: %s" % filename)
		return []
	except BaseException as e:  # if_error
		new_value_err = (str(e), filename)
		logging.error("@new_value error: %s, current: %s" % new_value_err)
	else:  # if_ok
		# print((last_key, last_value, new_value)) #; '@last_key/@last_value/@new_value 2852;124;8'
		logging.info(
			"@last_key/@last_value/@new_value %s"
			% ";".join(map(str, [last_key, last_value, new_value]))
		)

		dl[str(last_key)] = str(new_value)  # обновить_недостающее_количество_кадров

	"""
	dl_new = [{"key": str(k), "value": str(v)} for k, v in dl.items()]

	try:
		dl_data = {"dl_new": dl_new}
		key_list = jmespath.search("dl_new[*].key", dl_data)
		value_list = jmespath.search("dl_new[*].value", dl_data)
		zip_key_value = zip(key_list, value_list)
	except BaseException as e:
		logging.error("@dl_data error: %s" % str(e))
	else:
		logging.info("@dl_data current: %s" % str(zip_key_value))
	"""

	sm = 0

	try:
		for _, v in dl.items():
			try:
				assert all((v, dl)), ""
			except AssertionError:
				continue
			else:
				sm += int(v)
	except:
		sm = 0
	else:
		logging.info("@sm %s" % str(sm))

	try:
		sm_status = False if len(set(dl.values())) == 1 else True  # True
	except:
		sm_status = str(None)
	finally:
		# "@sm/set {'124', '8'}, status: True, currnet: None"
		logging.info(
			"@sm/set %s, status: %s, currnet: %s"
			% (str(set(dl.values())), str(sm_status), filename)
		)  # one(no_change), >one(some_change) # "@sm/set {'124', '128'}, status: True"

	try:
		dl_filter = (
			False if sm < def_fc else True
		)  # False(not_full) / True(is_full) # pass_2_of_2 # True
	except:
		dl_filter = str(None)
	finally:
		# '@dl_filter True, last_key: ?, last_value: ?, crrent: %s' % filename
		dl_filter_str = (str(dl_filter), str(last_key), dl[str(last_key)], filename)
		logging.info(
			"@dl_filter %s, last_key: %s, last_value: %s, current: %s" % dl_filter_str
		)

	# 'sum: 2860, framecount: 2860, current: None'
	sfc_str = (str(sm), def_fc, filename)
	logging.info("sum: %s, framecount: %d, current: %s" % sfc_str)
	# """

	segments_status = (
		True if parts == len(tp_seg) else False
	)  # if_nortmal_by_trim / if_longer_by_trim

	# "@part_size": tp, "@framecount": framecount, "@parts": parts
	parts_info = {
		"parts_set": set(dl.values()),
		"@segments": {
			"@segments_length": len(tp_seg),
			"@segments_status": segments_status,
		},  # "segments_dict": len(dl)
	}

	fp_str = (filename, str(parts_info))
	logging.info("filename: %s, parts_info: %s" % fp_str)

	cmd_str = []

	# no_change_level(profile) - use default
	try:
		pr, le = wh.get_profile_and_level(filename)  # [main,30]
		assert all((pr, le)), ""
	except AssertionError:
		if any(
			(
				not pr,
				not le
			)
		):
			logging.warning("profile: %s, level: %s [%s]" % (pr, le, filename))
		else:
			logging.warning("no profile, no level [%s]" % filename)
	else:
		logging.info("@pr/@le %s" % ";".join(
			map(str, [pr, le]))
		)  # "main";"30"

	try:
		codecs = wh.get_codecs(filename)  # ['h264', 'aac']
		assert codecs, ""
	except AssertionError:
		logging.warning("no codecs [%s]" % filename)
		return []
	else:
		logging.info("@codecs %s" % ";".join(
			map(str, tuple(codecs)))
		)  # "h264";"aac"

	nw = nh = 0

	try:
		w, h, ic = wh.get_width_height(filename, is_calc=True, maxwidth=640)
		assert all((w, h)), ""
	except AssertionError:
		nw, nh = 0, 0
		if any(
			(
				not w,
				not h
			)
		):
			logging.warning("width: %d, height: %d [%s]" % (w, h, filename))
		else:
			logging.warning("no width, no height [%s]" % filename)
	except BaseException as e:
		nw, nh = 0, 0
		w_h_ic_error = (str(e), filename)
		logging.error(
			"@w/@h/@ic error calc width or height %s, current: %s" % w_h_ic_error
		)
	else:
		nw, nh = w, h
		logging.info("@w/@h/@ic %s" % ";".join(
			map(str, [w, h, ic]))
		)

	some_display_ar = {}

	try:
		with open(displayar_base, encoding="utf-8") as dbf:
			some_display_ar = json.load(dbf)
	except:
		with open(displayar_base, "w", encoding="utf-8") as dbf:
			json.dump(some_display_ar, dbf, ensure_ascii=False, indent=4, sort_keys=False)

	display_ar = some_display_ar

	# @add_or_update_display_aspect_ratio_list_every_job
	try:
		assert all((w, h)), ""
	except AssertionError:
		logging.warning(f"@display_ar skip (width={w} / height={h}) is null, current: {filename}")
	except BaseException as e:
		display_ar_err = (str(e), filename)
		logging.error("@display_ar error: %s, current: %s" % display_ar_err)
	else:
		display_ar["x".join(map(str, (w, h)))] = ";".join(map(str, ((w / h), filename))) # append_dar(title_by_width_and_height) # append_update(+filename)

		logging.info(f"@display_ar add or update (width={w} / height={h}), current: {filename}")

		some_display_ar |= display_ar  # python 3.9
		# some_display_ar.update(display_ar)  # update_every_job(+last_filename) 
		# some_display_ar_new = {**some_display_ar, **display_ar} # a.update(b) # a |= b # python 3.9

		try:
			assert some_display_ar, ""
		except AssertionError:
			logging.warning("@some_display_ar is null, save skipped")
		else:
			with open(displayar_base, "w", encoding="utf-8") as dbf:
				json.dump(some_display_ar, dbf, ensure_ascii=False, indent=4, sort_keys=False)		

	# sar=(w/h) ; par=(sar/(w/h)) ; dar=(sar * par)

	# aspect_ratio
	# """
	sar = par = dar = None

	try:
		assert any((w, h)), ""  # all -> any
	except AssertionError:
		logging.warning("w/h %s, current: %s" % ("x".join(
			map(str, [w, h])), filename)
		)
	except BaseException as e:
		sar, sar_err = 0, (str(e), filename)
		logging.error("@sar error: %s, current: %s" % sar_err)
	else:
		try:
			sar = w / h
		except:
			sar = None
		else:
			logging.info(
				"@sar/w/h %s, current: %s" % ("x".join(map(str, [sar, w, h])), filename)
			)  # scale

	try:
		assert any((sar, w, h)), ""  # all -> any
	except AssertionError:
		logging.warning(
			"@sar/w/h %s, current: %s" % ("x".join(map(str, [sar, w, h])), filename)
		)
	except BaseException as e:
		par, par_err = None, (str(e), filename)
		logging.error("@par error: %s, current: %s" % par_err)
	else:
		try:
			par = sar / (w / h)
		except:
			par = None
		else:
			logging.info(
				"@par/@sar/w/h %s, current: %s"
				% ("x".join(map(str, [par, sar, w, h])), filename)
			)  # pixel

	try:
		assert any((sar, par)), ""  # all -> any
	except AssertionError:
		logging.warning(
			"@sar/@par %s, current: %s" % ("x".join(map(str, [sar, par])), filename)
		)
	except BaseException as e:
		dar, dar_err = None, (str(e), filename)
		logging.error("@dar error: %s, current: %s" % dar_err)
	else:
		try:
			dar = sar * par
		except:
			dar = None
		else:
			logging.info(
				"@dar/@sar/@par %s, current: %s"
				% ("x".join(map(str, [dar, sar, par])), filename)
			)  # display
	# """

	# del wh # clear_mem # debug

	is_scale = True if ic else False  # need_change_scale

	# @job(optimize_run)

	init_ffmpeg = " ".join(
		["cmd /c", "".join([path_for_queue, "ffmpeg.exe"])]
	)  # init_ffpeg_cmd # cmd /k
	init_file = " ".join(["-hide_banner", "-y", "-i"])  # hide_banner_and_input_file
	init_file += "".join([" ", '"', filename, '"'])  # full_name

	pr_le_sc = [
		"main" in pr.lower(),
		int(le) <= 30,
		not is_scale,
	]  # profile / level / scale

	init_nometa_vfile = ""

	# clear_meta_and_codec(copy)
	try:
		if (
			pr_le_sc.count(True) != 3
		):  # some_optimized
			init_nometa_vfile = "-map_metadata -1 -preset medium -threads 2 -c:v libx264"  # video_stabilize
		elif (
			pr_le_sc.count(True) == 3
		):  # all_optimized
			init_nometa_vfile = (
				"-map_metadata -1 -preset medium -threads 2 -c:v copy"  # video_copy
			)
		assert init_nometa_vfile, ""
	except AssertionError:
		init_nometa_vfile = (
			"-map_metadata -1 -preset medium -threads 2 -c:v libx264"  # video_stabilize
		)
	else:
		logging.info("@pr_le_sc %s" % ";".join(
			map(str, [pr_le_sc]))
		)

	pr_le_sc_str = ""

	# @profile
	if not "main" in pr.lower():
		pr_le_sc_str += "".join([" ", "-profile:v main", " "])

	# @level
	if int(le) > 30:
		pr_le_sc_str += "".join([" ", "-level 30", " "])

	# @scale
	if is_scale:
		pr_le_sc_str += "".join(
			[" ", "-vf scale=%d:%d" % (nw, nh), " "]
		)  # scale=0:0:flags=lanczos

	try:
		assert pr_le_sc_str, ""
	except AssertionError:
		logging.warning(
			"@pr_le_sc_str profile and level and scale parameters for '%s'" % filename
		)
	else:
		logging.info(
			"@pr_le_sc_str profile or level or scale parameters %s for '%s'"
			% (pr_le_sc_str, filename)
		)

	video_filter = (
		pr_le_sc_str if pr_le_sc_str else ""
	)  # +vf / +profile / +level / +scale

	init_afile = ""

	try:
		if (
			pr_le_sc.count(True) != 3
		):  # some_optimized
			init_afile = (
				'-threads 2 -c:a %s -af "dynaudnorm"' % "aac"
			)  # sound_stabilize # ffmpeg release?
		elif (
			pr_le_sc.count(True) == 3
		):  # all_optimized
			init_afile = "-threads 2 -c:a copy"  # sound_copy
		assert init_afile, ""
	except AssertionError:
		init_afile = '-threads 2 -c:a aac -af "dynaudnorm"'  # sound_stabilize
	finally:
		logging.info("@init_file %s" % str(init_afile))

	# project_file = "".join(["\"", path_to_done, filename.split("\\")[-1], "\""]) # done_full_path(debug)
	short_name, ext = filename.split("\\")[-1].split(".")[0], "".join(
		[".", filename.split(".")[-1]]
	)  # short_filename / file_ext

	w, h = map(int, (w, h))

	# if not isinstance(w, int):
	# w = int(w)

	# if not isinstance(h, int):
	# h = int(h)

	# debug(one_line/one_cmd)
	cmd = ""

	# @segment(fast_run) / @segment_time! / @segment_list / @segment_format # muxer segment

	# @"обычная" разрезка по segment_time(1)

	# @{file_short)_%03d.mp4 # filename = "c:\\downloads\\mytemp\\test.tst"; path_to_done = "c:\\downloads\\list\\"
	try:
		# 'c:\\downloads\\list\\test_%03d.mkv'
		split_stream = os.path.join(
			"".join(['"', path_to_done]),
			"".join(
				[
					filename.split("\\")[-1].split(".")[0],
					"".join(["_", f"%0{mx_str}d"]),
					ext,
					'"',
				]
			),
		).replace(
			"__", "_"
		)  # 'c:\\downloads\\list\\test_%03d.mp4' # "%03d" -> f"%0{mx_str}d"

		assert split_stream, ""
	except AssertionError:  # if_null
		logging.warning("@split_stream current: %s" % filename)
		return []
	except BaseException as e:  # if_error
		split_stream_err = (filename, str(e))
		logging.error("@split_stream current: %s, error: %s" % split_stream_err)
		return []
	else:  # if_ok
		split_stream_str = (filename, split_stream)
		logging.info("@split_stream current: %s, parameters: %s" % split_stream_str)

	init_segment = " ".join(
		[
			"-f",
			"segment",
			"-segment_time",
			f"{tp}",
		]  # "-reset_timestamps", "1" -> mark's_timer(start_0)
	)  # is_full_framecount_by_segment # src[any] - > dst[mp4] # ok

	# sequence_job(cmd + ext2ext)
	try:
		cmd = " ".join(
			[
				init_ffmpeg,
				init_file,
				init_nometa_vfile,
				video_filter,
				init_afile,
				init_segment,
				split_stream,
			]
		)  # filename[src] / vinit / vf / +profile(level/scale) / ainit / filter(segment) / filename_%03d.mp4[dst] # if_not_optimized(sequence_line(job->sequence->merge)) / skip_optimized_lines
	except BaseException as e:  # AssertionError:
		cmd = ";".join(["".join(["'", filename, "'"]), str(e)])
	finally:
		# scale(True=1, ffmpeg) / profile(True=1, ffmpeg) / level(True=1, ffmpeg) / "any"(True=0) # True(is_optimized)
		if (
			pr_le_sc.count(True) >= 0
		):
			logging.info(
				"@cmd command: %s" % cmd_whitespace.sub(" ", cmd)
			)  # cmd -> cmd_whitespace.sub("", cmd) # debug

			with open(sequence_list, "a", encoding="utf-8") as slf:  # buffering=1
				slf.write(
					"%s\n" % cmd_whitespace.sub(" ", cmd)
				)  # writelines # if not_include_regex.findall(cmd):  # skip_copy

		# segments(cmd)
		print(Style.BRIGHT + Fore.CYAN + "%s" % cmd)
		logging.info("@cmd %s" % cmd)

	# is_debug(@init_segment) / @{file_short}_%03d.mp4
	# cmd /c d:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i "D:\Downloads\Temp\Serials\Sanctuary_01s11e.mp4" -map_metadata -1 -preset medium -threads 2 -c:v libx264 -profile:v main -vf scale=640:360 -threads 2 -c:a aac -af "dynaudnorm" -f segment -segment_time 89 "d:\downloads\list\Sanctuary_01s11e_%03d.mp4"
	# cmd /c d:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i "input.mp4" -map_metadata -1 -preset medium -threads 2 -c:v libx264 -profile:v main -vf scale=0:0:flags=lanczos -threads 2 -c:a aac -af "dynaudnorm" -f segment -segment_time {tp} "d:\downloads\list\Sanctuary_01s11e_%03d.mp4"

	# @hls(any2m3u8) / @start_number / @hls_time! / @hls_list_size / @hls_segment_filename # muxer hls(m3u8)?!

	# @"обычная" разрезка по hls_time(2)

	# Наименование;Разрешение;Ширина(width);Высота(height);Кадров в сек.(fps);Скорость (Мб/с)
	"""
	UHD (4K);2160p;3840;2160;60;22,46-28,80
	UHD (4K);2160p;3840;2160;30;13,67-17,77
	2K;1440p;2560;1440;60;?
	2K;1440p;2560;1440;30;?
	FullHD;1080p;1920;1080;60;5,66-7,22
	FullHD;1080p;1920;1080;30;4,39-5,17
	HD;720p;1280;720;60;3,41-4,29
	HD;720p;1280;720;30;2,44-3,12
	SD;480p;854;480;30;1,22-1,56
	SD;360p;640;360;30;0,68-0,87
	SD;240p;426;240;30;0,39-0,58
	"""

	# -- include_filename(one_review_need_unique_folder(v%d)) / use_for_web_server(test_only_for_players) --
	# @640x266 # new(cmd4) # multiple(is_ok/test_on_ready) # test_10sec # manual
	# 576:(640/266)*240 # 866:(640/266)*360 # 1154:(640/266)*480
	"""
	ffmpeg -i "Golovolomka_2(2024)_trailer.mp4" \
	-filter_complex \
	"[0:v]split=3[v1][v2][v3]; \
	[v1]copy[v1out]; [v2]scale=w=1154:h=480[v2out]; [v3]scale=w=866:h=360[v3out]" \
	-map "[v1out]" -c:v:0 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:0 7500k -maxrate:v:0 15M -minrate:v:0 15M -bufsize:v:0 15M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
	-map "[v2out]" -c:v:1 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:1 4M -maxrate:v:1 8M -minrate:v:1 8M -bufsize:v:1 8M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
	-map "[v3out]" -c:v:2 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:2 1500k -maxrate:v:2 3M -minrate:v:2 3M -bufsize:v:2 3M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
	-map a:0 -c:a:0 aac -b:a:0 128k -ac 2 \
	-map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
	-map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
	-f hls \
	-hls_time 10 \
	-hls_playlist_type vod \
	-hls_flags independent_segments \
	-hls_segment_type mpegts \
	-hls_segment_filename "v%v/Golovolomka_2(2024)_%03d.ts" \
	-master_pl_name "Golovolomka_2(2024).m3u8" \
	-var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" "v%v/prog_index.m3u8"
	"""

	"""
	ffmpeg -y -i "Golovolomka_2(2024)_trailer.mp4"  \
	-preset slow -g 48 -sc_threshold 0 \
	-map 0:0 -map 0:1 -map 0:0 -map 0:1 -map 0:0 -map 0:1 \
	-s:v:0 576x240 -c:v:0 libx264 -b:v:0 580k \
	-s:v:1 866x360 -c:v:1 libx264 -b:v:1 870k \
	-s:v:2 1154x480 -c:v:2 libx264 -b:v:2 1560k \
	-c:a copy \
	-var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" \
	-master_pl_name "Golovolomka_2(2024).m3u8" \
	-f hls -hls_time 10 -hls_list_size 0 \
	-hls_segment_filename "v%v/Golovolomka_2(2024)_%d.ts" \
	"v%v/prog_index.m3u8"
	"""

	# %v is expected either in the filename or in the sub-directory name of file v%v/v%v_index.m3u8, but only in one of them
	# Could not write header for output file #0 (incorrect codec parameters ?): Invalid argument
	# Error initializing output stream 0:4 --

	# ffmpeg -i video.mp4 -threads 2 -c:v copy -hls_segment_type mpegts -map v:0 -hls_time {tp} out_vid.m3u8 # video(mp4) -> m3u8(end_format)
	# ffmpeg -i audio.aac -threads 2 -c:a copy -hls_segment_type mpegts -map a:0 -hls_time {tp} out_aud.m3u8 # audio(aac) -> m3u8(end_format)

	# @{file_short}.m3u8/@{file_short}%d.ts # filename = "c:\\downloads\\mytemp\\test.tst"; path_to_done = "c:\\downloads\\list\\"
	try:
		# 'c:\\downloads\\list\\test.m3u8'
		split_stream2 = os.path.join(
			"".join(['"', path_to_done]),
			"".join(
				[
					filename.split("\\")[-1].replace(
						filename.split("\\")[-1].split(".")[-1], "m3u8"
					),
					'"',
				]
			),
		).replace(
			"__", "_"
		)  # 'c:\\downloads\\list\\test.m3u8'

		assert split_stream2, ""
	except AssertionError:  # if_null
		logging.warning("@split_stream2 current: %s" % filename)
		return []
	except BaseException as e:  # if_error
		split_stream_err = (filename, str(e))
		logging.error("@split_stream2 current: %s, error: %s" % split_stream_err)
		return []
	else:  # if_ok
		split_stream_str = (filename, split_stream2)
		logging.info("@split_stream2 current: %s, parameters: %s" % split_stream_str)

	try:
		split_mpegts = os.path.join(
			"".join(['"', path_to_done]),
			"".join(
				[
					filename.split("\\")[-1].split(".")[0],
					f"_%0{mx_str}d",
					filename.split(".")[-1].replace(filename.split(".")[-1], ".ts"),
					'"',
				]
			),
		)  # '"d:\\downloads\\list\\Tracker_01s10e_%03d.ts"' # debug(ok)

		assert split_mpegts, ""
	except AssertionError:  # if_null
		logging.warning("@split_mpegts current: %s" % filename)
		return []
	except BaseException as e:  # if_error
		split_mpegts_err = (filename, str(e))
		logging.error("@split_mpegts current: %s, error: %s" % split_mpegts_err)
		return []
	else:
		split_mpegts_str = (filename, split_mpegts)
		logging.info("split_mpegts current: %s, parameters: %s" % split_mpegts_str)

	init_hls = " ".join(
		[
			"-start_number",
			"0",
			"-hls_time",
			f"{tp}",
			"-hls_list_size",
			"0",
			"-f",
			"hls",
			"-hls_segment_filename",
			f"{split_mpegts}",
		]  # (tp / framecount / parts(>=5)) # len(dl) <-> len(dl) + 1
	)  # is_full_framecount_by_m3u8 # src[any] -> mpegts(croped/hls_list_size("debug")) / dst[!mp4] # -hls_list_size 0 ~ all_segments_in_one_playlist

	# hls_job(cmd + any2m3u8)
	try:
		cmd2 = " ".join(
			[
				init_ffmpeg,
				init_file,
				init_nometa_vfile,
				video_filter,
				init_afile,
				init_hls,
				split_stream2,
			]
		)  # filename[src] / vinit / vf / +profile(level/scale) / ainit / filter(hls) / filename.m3u8[dst] # if_not_optimized(sequence_line(job->sequence->merge)) / skip_optimized_lines
	except BaseException as e:  # AssertionError:
		cmd2 = ";".join(["".join(["'", filename, "'"]), str(e)])
	finally:
		# scale(True=1, ffmpeg) / profile(True=1, ffmpeg) / level(True=1, ffmpeg) / "any"(True=0) # True(is_optimized)
		if pr_le_sc.count(True) >= 0:
			logging.info(
				"@cmd command: %s" % cmd_whitespace.sub(" ", cmd2)
			)  # cmd2 -> cmd_whitespace.sub("", cmd2) # debug

			with open(sequence_list2, "a", encoding="utf-8") as slf2:  # buffering=1
				slf2.write(
					"%s\n" % cmd_whitespace.sub(" ", cmd2)
				)  # writelines # if not_include_regex.findall(cmd):  # skip_copy

		# hls(cmd)
		print(Style.BRIGHT + Fore.CYAN + "%s" % cmd2)
		logging.info("@cmd2 %s" % cmd2)

	# is_debug(init_hls) / @{file_short}%d.ts -> @{file_short}_%03d.ts # f"%0{mx_str}d"
	# cmd /c d:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i "D:\Downloads\Temp\Serials\Sanctuary_01s11e.mp4" -map_metadata -1 -preset medium -threads 2 -c:v libx264 -profile:v main -vf scale=640:360 -threads 2 -c:a aac -af "dynaudnorm" -start_number 0 -hls_time 89 -hls_list_size 0 -f hls -hls_segment_filename "d:\downloads\list\Sanctuary_01s11e_%03d.ts" "d:\downloads\list\Sanctuary_01s11e.m3u8"
	# cmd /c d:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i "input.mp4" -map_metadata -1 -preset medium -threads 2 -c:v libx264 -profile:v main -vf scale=0:0:flags=lanczos -threads 2 -c:a aac -af "dynaudnorm" -start_number 0 -hls_time {tp} -hls_list_size 0 -f hls -hls_segment_filename "output_%03d.ts" "output.m3u8"

	# mp4 -> hls(m3u8) ~ pass_1_of_2 # hls(m3u8) -> mp4 ~ pass_2_of_2 # debug
	"""
	For a given video file (mp4 format), a m3u8 file which points to segments with some duration can be generated as follows:
	ffmpeg -v quiet -i input.mp4 -c copy -f segment -segment_list intermediate.m3u8 -segment_time <duration> intermediate_%03d.ts

	@rejoin the segments back -> ffmpeg -i intermediate.m3u8 -c copy output.mp4
	"""

	# g://"Как создать мастер-плейлист HLS с помощью ffmpeg"

	# @обычная разрезка по ключевым кадрам(3) # keyint(optimal_run/skip_frames)

	# debug(test/manual_run) # segments_list(input.ffcat) # is_hide_prompt(-v error)
	# framecount = (2 * 3600) + (19 * 60) = 8340; parts_list = [8340 // 60, 8340 % 60]; parts = [139 + 0] // 2 = 69; tp = 8340 // 69 = 120(segment_time)

	# g://"ffmpeg" muxer concatenate # -segment_list

	fname = filename.split("\\")[-1]

	# +path_to_done! # @segment_list(ffcat) # debug(concat_name)
	# """
	try:
		concat_name = os.path.join(
			path_to_done,
			"".join([filename.split("\\")[-1].split(".")[0], "".join([".", "ffcat"])]),
		)

		assert concat_name, ""
	except AssertionError:  # if_null
		concat_name = "".join(
			['"', filename.split("\\")[-1], "".join([".", "ffcat"]), '"']
		)
	except BaseException as e:  # if_error
		concat_name_err = (filename, str(e))
		logging.error("@concat_name current: %s, error: %s" % concat_name_err)
		return []
	else:
		concat_name_str = (filename, concat_name)
		logging.info("@concat_name current: %s, parameters: %s" % concat_name_str)
	# """

	# -path_to_done! # @segment_list # debug(concat_name2)
	# """
	try:
		concat_name2 = "".join(
			[filename.split("\\")[-1].split(".")[0], "".join([".", "ffcat"])]
		)

		assert concat_name2, ""
	except AssertionError:  # if_null
		concat_name2 = "".join(
			['"', filename.split("\\")[-1], "".join([".", "ffcat"]), '"']
		)
	except BaseException as e:  # if_error
		concat_name_err = (filename, str(e))
		logging.error("@concat_name2 current: %s, error: %s" % concat_name_err)
		return []
	else:
		concat_name_str = (filename, concat_name2)
		logging.info("@concat_name2 current: %s, parameters: %s" % concat_name_str)
	# """

	# split_any_to_segments(+ffcat) / semi_auto # +path_to_done! # segments(seg) # debug(split_stream3)
	# """
	try:
		split_stream3 = os.path.join(
			"".join(['"', path_to_done]),
			"".join(
				[
					filename.split("\\")[-1].split(".")[0],
					f"_%0{mx_str}d",
					filename.split(".")[-1].replace(filename.split(".")[-1], ".seg"),
					'"',
				]
			),
		).replace(
			"__", "_"
		)  # '"d:\\downloads\\list\\Tracker_01s10e_%03d.seg"' # "%03d" -> f"%0{mx_str}d"

		assert split_stream3, ""
	except AssertionError:  # if_null
		logging.warning("@split_stream3 current: %s" % filename)
		return []
	except BaseException as e:  # if_error
		split_stream_err = (filename, str(e))
		logging.error("@split_stream3 current: %s, error: %s" % split_stream_err)
		return []
	else:
		split_stream_str = (filename, split_stream3)
		logging.info("@split_stream3 current: %s, parameters: %s" % split_stream_str)
	# """

	init_segment2 = " ".join(
		[
			"-f",
			"segment",
			"-segment_time",
			f"{tp}",
			"-segment_format",
			filename.split(".")[-1],
			"-segment_list",
			"".join(['"', f"{concat_name}", '"']),
			"-reset_timestamps",
			"1",
			"-v",
			"error",
		]  # "-reset_timestamps", "1" -> mark's_timer(start_0)
	)  # is_full_framecount_by_segment # src[any] - > dst[mp4] # debug(test)

	# concat_from_ffcat / semi_auto # only_current_folder! # segments(merge)
	# """
	# fname = "Argyle_Supershpion(2024)_.mp4"; path_to_done = "%sdownloads\\list\\" % "c:\\" # debug(split_stream4)
	try:
		split_stream4 = "".join(
			[fname.split(".")[0], "_keyint_", "".join([".", fname.split(".")[-1]])]
		).replace(
			"__", "_"
		)  # for_auto_run

		assert split_stream4, ""
	except AssertionError:  # if_null
		logging.warning("@split_stream4 current: %s" % filename)
		return []
	except BaseException as e:  # if_error
		split_stream_err = (filename, str(e))
		logging.error("@split_stream4 current: %s, error: %s" % split_stream_err)
		return []
	else:
		split_stream_str = (filename, split_stream4)
		logging.info("@split_stream4 current: %s, parameters: %s" % split_stream_str)
	# """

	# ffmpeg -v error -i f"{concat_name}" -map 0 -c copy f"{split_stream4}" # '"c:\\downloads\\list\\Argyle_Supershpion(2024)_keyint_.mp4"' # split_stream4
	merge_after_sequence = [
		init_ffmpeg,
		"-v",
		"error",
		"-i",
		"".join(['"', f"{concat_name2}", '"']),
		"-map",
		"0",
		"-c",
		"copy",
		"".join(['"', f"{split_stream4}", '"']),
	]  # "-y" -> permission_error

	init_map = " ".join(["-map", "0:v", "-map", "0:a"])

	# keyint_job(cmd + segments_by_keyint)
	try:
		cmd3 = " ".join(
			[
				init_ffmpeg,
				init_file,
				init_map,
				init_nometa_vfile,
				video_filter,
				init_afile,
				init_segment2,
				split_stream3,
			]
		)  # input.mp4[src] / vinit / map(video/audio) / vf / +profile(level/scale) / ainit / filter(keyint) / output_%03d.mp4[dst] / +merge_segments(test/debug)
	except BaseException as e:  # AssertionError:
		cmd3 = ";".join(["".join(["'", filename, "'"]), str(e)])
	finally:
		old_cmd3 = cmd3 if cmd3 else []
		# segment(keyint)
		# any(input) -> segments -> any(output)
		try:
			cmd3_new = " & ".join(
				[cmd3, " ".join(merge_after_sequence)]
			)  # cmd3 += " ".join(merge_after_sequence)
		except:
			cmd3_new = cmd3
		finally:
			cmd3 = cmd3_new
			print(Style.BRIGHT + Fore.CYAN + "%s" % cmd3)
			logging.info("@cmd3 %s" % cmd3)

		# scale(True=1, ffmpeg) / profile(True=1, ffmpeg) / level(True=1, ffmpeg) / "any"(True=0) # True(is_optimized)
		if (
			pr_le_sc.count(True) >= 0
		):
			logging.info(
				"@cmd command: %s" % cmd_whitespace.sub(" ", cmd3)
			)  # cmd3 -> cmd_whitespace.sub("", cmd3) # debug

			with open(sequence_list3, "a", encoding="utf-8") as slf3:  # buffering=1
				slf3.write(
					"%s\n" % cmd_whitespace.sub(" ", old_cmd3)
				)  # writelines # if not_include_regex.findall(cmd):  # skip_copy

	# @sequence_list4
	# <input> -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:-1:-1,setsar=1" -r 60 -threads 2 -c:a copy <output>; {width}i:{height}p<:{padx}:{pady}><decrease> # hd(720p) + fps(60) # black_borders # scaling(+)

	# @template
	# ffmpeg -i "inout.mp4" -map 0 -codec copy -f segment -segment_time {tp} -segment_list "output.ffconcat" -segment_list_type ffconcat "output_%05d.ts" # if_copy(no_recoding/debug)
	# ffplay "output.ffconcat" # play_segment_part_by_part # merge(no_recoding/debug)

	# @example(nometa[1]/<profile/scale/level>[1]/segment_time[1]/concat[2]) # <cmd> & <cmd2>
	# ffmpeg -fflags +genpts -i "Argyle_Supershpion(2024)_.mp4" -map_metadata -1 -preset medium -map 0:v:0 -map 0:a:0 -threads 2 -c:v libx264 -vf "scale=-1:480:flags=lanczos" -threads 2 -c:a aac -af "dynaudnorm" -f segment -segment_time 120 -segment_format mp4 -segment_list "Argyle_Supershpion(2024)_.ffcat" -reset_timestamps 1 -v error "Argyle_Supershpion(2024)_%03d.seg" # original(input->segments)
	# ffmpeg -y -v error -i "Argyle_Supershpion(2024)_.ffcat" -map 0 -c copy "Argyle_Supershpion(2024)_keyint_.mp4" # destonation(segments->output) # error(yes_recoding) / use_old_concat

	# cmd /c d:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i "D:\Downloads\Temp\Serials\Sanctuary_01s11e.mp4" -map 0:v -map 0:a -map_metadata -1 -preset medium -threads 2 -c:v libx264  -profile:v main  -vf scale=640:360  -threads 2 -c:a aac -af "dynaudnorm" -f segment -segment_time 89 -segment_format mp4 -segment_list "d:\downloads\list\Sanctuary_01s11e.ffcat" -reset_timestamps 1 -v error "d:\downloads\list\Sanctuary_01s11e_%03d.seg"
	# cmd /c d:\\downloads\\mytemp\\ffmpeg.exe -v error -i "Sanctuary_01s11e.ffcat" -map 0 -c copy "Sanctuary_01s11e_keyint_.mp4"

	# skip_slide	
	"""
	try:
		# save_slide(slide, framecount, filename, width, height)
		# save_slide(slide=20, framecount=framecount, filename, w, h)
		save_slide(20, framecount, filename, w, h) # default(is_calc_width_and_height)
	except BaseException as e:
		save_slide_err = (str(e), filename)
		logging.error("@save_slide error: %s, current: %s" % save_slide_err)
	else:
		logging.info("@save_slide complete slides for %s" % filename)
	"""

	try:
		if filename in [*some_dict]:  # some_file / is_skip_update
			some_dict.pop(filename)
	except:
		some_dict[filename] = []

	cnt = 1  # 0 -> 1(start)

	# (for /f "delims=" %a in (ext.lst) do @echo file '%a') > concat.lst # cmd_line(in_cmd)
	# (for /f "delims=" %%a in (ext.lst) do @echo file '%%a') > concat.lst # cmd_file(in_script)

	# (dir /r/b/s "Gentlemeny(2019)__0*.mp4") > ext.lst # segment_job(with_counted) # debug(cinema)

	# --- dos_shell(-c copy (fast_copy) / without diff param) ---
	# (dir /r/b/s Short_AAsBBe*p.ext) > ext.lst # check_sort # optimal_job(with_parts)
	# (for /f "delims=" %a in (ext.lst) do @echo file '%a') > concat.lst
	# ffmpeg -f concat -safe 0 -y -i concat.lst -c copy Short_AAsBBe.ext

	"""
	FORFILES /D +8.5.2024 /C "cmd /c echo @fname является новым сегодня"
	FORFILES /D -30 /M *.exe /C "cmd /c echo @path 0x09 был изменен 30 дней назад"
	FORFILES /D 01.01.2001 /C "cmd /c echo @fname является новым с 1-янв-2001"
	FORFILES /M *.exe /D +1
	FORFILES /M *.txt /C "cmd /c if @isdir==FALSE notepad.exe @file"
	FORFILES /P C:\ /S /M *.bat
	FORFILES /P C:\WINDOWS /S /M DNS*.*
	FORFILES /S /M *.doc /C "cmd /c echo @fsize"
	FORFILES /S /M *.txt /C "cmd /c type @file | more"
	"""

	# cmd_file (%%a) # cmd_line (%a)

	def concat_short_to_original(
		filename, is_merge: bool = True
	):  # debug # def_parts: int = parts
		mp4, old = "mp4", filename.split(".")[-1]  # for_merge(any)

		try:
			assert bool(mp4 == old), ""
		except AssertionError:
			old = filename.split(".")[-1]
			ext = "".join([".", "mp4"])  # another_ext
		else:
			old = ext = "".join([".", "mp4"])  # default_ext

		if is_merge:
			merge_files_path = (
				"ext.lst"  # default # "\"%s\\ext.lst\"" % script_path # clear_old
			)
			concat_files_path = "".join(
				[
					'"',
					filename.split("\\")[-1].split(".")[0],
					".",
					ext.lower().replace(ext.lower(), "lst"),
					'"',
				]
			)  # "concat.lst" # default # "\"%s\\concat.lst\"" % script_path # clear_old
			only_short = (
				filename.split("\\")[-1].replace(old, ext).replace("..", ".")
			)  # debug(ext)
			short_file = only_short.split(".")[0]  # short
			short_file_ext = ext.lower()  # short_ext

			"""
			part_file = f"{short_file}*p{short_file_ext}".replace(
				"..", "."
			)  # debug(ext) # 'hello_01s01e01p..mp4' -> 'hello_01s01e01p.mp4' # old
			"""
			part_file = f"{short_file}_0*{short_file_ext}".replace(
				"..", "."
			)  # debug(new) / correct_run_from_project(cmd)

			new_min = 60 * 5  # 300ms(5min)

			# @job(optimize_run)

			init_ffmpeg = " ".join(
				["cmd /c", "".join([path_for_queue, "ffmpeg.exe"])]
			)  # init_ffpeg_cmd # cmd /k

			try:
				assert os.path.exists('"%s\\ext.lst"' % script_path), ""
			except AssertionError:
				logging.warning(
					"@merge_files_path no file %s for delete" % merge_files_path
				)
			else:
				try:
					os.rename(
						'"%s\\ext.lst"' % script_path, '"%s\\ext.lst.bak"' % script_path
					)
				except:
					os.remove('"%s\\ext.lst"' % script_path)
				finally:
					logging.info("os.remove ext.lst")

			try:
				# assert os.path.exists("\"%s\\concat.lst\"" % script_path), ""
				assert os.path.exists('"%s\\%s"' % (script_path, concat_files_path)), ""
			except AssertionError:
				logging.warning(
					"@concat_files_path no file %s for delete" % concat_files_path
				)
			else:
				try:
					os.rename(
						'"%s\\%s"' % (script_path, concat_files_path),
						'"%s\\%s.bak"' % (script_path, concat_files_path),
					)
				except:
					os.remove('"%s\\%s"' % (script_path, concat_files_path))
				else:
					logging.info("os.remove %s" % concat_files_path)

			# (dir /r/b/s Short_AAsBBe*p.ext) > ext.lst
			try:
				line1 = f':(dir /r/b/s "{part_file}") > {merge_files_path}'  # is_ok(debug)
			except BaseException as e1:
				line1 = ""
				logging.error("@line1 file: %s, error: %s" % (filename, str(e1)))
			else:
				logging.info("@line1 file: %s, line1: %s" % (filename, line1))

			# (for /f "delims=" %a in (ext.lst) do @echo file '%a') > concat.lst # cmd_line
			# (for /f "delims=" %%a in (ext.lst) do @echo file '%%a') > concat.lst # cmd_file
			try:
				line2 = f":(for /f \"delims=\" %%a in ({merge_files_path}) do @echo file '%%a') > {concat_files_path}"  # is_ok
			except BaseException as e2:
				line2 = ""
				logging.error("@line2 file: %s, error: %s" % (filename, str(e2)))
			else:
				logging.info("@line2 file: %s, line2: %s" % (filename, line2))

			# ffmpeg -f concat -safe 0 -y -i concat.lst -c copy Short_AAsBBe.ext
			try:
				line3 = f':{init_ffmpeg} -f concat -safe 0 -y -i {concat_files_path} -c copy "{only_short}"'  # is_ok
			except BaseException as e3:
				line3 = ""
				logging.error("@line3 file: %s, error: %s" % (filename, str(e3)))
			else:
				logging.info("@line3 file: %s, line3: %s" % (filename, line3))

			# cmd /c timeout /t 300
			try:
				line4 = f":cmd /c timeout /t {new_min}"  # is_debug
			except BaseException as e4:
				line4 = ""
				logging.error("@line4 file: %s, error: %s" % (filename, str(e4)))
			else:
				logging.info("@line4 file: %s, line4: %s" % (filename, line4))

			# cmd /c del /f {merge_files_path}
			try:
				line5 = f":cmd /c del /f {merge_files_path}"  # is_ok
			except BaseException as e5:
				line5 = ""
				logging.error("@line5 file: %s, error: %s" % (filename, str(e5)))
			else:
				logging.info("@line5 file: %s, line5: %s" % (filename, line5))

			# cmd /c del /f concat.lst
			try:
				line6 = f":cmd /c del /f {concat_files_path}"  # is_ok
			except BaseException as e6:
				line6 = ""
				logging.error("@line6 file: %s, error: %s" % (filename, str(e6)))
			else:
				logging.info("@line6 file: %s, line6: %s" % (filename, line6))

			# cmd /c del /f "Hello_01s01e*p.mp4"
			try:
				line7 = f':cmd /c del /f "{part_file}"'  # is_optimal_run(is_delete) / segment_run(no_delete) # *p(default) -> _0*(segment)  # debug(new)
			except BaseException as e7:
				line7 = ""
				logging.error("@line7 file: %s, error: %s" % (filename, str(e7)))
			else:
				logging.info("@line7 file: %s, line7: %s" % (filename, line7))

			some_dict[filename].append(line1.replace("__", "_"))  # list_files
			some_dict[filename].append(line2.replace("__", "_"))  # concat_list_files
			some_dict[filename].append(line3.replace("__", "_"))  # concat_by_ffmpeg

			some_dict[filename].append(line4.replace("__", "_"))  # if_need_timer

			some_dict[filename].append(
				line5.replace("__", "_")
			)  # remove("ext.lst") # is_ok
			some_dict[filename].append(
				line6.replace("__", "_")
			)  # remove("concat.lst") # is_ok

			some_dict[filename].append(
				line7.replace("__", "_")
			)  # remove_old_parts # is_ok

	if all(
		(
			is_trim,
			pr_le_sc.count(False) > 0
		)
	):  # is_trim / "skip_trim" / need_optimize
		mx = len(str(len(dl))) + 1  # dl ~ parts

		for k, v in dl.items():

			mp4, old = "mp4", filename.split(".")[-1]  # for_slice(any)

			try:
				assert bool(mp4 == old), ""
			except AssertionError:
				old = filename.split(".")[-1]
				ext = "".join([".", "mp4"])  # another_ext
			else:
				old = ext = "".join([".", "mp4"])  # default_ext

			# cnt += 1 # old_pos

			# logging.info("%s [%s]" % (video_filter, filename)) # is_heap(kucha/no_log)

			# test(2003) -> test(2003)_01p # filename_01s01e -> filename_01s01e01p

			# ? / Assasin_iz_buduxhego_HD(2020)01p_.mp4

			# if all((not year_regex.findall(filename), ffmpeg)):
			# cmd_line.append("-movflags faststart") # seek(0)

			# ext_filter = if ext

			# ext(mp4)

			# mx = len(str(def_parts))

			sep_for_file = "".join(["_", one_to_double(cnt, mx=mx), "p", ext]).replace(
				"__", "_"
			)

			ofilename = "".join(
				['"', path_to_done, "".join([short_name, sep_for_file, '"'])]
			)  # for_big_films(low_end_pc)

			cmd_str.append(
				" ".join(
					[
						init_ffmpeg,
						" ".join(["-ss", k]),
						init_file,
						" ".join(["-to", v]),
						init_nometa_vfile,
						video_filter,
						init_afile,
						ofilename,
					]
				)
			)  # -ss / -to # append_sequence

			cnt += 1  # new_pos(is_add_all) # debug

			# debug(save_in_dict)
			if not save_last[0]:  # multiple_lines
				if not filename in [*some_dict]:
					some_dict[filename] = [
						space_regex.sub(" ", cmd_str[-1]).replace("__", "_")
					]
				else:
					some_dict[filename].append(
						space_regex.sub(" ", cmd_str[-1]).replace("__", "_")
					)
			elif save_last[0]:  # only_last_line(debug)
				some_dict[filename] = [
					space_regex.sub(" ", "".join([":", cmd_str[-1]])).replace("__", "_")
				]  # wait_last_cmd
				# break # only_first

		try:
			concat_short_to_original(
				filename
			)  # mutliple_part # debug(is_merge=False/no_concat)
		except BaseException as e:
			concat_short_to_original_err = (filename, str(e))
			logging.error(
				"@concat_short_to_original file: %s, error: %s"
				% concat_short_to_original_err
			)
		else:
			logging.info(
				"@concat_short_to_original added 'new lines' in file: %s" % filename
			)

	elif all(
		(
			not is_trim,
			pr_le_sc.count(False) > 0
		)
	):  # is_no_trim / need_optimize
		parts = 0

		ofilename = "".join(['"', path_to_done, "".join([short_name, ext]), '"'])

		logging.info("%s [%s]" % (video_filter, filename))

		cmd_str.append(
			" ".join(
				[
					init_ffmpeg,
					init_file,
					init_nometa_vfile,
					video_filter,
					init_afile,
					ofilename,
				]
			)
		)  # append_cmd

		if not filename in [*some_dict]:
			some_dict[filename] = [
				space_regex.sub(" ", cmd_str[-1]).replace("__", "_")
			]  # update_every_time
		else:
			some_dict[filename].append[
				space_regex.sub(" ", cmd_str[-1]).replace("__", "_")
			]

		try:
			concat_short_to_original(filename, is_merge=False)  # one_part
		except BaseException as e:
			concat_short_to_original_err = (filename, str(e))
			logging.error(
				"@concat_short_to_original file: %s, error: %s"
				% concat_short_to_original_err
			)
		else:
			logging.info(
				"@concat_short_to_original no need add lines in file: %s" % filename
			)

	# """
	not_ready_dict: dict = {}
	# ready_dict: dict = {} # skip_ready

	if some_dict:
		some_dict = {
			k: v for k, v in some_dict.items() if os.path.exists(k) and v
		}  # full_base

		not_ready_dict = {
			k: v
			for k, v in some_dict.items()
			if list(filter(lambda x: "ffmpeg" in x, tuple(v)))
		}  # not_optimized(+concat)
		# ready_dict = {
		# k:v for k, v in some_dict.items() if list(filter(lambda x: "ffplay" in x, tuple(v)))
		# } # optimized

	some_dict = (
		not_ready_dict if not_ready_dict else some_dict
	)  # not_ready_files / all_files
	# """

	# """
	open(not_ready_base, "w", encoding="utf-8").close()  # clean

	try:
		assert not_ready_dict, ""
	except AssertionError:
		logging.warning("@not_ready_dict no new jobs")
	else:
		logging.info("@not_ready_dict add %d new jobs" % len(not_ready_dict))

	with open(not_ready_base, "w", encoding="utf-8") as nrbf:
		json.dump(
			not_ready_dict, nrbf, ensure_ascii=False, indent=4, sort_keys=True
		)  # save_not_optimized # debug(is_not_null)
	# """

	"""
	open(ready_base, "w", encoding="utf-8").close()

	try:
		assert	ready_dict, ""
	except AssertionError:
		logging.warning("@ready_dict no optimized jobs")
	else:
		logging.info("@ready_dict add %d new optimized jobs" % len(ready_dict))

		with open(ready_base, "w", encoding="utf-8") as rbf:
			json.dump(ready_dict, rbf, ensure_ascii=False, indent=4, sort_keys=True)	# save_optimized # debug(is_not_null)
	"""

	k_skip = []

	# create_cmd_file_after_generate(filter) # default_filter_job
	for k, v in some_dict.items():
		if os.path.exists(".".join([k, "bak"])):  # skip_backup
			try:
				os.remove(k.replace(sf.split(".")[-1], "cmd"))  # delete_from_src
			except BaseException as e:
				logging.error("@some_dict/@k/@error %s" % (k, str(e)))
			else:
				k_skip.append(k.split("\\")[-1])
				logging.info("@some_dict/@k %s" % k)

			continue

		try:
			assert os.path.exists(k), ""
		except AssertionError:
			logging.warning("@k no file %s exists" % k)
		else:
			logging.info("Файл %s найден и будет записано %d строк(и)" % (k, len(v)))				

			with open(
				k.replace(k.split(".")[-1], "cmd"), "w", encoding="utf-8"
			) as mcf:  # save_new_cmd(is_multi_line)

				mcf.writelines("%s\n" % cmd for cmd in v)  # multicommander(list)
				# mcf.writelines("%s\\\n" % cmd for cmd in v) # totalcommander(list)

			try:
				fsize1 = os.path.getsize(k.replace(k.split(".")[-1], "cmd"))
			except:
				fsize1 = 0

			move(
				k.replace(k.split(".")[-1], "cmd"),
				os.path.join(
					path_to_done, k.split("\\")[-1].replace(k.split(".")[-1], "cmd")
				),
			)  # if_not_found_cmd_file_in_dst

			try:
				fsize2 = os.path.getsize(
					os.path.join(
						path_to_done, k.split("\\")[-1].replace(k.split(".")[-1], "cmd")
					)
				)
			except:
				fsize2 = 0

			try:
				assert all(
					(fsize2, os.path.exists(k.replace(k.split(".")[-1], "cmd")))
				), ""
			except AssertionError:
				logging.warning("@fsize2/@cmd %s is null or not exists" % k)
			else:
				os.remove(
					k.replace(k.split(".")[-1], "cmd")
				)  # if_found_cmd_file_in_src
	else:
		logging.info("end calc_parts %s" % str(datetime.now()))

	# @trimmer_base; load / create(if_error)
	try:
		with open(trimer_base, encoding="utf-8") as tbf:
			some_dict = json.load(tbf)
	except BaseException:
		some_dict = {}

		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)

	try:
		assert some_dict, ""
	except AssertionError:
		logging.warning("@some_dict is null")
	else:
		some_dict: dict[str, list] = {
			k2:v2 for k2, v2 in some_dict.items() if not k2.split("\\")[-1] in k_skip
		}  # skip_files_not_included # python 3.9(-hide/debug)

		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)		

	try:
		assert some_dict, ""
	except:
		some_dict = {}
	else:
		some_dict = {
			k: v for k, v in some_dict.items() if os.path.exists(k) and v
		}

	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump(
			some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=True
		)  # default_save(exists/cmd_file)

	# del some_dict # clear_mem # debug
	return cmd_str


async def scan_folder(
	fsf: str = "", ext=".mp4", filter_list: list = []
) -> list:  # docstring(description)
	"""fsf - folders(str), ext - extention(str), filter_list - short_text(list)"""
	folders = files = []

	folders_dict: dict = {}

	# generate_files_from_folder
	try:
		folders: list[str] = [
			os.path.join(a, cf)
			for a, _, c in os.walk(fsf)
			for cf in c
			if os.path.isdir(a)
		]  # in_folders # python 3.9(-hide/debug)

		assert folders, ""
	except AssertionError:
		folders: list[str] = [
			os.path.isdir(a, bf)
			for a, b, _ in os.walk(fsf)
			for bf in b
			if os.path.isdir(os.path.join(a, bf))
		]  # in_subfodlers # python 3.9(-hide/debug)
	finally:
		logging.info("@folders %s" % ";".join(folders))

	folders = sorted([*folders], key=os.path.getctime) if folders else []  # getmtime -> debug(getctime/optimal)

	files: list[str] = [
		os.path.join(folders, f)
		for f in os.listdir(folders)
		if os.path.isfile(os.path.join(folders, f)) and video_regex.findall(f)
	]  # python 3.9(-hide/debug)

	return files


def ms_to_time(ms: int = 0, mn: int = 60) -> int:  # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	try:
		h, m, s = (
			ms // 3600, ms % 3600 // 60, ms % 3600 % 60
		)
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


def difference_time(date1, date2):
	# '2024-05-15 19:38:57.349599'

	h1, m1, s1 = date1.hour, date1.minute, date1.second
	h2, m2, s2 = date2.hour, date2.minute, date2.second

	hours1 = "0%d" % h1 if h1 < 10 else h1
	minutes1 = "0%d" % m1 if m1 < 10 else m1
	seconds1 = "0%d" % s1 if s1 < 10 else s1

	hours2 = "0%d" % h2 if h2 < 10 else h2
	minutes2 = "0%d" % m2 if m2 < 10 else m2
	seconds2 = "0%d" % s2 if s2 < 10 else s2

	try:
		start = datetime.strptime("%s:%s:%s" % (hours1, minutes1, seconds1), "%H:%M:%S")
		end = datetime.strptime("%s:%s:%s" % (hours2, minutes2, seconds2), "%H:%M:%S")
	except:
		start = end = 0

	difference = end - start

	return difference


"""
Можно ли имея промежуток времени от начала до текущего времени, суммы файлов и размера
каждого файла отдельно, получить расчетное время обработки файлов? Ранее видел что-то
типа размер файла разделить на промежуток времени чтобы получить скорость обработки файла.
Так как после размер файла разделить на скорость получаем "расчетное" время обработки файла
"""


# @count_time
"""
Дано:
A - Количество итераций (кол-во файлов максимум)
B - среднее время одной операции 1 / abs(date1 - date2).seconds
C - время начала обработки (time())
Найти:
D - время до конца (time())
Решение:
D = C + (A * B) # new_time = datetime.now() - timedelta(seconds=60); print("%s:%s:%s" % (str(new_time.hour), str(new_time.minute), str(new_time.second))) # ?
"""


# speed_calc(filename, date1, date2, /) -> int:  # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
'''
def speed_calc(filename, date1, date2):
	"""скорость обработки данных (v = s / t)"""
	speed_file: float = 0

	sizes_dict: dict = {}

	sizes_dict[1] = "Kb"
	sizes_dict[2] = "Mb"
	sizes_dict[3] = "Gb"

	try:
		fsize = os.path.getsize(filename)
	except BaseException as e:
		fsize = 0
		logging.error("@fsize %s" % str(e))
	else:
		logging.info("@fsize %d" % fsize)

		try:
			speed_file = fsize / abs(date1 - date2).seconds  # S = A / T # скорость передачи # V = S / T

			assert all(
				(speed_file, abs(date1 - date2).seconds > 0)
			), ""  # speed_file > 0, time > 0
		except AssertionError:
			logging.warning("@speed_file is null, current: %s" % filename)
		except BaseException as e:  # division by zero
			speed_file, speed_file_err = 0, (filename, str(e))
			logging.error("@speed_file current: %s, error: %s" % speed_file_err)

		try:
			speed_file = (
				int(speed_file) if not isinstance(speed_file, int) else speed_file
			)
		except:  # ValueError
			speed_file = 0

		speed_convert = ""

		speed_convert = " ".join([speed_file // (1024 ** 2), "mb/s"]) if speed_file // (1024 ** 2) > 0 else " ".join([speed_file // (1024 ** 2), "kb/s"])

		logging.info("@speed_file %d [%s] current: %s" % (speed_file, speed_convert, filename))

		try:
			speed_list = [
				(speed_file // (1024**i), sizes_dict[i])
				for i in range(1, 4)
				if speed_file // (1024**i) > 0
			]
			assert speed_list, ""
		except AssertionError:
			logging.warning("@speed_list no speed current: %s" % filename)
		except BaseException as e:
			speed_list, speed_list_err = [], (filename, str(e))
			logging.error("@speed_list current: %s, error: %s" % speed_list_err)
		else:
			logging.info("@speed_list %s, current: %s" % (str(speed_list), filename))

		"""
		video_trimmer2.py [ LINE: 1203 ]#     INFO [2024-04-29 14:59:25,019]  @fsize 87045762
		video_trimmer2.py [ LINE: 1211 ]#     INFO [2024-04-29 14:59:25,021]  @speed_file 4145036.285714286 mb/s
		video_trimmer2.py [ LINE: 1223 ]#     INFO [2024-04-29 14:59:25,022]  @speed_list [(4047, 'Kb'), (3, 'Mb')]
		"""

	return speed_file
'''


# time_calc(filename, speed_file, /) -> int:  # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
'''
def time_calc(filename, speed_file):
	"""время обработки файла ( t = s / v)"""
	time_file = 0.0
	time_list = []

	try:
		fsize = os.path.getsize(filename)
	except:
		fsize = 0
	else:
		logging.info("@fsize %d" % fsize)

		nfsize = 0  # ntime = 0

		is_gb = fsize // (1024**3) > 0

		if is_gb:
			nfsize = (
				fsize // (1024**3)
			) * 1024  # gb -> mb # ntime = nfsize / speed_file # время передачи (T)

		try:
			time_file = (
				nfsize / speed_file if nfsize else fsize / speed_file
			)  # T = A / S # время передачи # default(one_file) # T = S / V
			assert all((time_file, speed_file)), ""  # time_file > 0, speed_file > 0
		except AssertionError:
			logging.warning("@time_file is null current: %s" % filename)
		except BaseException as e:  # division by zero
			time_file, time_file_err = 0, (filename, str(e))
			logging.error("@time_file current: %s, error: %s" % time_file_err)

		time_str = ""

		try:
			time_file = (
				int(time_file) if not isinstance(time_file, int) else time_file
			)
		except:  # ValueError
			time_file = 0

		# hh / mm # mm # S/T = 4145036,2857142857142857142857143 # 23:56
		try:
			time_list = [
				time_file // 3600,
				time_file % 3600 // 60,
				time_file % 3600 % 60,
			]  # hh /mm/ss
			assert time_list, ""
		except AssertionError:
			time_list = [0, 0, 0]
			logging.warning("@time_list no time for %s" % filename)
		else:
			filter_time = list(filter(lambda x: x, tuple(time_list)))
			time_list = filter_time[:]
			time_list_str = (":".join(map(str, time_list)), filename)
			logging.info("@time_list(@time_file) %s, current: %s" % time_list_str) # time_file ~ time_list

		try:
			with open(filename_length_json, encoding="utf-8") as flj:
				fl = json.load(flj)
		except:
			fl = {}

			with open(filename_length_json, "w", encoding="utf-8") as flj:
				json.dump(fl, flj, ensure_ascii=False, indent=4, sort_keys=True)

		if len(time_list) >= 1:
			time_str = ",".join(str(time_list).replace(" ", "").split(","))
			fl[filename] = "@time_list %s" % time_str
			logging.info("@time_list %s" % time_str)

		logging.info(
			"@fl @time_by_framecount %s" % ";".join(map(str, [filename, fl[filename]]))
		)

		try:
			fl = {
				k: v for k, v in fl.items() if os.path.exists(k)
			}

			assert fl, ""
		except AssertionError:
			logging.warning("@fl no filenames with length, current: %s" % filename)
		else:
			fl_str = (len(fl), filename)
			logging.info("@fl %d filenames with length, current: %s" % fl_str)

			with open(filename_length_json, "w", encoding="utf-8") as flj:
				json.dump(fl, flj, ensure_ascii=False, indent=4, sort_keys=True)

			# del fl # clear_mem # debug

	"""
	video_trimmer2.py [ LINE: 1237 ]#     INFO [2024-04-29 14:59:25,026]  @fsize 87045762
	video_trimmer2.py [ LINE: 1256 ]#     INFO [2024-04-29 14:59:25,027]  @time_file 21
	video_trimmer2.py [ LINE: 1286 ]#     INFO [2024-04-29 14:59:25,031]  @time_list 00, 21 [current_hour]
	"""

	return time_file
'''


# data_calc(filename, time_file, speed_file, /) -> int:  # *(pos_or_keyw), ... # ..., \(pos) # python 3.8
'''
def data_calc(filename, time_file, speed_file):
	"""общий размер файла (s = t * v)"""
	sizes_dict: dict = {}

	sizes_dict[1] = "Kb"
	sizes_dict[2] = "Mb"
	sizes_dict[3] = "Gb"

	try:
		data_file = time_file * speed_file  # A = T * S # сколько данных было передано # S = T * V
		
		assert data_file, ""
	except AssertionError:
		logging.warning("@data_file is null, current: %s" % filename)
	except BaseException as e:
		data_file, date_file_err = 0, (filename, str(e))
		logging.error("@data_file current: %s, error: %s" % date_file_err)

	try:
		data_file = (
			int(data_file) if not isinstance(data_file, int) else data_file
		)
	except:  # ValueError
		data_file = 0

	# diff_status = True if (data_file / os.path.getsize(filename)) * 100 == 100 else False # equal(True) / diff(False)
	try:
		diff_value = (data_file / os.path.getsize(filename)) * 100  # percent
	except:
		diff_value = 0

	logging.info(
		"@data_file: %s, @diff_percent: %s, current: %s"
		% (
			str(data_file),
			str(diff_value),
			filename,
		)
	)  # "<->".join(map(str, [data_file, os.path.getsize(filename)])) -> str((data_file / os.path.getsize(filename))*100)

	try:
		data_list = [
			(data_file // (1024**i), sizes_dict[i])
			for i in range(1, 4)
			if data_file // (1024**i) > 0
		]
		assert data_list, ""
	except AssertionError:
		logging.warning("@data_list no data current: %s" % filename)
	except BaseException as e:
		data_list, date_list_err = [], (filename, str(e))
		logging.error("@data_list current: %s, error: %s" % date_list_err)
	else:
		date_list_str = (str(data_list), filename)
		logging.info("@data_list %s, current: %s" % date_list_str)

	"""
	video_trimmer2.py [ LINE: 1331 ]#     INFO [2024-04-29 14:59:25,039]  @data_file 87045756
	video_trimmer2.py [ LINE: 1341 ]#     INFO [2024-04-29 14:59:25,040]  @data_list [(85005, 'Kb'), (83, 'Mb')]
	"""

	return data_file
'''


def fspace(src: str = "", dst: str = "") -> bool:  # 11  # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
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
	except:
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


def avg_calc(s, l, /):  # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
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
):  # fs = real_fs // (1024 * 2), sp = (10/8) * 1024 # 10/8 mb/s(real_speed~10mb) * 1024 kb(is_convert~1280kb)
	"""
	>>> fs, sp = 865, 1280
	>>> fs / sp # 0.67578125
	>>> (fs * 1024) / sp # 692.0
	>>> ((fs * 1024) / sp) // 60 # 	11.0
	>>> ((fs * 1024) / sp) % 60 # 32.0
	"""
	try:
		fs = os.path.getsize(filename) / (1024**2)
	except:  # if_not_exists
		fs = 0
	finally:
		try:
			assert bool(fs == int(fs)), ""
		except AssertionError:
			fs = int(fs)

	try:
		sp = (sp / 8) * 1024
	except:  # value_error
		sp = 0
	finally:
		try:
			assert bool(sp == int(sp)), ""
		except AssertionError:
			sp = int(sp)

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


# lanczos -> neighbor -> some? # need_best_quailiy # default(downscale), debug(upscale) # insert_in_cmd(debug/test)
def upscale_video(
	width: int = 640, height: int = 480, resolution: str = "1080"
):  # r(resolution) # debug(need_test's) # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	"""
	# @outupt_%flags%_(width)i(height)p.%ext% / example: "Klon(2021)_lanczos_900i480p_.mp4"

	# @if_new
	# ffmpeg.exe -hide_banner -y -i "input" -map_metadata -1 -preset medium -threads 2 -c:v libx264  -profile:v main  -vf scale=ow:oh:flags=lanczos  -threads 2 -c:a aac -af "dynaudnorm" -f segment -segment_time {tp} "output__%03d.mp4"
	# ffmpeg.exe -hide_banner -y -i "input" -map_metadata -1 -preset medium -threads 2 -c:v libx264  -profile:v main  -vf scale=ow:oh:flags=lanczos  -threads 2 -c:a aac -af "dynaudnorm" -start_number 0 -hls_time {tp} -hls_list_size 0 -f hls -hls_segment_filename "output__%03d.ts" "playlist.m3u8"

	# flags=print_info+lanczos -> logging(scaling)

	# @compare_quality_"after_resize"
	# ffmpeg -i video1.mp4 -i video2.mp4 -filter_complex hstack result.mp4 # video_in_horizontal_row(is_one_height_only)
	# ffmpeg -i video1.mp4 -i video2.mp4 -i video3.mp4 -filter_complex vstack=3 result.mp4 # video_in_vertical_col(is_one_width_only)

	# @if_ready(some_this) # !!test_and_use, !calc, "!"no_test
	!!<input> -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:-1:-1,setsar=1" -r 60 -threads 2 -c:a copy <output>; {width}i:{height}p<:{padx}:{pady}><decrease> # hd(720p) + fps(60) # black_borders # scaling(+)
	!!<input> -vf "scale=640:trunc(ih/iw)*ow:flags=lanczos" <output>; ow/iw/ih; (width)i:(height)p<(flags)lanczos> # sd(360p/480p), hd(720p/1080p), 4k(2160p) # calc(debug)!
	!!<input> -vf "scale=trunc(iw/ih)*oh:360:flags=lanczos" <output>; ow/iw/ih; (width)i:(height)p<(flags)lanczos> # calc(debug)!
	!<input> -vf "scale=%04d:-1:flags=lanczos" -threads 2 -c:v libx264 -preset medium -crf 21 -threads 2 -c:a copy <output>; (width)i:(height)p<(flags)lanczos> # sd(360p/480p)/hd(720p/1080p)/4k(2160p) # calc!
	!<input> -vf "scale=-1:%04d:flags=lanczos" -threads 2 -c:v libx264 -preset medium -crf 21 -threads 2 -c:a copy <output>; (width)i:(height)p<(flags)lanczos> # calc!
	!<input> -vf "scale=1280:-2:flags=lanczos,format=yuv420p" <output>; (width)i:(height)p/(flags)lanczos/(format)yuv420p # calc!
	!<input> -vf "scale=320:240:force_original_aspect_ratio=1,pad=320:240:(( (ow - iw)/2 )):(( (oh - ih)/2 ))" <output>; ow/oh/iw/ih; {width}i:{height}p<{padx}:{pady}> # sd(240p) # calc!
	!<input> -vf "scale=iw*2:ih*2:flags=lanczos,scale=-2:720" <output>; iw/ih; (width)i:(height)p<(flags)lanczos> # calc!
	<input> -vf "scale=640x360:flags=lanczos" -preset slow -crf 21 -threads 2 -c:a copy <output>; {width}ix{height}p<(flags)lanczos> # sd(360p/480p), hd(720p/1080p), 4k(2160p)
	<input> -vf "scale=w=256:h=256:force_original_aspect_ratio=increase,crop=256:256" <output>; (width)i:(height)p<increase> # cover # crop_to_fit(-)
	{"scale": [
			width, height, eval, interl, flags, "size, s", in_color_matrix/out_color_matrix, in_range/out_range, in_chroma_loc/out_chroma_loc,
			force_original_aspect_ratio, force_divisible_by, in_w/in_h, iw/ih, out_w/out_h, ow/oh, a, sar, dar, hsub/vsub, ohsub/ovsub, n,
			t, pos, "ref_w, rw", "ref_h, rh", ref_a, "ref_dar, rdar", ref_n, ref_t, ref_pos
			]}
	"""

	# samples # [(720, 384, "D:\\Downloads\\Temp\\Kino\\Klon(2021)_.mp4")]
	# trunc(iw/ih)*oh:480 ~ 960:480; 640:270; (ow > iw, oh > ih, ow != oh); padx, pady = (960 - 640) / 2 = 160, (480 - 270) / 2 = 105 -> -1:480
	# 720:trunc(ih/iw)*ow ~ 720:270; 640:270; (ow > iw, oh == ih); padx, pady = (720 - 640) / 2 = 40, oh  # debug(ffmpeg/test) -> 720:-1
	# 960:480 <-> 720:270

	# 900:480; 720:384; padx, pady = (900 - 720) / 2 = 90, (480 - 384) / 2 = 48

	# (up/down)scale_(neighbor/lanczos/(bicubic/bilinear)) # debug(test)

	# sd(360p/480p), hd(720p/1080p), 4k(2160p)

	pass


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
		# logging.error(";".join(["debug soundnotify[error]",	"Не смог произнести текст! [%s]" % str(e)]))
	else:
		if text:
			print(Style.BRIGHT + Fore.GREEN + "Текст [%s] успешно произнесён" % text)
			# logging.info(";".join(["debug soundnotify[ok]", "Текст [%s] успешно произнесён" % text]))


def find_percent(value: int = 0, percent: int = 0):  # hide # *(pos_or_keyw), ... # ..., /(pos) # python 3.8
	# return value * (percent / 100)  # 20000 * (30 / 100) = 6000
	return (value * percent) / 100  # (80 * 30) / 100 ~ 24 -> 8 * 3 = 24


# debug(for_use)
"""
The method "utcnow" in class "datetime" is deprecated
  Use timezone-aware objects to represent datetimes in UTC; e.g. by calling .now(datetime.timezone.utc)Pylance
(method) def utcnow() -> datetime
Construct a UTC datetime from time.time().
"""
"""
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
"""	


if __name__ == "__main__":  # skip_main(debug)

	all_period_dict = {}

	folders_filter = []

	try:
		with open(all_period_json, encoding="utf-8") as apjf:
			all_period_dict = json.load(apjf)
	except:
		all_period_dict = {}

	folders_filter = [v[0].strip() for k, v in all_period_dict.items() if os.path.exists(v[1])] if all_period_dict else []

	dt = datetime.now()

	filter_list = main_filter = []

	# """
	# @day
	try:
		with open(days_ago_base, encoding="utf-8") as dalf:
			filter1 = [d.strip() for d in filter(lambda x: x, tuple(dalf.readlines()))]
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
			filter2 = [m.strip() for m in filter(lambda x: x, tuple(mflf.readlines()))]
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
			filter3 = [c.strip() for c in filter(lambda x: x, tuple(cylf.readlines()))]
	except:
		filter3 = []

		# open(calc_year_base, "w", encoding="utf-8").close()
	else:
		main_filter += filter3
	# '''

	main_filter = list(
		set(main_filter)
	)  # if main_filter else period_list # load_last_data / known_datetime

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
			logging.info("@two_periods/@a/@b diff: %s" % ";".join(
				map(str, [a, b]))
			)
			pj_dict[a.strip()] = "%s" % b

	pj_dict = {
		k: v if k == v else v for k, v in pj_dict.items()
	}  # debug

	with open(period_json, "w", encoding="utf-8") as pjf:
		json.dump(pj_dict, pjf, ensure_ascii=False, indent=4, sort_keys=True)

	# '''
	# @period.lst(video_trimmer2) # update_period_list # save
	try:
		assert pj_dict, ""
	except AssertionError:
		logging.warning("no periods")
	else:
		# @period.lst
		with open(period_base, "w", encoding="utf-8") as pbf:
			# pbf.writelines("%s\n" % p for p in list(pj_dict.keys()))  # multicommander
			pbf.writelines("%s\\\n" % p for p in list(pj_dict.keys()))  # totalcommander
	# '''

	files_count = 0

	# @load_base(update)
	# '''
	try:
		with open(trimer_base, encoding="utf-8") as tbf:
			some_dict = json.load(tbf)
	except:
		some_dict = {}

		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump({}, tbf, ensure_ascii=False, indent=4, sort_keys=True)

	try:
		assert some_dict, ""
	except:
		some_dict = {}
	else:
		some_dict = {
			k: v for k, v in some_dict.items() if os.path.exists(k) and v
		}

	# @new_base
	"""
	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump({}, tbf, ensure_ascii=False, indent=4, sort_keys=False) # clear_after_load
	"""

	sm = ln = ag = cntfiles = sf = files_count = len_files = 0  # int
	fsizes = (
		files
	) = (
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
		# """
		try:
			assert bool(os.path.isdir(a) and a in some_subfolders), ""
		except AssertionError:
			some_subfolders.add(a)
			folders.append(a)
			logging.warning("@folders_filter folders %s is filtred" % a)
			# continue  # skip_null_folders
		else:
			logging.info("@folders_filter %s" % a)
		# """

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
					]  # subfolders # python 3.9(-hide/debug)

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

	# """
	filter_folder = []
	all_period_dict_filter = {}

	try:
		for ff, f in zip(folders_filter, folders):  # debug(product -> zip)
			if all((ff, f, ff in f)):
				filter_folder.append({"short": ff, "full": f})

		try:
			ff_data = {"filter_folder": filter_folder}
			short_ff = jmespath.search("filter_folder[*].short", ff_data)
			full_f = jmespath.search("filter_folder[*].full", ff_data)

			assert all((short_ff, len(short_ff) == len(full_f))), ""
		except AssertionError:
			logging.warning("@short_ff/@full_f some null %s" % "..".join(map(str, (short_ff, full_f))))
		else:
			logging.info("@short_ff/@full_f some null %s" % "..".join(map(str, (short_ff, full_f))))

			for a, b in zip(short_ff, full_f):  # debug(product -> zip)
				if all((a in b, a in sf.strip())):  # b - folder
					all_period_dict_filter[sf.strip()] = a  # sf - file
	except:
		all_period_dict_filter = {sf.strip(): os.path.getctime(sf) for sf in filter(lambda x: os.path.exists(x), tuple(some_files)) for _, v in all_period_dict.items() if all((v, v[0] in sf.strip()))}
		logging.warning("@all_period_dict_filter %d [2]" % len(all_period_dict_filter))
	else:
		logging.warning("@all_period_dict_filter %d [1]" % len(all_period_dict_filter))
	# """

	"""
	try:
		ag = avg_calc(sm, ln)  # avg_calc(100, 2) # 50
	except:
		ag = 0  # 0
	else:
		logging.info("@files/@folders/@ag %d %d %d" % (len(files), len(folders), ag))
	"""

	# all_period_dict[week_status.strip()] = [fsf.split("\\")[-1], fsf, len_files, week_status, ]

	def_some_files = some_files

	# find_files_by_folder
	all_period_list = sorted([*all_period_dict_filter], key=os.path.getctime)  # sort_by_create_time_file # reverse=False(abc_jobs)
	some_files = all_period_list if all_period_list else def_some_files  # (def_some_files, all_period_list)[len(all_period_list) > 0]

	# """
	n = 100
	some_filesizes = [os.path.getsize(sf) for sf in filter(lambda x: os.path.exists(x), tuple(some_files))]

	try:	
		ag = sum(some_filesizes) // len(some_filesizes)
	except:
		ag = 0
	else:
		logging.info(f"Количество обучений: {n}")

		even_count1 = sum(1 for sf in some_filesizes if sf - ag >= 0)
		probability_even1 = round((even_count1 / n) * 100) # ?

		probability1 = (True if probability_even1 > 50 else False)

		logging.info(f"Количество чисел по классификации: {even_count1}")
		logging.info(f"Вероятность классификации числа: {probability_even1:.2f}")	

		even_count2 = sum(1 for sf in some_filesizes if sf - ag < 0)
		probability_even2 = round((even_count2 / n) * 100) # ?

		probability2 = (True if probability_even2 > 50 else False)

		logging.info(f"Количество чисел по классификации: {even_count2}")
		logging.info(f"Вероятность классификации числа: {probability_even2:.2f}")

		# v - avg >= 0 # more
		try:
			some_filesizes_filter = [sf.strip() for sf in filter(lambda x: os.path.exists(x), tuple(some_files)) if probability1 and os.path.getsize(sf) - ag >= 0]  # classify_1
			assert some_filesizes_filter, ""
		except AssertionError:
			some_filesizes_filter = [sf.strip() for sf in filter(lambda x: os.path.exists(x), tuple(some_files)) if not probability1 and os.path.getsize(sf) - ag >= 0] # classify_2
			logging.warning("@some_filesizes_filter/@classify_2 %d files filter" % len(some_filesizes_filter))
		else:
			logging.info("@some_filesizes_filter/@classify_1 %d files filter" % len(some_filesizes_filter))

		if not some_filesizes_filter:
			# v - avg < 0 # less
			try:
				some_filesizes_filter = [sf.strip() for sf in filter(lambda x: os.path.exists(x), tuple(some_files)) if probability2 and os.path.getsize(sf) - ag < 0]  # classify_3
				assert some_filesizes_filter, ""
			except AssertionError:
				some_filesizes_filter = [sf.strip() for sf in filter(lambda x: os.path.exists(x), tuple(some_files)) if not probability2 and os.path.getsize(sf) - ag < 0]  # classify_4
				logging.warning("@some_filesizes_filter/@classify_4 %d files filter" % len(some_filesizes_filter))
			else:
				logging.info("@some_filesizes_filter/@classify_3 %d files filter" % len(some_filesizes_filter))

		some_files = sorted(some_filesizes_filter, key=os.path.getctime)  # classify(+date_create_file)
	# """

	some_dict = {}

	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump({}, tbf, ensure_ascii=False, indent=4, sort_keys=True)  # clear_jobs

	# logging.info("@files/@folders/@ag %d %d %d" % (len(files), len(folders), ag))

	a, cnt, last_file = len(some_files), 0, ""
	some_set = ms_set = te_set = mx_set = set()
	mx1 = mx2 = mx3 = 0
	strt, cur_iter, max_iter = (
		time(),
		0,
		len(some_files),
	)  # -> sum(some_files_fsizes) # debug
	filter_max_iter = 0
	filter_some_files = []

	sm = ln = ag = 0  # max_ag

	for sf in filter(
		lambda x: video_regex.findall(x), tuple(some_files)
	):  # pass_1_of_3
		try:
			today = datetime.now()
			fdate = os.path.getctime(sf)  # getmtime -> debug(getctime/optimal)
			ndate = datetime.fromtimestamp(fdate)
		except BaseException as e:
			sf_err = (str(e), sf)

			if sf_err[0]:
				logging.error(
					"@sf error: %s, current: %s" % sf_err
				)

			continue  # if_winerror

	for sf in filter(
		lambda x: video_regex.findall(x), tuple(some_files)
	):  # pass_2_of_3
		period_list_filter = []

		try:
			today = datetime.now()
			fdate = os.path.getctime(sf)  # getmtime -> debug(getctime/optimal)
			ndate = datetime.fromtimestamp(fdate)
		except BaseException as e:
			sf_err = (str(e), sf)

			logging.error(
				"@sf error: %s, current: %s" % sf_err
			)

			continue  # if_winerror

		try:
			days_ago = abs(today - ndate).days
			assert bool(days_ago >= 0), ""
		except AssertionError:  # if_none(today)
			continue  # days_ago = 0
		else:
			logging.info("@days_ago %d days ago, file: %s" % (days_ago, sf))

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

	# short_files
	# '''
	"""
	short_list: list[str] = list(
		set([crop_filename_regex.sub("", sf.split("\\")[-1]) for sf in some_files])  # short_filename(template)
	)  # some_jobs
	"""
	short_list: list[str] = [sf.split("\\")[-1].strip() for sf in filter(lambda x: os.path.getctime(x), tuple(some_files))]  # # short_filename(no_path)
	short_list.sort()

	# @fcd.txt
	with open(combine_base, "w", encoding="utf-8") as cbf:  # fcd.txt
		# cbf.writelines("%s\n" % sl for sl in filter(lambda x: len(x) > 1, tuple(short_list)))  # multicommander(is_short)
		cbf.writelines(
			"%s\\\n" % sl for sl in filter(lambda x: len(x) > 1, tuple(short_list))
		)  # totalcommander(is_short)
	# '''

	# [filename, length, filesize, short_filename, seas_or_year, split_filename + regex, seasepis_or_year, moddate)} # list(params)

	# import os
	# import re
	# crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)", re.I)

	# filename = "F:\\Videos\\Serials\\Serials_Conv\\2_Broke_Girls\\2_Broke_Girls_06s17e.mp4"
	# filename = "F:\\Videos\\Kino\\Big_films\\1956\\Vesna_na_Zarechnoy_ulitse(1956)_Rus.mp4"

	# ['2', 'Broke', 'Girls', '06s17e'] # ['Vesna', 'na', 'Zarechnoy', 'ulitse(1956)', 'Rus']
	try:
		keywords = (
			sf.split("\\")[-1].split(".")[0].split("_")
			if len(sf.split(".")[0].split("_")) > 0
			else [sf.split("\\")[-1].split(".")[0]]
		)
		def_k = keywords

		# ['2', 'Broke', 'Girls'] # ['Vesna', 'na', 'Zarechnoy', 'ulitse(1956)']
		keywords = (
			def_k[0 : len(def_k) - 1]
			if len(def_k[0 : len(def_k) - 1]) > 0
			else def_k[0:]
		)

		# '2_Broke_Girls' # 'Vesna_na_Zarechnoy_ulitse(1956)'
		keywords = "_".join(keywords)
	except BaseException as e:
		keywords, keywords_err = "", (str(e), sf)
		logging.error("@keywords error: %s, current: %s" % keywords_err)
	else:
		keywords_str = (keywords, sf)
		logging.info("@keywords keywords: %s, current: %s" % keywords_str)

	# @full
	# sort_type = (
	# filename.split("\\")[-1], os.path.getsize(filename), crop_filename_regex.sub("", filename.split("\\")[-1]), ";".join(crop_filename_regex.findall(filename.split("\\")[-1])[0]).split(";")[0], keywords, os.path.getmtime(filename)
	# )
	# ('2_Broke_Girls_06s17e.mp4', 60670359, '2_Broke_Girls', '_06s', '2_Broke_Girls', 1552443441.0)
	# ('Vesna_na_Zarechnoy_ulitse(1956)_Rus.mp4', 423755212, 'Vesna_na_Zarechnoy_ulitse', '(1956)', 'Vesna_na_Zarechnoy_ulitse(1956)', 1722523488.086902)

	sl_regex = re.compile(r"(\(|_).*\..*", re.I)
	# video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg))$", re.M)
	# some_files = [
	# os.path.join(os.getcwd(), f) for f in os.listdir(os.getcwd())
	# ] # debug
	# short_filename / sorted_by_filesize(int) / sorted_by_short_filename(str) / "sorted_by_seas_or_year(str)" / "sorted_keywords(list)" / sorted_by_modifydate(float)

	file_and_time = fat_sort = []

	cinema_filter = tvseries_filter = False

	seas_regex = re.compile(r".*(_[\d+]{2,4}s).*", re.I)
	year_regex = re.compile(r".*(\([\d+]{4}\)).*", re.I)

	sort_index = 0 # short_filename(no_path)

	# cinema(sort)
	for sf in filter(lambda x: year_regex.findall(x), tuple(some_files)):
		try:
			assert sf, ""
		except AssertionError:
			continue
		else:
			cinema_filter = True
	else:
		if cinema_filter:
			sort_index = 2 # filesize

	# tv_series(sort)
	for sf in filter(lambda x: seas_regex.findall(x), tuple(some_files)):
		try:
			assert sf, ""
		except AssertionError:
			continue
		else:
			tvseries_filter = True
	else:
		if tvseries_filter:
			sort_index = 4 # date_create_file	

	logging.info("@sort_index/cinema_filter/tvseries_filter %s" % ";".join(
		map(str, (sort_index, cinema_filter, tvseries_filter)))
	)

	# """
	try:
		# fullname = [0], short = [1] / fsize = [2] / short_no_seasyear [3] / mtime [-1] # debug(sort_type)
		file_and_time = [
			(
				sf.strip(),
				sf.split("\\")[-1],
				os.path.getsize(sf),
				crop_filename_regex.sub("", sf.split("\\")[-1]),
				os.path.getctime(sf),
			)
			for sf in filter(lambda x: video_regex.findall(x), tuple(some_files))
		]  # data_for_sort # getmtime -> debug(getctime/optimal)

		# fat_sort = sorted(file_and_time, key=lambda file_and_time: file_and_time[1]) # sort_by_key(abc)
		# fat_sort = sorted(file_and_time, key=lambda file_and_time: file_and_time[1]) # sort_by_key(filesize)
		fat_sort = sorted(
			file_and_time, key=lambda file_and_time: -file_and_time[sort_index]
		)  # sort_by_key(short_filename) # -file_and_time[sort_index] -> reverse(True)(cba) # file_and_time[sort_index] -> reverse(False)(abc)
		# fat_sort = sorted(file_and_time, key=lambda file_and_time: file_and_time[2]) # sort_by_key(modtime)
	except BaseException as e:
		logging.error("@file_and_time error: %s" % str(e))
	else:
		file_and_time = fat_sort
		# debug # @combine_base2
		try:
			short_list2 = [f[1].strip() for *f, _ in file_and_time if os.path.exists(f[0]) and f[1]] # if_exist_file_and_have_short_filename(sort_by_index)

			assert short_list2, ""
		except AssertionError:  # if_null
			logging.warning(
				"@short_list2 is null, but files: %d sorted" % len(file_and_time)
			)
		except BaseException as e2:  # if_error
			logging.error("@short_list2 error: %s" % str(e2))
		else:
			# @fcd_.txt
			with open(combine_base2, "w", encoding="utf-8") as cbf2:  # fcd_.txt
				cbf2.writelines(
					"%s\n" % sl
					for sl in filter(lambda x: len(x) > 1, tuple(short_list2))
				)  # multicommander(is_short)
				# cbf2.writelines("%s\\\n" % sl2 for sl2 in filter(lambda x: len(x) > 1, tuple(short_list2)))  # totalcommander(is_short)

		logging.info("@file_and_time, files: %d sorted" % len(file_and_time))
	# """

	trimmer_dict = {}

	t = Timer(max_iter)

	date1 = datetime.now()

	current_dict = {}

	with open(current_json, "w", encoding="utf-8") as cjf:
		json.dump({}, cjf, ensure_ascii=False, indent=4, sort_keys=False)

	# @(create/remove)_cmd_in_src_folder
	for sf in filter(
		lambda x: video_regex.findall(x), tuple(some_files)
	):  # pass_3_of_3
		cmd_str = []

		last_file = sf

		date2 = datetime.now()

		try:
			# sc = speed_calc(sf, date1, date2)  # debug(manual)
			sc = os.path.getsize(sf) // abs(date1-date2).seconds
		except:
			sc = 0
		else:
			def_sc = sc  # backup(speed)

			while sc // (1024**2) > 0:
				try:
					sc //= (1024**2)
					logging.info("@sc %d, current: %s" % (sc, sf))
				except:
					sc = def_sc  # restore(last_speed)
					break
				else:
					def_sc = sc
			else:  # if_no_break
				sc = def_sc  # restore

			sc = def_sc  # use_last

		try:
			# tc = time_calc(sf, sc)  # debug(manual)
			tc = os.path.getsize(sf) // sc
		except:
			tc = 0
		else:
			def_tc = tc  # backup(time)

			while tc // (1024**2) > 0:
				try:
					tc //= (1024**2)
					logging.info("@tc %d, current: %s" % (tc, sf))
				except:
					tc = def_tc  # restore(last_time)
					break
				else:
					def_tc = tc
			else:  # if_no_break
				tc = def_tc  # restore

			tc = def_tc	 # use_last		

		try:
			# dc = data_calc(sf, tc, sc)  # debug(manual)
			dc = sc * tc
		except:
			dc = 0
		else:
			def_dc = dc  # backup(data)

			while dc // (1024**2) > 0:
				try:
					dc //= (1024**2)
					logging.info("@dc %d, current: %s" % (dc, sf))
				except:
					dc = def_dc  # restore(last_data)
					break
				else:
					def_dc = dc
			else:  # if_no_break
				dc = def_dc  # restore

			dc = def_dc  # use_last

		try:
			assert all((sc, tc, dc)), ""
		except AssertionError:
			logging.warning(
				"@sc/@tc/@dc/@filename is some null %s"
				% ";".join(map(str, [sc, tc, dc, sf]))
			)
		else:
			logging.info(
				"@sc/@tc/@dc/@filename %s" % ";".join(map(str, [sc, tc, dc, sf]))
			)

		# sleep(1) # 0.05
		cur_iter += 1  # -> cur_iter += os.path.getsize(sf) # debug

		try:
			cmd_str: list[str] = calc_parts(
				filename=sf.strip(),
				is_update=True,
				parts=10,
				is_run=False,
				save_last=[True],
			)  # debug(save_last - only_last_line) # parts/at_last_key_calculate_to_end_framecount # python 3.9(-hide/debug)
			assert cmd_str, ""
		except AssertionError:  # if_null(ready)
			print(
				Style.BRIGHT + Fore.GREEN + "current: %s is ready" % sf
			)  # job_ready_print
			logging.info("current: %s is ready" % sf)  # job_ready_logging
			continue  # skip_ready(-time)
		except BaseException:  # if_error(some)
			logging.error("@cmd_str error in current: %s" % sf)
			continue  # skip_error(-time)
		else:
			try:
				assert bool(some_dict[sf.strip()] == cmd_str.replace("__", "_")), ""
			except AssertionError:
				logging.warning("@sf record not found, current: %s" % sf)
				some_dict[sf.strip()] = cmd_str.replace("__", "_")
			except BaseException as e:
				sf_err = (str(e), sf)
				logging.error("@sf error in record, error: %s, current: %s" % sf_err)
			finally:
				try:
					assert bool(some_dict[sf.strip()]), ""
				except AssertionError:
					logging.warning("@some_dict record is null, current: %s" % sf)
				except BaseException as e2:
					some_dict_err = (str(e2), sf)
					logging.error(
						"@some_dict error in record, error: %s, current: %s"
						% some_dict_err
					)

			try:
				assert cmd_str, ""
			except AssertionError:
				logging.warning("@cmd_str file %s is ready")
			else:
				print(
					Style.BRIGHT + Fore.BLUE + "%s" % space_regex.sub(" ", cmd_str[-1])
				)  # last_cmd_print
				logging.info(
					"@cmd_str %s" % space_regex.sub(" ", cmd_str[-1])
				)  # last_cmd_logging

				current_dict[sf.strip()] = space_regex.sub(" ", cmd_str[-1])

				logging.info(
					"@(create/remove)_cmd_in_src_folder %s" % add.full_to_short(sf)
				)

				try:
					fn, hhmm, ss = calc_download_time(sf, fs=os.path.getsize(sf), sp=10)
				except BaseException as e:
					calc_download_time_error = (str(e), sf)
					logging.error(
						"@calc_download_time error %s, current: %s"
						% calc_download_time_error
					)
				else:
					logging.info(
						"@calc_download_time current: %s, time: %s"
						% (fn, ":".join(map(str, [hhmm, ss])))
					)

				trimmer_dict[sf.strip()] = cmd_str

		telapsed, tleft, etime, current = calcProcessTime(
			strt, cur_iter, max_iter, add.full_to_short(sf)
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
			prstime = (t.remains(cur_iter), etime, add.full_to_short(sf))

			try:
				te_set.add(prstime[0])  # t.remains(cur_iter)
			except BaseException as e:
				te_str = (str(e), sf)
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
			te_str = (str(e2), sf)
			logging.error("@te_str error: %s, filename: %s" % te_str)
		else:
			prstime = (t.remains(cur_iter), etime, add.full_to_short(sf))

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
			"@some_dict time_end: %s, current: %s" % (str(datetime.now()), last_file)
		)

	with open(current_json, "w", encoding="utf-8") as cjf:
		json.dump(
			current_dict, cjf, ensure_ascii=False, indent=4, sort_keys=False
		)  # save_current_jobs(cmd)

	with open(current_base, "w", encoding="utf-8") as cbf:
		cbf.writelines(
			"%s\n" % k for k, _ in current_dict.items()
		)  # save_only_fpaths(file)

	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump(
			trimmer_dict, tbf, ensure_ascii=False, indent=4, sort_keys=True
		)  # save_by_filter # some_dict -> trimmer_dict

	sl = sl2 = sl3 = []

	seas_regex = re.compile(r"_[\d+]{2}s[\d+]{2,4}e", re.I)
	year_regex = re.compile(r"\([\d+]{4}\)", re.I)

	type_check1: list[str] = [
		sf.strip() for sf in some_files if seas_regex.findall(sf.split("\\")[-1])
	]  # tv_series(filter) # python 3.9(-hide/debug)
	type_check2: list[str] = [
		sf.strip() for sf in some_files if year_regex.findall(sf.split("\\")[-1])
	]  # cinema(filter) # python 3.9(-hide/debug)

	sf_skip = []

	# after_add_segment_line_at_start(debug) # project_filter_job
	# """
	for sf in filter(lambda x: os.path.exists(x), tuple(some_files)): # any_exists / "filter(only_files)"
		if os.path.exists(".".join([sf, "bak"])):  # skip_backup
			try:
				os.remove(sf.replace(sf.split(".")[-1], "cmd"))  # delete_from_src
			except BaseException as e:
				logging.error("@some_files/@sf/@error %s" % ";".join(
					map(str, (sf, e)))
				)  # some_files_err
			else:
				sf_skip.append(sf.split("\\")[-1])
				logging.info("@some_files/@sf %s" % sf)

			"""
			try:
				os.remove(os.path.join(path_to_done, sf.split("\\")[-1].replace(sf.split(".")[-1], "cmd")))  # delete_from_dst
			except BaseException as e2:
				logging.error("@some_files/@+sf/@error %s" % ";".join(
					map(str, (os.path.join(path_to_done, sf.split("\\")[-1].replace(sf.split(".")[-1], "cmd")), str(e2))))
				)   # some_files_err
			else:
				logging.info("@some_files/@+sf %s" % os.path.join(path_to_done, sf.split("\\")[-1].replace(sf.split(".")[-1], "cmd")))
			"""

			continue				
		
		try:
			assert os.path.exists(
				os.path.join(
					path_to_done, sf.split("\\")[-1].replace(sf.split(".")[-1], "cmd")
				)
			), ""
		except AssertionError:
			if not os.path.isdir(sf):
				logging.warning(
					"@sf no file %s"
					% os.path.join(
						path_to_done, sf.split("\\")[-1].replace(sf.split(".")[-1], "cmd")
					)
				)  # is_file(job_cmd)
			elif os.path.isdir(sf):
				logging.warning(
					"@sf no folder %s" % sf
				)  # is_folder
			continue
		except BaseException as e:
			if not os.path.isdir(sf):
				logging.error(
					"@sf error %s, current: %s"
					% (
						str(e),
						os.path.join(
							path_to_done, sf.split("\\")[-1].replace(sf.split(".")[-1], "cmd"),
						),
					)
				)  # is_file(job_cmd+error)
			elif os.path.isdir(sf):
				logging.error("@sf error %s, current: %s" % 
					(
						str(e),
						sf,
					)
				)  # is_folder(+error)
			continue
		else:
			# path_to_done
			with open(
				os.path.join(
					path_to_done, sf.split("\\")[-1].replace(sf.split(".")[-1], "cmd")
				),
				"r+",
				encoding="utf-8",
			) as cf:
				with open(sequence_list, encoding="utf-8") as slf:
					lines = cf.read()

					try:
						sl = list(
							set([s for s in slf.readlines() if sf.split("\\")[-1] in s])
						)  # run(cmd) # ["".join([":", s]) for s in slf.readlines() if sf.split("\\")[-1] in s] # hide(cmd)

						assert sl, ""
					except AssertionError:
						logging.warning("@sl no file %s in sequence_list" % sf)
						continue
					except BaseException as e2:
						logging.error("@sl error %s, current: %s" % (str(e2), sf))
						continue
					else:
						cf.seek(0, 0)  # merge_to_start_line
						cf.write(sl[0])  # cmd_for_run_job(new_line_at_start)
						cf.write(lines)  # last_lines
	# """

	# @trimmer_base; load / create(if_error)
	try:
		with open(trimer_base, encoding="utf-8") as tbf:
			some_dict = json.load(tbf)
	except BaseException:
		some_dict = {}

		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)				

	try:
		assert some_dict, ""
	except AssertionError:
		logging.warning("@some_dict is null")
	else:
		some_dict: dict[str, list] = {
			k2:v2 for k2, v2 in some_dict.items() if not k2.split("\\")[-1] in sf_skip
		}  # skip_files_not_included # python 3.9(-hide/debug)
		
		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)					

	# @sf_skip # res = list(filter(lambda x: x[0] != x[1], zip(test_list1, test_list2)))

	try:
		with open(sequence_list, encoding="utf-8") as slf:
			sl = slf.readlines()  # sort_by_index(sf_skip)

		assert sl, ""
	except AssertionError:
		logging.warning("@sequence_list no files")
	else:
		# pass_1_of_2
		res = []
		# res = list(set([j for i in sf_skip for j in sl if not i in j])) # unique_at_end

		if all(
			(
				sf_skip,
				len(sf_skip) <= len(sl2)
			)
		):
			for i in sf_skip:
				for j in sl:
					if not i.split("\\")[-1] in j:
						try:
							assert bool(j in res), ""
						except AssertionError:
							res.append(j)  # unique_always

			try:
				assert res, ""
			except AssertionError:
				logging.warning("@sf_skip[1] is null")
			else:
				sl = res
				logging.info("@sf_skip filter: %d, files: %d" % (len(sl), len(sf_skip)))

		# pass_2_of_2 # filter(lambda x: x.split("\\")[-1] not in sl, sf_skip) # debug
		with open(sequence_list, "w", encoding="utf-8") as slf:
			slf.writelines(
				"%s" % s for s in list(filter(lambda x: not "copy" in x, tuple(sl)))
			)  # skip_copy(-skip_files) # not sf_skip in x # 'in <string>' requires string as left operand, not list

		logging.info("@sequence_list %d files" % len(sl))

	# @sf_skip # res = list(filter(lambda x: x[0] != x[1], zip(test_list1, test_list2)))		

	try:
		with open(sequence_list2, encoding="utf-8") as slf2:
			sl2 = sorted(slf2.readlines(), reverse=False)  # abc_sort(sf_skip)

		assert sl2, ""
	except AssertionError:
		logging.warning("@sequence_list2 no files")
	else:
		# pass_1_of_2
		res2 = []
		# res2 = list(set([j for i in sf_skip for j in sl2 if not i in j])) # unique_at_end

		if all(
			(
				sf_skip,
				len(sf_skip) <= len(sl2)
			)
		):
			for i in sf_skip:
				for j in sl2:
					if not i.split("\\")[-1] in j:
						try:
							assert bool(j in res), ""
						except AssertionError:
							res2.append(j)  # unique_always

			try:
				assert res, ""
			except AssertionError:
				logging.warning("@sf_skip[2] is null")
			else:
				sl2 = res2
				logging.info("@sf_skip filter: %d, files: %d" % (len(sl2), len(sf_skip)))

		# pass_2_of_2 # filter(lambda x: x.split("\\")[-1] not in sl2, sf_skip) # debug
		with open(sequence_list2, "w", encoding="utf-8") as slf2:
			slf2.writelines(
				"%s" % s2 for s2 in list(filter(lambda x: not "copy" in x, tuple(sl2)))
			)  # skip_copy(-skip_files) # not sf_skip in x # 'in <string>' requires string as left operand, not list

		logging.info("@sequence_list2 %d files" % len(sl2))

	# @sf_skip # res = list(filter(lambda x: x[0] != x[1], zip(test_list1, test_list2)))	

	try:
		with open(sequence_list3, encoding="utf-8") as slf3:
			sl3 = sorted(slf3.readlines(), reverse=False)  # abc_sort(sf_skip)

		assert sl3, ""
	except AssertionError:
		logging.warning("@sequence_list3 no files")
	else:
		# pass_1_of_2
		res3 = []
		# res3 = list(set([j for i in sf_skip for j in sl3 if not i in j])) # unique_at_end

		if all(
			(
				sf_skip,
				len(sf_skip) <= len(sl3)
			)
		):
			for i in sf_skip:
				for j in sl3:
					if not i.split("\\")[-1] in j:
						try:
							assert bool(j in res), ""
						except AssertionError:
							res3.append(j)  # unique_always

			try:
				assert res, ""
			except AssertionError:
				logging.warning("@sf_skip[3] is null")
			else:
				sl3 = res3
				logging.info("@sf_skip filter: %d, files: %d" % (len(sl3), len(sf_skip)))

		# pass_2_of_2 # filter(lambda x: x.split("\\")[-1] not in sl3, sf_skip) # debug
		with open(sequence_list3, "w", encoding="utf-8") as slf3:
			slf3.writelines(
				"%s" % s3 for s3 in list(filter(lambda x: not "copy" in x, tuple(sl3)))
			)  # skip_copy(-skip_files) # not sf_skip in x # 'in <string>' requires string as left operand, not list

		logging.info("@sequence_list3 %d files" % len(sl3))

	# debug
	# exit()

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
				"video_trimmer2.py run, time: %d ms, calc_time: %s, count: %d, time_per_file_list: %s"
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
		logging.info("@finish/@job_count %s" % ", ".join(
			map(str, (finish, job_count)))
		)

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

	'''
	# RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0 # sleep mode(windows)

	utc = asyncio.run(utc_time())
	'''

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
		# run(["cmd", "/c", "shutdown", "/s", "/f", "/t", "600", "/c", "Чтобы отменить выключение, выполните в командной строке shutdown /a"], shell=False) # shutdown(10min) (midnight - 7am) # start_after # if_updates(force)

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
