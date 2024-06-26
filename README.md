# multilang_site

multilang_site est un projet Django conçu pour créer un site web simple et multilingue avec une gestion de contenu basique et des fonctionnalités avancées utilisant des modèles de langage (LLM). Ce projet met l'accent sur l'internationalisation, permettant de basculer entre plusieurs langues, et intègre des outils d'intelligence artificielle pour améliorer l'expérience utilisateur.

## Fonctionnalités

- **Internationalisation (i18n)** : Support de plusieurs langues (français et anglais).
- **Gestion des Articles de Blog** : Création, lecture et affichage des articles de blog.
- **Interface Utilisateur Multilingue** : Possibilité de changer la langue de l'interface utilisateur.
- **Chatbot Intégré** : Vue dédiée pour interragir avec un modèle de langage.

- Visiter le site : https://multilang-site-1.onrender.com

- 

## Instructions pour exécuter le projet

### Prérequis

Avant de démarrer, assurez-vous d'avoir installé les éléments suivants sur votre système :

- Python (version 3.x recommandée)
- Django
- pip (gestionnaire de paquets Python)
- Environnement virtuel (recommandé pour isoler les dépendances du projet)
  

### Installation des dépendances

Clonez le repository depuis GitHub :

```bash
git clone <lien_vers_votre_repository>
cd multilang_site

#Créez et activez votre environnement virtuel :

bash

python -m venv env
source env/bin/activate  # Pour Linux/Mac
env\Scripts\activate     # Pour Windows

#Installez les dépendances Python nécessaires à l'aide de pip en utilisant le fichier requirements.txt :

bash

pip install -r requirements.txt


#Configuration de l'application Django
#Configurez les variables d'environnement nécessaires. Créez un fichier .env à la racine du projet avec les informations sensibles :

dotenv

SECRET_KEY=your_secret_key_here
DEBUG=True

#Appliquez les migrations pour créer la structure de base de données :

bash

python manage.py migrate

#Chargez les données initiales si nécessaire :

bash

python manage.py loaddata initial_data

#Lancez le serveur de développement Django pour voir votre application en action :

bash

python manage.py runserver

