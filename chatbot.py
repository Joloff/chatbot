import tkinter as tk
from tkinter import ttk, scrolledtext
import re

# Avainsanoihin perustuvat vastaukset chatbotille
keyword_responses = {
    "sähköposti": "Opinto-ohjaajan sähköposti on opo@lapinamk.fi.",
    "tuki": "Voit kysyä IT-tuesta tai opintotuesta. Kumpaa tarkoitat?",
    "vaihto-opiskelu": "Lapin AMK tarjoaa mahdollisuuden suorittaa vaihto-opintoja ulkomailla.",
    "kurssi": "Voit ilmoittautua kursseille Lapin AMK:n verkkopalvelun kautta tai opintotoimistossa.",
    "harjoittelu": "Voit etsiä harjoittelupaikkoja Lapin AMK:n työelämäpalveluiden kautta.",
    "opintopisteet": "Voit tarkistaa kertyneet opintopisteesi Lapin AMK:n opiskelijaportaalista.",
    "valmistuminen": "Tutkintotodistuksen hakeminen tapahtuu opiskelijapalveluiden kautta.",
    "lukujärjestys": "Lukujärjestykset löytyvät Pepistä ja Moodlesta.",
    "opintotuki": "Opintotukea haetaan Kelan verkkopalvelun kautta.",
    "itseopiskelu": "Voit hyödyntää Lapin AMK:n itseopiskelumateriaaleja verkkosivustolla.",
    "kirjasto": "Lapin AMK:n kirjasto tarjoaa monia hyödyllisiä kirjoja ja e-aineistoja.",
    "tentit": "Tenttipäivät ja aikataulut löytyvät Pepistä ja kurssikohtaisilta Moodlen sivuilta.",
    "opiskelijakortti": "Opiskelijakortin voi tilata opiskelijakunnan kautta.",
    "palautteet": "Voit antaa palautetta kursseista suoraan Pepin kautta tai suoraan opettajalle.",
    "ruokailu": "Opiskelijaruokalat tarjoavat edullisia aterioita opiskelijoille.",
    "asuminen": "Opiskelija-asuntoja voi hakea esimerkiksi Domus Arctica -säätiön kautta.",
    "liikunta": "Lapin AMK tarjoaa opiskelijoilleen liikuntapalveluja, katso lisätietoja verkkosivuilta.",
}


def preprocess_text(text):
    """Poistaa ylimääräiset välit ja erikoismerkit sekä muuntaa pieniksi kirjaimiksi"""
    return " ".join(re.findall(r"\w+", text.lower()))


def send_message():
    """Lähettää viestin ja hakee sopivan vastauksen"""
    user_input = entry.get().lower()
    chat_area.insert(tk.END, "Sinä: " + user_input + "\n", "user")
    entry.delete(0, tk.END)

    processed_input = preprocess_text(user_input)

    for keyword, response in keyword_responses.items():
        if re.search(r"\b" + re.escape(keyword) + r"\b", processed_input):
            chat_area.insert(tk.END, "Botti: " + response + "\n", "bot")
            chat_area.yview(tk.END)
            return

    chat_area.insert(
        tk.END,
        "Botti: En valitettavasti ymmärtänyt kysymystäsi. Voit kysyä esimerkiksi 'opintotuki', 'lukujärjestys' tai 'harjoittelu'.\n",
        "bot",
    )
    chat_area.yview(tk.END)


def show_help():
    """Näyttää listan aiheista, joita voi kysyä"""
    help_text = """Voit kysyä esimerkiksi: 
- Opinto-ohjaajan yhteystiedot 
- Opintotuen hakeminen 
- Vaihto-opiskelumahdollisuudet 
- Kurssi-ilmoittautuminen 
- Harjoittelupaikan haku 
- IT-tuki 
- Opintopisteet 
- Valmistuminen 
- Lukujärjestys 
- Kirjasto 
- Tentit 
- Opiskelijakortti 
- Palautteet 
- Ruokailu 
- Asuminen 
- Liikunta"""
    chat_area.insert(tk.END, "Botti: " + help_text + "\n", "bot")
    chat_area.yview(tk.END)


# Tkinter-käyttöliittymä
root = tk.Tk()
root.title("Lapin AMK Chatbot")
root.geometry("500x450")
root.configure(bg="#2c2f33")  # Tumma tausta

style = ttk.Style()
style.configure("TButton", font=("Arial", 16), padding=6)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=50,
    height=15,
    font=("Arial", 16),
    bg="#23272a",
    fg="white",
    borderwidth=3,
    relief="sunken",
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.tag_configure("user", foreground="#f1c40f", font=("Arial", 16, "bold"))
chat_area.tag_configure("bot", foreground="#1abc9c", font=("Arial", 16))

# Lisää tervetuloviesti ja ohjeet käyttöön heti sovelluksen käynnistyessä
chat_area.insert(tk.END, "Botti: Tervetuloa Lapin AMK Chatbotiin! 😊\n", "bot")
chat_area.insert(
    tk.END,
    "Botti: Voit kysyä esimerkiksi opintotuesta, kursseista tai kirjastosta. Kirjoita kysymyksesi alla olevaan kenttään ja paina Lähetä.\n",
    "bot",
)
chat_area.yview(tk.END)

entry_frame = tk.Frame(root, bg="#2c2f33")
entry_frame.pack(pady=5, fill=tk.X)

entry = ttk.Entry(entry_frame, width=50, font=("Arial", 16))
entry.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)

send_button = ttk.Button(
    entry_frame, text="Lähetä", command=send_message, style="TButton"
)
send_button.pack(side=tk.RIGHT, padx=5)

help_button = ttk.Button(
    root, text="Miten voin auttaa?", command=show_help, style="TButton"
)
help_button.pack(pady=5)

root.mainloop()
