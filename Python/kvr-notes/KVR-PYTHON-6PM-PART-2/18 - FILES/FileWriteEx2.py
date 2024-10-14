#program for writing Iterable object to file --- iterdata.info
#FileWriteEx2.py
obj={10:"Python",30:"Data Science",20:"Java"}
with open("iterdata.info","a") as fp:
	fp.writelines(str(obj)+"\n")
	print("Iterable Object data written to the file")