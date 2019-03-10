import subprocess

subprocess.run("python curlAll.py")
subprocess.run("ls results/curl > results_curl.txt")

print("""
###########################\n
#### Download Complete ####\n
###########################\n
""", flush=True)

subprocess.run("python boiler.py")

print("""
###########################\n
### Extraction Complete ###\n
###########################\n
""", flush=True)


print("\n\n\n", flush=True)
print("""
###########################\n
### Operations Complete ###\n
###########################\n
""", flush=True)
