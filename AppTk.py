from tkinter import *
from chat import get_response, bot_name

# Définition des couleurs de fond, de texte et des polices pour la GUI
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        # Configuration de la fenêtre principale
        self.window.title("Chatbot assistant ")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=570, height=750, bg=BG_COLOR)
        self.window.iconbitmap(r'la-poste-tunisienne-logo-6EDCA63698-seeklogo.com-_1_.ico')

        # Label d'en-tête
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="bienvenue", font=FONT_BOLD, pady=15)
        head_label.place(relwidth=1)

        # Petite ligne de séparation
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Zone de texte
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Barre de défilement
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Label inférieur
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Zone de saisie de message
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Bouton d'envoi
        send_button = Button(bottom_label, text="Envoyer", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        # Récupération du message saisi par l'utilisateur
        msg = self.msg_entry.get()
        # Insertion du message dans la zone de texte
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        # Vérification si le message est vide
        if not msg:
            return
        # Effacement de la zone de saisie de message
        self.msg_entry.delete(0, END)
        # Insèrer le message envoyé par l'utilisateur dans la zone de texte et désactive la modification de la zone de texte
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # Obtient la réponse du chatbot en appelant la fonction get_response() et construit le message de réponse
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        # Insèrer le message de réponse du chatbot dans la zone de texte et désactive la modification de la zone de texte
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        # Fait défiler la zone de texte pour afficher les derniers messages
        self.text_widget.see(END)


if __name__ == "__main__":
    # Initialiser l'application de chat
    app = ChatApplication()
    app = ChatApplication()
    # Lancer l'application
    app.run()