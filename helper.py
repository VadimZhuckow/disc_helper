import subprocess

def disk_usage():
    result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    for line in output.splitlines():
        if line.startswith('/dev/'):
            parts = line.split()
            print(f"{parts[0]} использовано {parts[2]} из {parts[1]} ({parts[4]} свободно)")

disk_usage()
