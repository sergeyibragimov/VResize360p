# -*- coding: utf-8 -*-

# Полуавтоматическое форматрирование файлов с проектами по периоду(datetime)

# from os import getcwd # cpu_count  # текущая папка # cpu_count
# from psutil import cpu_count  # viirtual_memory # pip install --user psutil
# from scprle import *
# from video_trimmer2 import *
# import gevent.monkey # pip install --user gevent # is_async(debug)
# import psutil
from datetime import datetime  # timedelta # дата и время
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

# pip install --user youtube-dl # youtube-dl --hls-prefer-native "http://host/folder/file.m3u8" # youtube-dl -o "%%(title)s.%%(resolution)s.%%(ext)s" --all-formats "https://v.redd.it/8f063bzbdx621/HLSPlaylist.m3u8"

# debug_moules
# exit()

# mklink /h optimizedays.py optimize_days.py

# abspath_or_realpath
basedir = os.path.dirname(os.path.abspath(__file__)).lower()  # folder_where_run_script
script_path = os.path.dirname(os.path.realpath(__file__)).lower()  # is_system_older
current_folder = "".join([os.path.dirname(os.path.realpath(sys.argv[0])), "\\"])

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
days_ago_base = "%s\\days_ago.lst" % script_path
days_ago_json = "%s\\days_ago.json" % script_path
month_forward_base = "%s\\month_forward.lst" % script_path
month_forward_json = "%s\\month_forward.json" % script_path
calc_year_base = "%s\\calc_year.lst" % script_path
calc_year_json = "%s\\calc_year.json" % script_path
all_period_json = "%s\\all_period.json" % script_path
all_period_base = "%s\\all_period.lst" % script_path
period_base = "%s\\period.lst" % script_path
combine_base = "%s\\fcd.txt" % script_path
period_base = "%s\\period.lst" % script_path

# '''
try:
	dsize = disk_usage(r"%s" % dletter).free  # "c:\\"
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
# logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+5s ]# %(levelname)+8s [%(asctime)s]  %(message)s',	level=logging.INFO) # no_file # debug

try:
	assert os.path.exists(path_to_done), ""
except AssertionError:
	try:
		os.mkdir(path_to_done)
	except BaseException:
		exit()  # path_to_done = "c:\\downloads\\"

# @regex
# not_include_regex = re.compile(r"^.*(?!(copy).*)$", re.I) # debug
# video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg|^.dmf|^.txt|^.srt|^.vtt|^.dmfr|^.aria2|^.crswap|^.filepart|^.crdownload))$", re.M)
space_regex = re.compile(
	r"[\s]{2,}"
)  # text = "hello  world" # space_regex.sub(" ", text)
video_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg))$",
	re.M,
)
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
		if sec < 60:
			return "{} seconds".format(sec)
		else:
			return "{} minutes".format(int(sec / 60))


# @ oop
class Additional:
	def __init__(self):
		pass

	# change_full_to_short(if_need_or_test_by_logging) # temporary_not_use
	def full_to_short(self, filename) -> str:
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

		# noinspection PyBroadException
		try:
			short_filename = "".join(
				[self.filename[0], ":\\...\\", self.filename.split("\\")[-1]]
			).strip()  # is_ok
		except:
			short_filename = self.filename.strip()  # if_error_stay_old_filename

		return short_filename

	# """
	def parse_file(self, filename):  # full_name
		self.filename = filename

		try:
			filename = file_regex.findall(self.filename)[
				0
			]  # ; print(file_regex.findall(filename), end="\t\n") # short_filename
		except BaseException:
			return (0, [], [])

		# filename = "7f_Aktrisy.S01.E01.2023.WEB-DL.1080p.v1a1.30.03.23.mp4" # is_rus
		# filename = "7f_30.Monedas.S01E06.Guerra.Santa.1080p.HBO.WEB-DL.Rus.Spa.Eng.BenderBEST.a1.09.01.21.mp4"

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

		parse_template.append(
			re.compile(
				r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([\d+]{1,2})\.sezon\.([\d+]{1,2})\.seriya"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([eE]{1}[\d+]{2})"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([sS]{1}[\d+]{2})\.([eE]{1}[\d+]{2})"
			)
		)  # is_rus
		parse_template.append(
			re.compile(
				r"^[0-9]f_(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*([sS]{1}\.[\d+]{1}).*([\d+]{2})"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_(?:([A-Z][a-z\.\d+]{1,}|[A-Za-z\.\d+]{1,})).*([sS]{1}[\d+]{1}).*([\d+]{2})"
			)
		)
		parse_template.append(re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,})-([\d+]{3}).*"))
		parse_template.append(
			re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*(S[1,2])\.ep([\d+]{1,2})")
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.Vypusk-([\d+]{2})"
			)
		)
		parse_template.append(
			re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})x([\d+]{2})")
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})\.sezon\.([\d+]{2})\.seria"
			)
		)
		parse_template.append(
			re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d]{1})x([\d+]{2})")
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})"
			)
		)  # is_eng
		parse_template.append(
			re.compile(
				r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[\.]{1,}([\d+]{1})\.s-n\.([\d+]{1,2})\.s"
			)
		)
		parse_template.append(
			re.compile(r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*[sS]{1}([\d+]{2})[x]([\d+]{2})")
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([A-Za-z\.\-\d+]{1,})\.([\d+]{2})\.seriya\.iz\.([\d+]{2})"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([\d+]{1,2})[\.]{1,}(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,})).*[\d+]{4}"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([\d+]{2})-([A-Za-z\.\-\d+]{1,}).*([\d+]{1}[sS]{1})ezon"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([\d+]{2}).*[\.]{1,}([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})"
			)
		)
		parse_template.append(
			re.compile(r"^[0-9]f_([\d+]{2})\-([A-Za-z\.\-\d+]{1,}).*([sS]{1}[\d+]{2})")
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_(\[.*\]).*\.(?:([A-Z][a-z\.\-\d+]{1,}|[A-Za-z\.\-\d+]{1,}))\.([\d+]{1,2})\.\-\.([\d+]{1,2})"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*([\d+]{1})\.sezon\.([\d+]{2})\.serija"
			)
		)
		parse_template.append(
			re.compile(
				r"^[0-9]f_([A-Za-z\.\-\d+]{1,}).*\[([sS]{1}[\d+]{2})([eE]{1}[\d+]{2})"
			)
		)

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

	# """

	def __del__(self):
		print("%s удалён" % str(self.__class__.__name__))
		# logging.info("%s удалён" % str(self.__class__.__name__))


add = Additional()


# t = Timer(12987) # max_count_tasks # There are 12987 units in this task

# do some work

# sleep(1) # time.sleep(1)

# after some time passed, or after some units were processed
# eg.  37 units, calculate, and print the remaining time:
# print(t.remains(37)) # current_how_match # let the process continue and once in a while print the remining time.


"""
from time import sleep # time
import random

def recurring(interval, callable):
	i = 0
	start = time.time()
	while i < interval:  # True
		i += 1
		callable()
		remaining_delay = max(start + (i * interval) - time.time(), 0)
		print(remaining_delay); sleep(remaining_delay)

def tick_delay():
	sv = random.randrange(1, 4)
	print('tick start %d' % sv)
	sleep(sv)
	print('tick end')

recurring(5, tick_delay)
"""


def check_dict(dct: dict, item=["", None]):  # dict(json) / find_key / find_value
	# >>> a = {"a":1, "b":2, "c":3}
	# >>> a.get(5,4) # 4 # no_key
	# >>> a.get("a",4) # 1 # yes_key
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


def clear_base_and_lists():
	# @clear_log_and_bases

	# pass

	# '''
	create_files = []

	# automatic(is_no_semiautomatic)
	create_files.extend(
		[
			period_base,
			log_file,
			days_ago_base,
			days_ago_json,
			month_forward_base,
			month_forward_json,
			calc_year_base,
			calc_year_json,
			all_period_json,
			all_period_base,
		]
	)  # clear_all_data

	try:
		for cf in filter(lambda x: os.path.getsize(x), tuple(create_files)):
			open(cf, "w", encoding="utf-8").close()
	except BaseException as err:
		logging.error("%s" % str(err))

	try:
		for cf in filter(lambda x: os.path.exists(x), tuple(create_files)):
			os.remove(cf)
	except BaseException as err:
		logging.error("%s" % str(err))
	# '''


# logging.basicConfig(level=logging.INFO)

# @logging
# with_encoding # utf-8 -> cp1251
# filename / lineno / name / levelname / message / asctime # save_logging_manuals


open(log_file, "w", encoding="utf-8").close()


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
			assert bool(int(ds) > 0), ""
		except AssertionError:
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
	# write_log("debug dtw[ok]", "Today is: %s, weekday is: %s, season(days): %s, number_of_day: %s, days_to_ny: %s" % d_w_s_n_d_str)

clear_base_and_lists()

logging.info("%s" % ";".join([basedir, script_path]))

try:
	files_types = [
		0 if os.path.isfile(os.path.join(os.getcwd(), f)) else 1
		for f in os.listdir(os.getcwd())
	]
	assert files_types, ""
except AssertionError:
	logging.warning("@files_types no files or no folders")
else:
	if files_types.count(1) == 0:
		os.chdir("..")

	logging.info("@files_types found %d data" % len(files_types))

# 15632076800 # 3687570583552
# """
dspace_list = []
dspace_another_drive = 0.0

for dl in range(ord("c"), ord("z") + 1):
	du = "".join([str(chr(dl)), ":\\"])

	try:
		assert int(disk_usage(r"%s" % du).used) != 0, ""
	except AssertionError:
		continue  # break
	except BaseException:
		continue
	else:
		logging.info(
			"@du %d" % int(disk_usage(r"%s" % du).used)
		)  # print(int(disk_usage(r"%s" % du).used))

		dspace_list.append(int(disk_usage(r"%s" % du).used))

try:
	dspace_another_drive = (
		((sum(dspace_list) * 0.30) / (1024**3), "Gb")
		if (sum(dspace_list) * 0.30) / (1024**3) < 1000
		else ((sum(dspace_list) * 0.30) / (1024**4), "Tb")
	)
except BaseException as e:
	dspace_another_drive = (0, "Unknown")
	logging.error(
		"@dspace_another_drive не получилось получить размер резервного пространства [%s]"
		% str(e)
	)
finally:
	logging.info(
		"@dspace_another_drive на данный момент нужно %s" % str(dspace_another_drive)
	)  # print(dspace_another_drive)
# """

job_count = 0

test_folders = test_files = []


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

	try:
		assert isinstance(h, int) and isinstance(m, int) and isinstance(s, int), ""
	except AssertionError:
		h, m, s = int(h), int(m), int(s)

	# ms_time = None

	try:
		ms_time = (lambda hh, mm, ss: (hh * 3600) + (mm * 60) + ss)(h, m, s)
		# ms_time = '{:02d}:{:02d}:{:02d}'.format(h, m, s)  # hh:mm:ss # '{:02d} час. {:02d} мин. {:02d} сек.'.format(h, m, s) # hh mm ss
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

	# need_read_subfolder_from_current_folder
	try:
		*fileparam, _ = os.walk(os.getcwd())  # folder/[subfolder]/[files]
	except BaseException:
		fileparam = ("", [], [])
	# else:
	# need_sort_by_regex

	# hide_avg
	# """
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

	# """

	# type(fileparam) # list(full_path=%s,?=list,short_file=list)
	# ('D:\\Multimedia\\Video\\Serials_Europe\\Zolotaya_kletka_Rus', [], ['01s01e.txt'])

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
							some_files.add(f)
							if video_regex.findall(f.split("\\")[-1]):
								files.append(f)
								logging.info("@files %s" % f)

								"""
								try:
									seas_or_year = crop_filename_regex.findall(f.split("\\")[-1])[0][0].strip() # regex(short) # type1
									# seas_or_year2 = "".join(crop_filename_regex.findall(fname.split(".")[0])[0]) # .replace("_", "").replace("(", "").replace(")", "") # is_crop_syms # str(short) # type2
								except BaseException:
									seas_or_year = ""
								else: # is_hide_count
									if seas_or_year:
										seasyear_count[seas_or_year.strip()] = seasyear_count.get(seas_or_year.strip(), 0) + 1 # seas_or_year_count
								"""

	# """
	try:
		ag = avg_calc(sm, ln)  # avg_calc(100, 2) # 50
	except BaseException:
		ag = 0  # 0
	# """

	"""
	select_first = list(seasonyear_count.keys()) if len(seasyear_count) > 0 else []
	select_first.sort(reverse=False)
	try:
		assert select_first, ""
	except AssertionError:
		first_str = ""
	else:
		first_str = select_first[0]

	try:
		assert first_str, ""
	except AssertionError:
		first_regex = None
	else:
		first_regex = re.compile(r"%s" % first_str, re.M)
	"""

	logging.info("@files/@folders/@ag %d %d %d" % (len(files), len(folders), ag))

	open(period_base, "w", encoding="utf-8").close()
	open(all_period_base, "w", encoding="utf-8").close()

	fsf_set = set()
	nt = 0
	days = months = years = []

	def calcProcessTime(starttime, cur_iter, max_iter, filename):
		telapsed = time() - starttime
		testimated = (telapsed / cur_iter) * (max_iter)

		finishtime = starttime + testimated
		finishtime = datetime.fromtimestamp(finishtime).strftime("%H:%M:%S")  # in time

		lefttime = testimated - telapsed  # in seconds

		return (int(telapsed), int(lefttime), finishtime, filename)

	strt, cur_iter, max_iter = time(), 0, len(some_folders)
	te_set = mx_set = set()
	mx1 = mx2 = mx3 = 0
	last_folder = ""

	t = Timer(max_iter)

	days = months = years = []

	# """
	for fsf in filter(
		lambda x: os.path.isdir(x), tuple(some_subfolders)
	):  # read_folders # some_folders -> folders
		period_list_filter = []

		is_day = is_month = is_year = False

		# add_new_folder
		try:
			assert fsf, ""
		except AssertionError:
			continue

		last_folder = fsf

		try:
			assert bool(fsf in fsf_set), ""
		except AssertionError:
			logging.warning(
				"Папка %s не найдена в общем списке для обработки" % fsf.split("\\")[-1]
			)
			fsf_set.add(fsf)
		finally:
			logging.info("Папка %s упешно добавлена" % fsf.split("\\")[-1])
			# continue

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
			continue
		"""
		else:
			if all((first_regex != None, first_str != "")):
				list_files_old = list_files # backup_files
				list_filter = [lf.strip() for lf in list_files if first_regex.findall(lf.split("\\")[-1])]
				list_files = list_filter if list_filter else list_files_old # filter / debug
		"""

		"""
		try:
			assert list_files, ""
		except AssertionError: # if_not_filtred
			break
		# else:
			# if_filtred
		"""

		# @period
		today = datetime.now()
		fdate = os.path.getmtime(fsf)
		ndate = datetime.fromtimestamp(fdate)

		# @count
		len_files = len(
			list(
				filter(
					lambda x: video_regex.findall(x.split("\\")[-1]), tuple(list_files)
				)
			)
		)  # all_types

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
		if len(list_files) > 1:
			create_time_list = sorted(
				[os.path.getmtime(f) for f in list_files], reverse=False
			)  # list
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
						# write_log("debug project_file[utime][description]", "%s" % ";".join([unixtime_to_date(ctl), unixtime_to_date(otl), pf]))
						os.utime(
							pf, times=(otl, ctl)
						)  # sort_and_update_some_date # old -> new
					else:
						continue

		# group_folders_by_date # change_datetime_at_folder_by_last_(access/modify/create)_date
		"""
		maxdate_m = "" # maxdate_c = maxdate_m = maxdate_a = ""

		try:
			files = [os.path.join(fsf, f) for f in os.listdir(fsf) if os.path.exists(os.path.join(fsf, f))]
			files = [f.strip() for f in files if os.path.isfile(f)]
			assert files, ""
		except AssertionError:
			continue
		else:
			try:
				maxdate_folder = os.path.getctime(fsf) # create(min) # debug # pass_1_of_2
				# maxdate_folder = os.path.getatime(fsf) # access(max) # debug # pass_1_of_2
			except:
				maxdate_folder = None
	
			# maxdate_c = max(files, key=os.path.getctime) # 'C:\\Python27\\LICENSE.txt' # created
			# maxdate_a = max(files, key=os.path.getatime) # 'C:\\Python27\\LICENSE.txt' # access
			maxdate_m = max(files, key=os.path.getmtime) # 'C:\\Python27\\LICENSE.txt' # modified
	
			try:
				maxdate_file = os.path.getmtime(maxdate_m) # modify # debug # pass_2_of_2
			except:
				maxdate_file = None
	
			if all((maxdate_folder != None, maxdate_file != None, maxdate_folder != maxdate_file)):
				os.utime(fsf, times=(maxdate_folder, maxdate_file)) # is_recovery_datetime # old -> new
		"""

		try:
			days_ago = abs(today - ndate).days
			assert bool(days_ago >= 0), ""
		except AssertionError:  # if_none(today)
			days_ago = 0

		max_days_by_year = 366 if today.year % 4 == 0 else 365

		1 if days_ago % 7 <= 4 else 0

		# @filter_period # any_day / limit_by_month / limit_by_year
		# period_list_filter = [days_ago // 7 in range(5),  days_ago // 30 in range(13), days_ago // max_days_by_year in range(max_days_by_year + 1)] # week / month / year
		period_list_filter = [
			True if days_ago % 7 <= 4 else False,
			True if days_ago % 30 <= 12 else False,
			True if days_ago % max_days_by_year <= max_days_by_year + 1 else False,
		]  # period(by_generator)
		# period_list_filter = [days_ago % 7 <= 4, days_ago % 30 <= 12, days_ago % max_days_by_year <= max_days_by_year + 1] # to_week / to_month / to_year

		try:
			plf = (
				str(days_ago),
				str(days_ago % 7),
				str(days_ago % 30),
				str(days_ago % max_days_by_year),
				fsf.split("\\")[-1],
			)  # any_day / week / month / year / folder
			assert plf, ""
		except AssertionError:
			plf = (fsf.split("\\")[-1],)
		finally:
			try:
				mx1 = days_ago % 7 if mx1 < days_ago % 7 else mx1
				mx2 = days_ago % 30 if mx2 < days_ago % 30 else mx2
				mx3 = (
					days_ago % max_days_by_year
					if mx3 < days_ago % max_days_by_year
					else mx3
				)
				assert bool((mx1, mx2, mx3) in mx_set), ""
			except AssertionError:
				if any((mx1, mx2, mx3)):
					mx_set.add((mx1, mx2, mx3))
					# period_list_filter = [mx1 >= 0, mx2 >= 0, mx3 >= 0] # any_day_by_max # some_zero
			else:
				logging.info("max period: %s" % str((mx1, mx2, mx3)))

		try:
			assert bool(days_ago >= 0), ""
		except AssertionError:
			logging.warning("@days_ago error period, folder: %s" % fsf.split("\\")[-1])
			continue
		except BaseException as e:
			days_ago_err = (str(e), fsf.split("\\")[-1])
			logging.error("@days_ago error: %s, folder: %s" % days_ago_err)
			continue
		else:
			logging.info("@plf %s" % str(plf))

		if all((len_files, period_list_filter.count(True) > 0)):  # some_projects
			job_count += 1

			if period_list_filter[0]:
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

			elif period_list_filter[1]:
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

			elif period_list_filter[-1]:
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

			week_status_str = (all_period[0], week_status, all_period[2])
			logging.info(
				"@datetime [period] folder: %s, days_ago: %s, count_files: %d"
				% week_status_str
			)  # folder / days_ago / count_files

			with open(period_base, "a", encoding="utf-8") as pbf:
				pbf.writelines(
					"%s\n" % all_period[0]
				)  # multicommander # fsf.split("\\")[-1]
				# pbf.writelines("%s\\\n" % all_period[0]) # totalcommander # fsf.split("\\")[-1]

		else:  # if_no_projects
			week_status = "%d дней назад!" % days_ago  # is_another_period
			week_status_str = (all_period[0], week_status, all_period[2])

			logging.info(
				"@datetime [another_period] folder: %s, days_ago: %s, count_files: %d"
				% week_status_str
			)  # folder / days_ago / count_files

			with open(all_period_base, "a", encoding="utf-8") as apbf:
				apbf.writelines(
					"%s\n" % all_period[0]
				)  # multicommander # fsf.split("\\")[-1]
				# apbf.writelines("%s\\\n" % all_period[0]) # totalcommander # fsf.split("\\")[-1]

		# else:
		# continue # skip_another_period

		try:
			sleep(60 - time() + strt)
		except BaseException:
			sleep(0.05)

		# prstime = calcProcessTime(strt, cur_iter, max_iter, fsf.split("\\")[-1]) # some_value_as_set
		# print("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % prstime)
		# logging.info("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % prstime)

		try:
			assert bool(t.remains(cur_iter) in te_set), ""
		except AssertionError:
			prstime = (t.remains(cur_iter), fsf.split("\\")[-1])

			try:
				te_set.add(prstime[0])  # t.remains(cur_iter)
			except BaseException as e:
				te_str = (str(e), fsf.split("\\")[-1])
				logging.error("@te_str add error: %s, current: %s" % te_str)
			else:
				print(
					"@prstime left: %s(s), current: %s" % prstime
				)  # t.remains(cur_iter)
				logging.info("@prstime left: %s(s), current: %s" % prstime)
		except BaseException as e2:
			te_str = (str(e2), fsf.split("\\")[-1])
			logging.error("@te_str error: %s, filename: %s" % te_str)
		else:
			prstime = (t.remains(cur_iter), fsf.split("\\")[-1])

			print("@prstime left: %s(s), current: %s" % prstime)  # t.remains(cur_iter)
			logging.info("@prstime left: %s(s), current: %s" % prstime)
	else:
		logging.info(
			"@fsf time_end: %s, current: %s" % (str(datetime.now()), last_folder)
		)

	# """

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

	"""
	if any((ag, cntfiles)):
		cntfiles = ag if ag > cntfiles else cntfiles
		logging.info("@cntfiles/sum/len/avg %s" % ";".join([str(cntfiles), str(sm), str(ln), str(ag)]))
	"""

	# all_period_dict[%period%] = [fsf.split("\\")[-1], fsf, len_files]
	# all_period_dict = {k:v for k, v in all_period_dict.items() if all((v[2], v[2] - cntfiles < 0))} # ?(is_none_classify)

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

	try:
		assert periods, ""
	except AssertionError:
		logging.warning("no periods")
	else:
		with open(combine_base, "w", encoding="utf-8") as cbf:
			# cbf.writelines("%s\n" % p for p in periods)
			cbf.writelines("%s\\\n" % p for p in periods)  # totalcommander

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

	sizes_dict = {}

	sizes_dict[1] = "Kb"
	sizes_dict[2] = "Mb"
	sizes_dict[3] = "Gb"

	try:
		dsize = disk_usage(r"%s" % dletter).free  # "c:\\"
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

	logging.info(f"@finish {str(datetime.now())}")

	# '''
	dt = datetime.now()

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
	# '''

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

	try:
		filename = "\\".join([script_path, __file__.replace(ext, ".glob")])
	except BaseException:
		filename = ""
	else:
		if filename:
			try:
				with open(filename, "w", encoding="utf-8") as fj:
					json.dump(
						glob_dict, fj, ensure_ascii=False, indent=4, sort_keys=False
					)
			except BaseException:
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
	except BaseException:
		pass
