# Chatbot

Tervetuloa käyttämään Lapin AMK:n chatbot-sovellusta! Tämä ohjelma auttaa opiskelijoita löytämään tietoa liittyen opiskeluun, kuten opintotukeen, lukujärjestyksiin, harjoitteluun ja muihin tärkeisiin aiheisiin.

## Käyttöohjeet

1. **Käynnistä ohjelma**
   - Voit käynnistää chatbotin suorittamalla seuraavan komennon komentorivillä:
     ```sh
     python3 chatbot.py
     ```

2. **Kysy kysymyksiä**
   - Kirjoita kysymyksesi tekstikenttään ja paina "Lähetä"-painiketta.
   - Voit kysyä esimerkiksi:
     - "Miten haen opintotukea?"
     - "Missä voin tarkistaa lukujärjestykseni?"
     - "Miten voin hakea harjoittelupaikkaa?"

3. **Näytä avainsanoja**
   - Paina "Miten voin auttaa?" -painiketta saadaksesi listan kysymyksistä, joihin chatbot osaa vastata.

## Ominaisuudet

- **Helppokäyttöinen käyttöliittymä** – Tumma teema ja moderni ilme.
- **Automaattinen vieritys** – Keskustelu rullaa automaattisesti alaspäin uusien viestien myötä.
- **Avainsanoihin perustuva vastauslogiikka** – Botin vastaus perustuu kysymykseen liittyviin avainsanoihin.
- **Tietoa opiskelusta** – Chatbot osaa vastata muun muassa opintotukeen, kurssi-ilmoittautumisiin ja muihin opiskeluun liittyviin kysymyksiin.

## Asennus ja vaatimukset

### **1. Asenna Python**
Varmista, että sinulla on asennettuna **Python 3.10 tai uudempi**. Voit tarkistaa version seuraavalla komennolla:
```sh
python3 --version
```

### **2. Asenna tarvittavat kirjastot**
Ohjelma käyttää **Tkinteriä**, joka sisältyy Pythonin mukana. Erillistä asennusta ei tarvita.

### **3. Lataa tai kloonaa ohjelma GitHubista**
```sh
git clone https://github.com/joloff/chatbot.git
cd chatbot
```

## Kehitys ja muokkaaminen

Jos haluat kehittää chatbotia edelleen:
- Voit lisätä uusia avainsanoja ja vastauksia `keyword_responses`-sanakirjaan.
- Muokkaa käyttöliittymän ulkoasua **Tkinterin** avulla muuttamalla **taustaväriä, fontteja ja painikkeita**.
- Jos haluat lisätä kehittyneempiä ominaisuuksia, voit hyödyntää **luonnollisen kielen käsittelyn (NLP) kirjastoja**, kuten `spaCy` tai `transformers`.

## Lisenssi

Tämä projekti on avoimen lähdekoodin ja jaettu MIT-lisenssillä.

---

Toivottavasti tämä chatbot auttaa sinua löytämään tarvittavan tiedon nopeasti ja helposti! 😊


