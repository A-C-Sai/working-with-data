#program for demonstrating multiple case labels
#matchcaseEx4.py
wkd=input("Enter a weekday:")
match(wkd[0:3].upper() ):
	case "MON" | "TUE" | "WED" | "THU" | "FRI":
		print("{} is Working Day:".format(wkd))
	
	case "SAT":
		print("{} is Week End:".format(wkd))
	case "SUN":
		print("{} is Holy Day:".format(wkd))
	case _:
		print("{} is a not week day".format(wkd))