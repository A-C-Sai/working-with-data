#program for demonstrating multiple case labels
#matchcaseEx2.py
wkd=input("Enter a weekday:")
match(wkd.upper()):
	case "MONDAY":
		print("{} is Working Day:".format(wkd))
	case "TUESDAY":
		print("{} is Working Day:".format(wkd))
	case "WEDNESDAY":
		print("{} is Working Day:".format(wkd))
	case "THURSDAY":
		print("{} is Working Day:".format(wkd))
	case "FRIDAY":
		print("{} is Working Day:".format(wkd))
	case "SATURDAY":
		print("{} is Week End:".format(wkd))
	case "SUNDAY":
		print("{} is Holy Day:".format(wkd))
	case _:
		print("{} is a not week day".format(wkd))

