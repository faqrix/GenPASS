import hmac
import hashlib
import string
import webbrowser

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

Window.clearcolor = (44/255, 62/255, 80/255, 1)  # #2c3e50
Window.set_title("GenPASS")

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

    return mot_de_passe[:longueur]

class PasswordGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=20, **kwargs)
        self.size_hint = (1, 1)  # ou laisse par défaut pour que size_hint_y fonctionne
        self.pos_hint = {"center_x": 0.5}

        with self.canvas.before:
            Color(52/255, 73/255, 94/255, 1)  # #34495e
            self.bg = RoundedRectangle(radius=[20], size=self.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        self.add_widget(Label(text="GenPASS - Générateur de Mot de Passe",
                              font_size=28, color=(1, 1, 1, 1), size_hint_y=None, height=40))

        # Mot de passe maître
        self.add_widget(Label(text="Mot de passe maître", color=(1, 1, 1, 1)))
        self.input_maitre = TextInput(password=True, multiline=False, font_size=18, size_hint_y=None, height=45,
                                      background_color=(1,1,1,1), foreground_color=(0,0,0,1))
        self.add_widget(self.input_maitre)

        # Nom du site / clé
        self.add_widget(Label(text="Nom du site / clé", color=(1, 1, 1, 1)))
        self.input_site = TextInput(multiline=False, font_size=18, size_hint_y=None, height=45,
                                    background_color=(1,1,1,1), foreground_color=(0,0,0,1))
        self.add_widget(self.input_site)

        # Checkbox + label
        symbol_line = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        self.checkbox_symbols = CheckBox(active=True)
        symbol_line.add_widget(self.checkbox_symbols)
        symbol_line.add_widget(Label(text="Inclure des symboles", color=(1, 1, 1, 1)))
        self.add_widget(symbol_line)

        # Résultat
        self.result_label = Label(text="", font_size=22, bold=True, halign='center',
                                  valign='middle', color=(1, 1, 1, 1))
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.add_widget(self.result_label)

        # Boutons
        self.btn_generer = self.make_button("Générer", self.on_generer)
        self.add_widget(self.btn_generer)

        self.btn_copier = self.make_button("Copier", self.on_copier)
        self.add_widget(self.btn_copier)

        # Footer
        self.footer = Button(
            text="Développé avec ❤️ par faqrix",
            size_hint_y=None,
            height=40,
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 0.6),
            font_size=14
        )
        self.footer.bind(on_press=lambda *_: webbrowser.open("https://github.com/faqrix/GenPASS"))
        self.add_widget(self.footer)

    def make_button(self, text, callback):
        btn = Button(
            text=text,
            font_size=18,
            size_hint_y=None,
            height=50,
            background_normal='',
            background_color=(52/255, 152/255, 219/255, 1),  # #3498db
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=callback)
        return btn

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def on_generer(self, instance):
        mdp = generer_mot_de_passe(
            self.input_maitre.text,
            self.input_site.text,
            self.checkbox_symbols.active
        )
        if not mdp:
            self.result_label.text = "[color=ffaaaa]Veuillez entrer un mot de passe maître et un nom de site.[/color]"
        else:
            self.result_label.text = mdp

    def on_copier(self, instance):
        Clipboard.copy(self.result_label.text)

class GenPASSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        layout.add_widget(PasswordGenerator(size_hint_y=0.5))  # occupe moitié écran
        layout.add_widget(Widget(size_hint_y=0.5))  # vide en dessous pour clavier
        return layout


if __name__ == '__main__':
    GenPASSApp().run()
