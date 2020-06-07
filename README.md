# graph-text

Attention: le PageRank n'a pas de sens pour un graphe non-orienté!! Trouver un Ersatz

### Liste des features à utiliser :
* Features indépendants de la structure :
  * Nombre de mots en commun dans le titre
  * Nombre de mots en commun dans l'abstract (éventuellement avec tf-idf et/ou stemming) (Aurélien)
  * Ecart en années entre les dates de publication
  * Nombre d'auteurs en commun
* Features de structure :
  * local edge/node connectivity entre les sommets (mathieu)
  * nombre de voisins en commun (éventuellement normalisé par le nombre total de voisins de chaque sommet) (Aurélien)
  * Pagerank de chaque sommet (mathieu)
  * Nombre de voisins de chaque sommet (mathieu)
  * Appartenance ou non au même cluster 
* On compte également faire un graphe des auteurs pour intégrer des features supplémentaires : (Clément et Julien)
  * Pagerank (éventuellement pagerank maximal si plusieurs auteurs) de chaque auteur
  * Nombre total de citations de chaque auteur
  * Appartenance ou non au même cluster d'auteurs
