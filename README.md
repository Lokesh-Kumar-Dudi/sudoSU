&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***sudoSU*** is a Free Software package written using [python](https://www.python.org/), [PyGObject](https://pygobject.readthedocs.io/en/latest/) and **BASH**. It is designed to utilize [SeisUnix (SU)](https://github.com/JohnWStockwellJr/SeisUnix/wiki) programs installed by user to process **Seismic Data**. t is developed for Linux based systems and  supports **Ubuntu 18.04 or higher** and other **Gnome** based **Linux** Distributions. It provides user with an intuitive UI to execute multiple commands by just a few clicks instead of the tedious Command Line Interface for ***SeisUnix*** and knowledge of BASH scripting. It is a modular package and can be easily extended/modified by the end user. It can be used to develop a module for any linux command that can be run on terminal since it uses a [Terminal Emulator](https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal)  to process the commands. It supports batch processing, Workflow creation and execution using **BASH** scripts for SU/SEGY files.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This Project started as a result of my desire to learn **python** and evolved over time from simple **tkinter** project to what it is now.  If you have any Suggetions, Queries or Bug reports get in touch with me at my [linkedin profile](https://www.linkedin.com/in/lokesh-kumar-3b4589163).

Follow the steps Described below to install and run sudoSU:

1. Open a terminal execute the following command:  
'bash install.sh'  
2. Follow the instructions on terminal and finish installation  
3. Open sudoSU from terminal anywhere in the system by executing the following Command:   
'sudoSU'  
**or**  
4. An App Shortcut will also be added to your Apps, search sudoSU and run it from there.  
**or**
5. Go to the '{installation directory}/bin/main' and and execute the following command:  
'python3 sudoSU.py'
6. Do not edit main_config.txt under any circumstance unless you know what you are doing.

Checkout the Documentation to learn How to Use sudoSU.


