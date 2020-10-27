def programma():
    print("\nWelkom bij het verhaal over een nieuwkomer. Dit is een project van school en ik als student heb dit gemaakt. Dit is een meer keuze vraag en je kan op verschillende eindes komen.")
    print("\nWat is jou naam?")
    naam = input()

    begin_stuk = "Je bent een man die vanaf Pakistan naar Nederland wilt vluchten."


    def vraag21():

        print("\nJe heb ineens veel mee gemaakt, wil je er nu een einde aan maken?")
        print("vraag 21: Zelfmoord?\nA. ja\nB. nee")

        antwoord21 = input()
        if antwoord21 == "a" or antwoord21 == "A":
            vraag12()
        elif antwoord21 == "b" or antwoord21 == "B":
            print("\nJe sprong van een brug af. (dood einde)")
            return
        else:
            print("Je mag alleen a, b of c typen.")
            vraag21()
#--------------------------------------------------------------------------------------------------------------------------------
    def vraag20():

        print("vraag 20: REN?!?!?!?\nA. nee\nB. ja")

        antwoord20 = input()
        if antwoord20 == "a" or antwoord20 == "A":
            print("\nJe blijf stil staan in plaat van vluchten dus ze hebben je dood geslagen met meerdere mensen, maar je zus rende wel dus zei heeft een baan gevonden en woont nu in Nederland. (dood einde)")
            return
        elif antwoord20 == "b" or antwoord20 == "B":
            print("\nJe bent alweer gevlucht.")
            vraag21()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag20()

    def vraag19():

        print("vraag 19: Ga je met je zus haar leugen mee?\nA. ja\nB. nee")

        antwoord19 = input()
        if antwoord19 == "a" or antwoord19 == "A":
            print("\nZe vonden het redelijk klinken dus ze laten je met rust.")
            vraag12()
        elif antwoord19 == "b" or antwoord19 == "B":
            print("\nJe krijg ruzie met je zus want je leug niet mee.")
            vraag20()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag19()

    def vraag18():

        print("vraag 18: Wie van je fammillie ga je om hulp vragen?\nA. moeder\nB. broer\nC. zus")

        antwoord18 = input()
        if antwoord18 == "a" or antwoord18 == "A":
            print("\nJe moeder vond het geen goed idee dus ze sloch je met een slipper. (slecht einde, want je bent niet gevlucht)")
            return
        elif antwoord18 == "b" or antwoord18 == "B" or antwoord18 == "c" or antwoord18 == "C":
            print("\nGoede keuzen")
            vraag2()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag18()

    def vraag17():

        print("vraag 17: Met welke vervoer wil je gaan vluchten?\nA. vliegtuig\nB. auto")

        antwoord17 = input()
        if antwoord17 == "a" or antwoord17 == "A":
            vraag7()
        elif antwoord17 == "b" or antwoord17 == "B":
            vraag3()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag17()

    def vraag16():

        print("vraag 16: Wie ga je vragen om je te helpen vluchten?\nA. smokkelaar\nB. fammillie")

        antwoord16 = input()
        if antwoord16 == "a" or antwoord16 == "A":
            print("\nJe heb iemand gevonden die je kan helpen.")
            vraag17()
        elif antwoord16 == "b" or antwoord16 == "B":
            vraag18()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag16()
#--------------------------------------------------------------------------------------------------------------------------------
    def vraag15():

        print("\nZe hebben jou gezien en willen je dood hebben")
        print("vraag 15: REN?!?!?!?\nA. nee\nB. ja")

        antwoord15 = input()
        if antwoord15 == "a" or antwoord15 == "A":
            print("\nJe blijf stil staan in plaat van vluchten dus ze hebben je dood geslagen met meerdere mensen. (dood einde)")
            return
        elif antwoord15 == "b" or antwoord15 == "B":
            print("\nJe bent gevlucht van hun en gaat nu wat anders doen.")
            vraag12()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag15()

    def vraag14():

        print("\nDe gang wilt geld dus ze gaan een bank beroven.")
        print("vraag 14: Ga je ze helpen?\nA. nee\nB. ja")

        antwoord14 = input()
        if antwoord14 == "a" or antwoord14 == "A":
            vraag15()
        elif antwoord14 == "b" or antwoord14 == "B":
            print("\nJe helpt ze maar je vindt het toch geen goed idee. Dus je zorgt er voor de vlucht auto der banden lek zijn.")
            vraag11()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag14()

    def vraag13():

        print("vraag 13: Vindt je de kroket lekker?\nA. ja\nB. nee")

        antwoord13 = input()
        if antwoord13 == "a" or antwoord13 == "A":
            print("\nJe vond het lekker dus je wordt verder begeleid in de vluchtenlingenkamp.")
            vraag12()
        elif antwoord13 == "b" or antwoord13 == "B":
            print("\nJe heb geen baan gevonden dus je werdt een zwerfer. (slecht einde)")
            return
        else:
            print("Je mag alleen a, b of c typen.")
            vraag13()

    def vraag12():

        print("\nJe heb veel mee gemaakt maar je moet nu iets doen.")
        print("vraag 12: Wil je een baan zoeken?\nA. ja\nB. nee")

        antwoord12 = input()
        if antwoord12 == "a" or antwoord12 == "A":
            print("\nJe heb een baan gevonden en heb een huis gekocht. (Goed einde)")
            print("\n\nWees blij je heb HET einde van dit verhaal gekregen!!!\nGefelicedeerd " + naam + ".")
            return
        elif antwoord12 == "b" or antwoord12 == "B":
            vraag21()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag12()

    def vraag11():

        print("vraag 11: Ga je liegen of ben je eerlijk?\nA. ja\nB. nee\nC. mee met broer (alleen toegang kelijk als je bij vraag 18 het antwoord broer keus(niet vals spelen)")

        antwoord11 = input()
        if antwoord11 == "a" or antwoord11 == "A":
            print("\nZe belonde jou eerlijkheid met een normaal leven?(normaal einde)")
            return
        elif antwoord11 == "b" or antwoord11 == "B":
            print("\nZe hebben je gedood omdat je leug. (dood einde)")
            return
        elif antwoord11 == "c" or antwoord11 == "C":
            print("\nJe leug met je broer waardoor jullie de krachten van broers gebruikten om hun te verslaan. (goed einde, want je bent gevlucht en heb de politie geholpen om de gang te aresteren.)")
            return
        else:
            print("Je mag alleen a, b of c typen.")
            vraag11()
#--------------------------------------------------------------------------------------------------------------------------------
    def vraag10():

        print("\nJe moet er nog over nadenken (of overleggen met je zus)")
        print("vraag 10: Weet je het zeker of je in de gang wilt?\nA. ja\nB. nee\nC. luister naar je zus (alleen toegang kelijk als je bij vraag 18 het antwoord zus keus(niet vals spelen))")

        antwoord10 = input()
        if antwoord10 == "a" or antwoord10 == "A":
            print("\nJe bent nu deel van de gang.")
            vraag14()
        elif antwoord10 == "b" or antwoord10 == "B":
            print("\nJe heb toch nee gezegt en gaat nu wat anders doen.")
            vraag12()
        elif antwoord10 == "c" or antwoord10 == "C":
            print("\nluister naar je zus (alleen toegang kelijk als je bij vraag 18 het antwoord zus keus)")
            vraag19()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag10()

    def vraag9():

        print("\nZe vragen jou me je aan te sluiten bij een gang.")
        print("vraag 9: Sluit je aan?\nA. ja\nB. nee")

        antwoord9 = input()
        if antwoord9 == "a" or antwoord9 == "A":
            vraag10()
        elif antwoord9 == "b" or antwoord9 == "B":
            print("\nJe zei nee en ze lieten jou met rust waardoor je een normaal leven kunnen opbouwen zonder problemen (na dat je wat nederlands had geleerd). (normaal einde, want je bent naar nederland gevlucht met weinig problemen)")
            return
        else:
            print("Je mag alleen a, b of c typen.")
            vraag9()

    def vraag8():

        print("vraag 8: Steel een gebruik de fiets of verder lopen?\nA. lopen\nB. fiets")

        antwoord8 = input()
        if antwoord8 == "a" or antwoord8 == "A":
            print("lopen")
            print("\nJe liep verder en je had geen eten en drinken meer toen ging je dood. (dood einde)")
            return
        elif antwoord8 == "b" or antwoord8 == "B":
            print("\nOmdat je de fiets komt kwam je door fiets-magie in Nederland.")
            vraag3()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag8()

    def vraag7():

        print("\nDe plotie die op het vliegtuig zitten vinden jou er verdacht uit zie, want je zweet heel er en er ziet angst in je ogen.")
        print("vraag 7: Ga je wat zeggen in het Engels of je Pakistaans?\nA. Pakistaans\nB. Engels")

        antwoord7 = input()
        if antwoord7 == "a" or antwoord7 == "A":
            print("\nZe begrepen jou niet dus je werdt onder vraagt. Je bent nu in Iran. (normaal einde, want je bent gevlucht van Pakistan maar niet vergenoeg)")
            return
        elif antwoord7 == "b" or antwoord7 == "B":
            print("\nZe begrepen dat je vlieg angst heb en ze lieten je met rust.")
            vraag4()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag7()

    def vraag6():

        print("vraag 6: Zal je mee gaan met een vliegtuig of vederlopen?\nA. vliegtuig\nB. lopen")

        antwoord6 = input()
        if antwoord6 == "a" or antwoord6 == "A":
            print("\nJe bent nu in een vliegtuig die naar Nederland gaat.")
            vraag7()
        elif antwoord6 == "b" or antwoord6 == "B":
            print("\nJe ziet een fiets na een stukje lopen.")
            vraag8()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag6()

#--------------------------------------------------------------------------------------------------------------------------------

    def vraag5():

        print("vraag 5: Via welke route zal je gaan lopen?\nA. wegen\nB. woestijn\nC. waterkant")

        antwoord5 = input()
        if antwoord5 == "a" or antwoord5 == "A":
            print("\nJe loopt via de wegen en komt uit bij een vliegveld.")
            vraag6()
        elif antwoord5 == "b" or antwoord5 == "B":
            print("\nJe liep door het woestijn heen en je had geen eten en drinken meer toen ging je dood. (dood einde)")
            return
        elif antwoord5 == "c" or antwoord5 == "C":
            print("\nOmdat er altijd water bij je was ben je uit eindelijk in Nederland beland.")
            vraag3()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag5()

    def vraag4():

        print("\nJe bent door de poltie in een vluchtenlingenkamp beland en iemand bied je een kroket aan.")
        print("vraag 4: Neem je het aanbod aan?\nA. nee\nB. ja")

        antwoord4 = input()
        if antwoord4 == "a" or antwoord4 == "A":
            print("nee")
            print("\nOmdat je de kroket niet wou proberen ben je weg gestuurd uit Nederland en ben je heel erg verward geraakt. Je was zo erg verward dat je weer terug ging naar Pakistan. (slecht einde)")
            return
        elif antwoord4 == "b" or antwoord4 == "B":
            vraag13()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag4()

    def vraag3():

        print("\nJe bent beland in Nederland, Maar je weet niet wat je nu moet doen.")
        print("vraag 3: Zal je hulp vragen aan de poltie?\nA. ja\nB. nee")

        antwoord3 = input()
        if antwoord3 == "a" or antwoord3 == "A":
            print("\nJe vroeg om hulp en de poltie was aardig.")
            vraag4()
        elif antwoord3 == "b" or antwoord3 == "B":
            print("\nJe heb een groep mensen gevonden en je vraag hun om hulp")
            vraag9()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag3()

    def vraag2():

        print("vraag 2: Met welk vervoer wil je gaan vluchten?\nA. auto\nB. vliegtuig\nC. lopend")

        antwoord2 = input()
        if antwoord2 == "a" or antwoord2 == "A":
            print("\nJe pakt je auto en rijdt weg.")
            vraag3()
        elif antwoord2 == "b" or antwoord2 == "B":
            print("\nJe bent naar een vliegveld gegaan en zit nu in een vliegtuig.")
            vraag7()
        elif antwoord2 == "c" or antwoord2 == "C":
            print("\nJe gaat lopen, je kiest alleen nog een route.")
            vraag5()
        else:
            print("Je mag alleen a, b of c typen.")
            vraag2()

    def vraag1():

        print("(Als je net klaar ben, kies dan C.)\n")
        print("vraag 1: Wil je wel gaan vluchten?\nA. ja\nB. met hulp\nC. nee")

        antwoord1 = input()
        if antwoord1 == "a" or antwoord1 == "A":
            print("\nJe gaat je spullen inpakken en gaat vluchten.")
            vraag2()
        elif antwoord1 == "b" or antwoord1 == "B":
            print("\nJe gaat je spullen inpakken maar je wilt niet alleen dus je vraag iemand.")
            vraag16()
        elif antwoord1 == "c" or antwoord1 == "C":
            print("Slecht einde, want je bent niet gevlucht")
            return
        else:
            print("Je mag alleen a, b of c typen.")
            vraag1()
        vraag1()
#--------------------------------------------------------------------------------------------------------------------------------
    vraag1()

    print("\nwil je het herstarten? Y/N")
    herstarten = input()
    if herstarten == "Y" or herstarten == "y":
        programma()
    else:
        print("Bye bye " + naam)

programma()
