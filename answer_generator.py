import sys
import os
import shutil
import random
import hashlib
from contextlib import contextmanager

try:
	import pyperclip
except NameError:
	pass


@contextmanager
def clip(text):
	try:
		old_text = pyperclip.paste()
		pyperclip.copy(text)
		print("Copied to clipboard. ", end = "")
		try:
			yield			
		finally:
			if text == pyperclip.paste():
				pyperclip.copy(old_text)
	except NameError:
		yield


def configure():
	min_len = 3
	max_len = 12

	print("The seed is generated from a password. Be sure to:")
	print()
	print("  * Use a hard-to-guess password.")
	print("  * Remember it in case you ever need to reinstall.")
	print()

	# create seed
	passwd = input("Password: ")
	print()
	bytes  = hashlib.sha512(passwd.encode()).digest()[-8:]
	seed   = int.from_bytes(bytes, "big")
	with open("seed", "w") as f:
		f.write(str(seed))

	lines = []
	for word_file in os.listdir("word_lists"):
		with open(os.path.join("word_lists", word_file)) as f:
			lines += f.readlines()
	lines = [w.strip()+"\n" for w in lines]
	lines = [w for w in set(lines) if len(w) >= min_len+1 and len(w) <= max_len+1]
		
	# shuffle words so each word has a new index
	# The seeding method is guaranteed to be stable.
	random.seed(seed, 2) 
	random.shuffle(lines)
	with open("words", "a") as f:
		lines = f.writelines(lines)
	
	print("Setup complete.")
	print()

def get_answer(question):	
	with open("seed", "r") as f:
		seed = f.readline().strip()

	# get list of words
	with open("words") as f:
		words = f.readlines()
	words = [w.strip() for w in words]

	# create answer to security question
	question = question.strip().lower() + seed
	index = int.from_bytes(hashlib.sha512(question.encode()).digest(), "big") % len(words)
	width = len(str(len(words)))
	ans   = words[index] + str(index).zfill(width)
	
	return ans

def main():
	if not os.path.isfile("seed"):
		configure()
	
	# get security question
	question = sys.argv[1:]
	if len(question) == 0:
		question = input("Security Question: ")
		print()
	else:
		question = " ".join(question)

	# display answer
	ans = get_answer(question)
	print(f"             >>>   {ans}   <<<")
	print()
	with clip(ans):
		input("Press Enter to quit.")

main()