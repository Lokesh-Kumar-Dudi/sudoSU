import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import os
import re
import glob
import ntpath
from pathlib import Path
home= str(Path.home())

class create_dlg:
    def __init__(self,parent,lis):
        self.parent = parent
        self.lis = lis
        self.glade_file = parent.props.UiPath + "main/workflow_create.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.create_dlg = self.builder.get_object("create_workflow")
        self.builder.connect_signals(self)
        self.create_dlg.show_all()
    
    def done(self,widget):
        self.new_name =self.builder.get_object("new_name").get_text()
        try:
            f = open(self.parent.props.curr_project+"/workflows/"+self.new_name,'w')
            f.write("infile=input_file\n")
            wf_name,ext = os.path.splitext(self.new_name)
            #f.write("prefix="+wf_name+"\n")
            f.close()
            self.lis.append([self.new_name])
            self.parent.workflow_treeview.refresh(self.parent.props.curr_project)
            self.create_dlg.destroy()
        except:
            self.parent.send_message("No 'workflows' folder found in the Project",1)


