# Himmelilaskuri 2019
# Opiskelijan tulojen laskemiseen tarkoitettu python-laskuri

def LaskeOpintotukiKuukaudet(ansioTulot, alkupOsinkoTulot):
    totTulot = float(ansioTulot + alkupOsinkoTulot)
    maxVal = 0
    for i in range(13):
        maxVal = ((12 - i) * 667) + i * 1990
        if(maxVal >= totTulot):
            break

    return(maxVal, 12 - i)

def LaskePaaomavero(alkupOsinkoTulot):
    print("\nPääomatulojen laskenta")
    osinkoTulot = 0.85 * alkupOsinkoTulot
    print("    Veronalaiset pääomatulot")
    print("        Osinkotulot: {:.2f} €".format(osinkoTulot))

    if(osinkoTulot < 30000):
        paaOmavero = 0.3 * osinkoTulot
    else:
        paaOmavero = 0.34 * osinkoTulot

    print("    Pääomavero: {:.2f} €".format(paaOmavero))
    
    return(osinkoTulot, paaOmavero)

def LaskePuhtaatAnsiotulot(palkkaTulot, opintoRaha, stipendit):
    print("\nPuhtaiden ansiotulojen laskenta")
    puhtaatAnsiotulot = float(palkkaTulot + opintoRaha + stipendit)

    # Luonnolliset vähennykset:
    # Tulonhankkimisvähennys 750 €
    puhtaatAnsiotulot -= 750
    print("    Vähennykset\n        Tulonhankkimisvähennys: 750.00 €\n    Puhtaat ansiotulot: {:.2f} €".format(puhtaatAnsiotulot))

    return(puhtaatAnsiotulot)

def LaskeVerotettavatTulot(puhtaatAnsiotulot, palkkaTulot):
    print("\nVerotettavien tulojen laskenta")
    # Sairasvakuutuksen päivärahamaksu
    if(palkkaTulot > 14574):
        sairasvakuutusPaivaraha = (0.018 * palkkaTulot)
        verotettavatTulot = puhtaatAnsiotulot - sairasvakuutusPaivaraha
    else:
        sairasvakuutusPaivaraha = 0
        verotettavatTulot = puhtaatAnsiotulot

    # Pakolliset ja vapaaehtoiset eläkevakuutusmaksut
    pakollinenElakemaksu = 0.0715 * palkkaTulot

    # Pakollinen työttömyysvakuutusmaksu
    tyottomyysVakuutusmaksu = 0.0125 * palkkaTulot
    
    verotettavatTulot -= pakollinenElakemaksu + tyottomyysVakuutusmaksu

    print("    Verotettavat tulot: {:.2f} €\n    Sairasvakuutuksen päivärahamaksu: {:.2f} €".format(verotettavatTulot, sairasvakuutusPaivaraha))
    print("    Pakolliset ja vapaaehtoiset eläkevakuutusmaksut: {:.2f} €\n    Työttömyysvakuutusmaksu: {:.2f} €".format(pakollinenElakemaksu, tyottomyysVakuutusmaksu))

    return(verotettavatTulot, pakollinenElakemaksu, tyottomyysVakuutusmaksu, sairasvakuutusPaivaraha)



def LaskeKunnallisvero(verotettavatTulot, puhtaatAnsiotulot, palkkaTulot, opintoRaha):
    print("\nKunnallisveron laskenta\n    Vähennykset")
    #------------ Kunnallisverotuksen ansiotulovähennys 2020 ----------------#
    if(2500 < palkkaTulot < 7230):
        ansioTuloVahennys = 0.51 * (palkkaTulot - 2500)
    elif(7230 < palkkaTulot):
        ansioTuloVahennys = ((0.51 * 4730) + (0.28 * (palkkaTulot - 7230)))
    else:
        ansioTuloVahennys = 0

    if(ansioTuloVahennys > 3570): # Korjataan tarvittaessa enimmäismäärään
        ansioTuloVahennys = 3570

    if(puhtaatAnsiotulot > 14000): # Ansiotulovähennyksen pienentyminen
        ansioTuloVahennys -= 0.045 * (puhtaatAnsiotulot - 14000)

    if(ansioTuloVahennys < 0):
        ansioTuloVahennys = 0
    print("        Kunnallisveron ansiotulovähennys: {:.2f} €".format(ansioTuloVahennys))

    #------------------ Opintorahavähennys 2020 -----------------#
    if(opintoRaha > 2600):
        opintoRahaVahennys = 2600
    else:
        opintoRahaVahennys = opintoRaha

    if(2600 < puhtaatAnsiotulot < 7800): # Puhtaiden ansiotulojen aiheuttama pienentyminen
        opintoRahaVahennys -= 0.5 * (puhtaatAnsiotulot - 2600)
    elif(puhtaatAnsiotulot > 7800):
        opintoRahaVahennys = 0

    print("        Opintorahavähennys: {:.2f} €".format(opintoRahaVahennys))

    #---------------- Kunnallisveron alaiset tulot 2020 --------------#
    kunnallisveroTulo = verotettavatTulot - ansioTuloVahennys - opintoRahaVahennys
    print("    Kunnallisveron alaiset tulot: {:.2f} €".format(kunnallisveroTulo))

    # Perusvähennys ja lopullinen vero
    if(kunnallisveroTulo < 3540):
        kunnallisVero = 0
        perusVahennys = kunnallisveroTulo
    elif(3540 < kunnallisveroTulo < 23200):
        perusVahennys = 3305 - (0.18 * (kunnallisveroTulo - 3305)) # Perusvähennyksen kunnallisveron alaisiin tuloihin perustuva pieneneminen
        kunnallisVero = 0.18 * (kunnallisveroTulo - perusVahennys)
    else:
        perusVahennys = 0
        kunnallisVero = 0.18 * kunnallisveroTulo

    print("    Perusvähennys: {:.2f} €\n    Kunnallisvero: {:.2f} €".format(perusVahennys, kunnallisVero))
    
    return(kunnallisVero)

def LaskeValtionVero(verotettavatTulot):
    print("\nValtionveron laskenta")
    #------------------  Tuloveroasteikko -------------------#
    if(18100 <= verotettavatTulot < 27200):
        porras = 18100
        prosentti = 0.06
    elif(27200 <= verotettavatTulot < 44800):
        porras = 27200
        prosentti = 0.1725
    elif(44800 <= verotettavatTulot < 78500):
        porras = 44800
        prosentti = 0.2125
    elif(78500 <= verotettavatTulot):
        porras = 78500
        prosentti = 0.3125
    else:
        porras = 0
        prosentti = 0

    print("    Veroporras: {:d} €\n    Verorosentti {:.2f}".format(porras, prosentti))

    #---------------------- Valtionveron laskenta -----------------#
    valtionVero = prosentti * (verotettavatTulot - porras)

    print("    Valtionvero: {:.2f} €".format(valtionVero))

    return(valtionVero)

def LaskeYleVero(puhtaatAnsiotulot, paaOmaTulot):
    print("\nYle-veron laskenta")
    # Ansio + pääomatulot > 14000€, 2,50%, max 163€
    totTulot = puhtaatAnsiotulot + paaOmaTulot

    if(14000 < totTulot < 20519.8):
        yleVero = 0.025 * (totTulot - 14000)
    elif(totTulot > 20519.8):
        yleVero = 163
    else:
        yleVero = 0

    print("    Yle-vero: {:.2f} €".format(yleVero))
    return(yleVero)

def LaskeSairaanhoitomaksu(opintoRaha):
    print("\nSairaanhoitomaksun laskenta")
    # Korotettu sairaanhoitomaksu
    sairaanhoitoMaksu = opintoRaha * 0.0165
    print("    Sairaanhoitomaksu: {:.2f} €".format(sairaanhoitoMaksu))

    return(sairaanhoitoMaksu)

def LaskeVahennykset(palkkaTulot, puhtaatAnsiotulot):
    print("\nMuut vähennykset")
    # Työtulovähennys 2020
    # 12.5 % 2500€ ylittävältä osalta, max 1770€
    # >33000 € -> pienenee 0.0184 * (pa - 33000)
    if(2500 < palkkaTulot < 33000):
        tyotuloVahennys = 0.125 * (palkkaTulot - 2500)
    
    else:
        tyotuloVahennys = 0

    if(tyotuloVahennys > 1770): # Korjataan tarvittaessa maksimisummaan
        tyotuloVahennys = 1770

    if(palkkaTulot > 33000):
        tyotuloVahennys -= 0.0184 * (puhtaatAnsiotulot - 33000)

    if(tyotuloVahennys < 0):
        tyotuloVahennys = 0

    print("    Työtulovähennys: {:.2f} €".format(tyotuloVahennys))

    return(tyotuloVahennys)

def LaskeAsumistuki(totTulot):
    perusOmavastuu = 0.42 * ((totTulot / 12) - (603 + 100 * 1))
    if(perusOmavastuu < 0):
        perusOmavastuu = 0
    
    asumisTuki = 0.8 * (503 - perusOmavastuu) * 12

    if(asumisTuki < 0):
        asumisTuki = 0
    


    return(asumisTuki)

def main():
    from os import system

    system("cls")

    print("Himmelilaskuri 2019\n(syötä kaikki tulot ennakonpidätyksen alaisina summina)\n")

    # Raakatulot
    palkkaTulot = float(input("\nSyötä palkkatulot vuoden ajalta: "))
    alkupOsinkoTulot = float(input("Syötä osinkotulot vuoden ajalta: "))
    stipendit = float(input("Syötä stipendit vuoden ajalta: "))
    
    ansioTulot = float(palkkaTulot + stipendit)
    opintorahaTuloraja, tukiKuukaudet = LaskeOpintotukiKuukaudet(ansioTulot, alkupOsinkoTulot)

    opintoRaha = tukiKuukaudet * 250.28

    totTulot = float(palkkaTulot + opintoRaha + alkupOsinkoTulot + stipendit)

    osinkoTulot, paaOmavero = LaskePaaomavero(alkupOsinkoTulot)
    # Tulot vähennysten jälkeen
    puhtaatAnsiotulot = LaskePuhtaatAnsiotulot(palkkaTulot, opintoRaha, stipendit)
    verotettavatTulot, pakollinenElakemaksu, tyottomyysVakuutusmaksu, sairasvakuutusPaivaraha = LaskeVerotettavatTulot(puhtaatAnsiotulot, palkkaTulot)

    # Kunnallisvero
    kunnallisVero = LaskeKunnallisvero(verotettavatTulot, puhtaatAnsiotulot, palkkaTulot, opintoRaha)

    if(kunnallisVero < 0):
        kunnallisVero = 0
    # Valtionvero
    valtionVero = LaskeValtionVero(puhtaatAnsiotulot)

    if(valtionVero < 0):
        valtionVero = 0

    # YLE-vero
    yleVero = LaskeYleVero(puhtaatAnsiotulot, osinkoTulot)

    # Sairaanhoitomaksu (etuuksista)
    sairaanhoitoMaksu = LaskeSairaanhoitomaksu(opintoRaha)

    # Vähennykset
    vahennykset = LaskeVahennykset(palkkaTulot, puhtaatAnsiotulot)

    ansiotuloVerot = kunnallisVero + valtionVero + yleVero - vahennykset

    if(ansiotuloVerot < 0): # Negatiivisten verojen korjaus
        ansiotuloVerot = 0

    totVerot = paaOmavero + ansiotuloVerot
 
    totMaksut = sairaanhoitoMaksu + tyottomyysVakuutusmaksu + pakollinenElakemaksu + sairasvakuutusPaivaraha

    nettoTulot = totTulot - totVerot - totMaksut

    veroOsuus = (totVerot - paaOmavero) / (totTulot - alkupOsinkoTulot)


    asumisTuki = LaskeAsumistuki(totTulot)

    print("\n----------------------------------------------------------------")
    print("Asumistuki: {:.2f} €".format(asumisTuki))
    print("Opintotuki: {:.2f} € ({:d} kuukautta)".format(opintoRaha, tukiKuukaudet))
    
    print("\n----------------------------------------------------------------")
    print("Bruttotulot: {:.2f} €".format(totTulot - opintoRaha))
    print("Tulot verojen jälkeen: {:.2f} €\nKokonaisverot: {:.2f} €\nAnsiotuloverojen osuus: {:.4f}\n".format(totTulot - totVerot, totVerot, veroOsuus))
    print("Maksut: {:.2f} €\nNettotulot: {:.2f} €".format(totMaksut, nettoTulot - opintoRaha))
    
    print("\n----------------------------------------------------------------")
    print("Kokonaistulot tukien jälkeen: {:.2f}\n".format(nettoTulot + asumisTuki))

def ExternalRun(palkkaTulot, alkupOsinkoTulot, stipendit):
    ansioTulot = float(palkkaTulot + stipendit)
    opintorahaTuloraja, tukiKuukaudet = LaskeOpintotukiKuukaudet(ansioTulot, alkupOsinkoTulot)

    opintoRaha = tukiKuukaudet * 250.28

    totTulot = float(palkkaTulot + opintoRaha + alkupOsinkoTulot + stipendit)

    osinkoTulot, paaOmavero = LaskePaaomavero(alkupOsinkoTulot)
    # Tulot vähennysten jälkeen
    puhtaatAnsiotulot = LaskePuhtaatAnsiotulot(palkkaTulot, opintoRaha, stipendit)
    verotettavatTulot, pakollinenElakemaksu, tyottomyysVakuutusmaksu, sairasvakuutusPaivaraha = LaskeVerotettavatTulot(puhtaatAnsiotulot, palkkaTulot)

    # Kunnallisvero
    kunnallisVero = LaskeKunnallisvero(verotettavatTulot, puhtaatAnsiotulot, palkkaTulot, opintoRaha)

    if(kunnallisVero < 0):
        kunnallisVero = 0
    # Valtionvero
    valtionVero = LaskeValtionVero(puhtaatAnsiotulot)

    if(valtionVero < 0):
        valtionVero = 0

    # YLE-vero
    yleVero = LaskeYleVero(puhtaatAnsiotulot, osinkoTulot)

    # Sairaanhoitomaksu (etuuksista)
    sairaanhoitoMaksu = LaskeSairaanhoitomaksu(opintoRaha)

    # Vähennykset
    vahennykset = LaskeVahennykset(palkkaTulot, puhtaatAnsiotulot)

    ansiotuloVerot = kunnallisVero + valtionVero + yleVero - vahennykset

    if(ansiotuloVerot < 0): # Negatiivisten verojen korjaus
        ansiotuloVerot = 0

    totVerot = paaOmavero + ansiotuloVerot
 
    totMaksut = sairaanhoitoMaksu + tyottomyysVakuutusmaksu + pakollinenElakemaksu + sairasvakuutusPaivaraha

    nettoTulot = totTulot - totVerot - totMaksut

    veroOsuus = (totVerot - paaOmavero) / (totTulot - alkupOsinkoTulot)


    asumisTuki = LaskeAsumistuki(totTulot)

    print("\n----------------------------------------------------------------")
    print("Asumistuki: {:.2f} €".format(asumisTuki))
    print("Opintotuki: {:.2f} € ({:d} kuukautta)".format(opintoRaha, tukiKuukaudet))
    
    print("\n----------------------------------------------------------------")
    print("Bruttotulot: {:.2f} €".format(totTulot - opintoRaha))
    print("Tulot verojen jälkeen: {:.2f} €\nKokonaisverot: {:.2f} €\nAnsiotuloverojen osuus: {:.4f}\n".format(totTulot - totVerot, totVerot, veroOsuus))
    print("Maksut: {:.2f} €\nNettotulot: {:.2f} €".format(totMaksut, nettoTulot - opintoRaha))
    
    print("\n----------------------------------------------------------------")
    print("Kokonaistulot tukien jälkeen: {:.2f}\n".format(nettoTulot + asumisTuki))

    return(nettoTulot + asumisTuki, asumisTuki, opintoRaha, totVerot)

#main()