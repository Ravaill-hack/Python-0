def all_thing_is_obj(object: any)-> int:
	type_obj = type(object)
	if type_obj != str :
	 	sentence_before = str(type_obj).split("'")[1].capitalize() + " :"
	else :
	 	sentence_before = object + " is in the kitchen :"
	if (type_obj == str or type_obj == set or type_obj == tuple or type_obj == dict or type_obj == list) :
		print (f"{sentence_before} {str(type_obj)}")
	else :
		print ("Type not found")
	return 42