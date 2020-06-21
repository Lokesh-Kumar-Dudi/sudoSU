import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import os
import re
import glob
import ntpath
from pathlib import Path
home= str(Path.home())

class append_dlg:
    def __init__(self,parent):
        self.parent = parent
        self.glade_file = parent.props.UiPath + "main/workflow_manager.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.builder.connect_signals(self)
        self.append_dlg = self.builder.get_object("append_workflow")
        self.wf_list = self.builder.get_object("workflow_store")
        self.refresh( self.parent.props.curr_project)
        self.append_dlg.show_all()


    def refresh(self,arg):
        if arg==None:
            pass
        else:
            lis = [name for name in glob.glob(arg+'/workflows/*.sh')]
            lis.sort()
            for i in lis:
                self.wf_list.append([ntpath.basename(i)])
    def append(self,widget):
        obj = self.builder.get_object('list')
        tree_iter = obj.get_active_iter()
        if tree_iter is not None:
            model = obj.get_model()
            row_id = model[tree_iter][0]
        f = open(self.parent.props.curr_project+"/workflows/"+row_id,'a+')
        f.write(self.parent.append_cmd+"\n")
        f.close()
        self.append_dlg.destroy()

    def create(self,widget):
        self.builder2 = Gtk.Builder()
        self.builder2.add_from_file(self.glade_file)
        self.create_dlg = self.builder2.get_object("create_workflow")
        self.builder2.connect_signals(self)
        self.create_dlg.show_all()
    
    def done(self,widget):
        self.new_name =self.builder2.get_object("new_name").get_text()
        f = open(self.parent.props.curr_project+"/workflows/"+self.new_name,'w')
        f.write("infile=input_file\n")
        wf_name,ext = os.path.splitext(self.new_name)
        f.close()
        self.wf_list.append([self.new_name])
        self.parent.workflow_treeview.refresh(self.parent.props.curr_project)
        self.create_dlg.destroy()
    
    def cancel(self,widget):
        self.append_dlg.destroy()