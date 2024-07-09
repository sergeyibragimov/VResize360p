# -*- coding: utf-8 -*-

# Полуавтоматическое форматрирование файлов для разделения(trim) и сбора(concat)
# Файл с разрезами и одной частью если небольшой("оптимально"" для любого компьютера)

# from math import sqrt
# from os import getcwd # cpu_count  # текущая папка # cpu_count
# import gevent.monkey # pip install --user gevent # is_async(debug)
# import psutil
from datetime import datetime, timedelta  # дата и время
from psutil import cpu_count  # viirtual_memory # pip install --user psutil
from shutil import (
	disk_usage,
	move,
)  # copy # файлы # usage(total=16388190208, used=16144154624, free=244035584)
from subprocess import (
	run,
)  # TimeoutExpired, check_output, Popen, call, PIPE, STDOUT # Работа с процессами # console shell=["True", "False"]
from threading import Semaphore  # Thread, Barrier # работа с потоками # mutli_async
from time import time, sleep
import asyncio  # TaskGroup(3.11+)
import json  # JSON (словарь)
import logging  # журналирование и отладка
import os  # система
import re  # реуглярные выражения/regular expression # .*(\?|$)
import sys

# pip install --user youtube-dl # youtube-dl --hls-prefer-native "http://host/folder/file.m3u8" # youtube-dl -o "%%(title)s.%%(resolution)s.%%(ext)s" --all-formats "https://v.redd.it/8f063bzbdx621/HLSPlaylist.m3u8"

# Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.
# Back, Cursor # Fore.color, Back.color # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE # pip install --user colorama
# from colorama import ( Fore, Style, init )

# debug_moules
# exit()

# mklink /h videotrimmer.py video_trimmer2.py

# abspath_or_realpath
basedir = os.path.dirname(os.path.abspath(__file__)).lower()  # folder_where_run_script
script_path = os.path.dirname(os.path.realpath(__file__)).lower()  # is_system_older
current_folder = "".join([os.path.dirname(os.path.realpath(sys.argv[0])), "\\"])

dletter = "".join(
	[basedir.split("\\")[0], "\\"]
)  # "".join(script_path[0:5]) if script_path else "".join(os.getcwd()[0:5])

# logging(start)
log_base = "%s\\trimmer_job.json" % script_path  # main_debug(json)
log_print = "%s\\trim.log" % script_path  # main_debug(logging)

# --- path's ---
path_for_queue = r"d:\\downloads\\mytemp\\"
path_to_done = "%sdownloads\\list\\" % dletter  # "c:\\downloads\\" # ready_folder
path_for_folder1 = "".join([os.getcwd(), "\\"])

# copy_dst = "c:\\downloads\\combine\\original\\"
cmd_list = "%s\\video_trimmer2.cmd" % script_path  # command_line_for_trim
sequence_list = "%s\\sequence_list.cmd" % script_path

# list(json)
days_ago_base = "%s\\days_ago.lst" % script_path
days_ago_list = "%s\\days_ago.txt" % script_path  # txt_by_list(one_day_ago_base)
month_forward_base = "%s\\month_forward.lst" % script_path
calc_year_base = "%s\\calc_year.lst" % script_path
all_period_json = "%s\\all_period.json" % script_path
filename_length_json = "%s\\filename_length.json" % script_path
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
	)  # no_file # pass
finally:
	if dsize // (1024**2) > 0:  # any_Mb # debug
		logging.basicConfig(
			handlers=[logging.FileHandler(log_print, "w", "cp1251")],
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
crop_filename_regex = re.compile(r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)", re.I)
file_regex = re.compile(r"([0-9]f_.*)", re.M)
space_regex = re.compile(r"[\s]{2,}")
cmd_whitespace = re.compile(
	r"[\s]{2,}"
)  # text = "hello  world" # space_regex.sub(" ", text)
video_regex = re.compile(
	r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg))$",
	re.M,
)
year_regex = re.compile(r"\([\d+]{4}\)", re.M)
seasyear = re.compile(
	r"(?:(_[\d+]{2,4}s|\([\d+]{4}\)))", re.M
)  # MatchCase # season_and_year(findall) # +additional(_[\d+]{2}p)

start = time()

job_count = 0
some_dict = {}

mytime: dict = {
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
		except:  # if_error
			return item[1]  # use_value(None -> no_value)


def clear_base_and_lists():
	# @clear_log_and_bases

	pass

	"""
	create_files = []

	# create_files.extend([period_base, cmd_list, log_base, log_print, days_ago_base, days_ago_list, month_forward_base, calc_year_base, all_period_json, filename_length_json])
	create_files.extend([period_base, cmd_list, log_print, filename_length_json]) # log_base # skip_periods

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

# --- CPU optimize / debug ---
try:
	assert cpu_count(), ""
except AssertionError:
	unique_semaphore = Semaphore(2)
	# bar = Barrier(2, timeout=15)
else:
	unique_semaphore = Semaphore(cpu_count())
	# bar = Barrier(cpu_count(), timeout=15)

open(log_print, "w", encoding="utf-8").close()
open(sequence_list, "w", encoding="utf-8").close()

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

# clear_base_and_lists()

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

test_folders = test_files = []

# 15632076800 # 3687570583552
# """
dspace_list = []
dspace_another_drive = 0.0

for dl in range(ord("c"), ord("z") + 1):
	try:
		du = "".join([str(chr(dl)), ":\\"])
	except:
		continue

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

trimer_base = log_base
not_ready_base = "%s\\new_job.json" % script_path
ready_base = "%s\\ready_job.json" % script_path

# @pass_1_of_2

# @trimmer_base; load / create(if_error)
try:
	with open(trimer_base, encoding="utf-8") as tbf:
		some_dict = json.load(tbf)
except BaseException:
	some_dict = {}

	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=False)

if some_dict:
	for k, _ in some_dict.items():
		if os.path.exists(
			"".join([path_to_done, k.split("\\")[-1].replace(k.split(".")[-1], "cmd")])
		) and os.path.exists(k.replace(k.split(".")[-1], "cmd")):
			os.remove(
				k.replace(k.split(".")[-1], "cmd")
			)  # if_found_cmd_file_in_dst_clear_in_src
		elif not os.path.exists(
			"".join([path_to_done, k.split("\\")[-1].replace(k.split(".")[-1], "cmd")])
		) and os.path.exists(k.replace(k.split(".")[-1], "cmd")):
			move(
				k.replace(k.split(".")[-1], "cmd"),
				"".join(
					[path_to_done, k.split("\\")[-1].replace(k.split(".")[-1], "cmd")]
				),
			)  # if_not_found_cmd_file_in_dst

	"""
	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump({}, tbf, ensure_ascii=False, indent=4, sort_keys=False) # clear_after_load
	"""

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

		try:
			short_filename = "".join(
				[self.filename[0], ":\\...\\", self.filename.split("\\")[-1]]
			).strip()  # is_ok
		except:
			short_filename = self.filename.strip()  # if_error_stay_old_filename

		return short_filename

	"""
	def parse_file(self, filename):  # full_name
	
		
		
		try:
			filename = file_regex.findall(filename)[0] #; print(file_regex.findall(filename), end="\t\n") # short_filename
		except:
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
			parse_list = list(set([(tuple(pt.findall(short_filename)), pt) for pt in parse_template if pt.findall(short_filename)])) # try_unique
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
		print("%s удалён" % str(self.__class__.__name__))
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
			return

		# ffprobe -v error -show_entries stream=width,height -of csv=p=0:s=x input.m4v
		cmd_wh = [
			"".join([path_for_queue, "ffprobe.exe"]),
			"-v",
			"error",
			"-show_entries",
			"stream=width,height",
			"-of",
			"csv=p=0:s=x",
			self.filename,
		]  # output_format
		wi = "".join([current_folder, "wh.nfo"])  # path_for_queue

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
					# job_status = "%s" % str((width, height, add.full_to_short(self.filename), "ok")) if width <= maxwidth else "%s" % str((width, height, add.full_to_short(self.filename), "job"))
					job_status = (
						"%s" % str((width, height, self.filename, "ok"))
						if width <= maxwidth
						else "%s" % str((width, height, self.filename, "job"))
					)
				except BaseException:
					job_status = ""
				finally:
					if job_status:
						print(job_status)
						logging.info(
							job_status
						)  # write_log("debug [w/h/$file$]", "%s" % job_status)

				try:
					assert all((width > 0, maxwidth > 0, height > 0)), ""
				except AssertionError:
					logging.warning(
						"@width/@maxwidth/@height another value, current: %s"
						% self.filename
					)
				else:
					if all((width > maxwidth, height, width >= height)):
						print("debug [w/h/$file$]: %s" % job_status)
						job_count += 1

						logging.info(
							"@width/@maxwidth/@height/@file %s"
							% ";".join(
								[str(width), str(maxwidth), str(height), self.filename]
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
			print("@width/@height/@error current: %s" % self.filename)
			logging.error("@width/@height/@error current: %s" % self.filename)

		is_owidth, changed, ar_find = (
			width,
			False,
			(width >= height),
		)  # old_width? / optimized? / width => height -> some_aratio

		def ar_calc(
			h, w, nw=640
		) -> tuple:  # 720x406 => (406 / 720) * 640 = 360,8888888888889
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
					"@ar_calc value is normal [%s]" % "x".join([str(nw), str(ac)])
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
					if all((ac, h, ac != h)):
						is_clc = True

				try:
					assert isinstance(ac, int), ""  # height(int)
				except AssertionError:  # if_not_int
					is_clc = True
					ac = int(ac)
					logging.warning(
						"@ar_calc converted height float to int %s" % str(ac)
					)

				try:
					assert bool(is_clc == True), ""
				except AssertionError:
					logging.warning("@is_clc not changed width and height")
				else:
					logging.info("@is_clc changed width and height")

			return (nw, ac)

		if all(
			(is_calc == True, width > maxwidth, height, width >= height, ar_find)
		):  # True;True;h;w >= h("any" -> 1:1);calc_ar

			# additional(calc)
			try:
				tst_width, tst_height = ar_calc(height, width, maxwidth)
			except BaseException:
				tst_width = tst_height = 0
			else:
				width, height = tst_width, tst_height

			try:
				ar_calc_status = "x".join([str(width), str(height)])
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
				logging.info("@ar_calc/file %s" % ";".join([ar_calc_status, filename]))

			changed = bool(
				is_owidth > maxwidth
			)  # ; print(width, height, changed) # diff_width

			wh_status = (
				"x".join([str(width), str(height)]) + " resized"
				if changed
				else "x".join([str(width), str(height)]) + " no resized"
			)

			if all((width, height, wh_status)):
				logging.info(
					"@width/@height %s, filename: %s" % (wh_status, self.filename)
				)

				# print(wh_status)

		# return (int(width), int(height), is_owidth != width)
		return (int(width), int(height), changed)  # width <= maxwidth

	def get_profile_and_level(self, filename) -> tuple:

		self.filename = filename

		cmd_pl = [
			"".join([path_for_queue, "ffprobe.exe"]),
			"-v",
			"error",
			"-show_entries",
			"stream=profile,level",
			"-of",
			"default=noprint_wrappers=1",
			self.filename,
		]  # output_format
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

		# logging.info("filename: %s, profile/level: %s" % (add.full_to_short(filename), "x".join([str(pl_list[0]), str(pl_list[-1])])))
		logging.info(
			"filename: %s, profile/level: %s"
			% (filename, "x".join([str(pl_list[0]), str(pl_list[-1])]))
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
				# write_log("debug profilelevel", ";".join([pl_list[0].split("=")[-1].lower().strip(), pl_list[1].split("=")[-1].lower().strip(), filename]))

				return (
					pl_list[0].split("=")[-1].lower().strip(),
					pl_list[1].split("=")[-1].lower().strip(),
				)  # [main,30]

	def get_length(self, filename) -> int:
		cmd_fd = [
			"".join([path_for_queue, "ffprobe.exe"]),
			"-v",
			"error",
			"-show_entries",
			"format=duration",
			"-of",
			"compact=p=0:nk=1",
			self.filename,
		]  # output_format
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

		print("Duration time is %d" % int(duration_null))

		return duration_null

	def length_to_framecount(self, filename, fcnt, hh, mm, ss, is_manual: bool = False):

		h = m = s = 0

		fc: int = 0  # ; ln: int = 0

		try:
			h, m, s = fcnt // 3600, fcnt % 3600 // 60, fcnt % 3600 % 60
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

		try:
			assert (
				isinstance(h1, int) and isinstance(m1, int) and isinstance(s1, int)
			), ""
		except AssertionError:
			h1, m1, s1 = int(h1), int(m1), int(s1)

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
		cmd = [
			"".join([path_for_queue, "ffprobe.exe"]),
			"-v",
			"error",
			"-show_entries",
			"stream=codec_name",
			"-of",
			"csv=p=0:s=x",
			self.filename,
		]  # output_format
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
		print("%s удалён" % str(self.__class__.__name__))


# del add # clear_mem # debug


# @slide_from_job
# '''
def screenshot_cut(slide, framecount):

	try:
		assert all((slide, framecount)), ""
	except AssertionError:
		return 0

	if framecount < 2:
		framecount == 2

	return slide // framecount


def save_slide(slide, framecount, filename, width, height):
	try:
		# sc = screenshot_cut(slide=5, framecount=int(fdict["duration"].split(".")[0]) - 2)
		sc = screenshot_cut(slide, framecount - 2)
		assert sc, ""
	except AssertionError:
		logging.warning("@sc can't run screenshot_cut is some null")
		return
	except BaseException as e:
		logging.error("@sc can't run screenshot_cut error: %s" % str(e))
		return

	try:
		assert os.path.exists(filename), ""
	except AssertionError:
		fname = filename
	else:
		fname = filename.split("\\")[-1]

	# short_filename = None

	if sc > 0:
		# short_filename = crop_filename_regex.sub("", filename.split("\\")[-1])

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
				% ";".join([str(width), str(height), str(sc), split_stream])
			)
		else:
			screenshot_video = [
				init_ffmpeg,
				init_file,
				"-vf",
				"scale=%s:%s" % (str(width), str(height)),
				"-r",
				str(sc),
				"-f",
				"image2",
				"".join(['"', split_stream, '"']),
			]

		try:
			assert screenshot_video, ""
		except AssertionError:
			logging.warning("@screenshot_video command is null or read err")
		else:
			if screenshot_video:
				try:
					p = run(screenshot_video, shell=True)
					assert bool(p == 0), ""
				except AssertionError:
					logging.warning("@screenshot_video error run")
				except BaseException as e:
					screenshot_video_err = (fname, str(e))
					logging.error(
						"@screenshot_video error: can't save image for %s, error: %s"
						% screenshot_video_err
					)
					# print(Style.BRIGHT + Fore.RED + "[debug screenshot error] can't save image for %s. %s" % screenshot_video_err)
					# write_log("debug screenshot error", "can't save image for %s. %s" % screenshot_video_err)
				else:
					logging.info(
						"@screenshot_video command: %s" % " ".join(screenshot_video)
					)


# '''


def one_to_double(cnt) -> str:  # double ~ triple

	if cnt in range(0, 10):  # 9
		return "".join(["00", str(cnt)])
	elif cnt in range(10, 100):  # 99
		return "".join(["0", str(cnt)])
	elif cnt in range(100, 1000):  # 999
		return str(cnt)


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
) -> list:

	try:
		assert os.path.exists(filename), ""
	except AssertionError:
		logging.warning("@filename %s not exists" % filename)
		return []
	except BaseException as e:
		calc_parts_err = (filename, str(e))
		logging.error("@filename %s, error: %s" % calc_parts_err)
		return []

		mp4, old = "mp4", filename.split(".")[-1]  # for_job(any)

		try:
			assert bool(mp4 == old), ""
		except AssertionError:
			old = filename.split(".")[-1]
			ext = "".join([".", "mp4"])  # another_ext
		else:
			old = ext = "".join([".", "mp4"])  # default_ext

	try:
		assert bool(video_regex.findall(filename.split("\\")[-1])), ""  # is_not_video
	except AssertionError:
		return []

	some_dict = {}

	# @trimer_base load / create(if_error)
	try:
		with open(trimer_base, encoding="utf-8") as tbf:
			some_dict = json.load(tbf)
	except:
		some_dict = {}

		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump({}, tbf, ensure_ascii=False, indent=4, sort_keys=True)

	try:
		with open(filename_length_json, encoding="utf-8") as flj:
			fl = json.load(flj)
	except:
		fl = {}

	wh = width_height(filename)

	try:
		fl = {k: v for k, v in fl.items() if os.path.exists(k)}
		assert fl, ""
	except AssertionError:  # if_no_exists_files
		logging.warning("@fl no exist files")
	except BaseException as e:
		fl_err = (str(e), filename)
		logging.error("@fl error: %s, current: %s" % fl_err)

	fc = 0

	try:
		framecount = wh.get_length(filename)  # ms_to_time(framecount) # 2553 # debug
	except BaseException:
		return []
	else:
		try:
			fc = wh.length_to_framecount(filename, framecount, 0, 0, 0, is_manual=False)
		except:
			fc = 0
		finally:
			logging.info("@fc %d" % fc)

	time_by_cpu = int(cpu_count())  # cpu # min_by_cpu(int) # 2
	logging.info("@time_by_cpu %d" % time_by_cpu)

	# time_by_cpu *= 2.5 # optimal_by_parts(float) # need_generator # 2 * 2.5 ~ 5min
	# logging.info("@time_by_cpu %d" % time_by_cpu)

	def_fc = framecount  # ; def_p = parts

	try:
		assert isinstance(time_by_cpu, int), ""
	except AssertionError:
		time_by_cpu = int(time_by_cpu)

	parts = tp = 0
	tp_diff: float = 0  # tp_float: float = 0

	def some_parts(
		filename, tbc: int = 2, fc: int = 0, def_parts: int = 10
	):  # fc ~ 2899 # debug
		parts = 0

		sm = ln = ag = 0

		try:
			for i in range(1, def_parts + 1):
				sm += fc // (60 * i)  # fc % i
				ln += 1
		except:
			sm = ln = 0

		c_parts = (lambda framecount, tcpu: framecount // (60 * tcpu))(fc, tbc)

		try:
			assert all((sm, ln)), ""
		except AssertionError:  # if_null
			logging.warning("@ag/@parts sum or len some null, current: %s" % filename)
			ag, parts = 0, c_parts  # fc // (60 * tbc)
		except BaseException as e:  # DevideByZero # if_error
			ag_parts_err = (str(e), filename)
			logging.error("@ag/@parts error: %s, current: %s" % ag_parts_err)
			ag, parts = 0, c_parts  # fc // (60 * tbc)
		else:  # calc_parts_by_avg
			ag = (lambda s, l: s // l)(
				sm, ln
			)  # ag = (lambda s,l: s//l); parts = ag(sm, ln)
			parts = ag
			

		parts_str = (fc, parts, (fc / parts), filename)

		# print("fc: %d, parts: %d, tp: %f, current: %s" % parts_str)
		logging.info("fc: %d, parts: %d, tp: %f, current: %s" % parts_str)

		return parts

	try:
		parts = some_parts(filename, tbc=time_by_cpu, fc=framecount)  # debug(combine)
		assert parts, ""
	except AssertionError:
		parts = framecount // (60 * time_by_cpu)  # parts_count(default)
	except BaseException:  # if_error
		parts = 0
		return []

	# %03d.mkv # filename = "c:\\downloads\\mytemp\\test.tst"; path_to_done = "c:\\downloads\\list\\"
	try:
		# 'c:\\downloads\\list\\test_%03d.tst'
		split_stream = os.path.join(
			path_to_done,
			"".join(
				[
					filename.split("\\")[-1].split(".")[0],
					"".join(["_", "%03d"]),
					"".join([".", filename.split(".")[-1]]),
				]
			),
		)
		assert split_stream, ""
	except AssertionError:  # if_null
		logging.warning("@split_stream current: %s" % filename)
	except BaseException as e:  # if_error
		split_stream_err = (filename, str(e))
		logging.error("@split_stream current: %s, error: %s" % split_stream_err)
	else:  # if_ok
		split_stream_str = (filename, split_stream)
		logging.info("@split_stream current: %s, parameters: %s" % split_stream_str)

	# @one_time(any_format) # one_line(one_cmd)
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c copy -f segment -segment_time {tp} \"{split_stream}\"" # copy_streams #is_ok
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale="0:0"\" -profile:v main -level 30 -threads 2 -c:a aac -af \"dynaudnorm\" -f segment -segment_time {tp} \"{split_stream}\"" # full(is_debug)
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c:v libx264 -vf \"scale="0:0"\" -profile:v main -level 30 -threads 2 -c:a copy -f segment -segment_time {tp} \"{split_stream}\"" # only_video
	# f"ffmpeg -hide_banner -y -i \"{filename}\" -map_metadata -1 -threads 2 -c:v copy -threads 2 -c:a aac -af \"dynaudnorm\" -f segment -segment_time {tp} \"{split_stream}\"" # only_audio

	# @one_filesize(only_mkv)
	# mkvmerge -o "output.mkv" --split 100M "input.mkv"

	framecount = def_fc  # tp * parts # 2860

	# filter_framecount(int) # debug
	"""
	try:
		to_fr_pa = {
			"@part_size": framecount // parts,
			"@length": tp * parts,
			"@part_count": framecount // tp,
		}  # is_int / is_int / is_int
		assert all((framecount, parts, tp)), "" # to_fr_pa
	except AssertionError:  # if_null
		logging.warning("@to_fr_pa can't get some parameters for %s" % filename)
	except BaseException as e:  # DevideByZero(integer division or modulo by zero) # if_error
		to_fr_pa_err = (filename, str(e))
		logging.error("@to_fr_pa some error in %s [%s]" % to_fr_pa_err)
	else:  # if_ok
		to_fr_pa_str = (str(to_fr_pa), filename)
		logging.info("@tp_fr_pa %s, current: %s" % to_fr_pa_str)
	"""

	try:
		tp_seg = range(0, def_fc, tp)
	except:
		return []

	try:
		two_times = (tp / 60, tp % 60)  # slice_size(mm, ss)
	except BaseException as e:
		two_times = (tp, str(e))
		logging.error("@tp part_size: %d, error: %s" % two_times)
	else:
		two_times_str = (tp, str(two_times))
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
	)  # 8, 36, 2 # 88737

	try:
		tp_diff = round(
			(lambda l, m: l / m)(framecount / parts, tp) * 100, 2
		)  # less / max # <= 100 # float
	except BaseException as e:
		tp_diff, tp_diff_str = 0, (filename, str(e))
		logging.error("@tp_diff current: %s, error: %s" % tp_diff_str)

	try:
		framecount_diff = round(
			(lambda l, m: l / m)(filter_framecount, framecount) * 100, 2
		)  # less / max # <= 100 # float
	except BaseException as e:
		framecount_diff, framecount_diff_err = 0, (filename, str(e))
		logging.error("@framecount_diff current: %s, error: %s" % framecount_diff_err)

	try:
		parts_diff = round(
			(lambda l, m: l / m)(framecount / tp, parts) * 100, 2
		)  # less / max # <= 100 # float
	except BaseException as e:
		parts_diff, parts_diff_err = 0, (filename, str(e))
		logging.error("@parts_diff current: %s, error: %s" % parts_diff_err)

	try:
		tp_fr_pa_info = {
			"@tp": tp_diff,
			"@framecount": framecount_diff,
			"@parts": parts_diff,
		}
		assert tp_fr_pa_info, ""
	except AssertionError:
		logging.warning(
			"@tp_fr_pa_info cant calc tp/framecount/parts, current: %s" % filename
		)
	else:
		tp_fr_pa_info_str = (str(tp_fr_pa_info), filename)
		logging.info("%s, current: %s" % tp_fr_pa_info_str)

	# tp_seg = range(0, def_fc, tp)

	try:
		# dl = {str(chunk): str(chunk + tp) for i, chunk in enumerate(chunks)} # for_sequence(- 1)
		dl = {str(chunk): str(tp) for item, chunk in enumerate(tp_seg)}  # for_ffmpeg

		assert dl, ""
	except AssertionError:
		return []

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
	except BaseException as e:  # if_error
		new_value_err = (str(e), filename)
		logging.error("@new_value error: %s, current: %s" % new_value_err)
	else:  # if_ok
		# print((last_key, last_value, new_value)) #; '@last_key/@last_value/@new_value 2852;124;8'
		logging.info(
			"@last_key/@last_value/@new_value %s"
			% ";".join([str(last_key), str(last_value), str(new_value)])
		)

		dl[str(last_key)] = str(new_value)  # обновить_недостающее_количество_кадров

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

	try:
		sm_status = False if len(set(dl.values())) == 1 else True  # True
	except:
		sm_status = str(None)

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
		if any((not pr, not le)):
			logging.warning("profile: %s, level: %s [%s]" % (pr, le, filename))
		else:
			logging.warning("no profile, no level [%s]" % filename)

		return []

	try:
		codecs = wh.get_codecs(filename)  # ['h264', 'aac']
		assert codecs, ""
	except AssertionError:
		logging.warning("no codecs [%s]" % filename)

		return []

	try:
		w, h, ic = wh.get_width_height(filename, is_calc=True, maxwidth=640)
		assert all((w, h)), ""
	except AssertionError:
		if any((not w, not h)):
			logging.warning("width: %d, height: %d [%s]" % (w, h, filename))
		else:
			logging.warning("no width, no height [%s]" % filename)

		return []

	# sar=(w/h) ; par=(sar/(w/h)) ; dar=(sar * par)

	# aspect_ratio
	# """
	sar = par = dar = None

	try:
		assert any((w, h)), ""  # all -> any
	except AssertionError:
		logging.warning("w/h %s, current: %s" % ("x".join([str(w), str(h)]), filename))
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
				"@sar/w/h %s, current: %s"
				% ("x".join([str(sar), str(w), str(h)]), filename)
			)  # scale

	try:
		assert any((sar, w, h)), ""  # all -> any
	except AssertionError:
		logging.warning(
			"@sar/w/h %s, current: %s"
			% ("x".join([str(sar), str(w), str(h)]), filename)
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
				% ("x".join([str(par), str(sar), str(w), str(h)]), filename)
			)  # pixel

	try:
		assert any((sar, par)), ""  # all -> any
	except AssertionError:
		logging.warning(
			"@sar/@par %s, current: %s" % ("x".join([str(sar), str(par)]), filename)
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
				% ("x".join([str(dar), str(sar), str(par)]), filename)
			)  # display
	# """

	# del wh # clear_mem # debug

	is_scale = ic == True  # need_change_scale

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
		if pr_le_sc.count(True) != 3:  # some_optimized
			init_nometa_vfile = "-map_metadata -1 -preset medium -threads 2 -c:v libx264"  # video_stabilize
		elif pr_le_sc.count(True) == 3:  # all_optimized
			init_nometa_vfile = (
				"-map_metadata -1 -preset medium -threads 2 -c:v copy"  # video_copy
			)
		assert init_nometa_vfile, ""
	except AssertionError:
		init_nometa_vfile = (
			"-map_metadata -1 -preset medium -threads 2 -c:v libx264"  # video_stabilize
		)

	pr_le_str = ""

	# @profile
	if not "main" in pr.lower():
		pr_le_str += "".join([" ", "-profile:v main", " "])

	# @level
	if int(le) > 30:
		pr_le_str += "".join([" ", "-level 30", " "])

	try:
		assert pr_le_str, ""
	except AssertionError:
		logging.warning("@pr_le_str profile and level optimized for '%s'" % filename)
	else:
		logging.info(
			"@pr_le_str profile \"or\" level parameters %s for '%s'"
			% (pr_le_str, filename)
		)

	init_afile = ""

	try:
		if pr_le_sc.count(True) != 3:  # some_optimized
			init_afile = (
				'-threads 2 -c:a %s -af "dynaudnorm"' % "aac"
			)  # sound_stabilize # ffmpeg release?
		elif pr_le_sc.count(True) == 3:  # all_optimized
			init_afile = "-threads 2 -c:a copy"  # sound_copy
		assert init_afile, ""
	except AssertionError:
		init_afile = '-threads 2 -c:a aac -af "dynaudnorm"'  # sound_stabilize

	# project_file = "".join(["\"", path_to_done, filename.split("\\")[-1], "\""]) # done_full_path(debug)
	short_name, ext = filename.split("\\")[-1].split(".")[0], "".join(
		[".", filename.split(".")[-1]]
	)  # short_filename / file_ext

	# w = int(w) if not isinstance(w, int) else w
	# h = int(h) if not isinstance(h, int) else h

	if not isinstance(w, int):
		w = int(w)

	if not isinstance(h, int):
		h = int(h)

	video_filter = ""

	if all((not is_trim, is_scale)):
		video_filter = '-vf "scale=%d:%d"' % (w, h)  # no_trim
	elif all((not is_trim, not is_scale)):  # no_trim # no_scale
		return []

	# debug(one_line/one_cmd)
	# """
	cmd = ""

	# f"ffmpeg -hide_banner -y -i "input.mkv" -threads 2 -c:v libx264 -vf \"scale="0:0"\" -profile:v main -level 30 -threads 2 -c:a aac -af \"dynaudnorm\" -f segment -segment_time {tp} \"{split_stream}\""
	# pr_le_sc = ["main" in pr.lower(), int(le) <= 30, not is_scale] # profile / level / scale

	# filename;"-map_metadata -1 -preset medium -threads 2 -c:v libx264";"-vf \"scale=%d:%d\"" % (w, h);" -profile:v main ";"-threads 2 -c:a aac -af \"dynaudnorm\"";0;filename_03%d

	init_segment = " ".join(
		["-f", "segment", "-segment_time", f"{tp}"]
	)  # is_full_framecount_by_segment

	# str(pr_le_sc.count(True)) # is_debug
	try:
		cmd = " ".join(
			[
				init_ffmpeg,
				init_file,
				init_nometa_vfile,
				video_filter,
				pr_le_str,
				init_afile,
				init_segment,
				"".join(['"', split_stream, '"']),
			]
		)  # filename[src] / vinit / vf / profile(level) / ainit / filename_03%d[dst]
	except BaseException as e:  # AssertionError:
		cmd = ";".join(["".join(["'", filename, "'"]), str(e)])
	finally:
		# scale(True=1, ffmpeg) / profile(True=1, ffmpeg) / level(True=1, ffmpeg) / "any"(True=0) # True(is_optimized)
		if pr_le_sc.count(True) >= 0:
			logging.info(
				"@cmd command: %s" % cmd_whitespace.sub(" ", cmd)
			)  # cmd -> cmd_whitespace.sub("", cmd) # debug

			with open(sequence_list, "a", encoding="utf-8") as slf:
				slf.write(
					"%s\n" % cmd
				)  # writelines # if not_include_regex.findall(cmd):  # skip_copy
	# """

	# save_slide(slide, framecount, filename, width, height)
	# save_slide(slide=5, framecount=framecount, filename, w, h)
	save_slide(5, framecount, filename, w, h)

	try:
		if filename in [*some_dict]:  # some_file / is_skip_update
			some_dict.pop(filename)
	except:
		some_dict[filename] = []

	cnt = 1  # 0 -> 1(start)

	# --- dos_shell(-c copy (fast_copy) / without diff param) ---
	# (dir /r/b/s Short_AAsBBe*p.ext) > ext.lst # check_sort
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

	def concat_short_to_original(filename, is_merge: bool = True):  # debug

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
			part_file = f"{short_file}*p{short_file_ext}".replace(
				"..", "."
			)  # debug(ext) # 'hello_01s01e01p..mp4' -> 'hello_01s01e01p.mp4'
			new_min = 60 * 5  # 300ms(5min)

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

			# (dir /r/b/s Short_AAsBBe*p.ext) > ext.lst
			try:
				line1 = f'(dir /r/b/s "{part_file}") > {merge_files_path}'  # is_ok
			except BaseException as e1:
				line1 = ""
				logging.error("@line1 file: %s, error: %s" % (filename, str(e1)))
			else:
				logging.info("@line1 file: %s, line1: %s" % (filename, line1))

			# (for /f "delims=" %a in (ext.lst) do @echo file '%a') > concat.lst # cmd_line
			# (for /f "delims=" %%a in (ext.lst) do @echo file '%%a') > concat.lst # cmd_file
			try:
				line2 = f"(for /f \"delims=\" %%a in ({merge_files_path}) do @echo file '%%a') > {concat_files_path}"  # is_ok
			except BaseException as e2:
				line2 = ""
				logging.error("@line2 file: %s, error: %s" % (filename, str(e2)))
			else:
				logging.info("@line2 file: %s, line2: %s" % (filename, line2))

			# ffmpeg -f concat -safe 0 -y -i concat.lst -c copy Short_AAsBBe.ext
			try:
				line3 = f'{init_ffmpeg} -f concat -safe 0 -y -i {concat_files_path} -c copy "{only_short}"'  # is_ok
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
				line5 = f"cmd /c del /f {merge_files_path}"  # is_ok
			except BaseException as e5:
				line5 = ""
				logging.error("@line5 file: %s, error: %s" % (filename, str(e5)))
			else:
				logging.info("@line5 file: %s, line5: %s" % (filename, line5))

			# cmd /c del /f concat.lst
			try:
				line6 = f"cmd /c del /f {concat_files_path}"  # is_debug
			except BaseException as e6:
				line6 = ""
				logging.error("@line6 file: %s, error: %s" % (filename, str(e6)))
			else:
				logging.info("@line6 file: %s, line6: %s" % (filename, line6))

			# cmd /c del /f "Hello_01s01e*p.mp4"
			try:
				line7 = f'cmd /c del /f "{part_file}"'  # is_debug(diskspace)
			except BaseException as e7:
				line7 = ""
				logging.error("@line7 file: %s, error: %s" % (filename, str(e7)))
			else:
				logging.info("@line7 file: %s, line7: %s" % (filename, line7))

			some_dict[filename].append(line1)  # list_files
			some_dict[filename].append(line2)  # concat_list_files
			some_dict[filename].append(line3)  # concat_by_ffmpeg

			some_dict[filename].append(line4)  # if_need_timer

			some_dict[filename].append(line5)  # remove("ext.lst") # is_debug
			some_dict[filename].append(line6)  # remove("concat.lst") # is_ok

			some_dict[filename].append(line7)  # remove_old_parts # is_ok

	if all(
		(is_trim, pr_le_sc.count(False) > 0)
	):  # is_trim / "skip_trim" / need_optimize
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

			if is_trim:  # @scale
				# video_filter = "-vf \"trim=%d:%d,scale=%d:%d\"" % (int(k), int(v), w, h) if is_scale else "-vf \"trim=%d:%d\"" % (int(k), int(v))
				video_filter = (
					'-vf "scale=%d:%d"' % (w, h) if is_scale else ""
				)  # -ss / -to

			# '''
			if all((video_filter, pr_le_str)):  # +vf / +profile / +level
				video_filter = " ".join([video_filter, pr_le_str])
			elif all((not video_filter, pr_le_str)):  # +profile  / +level
				video_filter = pr_le_str
			# '''

			# logging.info("%s [%s]" % (video_filter, filename)) # is_heap(kucha/no_log)

			# test(2003) -> test(2003)_01p # filename_01s01e -> filename_01s01e01p

			# ? / Assasin_iz_buduxhego_HD(2020)01p_.mp4

			# if all((not year_regex.findall(filename), ffmpeg)):
			# cmd_line.append("-movflags faststart") # seek(0)

			# ext_filter = if ext

			# ext(mp4)

			# if cnt <= parts:
			sep_for_file = (
				"".join(["_", one_to_double(cnt), "p", ext])
				if year_regex.findall(short_name)
				else "".join([one_to_double(cnt), "p", ext])
			)

			# ofilename = "".join(["\"", path_to_done, "".join([short_name, "".join([one_to_double(cnt), "p", ext]), "\""])]) # for_big_films(low_end_pc)
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
			)  # -ss / -to
			# cmd_str.append(" ".join([init_ffmpeg, init_file, init_nometa_vfile, video_filter, init_afile, ofilename])) # project_file -> ofilename

			if not filename in [*some_dict]:
				some_dict[filename] = [space_regex.sub(" ", cmd_str[-1])]
			else:
				some_dict[filename].append(space_regex.sub(" ", cmd_str[-1]))

			cnt += 1  # new_pos(is_add_all) # debug

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

	elif all((not is_trim, pr_le_sc.count(False) > 0)):  # is_no_trim / need_optimize
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
		)

		if not filename in [*some_dict]:
			some_dict[filename] = [
				space_regex.sub(" ", cmd_str[-1])
			]  # update_every_time
		else:
			some_dict[filename].append[space_regex.sub(" ", cmd_str[-1])]

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
		# ready_dict = {k:v for k, v in some_dict.items() if list(filter(lambda x: "ffplay" in x, tuple(v)))} # optimized

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

	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump(
			some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=True
		)  # default_save(exists/cmd_file)

	# create_cmd_file_after_generate # need_change_script_for_ready_files
	for k, v in some_dict.items():
		try:
			assert os.path.exists(k), ""
		except AssertionError:
			logging.warning("Файл %s не найден и будет пропущен" % k)
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

			try:
				fsize2 = os.path.getsize(
					"".join(
						[
							path_to_done,
							k.split("\\")[-1].replace(k.split(".")[-1], "cmd"),
						]
					)
				)
			except:
				fsize2 = 0

			try:
				assert bool(fsize1 != fsize2), ""
			except AssertionError:
				try:
					logging.info(
						"Файл %s уже создан и будет удален"
						% k.replace(k.split(".")[-1], "cmd")
					)  # if_exists
					os.remove(k.replace(k.split(".")[-1], "cmd"))
				except BaseException as e:
					fsize_err = (
						k.replace(k.split(".")[-1], "cmd").split("\\")[-1],
						str(e),
					)
					logging.error("%s [%s]" % fsize_err)
			else:
				if fspace(
					k.replace(k.split(".")[-1], "cmd"),
					"".join(
						[
							path_to_done,
							k.split("\\")[-1].replace(k.split(".")[-1], "cmd"),
						]
					),
				):  # try_fspace(debug)
					try:
						logging.info(
							"Файл будет перемещён в %s"
							% "".join(
								[
									path_to_done,
									k.split("\\")[-1].replace(k.split(".")[-1], "cmd"),
								]
							)
						)  # source
						move(
							k.replace(k.split(".")[-1], "cmd"),
							"".join(
								[
									path_to_done,
									k.split("\\")[-1].replace(k.split(".")[-1], "cmd"),
								]
							),
						)  # destonation
					except BaseException as e2:
						fsize_err = (
							k.replace(k.split(".")[-1], "cmd").split("\\")[-1],
							str(e2),
						)
						logging.error("%s [%s]" % fsize_err)

	# with open(trimer_base, "w", encoding="utf-8") as tbf:
	# json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=True)	# save_by_filter

	# del some_dict # clear_mem # debug
	return cmd_str


# fsf - folders(str), ext - extention(str), filter_list - short_text(list)
async def scan_folder(fsf: str = "", ext=".mp4", filter_list: list = []) -> list:

	folders = files = []

	folders_dict: dict = {}

	# generate_files_from_folder
	try:
		folders = [
			os.path.join(a, cf)
			for a, _, c in os.walk(fsf)
			for cf in c
			if os.path.isdir(a)
		]  # in_folders
		assert folders, ""
	except AssertionError:
		folders = [
			os.path.isdir(a, bf)
			for a, b, _ in os.walk(fsf)
			for bf in b
			if os.path.isdir(os.path.join(a, bf))
		]  # in_subfodlers
	finally:
		logging.info("@folders %s" % ";".join(folders))

	folders = sorted([*folders], key=os.path.getmtime) if folders else []

	files = [
		os.path.join(folders, f)
		for f in os.listdir(folders)
		if os.path.isfile(os.path.join(folders, f)) and video_regex.findall(f)
	]

	return files


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


def speed_calc(filename, date1, date2) -> int:  # скорость обработки данных (v = s / t)

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
			speed_file = (
				fsize / abs(date1 - date2).seconds
			)  # S = A / T # скорость передачи # V = S / T
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

		logging.info("@speed_file %d, current: %s" % (speed_file, filename))

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


def time_calc(filename, speed_file) -> int:  # время обработки файла ( t = s / v)

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
			time_file = int(time_file) if not isinstance(time_file, int) else time_file
		except:  # ValueError
			time_file = 0

		logging.info("@time_file %d, current: %s" % (time_file, filename))

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
			time_list = filter_time
			time_list_str = (str(time_list), filename)
			logging.info("@time_list %s, current: %s" % time_list_str)

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

		logging.info("@fl @time_by_framecount %s" % ";".join([filename, fl[filename]]))

		try:
			fl = {k: v for k, v in fl.items() if os.path.exists(k)}

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


def data_calc(filename, time_file, speed_file) -> int:  # общий размер файла (s = t * v)

	sizes_dict: dict = {}

	sizes_dict[1] = "Kb"
	sizes_dict[2] = "Mb"
	sizes_dict[3] = "Gb"

	try:
		data_file = (
			time_file * speed_file
		)  # A = T * S # сколько данных было передано # S = T * V
		assert data_file, ""
	except AssertionError:
		logging.warning("@data_file is null, current: %s" % filename)
	except BaseException as e:
		data_file, date_file_err = 0, (filename, str(e))
		logging.error("@data_file current: %s, error: %s" % date_file_err)

	try:
		data_file = int(data_file) if not isinstance(data_file, int) else data_file
	except:  # ValueError
		data_file = 0

	logging.info("@data_file %s, current: %s" % (str(data_file), filename))

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


if __name__ == "__main__":  # skip_main(debug)

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

	try:
		assert periods, ""
	except AssertionError:
		logging.warning("no periods")
	else:
		with open(combine_base, "w", encoding="utf-8") as cbf:
			# cbf.writelines("%s\n" % p for p in periods)
			cbf.writelines("%s\\\n" % p for p in periods)  # totalcommander
	# """

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
	# '''

	# @new_base
	"""
	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump({}, tbf, ensure_ascii=False, indent=4, sort_keys=False) # clear_after_load
	"""

	sm = ln = ag = cntfiles = sf = files_count = len_files = 0  # int
	all_period_dict = folders_filter = {}  # dict
	fsizes = (
		files
	) = (
		files2
	) = (
		folders
	) = new_folders = old_folders = some_files_filter = period_files = []  # list
	all_period_set = (
		some_folders
	) = some_subfolders = some_files = set()  # ("", "", 0) / folders / files # set

	seasyear_count = {}

	# @sorted_by_filter
	# """
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
	# """

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

	filter_files = []

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

	# @add_equal_files
	# """
	if all((files, faf_sorted_tuple)):  # files / files_with_filter
		for a, b in faf_sorted_tuple:
			try:
				assert bool(a in files), ""
			except AssertionError:
				continue
			else:
				filter_files.append(a)

		if all((filter_files, files)):
			logging.info(
				"@filter_files/@files filter %s" % str(len(filter_files) == len(files))
			)  # equal(True) / diff(False)
	# """

	# """
	try:
		ag = avg_calc(sm, ln)  # avg_calc(100, 2) # 50
	except:
		ag = 0  # 0
	# """

	logging.info("@files/@folders/@ag %d %d %d" % (len(files), len(folders), ag))

	# debug
	# exit()

	mx_set = set()
	mx1 = mx2 = mx3 = 0

	try:
		some_files = sorted(
			some_files, key=os.path.getmtime
		)  # if some_files_filter else sorted(some_files, key=os.path.getmtime)
		assert some_files, ""
	except AssertionError:
		logging.warning("@some_file no files")
	else:
		logging.info(";".join(some_files))  # debug(print)
		logging.info("@some_files count: %d" % len(some_files))  # 0?

	for sf in filter(
		lambda x: os.path.isfile(x), tuple(some_files)
	):  # folder_scan_full
		period_list_filter = []

		today = datetime.now()
		fdate = os.path.getmtime(sf)
		ndate = datetime.fromtimestamp(fdate)

		try:
			days_ago = abs(today - ndate).days
			assert bool(days_ago >= 0), ""
		except AssertionError:  # if_none(today)
			continue  # days_ago = 0

		max_days_by_year = 366 if today.year % 4 == 0 else 365

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
				sf,
			)  # any_day / week / month / year / file
			assert plf, ""
		except AssertionError:
			plf = (sf.split("\\")[-1],)
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
			logging.warning("@days_ago error period, folder: %s" % sf.split("\\")[-1])
			continue
		except BaseException as e:
			days_ago_err = (str(e), sf.split("\\")[-1])
			logging.error("@days_ago error: %s, folder: %s" % days_ago_err)
			continue
		else:
			# period_list_filter.append(days_ago >= 0) # all_days(if_only_day)
			logging.info("@plf %s" % str(plf))

		if period_list_filter.count(True) > 0 and not sf in period_files:
			period_files.append(sf)
		# elif period_list_filter.count(True) == 0 and sf in period_files:
		# period_files.pop(sf)

	some_files = sorted(
		period_files, key=os.path.getmtime
	)  # if some_files_filter else sorted(some_files, key=os.path.getmtime)

	tim, date1, timer = time(), datetime.now(), 0

	for sf in filter(lambda x: os.path.isfile(x), tuple(some_files)):

		# files = []
		# jobs = [] # gevent.monkey(is_async)
		# gevent.monkey.patch_all() # optimal_run(is_async/debug)

		files_count += 1

		# jobs = [gevent.spawn(calc_parts, filename=sf.strip(), is_update=True, parts=10, is_run=False)] # debug

		# gevent.wait(jobs) # gevent(is_async/debug)

		cmd_str = []

		try:
			cmd_str = calc_parts(
				filename=sf.strip(), is_update=True, parts=10, is_run=True
			)

			try:
				assert cmd_str, ""
			except AssertionError:
				logging.warning("@calc_parts current[is_ready]: %s" % sf.strip())
			except BaseException as e:
				cmd_str_err = (sf.strip(), str(e))
				logging.error("@calc_parts current: %s, error: %s" % cmd_str_err)
		except BaseException as e2:
			cmd_str_err2 = (sf.strip(), str(e2))
			logging.error("@calc_parts current: %s, error: %s" % cmd_str_err2)  # error#
			# continue
		else:
			cmd_status = (
				space_regex.sub(" ", cmd_str[-1])
				if cmd_str
				else "%s is ready" % add.full_to_short(sf.strip())
			)
			print(cmd_status)  # last_cmd_or_ready_status
			logging.info("@calc_parts last: %s" % cmd_status)  # sf.strip()

		tim2, date2 = time(), datetime.now()

		timer = abs(tim - tim2)

		logging.info(
			"@difference_time: %s" % str(difference_time(date1, date2))
		)  # debug # eliminate_time

	# @load_for_filter
	try:
		with open(trimer_base, encoding="utf-8") as tbf:
			some_dict = json.load(tbf)
	except:
		some_dict = {}

		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump(
				{}, tbf, ensure_ascii=False, indent=4, sort_keys=True
			)  # save_full

	some_dict_old: dict = {}

	# pass_2_of_2
	# """
	# "E:\\Multimedia\\Video\\Serials_Europe\\Medium_Rus\\Medium_02s03e.mp4": ["cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -ss 0 -hide_banner -y -i \"E:\\Multimedia\\Video\\Serials_Europe\\Medium_Rus\\Medium_02s03e.mp4\" -to 311 -map_metadata -1 -preset medium -threads 2 -c:v libx264 -profile:v main -level 30 -threads 2 -c:a aac -af \"dynaudnorm\" \"c:\\downloads\\list\\Medium_02s03e01p.mp4\""]
	if some_dict:
		with open(trimer_base, "w", encoding="utf-8") as tbf:
			json.dump(some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=True)

		some_dict_old = some_dict

		# generate_cmd_for_all_jobs_after_finish
		with open(cmd_list, "w", encoding="utf-8") as clf:  # cmd_lines
			clf.writelines(
				"%s\n" % f for _, v in some_dict.items() for f in v
			)  # multicommander
			# clf.writelines("%s\\\n" % f for _, v in some_dict.items() for f in v) # totalcommander

		some_dict = {
			k: v
			for k, v in some_dict.items()
			if list(filter(lambda x: "ffmpeg" in x, tuple(v)))
		}  # not optimized

		for k, _ in some_dict_old.items():
			if not k in [*some_dict] and os.path.exists(
				k.replace(k.split(".")[-1], "cmd")
			):
				os.remove(k.replace(k.split(".")[-1], "cmd"))

		a, cnt, last_file = len(some_dict), 0, ""

		date1 = datetime.now()  # start_time

		ms_set = run_set = set()

		# filename = "7f_30.Monedas.S01E06.Guerra.Santa.1080p.HBO.WEB-DL.Rus.Spa.Eng.BenderBEST.a1.09.01.21.mp4"
		# l, pl, pt = add.parse_file(k) # len / parse_list / parse_text # (0, [], []) # parse_original_http_from_description_file

		for k, v in some_dict.items():  # {filename: [cmd]} # update_run_files
			"""
			s = "c:\\downloads\\mytemp\\downloads.txt"

			>>> "\\".join(s.split("\\")[::-1]) # 'downloads.txt\\mytemp\\downloads\\c:  # reverse_path
			>>> s.split("\\")[-1::] # ['downloads.txt'] # only_short_name
			>>> "\\".join(s.split("\\")[:-1:]) # 'c:\\downloads\\mytemp' # only_folder
			"""

			# if os.path.exists(k.replace(k.split(".")[-1], "cmd")):  # clear_old_cmd
			# os.remove(k.replace(k.split(".")[-1], "cmd"))

			with open(
				k.replace(k.split(".")[-1], "cmd"), "w", encoding="utf-8"
			) as mcf:  # save_new_cmd(is_multi_line)
				mcf.writelines("%s\n" % cmd for cmd in v)  # multicommander(list)
				# mcf.writelines("%s\\\n" % cmd for cmd in v) # totalcommander(list)

			if fspace(
				k.replace(k.split(".")[-1], "cmd"),
				"".join(
					[path_to_done, k.split("\\")[-1].replace(k.split(".")[-1], "cmd")]
				),
			):  # try_fspace(debug)
				move(
					k.replace(k.split(".")[-1], "cmd"),
					"".join(
						[
							path_to_done,
							k.split("\\")[-1].replace(k.split(".")[-1], "cmd"),
						]
					),
				)

		def calcProcessTime(starttime, cur_iter, max_iter, filename):
			telapsed = time() - starttime
			testimated = (telapsed / cur_iter) * (max_iter)

			finishtime = starttime + testimated
			finishtime = datetime.fromtimestamp(finishtime).strftime(
				"%H:%M:%S"
			)  # in time

			lefttime = testimated - telapsed  # in seconds

			return (int(telapsed), int(lefttime), finishtime, filename)

		strt, cur_iter, max_iter = time(), 0, len(some_dict)

		t = Timer(max_iter)

		te_set = set()

		# show_meta_info(if_run)
		# """
		for k, v in some_dict.items():  # {filename: [cmd]} # run_job_by_time
			try:
				assert os.path.exists(k) and all((v, isinstance(v, list))), ""
			except AssertionError:
				logging.warning("file %s not exists" % k)
				continue  # skip_if_some_(not_exists/null)
			except BaseException as e:
				some_dict_err = (k, str(e))
				logging.error("error in file %s [%s]" % some_dict_err)

			last_file = k

			try:
				assert bool(k in run_set), ""  # run_one_times
			except AssertionError:
				run_set.add(k)
			else:
				continue

			# sleep(1) # 0.05
			cur_iter += 1

			try:
				assert v, ""  # run_if_have_cmd
			except AssertionError:  # if_no_cmd(skip)
				continue
			else:
				for vstr in filter(lambda x: x, tuple(v)):
					# os.system("%s" % vstr) # if_run(debug) # if_manual(skip)

					date2 = datetime.now()  # end_time

					# calc_parts(is_run = False)
					try:
						b = 1 / abs(date1 - date2).seconds
						assert all(
							(a * b > 0, abs(date1 - date2).seconds > 0)
						), ""  # some_time > 0, time > 0
					except AssertionError:
						logging.warning("@some_dict/@k: %s" % k)
					except BaseException as e:  # division by zero
						some_dict_err = (k, str(e))
						logging.error("@some_dict/@k: %s, error: %s" % some_dict_err)
					else:
						cnt += 1

						try:
							speed_file = (
								os.path.getsize(k) // abs(date1 - date2).seconds
							)  # s / t # mb / s
							time_file = os.path.getsize(k) // speed_file  # s / v # s
							data_file = speed_file * time_file  #  v * t # mb
							assert all((speed_file, time_file, data_file)), ""
						except AssertionError:
							logging.warning(
								"speed/time/data current: %s, error calc!" % k
							)
						except BaseException as e:
							speed_file = time_file = data_file = 0
							std_err = (k, str(e))
							logging.error(
								"speed/time/data current: %s, error: %s" % std_err
							)
						else:
							# {'@speed[mb/s]': 0, '@time[s]': 0, '@data[mb]': 0, '@file': 'test.tst'} # @trim.log

							logging.info(
								str(
									{
										"@speed": speed_file,
										"@time": time_file,
										"@data": data_file,
										"@file": k,
									}
								)
							)  # original_value
							# logging.info(str({"@speed[mb/s]": (speed_file / (1024**2)), "@time[s]": (time_file / 60), "@data[mb]": (data_file // (1024**2)), "@file": k})) # original_value

						try:
							new_time = date1 - timedelta(
								seconds=-ms_to_time(a * b)
							)  # datetime.datetime(2024, 5, 31, 11, 55, 51, 529282) # time
							new_time = abs(date1 - new_time).seconds  # ms
							assert new_time, ""
						except AssertionError:
							logging.warning("@new_time %s" % k)
						except BaseException as e:
							new_time_err = (k, str(e))
							logging.error(
								"@new_time current: %s, error: %s" % new_time_err
							)
						else:
							try:
								assert all((new_time >= 0, new_time in ms_set)), ""
							except AssertionError:
								if (
									not new_time in ms_set
								):  # unique_ms_only(any_count_files)
									ms_set.add(new_time)

							else:
								skip_str = run_str = ""
								if cnt > a:
									skip_str = "Пропущено: %d" % abs(cnt - a)
								elif cnt <= a:
									run_str = "Обработано %d из %d" % (cnt, a)

								try:
									skip_or_run_str = run_str if run_str else skip_str
								except:
									skip_or_run_str = str(None)

								print(
									"Осталось %d ms до окончания обработки, всего: %d, задач: %d, debug: %s, current: %s"
									% (
										new_time,
										cnt,
										a,
										skip_or_run_str,
										add.full_to_short(k),
									)
								)
								logging.info(
									"Осталось %d ms до окончания обработки, всего: %d, задач: %d, debug: %s, current: %s"
									% (
										new_time,
										cnt,
										a,
										skip_or_run_str,
										add.full_to_short(k),
									)
								)

			try:
				sleep(60 - time() + strt)  # pause_for_debug
			except:
				sleep(0.05)

			# prstime = calcProcessTime(strt, cur_iter, max_iter, k) # some_value_as_set
			# print("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % prstime)
			# logging.info("time elapsed: %s(s), time left: %s(s), estimated finish time: %s, current: %s" % prstime)

			try:
				assert bool(t.remains(cur_iter) in te_set), ""
			except AssertionError:
				prstime = (t.remains(cur_iter), k)

				try:
					te_set.add(prstime[0])  # t.remains(cur_iter)
				except BaseException as e:
					te_str = (str(e), k)
					logging.error("@te_str add error: %s, current: %s" % te_str)
				else:
					print(
						"@prstime left: %s(s), current: %s" % prstime
					)  # t.remains(cur_iter)
					logging.info("@prstime left: %s(s), current: %s" % prstime)
			except BaseException as e2:
				te_err = (str(e2), k)
				logging.error("@te_str error: %s, filename: %s" % te_err)
			else:
				prstime = (t.remains(cur_iter), k)

				print(
					"@prstime left: %s(s), current: %s" % prstime
				)  # t.remains(cur_iter)
				logging.info("@prstime left: %s(s), current: %s" % prstime)

		else:
			logging.info(
				"@some_dict time_end: %s, current: %s"
				% (str(datetime.now()), last_file)
			)
		# """

	with open(trimer_base, "w", encoding="utf-8") as tbf:
		json.dump(
			some_dict, tbf, ensure_ascii=False, indent=4, sort_keys=True
		)  # save_by_filter

	# """

	# del some_dict # clear_mem # debug

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
		if os.path.exists(log_print) and os.path.getsize(log_print):
			fsizes_lst = [
				(os.path.getsize(log_print) // (1024**i), sizes_dict[i])
				for i in range(1, 4)
				if os.path.getsize(log_print) // (1024**i) > 0
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

	"""
	if os.path.exists(log_print):
		lpf_lines = []

		splited_dict = {}

		splited_set = set()

		# string = "hello world"
		splited_regex = re.compile(r"(\w+|\d+|^\s+)", re.I)
		# splited = ";".join(splited_regex.split(string)); print(splited)

		try:
			with open(log_print, encoding="utf-8") as lpf:
				lpf_lines = lpf.readlines()
		except:
			with open(log_print) as lpf:  # no_encoding
				lpf_lines = lpf.readlines()

		for ll in lpf_lines:
			try:
				assert bool(";".join(ll.split(" ")) in splited_set), "" # assert bool(";".join(splited_regex.split(ll)) in splited_set), ""
			except AssertionError:
				splited_set.add(";".join(ll.split(" "))) # splited_set.add(";".join(splited_regex.split(ll)))

			try:
				splited_dict[";".join(ll.split(" "))] = splited_dict.get(";".join(ll.split(" ")), 0) + 1
				# splited_dict[";".join(splited_regex.split(ll))] = splited_dict.get(";".join(splited_regex.split(ll)), 0) + 1 # ;xlevel;=;30;
			except:
				continue

		for k, v in splited_dict.items():
			if v > 1:  # elif v == 1:
				logging.info("@splited_dict not unique %s" % k) # logging.info("@splited_dict unique %s" % k)
			else:
				continue
	"""

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
		# script_path = os.path.dirname(os.path.realpath(__file__)).lower()
		filename = "\\".join([script_path, __file__.replace(ext, ".glob")])  # ?
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
