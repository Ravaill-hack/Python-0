# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lmatkows <lmatkows@student.42perpignan.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/30 14:22:56 by lmatkows          #+#    #+#              #
#    Updated: 2026/04/30 14:22:59 by lmatkows         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[-1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.remove("tutu!")
ft_set.add("Perpignan!")
ft_dict["Hello"] = "42Perpignan!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
