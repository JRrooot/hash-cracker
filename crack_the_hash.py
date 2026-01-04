from pwn import *
import re
import sys
import argparse


parser = argparse.ArgumentParser(description="Dictionary-based hash cracking tool")
parser.add_argument("-H",dest="hash_value",help="Target Hash to crack", required=True)
parser.add_argument("-W",dest="wordlist",help="Path to wordlist file",required=True)
args = parser.parse_args()

target_hash = args.hash_value.lower()


hash_Functions = {"md5": md5sumhex,"sha1": sha1sumhex,"sha256": sha256sumhex,"sha512": sha512sumhex}

def detect(target_hash):
	t_hash = target_hash.strip().lower()
	if not re.fullmatch(r"[0-9a-f]+", t_hash):
		return "Invalid"
		
	return {32:"md5", 128:"sha512", 64:"sha256", 40:"sha1"}.get(len(t_hash), "Unsupported")
	
hash_type = detect(target_hash)
if hash_type in ("Invalid", "Unsupported"):
	print(f" Hash Error: {target_hash}:Unsupported Format")
	sys.exit()
	
print(f" Hash Detected : {hash_type}")

def crack(target_hash):
	hash_func = hash_Functions[hash_type]
	attempts = 0

	try:
		with log.progress(f" Attempting to crack the hash: {target_hash}") as p:
			with open(args.wordlist, "r", encoding='latin-1') as password_list:
				for password in password_list:
					password = password.strip()
					attempts += 1

					password_hash = hash_func(password.encode())
					p.status(f"\ncracking >>>> {password}:{password_hash}")

					if target_hash == password_hash:
						p.success(f"\nPassword found after {attempts} attempts : {password}")
						sys.exit()

				p.failure(f"Password not found, Try using a different Wordlist")
	except KeyboardInterrupt:
		log.failure("Interrupted by user")
		sys.exit()
		
crack(target_hash)			