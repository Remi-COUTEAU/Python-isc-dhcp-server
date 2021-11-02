# Python-isc-dhcp-server

RÔLE:

Installation isc-dhcp-server

EXIGENCES:

Valable uniquement pour serveur ubuntu 18.04
posséder une interface reseau d'écoute

DEROULEMENT:

1 Le script vérifie si isc-dhcp-server est installé.
  2.1 Si il est installé alors il est possible de le désinstaller (ATTENTION car la désinstallation entraine un redémarrage du server).
  2.2 Si il n'est pas installé, il est possible de l'installer.
    3 Le script demandera de choisir l'interface d'ecoute du server dhcp.
    4 Le script demandera de renseigner les adresses: reseau, masque, plage d'adresses, dns, passerelle.
    5 Pour finir, le script vous confirme le bon fonctionnement du service.


