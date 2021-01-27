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




