import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import os
import re
from pathlib import Path
home= str(Path.home())

def find(str): 
    pattern = ".sh"
    if re.search(pattern, str):
        return True
    else:
        return False

class treeview(Gtk.Box):

    def __init__(self,parent):

        self.parent = parent
        self.vbox = Gtk.Box()

        # create a TreeStore with one string column to use as the model
        self.store = Gtk.TreeStore(str)
        self.refresh( home+"/sudoSU/Projects/")
    
        # create the TreeView using treestore
        treeview = Gtk.TreeView(self.store)
        tvcolumn = Gtk.TreeViewColumn('Workflows')  #extra space stops the treeview column from changing width weirdly
        treeview.append_column(tvcolumn)
        treeview.connect("row-activated", self.on_activated)


        cell = Gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 0)

        self.vbox.pack_start(treeview,True,True,0)

    def on_activated(self,widget,row,column):  
        model = widget.get_model()
        tab_id = model[row][0] 
        print(tab_id)
    def refresh(self,arg):
        self.store.clear()
        lis =os.listdir(arg)
        lis.sort()
        for i in lis:
            if find(i):
                self.store.append(None,[i])
            else:
                pass
            # if find(name):
            #     self.store.append(None,[str(i) + ". " +self.parent.get_outname(name,None,2)])
            # else:
            #     pass

