# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmatkows <lmatkows@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/30 14:23:06 by lmatkows          #+#    #+#              #
#    Updated: 2026/04/30 14:23:09 by lmatkows         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

time_now = time.time()
seconds_time = f"{time_now:,.4f}"
scientific_time = f"{time_now:.3e}"
text_bef = "Seconds since January 1, 1970: "
text_aft = " in scientific notation"
print(f"{text_bef}{seconds_time} or {scientific_time}{text_aft}")
print(time.ctime(time_now))
