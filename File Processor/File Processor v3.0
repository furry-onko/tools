'''
  * FILE PROCESSOR
	by Onko Aikuu (@furry_onko)
	version 2.1
'''

import random
import re
import charset_normalizer as cn
import os
from colorama import Fore, Back, Style, init

UNDERLINED = '\033[4m'

init()

def help():
    print(Fore.RED + Style.BRIGHT + "==============HELP==============" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + "WHEN FILE IS SELECTED" + Style.RESET_ALL)
    print(Fore.YELLOW + "  - seek:" + Style.RESET_ALL + " searching file")
    print(Fore.CYAN + Style.BRIGHT + "    - lines:" + Style.RESET_ALL + " returns all lines in file")
    print(Fore.CYAN + Style.BRIGHT + "    - numbers:" + Style.RESET_ALL + " returns all numbers in file")
    print(Fore.CYAN + Style.BRIGHT + "    - char:" + Style.RESET_ALL + " searching file for a character and counting occurrences of it")
    print(Fore.CYAN + Style.BRIGHT + "    - word:" + Style.RESET_ALL + " searching file for word and counting occurrences of it")
    print(Fore.CYAN + Style.BRIGHT + "    - strings:" + Style.RESET_ALL + " searching file for text")
    print(Fore.GREEN + Style.BRIGHT + "      - +:" + Style.RESET_ALL +" include other types")
    print(Fore.GREEN + Style.BRIGHT + "      - !:" + Style.RESET_ALL +" exclude ASCII characters\n")
    print(Fore.YELLOW + "  - encoding:" + Style.RESET_ALL + " see or set encoding")
    print(Fore.GREEN + Style.BRIGHT + "    - ?: " + Style.RESET_ALL + "see encoding")
    print(Fore.GREEN + Style.BRIGHT + "    - !: " + Style.RESET_ALL + "set encoding to UTF-8\n")
    print(Fore.YELLOW + "  - truncate:" + Style.RESET_ALL + " wipe all data from file\n")
    print(Fore.YELLOW + "  - line:" + Style.RESET_ALL + " add selected amount of lines to the file\n")
    print(Fore.YELLOW + "  - file:" + Style.RESET_ALL + " display file info")
    print(Fore.GREEN + Style.BRIGHT + "    - name: " + Style.RESET_ALL + " get file name")
    print(Fore.GREEN + Style.BRIGHT + "    - size: " + Style.RESET_ALL + " get file size")
    print(Fore.YELLOW + "  - del:" + Style.RESET_ALL + " delete file")
    print(Fore.YELLOW + "  - rename:" + Style.RESET_ALL + " rename file")
    print(Fore.MAGENTA + Style.BRIGHT + "WHEN FILE IS NOT SELECTED" + Style.RESET_ALL)
    print(Fore.YELLOW + "  - makefile:" + Style.RESET_ALL + " create file in selected directory\n")
    print(Fore.MAGENTA + Style.BRIGHT + "FOR EVERY STATE" + Style.RESET_ALL)
    print(Fore.YELLOW + "  - exit / #:" + Style.RESET_ALL + " exit program")
    print(Fore.YELLOW + "  - cl / ~ / $:" + Style.RESET_ALL + " clear screen")
    print(Fore.YELLOW + "  - help / ?:" + Style.RESET_ALL + " see help screen")
    print(Fore.YELLOW + "  - open:" + Style.RESET_ALL + " open file")
    print(Fore.RED + Style.BRIGHT + "================================" + Style.RESET_ALL)

def delete(file):
	def conf():
		confirm = input(Fore.RED + Style.BRIGHT + f"Are you sure you want to delete \"{os.path.basename(file)}\"? (Y/N): " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT)
		return confirm
	while True:
		confirm = conf()
		confirm = confirm.upper()
		if confirm == "Y":
			try:
				os.remove(file)
				print(Fore.GREEN + Style.BRIGHT + "Done." + Style.RESET_ALL)
				typePath()
				break
			except FileNotFoundError:
				print(Back.RED + 'File ' + Style.RESET_ALL + Fore.RED + Style.BRIGHT + file + Style.RESET_ALL + Back.RED + ' does not exist' + Style.RESET_ALL)
				break
			except PermissionError:
				print(Back.RED + 'You do not have permission to delete ' + Style.RESET_ALL + Fore.RED + Style.BRIGHT + file + Style.RESET_ALL)
				break
			except Exception as exc:
				print(Back.RED + "An unknown error occured: " + Style.RESET_ALL + Fore.red + exc + Style.RESET_ALL)

		elif confirm == "N":
			print(Fore.GREEN + Style.BRIGHT + "File " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + file + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " was not deleted" + Style.RESET_ALL)
			break

def rename(file, ext, path):
	current = os.path.join(path, os.path.basename(file))
	def ren():
		new = input(Fore.CYAN + "Type new name (or type \"###\" to exit): " + Style.RESET_ALL + Fore.YELLOW)
		return new
	while True:
		new = ren()
		if new == os.path.basename(current):
			print(Fore.GREEN + Style.BRIGHT + "File name will not change" + Style.RESET_ALL)
			break
		elif not new:
			print(Back.RED + "Error. Type a new name" + Style.RESET_ALL)
		else:
			try:
				new = os.path.join(path, f"{new}{ext}")
				os.rename(current, new)
				current = new
				with open(new, 'r', encoding='utf-8', errors='replace') as f:
					pass
				print(Fore.GREEN + Style.BRIGHT + "Done." + Style.RESET_ALL)
				quietPrepare(new)
				break
			except FileNotFoundError:
				print(Back.RED + "Error. File does not exist" + Style.RESET_ALL)
				break
			except PermissionError:
				print(Back.RED + "Error. You do not have permission to rename this file" + Style.RESET_ALL)
				break
			except Exception as exc:
				print(Back.RED + "An unknown error occured: " + Style.RESET_ALL + Fore.RED + exc + Style.RESET_ALL)
				break

def enc(file, type):
	if type == 1:
		with open(file, 'r', encoding='utf-8', errors='replace') as f:
			content = f.read()

		with open(file, 'w', encoding='utf-8') as f:
			f.write(content)

		with open(file, 'rb') as f:
			detected = cn.detect(f.read())
			encoding = detected['encoding']

		with open(file, 'r', encoding='utf-8', errors='replace') as f:
			fileLines = f.readlines()

		if encoding == 'utf-8':
			print(Fore.YELLOW + 'File encoding is already UTF-8' + Style.RESET_ALL)
		else:
			print(Fore.YELLOW + "Encoding will change to UTF-8 after adding UTF-8 characters." + Style.RESET_ALL)
			mainProgram(fileLines, file, encoding)

	elif type == 2:
		with open(file, 'rb') as f:
			detected = cn.detect(f.read())
			print(Fore.YELLOW + f"Detected encoding: {detected['encoding']}" + Style.RESET_ALL)

	else:
		print(Back.RED + "What the fuck?" + Style.RESET_ALL)

def line(fileLines, file):
	def amn():
		amount = input(Fore.CYAN + Style.BRIGHT + "Type amount of lines (or type \"###\" to exit): " + Style.RESET_ALL)
		return amount
	while True:
		amount = amn()
		if amount == "###":
			print(Fore.YELLOW + "Going back" + Style.RESET_ALL)
			break
		elif amount:
			amount = int(amount)
			with open(file, 'a', encoding='utf-8', errors='replace') as f:
				while amount > 0:
					insert = input(Fore.CYAN + Style.BRIGHT + ">> " + Style.RESET_ALL)
					f.write(f"{insert}\n")
					amount -= 1
			with open(file, 'r', encoding='utf-8', errors='replace') as f:
				fileLines[:] = f.readlines()
			print(Fore.GREEN + Style.BRIGHT + "File updated" + Style.RESET_ALL)
			break
		else:
			print(Fore.RED + Style.BRIGHT + "Type amount of lines" + Style.RESET_ALL)

def makefile(encoding):
	def pathtype(fname, ext, encoding):
		fullfilename = f"{fname}.{ext}"
		while True:
			directory = input(Fore.CYAN + Style.BRIGHT + "Type your file directory (example: C:/dir/ (add \"/\" at the end)): " + Style.RESET_ALL)
			if directory:
				fullsave = f"{directory}{fullfilename}"
				with open(fullsave, 'w', encoding=encoding, errors='replace') as savefile:
					print(Fore.GREEN + Style.BRIGHT + "File created" + Style.RESET_ALL)
				break
			else:
				print(Back.RED + "Type a file directory." + Style.RESET_ALL)

	while True:
		filename = input(Fore.CYAN + Style.BRIGHT + "Type file name: " + Style.RESET_ALL)
		if filename:
			while True:
				ext = input(Fore.CYAN + Style.BRIGHT + "Type file extension (default: txt): " + Style.RESET_ALL)
				if ext:
					pathtype(filename, ext, encoding)
					break
				else:
					pathtype(filename, 'txt', encoding)
					break
			break
		else:
			print(Back.RED + "Error. Type a file name" + Style.RESET_ALL)

def truncate(file, encoding):
	while True:
		confirm = input(Fore.RED + "Are you sure? (Y/N): " + Style.RESET_ALL)
		confirm = confirm.upper()
		if confirm == 'Y':
			with open(file, 'w', encoding=encoding, errors='replace') as truncate:
				pass
			print(Fore.GREEN + Style.BRIGHT + "Done." + Style.RESET_ALL)
			typePath()
			break
		elif confirm == 'N':
			print(Fore.GREEN + Style.BRIGHT + "File was not truncated." + Style.RESET_ALL)
			break
		else:
			pass

def seek(what, fileLines, file=None):
	if what == "lines":
		print(Fore.MAGENTA + Style.BRIGHT + "All lines:" + Style.RESET_ALL)
		for lineId, line in enumerate(fileLines, start=1):
			print(Fore.CYAN + str(lineId) + Style.RESET_ALL + ' | ' + Fore.YELLOW + Style.BRIGHT + line.strip() + Style.RESET_ALL)

	elif what == "strings":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.match("^[a-zA-Z]$", word):
					result.append(word)
		if result == []:
			print(Fore.YELLOW + "File has no strings" + Style.RESET_ALL)
		else:
			print(Fore.MAGENTA + Style.BRIGHT + "Result:" + Style.RESET_ALL)
			print(Fore.YELLOW + Style.BRIGHT + f"{' '.join(result)}" + Style.RESET_ALL)

	elif what == "string_other":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.findall(r"\b[^\W\d_]\b", word):
					result.append(word)

		if result == []:
			print(Fore.YELLOW + "File has no other strings" + Style.RESET_ALL)
		else:
			print(Fore.MAGENTA + Style.BRIGHT + "Result:" + Style.RESET_ALL)
			print(Fore.YELLOW + Style.BRIGHT + f"{' '.join(result)}" + Style.RESET_ALL)

	elif what == "numbers":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.match("^[0-9]$", word):
					result.append(word)
		if result == []:
			print(Fore.YELLOW + "File has no numbers" + Style.RESET_ALL)
		else:
			print(Fore.MAGENTA + Style.BRIGHT + "Result:" + Style.RESET_ALL)
			print(Fore.YELLOW + Style.BRIGHT + f"{' '.join(result)}" + Style.RESET_ALL)

	elif what == "char":
		while True:
			seekChar = input(Fore.CYAN + Style.BRIGHT + "Type character (or type \"###\" to exit): " + Style.RESET_ALL)
			if seekChar == '###':
				print(Fore.YELLOW + "Going back" + Style.RESET_ALL)
				break
			elif seekChar:
				seekChar = seekChar.split()
				seekChar = seekChar[0]
				result = []
				for line in fileLines:
					words = line.strip()
					for word in line:
						if re.match(re.escape(seekChar), word):
							result.append(word)
				counted = len(result)
				if counted == 0:
					print(Back.RED + "No " + Style.RESET_ALL + Fore.RED + ' ' + seekChar + ' ' + Style.RESET_ALL + Back.RED + "found" + Style.RESET_ALL)
					break
				else:
					print(Fore.GREEN + Style.BRIGHT	+ "Character: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + seekChar + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ' occurs ' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + str(counted) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ' times' )
					break
			else:
				print(Back.RED + "Error. Type any character" + Style.RESET_ALL)

	elif what == "word":
		while True:
			seekWord = input(Fore.CYAN + Style.BRIGHT + "Type word (or type \"###\" to exit): " + Style.RESET_ALL)
			if seekWord == "###":
				print(Fore.YELLOW + "Going back" + Style.RESET_ALL)
				break
			elif seekWord:
				result = []
				for line in fileLines:
					words = re.findall(r'\w+', line.strip())
					for word in words:
						if re.match(f"^{re.escape(seekWord)}$", word):
							result.append(word)
				counted = len(result)
				if counted == 0:
					print(Back.RED + "No occurences of" + Style.RESET_ALL + Fore.RED +  f" {seekWord} " + Style.RESET_ALL + Back.RED + "found" + Style.RESET_ALL)
					break
				elif result == []:
					print(Back.RED + "File has no words" + Style.RESET_ALL)
					break
				else:
					print(Fore.GREEN + Style.BRIGHT	+ "Word: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + seekWord + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ' occurs ' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + str(counted) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ' times' )
					break
			else:
				print(Back.RED + "Error. Type any word" + Style.RESET_ALL)
	elif what == "weird_strings":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.match(r"[^\x20-\x7E]", word):
					result.append(word)
		if result == []:
			print(Back.RED + "File has no non ASCII characters" + Style.RESET_ALL)
		else:
			print(Fore.MAGENTA + Style.BRIGHT + "Result:" + Style.RESET_ALL)
			print(Fore.YELLOW + Style.BRIGHT + f"{' '.join(result)}" + Style.RESET_ALL)
	else:
		print(Back.RED + "What the fuck?" + Style.RESET_ALL)

def mainProgram(fileLines=None, file=None, encoding='utf-8', banEdit=False):
	def inp():
		command = input(Fore.CYAN + Style.BRIGHT + "> " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT)
		return command
	while True:
		command = inp()
		if banEdit == False:
			if command == "seek lines":
				seek('lines', fileLines)

			elif command == "seek strings":
				seek('strings', fileLines)

			elif command == "seek strings +":
				seek('string_other', fileLines)

			elif command == "seek strings !":
				seek('weird_strings', fileLines, file)

			elif command == "seek numbers":
				seek('numbers', fileLines)

			elif command == "seek char":
				seek("char", fileLines)

			elif command == "seek word":
				seek("word", fileLines)

			elif command == "open":
				typePath()

			elif command == "encoding !":
				enc(file, 1)

			elif command == "encoding" or command == "encoding ?":
				enc(file, 2)

			elif command == "truncate":
				truncate(file, encoding)

			elif command == "del":
				delete(file)

			elif command == "rename":
				filename = os.path.basename(file)
				fname, ext = os.path.splitext(filename)
				pathto = os.path.dirname(os.path.abspath(file))
				rename(file, ext, pathto)

			elif command == "cl" or command == "~" or command == "$":
				os.system("cls")

			elif command == "exit" or command == "#":
				bye = ['Bye!', 'Have a nice day', 'See you next time', 'See ya!']
				print(Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + random.choice(bye) + Style.RESET_ALL)
				exit()

			elif command == "line":
				line(fileLines, file)

			elif command == "file size":
				size = os.path.getsize(file)
				print(Fore.GREEN + Style.BRIGHT + 'Size: ' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + str(size) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ' bytes' + Style.RESET_ALL)

			elif command == "file name":
				filename = os.path.basename(file)
				print(Fore.GREEN + Style.BRIGHT + 'Full file name: ' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + filename + Style.RESET_ALL)

			elif command == "file":
				size = os.path.getsize(file)
				filename = os.path.basename(file)
				fname, ext = os.path.splitext(filename)
				print(Fore.GREEN + Style.BRIGHT + 'File name: ' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + fname + Style.RESET_ALL)
				print(Fore.GREEN + Style.BRIGHT + 'Extenstion: ' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + ext + Style.RESET_ALL)
				print(Fore.GREEN + Style.BRIGHT + 'Size: ' + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + str(size) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ' bytes' + Style.RESET_ALL)

			elif command == "help" or command == "?":
				help()

			elif not command.strip():
				print(Back.RED + "Error. No command" + Style.RESET_ALL)

			else:
				print(Back.RED + "Error. Wrong command" + Style.RESET_ALL)

		elif banEdit == True:
			if command == "makefile":
				makefile('utf-8')

			elif command == "cl" or command == "~" or command == "$":
				os.system("cls")

			elif command == "exit" or command == "#":
				bye = ['Bye!', 'Have a nice day', 'See you next time', 'See ya!']
				print(Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + random.choice(bye) + Style.RESET_ALL)
				exit()

			elif command == "open":
				typePath()

			elif command == "help" or command == "?":
				help()

			elif not command.strip():
				print(Back.RED + "Error. No command" + Style.RESET_ALL)

			else:
				print(Back.RED + "Error. Wrong command" + Style.RESET_ALL)
# hehe 420 7w7
		else:
			print(Back.RED + "Error. You are at the point, where you are in no state. This means, that you will not be able to execute any command. Please restart our program" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT)
			os.system("Pause")
			print(Style.RESET_ALL)
			exit()

def quietPrepare(file):
	while True:
		try:
			with open(file, 'rb') as f:
				detected = cn.detect(f.read())
				encoding = detected['encoding']

			with open(file, 'r', encoding=encoding, errors='replace') as f:
				fileLines = f.readlines()
			mainProgram(fileLines, file, encoding)
			break

		except FileNotFoundError:
			print(Back.RED + "Error. File in path" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + ' ' + UNDERLINED + file + Style.RESET_ALL + ' ' + Back.RED + "does not exist." + Style.RESET_ALL)
			break

		except Exception as exc:
			print(Back.RED + "An error occurred:" + Style.RESET_ALL + ' ' + Fore.RED + Style.BRIGHT + exc + Style.RESET_ALL)
			break 

def prepareFile(file):
	while True:
		try:
			with open(file, 'rb') as f:
				detected = cn.detect(f.read())
				encoding = detected['encoding']
				print(Fore.GREEN + Style.BRIGHT + "File encoding: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + encoding + Style.RESET_ALL)
				if encoding != 'utf-8':
					print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "File is in wrong encoding. Changing encoding immediately when characters change." + Style.RESET_ALL)

			with open(file, 'r', encoding='utf-8', errors='replace') as f:
				fileLines = f.readlines()
				countedLines = len(fileLines)
				size = os.path.getsize(file)
				print(Fore.GREEN + Style.BRIGHT + "Processing lines completed (" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + str(countedLines) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " lines.)" + Style.RESET_ALL)
				print(Fore.GREEN + Style.BRIGHT + "Size: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + str(size) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " bytes" + Style.RESET_ALL)
			mainProgram(fileLines, file, encoding)
			break

		except FileNotFoundError:
			print(Back.RED + "Error. File in path" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + ' ' + UNDERLINED + file + Style.RESET_ALL + ' ' + Back.RED + "does not exist." + Style.RESET_ALL)
			typePath()
			break

		except Exception as exc:
			print(f"An error occurred: {exc}")
			typePath()
			break

def processPath(path):
	path = path.replace('"', '')
	print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN + "Processing path completed." + Style.RESET_ALL)
	prepareFile(path)

def typePath():
	while True:
		path = input(Fore.BLUE + Style.BRIGHT + "Paste path here (or type \"###\" to skip): " + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT)
		if path == "###":
			print(Style.RESET_ALL + Back.YELLOW + Fore.BLACK + "No file entered. Modifying files will be impossible" + Style.RESET_ALL)
			mainProgram(banEdit=True)
			break
		elif path == "exit":
			print(Style.RESET_ALL + Fore.GREEN + "Bye!" + Style.RESET_ALL)
			exit()
		elif '/' and ':' in path:
			processPath(path)
			break
		else:
			print(Style.RESET_ALL + Back.RED + "Incorrect path name" + Style.RESET_ALL)
			typePath()
			break

print(Fore.BLUE + Style.BRIGHT + "File Processor 3.0\nBy Onko Aikuu (@furry_onko)" + Style.RESET_ALL)
typePath()
