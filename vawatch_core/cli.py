import argparse
from vawatch_core.runner import run
from vawatch_core.telegram import send

def main():
    p = argparse.ArgumentParser(prog="vawatch")
    p.add_argument("-n", "--interval", type=int, default=60)
    p.add_argument("--timeout", type=int, default=30)
    p.add_argument("--no-overlap", action="store_true")
    p.add_argument("--send", help="send a test message to Telegram and exit")
    p.add_argument("command", nargs=argparse.REMAINDER)
    args = p.parse_args()

    # test telegram message
    if args.send:
        send(args.send, timeout=args.timeout)
        print("sent")
        return

    if not args.command:
        p.error("no command specified")

    run(args)
