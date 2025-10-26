
# ShadowScript - Transforms shell scripts into silent, hassle-free processes
# Copyright (c) 7wp81x 2025
#
# DISCLAIMER: This tool is for ethical, lawful use only (e.g., workflow automation, education).
# It is not intended for malicious purposes like malware creation or evading security.
# Users are responsible for complying with all applicable laws and GitHub policies.

import base64
import argparse
import os

banner = """
  \033[2;92m⢎⡑ ⣇⡀ ⢀⣀ ⢀⣸ ⢀⡀ ⡀ ⢀ \033[2;97m⢎⡑ ⢀⣀ ⡀⣀ ⠄ ⣀⡀ ⣰⡀
  \033[2;92m⠢⠜ ⠇⠸ ⠣⠼ ⠣⠼ ⠣⠜ ⠱⠱⠃ \033[2;97m⠢⠜ ⠣⠤ ⠏  ⠇ ⡧⠜ ⠘⠤ \033[0;93mv1.0\033[0m
 
 \033[1;93m::\033[1;97m Github    : \033[4;32mgithub.com/7wp81x/ShadowScript\033[0m
 \033[1;93m::\033[1;97m Coded by  : \033[0;32m7wp81x\033[0m
"""

ERROR = lambda msg: print(f"\033[0m[\033[1;31m!\033[0m] {msg}\033[0m")
SUCCESS = lambda msg: print(f"\033[0m[\033[1;32m+\033[0m] {msg}\033[0m")
INFO = lambda msg: print(f"\033[0m[\033[1;36m*\033[0m] {msg}\033[0m")


parser = argparse.ArgumentParser(description='A python script that turns your simple shell script into a stealthy process with no interruptions.')
parser.add_argument('-f', '--file', required=True, help='shell script that you want to encode')
parser.add_argument('-o', '--output', required=True, help='output file')
parser.add_argument("--shebang",action="store_true",required=False, default=False,help="Add '#!/bin/sh' at first line (default: no)")

args = parser.parse_args()


if not os.path.exists(args.file):
	ERROR(f"File: {args.file}, not found.")

def main():
	shell_content = ""
	shell_output = ""

	print(banner)

	INFO("Encoding shell script...")
	with open(args.file, "r") as fp:
		shell_content = fp.read()

	base64_payload = base64.b64encode(shell_content.encode()).decode("utf-8")
	if args.shebang:
		shell_output = "#!/bin/sh\n"

	shell_output += '( nohup bash -c "$(echo \''+base64_payload+'\' | base64 -d)" >/dev/null 2>&1 < /dev/null & )'
	with open(args.output, "w+") as output:
		output.write(shell_output)
	SUCCESS("Script has been encoded.")
	INFO(f"Output: \033[4;32m{args.output}\n")


if __name__ == '__main__':
	main()