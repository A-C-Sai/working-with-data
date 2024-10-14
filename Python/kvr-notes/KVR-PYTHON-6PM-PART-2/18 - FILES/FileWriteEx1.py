#proigram wrting address of different people into file addr1.data
#FileWriteEx1.py
with open("addr1.data","a") as fp:
	fp.write("Travis Oliphant\n")
	fp.write("HNO:13-14,RED SEA  SIDE\n")
	fp.write("NUMPY Software Foundation\n")
	fp.write("Nether lands-53\n")
	print("\nData Written to the file--veridy")
