#! python3

# Advent of code
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
from termcolor import colored

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
                # Format result to take up at least 15 characters, left-aligned
                print(f"{str(result):<15}", end="")
                print(f"[{(end-start) / 10**6:.3f} ms]", end="")
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
            if i in ans and ans[i]:
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
        except ImportError as e:
            print(e)
        else:
            try:
                data = get_data(day=args.day, year=args.year)
            except AocdError as e:
                print(e)
            else:
                with open(input_paths["input"], "w") as f:
                    f.write(data)

    module_name = f"{args.year}.{args.day:02}"

    print(f"{module_name}")

    module = import_module(module_name)

    # Try to get examples from aocd puzzle
    try:
        from aocd.models import Puzzle
        puzzle = Puzzle(year=args.year, day=args.day)
        aocd_examples = puzzle.examples
    except Exception:
        aocd_examples = []

    for i in ("p1", "p2"):
        # Check for suffixed version first if extra is specified
        func_name = i
        if args.extra and hasattr(module, f"{i}_{args.extra}"):
            func_name = f"{i}_{args.extra}"
        elif not hasattr(module, i):
            continue
        print(f"--- {i} ---")
        print("sample:", end="\t")

        # Get example answer for this part
        example_answer = None
        # First check for manual answers in the module
        if hasattr(module, f'answer_{i[-1]}') and getattr(module, f'answer_{i[-1]}'):
            try:
                example_answer = str(getattr(module, f'answer_{i[-1]}'))
            except:
                pass
        # Fall back to aocd examples if no manual answer
        elif aocd_examples:
            example = aocd_examples[0]  # Take first example
            if i == "p1":
                example_answer = example.answer_a
            else:
                example_answer = example.answer_b

        # Run example
        has_valid_example = False
        if hasattr(module, 'example'):
            if isinstance(module.example, str) and module.example.strip():
                # Non-empty string
                result = run(getattr(module, func_name), StringIO(module.example), example=True)
                has_valid_example = True
            elif isinstance(module.example, StringIO) and module.example.getvalue().strip():
                # Non-empty StringIO
                module.example.seek(0)  # Reset position to start
                result = run(getattr(module, func_name), module.example, example=True)
                has_valid_example = True
            elif module.example and not isinstance(module.example, (str, StringIO)):
                # Other non-empty object (like a custom input object)
                result = run(getattr(module, func_name), module.example, example=True)
                has_valid_example = True

        # Fall back to aocd examples if no valid example
        if not has_valid_example and aocd_examples:
            result = run(getattr(module, func_name), StringIO(aocd_examples[0].input_data), example=True)
        # Fall back to sample file if no other options
        elif not has_valid_example:
            result = run(getattr(module, func_name), f"input/{args.year}/day{args.day:02}_sample.txt")

        # Check example answer if available
        if example_answer is not None:
            if str(result) == str(example_answer):
                print("\t" + colored(f"✓ (Expected: {example_answer})", "green"))
            else:
                print("\t" + colored(f"✗ (Expected: {example_answer})", "red"))
        else:
            print()

        reload(module)
        print("input:", end="\t")
        ans[i] = run(getattr(module, func_name), f"input/{args.year}/day{args.day:02}.txt")
        print()

    if args.submit:
        submit()
