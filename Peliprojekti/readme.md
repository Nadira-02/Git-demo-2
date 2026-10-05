## Trooppisen saaren aarre jahti seikkailupeli ##
------------------------------------------------------------------------------------------------------------------

1. Alkuvaihe

Vaiheen kuvaus:
Pelaaja toimii oppaana ja ennenkuin turistit saapuvat, pelaaja kerää merivirtauksesta tulleet muovijätteet ja roskat, ennen turistilaivan saavuttua. 

Toteutus: 
Toteutin pelaajan ominaisuuden käyttämällä Pelaaja-luokka ja olio-ohjelmointia, johon tallensin nimi, roskien määrää ja inventaario. Pääohjelma kysyy syötteenä kerättävien roskien määrän ja päivittää tiedon pelaaja-oliolle luokan oman metodin avulla.

2. Turistien saapuminen ja reittivalinta

Vaiheen kuvaus: 
Turistien saavuttua pelaaja valitsee suunnan, johon ryhmää lähdetään ohjaamaan.

Toteutus: 
Olen toteuttanut pääohjelman reittifunktiossa valintasilmukana ja ehtolauseina (if-elif-else). Käyttäjän syöttämän numerovalinnan perusteella ohjelma kutsuu vastaavaa kohdefunktiota ja siirtää pelin kulkua halutulle reitille.

3. Kohde 3

Vaiheen kuvaus:
Kohde, jossa turistit saavat ihailla luontoa ja ottaa valokuvia matkamuistoksi

Toteutus: 
Toteutettu omana kohdefunktiona pelilogiikkamoduulissa. Funktio tulostaa tarinallisen kuvauksen ruudulle, pysäyttää ohjelman suorituksen odottamaan käyttäjän ENTER-painallusta ja jatkaa sen jälkeen automaattisesti matkaa seuraavaan kohteeseen (Temppeliin).

4. Kohde 2

Vaiheen kuvaus: 
Turistit tutustuvat saaren historiaan ja voivat halutessaan ostaa matkamuistoja torilta reppuun.

Toteutus:
Toteutettu omana kohdefunktiona, jossa hyödynnetään ehtolauseita ja toistorakennetta (while-silmukka). Mikäli pelaaja päättää ostaa jotain, syötetyt ostokset lisätään merkkijonoina pelaaja-olion inventaario-listaan luokan ostosmetodilla, kunnes pelaaja päättää lopettaa ostokset painamalla ENTER.

5. Kohde 1

Vaiheen kuvaus:
Luolassa kohdataan kolme eri väristä ovea. Oikea ovi selviää seinään kaiverretun matemaattisen vihjeen avulla. Väärä valinta päättää pelin.

Toteutus:
Luolafunktio tulostaa arvoituksen ja pyytää pelaajalta valintaa (1, 2 tai 3). Valinta käsitellään ehtolauseilla, joista jokainen haara johtaa erilaiseen lopputulokseen.

6. Vihje

Vaiheen kuvaus:
Luolan seinässä on yhtälö: 6x + 4 = 20 - 2x.

Toteutus:
Yhtälö esitetään tekstinä käyttäjälle. Yhtälön matemaattinen ratkaisu (x = 2)toimii loogisena perusteena sille, miksi koodissa ovi numero 2 on määritelty ainoaksi oikeaksi vaihtoehdoksi.

7. Ovet
    1) Ovi 1(Sininen ovi):
       Vaiheen kuvaus: 
       Väärä ovi, jonka takana ei ole mitään (Game Over).
       Toteutus:
       Ehtolauseen ensimmäinen haara tulostaa ilmoituksen tyhjästä huoneesta ja palauttaa pääohjelmalle häviötilan ilmaisevan tekstimerkin, mikä päättää seikkailun.
    2) Ovi 2(Vihreä ovi):
       Vaiheen kuvaus:
       Oikea ovi, jonka takaa löytyy hehkuva muinainen kristalli. Pelaaja saa valita ottaako sen reppuunsa.
       Toteutus:
       Ehtolauseen oikea haara esittää lisäkysymyksen esineen poimimisesta. Myöntävällä vastauksella kristalli lisätään pelaajan inventaarioon. Funktio palauttaa pääohjelmalle voittotilan.
    3) Ovi 3(Punainen ovi):
       Vaiheen kuvaus:
       Väärä ovi, jonka takana on käärme (Game Over).
       Toteutus:
       Ehtolauseen kolmas haara tulostaa vaaratilanteen ja palauttaa pääohjelmalle häviötilan.

8. Viimeinen vaihe

Vaiheen kuvaus:
Ryhmä palaa alkupisteeseen ja peli päättyy.

Toteutus:
Pääohjelma ottaa vastaan reitiltä palautetun lopputuloksen (Voitit/Hävisit), tulostaa loppuyhteenvedon pelaajan tiedoista, kerätyistä roskista ja repun sisällöstä, sekä tallentaa lopullisen pelitilanteen automaattisesti tekstitiedostoon (tallennus.txt) tallennusfunktion avulla.

------------------------------------------------------------------------------------------------------------------

Projektin rakenne ja moduulit:
- main.py: Pääohjelma, joka ohjaa pelin kulkua ja valikkoja.

- Peli/pelaaja01.py: Pelaaja-luokka ja sen metodit.

- Peli/kohteet02.py: Pelialueet, tapahtumat ja reittilogiikka.

- Peli/tallennus03.py: Pelitilanteen tallennus, lataus ja tiedostojen lukeminen.

- Tekstitiedostot (.txt): Ohje- ja tallennustiedostot projektin juuressa.

------------------------------------------------------------------------------------------------------------------

--- Kestävä kehitys pelissä ---

Ympäristösuojelu (Ekologinen kestävyys): Rannikon muovijätteiden ja roskien siivoaminen ehkäisee merien saastumista ja suojelee saaren ekosysteemiä.

Kulttuuri ja talous: Vastuullisen matkailun järjestäminen sekä paikallisen torikaupan ja historian tukeminen.


Nadira Harakow