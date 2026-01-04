# Hash Cracker (Learning Project)

## Description
A dictionary-based hash cracking tool built to understand how
common hashing algorithms work internally.

## Supported Hash Algorithms
- MD5
- SHA1
- SHA256
- SHA512

## Usage
python3 crack_the_hash.py -H <hash> -W <wordlist>

## Example
python3 crack_the_hash.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -W rockyou.txt

## Limitations
- Dictionary-based only
- No salting support
- Limited hash algorithm support (more planned)


