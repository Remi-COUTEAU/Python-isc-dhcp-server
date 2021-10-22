#!/usr/bin/env python3
import os

#Fonction installation server dhcp
def installation():
    install = "sudo apt-get -y -qq install isc-dhcp-server"
    os.system(install)

#Fonction configuration du fichier isc-dhcp-server
def configfile1():
    #Récuperation du nom de l'interface d'ecoute du server dhcp
    interface = input("Entrer le nom de l'interface Internet: \n")

    #Déclaration des variables
    texte = ["DHCPDv4_CONF=/etc/dhcp/dhcpd.conf", "INTERFACESv4=", " \n", '"']
    texte1 = texte[0] + texte[2]
    texte2 = texte[1] + texte[3] + interface + texte[3] + texte[2]

    #Modification du fichier
    file = open("/etc/default/isc-dhcp-server", 'r')
    list = file.readlines()
    file.close()
    list[3] = texte1
    list[16] = texte2
    file = open("/etc/default/isc-dhcp-server", "w")
    file.writelines(list)
    file.close()

#Fonction configuration du fichier dhcpd.conf
#Fonction redémarrage du server dhcp
def restartservice():
    restart = "systemctl restart isc-dhcp-server"
    os.system(restart)

#installation()
#configfile1()
#restartservice()
