def programma():
    print("Hello you!")
    print("Ik ben Bas")
    print("Wat is jou naam?")
    naam = input()

    print("")
    print("wat een mooie naam, " + naam + "!")

    print("")
    print("Ik ben een nieuwkomer op het MA college.")
    print("Ik geef je nu een meer keuzen vraag zodat je mij beter leert kennen.")

    print("")
    vraag1 = "1. Welke opleiding heb ik gekeuzen?\nA. Media developer\nB. software developer\nC. game developer"
    vraag2 = "2. Welke kleur haar heb ik?\nA. groen\nB. roze\nC. roze met wat zilver"
    vraag3 = "3. Waar heb ik op school gezeten?\nA. basicschool\nB. middelbareschool\nC. college"

    print("")
    print(vraag1)


    def vraag1Juist():

        antwoordVraag1 = input()
        if antwoordVraag1 == "c" or antwoordVraag1 == "b" or antwoordVraag1 == "C" or antwoordVraag1 == "B":
            print("Ja, dat is goed. Ik moet eerst software developer doen voor dat ik game developer kan doen.")
        elif antwoordVraag1 == "a" or antwoordVraag1 == "A":
            print("Nee, ik ga geen media developer doen want ik vind dat niet leuk.")
        else:
            print("Je mag alleen a, b of c typen.")
            vraag1Juist()
    vraag1Juist()

    print(vraag2)

    def vraag2Juist():

        antwoordVraag2 = input()
        if antwoordVraag2 == "a" or antwoordVraag2 == "b" or antwoordVraag2 == "A" or antwoordVraag2 == "B":
            print("nee, je heb het fout, als je b zei dan was je dichtbij.")
            print(vraag3)
        elif antwoordVraag2 == "c" or antwoordVraag2 == "C":
            print("Ja je heb gelijk, ken je shoto todoroki, zo ja hij is de inspiratie, zo nee hij is de inspiratie")
        else:
            print("Je mag alleen a, b of c typen.")
            vraag2Juist()
    vraag2Juist()

    print(vraag3)

    def vraag4():

        print("4. Wat is mijn favorieten eten?\nA. Macaroni\nB. Shusi\nC. kiptandori")
        antwoordvraag4 = input()
        if antwoordvraag4 == "a" or antwoordvraag4 == "A" or antwoordvraag4 == "c" or antwoordvraag4 == "C":
            print("Het is wel lekker maar niet het lekkers.")
        elif antwoordvraag4 == "b" or antwoordvraag4 == "B":
            print("Shusi is natuurlijk mijn favo eten.")
        else:
            print("Je mag alleen a, b of c typen.")
            vraag4()

    def vraag5():

        print("5. Wat is mijn hobby?\nA. Gamen\nB. Paardrijden\nC. Fitness")
        antwoordvraag4 = input()
        if antwoordvraag4 == "a" or antwoordvraag4 == "A" or antwoordvraag4 == "c" or antwoordvraag4 == "C":
            print("Ja dat klopt.")
            print("Je kent me nu wel goed :D")
        elif antwoordvraag4 == "b" or antwoordvraag4 == "B":
            print("Nee ik heb nooit op een paard gerijden.")
        else:
            print("Je mag alleen a, b of c typen.")
            vraag5()

    def vraag3Juist():

        antwoordVraag3 = input()
        if antwoordVraag3 == "a" or antwoordVraag3 == "b" or antwoordVraag3 == "A" or antwoordVraag3 == "B":
            print("Ja, maar nu niet meer.\nJe kent mij niet goed, jij moet meer vragen beantworden.\n")
            print(vraag5())
        elif antwoordVraag3 == "c" or antwoordVraag3 == "C":
            print("Ja, ik zit daar nu op.\nJe kent mij best goed, jij mag meer vragen beantworden.\n")
            print(vraag4())

        else:
            print("Je mag alleen a, b of c typen.")
            vraag3Juist()
    vraag3Juist()

    print("wil je het herstarten? Y/N")
    herstarten = input()
    if herstarten == "Y" or herstarten == "y":
        programma()
    else:
        print("Bye bye " + naam)

programma()
