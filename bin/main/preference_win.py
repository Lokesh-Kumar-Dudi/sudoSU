import ntpath
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from pathlib import Path

# makes a builder to make GUI rom xml glade file
#makes the preference window, sets geometry,and connects 
# delete signal and rest of the signals from glade 
# file to their handlers
class preference_window():

    def __init__(self,parent):

        self.parent = parent
        self.data  = self.parent.props.main_config_data
        self.run=1
        self.glade_file=str(Path(__file__).parent / "preference_win.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.window2 = self.builder.get_object("preference_window ") 
        self.builder.connect_signals(self)
           
        self.builder.get_object("width").set_text(str(self.data[3].rstrip()))
        self.builder.get_object("height").set_text(str(self.data[4].rstrip()))
        self.builder.get_object("project_dir").set_text(self.parent.props.sudoSU_projects) 
        if int(self.data[2])==1:
            self.builder.get_object("dark_theme").set_active(True) 

        self.window2.show_all()

    def select_project_dir(self,widget):
        dialog = Gtk.FileChooserDialog(title="Please choose a Folder", parent=None,
                                        action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL, 2, "Select", 1)
        response = dialog.run()
        if response == 1:
            self.builder.get_object("project_dir").set_text(dialog.get_filename())
            self.parent.props.sudoSU_projects = dialog.get_filename()+"/"
            self.data[1]=dialog.get_filename()+"/"

        elif response == 2:
            pass
        dialog.destroy()

    def close(self,widget):
        self.window2.destroy()
    
    def get_size(self,widget):
        self.parent.props.width,self.parent.props.height = self.parent.window.get_size()
        self.builder.get_object("width").set_text(str(self.parent.props.width))
        self.builder.get_object("height").set_text(str(self.parent.props.height))
        self.data[3],self.data[4]=self.parent.props.width,self.parent.props.height
    
    def set_dark(self,widget):
        self.settings = Gtk.Settings.get_default()  
        if self.builder.get_object("dark_theme").get_active():
            self.settings.set_property("gtk-application-prefer-dark-theme", True)
        else:
            self.settings.set_property("gtk-application-prefer-dark-theme", False)


    
    def set_preference(self,widget): 
        self.parent.window.resize(int(self.parent.props.width),int(self.parent.props.height)) 
        text=self.builder.get_object("project_dir").get_text()
        if text[len(text)-1]=='/':
            self.data[1]  = text
        else:
            self.data[1]=text+'/'

        if self.builder.get_object("dark_theme").get_active():
            self.data[2]="1"
        else:
            self.data[2]="0"
        self.data[3]=self.builder.get_object("width").get_text()
        self.data[4]=self.builder.get_object("height").get_text()
        self.parent.props.write_properties(self.data)
        
        


        


