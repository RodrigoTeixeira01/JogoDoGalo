import Easy, Normal, Hard
a=input("1) Facil\n2) Medio\n3) Díficil\nR.:")
while a not in ["1","2","3"]:
    a=input("1) Facil\n2)Medio\n3)Díficil\nR.:")
if a=="1":
    Easy.main()
elif a=="2":
    Normal.main()
elif a=="3":
    Hard.main()
