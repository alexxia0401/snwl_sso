#!/usr/bin/env python3

import random


def random_half(l):
    random.shuffle(l)
    print("Run case number", len(l))
    print("Return failed case number", len(l) // 2)
    return l[:(len(l) // 2)]


failed_cases = list(range(1,300001))

test_round = 1
# print("Failed test cases:", failed_cases)

if len(failed_cases) <= 100:
    test_round = -1  # quit loop
    print("Cases <= 100, stop running")
else:
    test_round += 1
    to_run_cases = {}
    n = 0
    if len(failed_cases) <= 20000:
        # no need to split, just run again
        to_run_cases[n] = failed_cases
    else:
        while len(failed_cases) > 20000:
            to_run_cases[n] = failed_cases[0:20000]
            del failed_cases[0:20000]
            n += 1
        else:
            to_run_cases[n] = failed_cases

# for i in to_run_cases:
#     print(i, to_run_cases[i])


while test_round > 1:
    tmp_total_failed_cases = []
    # run split cases
    for i in to_run_cases:
        # print(i, to_run_cases[i])
        print(f"run round {i+1}")
        split_test_result = random_half(to_run_cases[i])
        tmp_total_failed_cases.extend(split_test_result) # equiavelent to failed_cases

    # print(len(tmp_total_failed_cases))
    # test_round = -1

    if len(tmp_total_failed_cases) <= 100:
        test_round = -1  # quit loop
        print("Cases <= 100, stop running")
    else:
        test_round += 1
        to_run_cases = {}
        n = 0
        if len(tmp_total_failed_cases) <= 20000:
            # no need to split, just run again
            to_run_cases[n] = tmp_total_failed_cases
        else:
            while len(tmp_total_failed_cases) >= 20000:
                to_run_cases[n] = tmp_total_failed_cases[0:20000]
                del tmp_total_failed_cases[0:20000]
                n += 1
            else:
                to_run_cases[n] = tmp_total_failed_cases
