import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import os
import re
import glob
import ntpath
from pathlib import Path
home= str(Path.home())

def assemble(file, arg1, arg2):
    with open("temp.sh", 'w'): pass
    f1 = open(file, 'r')
    f2 = open('temp.sh', 'a+')
    for line in f1:
        f2.write(line.replace(arg1, arg2))
    f1.close()
    f2.close()


class treeview(Gtk.Box):

    def __init__(self,parent):

        self.parent = parent
        self.vbox = Gtk.Box()
        self.parent = parent
        self.glade_file = parent.props.UiPath + "main/workflow.glade"
        self.store = Gtk.TreeStore(str)
        self.lis=[]
        self.refresh( home+"/sudoSU/Projects/")
        
    
        treeview = Gtk.TreeView(self.store)
        tvcolumn = Gtk.TreeViewColumn('Workflows')
        treeview.append_column(tvcolumn)
        treeview.connect("row-activated", self.on_activated)


        cell = Gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 0)

        self.vbox.pack_start(treeview,True,True,0)

    def on_activated(self,widget,row,column):  
        model = widget.get_model()
        self.tab_id = model[row][0] 
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.run_dlg = self.builder.get_object("run_workflow")
        self.file_name = self.builder.get_object("infile_name")
        try:
            self.file_name.set_text("Input file: "+self.parent.input_files[0])
        except:
            self.parent.send_message("No input file to execute Workflow",1)   
        self.builder.connect_signals(self)
        self.run_dlg.show_all()

    def delete(self,widget):
        os.remove(self.parent.props.curr_project+"/workflows/"+self.tab_id)
        self.refresh(self.parent.props.curr_project)
        self.run_dlg.destroy()


    def edit(self,widget):
        self.parent.run("gedit workflows/"+self.tab_id,1)


    def run(self, widget):
        if self.parent.input_files!=[]:
            self.workflow_file = self.parent.props.curr_project+"/workflows/"+self.tab_id
            assemble(self.workflow_file,"input_file",self.parent.input_files[0])
            self.parent.run("bash temp.sh",1 )
            self.parent.iconview.refresh(self.parent.props.curr_project)
            self.run_dlg.destroy()
        else:
            self.parent.send_message("No input file to execute Workflow",1)

    def refresh(self,arg):
        self.store.clear()
        try:
            self.lis = [name for name in glob.glob(arg+'/workflows/*.sh')]
            self.lis.sort()
            for i in self.lis:
                self.store.append(None,[ntpath.basename(i)])
        except:
            pass
