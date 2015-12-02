#!/usr/bin/env python

import readline # this makes arrow keys useful in the tool
import os, sys
from os.path import expanduser
from datetime import datetime, time

def get_opt_and_arg(response):
	if len(response) > 0 and response[0] == "-":
		if len(response) == 2:
			return (response[1], None)
		if len(response) > 3 and response[2] == " ":
			return (response[1], response[3:])
		return (None, None)
	else:
		return (None, response)


def confirm(message):
	while True:
		print("")
		print(">> "+message+" <<")
		confirmation = raw_input("Are you sure? (y/n) ")
		if confirmation == "y":
			return True
		elif confirmation == "n":
			return False


def run():
	start = datetime.now()
	marks = []

	name = ""
	if len(sys.argv) == 2:
		name = sys.argv[1] + "_"

	home_dir = expanduser("~")
	save_file_name = os.path.join(home_dir, "timemark_"+name+"-".join(map(str,[start.month,start.day,start.year,start.hour,start.minute,start.second]))+".txt")
	save_file_path = os.path.join(home_dir, save_file_name)
	save_file = open(save_file_path, "w")

	while True:

		if len(marks) > 0:
			print("")
			for mark in marks:
				print(mark)

		print("")
		response = raw_input(">> ")
		opt, arg = get_opt_and_arg(response)
		
		# quit
		if opt == "q":
			print("")
			print("Saved at " + save_file_path)
			print("Closing...")
			save_file.close()
			return

		# quit and delete the file
		elif opt == "D":
			if confirm("This will quit WITHOUT SAVING"):	
				os.remove(save_file_path)
				print("Closing...")
				return

		# new
		elif opt == "n":
			start = datetime.now()
			if arg == None:
				marks.append("=============")
			else:
				marks.append("== "+arg+" ==")

		# delete last entry
		elif opt == "d":
			if marks[-1][0] != "=": # cannot delete labels
				marks = marks[:-1]

		elif opt == None and arg != None:
			now = datetime.now()
			mark_timedelta = now - start
			mark_string = str(mark_timedelta).split(".")[0] + "  " + arg
			marks.append(mark_string)

		else:
			print("")
			print("**INVALID COMMAND**")

		# save file
		save_file.truncate() # clear the file
		save_file.seek(0)
		for mark in marks:
			save_file.write(mark+"\n")





if __name__ == "__main__":
	run()