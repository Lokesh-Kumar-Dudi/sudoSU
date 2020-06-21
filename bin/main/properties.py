from pathlib import Path
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

class properties():
    def __init__(self):
        self.home= str(Path.home())
        self.main_configfile = str(Path(__file__).parent.parent / "../main_config.txt")
        self.file1 = open(self.main_configfile, 'r')
        self.main_config_data = self.file1.readlines()
        self.file1.close()
        self.default_path = self.main_config_data[0]
        self.default_path = self.default_path.rstrip()
        self.sudoSU_projects = self.main_config_data[1].rstrip()
        self.UiPath = self.default_path+"/bin/"
        self.width = int(self.main_config_data[3])
        self.height = int(self.main_config_data[4])
        self.settings = Gtk.Settings.get_default()  
        if (int(self.main_config_data[2]) == 1):
            self.settings.set_property("gtk-application-prefer-dark-theme", True)            # settings.set_property("gtk-theme-name", "Adwaita-dark")     
        else:
            self.settings.set_property("gtk-application-prefer-dark-theme", False)
        self.curr_project = None
        self.new_project = " "
        self.segy_file = None
        self.tape = " "
    
    def write_properties(self,data):
        with open(self.main_configfile,'w'): pass
        file = open(self.main_configfile,"r+")
        lis = [str(i).rstrip() for i in data]
        for i in lis:
            file.writelines(i+"\n")
        file.close()
