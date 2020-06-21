import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import ntpath
from pathlib import Path
class sushape(Gtk.Box):
    def __init__(self,parent):
        self.parent = parent
        self.glade_file=str(Path(__file__).parent / "sushape.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        
        self.main_box = self.builder.get_object("sushape")
        self.title_box = self.builder.get_object("tab_title")
        self.builder.connect_signals(self)
        self.entry1 = self.builder.get_object("w")
        self.entry2 = self.builder.get_object("d")
        self.entry3 = self.builder.get_object("pnoise")
        self.entry4 = self.builder.get_object("nshape")
        self.showshaper = self.builder.get_object("showshaper")
        self.entry5 = self.builder.get_object("shape_file")
        self.wfile = self.builder.get_object("wfile")
        self.dfile = self.builder.get_object("dfile")
        self.output_files = self.builder.get_object("output_files")
        self.append_wf_cmd = ""
        self.parameters=""

    def set_parameters(self, widget):
        self.parameters  = ""
        if self.entry1.get_text()!="" and self.entry2.get_text()!="":
            str1= self.entry1.get_text().split(',')
            str2= self.entry2.get_text().split(',')
            if len(str1)==len(str2):
                self.parameters = "w="+self.entry1.get_text() + " d="+self.entry2.get_text()+" "
            else:
                self.parent.send_message("'d' and 'w' Array lengths must be same",1)
        else:
            try:
                self.parameters += "wfile="+ntpath.basename(self.wfile.get_filename())+" "
                self.parameters += "dfile="+ntpath.basename(self.dfile.get_filename())+" "
            except:
                self.parent.send_message("Required Parameters not choosen",1)
                self.parameters=""
        if self.parameters!="":
            if self.entry3.get_text()!="":
                self.parameters+="pnoise="+self.entry3.get_text()+" "
            if self.entry4.get_text()!="":
                self.parameters+="nshape="+self.entry4.get_text()+" "
            if self.showshaper.get_active():
                self.parameters+="showshaper=1 "
                self.command = "sushape < infile "+ self.parameters + " >" + "outfile >&"+self.entry5.get_text()
            else:
                self.command = "sushape < infile "+ self.parameters + " >" + "outfile"
                self.append_wf_cmd ="sushape < $infile "+ self.parameters + " >" + "$prefix.$infile"
            self.parent.send_command(self.command,1)
    
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
                if self.showshaper.get_active():
                    cmd = "sushape"+ " < " + input_file + " "+self.parameters \
                        +" > "+self.parent.output_files[i] +"> &"+self.entry5.get_text()
                else:
                    cmd = "sushape"+ " < " + input_file + " "+self.parameters \
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
        self.entry2.set_text("")
        self.vfile.unselect_filename(self.vfile.get_filename())


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
        help_dlg.set_title("SUSHAPE Help")
        help_dlg.show_all()


    def destroy(self, widget):
        self.main_box.destroy()
        self.parent.tabs['SUSHAPE'] = 0


class nb_page(Gtk.Box):
    def __init__(self,parent):
        self.main_class = sushape(parent)
        self.page = self.main_class.main_box
        self.title = self.main_class.title_box


    



