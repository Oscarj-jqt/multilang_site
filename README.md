# multilang_site

multilang_site est un projet Django conçu pour créer un site web simple et multilingue avec une gestion de contenu basique et des fonctionnalités avancées utilisant des modèles de langage (LLM). Ce projet est axé sur l'internationalisation, permettant de basculer entre plusieurs langues, et intègre des outils d'intelligence artificielle pour améliorer l'expérience utilisateur.

## Fonctionnalités

- **Internationalisation (i18n)** : Support de plusieurs langues (français et anglais).
- **Gestion des Articles de Blog** : Création, lecture et affichage des articles de blog.
- **Interface Utilisateur Multilingue** : Possibilité de changer la langue de l'interface utilisateur.
- **Chatbot Intégré** : Vue dédiée pour interragir avec un modèle de langage.


 Visiter le site : https://multilang-site-1.onrender.com
 

## Instructions pour exécuter le projet

### Installation des dépendances

Clonez le repository depuis GitHub :

```bash
git clone https://github.com/Oscarj-jqt/multilang_site

#Installez les dépendances Python nécessaires à l'aide de pip en utilisant le fichier requirements.txt :

pip install -r requirements.txt



python manage.py loaddata initial_data

#Lancez le serveur de développement Django pour voir votre application en action :


python manage.py runserver

