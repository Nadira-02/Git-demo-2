oikea_käytäjätunnus = "python"
oikea_salasana = "rules"

yritykset = 0
maksimi_yritykset = 5

while yritykset < maksimi_yritykset:
    käytäjätunnus = input("Anna käytäjätunnus: ")
    salasana = input("Anna salasana: ")

    if käytäjätunnus == oikea_käytäjätunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset +=1
        if yritykset == maksimi_yritykset:
            print("Pääsy evätty.")
        else:
            print("Väärä käytäjätunnus tai salasana. Yritä uudelleen.\n")
            