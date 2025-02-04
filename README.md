# WiFi Security Scanner

## Description
Ce projet est une application Python avec interface graphique qui permet d'analyser les réseaux WiFi à proximité et de détecter les éventuelles failles de sécurité. Il utilise `nmcli` pour récupérer les informations sur les réseaux et affiche les résultats de manière intuitive.

## Fonctionnalités
- Scanner les réseaux WiFi disponibles
- Afficher le SSID, la puissance du signal et le type de sécurité
- Alerter l'utilisateur si un réseau utilise WEP ou n'a aucune sécurité

## Prérequis
- Python 3.x
- `nmcli` installé (présent par défaut sur Linux)
- Tkinter (installé avec Python standard sur la plupart des systèmes)

## Installation
1. Clonez ce dépôt :
   ```sh
   git clone https://github.com/votre-repo/wifi-security-scanner.git
   cd wifi-security-scanner
   ```
2. Exécutez le script Python :
   ```sh
   python wifi_security_analysis.py
   ```

## Utilisation
1. Lancez l'application.
2. Cliquez sur le bouton "Scan WiFi".
3. Consultez la liste des réseaux disponibles avec leur niveau de sécurité.
4. Si un réseau vulnérable est détecté, un message d'alerte s'affiche.

## Remarque
- Ce programme fonctionne principalement sous Linux (Ubuntu, Debian, etc.) en raison de l'utilisation de `nmcli`.
- Pour Windows, il faudrait adapter le script en utilisant `netsh wlan show networks` au lieu de `nmcli`.

## Avertissement
Ce projet est destiné à une utilisation personnelle et éducative. Ne tentez pas d'accéder à des réseaux sans autorisation.

