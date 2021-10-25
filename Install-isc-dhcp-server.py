#!/usr/bin/env python3
import apt
import os
#Fonction vérification presence service isc-dhcp-server
def verification():
    isc = 'isc-dhcp-server'
    cache = apt.Cache()
    isc_installe = False

    if isc in cache:
        isc_installe = cache[isc].is_installed
    if isc_installe == True:
        print("##############################")
        print("#isc-dhcp-server est installé#")
        print("############################## \n")
    else:
        print("####################################")
        print("#isc-dhcp-server n'est pas installé#")
        print("#################################### \n")

#Fonction installation server dhcp
def installation():
    install = "sudo apt-get -y -qq install isc-dhcp-server"
    os.system(install)

#Fonction de désinstallation isc-dhcp-server
def desinstallation():
    remove = "sudo apt-get --purge -qq remove isc-dhcp-server"
    os.system(remove)

# Fonction creation d'un nouveau fichier dhcpd.conf et deplacement de l'ancien
def deplacefile1():
    deplace = "mv dhcpd.conf dhcpd.conf.origin"
    nouveau = "touch /etc/dhcp/dhcpd.conf"
    os.system(deplace)
    os.system(nouveau)

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

#desinstallation()
installation()
verification()
configfile1()
#restartservice()
