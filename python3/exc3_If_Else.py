negara = input("Ketik nama negara\n")
merdeka = int(input("Telah merdeka selama berapa tahun?\n"))
if negara == "Indonesia" or "indonesia":
    print("Negaraku {} telah merdeka selama {} tahun".format(negara, merdeka))
elif negara == "Narnia" or "narnia":
    print("Negri {} telah merdeka selama {} tahun".format(negara, merdeka))
else:
    print("{} telah merdeka selama {} tahun".format(negara, merdeka))
