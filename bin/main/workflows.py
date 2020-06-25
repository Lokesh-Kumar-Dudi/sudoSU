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


class treeview():

    def __init__(self,parent):

        self.parent = parent
        self.vbox = Gtk.Box() 
        self.glade_file=str(Path(__file__).parent / "workflow.glade")
        self.store = Gtk.TreeStore(str)
        self.lis=[]
        self.refresh( home+"/sudoSU/Projects/")
        
    
        self.treeview = Gtk.TreeView(self.store)
        self.tvcolumn = Gtk.TreeViewColumn('Workflows')
        self.treeview.append_column(self.tvcolumn)
        self.treeview.connect("row-activated", self.on_activated)


        self.cell = Gtk.CellRendererText()
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn.add_attribute(self.cell, 'text', 0)

        self.vbox.pack_start(self.treeview,True,True,0)

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


class append_dlg:
    def __init__(self,parent,typ=0):
        self.parent = parent
        self.typ =typ
        self.glade_file=str(Path(__file__).parent / "workflow_append.glade")
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
        create_dlg(self.parent,self.wf_list)
    
    def cancel(self,widget):
        self.append_dlg.destroy()

class create_dlg:
    def __init__(self,parent,lis):
        self.parent = parent
        self.lis = lis
        self.glade_file=str(Path(__file__).parent / "workflow_create.glade")
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


