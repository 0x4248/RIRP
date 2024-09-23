# SPDX-License-Identifier: GPL-3.0
# RIRP
#
# Create case script
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
# 
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

import os
import random
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_case():
    case_number = ""
    for i in range(6):
        case_number += str(random.choice(numbers))
    return case_number

def main():
    case_number = create_case()
    os.mkdir("cases/" + case_number)
    file = open("cases/" + case_number + "/README.md", "w")
    file.write(f"# ENTER_NAME [{case_number}]")
    file.close()
    os.mkdir("cases/" + case_number + "/media")
    os.mkdir("cases/" + case_number + "/recordings")
    print(f"Case {case_number} created.")
    print(f"Please now append:\n| [{case_number}](cases/{case_number}) |                      DESCRIPTION                    |")

if __name__ == "__main__":
    main()