echo -e "\nWelcome to sudoSU Installation. sudoSU is a Free Software package written using python, PyGObject and BASH. It is designed to utilize SeisUnix (SU) programs installed by user to process Seismic Data. t is developed for Linux based systems and supports Ubuntu 18.04 or higher and other Gnome based Linux Distributions. It provides user with an intuitive UI to execute multiple commands by just a few clicks instead of the tedious Command Line Interface for SeisUnix and knowledge of BASH scripting. It is a modular package and can be easily extended/modified by the end user. It can be used to develop a module for any linux command that can be run on terminal since it uses a Terminal Emulator to process the commands. It supports batch processing, Workflow creation and execution using BASH scripts for SU/SEGY files.\n"
echo "Hit return key to continue"  | tr -d "\012"
read RESP 
echo
	more ./LICENSE
echo
echo "By answering you agree to abide by the terms and conditions of the above License."| tr -d "\012"
while true; do
    read -p "Are you sure you want to continue? [y/n] " yn
    case $yn in
	[Yy]* ) 
		DEFAULT_PATH=$HOME/sudoSU
		echo -e "\nDefault Installation directory is $DEFAULT_PATH" 
		while true; do
    			read -p "Do you wish to change the directory? [y/n] " yn
    				case $yn in
					[Yy]* ) 
						echo "Input the directory Path: "
						read NEW_PATH
						FINAL_PATH=$NEW_PATH; break;;
       					[Nn]* ) FINAL_PATH=$DEFAULT_PATH; break;;
       					 * ) echo "Please answer y or n.";;
    				esac
		done
	echo  "moving necessary files to $FINAL_PATH ..."
	mkdir $FINAL_PATH
	cp -r ./bin $FINAL_PATH
	cp -r ./LICENSE $FINAL_PATH
	cp -r ./README.md $FINAL_PATH
	#cp config_format.txt $FINAL_PATH
	echo  "Done Moving..."
	cd $FINAL_PATH
	echo "Setting up sudoSU..."
	sleep 1
	echo "Creating Terminal Command 'sudoSU'..."
	echo "python3 $FINAL_PATH/bin/main/sudoSU.py">> sudoSU.sh
	sudo chmod +x sudoSU.sh
	if [ -d ~/bin ] 
	then
	     mv sudoSU.sh $HOME/bin/sudoSU
	else
	    mkdir ~/bin
	    mv sudoSU.sh $HOME/bin/sudoSU
	fi
	sleep 1
	echo "Moved terminal command 'sudoSU' to $HOME/bin..."
	sleep 1
	echo "Creating 'Projects' Directory"
	mkdir Projects
	sleep 1
	echo "Creating Configuration File..."
	echo -e "$FINAL_PATH\n$FINAL_PATH/Projects/\n1\n1000\n700">>main_config.txt
	sleep 1
	echo "Configuration File created..."
	sleep 1
	echo "Creating App Launcher File..."
	echo -e "[Desktop Entry]\n
	Name=sudoSU\n
	Comment=Seismic Data Processing environment\n
	Exec=$HOME/bin/sudoSU\n
	Type=Application\n
	Terminal=false\n
	Icon=$FINAL_PATH/bin/main/icon.png\n
	NoDisplay=false\n">>sudoSU.desktop
	sleep 1
	echo "Moving App Launcher... "
	sudo chmod +x sudoSU.desktop
	mv sudoSU.desktop $HOME/.local/share/applications/sudoSU.desktop
	sleep 1
	echo "App Launcher created..."
	sleep 2
	echo "sudoSU Installation Complete..."; break;;
[Nn]* ) exit;;
* ) echo "Please answer y or n.";;
esac
done


