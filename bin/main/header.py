import gi
import os
import time
from datetime import datetime
gi.require_version("Gtk","3.0")
gi.require_version("Vte","2.91")
from gi.repository import Gtk,Gdk,Vte,GLib
from pathlib import Path
home= str(Path.home())

import open_project
import new_project
import preference_win
class main:
    def __init__(self,parent,title="",subtitle=""):
        self.parent = parent
        self.header = Gtk.HeaderBar()
        self.header.set_title(title)
        self.header.set_subtitle(subtitle)
        self.menu_button = Gtk.Button(label = "Project")
        self.menu_button.connect("clicked",self.menu_button_clicked)
        self.menu_button.set_relief(Gtk.ReliefStyle.NONE)
        self.menu_button.set_alignment(0,0.5)
        self.header.pack_start(self.menu_button)

        self.preference_button = Gtk.Button(label = "Settings")
        self.preference_button.connect("clicked",self.preference_button_clicked)
        self.preference_button.set_relief(Gtk.ReliefStyle.NONE)
        self.preference_button.set_alignment(0,0.5)
        self.header.pack_start(self.preference_button)

        self.help_button = Gtk.Button(label = "Help")
        self.help_button.connect("clicked",self.help_button_clicked)
        self.help_button.set_relief(Gtk.ReliefStyle.NONE)
        self.help_button.set_alignment(0,0.5)
        self.header.pack_end(self.help_button)

        self.header.set_show_close_button(True)


        self.pop_menu = Gtk.Popover()
        self.vbox = Gtk.VBox()
        self.open = Gtk.ModelButton(label = "Open")
        self.open.connect("clicked",self.open_clicked)
        # self.open.set_alignment(0,0)
        self.new = Gtk.ModelButton(label = "New")
        self.new.connect("clicked",self.new_clicked)
        # self.new.set_alignment(0,0)
        self.save = Gtk.ModelButton(label = "Save")
        self.save.connect("clicked",self.save_clicked)
        # self.save.set_alignment(0,0)
        self.close = Gtk.ModelButton(label = "Close") 
        self.close.connect("clicked",self.close_clicked)
        # self.close.set_alignment(0,0)
        self.vbox.pack_start(self.new,True,True,0)
        self.vbox.pack_start(self.open,True,True,0)
        self.vbox.pack_start(self.save,True,True,0)
        self.vbox.pack_start(self.close,True,True,0)
        self.pop_menu.add(self.vbox)
        self.pop_menu.set_position(Gtk.PositionType.BOTTOM)

    




    def set_title(self, title):
        self.header.set_title(title)
    
    def set_subtitle(self,subtitle):
        self.header.set_subtitle(subtitle)

    def open_clicked(self,widget):
        open_project.open_project(self.parent)

    def new_clicked(self,widget):
        new_project.new_project_create(self.parent)

    def save_clicked(self,widget):
        if self.parent.props.curr_project!=None:
            history = open(self.parent.props.curr_project+"/history.txt",'a')
            if self.parent.history!=[]:
                for i in self.parent.history:
                    history.write("\n"+i+" @ "+str(datetime.now()))
            else:
                pass
            history.close()
        else:
            pass
        self.parent.history= []
        self.parent.send_message("Saved Project: "+self.parent.props.curr_project,1)

    def close_clicked(self,widget):
        self.builder = Gtk.Builder()
        self.glade_file = self.parent.props.UiPath + "main/dialog.glade"
        self.builder.add_from_file(self.glade_file)
        self.save_dialog = self.builder.get_object("save_dialog")  
        self.save_dialog.show_all()
        self.builder.connect_signals(self)   
        
    def close_project(self,widget):
        self.parent.iconview.refresh(self.parent.props.sudoSU_projects)
        self.parent.workflow_treeview.refresh(self.parent.props.sudoSU_projects)
        self.parent.send_message("Closed Project: "+self.parent.props.curr_project,1)
        self.parent.props.curr_project=None
        self.parent.home_obj.set_assets(None)
        self.save_dialog.destroy()


    def menu_button_clicked(self,widget):
        self.pop_menu.set_relative_to(self.menu_button)
        self.pop_menu.show_all()
        self.pop_menu.popup()

    def preference_button_clicked(self,widget):
        preference_win.preference_window(self.parent)
    def help_button_clicked(self,widget):
        pass
    
    def save_close(self,widget):
        if self.parent.props.curr_project!=None:
            history = open(self.parent.props.curr_project+"/history.txt",'a')
            if self.parent.history!=[]:
                for i in self.parent.history:
                    history.write("\n"+i+" @ "+str(datetime.now()))
            else:
                pass
            history.close()
        else:
            pass
        self.parent.history= []
        try:
            self.parent.send_message("Saved Project: "+self.parent.props.curr_project,1) 
            self.parent.props.curr_project=None
            self.parent.iconview.refresh(self.parent.props.sudoSU_projects)
            self.parent.workflow_treeview.refresh(self.parent.props.sudoSU_projects)
            self.parent.home_obj.set_assets(None)
            self.save_dialog.destroy()
        except:
            pass





    

