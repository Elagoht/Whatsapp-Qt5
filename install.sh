#!/usr/bin/bash
if [ "$EUID" -ne 0 ]
	then echo "Please run under root privileges."
else 
	sudo mkdir -p /usr/share/Whatsapp-Qt5
	sudo cp icon.png /usr/share/Whatsapp-Qt5 
	sudo cp Whatsapp /usr/share/Whatsapp-Qt5
	sudo chmod +x /usr/share/Whatsapp-Qt5/Whatsapp
	sudo echo "#!/usr/bin/bash
cd /usr/share/Whatsapp-Qt5/
./Whatsapp" > /usr/bin/whatsapp-qt5
	sudo chmod +x /usr/bin/whatsapp-qt5
	sudo echo "[Desktop Entry]
Name=Whatsapp
Comment=Whatsapp client made with PyQt5 by Elagoht.
Exec=whatsapp-qt5
Icon=/usr/share/Whatsapp-Qt5/icon.png
Terminal=false
Type=Application
Categories=Network"	> /usr/share/applications/Whatsapp.desktop
fi