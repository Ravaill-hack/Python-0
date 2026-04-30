# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmatkows <lmatkows@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/30 14:23:32 by lmatkows          #+#    #+#              #
#    Updated: 2026/04/30 14:23:33 by lmatkows         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

args = sys.argv

if (len(args) == 1):
    exit(1)

try:
    assert len(args) == 2
    raw_arg = args[1]
    int_arg = int(raw_arg)

    if (int_arg % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")

except (AssertionError):
    print("AssertionError : more than one argument is provided")

except (ValueError):
    print("AssertionError : argument is not an integer")
