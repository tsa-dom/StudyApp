# Learn Today

## Sovelluksen Heroku linkki
#### [Learn Today](https://tsoha-studyapp.herokuapp.com/)

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on että sivustoa käyttävä käyttäjä näkee listan sivustolla olevista muiden kirjautuneiden käyttäjien luomista suosituimmista oppimateriaaleista. Oppimateriaalien nimien ja kuvausten tarkastelu ei vaadi käyttäjältä kirjautumista, mutta käyttäjän on kirjauduttava palveluun nähdäkseen oppimateriaalin sisältöjä ja tehdessään omia oppimateriaaleja.

## Toteutetut ominaisuudet
* Käyttäjänä luoda käyttäjätunnuksen joka sisältää vähintään 3 merkkiä.
* Sovellus reagoi joihinkin käyttäjätunnusta luodessa tapahtuviin validointiongelmiin.
* Käyttäjänä voin kirjautua sovellukseen olemassa olevalla käyttäjätunnuksella ja salasanalla.
* Käyttäjänä voin tarkastella listaa käyttäjien luomista materiaaleista.
* Kirjautuneena käyttäjänä voin tarkastella oppimateriaalien sisältöjä.
* Kirjautuneena käyttäjänä voin luoda oman oppimateriaalin.
* Kirjautuneena käyttäjänä näen listan omista materiaaleista.
* Kirjautuneena käyttäjänä voin lisätä ja muokkaa sisältöä luomiini oppimateriaaleihin

## Ominaisuudet joita ei olla vielä tehty
* Sovelluksen oppimateriaalien hakutoiminnallisuus nimen, tekijän ja kategorian mukaan
* Palautteen anto mahdollisuus oppimateriaalin tekijälle, sekä pisteytyksen antaminen
* Oppimateriaalin ja sen sisällön poistaminen
* Mahdollisuus lisätä tehtäviä oppimateriaalille
* Mahdollisuus tehdä muiden käyttäjien luomia tehtäviä
* Oppimateriaalien järjestys niille annettujen pisteytysten mukaan
* Kirjautunut käyttäjä voi rajoittaa luomansa oppimateriaalin käyttöä kirjautumisavaimella

## Sovelluksen testaaminen herokussa
#### Käyttäjän luominen
Käyttäjän voi luoda antamalla käyttäjätunnuksen ja sille salasanan. Käyttäjätunnuksen tulee sisältää vähintään 3 merkkiä ja maksimissaan 20. Mikäli maksimi merkki määrä ylittyy, ei sovellus toistaiseksi ilmoita siitä, mutta et voi luoda käyttäjätunnusta. Käyttäjätunnuksen tulee olla myös uniikki, joten mikäli käyttäjätunnuksen luominen ei onnistu, saattaa olla syy tässä, mikäli yrittää luoda käyttäjätunnusta joka on jo olemassa. Salasanan tulee olla vähintään 8 merkkiä pitkä ja se on annettava kaksi kertaa ja molempien salasanojen tulee olla keskenään samat.

#### Kirjautuminen
Sovellukseen voi kirjautua antamalla olemassa olevan käyttäjätunnuksen ja sen salasanan. Mikäli kirjautuminen epäonnistuu, ei sovellus ilmoita siitä mutta et pääse kirjautumisruudusta pidemmälle.

#### Listaus sovellukseen tallennetuista oppimateriaaleista
Vaikka sovellukseen ei olisi kirjautunut pystyy katsomaan sovellukseen tallennettujen oppimateriaalien nimiä ja kuvauksia. Klikkaamalla materiaalia pääset tarkastelemaan materiaalia jos olet kirjautunut ja mikäli et ole kirjautunut sovellukseen, ohjaa sovellus tällöin kirjautumisikkunaan.

Kirjautunut käyttäjä pystyy tarkastelemaan myös listausta luomistaan oppimateriaaleista.

#### Oppimateriaali
Oppimateriaali sivu näyttää erillaiselta oppimateriaalin omistajalle ja sitä tarkastelevalle käyttäjälle. Käyttäjä joka ei omista oppimateriaalia näkee sivulla oppimateriaalin sisällöllisen kuvauksen, sekä linkin oppimateriaalin eri lukuihin jos sellaisia on oppimateriaalille luotu.

Mikäli käyttäjä joka omistaa oppimateriaalin, haluaa muokata oppimateriaalin sisällöllistä kuvausta voi painaa *muokkaa tekstiä* painiketta. Painikkeen painamisen jälkeen tekstiruutuun voi kirjoittaa lisää tekstiä. Tekstiruutu on kömpelö jos teksiä on vain muutama rivi, sillä se ei synkronoi kirjoitettujen rivien määrän kanssa. Käyttäjä saa kaksi toiminnallisuutta lisää, voi piilottaa tekstin muokkausmahdollisuuden, jolloin tekstiä ei voi muokata enään tai käyttäjä voi lähettää tekstiruudun silloisen sisällön palvelimelle.

Sisältö osassa käyttäjä näkee luomansa sisällöt oppimateriaalille. Oppimateriaalille voi luoda lisää sisältöä painamallla *lisää uusi kappale* nappulaa. Tämän jälkeen kaksi teksiruutua, joista toiseen voi kirjoittaa sisällön nimen ja toiseen enemmän tekstiä. Tekstit lähetetään palvelimelle *tallenna* nappulasta, jolloin uusi sisältö ilmestyy sivustolle jos se onnistuu.

#### Uuden oppimateriaalin luominen
Käyttäjä voi luoda oppimateriaalin antamalla sille nimen, sisällön (jota voidaan muokata jälkeenpäin) ja katergorian. Oppimateriaalin nimen tulee sisältää vähintään 4 merkkiä ja jos ehto ei täyty ilmoittaa sovellus käyttäjälle siitä. Kategoria ruudulla ei toistaiseksi ole mitään tekemistä sovelluksen nykyisen version kanssa, mutta sille tulee myöhemmin oppimateriaalien haun kannalta oleellinen ominaisuus.

#### Materiaalin nimen muuttaminen
Materiaalin nimeä voidaan muokata jos materiaali on käyttäjän oma tekemä. Selain tekee ponnahdusikkunan kun materiaalia yritetään luoda.

#### Materiaalin poistaminen
Oman luodun materiaalin voi poistaa jos hyväksyy poistamisen kirjoittamalla DELETE materiaalin poiston yhteydessä tulevaan ponnahdusikkunaan.

#### Materiaalien ranking
Materiaaleja voi käyttäjien osalta tykkää/epätykkää, jolloin sen pisteytys nousee tai laskee sen mukaan. Materiaalit on järjestetty pisteytyksen mukaan.

#### Palautteen antaminen
Materiaalille voi antaa palautetta, jolloin se on materiaalin luoneen käyttäjän nähtävissä.

#### Materiaalien hakutoiminnallisuus
Materiaaleja voidaan hakea nimen, tekijän ja tagin perusteella.
