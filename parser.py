import re
from decimal import *


def parser(i):
    # Regular expressions for timestamp, state, target
    state_regex = re.compile(r"state.q%s.*?([0-9.-]+)" % i)
    ts_regex = re.compile(r"state.ts.*?([0-9.-]+)")
    target_regex = re.compile(r"target.q%s.*?([0-9.-]+)" % i)

    # Create empty list of diffs to fill in later
    list_of_diffs = []

    # Open log file
    with open("kuka_robot.log", "r") as in_file:
        for line in in_file:
            # If log line matches regex, calculate the diff and append it to list
            if state_regex.search(line):
                target_radians = Decimal(target_regex.search(line).group(1))
                current_radians = Decimal(state_regex.search(line).group(1))
                diff = abs(current_radians - target_radians)
                list_of_diffs.append({
                    'ts': (ts_regex.search(line).group(1)),
                    'diff': diff})

    max_diff = max(list_of_diffs, key=lambda x: x['diff'])
    print('max difference for joint №%s :' % i, max_diff)

    return list_of_diffs
