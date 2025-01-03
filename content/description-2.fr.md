### Fonctionnalités principales (voir aussi [Tutoriels](tutorials))

- **Support des types de données**
    - Weasis fournit une implémentation très détaillée de la norme DICOM, permettant une visualisation et une interaction faciles avec la plupart des types de fichiers DICOM.
    - Affichage de la plupart des fichiers DICOM, y compris multi-trame, enhanced, MPEG-2, MPEG-4, MIME Encapsulation, DOC, SR, PR, KOS, SEG, AU, RT et ECG
    - Affichage des images DICOM contenant des données float ou double (Carte paramétrique)
    - Import de fichiers DICOM avec DICOM Query/Retrieve (C-GET, C-MOVE et WADO-URI) et DICOMWeb (QUERY et RETRIEVE)
    - Importation et exportation de CD/DVD DICOM avec DICOMDIR
    - Importation et exportation de fichiers DICOM ZIP
    - Support des formats d'image courants (TIFF, BMP, GIF, JPEG, PNG, RAS, HDR et PNM)

- **Exportation des données**
    - Exportation de fichiers DICOM localement avec plusieurs options (DICOMDIR, ZIP, fichier image ISO avec Weasis, TIFF, JPEG, PNG...)
    - Envoi de fichiers DICOM à un PACS distant ou serveur DICOMWeb (C-STORE ou STOW-RS)
    - Sauvegarde des mesures et annotations dans des DICOM Presentation States ou fichier XML

- **Affichage et rendu d'images**
    - Support de plusieurs écrans avec des calibrations différentes, support des écrans HiDPI (Haute Densité de Pixels), mode plein écran
    - Manipulation des images avec les boutons de la souris (déplacement, zoom, fenêtrage, rotation, défilement, réticule)
    - Support des Modality LUT, des VOI LUT, et des Presentation State LUT (même non linéaires)
    - Application des DICOM Presentation State (GSPS) et affichage des graphiques en superpositions
    - Support des superpositions DICOM, Shutter et DICOM Pixel Padding
    - Rendu volumétrique en 3D
    - Dispositions pour comparer des séries ou des études
    - Options avancées de synchronisation des séries
    - Affichage des lignes de coupe
    - Curseur 3D
    - Reconstruction multi-planaire oblique (MPR)
    - Projection d'Intensité Maximale
    - Loupe persistante

- **Outils de mesure et d'annotation**
    - Mesure de longueur, aire et angle
    - Statistiques régionales des pixels (Min, Max, Moyenne, Écart-type, Asymétrie, Kurtosis, Entropie)
    - Histogramme des valeurs de modalité
    - Mesure SUV

- **Visionneuses spécifiques**
    - DICOM ECG : affichage de toutes les formes d'onde DICOM et réalisation de certaines mesures
    - DICOM SR : visionneuse de rapports structurés avec des hyperliens vers des images et graphiques associés
    - DICOM AU : lecteur audio (permet l'exportation en fichiers WAV)

- **Autres outils**
    - Module Dicomizer pour convertir des images standards en DICOM
    - Impression de vues au format DICOM et sur imprimantes système
    - Application et création de Sélection d’images clés en sélectionnant des images avec le bouton étoile
    - Affichage et recherche dans tous les attributs DICOM
    - Outils DICOM RT pour la radiothérapie : affichage des ensembles de structure RT, des doses et graphiques DVH
