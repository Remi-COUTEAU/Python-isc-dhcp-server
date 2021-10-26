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
    return isc_installe

#Fonction installation server dhcp
def installation():
    install = "sudo apt-get -y -qq install isc-dhcp-server"
    os.system(install)

#Fonction de désinstallation isc-dhcp-server
def desinstallation():
    remove = "sudo apt-get --purge -qq remove isc-dhcp-server"
    os.system(remove)

#Fonction configuration du fichier etc/default/isc-dhcp-server
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

# Fonction creation d'un nouveau fichier dhcpd.conf et deplacement de l'ancien
def file2():
    deplace = "mv /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.origin"
    nouveau = "touch /etc/dhcp/dhcpd.conf"
    os.system(deplace)
    os.system(nouveau)

#Fonction configuration du fichier dhcpd.conf
def configfile2():
    #Récuperation des valeurs
    liste = ["subnet", "netmask", "rangedebut", "rangefin", "dns", "netmask", "router", "broadcast"]
    valeur = []
    i = 0
    while i < 8:
        val = input("Entrer l'adresse du: " + liste[i] + " : \n")
        valeur.append(val)
        i = i + 1
    #Edition du fichier dhcpd.conf
    fichier = open("/etc/dhcp/dhcpd.conf",'wt')
    fichier.writelines(["#dhcpd.conf \n\n", "authoritative; \n", "ddns-update-style none; \n", "log-facility local7; \n\n"])
    fichier.write("subnet " + valeur[0] + " netmask " + valeur[1] + " { \n")
    fichier.write("  range " + valeur[2] + " " + valeur[3] + "; \n")
    fichier.write("  option domain-name-servers " + valeur[4] + "; \n")
    fichier.write("  option subnet-mask " + valeur[5] + "; \n")
    fichier.write("  option routers " + valeur[6] + "; \n")
    fichier.write("  option broadcast-address " + valeur[7] + "; \n")
    fichier.writelines(["  default-lease-time 86400; \n", "  max-lease-time 86400; \n", "}"])
#Fonction redémarrage du server dhcp
def restartservice():
    restart = "systemctl restart isc-dhcp-server"
    status = "systemctl status isc-dhcp-server"
    os.system(restart)
    os.system(status)

#Fonction redemarrage du poste
def reboot():
    reboot = "sudo reboot"
    os.system(reboot)

#Déroulement du script
def main():

    relance = 1
    while relance == 1:
        verif = verification()
        if verif == True:
            x = 0
            while x == 0:
                desinstall = input("voulez-vous desinstaller isc-dhcp-server (y pour oui, n pour non, q pour quitter):\nATENTION la desinstallation entraine un redémarrage du poste\n")
                if desinstall == 'y':
                    desinstallation()
                    reboot()
                    x = 1
                elif desinstall == 'n':
                    print("votre réponse est non\n")
                    x = 1
                elif desinstall == 'q':
                    x = 1
                    relance = 2
                else:
                    print("votre réponse n'est pas appropiée\n")
                    x = 0
        else:
            y = 0
            while y == 0:
                install = input("Voulez-vous installer isc-dhcp-server (y pour oui n pour non q pour quitter:)\n")
                if install == 'y':
                    installation()
                    configfile1()
                    file2()
                    configfile2()
                    restartservice()
                    y = 1
                    print("L'installation est terminée\n")
                elif install == 'n':
                    print ("Votre reponse est non \n")
                    y = 1
                elif install == 'q':
                    y = 1
                    relance = 2
                else:
                    print ("votre reponse n'est pas appropiée")
                    y = 0
    print ("fin du programme")

main()
