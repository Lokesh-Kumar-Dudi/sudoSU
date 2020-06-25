
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import ntpath
import time
from pathlib import Path
home= str(Path.home())

def get_size(arg):
    i=0
    while (arg>1024):
        arg=arg/1024
        i+=1
    size = str(int(arg))
    if i==2:
        return size+" MB"
    elif i==3:
        return size+" GB"
    elif i==4:
        return size+" TB"
    else:
        return size+" KB"
        

class new_project_create():
    def __init__(self, parent):
        self.parent = parent
        self.glade_file=str(Path(__file__).parent / "new_project.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.prompt1 = self.builder.get_object("prompt1")
        self.prompt2 = self.builder.get_object("prompt2")
        self.segy_chooser = self.builder.get_object("segy_chooser")
        self.entry = self.builder.get_object("entry")
        self.size_label = self.builder.get_object("size")
        self.builder.connect_signals(self)
        self.segy_chooser.set_current_folder(home)
        self.filter_segy = Gtk.FileFilter()                                               # adds ".segy" filter
        self.filter_segy.set_name("SEG-Y files")
        self.filter_segy.add_pattern("*.segy")
        self.segy_chooser.add_filter(self.filter_segy)
        self.tape=""
        self.new_project=""
        self.prompt1.show()
        self.conv = self.builder.get_object("conv")
        self.ebcdic = self.builder.get_object("ebcdic")
        self.over = self.builder.get_object("over")
        self.trcwt = self.builder.get_object("trcwt")
        self.buff = self.builder.get_object("buff")
        self.hfile = self.builder.get_object("hfile")
        self.bfile = self.builder.get_object("bfile")
        self.xfile = self.builder.get_object("xfile")
        self.empty = self.builder.get_object("empty")
    
    def finish(self,widget):
        self.command = "segyread tape="+self.tape
        self.parameters =" "
        if self.conv.get_active():
            self.parameters+="conv=1 "
        if self.ebcdic.get_active():
            self.parameters+="ebcdic=1 "
        if self.over.get_active():
            self.parameters+="over=1 "
        if self.trcwt.get_active():
            self.parameters+="trcwt=1 "
        if self.buff.get_active():
            self.parameters+="buff=1 "
        if self.hfile.get_active():
            self.parameters+="hfile=ebcdic_headers.txt "
        if self.bfile.get_active():
            self.parameters+="bfile=Binary_headers.txt "
        if self.xfile.get_active():
            self.parameters+="xfile=Extented_binary_headers.txt "
        else:
            pass
        self.command+=self.parameters+ " >" +self.parent.get_outname("su",self.tape,None)
        self.parent.run(self.command,1)
        self.parent.refresh_file_ex(self.new_project)
        self.parent.home_obj.set_assets(self.new_project+"/"+self.tape)
        self.prompt2.destroy()

    def file_set(self, widget):
        self.original_path = self.segy_chooser.get_filename()
        self.tape = ntpath.basename(self.original_path)
        self.parent.props.segy_file = self.tape
        self.tape_info = os.stat(self.original_path)
        self.size_label.set_text("File Size: "+get_size(self.tape_info.st_size))

    def next(self, widget):
        if not self.empty.get_active():
            self.new_project = self.entry.get_text()                           # gets new project name from dialog
            if self.entry.get_text() != "" and self.tape!="":
                self.new_project = self.parent.props.sudoSU_projects+self.entry.get_text() 
                os.mkdir(self.new_project)
                self.workflows = self.new_project+"/workflows"
                os.mkdir(self.workflows)
                self.parent.send_message("New Project "+"created: "+"'"+self.new_project+"'",1)
                self.parent.run("cd "+self.new_project+"\n")
                self.parent.run("cp  "+self.original_path + " " +self.new_project + "\n")
                self.parent.send_message("Copied file '" + self.tape +"' into '"+self.new_project+"'",1 )
                self.parent.clear_terminal()
                self.parent.props.curr_project = self.new_project
                self.parent.refresh_file_ex(self.parent.props.curr_project)
                self.prompt1.destroy()
                self.prompt2.show()
            elif self.entry.get_text() == "":
                self.parent.send_message("New Project Name cannot be empty",1)
            elif self.tape=="":
                self.parent.send_message("Select a SEGY file for new project",1)
            
        else:
            self.new_project = self.entry.get_text()                           # gets new project name from dialog
            if self.entry.get_text() != "":
                self.new_project = self.parent.props.sudoSU_projects+self.entry.get_text() 
                os.mkdir(self.new_project)
                self.workflows = self.new_project+"/workflows"
                os.mkdir(self.workflows)
                self.parent.send_message("New Project "+"created: "+"'"+self.new_project+"'",1)
                self.parent.run("cd "+self.new_project+"\n")
                self.parent.clear_terminal()
                self.parent.props.curr_project = self.new_project
                self.parent.refresh_file_ex(self.parent.props.curr_project)
                self.prompt1.destroy()
    def refresh(self,widget):
        self.conv.set_active(False)
        self.ebcdic.set_active(False)
        self.over.set_active(False)
        self.trcwt.set_active(False)
        self.buff.set_active(False)
        self.hfile.set_active(False)
        self.bfile.set_active(False)
        self.xfile.set_active(False)

    def help(self, widget):
        builder = Gtk.Builder()
        builder.add_from_file(self.glade_file)
        help_dlg = builder.get_object("help")
        help_dlg.set_title("SEGYREAD Help")
        help_dlg.show_all()
    def exit_newp(self,widget):
        self.prompt1.destroy()

