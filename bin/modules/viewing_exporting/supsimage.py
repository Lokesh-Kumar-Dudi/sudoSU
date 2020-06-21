import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from pathlib import Path
import ntpath
import os

class supsimage(Gtk.Box):
    def __init__(self,parent):
        self.parent = parent
        self.glade_file=str(Path(__file__).parent/ "supsimage.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.main_box = self.builder.get_object("supsimage")
        self.title_box = self.builder.get_object("tab_title")
        self.builder.connect_signals(self)
        self.list = ['label1','label2','title','titlecolor','perc',"clip"]
        self.perc = self.builder.get_object("perc")
        #self.perc.set_text("99")
        self.output_files = self.builder.get_object("output_files")


    def set_parameters(self, button):
        self.parameters=""
        for item in self.list:
            obj = self.builder.get_object(item)
            if type(obj)==type(Gtk.Entry()):
                if obj.get_text()!="":
                    self.parameters+=item+'="'+obj.get_text()+'" '
                else:
                    pass
            elif type(obj)==type(Gtk.CheckButton()):
                if obj.get_active():
                    self.parameters+=item+"="+"1 "
                else:
                    pass
        if self.parameters!="":
            self.command = "supsimage < infile "+ self.parameters + " >" + "outfile"
            self.parent.send_command(self.command,1)
        else:
            self.parent.send_message("No Parameters choosen",1)
        self.temp = self.output_files.get_text()
        if self.temp!="":
            self.parent.output_files = self.temp.split(',')
        else:
            self.parent.send_message("No Output File names given",1)
    
    def run(self, widget):
        if self.parent.input_files==[]:
                self.parent.send_message("No Input Files selected",1)
                return True
        if len(self.parent.input_files)==len(self.parent.output_files):
            self.parent.console.set_current_page(2)
            for i,input_file in enumerate(self.parent.input_files):
                cmd = "supswigb"+ " < " + input_file + " "+self.parameters \
                    +" > "+self.parent.output_files[i]
                self.parent.terminal.run_command(cmd+"\n")
                self.parent.history.append(cmd)
            self.parent.refresh_file_ex(self.parent.props.curr_project)  
        else: 
            self.parent.send_message("No. of Output Files not equal to No. of Input Files",1)
    
    def refresh(self, widget):
        self.parameters=""
        for item in self.list:
            obj = self.builder.get_object(item)
            if type(obj)==type(Gtk.Entry()):
                obj.set_text("")
            elif type(obj)==type(Gtk.CheckButton()):
                obj.set_active(False)
        self.perc.set_text("99")
        
    
    def append(self,widget):
        pass


    def help(self, widget):
        builder = Gtk.Builder()
        builder.add_from_file(self.glade_file)
        help_dlg = builder.get_object("help")
        help_dlg.set_title("SUPSIMAGE Help")
        help_dlg.show_all()
        

    def destroy(self, widget):
        self.main_box.destroy()
        self.parent.tabs['SUPSIMAGE'] = 0


class nb_page(Gtk.Box):
    def __init__(self,parent):
        self.main_class = supsimage(parent)
        self.page = self.main_class.main_box
        self.title = self.main_class.title_box  
