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
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": 0.5}

        with self.canvas.before:
            Color(52/255, 73/255, 94/255, 1)  # #34495e
            self.bg = RoundedRectangle(radius=[20], size=self.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Titre avec retour à la ligne automatique
        self.title = Label(
            text="GenPASS - Générateur de Mot de Passe",
            color=(1, 1, 1, 1),
            size_hint_y=None,  # Permet à la taille de s'ajuster dynamiquement
            height=40,  # Taille initiale du titre
            halign='center',  # Alignement horizontal
            valign='middle',  # Alignement vertical
            text_size=(self.width - 40, 200)  # Largeur dynamique du texte avec retour à la ligne
        )

        self.add_widget(self.title)

        self.label_maitre = Label(text="Mot de passe maître", color=(1, 1, 1, 1))
        self.add_widget(self.label_maitre)

        self.input_maitre = TextInput(password=True, multiline=False, background_color=(1, 1, 1, 1),
                                      foreground_color=(0, 0, 0, 1), size_hint_y=None)
        self.add_widget(self.input_maitre)

        self.label_site = Label(text="Nom du site / clé", color=(1, 1, 1, 1))
        self.add_widget(self.label_site)

        self.input_site = TextInput(multiline=False, background_color=(1, 1, 1, 1),
                                    foreground_color=(0, 0, 0, 1), size_hint_y=None)
        self.add_widget(self.input_site)

        # Checkbox
        symbol_line = BoxLayout(orientation='horizontal', size_hint_y=None)
        self.symbol_label = Label(text="Inclure des symboles", color=(1, 1, 1, 1))
        symbol_line.add_widget(self.symbol_label)
        self.checkbox_symbols = CheckBox(active=True)
        symbol_line.add_widget(self.checkbox_symbols)
        self.add_widget(symbol_line)

        # Résultat
        self.result_label = Label(text="", bold=True, halign='center', valign='middle',
                                  color=(1, 1, 1, 1), size_hint_y=None)
        self.result_label.bind(size=self.result_label.setter('text_size'))
        self.add_widget(self.result_label)

        self.btn_generer = self.make_button("Générer", self.on_generer)
        self.add_widget(self.btn_generer)

        self.btn_copier = self.make_button("Copier", self.on_copier)
        self.add_widget(self.btn_copier)

        self.footer = Button(
            text="Développé par faqrix",
            size_hint_y=None,
            background_normal='',
            background_color=(0, 0, 0, 0),
            color=(1, 1, 1, 0.6)
        )
        self.footer.bind(on_press=lambda *_: webbrowser.open("https://github.com/faqrix/GenPASS"))
        self.add_widget(self.footer)

        # Responsive
        self.bind(size=self.on_layout_resize)

    def responsive_font(self, percent):
        return self.height * percent

    def responsive_height(self, percent):
        return self.height * percent


    def make_button(self, text, callback):
        btn = Button(
            text=text,
            background_normal='',
            background_color=(52/255, 152/255, 219/255, 1),
            color=(1, 1, 1, 1),
            size_hint_y=None
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

    def on_layout_resize(self, *args):
        rf = self.responsive_font
        rh = self.responsive_height

        self.title.font_size = rf(0.05)
        self.title.height = rh(0.1)
        self.title.text_size = (self.width - 40, None)

        self.label_maitre.font_size = rf(0.03)
        self.label_maitre.height = rh(0.05)
        self.input_maitre.font_size = rf(0.04)
        self.input_maitre.height = rh(0.06)

        self.label_site.font_size = rf(0.03)
        self.label_site.height = rh(0.05)
        self.input_site.font_size = rf(0.04)
        self.input_site.height = rh(0.06)

        self.symbol_label.font_size = rf(0.03)
        self.checkbox_symbols.size = (rh(0.04), rh(0.04))

        self.result_label.font_size = rf(0.04)
        self.result_label.height = rh(0.09)

        self.btn_generer.font_size = rf(0.035)
        self.btn_generer.height = rh(0.1)

        self.btn_copier.font_size = rf(0.035)
        self.btn_copier.height = rh(0.1)

        self.footer.font_size = rf(0.025)
        self.footer.height = rh(0.07)



class GenPASSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        layout.add_widget(PasswordGenerator())
        return layout


if __name__ == '__main__':
    GenPASSApp().run()
