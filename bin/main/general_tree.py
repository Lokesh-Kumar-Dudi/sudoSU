import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import dialog
class treeview(Gtk.Box):

    def __init__(self,parent):
        self.parent = parent
        self.store = Gtk.TreeStore(str)
        self.treeview = Gtk.TreeView(self.store)
        self.tvcolumn = Gtk.TreeViewColumn('') 
        self.treeview.append_column(self.tvcolumn)
        self.treeview.set_headers_visible(False)
        self.treeview.set_rubber_banding(True)
        self.treeview.connect("row-activated", self.on_activated)

        self.cell = Gtk.CellRendererText()
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn.add_attribute(self.cell, 'text', 0)

    def on_activated(self, widget,row,column):
        model = widget.get_model()
        tab_id = model[row][0]
        dlg_obj = dialog.dialog(self.parent)
        main_dialog = dlg_obj.main_box
        dlg_obj.label.set_text(tab_id)
        main_dialog.show_all()    