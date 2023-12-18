# Advent of code 2023
# Run Script
# Adopted from https://github.com/oliver-ni/advent-of-code.git
# Modified for my naming conventions and to accept example text from the script itself
# Efforts by aocd to parse examples from the problem statement are hit or miss
# This script runs sample text from a string called `example` in the module
# ie. example = ''' example lines '''.strip() # strip to remove leading and tailing newlines
# Requires aocd with token configured to automaticall fetch input
# Also added submit functionality using aocd

import argparse
import os.path
import time
import traceback
from datetime import datetime, timedelta, timezone
from importlib import import_module, reload
from io import StringIO

ans = {}

def run(func, input, example = False):
    try:
        if example:
            # f = StringIO(input)
            f = input
        else:
            f = open(input)
        with f:
            try:
                start = time.monotonic_ns()
                result = func(f)
                end = time.monotonic_ns()
                print(result, end="\t")
                print(f"[{(end-start) / 10**6:.3f} ms]")
                return result
            except:
                traceback.print_exc()
    except FileNotFoundError:
        print()

def submit():
    try:
        from aocd import submit
    except ImportError:
        print("No aocd module")
    else:
        for i in ("p1", "p2"):
            if i in ans:
                submit(ans[i], part=i[-1], day=args.day, year=args.year)

if __name__ == "__main__":
    now = datetime.now(timezone(timedelta(hours=-5)))
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--extra", "-e", help="Choose a different solution to run.")
    parser.add_argument("--submit", "-s", action="store_true", help="Submit the solutions with Aocd", default=False)
    args = parser.parse_args()

    input_paths = {
        "sample": f"input/{args.year}/day{args.day:02}_sample.txt",
        "input": f"input/{args.year}/day{args.day:02}.txt",
    }

    if not os.path.exists(input_paths["input"]):
        try:
            from aocd import AocdError, get_data
        except ImportError:
            pass
        else:
            try:
                data = get_data(day=args.day, year=args.year)
            except AocdError as e:
                print(e)
            else:
                with open(input_paths["input"], "w") as f:
                    f.write(data)

    module_name = f"{args.year}.{args.day:02}"
    if args.extra:
        module_name += f"_{args.extra}"

    print(f"{module_name}")

    module = import_module(module_name)

    for i in ("p1", "p2"):
        if not hasattr(module, i):
            continue
        print(f"--- {i} ---")
        print("sample:", end="\t")
        if hasattr(module, 'example'):
            run(getattr(module, i), module.example, example = True)
        else:
            run(getattr(module, i), f"input/{args.year}/day{args.day:02}_sample.txt")
        reload(module)
        print("input:", end="\t")
        ans[i] = run(getattr(module, i), f"input/{args.year}/day{args.day:02}.txt")

    if args.submit:
        submit()
