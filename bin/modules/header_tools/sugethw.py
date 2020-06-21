import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from pathlib import Path
import ntpath
import os

class sugethw(Gtk.Box):
    def __init__(self,parent):
        self.parent = parent
        self.glade_file=str(Path(__file__).parent / "sugethw.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.main_box = self.builder.get_object("sugethw")
        self.title_box = self.builder.get_object("tab_title")
        self.builder.connect_signals(self)
        self.output_files = self.builder.get_object("output_files")
        self.append_wf_cmd = ""
        self.parameters=""
    def set_parameters(self, button):
        self.parameters=""
        self.parameters = self.builder.get_object("keys").get_text()+" "
        obj = self.builder.get_object('output')
        tree_iter = obj.get_active_iter()
        if tree_iter is not None:
            model = obj.get_model()
            row_id = model[tree_iter][0]
            self.parameters +="output=" + row_id + " "
        self.command = "sugethw < infile "+ self.parameters + " >" + "outfile"
        self.append_wf_cmd ="sugethw < $infile "+ self.parameters + " >" + "$prefix.$infile"
        self.parent.send_command(self.command,1)

    
    def run(self, widget):
        self.temp = self.output_files.get_text()
        if self.temp!="":
            self.parent.output_files = self.temp.split(',')
        else:
            pass
        if self.parent.input_files==[]:
                self.parent.send_message("No Input Files selected",1)
                return True
        self.parent.console.set_current_page(2)
        for i,input_file in enumerate(self.parent.input_files):
            if self.parent.output_files!=[]:
                cmd = "sugethw"+ " < " + input_file + " "+self.parameters \
                    +" > "+self.parent.output_files[i]
            else:
                cmd = "sugethw"+ " < " + input_file + " "+self.parameters
            self.parent.terminal.run_command(cmd+"\n")
            self.parent.history.append(cmd)
        self.parent.refresh_file_ex(self.parent.props.curr_project)  
    
    def refresh(self, widget):
        self.append_wf_cmd=""
        self.parameters=""
        self.output_files.set_text("")
        self.parent.output_files=[]
        self.builder.get_object("keys").set_text("")
        
    
    def append(self,widget):
        if self.parent.props.curr_project!=None:
            if self.parameters!="":
                self.parent.workflow_append(self.append_wf_cmd,1)
            else:
                self.parent.send_message("No Parameters choosen",1)
        else:
            self.parent.send_message("Can not append command without opening a Project",1)

        
    def help(self, widget):
        builder = Gtk.Builder()
        builder.add_from_file(self.glade_file)
        help_dlg = builder.get_object("help")
        help_dlg.set_title("SUGETHW Help")
        help_dlg.show_all()
        

    def destroy(self, widget):
        self.main_box.destroy()
        self.parent.tabs['SUGETHW'] = 0

class nb_page(Gtk.Box):
    def __init__(self,parent):
        self.main_class = sugethw(parent)
        self.page = self.main_class.main_box
        self.title = self.main_class.title_box  
