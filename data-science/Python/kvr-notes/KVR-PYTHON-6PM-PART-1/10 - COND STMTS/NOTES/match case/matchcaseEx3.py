#program for demonstrating multiple case labels
#matchcaseEx3.py
wkd=input("Enter a weekday:")
match(wkd[0:3].upper() ):
	case "MON":
		print("{} is Working Day:".format(wkd))
	case "TUE":
		print("{} is Working Day:".format(wkd))
	case "WED":
		print("{} is Working Day:".format(wkd))
	case "THU":
		print("{} is Working Day:".format(wkd))
	case "FRI":
		print("{} is Working Day:".format(wkd))
	case "SAT":
		print("{} is Week End:".format(wkd))
	case "SUN":
		print("{} is Holy Day:".format(wkd))
	case _:
		print("{} is a not week day".format(wkd))
