import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import ntpath
from pathlib import Path
class suconv(Gtk.Box):
    def __init__(self,parent):
        self.parent = parent
        self.glade_file=str(Path(__file__).parent / "suconv.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        
        self.main_box = self.builder.get_object("suconv")
        self.title_box = self.builder.get_object("tab_title")
        self.builder.connect_signals(self)
        self.entry1 = self.builder.get_object("filter")
        self.checkbutton = self.builder.get_object("panel")
        self.sufile = self.builder.get_object("sufile")
        self.output_files = self.builder.get_object("output_files")
        self.append_wf_cmd = ""
        self.parameters=""

    def set_parameters(self, widget):
        self.parameters  = ""
        if (self.entry1.get_text()!="" and self.sufile.get_filename()):
            self.parent.send_message("Only sufile or filter must be given",1)
            self.parameters = None
        elif self.entry1.get_text()!="":
            self.parameters +=" filter="+self.entry1.get_text()
        elif(self.sufile.get_filename()):
            self.parameters += " sufile="+ntpath.basename(self.sufile.get_filename())
        if self.checkbutton.get_active():
            self.parameters += " panel=1"
        if self.parameters!="":
            self.command = "suconv < infile "+ self.parameters + " >" + "outfile"
            self.append_wf_cmd ="suconv < $infile "+ self.parameters + " >" + "$prefix.$infile"
            self.parent.send_command(self.command,1)
        else:
            self.parent.send_message("No Parameters choosen",1)
        

    


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
                cmd = "suconv"+ " < " + input_file + " "+self.parameters \
                    +" > "+self.parent.output_files[i]
                self.parent.terminal.run_command(cmd+"\n")
                self.parent.history.append(cmd)
            self.parent.refresh_file_ex(self.parent.props.curr_project)  
        else: 
            self.parent.send_message("No. of Output Files not equal to No. of Input Files",1)


    def refresh(self, widget):
        self.append_wf_cmd=""
        self.parameters=""
        self.output_files.set_text("")
        self.parent.output_files=[]
        self.entry1.set_text("")
        try:
            self.sufile.unselect_filename(self.sufile.get_filename())
        except:
            pass
        self.checkbutton.set_active(False)


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
        help_dlg.set_title("SUCONV Help")
        help_dlg.show_all()


    def destroy(self, widget):
        self.main_box.destroy()
        self.parent.tabs['SUCONV'] = 0


class nb_page(Gtk.Box):
    def __init__(self,parent):
        self.main_class = suconv(parent)
        self.page = self.main_class.main_box
        self.title = self.main_class.title_box


    



