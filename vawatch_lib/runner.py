import time
import subprocess

def run(args):
    cmd = " ".join(args.command)
    while True:
        start = time.time()
        try:
            out = subprocess.check_output(
                cmd, shell=True, stderr=subprocess.STDOUT, timeout=args.timeout
            )
            print(out.decode(errors="ignore"))
        except Exception as e:
            print(e)

        elapsed = time.time() - start
        time.sleep(max(0, args.interval - elapsed))
