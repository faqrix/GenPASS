# GenPASS - Générateur de Mots de Passe

GenPASS est une application permettant de générer des mots de passe sécurisés. L'application propose une version mobile pour Android (au format APK) et une version PC disponible dans le dossier `dist` de ce dépôt.

## Fonctionnalités
- Génération de mots de passe aléatoires et sécurisés.
- Personnalisation du mot de passe avec des options pour :
  - La longueur du mot de passe.
  - L'inclusion de symboles spéciaux.
  - L'inclusion de majuscules et minuscules.
  - L'inclusion de chiffres.

### Fonctionnement du générateur :
Les mots de passe sont générés à partir de deux éléments :
1. **Mot de passe maître** : Un mot de passe sécurisé que tu choisis et que tu retiens.
2. **Mot clé** : Par exemple, le nom d'un site (ex : "example.com").

Le mot de passe généré est **toujours le même** pour une combinaison de mot de passe maître et de mot clé (site). Cela signifie que tu n'as plus besoin d'enregistrer de mots de passe pour chaque site. Il te suffit de retenir ton mot de passe maître et d'entrer le mot clé (nom du site) pour obtenir le mot de passe correspondant. Les mots de passe **ne sont pas enregistrés** nulle part, assurant ainsi la confidentialité.

## Installation

### 1. Version Mobile (APK pour Android)
L'application mobile est disponible sous forme de fichier APK que tu peux installer sur ton appareil Android. Voici les étapes pour installer l'APK :

#### Étapes d'installation :
1. Télécharge l'APK depuis le lien suivant :
   - Télécharger [GenPASS APK](lien_vers_ton_apk_github)

2. Autorise l'installation d'applications à partir de sources inconnues dans les paramètres de ton appareil Android :
   - Va dans **Paramètres > Sécurité** (ou **Paramètres > Applications** selon ta version Android).
   - Active l'option **Installer des applications depuis des sources inconnues**.

3. Ouvre le fichier APK téléchargé et clique sur **Installer**.

4. Une fois l'installation terminée, tu peux ouvrir **GenPASS** et commencer à générer des mots de passe sécurisés.

### 2. Version PC (Disponible dans le dossier `dist`)
La version PC de l'application est disponible dans le dossier `dist` du projet. Cette version peut être exécutée sur des systèmes d'exploitation comme Windows, Linux ou macOS.

#### Étapes pour la version PC :
1. Navigue vers le dossier `dist` de ce dépôt.
2. Télécharge le fichier correspondant à ton système d'exploitation (par exemple, `GenPASS.exe` pour Windows ou `GenPASS.app` pour macOS).
3. Installe l'application en suivant les instructions spécifiques à ton système d'exploitation :
   - Pour **Windows**, exécute le fichier `.exe`.
   - Pour **Linux**, exécute le fichier binaire ou utilise les commandes appropriées pour installer l'application.

4. Une fois l'installation terminée, tu peux lancer **GenPASS** depuis ton menu d'applications ou en double-cliquant sur le fichier exécutable.

## Utilisation

### Générer un mot de passe
1. Ouvre l'application (Android ou PC).
2. Personnalise tes préférences :
   - Choisis la longueur du mot de passe.
   - Sélectionne si tu veux inclure des symboles, des chiffres, des majuscules, etc.
3. Clique sur **"Générer"** pour obtenir un mot de passe sécurisé.
4. Copie le mot de passe dans ton presse-papier ou utilise-le directement.

#### Exemple :
- Longueur : 16 caractères
- Inclure des symboles : Oui
- Inclure des chiffres : Oui

**Résultat** : A8*Xb#v3dH!L9t!q

---

**Note** : Le mot de passe généré est unique pour chaque combinaison de mot de passe maître et de mot clé, ce qui te permet de n'avoir qu'un seul mot de passe maître à retenir pour accéder à tous tes sites en toute sécurité.

