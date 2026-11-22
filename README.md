## Opettajien koepankki
- Sovelluksessa käyttäjät (opettajat) pystyvät jakamaan kokeitaan
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään kokeita, muokkaamaan sen tietoja ja poistamaan kokeen
- Käyttäjä näkee sovellukseen lisätyt kokeet
- Käyttäjä pystyy etsimään kokeita aineen, pitämisvuoden ja opettajan mukaan
- Käyttäjäsivu näyttää, montako koetta on lisännyt ja listaa lisätyt kokeet
- Käyttäjä pystyy valitsemaan eri aineiden, vuosien, opettajien kokeita ja kirjoittamaan niihin kommentteja

## Ohjeet tarkastajalle:

Aja ensin

```
$ pip install flask
```

Seuraavalla komennolla saat taulut tietokantaan
```
$ sqlite3 database.db < schema.sql
```
Jos olet koepankki-repositorion juuressa, niin ohjelma ajaa itsensä komennolla
```
$ flask run
```

## Kommentteja tarkistukseen
- Palautteen mukaisia muutoksia (layoutiin ei koskettu vielä ja varmasti joku return jäljellä)
- Dropdownit lisätty
- Turhat linkit piilotettu
- Estetty oikeuksia muokata, poistaa ja nähdä sivuja sivullisilta
- Vuosilukuun validointi, mihin tulee vielä muutos, kun tiedän, miten haluan vuosia rajoittaa. Nyt myös tämä vuosi + 1 sallittu
- Etusivun taulukko muokattu nätimmäksi ja siihen lisätty tekijä
