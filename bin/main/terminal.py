import gi
gi.require_version("Vte","2.91")
from gi.repository import Vte, Gtk,Gdk
from gi.repository import GLib

import os
import general_tree
import subprocess
class terminal(Gtk.Box):
    def __init__(self,parent):
        self.parent = parent
        self.glade_file = parent.props.UiPath + "main/terminal.glade"
        self.builder = Gtk.Builder()        
        self.builder.add_from_file(self.glade_file)
        self.main_box = self.builder.get_object("main_box")                                         # makes the main window
        self.builder.connect_signals(self)                                               # connects rest of the signals from glade file to their handlers
        
        self.terminal = Vte.Terminal()
        self.terminal.spawn_sync(Vte.PtyFlags.DEFAULT, os.getcwd(), 
                ["/bin/bash"], [], GLib.SpawnFlags.DO_NOT_REAP_CHILD, None, None,)
        self.terminal.set_size(100,10)
        self.terminal_box = self.builder.get_object("terminal_box")
        self.terminal_box.pack_start(self.terminal, True, True, 0)
        self.terminal_box = self.builder.get_object("scrollbar_box")

        self.scrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.VERTICAL,adjustment = Gtk.Scrollable.get_vadjustment(self.terminal))
        self.terminal_box.pack_start(self.scrollbar, True, True, 0)
        self.terminal_box.show()
        self.startup_cmds=["PS1='sudoSU@$PWD $: '\n","clear\n"]
        for i in self.startup_cmds:
            self.run_command(i)

        self.menu = self.builder.get_object("menu")
        self.main_box.connect_object("event", self.button_press, self.menu)
    def run_command(self,cmd):
        if (Vte.get_minor_version()==52):
            self.terminal.feed_child(cmd,len(cmd))
        else:
            self.terminal.feed_child_binary(bytes(cmd,'utf8'))
            
    def button_press(self, widget, event):
        if event.type == Gdk.EventType.BUTTON_RELEASE:
            x,button = event.get_button()
            if button == Gdk.BUTTON_SECONDARY:
                widget.popup(None,None, None, None, button, Gdk.CURRENT_TIME)

    def copy(self,widget):
        self.terminal.copy_primary()
    def paste(self,widget):
        self.terminal.paste_primary()
    def clear(self,widget):
        self.run_command("clear\n")
