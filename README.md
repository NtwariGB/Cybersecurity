Projet : Détection de mots clés sensibles avec YARA en Python

Description :
Ce petit projet consiste à utiliser la bibliothèque YARA en Python pour détecter des mots clés sensibles dans un fichier texte. Il utilise des règles YARA personnalisées pour spécifier les motifs à rechercher dans le fichier. Le projet permet de charger ces règles, d'analyser un fichier texte donné et de détecter les correspondances avec les motifs définis. Il affiche ensuite les correspondances trouvées.

Fonctionnalités du projet :
- Chargement des règles YARA depuis un fichier
- Analyse d'un fichier texte pour détecter les correspondances
- Affichage des correspondances trouvées

Documentation :

1. Installation des dépendances :
   - YARA : La bibliothèque YARA doit être installée sur le système. 

2. Structure du projet :
   - main.py : Le fichier principal du projet contenant le code pour l'analyse des fichiers.
   - rules.yar : Un fichier texte contenant les règles YARA spécifiant les motifs à rechercher.

3. Configuration du projet :
   - Assurez-vous que la bibliothèque YARA est correctement installée sur votre système.
   - Placez le fichier "main.py" et le fichier de règles "rules.yar" dans le même répertoire.

4. Utilisation du projet :
   - Assurez-vous que le fichier à analyser est disponible.
   - Ouvrez le fichier "rules.yar" et définissez les motifs de recherche en utilisant la syntaxe YARA.
   - Exécutez le fichier "main.py" à l'aide de Python.
   - Le programme demandera le chemin du fichier à analyser. Fournissez le chemin complet du fichier.
   - Le programme analysera le fichier et affichera les correspondances trouvées.

5. Exemple d'utilisation :
   - Supposons que nous ayons un fichier texte "texte.txt" contenant du contenu sensible.
   - Dans le fichier "rules.yar", nous définissons les motifs de recherche, par exemple : 
     ```
     rule sensitive_keyword {
         strings:
             $keyword = "sensible"
         condition:
             $keyword
     }
     ```
   - Exécutez le fichier "main.py" et fournissez le chemin complet du fichier "texte.txt".
   - Le programme analysera le fichier et affichera les correspondances si le mot clé "sensible" est trouvé.
