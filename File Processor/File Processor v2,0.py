'''
  * FILE PROCESSOR
	by Onko Aikuu (@furry_onko)
	version 2.0
'''

import random
import re
import charset_normalizer as cn
import os

def help():
	print("==============HELP==============")
	print("WHEN FILE IS SELECTED")
	print("  - seek: searching file")
	print("    - lines: returns all lines in file")
	print("    - numbers: returns all numbers in file")
	print("    - char: searching file for a character and counting occurrences of it")
	print("    - word: searching file for word and counting occurrences of it")
	print("    - strings: searching file for text")
	print("      - +: include other types")
	print("      - !: exclude ASCII characters\n")
	print("  - encoding: see or set encoding")
	print("    - ?: see encoding")
	print("    - !: set encoding to UTF-8\n")
	print("  - truncate: wipe all data from file\n")
	print("  - line: add selected amount of lines to the file\n")
	print("  - file: display file info")
	print("    - name: get file name")
	print("    - size: get file size")
	print("  - del: delete file")
	print("WHEN FILE IS NOT SELECTED")
	print("  - makefile: create file in selected direcotry\n")
	print("FOR EVERY STATE")
	print("- exit / #: exit program\n")
	print("- cl / ~ / $: clear screen\n")
	print("- help / ?: see help screen\n")
	print("- open: open file\n")

def delete(file):
	print(file)
	while True:
		confirm = input(f"Are you sure you want to delete \"{os.path.basename(file)}\"? (Y/N): ")
		confirm = confirm.upper()
		if confirm == "Y":
			try:
				os.remove(file)
				print("Done.")
				typePath()
				break
			except FileNotFoundError:
				print(f"File \"{file}\" does not exist")
				break
			except PermissionError:
				print(f"You do not have permission to delete \"{file}\"")
				break
			except Exception as exc:
				print(f"An unknown error occured: {exc}")

		elif confirm == "N":
			print(f"File \"{file}\" was not deleted")
			break

def enc(file, type, enc="utf-8"):
	if type == 1:
		with open(file, 'r', encoding=enc, errors='replace') as f:
			content = f.read()

		with open(file, 'w', encoding='utf-8') as f:
			f.write(content)

		with open(file, 'rb') as f:
			detected = cn.detect(f.read())
			encoding = detected['encoding']

		with open(file, 'r', encoding=encoding, errors='replace') as f:
			fileLines = f.readlines()
		
		print("Encoding changed to UTF-8")
		mainProgram(fileLines, file, encoding)

	elif type == 2:
		with open(file, 'rb') as f:
			detected = cn.detect(f.read())
			print(f"Detected encoding: {detected['encoding']}")

	else:
		print("What the fuck?")

def line(fileLines, file, encoding):
	while True:
		amount = input("Type amount of lines (or type \"###\" to exit): ")
		if amount == "###":
			print("Going back")
			break
		elif amount:
			amount = int(amount)
			with open(file, 'a', encoding='utf-8', errors='replace') as f:
				while amount > 0:
					insert = input(">> ")
					f.write(f"{insert}\n")
					amount -= 1
			with open(file, 'r', encoding=encoding, errors='replace') as f:
				fileLines[:] = f.readlines()
			print("File updated")
			break
		else:
			print("Type amount of lines")

def makefile(encoding):
	def pathtype(fname, ext, encoding):
		fullfilename = f"{fname}.{ext}"
		while True:
			directory = input("Type your file directory (example: C:/dir/ (add \"/\" at the end)): ")
			if directory:
				fullsave = f"{directory}{fullfilename}"
				with open(fullsave, 'w', encoding=encoding, errors='replace') as savefile:
					print("File created")
				break
			else:
				print("Type a file directory.")

	while True:
		filename = input("Type file name: ")
		if filename:
			while True:
				ext = input("Type file extension (default: txt): ")
				if ext:
					pathtype(filename, ext, encoding)
					break
				else:
					pathtype(filename, 'txt', encoding)
					break
			break
		else:
			print("Error. Type a file name")

def truncate(file, encoding):
	while True:
		confirm = input("Are you sure? (Y/N): ")
		confirm = confirm.upper()
		if confirm == 'Y':
			with open(file, 'w', encoding=encoding, errors='replace') as truncate:
				pass
			print("Done.")
			typePath()
			break
		elif confirm == 'N':
			print("File was not truncated.")
			break
		else:
			pass

def seek(what, fileLines, file=None):
	if what == "lines":
		print("All lines:")
		for lineId, line in enumerate(fileLines, start=1):
			print(f"{lineId} | {line.strip()}")
		print()

	elif what == "strings":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.match("^[a-zA-Z]$", word):
					result.append(word)
		if result == []:
			print("File has no strings")
		else:
			print(f"Result:\n{' '.join(result)}")

	elif what == "string_other":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.findall(r"\b[^\W\d_]\b", word):
					result.append(word)

		if result == []:
			print("File has no other strings")
		else:
			print(f"Result:\n{' '.join(result)}")

	elif what == "numbers":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.match("^[0-9]$", word):
					result.append(word)
		if result == []:
			print("File has no numbers")
		else:
			print(f"Result:\n{' '.join(result)}")

	elif what == "char":
		while True:
			seekChar = input("Type character (or type \"###\" to exit): ")
			if seekChar == '###':
				print("Going back")
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
					print(f"No {seekChar} found")
					break
				else:
					print(f"\"{seekChar}\" occurs {counted} times")
					break
			else:
				print("Error. Type any character")

	elif what == "word":
		while True:
			seekWord = input("Type word (or type \"###\" to exit): ")
			if seekWord == "###":
				print("Going back")
				break
			elif seekWord:
				result = []
				for line in fileLines:
					words = re.findall(r'\b\w+\b', line.strip())
					for word in words:
						if re.match(f"^{re.escape(seekWord)}$", word):
							result.append(word)
				counted = len(result)
				if counted == 0:
					print(f"No occurences of \"{seekWord}\" found")
					break
				elif result == []:
					print(f"File has no words")
					break
				else:
					print(f"\"{seekWord}\" occurs {counted} times")
					break
			else:
				print("Error. Type any word")
	elif what == "weird_strings":
		result = []
		for line in fileLines:
			words = line.strip()
			for word in line:
				if re.match(r"[^\x20-\x7E]", word):
					result.append(word)
		if result == []:
			print("File has no non ASCII characters")
		else:
			print(f"Result:\n{' '.join(result)}")
	else:
		print("What the fuck?")

def mainProgram(fileLines=None, file=None, encoding='utf-8', banEdit=False):
	while True:
		command = input("> ")
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
				enc(file, 1, encoding)

			elif command == "encoding" or command == "encoding ?":
				enc(file, 2)

			elif command == "truncate":
				truncate(file, encoding)

			elif command == "del":
				delete(file)

			elif command == "cl" or command == "~" or command == "$":
				os.system("cls")

			elif command == "exit" or command == "#":
				bye = ['Bye!', 'Have a nice day', 'See you next time', 'See ya!']
				print(random.choice(bye))
				exit()

			elif command == "line":
				line(fileLines, file, encoding)

			elif command == "file size":
				size = os.path.getsize(file)
				print(f"Size: {size} bytes")

			elif command == "file name":
				filename = os.path.basename(file)
				fname, ext = os.path.splitext(filename)
				print(f"File name: {fname}\nExtension: {ext}")

			elif command == "file":
				size = os.path.getsize(file)
				filename = os.path.basename(file)
				fname, ext = os.path.splitext(filename)
				print(f"File name: {fname}\nExtension: {ext}\nSize: {size} bytes")

			elif command == "help" or command == "?":
				help()

			elif not command.strip():
				print("Error. No command")

			else:
				print("Error. Wrong command")

		elif banEdit == True:
			if command == "makefile":
				makefile('utf-8')

			elif command == "cl" or command == "~" or command == "$":
				os.system("cls")

			elif command == "exit" or command == "#":
				bye = ['Bye!', 'Have a nice day', 'See you next time', 'See ya!']
				print(random.choice(bye))
				exit()

			elif command == "open":
				typePath()

			elif command == "help" or command == "?":
				help()

			elif not command.strip():
				print("Error. No command")

			else:
				print("Error. Wrong command")

		else:
			print("Error. You are at the point, where you are in no state. This means, that you will not be able to execute any command. Please restart our program")
			os.system("Pause")
			exit()

def prepareFile(file):
	while True:
		try:
			with open(file, 'rb') as f:
				detected = cn.detect(f.read())
				encoding = detected['encoding']
				print(f"File encoding: {encoding}")

			with open(file, 'r', encoding=encoding, errors='replace') as f:
				fileLines = f.readlines()
				countedLines = len(fileLines)
				size = os.path.getsize(file)
				print(f"Processing lines completed ({countedLines} lines).")
				print(f"Size: {size} bytes")
			mainProgram(fileLines, file, encoding)
			break

		except FileNotFoundError:
			print(f"Error. File in path \"{file}\" does not exist.")
			break

		except Exception as exc:
			print(f"An error occurred: {exc}")
			break


def processPath(path):
	path = path.replace('"', '')
	print("Processing path completed.")
	prepareFile(path)

def typePath():
	while True:
		path = input("Paste path here (or type ### to skip): ")
		if path == "###":
			print("No file entered. Modifying files will be impossible,")
			mainProgram(banEdit=True)
		elif path == "exit":
			print("Bye!")
			exit()
		elif path:
			print("Incorrect path name")
			typePath()
			break
		else:
			if path.strip():
				processPath(path)
				break
			else:
				print("Error. No path typed.")
				typePath()
				break

print("File Processor v2.0\nBy Onko Aikuu (@furry_onko)")
typePath() #hehe 420 7w7
