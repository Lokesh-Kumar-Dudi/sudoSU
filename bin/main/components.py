#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
from pathlib import Path
home= str(Path.home())
import os
import sys

import general_tree
import terminal
import draganddrop
# import file_explorer
import modules
import workflows
DRAG_ACTION = Gdk.DragAction.COPY


class add_all:
    def __init__(self,parent):
        self.parent = parent
        self.parent.module_treeview  = modules.treeview(self.parent)
        self.parent.workflow_treeview  = workflows.treeview(self.parent)
        self.parent.workflow_list = self.parent.workflow_treeview.lis
        self.parent.tabs = self.parent.module_treeview.notebook_manager.tabs

        self.parent.console  = self.parent.builder.get_object("ConsoleNotebook") 
        self.parent.notebook  = self.parent.builder.get_object("ModuleNotebook")

        self.parent.message_tree_class = general_tree.treeview(self.parent)
        self.parent.message_tree = self.parent.message_tree_class.treeview
        self.parent.message_box =  self.parent.builder.get_object("message_box")
        self.parent.message_box.pack_start(self.parent.message_tree,True, True, 0)
        self.parent.message_tree_class.store.append(None,['sudoSU started normally \U0001f60A'])

        self.parent.module_box = self.parent.builder.get_object("module_box")
        self.parent.module_box.pack_start(self.parent.module_treeview.vbox, True, True, 0)

        self.parent.workflow_box = self.parent.builder.get_object("workflow_box")
        self.parent.workflow_box.pack_start(self.parent.workflow_treeview.vbox, True, True, 0)
        # self.parent.workflow_box.pack_start(Gtk.Label(label="Cool Stuff coming up... \U0001f60A"),True,True,0)

        self.parent.commands_tree_class = general_tree.treeview(self.parent)
        self.parent.commands_tree = self.parent.commands_tree_class.treeview
        self.parent.commands_box =  self.parent.builder.get_object("commands_box")
        self.parent.commands_box.pack_start(self.parent.commands_tree,True, True, 0)

        self.parent.terminal = terminal.terminal(self.parent)
        self.parent.terminal_box = self.parent.builder.get_object("terminal_tab")
        self.parent.terminal_box.pack_start(self.parent.terminal.main_box,True,True,0)

        self.parent.target = self.parent.builder.get_object("selected_files")
        self.parent.target.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.parent.target.connect("drag-data-received", self.parent.on_drag_data_received)
        self.parent.iconview = draganddrop.DragSourceIconView()
        self.parent.iconview.refresh(home+"/sudoSU/Projects/")
        
        self.parent.dest = self.parent.builder.get_object("dest")
        self.parent.source = self.parent.builder.get_object("source")
        self.parent.vbox = self.parent.builder.get_object("vbox")
        
        self.parent.source.pack_start(self.parent.iconview, True, True, 0)
        self.parent.add_image_targets()
        self.parent.add_text_targets()
        """to add the treview file exporer)"""
        # self.fex = file_explorer.treeview(self)
        # self.parent.source.pack_start(self.fex.vbox, True, True,0)

        self.parent.selected_files = self.parent.builder.get_object("selected_files")
        self.parent.file_label = Gtk.Label()
        self.parent.file_label.set_xalign(0)
        self.parent.selected_files.pack_start(self.parent.file_label,False,False,0)
        



