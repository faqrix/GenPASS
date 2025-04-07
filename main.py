import hmac
import hashlib
import string

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

Window.set_title('GenPASS')

def generer_mot_de_passe(mdp_maitre, mot_cle, avec_symboles=True, longueur=16):
    if not mdp_maitre or not mot_cle:
        return ""

    h = hmac.new(mdp_maitre.encode(), mot_cle.encode(), hashlib.sha256)
    digest = h.digest()

    chars = string.ascii_letters + string.digits
    if avec_symboles:
        chars += "!@#$%^&*()-_=+[]{}<>?"

    mot_de_passe = ""
    for byte in digest:
        mot_de_passe += chars[byte % len(chars)]
        if len(mot_de_passe) >= longueur:
            break

    while len(mot_de_passe) < longueur:
        for byte in digest:
            mot_de_passe += chars[byte % len(chars)]
            if len(mot_de_passe) >= longueur:
                break

    return mot_de_passe[:longueur]

class PasswordGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        # Fond bleu nuit
        with self.canvas.before:
            Color(0, 0, 0.2, 1)  # Bleu nuit
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Titre
        self.title_label = Label(text="GenPASS - Générateur de Mot de Passe", font_size=30, color=(1, 1, 1, 1), size_hint_y=None, height=50)
        self.add_widget(self.title_label)

        # Mot de passe maître
        self.add_widget(Label(text="Mot de passe maître", color=(1, 1, 1, 1)))
        self.input_maitre = TextInput(password=True, multiline=False, font_size=20, size_hint_y=None, height=40)
        self.add_widget(self.input_maitre)

        # Nom du site / clé
        self.add_widget(Label(text="Nom du site / clé", color=(1, 1, 1, 1)))
        self.input_site = TextInput(multiline=False, font_size=20, size_hint_y=None, height=40)
        self.add_widget(self.input_site)

        # Option d'inclure des symboles
        self.checkbox_symbols = CheckBox(active=True)
        self.symbols_label = Label(text="Inclure des symboles", color=(1, 1, 1, 1))
        symbol_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        symbol_box.add_widget(self.checkbox_symbols)
        symbol_box.add_widget(self.symbols_label)
        self.add_widget(symbol_box)

        # Label du résultat
        self.result_label = Label(text="", font_size=28, bold=True, halign='center', valign='middle', color=(1, 1, 1, 1))
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.add_widget(self.result_label)

        # Bouton générer
        self.btn_generer = Button(text="Générer", font_size=24, size_hint_y=None, height=60, background_color=(0.2, 0.6, 0.8, 1))
        self.btn_generer.bind(on_press=self.on_generer)
        self.add_widget(self.btn_generer)

        # Bouton copier
        self.btn_copier = Button(text="Copier", font_size=24, size_hint_y=None, height=60, background_color=(0.2, 0.6, 0.8, 1))
        self.btn_copier.bind(on_press=self.on_copier)
        self.add_widget(self.btn_copier)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_generer(self, instance):
        mdp = generer_mot_de_passe(
            self.input_maitre.text,
            self.input_site.text,
            self.checkbox_symbols.active
        )
        self.result_label.text = mdp

    def on_copier(self, instance):
        Clipboard.copy(self.result_label.text)

class MDPApp(App):
    def build(self):
        self.title = "GenPASS - Générateur de MDP"
        return PasswordGenerator()

if __name__ == '__main__':
    MDPApp().run()
