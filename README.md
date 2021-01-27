# Novosadjani

SpaceInvaders je arkadna igra iz 1978. godine. Kreator je Tomoriho Nishikado.

Aplikacija koju smo napravili ima podršku za jednog ili dva igrača na lokalnoj mašini. Svaki igrač ima svoje tastere za kretanje:
  * Player 1 : strelice levo i desno za kretanje i SPACE za isapljivanje metka. 
  *	Player 2: A i D za kretanje, a S za ispaljivanje metka. 

*Igrica sadrži:*
  * Postoje tri tipa enemija koji kada se pogode donose različit broj poena. 
  * Postoje 4 štita koji štite playera od metaka koje ispaljuju enemy-iji.

### Workflow štitova

Štitovi su grafički objekti koji služe da štite igrača od metaka nepriljatelja.
Štitovi se postepeno uništavaju, na svaka 2 metka koja ih pogode, a kada su ukupno 6 puta pogođeni tada nestaju. 
Štit proverava sam za sebe da li ga je neki metak pogodio. Ukoliko jeste smanjuje sebi život i ukoliko nema više života briše se sa ekrana.

### Workflow igrač

Svaki igrač ima 3 života, koje gubi kada je pogođen.
Igrač ima mogućnost pucanja broja metaka u zavisnosti od toga na kojem nivou se nalazi. (npr. drugi nivo -> dva metka, treci nivo -> tri metka)
Igrač se kreće na osnovu odgovarajućih tastera. Kretanje je implementirano tako što čuvamo svako dugme koje je stisnuto u nizu i posle prolazimo kroz taj niz i pomeramo igrača
u odgovarajućem pravcu. Ovo se sve odvija u posebnoj niti da ne bi blokirali GUI u trenutku izvršavanja operacije.
Svaki igrač ima svoj rezultat koji se povećava na osnovu neprijatelja kojeg je pogodio ili DeusExMachine.

### Workflow DeusExMachine

DeusEx mašina se pojavljulje tačno jednom na svakom nivou i pojavljulje se u ravni sa igračima. Pojavljivanje se dešava nasumično nekada u toku nivoa. Postoji mogućnost da se ne pojavi u toku nekog nivoa.
Ukoliko igrač ne pokupi DeusEx mašinu a pređe na novi nivo ista nestaje i pojavljuje se nekada u toku novog nivoa.
Igrač dobija novi život ukoliko mu fali život a ukoliko ima sve živote dobija 15 poena.
DeusEx mašina se nalazi u novoj niti koja pokreće i novi proces koji služi da generiše x koordinatu u određenom opsegu.

### Workflow nepriljatelja

Na početku igre (i posle na svakom novom nivou) nastaje 5x11 različitih nepriljatelja.
Oni se pomeraju sa leve strane ekrana ka desnoj i obrnuto. Kada dođu do kraja ekrana pomere se za određenu vrednost na dole.
Nepriljatelji nasumičo pucaju i mogu pucati metkove srazmerno broju nivoa.
Na svakom novom nivou nepriljatelji se kreću brže kao i njihovi metkovi.
Nepriljatelji se kreću i pucaju u posebnoj niti.


### Workflow igre

Igra počinje na prvom nivou i svaki igrač ima tri života.
Igra se završava kada jedan od igrača izgubi sva tri života ili nepriljatelji dođu u nivo štitova ukoliko oni postoje a ukoliko ne postoje proverava se nivo igrača.


### Nešto o pythonu

Python je interpreterski jezik visokog nivoa apstrakcije, pa je zbog toga mnogo razumljivji i čitljiviji i ljudima koji se prvi put susreću sa njim, kao što smo i mi na ovom projektu. 
Ovaj programski jezik ima drugačiju sintaksu od jezika sa kojima smo se do sada susretali pa je zbog toga trebalo malo vremena kako bi se navikli. 
Programi koji su napisani u Pythonu su vrlo uredni i čitljivi što omogućava lako snalaženje u kodu.
Python ima isti interpreter na većini operativnih sistema pa ga je zbog toga vrlo lako pokretati na različitim operativnim sistemima.
Kod pythona jer nije tipiziran jezik IDE alati teže mogu predpostave šta korisnik želi da unese.

### Nešto o pyqt5

PyQt5 biblioteke su kreirane da povežu Python kao programski jezik i Qt aplikacijski okvir. 
PyQt5 biblioteka omogućava jednostavno kreiranje aplikacija sa grafičkim korisničkim interfejsom. 
Prednosti PyQt5 okvira su to što omogućava jednostavno pisanje inače složenih grafičkih programa, i uz pomoć svojih biblioteka skriva od programera složenu implementaciju grafike.
Mana PyQt5 može biti izgled samih grafičkih elemenata I to što pozicija istih zavisi isključivo od izvornog koda I zahteva razumevanje pozicioniranja na ekranu.

### Nešto o paralelizaciji rada

Python programski jezik u standradnoj biblioteci nudi podršku za više procesnu i više nitnu paralelizaciju rada. Pored ovoga nudi i sve potrebne dodatke (klase) koje su
potrebne da bi omogućili sinhronizaciju i komunikaciju između niti i/ili procesa.
Niti dele memorijski prostor dok ih procesi ne dele.






