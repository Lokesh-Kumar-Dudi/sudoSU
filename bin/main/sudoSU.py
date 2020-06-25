#!/usr/bin/python3
import properties
import components
import open_project
import new_project 
import header
import home
import workflows
import re
import os
import sys
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
import warnings
warnings.filterwarnings("ignore")
from pathlib import Path

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)
DRAG_ACTION = Gdk.DragAction.COPY

class Main:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.props = properties.properties()                                                    
        self.glade_file=str(Path(__file__).parent / "sudoSU.glade")
        self.builder.add_from_file(self.glade_file)
        self.window = self.builder.get_object("main")   
        self.header = header.main(self,"sudoSU")
        self.window.set_titlebar(self.header.header)                                      
        self.window.move(0,0)
        self.window.set_default_size(self.props.width, self.props.height)                     
        self.window.connect("delete-event", Gtk.main_quit)                                    
        self.builder.connect_signals(self)                                               
        self.input_files = []
        self.output_files=[]
        self.home_obj = home.home(self)
        self.history=[]
        self.workflow=""
        components.add_all(self)
        self.window.show_all()
        

    def add_image_targets(self, button=None):
        targets = Gtk.TargetList.new([])
        targets.add_image_targets(TARGET_ENTRY_PIXBUF, True)
        self.target.drag_dest_set_target_list(targets)
        self.iconview.drag_source_set_target_list(targets)

    def add_text_targets(self, button=None):
        self.target.drag_dest_set_target_list(None)
        self.iconview.drag_source_set_target_list(None)
        self.target.drag_dest_add_text_targets()
        self.iconview.drag_source_add_text_targets()
    
    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):
        if info == TARGET_ENTRY_TEXT:
            if data.get_text() not in self.input_files:
                self.input_files.append(data.get_text())    
                self.file_label.set_text(self.file_label.get_text()+"\n"+str(len(self.input_files))+". "+data.get_text())     
            else:
                pass
            self.selected_files.show_all()

    def clear_files(self,widget):
        self.input_files=[]
        self.file_label.set_text("")

    def send_message(self, msg,switch=0):
        """
        Adds Message sent from program to Messages Panel.\n
        msg = Message to be added.\n
        if switch = 1 Messages Panel Grabs focus after adding message\n
        if switch = 0  Messages Panel does not Grab focus after adding message

        """
        self.message_tree_class.store.prepend(None, [msg])
        if switch:
            self.console.set_current_page(0)
        else:
            pass
    
    def send_command(self, cmd,switch=0):
        """
        Adds Command set from Modules to Commands Panel.\n
        cmd =  Command to be added.\n
        if switch = 1 Commands Panel Grabs focus after adding command\n
        if switch = 0  Commands Panel does not Grab focus after adding command

        """
        self.commands_tree_class.store.prepend(None, [cmd])
        if switch:
            self.console.set_current_page(1)
        else:
            pass

    def clear_terminal(self):
        self.terminal.run_command("clear\n")


    def refresh_file_ex(self,widget):
        if self.props.curr_project!=None:
            path = self.props.curr_project
        else:
            path = home
        self.iconview.refresh(path)
        self.workflow_treeview.refresh(path)

    
    def run(self,cmd,switch=0):
        self.terminal.run_command(cmd+"\n")
        if switch:
            self.console.set_current_page(2)
        else:
            pass


    def display_trace_hdrs(self,widget):
        self.home_obj.display_trace_hdrs(self.props.segy_file)

    
    def workflow_append(self,command,typ):
        self.append_cmd= command
        workflows.append_dlg(self,typ)

    def get_outname(self,arg,infile=None,parameters=None):
        """
        Generates Output file name for Input file name.\n
        arg = "su" if Infile is SEGY and Outfile is SU\n
        arg =  "ps" if Infile is SU and Outfile is PS\n
        infile = Input file name\n
        parameters = SU Program Paramteters \n  
        """
        if parameters:
            lis = ['=','+','-',' ',]
            string=""
            for i in lis:
                string=parameters.replace(str(i),'.')
                parameters=string.replace('"','')
            perm=string
        else:
            perm=""
        if infile:
            if arg=="su":                              
                outfile = infile.replace('segy','su') 
            elif arg=="ps":
                outfile = infile.replace('su','ps')
            # elif arg=="":
            #     outfile= re.sub(r'\.\s*','',infile)   #to remove extension
            else:
                outfile=""
        return perm+outfile

if __name__ == '__main__':
    main = Main()
    Gtk.main()
