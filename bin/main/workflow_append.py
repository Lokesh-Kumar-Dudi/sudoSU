import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import os
import re
import glob
import ntpath
from pathlib import Path
home= str(Path.home())
import workflow_create

class append_dlg:
    def __init__(self,parent,typ=0):
        self.parent = parent
        self.typ =typ
        print(self.typ)
        self.glade_file = parent.props.UiPath + "main/workflow_append.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.builder.connect_signals(self)
        self.append_dlg = self.builder.get_object("append_workflow")
        self.wf_list = self.builder.get_object("workflow_store")
        self.prefix = self.builder.get_object("prefix")
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
        if self.typ:
            f.write("prefix="+self.prefix.get_text()+"\n")
            f.write(self.parent.append_cmd+"\n")
            f.write("infile=$prefix.$infile\n")
        else:
            f.write(self.parent.append_cmd+"\n")
        f.close()
        self.append_dlg.destroy()

    def create(self,widget):
        workflow_create.create_dlg(self.parent,self.wf_list)
    
    def cancel(self,widget):
        self.append_dlg.destroy()