import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from pathlib import Path
class dialog(Gtk.Dialog):
    def __init__(self,parent):
        
        self.parent = parent
        self.glade_file=str(Path(__file__).parent / "dialog.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)    
        self.main_box = self.builder.get_object("dialog")
        self.box = self.builder.get_object("box")
        self.label = self.builder.get_object("dialog_label")
        self.builder.connect_signals(self)
