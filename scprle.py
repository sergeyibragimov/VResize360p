# -*- coding: utf-8 -*-

# Полуавтоматическое форматрирование файлов с метаданными(scale/profile/level)
# Целый файл без разрезов(скрыть если не нужно)

# from os import getcwd # cpu_count  # текущая папка # cpu_count
# from psutil import cpu_count  # viirtual_memory # pip install --user psutil
# import gevent.monkey # pip install --user gevent # is_async(debug)
# import psutil
from datetime import datetime, timedelta  # дата и время
from shutil import (
	disk_usage,
	move,
)  # copy # файлы # usage(total=16388190208, used=16144154624, free=244035584)
from subprocess import (
	run,
)  # TimeoutExpired, check_output, Popen, call, PIPE, STDOUT # Работа с процессами # console shell=["True", "False"]
from time import time, sleep
import asyncio  # TaskGroup(3.11+)
import json  # JSON (словарь)
import logging  # журналирование и отладка
import os  # система
import re  # реуглярные выражения/regular expression # .*(\?|$)
import sys

# pip install --user youtube-dl # youtube-dl --hls-prefer-native "http://host/folder/file.m3u8" # youtube-dl -o "%%(title)s.%%(resolution)s.%%(ext)s" --all-formats "https://v.redd.it/8f063bzbdx621/HLSPlaylist.m3u8"

# debug_moules
# exit()

# mklink /h scale_profile_level.py scprle.py

# abspath_or_realpath
basedir = os.path.dirname(os.path.abspath(__file__)).lower()  # folder_where_run_script
script_path = os.path.dirname(os.path.realpath(__file__)).lower()  # is_system_older
current_folder = "".join([os.path.dirname(os.path.realpath(sys.argv[0])), "\\"])

dletter = "".join(
	[basedir.split("\\")[0], "\\"]
)  # "".join(script_path[0:5]) if script_path else "".join(os.getcwd()[0:5])

# logging(start)
log_file = "%s\\scprle.log" % script_path  # main_debug(logging)

# --- path's ---
path_for_queue = r"d:\\downloads\\mytemp\\"
path_to_done = "%sdownloads\\list\\" % dletter  # "c:\\downloads\\" # ready_folder
path_for_folder1 = "".join([os.getcwd(), "\\"])  # "c:\\downloads\\new\\"

cmd_list = "%s\\scprle.cmd" % script_path  # command_lines_for_(scale/profile/level)
fcd_base = "%s\\fcd.json" % script_path  # jobs_base(json)
fcd_lst = "%s\\fcd.lst" % script_path  # jobs_base(list)

# list(json)_by_period
days_ago_base = "%s\\days_ago.lst" % script_path
days_ago_list = "%s\\days_ago.txt" % script_path  # txt_by_list(one_day_ago_base)
month_forward_base = "%s\\month_forward.lst" % script_path
calc_year_base = "%s\\calc_year.lst" % script_path
all_period_json = "%s\\all_period.json" % script_path
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
	except:
		exit()  # path_to_done = "c:\\downloads\\"

# @regex
# video_regex = re.compile(r"(.*)(?:(_[\d+]{2,4}s|\([\d+]{4}\)))(.*)(?:(.qt|.mpg|.mp2|.mp3|.mpv|.mp4|.m4p|.m4v|.mpe|.mpv|.avi|.wmv|.mov|.flv|.f4v|.swf|.mkv|.webm|.mpeg|^.dmf|^.txt|^.srt|^.vtt|^.dmfr|^.aria2|^.crswap|^.filepart|^.crdownload))$", re.M)
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

start = time()

# files_count = 0

mytime = {
	"jobtime": [9, 18, 5],
	"dinnertime": [12, 14],
	"sleeptime": [0, 8],
	"anytime": [True],
}  # sleep_time_less_hour # debug


# @oop
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


class Additional:
	def __init__(self):
		pass

	# change_full_to_short(if_need_or_test_by_logging) # temporary_not_use
	def full_to_short(self, filename) -> str:
		self.filename = filename

		try:
			assert filename and os.path.exists(
				self.filename
			), f"Файл отсутствует @full_to_short/{self.filename}"  # is_assert_debug # filename
		except AssertionError:
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
		except BaseException:
			short_filename = filename.strip()  # if_error_stay_old_filename

		return short_filename

	def __del__(self):
		print("%s удалён" % str(self.__class__.__name__))


add = Additional()


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

	pass

	"""
	create_files = []
	
	# create_files.extend([[period_base, cmd_list, log_file, fcd_base, fcd_lst, days_ago_base, days_ago_list, month_forward_base, calc_year_base, all_period_json]])
	create_files.extend([[period_base, cmd_list, log_file, fcd_lst]]) # fcd_base # skip_periods

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

# pass_1_of_2

# @fcd_base; load / create(if_error)
try:
	with open(fcd_base, encoding="utf-8") as fjf:
		fcd = json.load(fjf)
except:
	fcd = {}

	with open(fcd_base, "w", encoding="utf-8") as fjf:
		json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=False)

if fcd:
	for k, _ in fcd.items():
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
	with open(fcd_base, "w", encoding="utf-8") as fjf:
		json.dump({}, fjf, ensure_ascii=False, indent=4, sort_keys=False) # clear_after_load
	"""

# @fcd_base; create(clear)
fcd = {}

with open(fcd_base, "w", encoding="utf-8") as fjf:
	json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=False)


class VideoProject:
	def __init__(self):
		pass

	def width_and_height(self, filename, is_log: bool = True):
		global job_count

		self.filename = filename

		# ffprobe -v error -show_entries stream=width,height -of csv=p=0:s=x input.m4v
		cmd_wh = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=width,height",
			"-of",
			"csv=p=0:s=x",
			self.filename,
		]  # output_format
		wi = "".join([current_folder, "wh.nfo"])  # path_for_queue

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
				print("debug [w/h error]: %s" % self.filename)
		finally:
			logging.info(
				"filename: %s, width/height: %s"
				% (add.full_to_short(filename), "x".join([str(width), str(height)]))
			)

			if all((width, height)):
				job_count += 1  # need_scale(debug)
				return (int(width), int(height), False)
			elif any((not width, not height)):
				return (0, 0, False)

	def get_profile_and_level(self, filename):
		global job_count

		self.filename = filename

		cmd_pl = [
			path_for_queue + "ffprobe.exe",
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
				"x".join([str(pl_list[0]), str(pl_list[-1])]),
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
				# write_log("debug profilelevel", ";".join([pl_list[0].split("=")[-1].lower().strip(), pl_list[1].split("=")[-1].lower().strip(), filename]))

				job_count += 1  # need_profile(debug)

				return (
					pl_list[0].split("=")[-1].lower().strip(),
					pl_list[1].split("=")[-1].lower().strip(),
				)  # [main,30]

	def get_length(self, filename):
		self.filename = filename

		cmd_fd = [
			path_for_queue + "ffprobe.exe",
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
		cmd = [
			path_for_queue + "ffprobe.exe",
			"-v",
			"error",
			"-show_entries",
			"stream=codec_name",
			"-of",
			"csv=p=0:s=x",
			filename,
		]  # output_format
		ci = "".join([current_folder, "codecs.nfo"])  # path_for_queue

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
		print("%s удалён" % str(self.__class__.__name__))


vp = VideoProject()


# @procedures
def hms(seconds: int = 0):
	try:
		h, m, s = seconds // 3600, seconds % 3600 // 60, seconds % 3600 % 60
		assert all(
			(h, m, s)
		), f"Нет какой-то величины времени @hms/{h}/{m}/{s}"  # is_assert_debug
	except AssertionError as err:  # if_null
		logging.warning("Нет какой-то величины времени @hms/%d" % seconds)
		raise err
	except BaseException as e:  # if_error
		h = m = s = 0
		h_m_s_err = (seconds, str(e))
		logging.error("Нет какой-то величины времени @hms/%d [%s]" % h_m_s_err)

	try:
		ms_time = (lambda hh, mm, ss: (hh * 3600) + (mm * 60) + ss)(h, m, s)  # ms
		# ms_time = '{:02d}:{:02d}:{:02d}'.format(h, m, s)  # hh:mm:ss # '{:02d} час. {:02d} мин. {:02d} сек.'.format(h, m, s) # hh mm ss
	except:
		ms_time = 0  # ms_time = str(ms_time)

	return str(ms_time)


# r"D:\\Multimedia\\Video\\Serials_conv\\Agatha_Christies_Marple\\Agatha_Christies_Marple_01s01e.mp4"
def width_height_profile_level(filename: str = "", ffmpeg: bool = True):

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
		print("%s" % str(e))
		w, h, ch = 0, 0, False
	finally:
		if all((any((w, h)), ch)):
			logging.info("@w @h @ch %s" % str((filename, w, h, ch)))

	try:
		p, l = vp.get_profile_and_level(filename)
		assert all((p, l)), ""
	except AssertionError:
		p = l = ""
	except BaseException as e:
		print("%s" % str(e))
		p = l = ""
	finally:
		if any((p, l)):
			logging.info("@p @l %s" % str((filename, p, l)))

	try:
		length = vp.get_length(filename)
		assert length, ""
	except AssertionError:
		length = -1
	except BaseException as e:
		print("%s" % str(e))
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
		print("%s" % str(e))
		codecs = []
	finally:
		codecs = str(",".join(codecs))
		logging.info("@codecs %s" % codecs)

	# del vp # clear_mem # debug

	try:
		# is_scale = (w > setup_dict["width"]) # 640
		is_scale = w > 640
	except BaseException:
		is_scale = False
	finally:
		logging.info("@is_scale %s" % str((filename, is_scale)))

	try:
		# is_profile = (not setup_dict["profile"] in p.lower()) # "main"
		is_profile = not "main" in p.lower()
	except BaseException:
		is_profile = False
	finally:
		logging.info("@is_profile %s" % str((filename, is_profile)))

	try:
		# is_level = (int(l) > setup_dict["level"]) # 30
		is_level = int(l) > 30
	except BaseException:
		is_level = False
	finally:
		logging.info("@is_level %s" % str((filename, is_level)))

	is_optimal = []

	# is_optimal.append({"scale": is_scale, "profile": is_profile, "level": is_level}) # status

	pr_le_sc = [is_profile, is_level, is_scale]  # profile / level / scale

	cmd_line = []

	if ffmpeg:
		init_ffmpeg = " ".join(
			["cmd /c", "".join([path_for_queue, "ffmpeg.exe"])]
		)  # cmd /k
		cmd_line.append(init_ffmpeg)

		cmd_line.append('-hide_banner -y -i "%s"' % filename)
		cmd_line.append("-map_metadata -1")

		cmd_line.append("-preset medium")  # debug_speed

		if pr_le_sc.count(True) != 3:  # some_optimized
			# cmd_line.append("-threads 2 -c:v %s" % setup_dict["cv"]) # "libx264"
			cmd_line.append("-threads 2 -c:v %s" % "libx264")  # video_optimize
		elif pr_le_sc.count(True) == 3:  # all_optimized
			cmd_line.append("-threads 2 -c:v copy")  # video_copy
	else:
		init_ffplay = " ".join(
			["cmd /c", "".join([path_for_queue, "ffplay.exe"])]
		)  # cmd /k
		cmd_line.append(init_ffplay)

	nw, nh = 0, 0
	np = nl = ""

	if not isinstance(w, int):
		w = int(w)

	if not isinstance(h, int):
		h = int(h)

	"""
	w0 - текущая ширина в пикселях, # 1600
	h0 - текущая высота в пикселях, # 900
	w1 - новая ширина в пикселях, # 640
	h1 - новая высота в пикселях. # 360

	w1 = (w0 * h1) / h0 # формула для вычисления новой ширины, если задана новая высота
	h1 = (h0 * w1) / w0 # формула для вычисления новой высоты, если задана новая ширина
	"""

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
			ar_calc_status = "x".join([str(width), str(height)])
			assert ar_calc_status, ""
		except AssertionError:
			logging.warning(
				"@ar_calc_status some status is null, current: %s" % filename
			)
		except BaseException as e:
			ar_calc_status_err = (str(e), filename)
			logging.error("@ar_calc_status error: %s, current: %s" % ar_calc_status_err)
		else:
			logging.info("@ar_calc/file %s" % ";".join([ar_calc_status, filename]))

		nw, nh = width, height

		changed = bool(w > 640)  # diff_width

		if any((nw != w, nh != h)):
			if not {"width": [nw, w], "height": [nh, h]} in is_optimal:
				is_optimal.append(
					{"width": [nw, w], "height": [nh, h]}
				)  # is_optimal.append({"width": [640, w], "height": [second, h]})

		if changed:
			cmd_line.append('-vf "scale=%s:%s"' % (nw, nh))
	elif not ffmpeg:
		nw, nh = w, h
		cmd_line.append('-vf "scale=%s:%s"' % (nw, nh))

	if all((is_profile, ffmpeg)):
		if not {"profile": ["main", p]} in is_optimal:
			is_optimal.append({"profile": ["main", p]})

		np = "main"

		cmd_line.append("-profile:v %s" % np)

	if all((is_level, ffmpeg)):
		if not {"level": ["30", l]} in is_optimal:
			is_optimal.append({"level": ["30", l]})

		nl = str(30)

		cmd_line.append("-level %s" % nl)

	# if all((not year_regex.findall(filename), ffmpeg)):
	# cmd_line.append("-movflags faststart") # seek(0)

	if ffmpeg:
		if pr_le_sc.count(True) != 3:  # some_optimized
			cmd_line.append(
				'-threads 2 -c:a %s -af "dynaudnorm"' % "aac"
			)  # sound_stabilize # ffmpeg release?
		elif pr_le_sc.count(True) == 3:  # all_optimized
			cmd_line.append("-threads 2 -c:a copy")  # sound_copy

		project_file = "".join([path_to_done, filename.split("\\")[-1]])
		cmd_line.append('"%s"' % project_file)  # ffmpeg
	else:
		cmd_line.append('"%s"' % filename)  # ffplay

	# @ffmpeg/@ffplay
	cmd_status = [
		cl.strip()
		for cl in filter(
			lambda x: any(("scale" in x, "profile" in x, "level" in x)), tuple(cmd_line)
		)
	]
	cmd = " ".join(cmd_line) if cmd_status else ""

	try:
		assert all((nw, nh)), ""
	except AssertionError:
		nw, nh = w, h  # default

	if cmd and all((nw, nh)):  # all((nw, nh, p, l))
		# logging.info("filename: %s, width/height: %s, profile/level: %s, length: %s, cmd: %s" % (filename, "x".join([str(nw), str(nh)]), "x".join([str(p), str(l)]), length, codecs, cmd)) # ffmpeg
		logging.info(
			"filename: %s, width/height: %s, length: %s, codecs: %s, cmd: %s"
			% (
				add.full_to_short(filename),
				"x".join([str(nw), str(nh)]),
				length,
				codecs,
				cmd,
			)
		)  # ffplay

	# print(filename, w, h, p, l, length, codecs, str(is_optimal), sep="\t", end="\n") # 576     320     high    21      [{'profile': 'main'}]

	return (filename, w, h, p, l, length, codecs, str(is_optimal), cmd)


# del add # clear_mem # debug


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


# def one_folder(folder, files_template) -> list:  # for_generator_in
# one_folder("c:\\downloads\\new\\", re.compile(r"(?:(zip))$")) # one_folder
# one_folder("c:\\downloads\\new\\", video_regex)
def one_folder(folder: str = "") -> list:
	files = []

	try:
		files = [
			os.path.join(folder, f)
			for f in os.listdir(folder)
			if os.path.exists(os.path.join(folder, f))
		]
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


# sub_folder("c:\\downloads\\combine\\", re.compile(r"(?:(zip))$")) # sub_folder
# sub_folder("c:\\downloads\\combine\\", video_regex) # sub_folder
def sub_folder(folder, files_template) -> list:
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
	except BaseException:
		fspace_status = False  # fspace(error-False)
	finally:
		return fspace_status


if __name__ == "__main__":  # skip_main(debug)

	dt = datetime.now()

	# """
	main_filter = []

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

	main_filter = list(set(main_filter)) if main_filter else []

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

	# if any((period_files, some_files_filter)):
	# some_files = period_files if period_files else some_files_filter # some_period / another_period

	# @load_base(update)
	"""
	try:
		with open(fcd_base, encoding="utf-8") as fjf:
			fcd = json.load(fjf)
	except BaseException:
		fcd = {}

		with open(fcd_base, "w", encoding="utf-8") as fjf:
			json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=False)
	"""

	# @new_base
	"""
	with open(fcd_base, "w", encoding="utf-8") as fjf:
		json.dump({}, fjf, ensure_ascii=False, indent=4, sort_keys=False)
	"""

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
					"->".join([f.split("\\")[-1], c]),
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
						"=>".join([f.split("\\")[-1], c]),
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
			fcd_time.append((k, os.path.getmtime(k)))

	fcd_sorted = sorted(fcd_time, key=lambda fcd_time: fcd_time[-1])

	fcd_dict_new = {k: v for k, v in fcd.items() for fn, mt in fcd_sorted if k == fn}

	if all((fcd_dict_new, len(fcd) == len(fcd_dict_new))):
		# fcd.update(fcd_dict_new)
		fcd_new = {**fcd, **fcd_dict_new}
		fcd = fcd_new
	# """

	fcd_old: dict = {}

	# pass_2_of_2
	# """
	# "E:\\Multimedia\\Video\\Serials_Europe\\Medium_Rus\\Medium_02s03e.mp4": "cmd /c c:\\downloads\\mytemp\\ffmpeg.exe -hide_banner -y -i \"E:\\Multimedia\\Video\\Serials_Europe\\Medium_Rus\\Medium_02s03e.mp4\" -map_metadata -1 -preset medium -threads 2 -c:v libx264 -vf \"scale=640:360.0\" -profile:v main -level 30 -movflags faststart -threads 2 -c:a aac -af \"dynaudnorm\" \"c:\\downloads\\list\\Medium_02s03e.mp4\"",
	if fcd:
		with open(fcd_base, "w", encoding="utf-8") as fjf:
			json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=True)

		fcd_old = fcd

		with open(cmd_list, "w", encoding="utf-8") as clf:
			clf.writelines("%s\n" % v for _, v in fcd.items())  # multicommander
			# clf.writelines("%s\\\n" % v for _, v in fcd.items()) # totalcommander

		fcd = {k: v for k, v in fcd.items() if "ffmpeg" in v.lower()}  # debug

		for k, _ in fcd_old.items():
			if k not in [*fcd] and os.path.exists(k.replace(k.split(".")[-1], "cmd")):
				os.remove(k.replace(k.split(".")[-1], "cmd"))

		a, cnt, last_file = len(fcd), 0, ""
		date1 = datetime.now()
		fcd_set = ms_set = set()

		def calcProcessTime(starttime, cur_iter, max_iter, filename):
			telapsed = time() - starttime
			testimated = (telapsed / cur_iter) * (max_iter)

			finishtime = starttime + testimated
			finishtime = datetime.fromtimestamp(finishtime).strftime(
				"%H:%M:%S"
			)  # in time

			lefttime = testimated - telapsed  # in seconds

			return (int(telapsed), int(lefttime), finishtime, filename)

		strt, cur_iter, max_iter = time(), 0, len(fcd)

		t = Timer(max_iter)

		te_set = set()

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
				b = 1 / abs(date1 - date2).seconds
				assert all(
					(a * b > 0, abs(date1 - date2).seconds > 0)
				), ""  # some_time > 0, time > 0
			except AssertionError:
				logging.warning("@fcd/@k: %s" % k)
			except BaseException as e:  # division by zero
				date_err = (k, str(e))
				logging.error("@fcd/@k: %s, error: %s" % date_err)
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
					logging.warning("speed/time/data current: %s, error calc!" % k)
				except BaseException as e:
					speed_file = time_file = data_file = 0
					std_err = (k, str(e))
					logging.error("speed/time/data current: %s, error: %s" % std_err)
				else:
					# {'@speed[mb/s]': 0, '@time[s]': 0, '@data[mb]': 0, '@file': 'test.tst'} # @scprle.log
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
					logging.error("@new_time current: %s, error: %s" % new_time_err)
				else:
					try:
						assert bool(new_time in ms_set), ""
					except AssertionError:
						if not new_time in ms_set:  # unique_ms_only(any_count_files)
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
							% (new_time, cnt, a, skip_or_run_str, add.full_to_short(k))
						)
						logging.info(
							"Осталось %d ms до окончания обработки, всего: %d, задач: %d, debug: %s, current: %s"
							% (new_time, cnt, a, skip_or_run_str, add.full_to_short(k))
						)

			"""
			s = "c:\\downloads\\mytemp\\downloads.txt"

			>>> "\\".join(s.split("\\")[::-1]) # 'downloads.txt\\mytemp\\downloads\\c:  # reverse_path
			>>> s.split("\\")[-1::] # ['downloads.txt'] # only_short_name
			>>> "\\".join(s.split("\\")[:-1:]) # 'c:\\downloads\\mytemp'	# only_folder			
			"""

			# if os.path.exists(k.replace(k.split(".")[-1], "cmd")):  # clear_old_cmd
			# os.remove(k.replace(k.split(".")[-1], "cmd"))

			with open(
				k.replace(k.split(".")[-1], "cmd"), "w", encoding="utf-8"
			) as mcf:  # save_new_cmd(is_one_line)
				mcf.writelines("%s\n" % v)  # multicommander(str)
				# mcf.writelines("%s\\\n" % v) # totalcommander(str)

			try:
				fsize1 = os.path.getsize(k.replace(k.split(".")[-1], "cmd"))
			except BaseException:
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
			except BaseException:
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

			try:
				sleep(60 - time() + strt)  # pause_for_debug
			except BaseException:
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
				te_str = (str(e2), k)
				logging.error("@te_str error: %s, filename: %s" % te_str)
			else:
				prstime = (t.remains(cur_iter), k)

				print(
					"@prstime left: %s(s), current: %s" % prstime
				)  # t.remains(cur_iter)
				logging.info("@prstime left: %s(s), current: %s" % prstime)
		else:
			logging.info(
				"@fcd time_end: %s, current: %s" % (str(datetime.now()), last_file)
			)

		with open(fcd_base, "w", encoding="utf-8") as fjf:
			json.dump(fcd, fjf, ensure_ascii=False, indent=4, sort_keys=True)
	# """

	fcd_list = []

	try:
		new_list = list(
			set(
				[
					"".join(
						[
							crop_filename_regex.sub(
								"", fv.split(" ")[-1].split("\\")[-1]
							),
							"_Rus",
						]
					)
					if "Rus" in fv
					else crop_filename_regex.sub("", fv.split(" ")[-1].split("\\")[-1])
					for fv in filter(lambda x: "ffmpeg" in x, tuple(fcd.values()))
				]
			)
		)  # only_ffmpeg(not_optimized)
	except:
		new_list = []
	else:
		logging.info("@new_list count: %d" % len(new_list))  # debug(print)

	try:
		ready_list = list(
			set(
				[
					"".join(
						[
							crop_filename_regex.sub(
								"", fv.split(" ")[-1].split("\\")[-1]
							),
							"_Rus",
						]
					)
					if "Rus" in fv
					else crop_filename_regex.sub("", fv.split(" ")[-1].split("\\")[-1])
					for fv in filter(lambda x: "ffplay" in x, tuple(fcd.values()))
				]
			)
		)  # only_ffplay(optimized)
	except:
		ready_list = []
	else:
		logging.info("@ready_list count: %d" % len(ready_list))  # debug(print)

	# some_jobs(new/ready)
	# fcd_list = ready_list if ready_list else new_list # have_ready_or_new_by_filter
	# fcd_list = ready_list if len(ready_list) > len(new_list) else new_list # compare_length_by_filter

	try:
		# fcd_list = list(set(ready_list) ^ set(new_list)) if len(list(set(ready_list) ^ set(new_list))) > len(list(set(ready_list) & set(new_list))) else list(set(ready_list) & set(new_list)) # combine # debug
		fcd_list = (
			list(set(ready_list)) if ready_list else list(set(new_list))
		)  # ready_job/new_job
		assert fcd_list, ""
	except AssertionError:  # if_null
		logging.warning("@fcd_list null")
	except BaseException as e:  # if_error
		fcd_list = []
		logging.error("@fcd_list %s" % str(e))
	else:
		logging.info(
			"@fcd_list %s [%d] [%s]"
			% (";".join(fcd_list), len(fcd_list), str(datetime.now()))
		)

	# seg_filter = list(set(seg2) ^ set(seg1)) # different(two_list) # [1, 3, 4, 6] # type1
	# seg_filter = list(set(seg2) & set(seg1)) # unique(two_list) # [2] # type2
	# seg_filter = list(set(seg1) - set(seg2)) # stay_different(only_first/clear_unique/one_list) # [1, 3] # type3

	# logging.info("string1: %s, string2: %s" % (";".join(ready_list), ";".join(new_list)))

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
					]
				),
			)
		)

	sizes_dict: dict = {}

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
		# script_path = os.path.dirname(os.path.realpath(__file__)).lower()
		filename = "\\".join(
			[script_path, __file__.replace(ext, ".glob")]
		)  # c:\downloads\soft\replace_file.glob
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
