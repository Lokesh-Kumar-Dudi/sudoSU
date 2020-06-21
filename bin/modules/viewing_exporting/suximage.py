import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from pathlib import Path
import ntpath
import os

class suximage(Gtk.Box):
    def __init__(self,parent):
        self.parent = parent
        self.glade_file=str(Path(__file__).parent/"suximage.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.main_box = self.builder.get_object("suximage")
        self.title_box = self.builder.get_object("tab_title")
        self.builder.connect_signals(self)
        self.list = ['label1','label2','title','labelcolor','titlecolor','perc',
                    'clip','cmap','units','legend','balance']
        self.perc = self.builder.get_object("perc")
        self.append_wf_cmd = ""
        self.parameters=""


    def set_parameters(self, button):
        self.parameters=""
        obj = self.builder.get_object('key')
        tree_iter = obj.get_active_iter()
        if tree_iter is not None:
            model = obj.get_model()
            row_id = model[tree_iter][0]
            self.parameters +="key=" + row_id + " "
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
            self.command = "suximage < infile "+ self.parameters + " &"
            self.append_wf_cmd ="suximage < $infile "+ self.parameters + " &"
            self.parent.send_command(self.command,1)
        else:
            self.parent.send_message("No Parameters choosen",1)

    
    def run(self, widget):
        self.parameters+='windowtitle="sudoSU"'
        if self.parent.input_files==[]:
                self.parent.send_message("No Input Files selected",1)
                return True
        else:
            self.parent.console.set_current_page(2)
            for i,input_file in enumerate(self.parent.input_files):
                cmd = "suximage"+ " < " + input_file + " "+self.parameters +" &"
                self.parent.terminal.run_command(cmd+"\n")
                self.parent.history.append(cmd,0)
    
    def refresh(self, widget):
        self.append_wf_cmd=""
        self.parameters=""
        self.parent.output_files=[]
        for item in self.list:
            obj = self.builder.get_object(item)
            if type(obj)==type(Gtk.Entry()):
                obj.set_text("")
            elif type(obj)==type(Gtk.CheckButton()):
                obj.set_active(False)
        
    
    def append(self,widget):
        if self.parent.props.curr_project!=None:
            if self.parameters!="":
                self.parent.workflow_append(self.append_wf_cmd,0)
            else:
                self.parent.send_message("No Parameters choosen",0)
        else:
            self.parent.send_message("Can not append command without opening a Project",1)




    def help(self, widget):
        builder = Gtk.Builder()
        builder.add_from_file(self.glade_file)
        help_dlg = builder.get_object("help")
        help_dlg.set_title("SUXIMAGE Help")
        help_dlg.show_all()
        

    def destroy(self, widget):
        self.main_box.destroy()
        self.parent.tabs['SUXIMAGE'] = 0


class nb_page(Gtk.Box):
    def __init__(self,parent):
        self.main_class = suximage(parent)
        self.page = self.main_class.main_box
        self.title = self.main_class.title_box  
