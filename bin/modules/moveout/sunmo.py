import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import ntpath
from pathlib import Path
class sunmo(Gtk.Box):
    def __init__(self,parent):
        self.parent = parent
        self.glade_file=str(Path(__file__).parent/"sunmo.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        
        self.main_box = self.builder.get_object("sunmo")
        self.title_box = self.builder.get_object("tab_title")
        self.builder.connect_signals(self)
        self.entry1 = self.builder.get_object("tnmo")
        self.entry2 = self.builder.get_object("vnmo")
        self.list = ['cdp','smute','lmute','sscale','invert','upward','voutfile']
        self.output_files = self.builder.get_object("output_files")
        self.append_wf_cmd = ""
        self.parameters=""

    def set_parameters(self, widget):
        self.parameters  = ""
        if self.entry1.get_text()!="" and self.entry2.get_text()!="":
            str1= self.entry1.get_text().split(',')
            str2= self.entry2.get_text().split(',')
            if len(str1)==len(str2):
                self.parameters = "tnmo="+self.entry1.get_text() + " vnmo="+self.entry2.get_text()+" "
                for item in self.list:
                    obj = self.builder.get_object(item)
                    if type(obj)==type(Gtk.Entry()):
                        if obj.get_text()!="":
                            self.parameters+=item+"="+obj.get_text()+" "
                        else:
                            pass
                    elif type(obj)==type(Gtk.CheckButton()):
                        if obj.get_active():
                            self.parameters+=item+"="+"1 "
                        else:
                            pass
            else:
                self.parent.send_message("'tnmo' and 'vnmo' Array lengths must be same",1)
        else:
            self.parent.send_message("Required Parameters not choosen",1)
            self.parameters=""
        if self.parameters!="":
            self.command = "sunmo < infile "+ self.parameters + " >" + "outfile"
            self.append_wf_cmd ="sunmo < $infile "+ self.parameters + " >" + "$prefix.$infile"
            self.parent.send_command(self.command,1)
        else:
            self.parent.send_message("Required Parameters not choosen",1)


    def run(self,widget):
        self.temp = self.output_files.get_text()
        if self.temp!="":
            self.parent.output_files = self.temp.split(',')
        else:
            self.parent.send_message("No Output File names given",1)
        if self.parent.input_files==[]:
                self.parent.send_message("No Input Files selected",1)
                return True
        if len(self.parent.input_files)==len(self.parent.output_files):
            self.parent.console.set_current_page(2)
            for i,input_file in enumerate(self.parent.input_files):
                cmd = "sunmo"+ " < " + input_file + " "+self.parameters \
                    +" > "+self.parent.output_files[i]
                self.parent.terminal.run_command(cmd+"\n")
                self.parent.history.append(cmd)
            self.parent.refresh_file_ex(self.parent.props.curr_project)  
        else: 
            self.parent.send_message("No. of Output Files not equal to No. of Input Files",1)


    def refresh(self, widget):
        self.parameters=""
        self.output_files.set_text("")
        self.parent.output_files=[]
        self.entry1.set_text("")
        self.entry2.set_text("")
        for item in self.list:
            obj = self.builder.get_object(item)
            if type(obj)==type(Gtk.Entry()):
                obj.set_text("")
            elif type(obj)==type(Gtk.CheckButton()):
                obj.set_active(False)
            elif type(obj)==type(Gtk.RadioButton()):
                obj.set_active(False)
            else:
                pass 


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
        help_dlg.set_title("SUNMO Help")
        help_dlg.show_all()


    def destroy(self, widget):
        self.main_box.destroy()
        self.parent.tabs['SUNMO'] = 0


class nb_page(Gtk.Box):
    def __init__(self,parent):
        self.main_class = sunmo(parent)
        self.page = self.main_class.main_box
        self.title = self.main_class.title_box


    



