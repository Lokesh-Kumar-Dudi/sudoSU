import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

import notebook_manager
class treeview(Gtk.Box):

    def __init__(self,parent):
        self.parent = parent
        self.vbox = Gtk.Box()
        self.notebook_manager =  notebook_manager.manager(self.parent)

        store = Gtk.TreeStore(str)
        row = store.append(None, ['Amplitude Correction'])
        store.append(row,['SUGAIN'])
        store.append(row,['SUDIVCOR'])
        row = store.append(None, ['Data Conversion'])
        store.append(row,['SEGYREAD'])
        row = store.append(None, ['Deconvolution Shaping'])
        store.append(row,['SUCDDECON'])
        store.append(row,['SUPEF'])
        store.append(row,['SUSHAPE'])
        row = store.append(None, ['Filtering'])
        store.append(row,['SUFILTER'])
        row = store.append(None, ['Header Tools'])
        store.append(row,['A2B'])
        store.append(row,['SUGETHW'])
        store.append(row,['SUSHW'])
        row = store.append(None,['Moveout, Resampling and Stretching'])
        store.append(row,['SUNMO'])
        row = store.append(None,['Muting, Sorting and Windowing'])
        store.append(row,['SUMUTE'])
        store.append(row,['SUSORT'])
        store.append(row,['SUWIND'])
        row = store.append(None,['Stacking'])
        store.append(row,['SUSTACK'])
        row = store.append(None,['Transforms'])
        store.append(row,['SUFFT'])
        store.append(row,['SURADON'])
        store.append(row,['SUSPECFX'])
        row = store.append(None,['Velocity Analysis'])
        store.append(row,['SUVELAN'])
        row = store.append(None,['Viewing and Exporting'])
        store.append(row,['SUPSIMAGE'])
        store.append(row,['SUPSWIGB'])
        store.append(row,['SUXIMAGE'])
        store.append(row,['SUXWIGB'])

        treeview = Gtk.TreeView(store)
        tvcolumn = Gtk.TreeViewColumn('Modules')
        treeview.append_column(tvcolumn)
        treeview.connect("row-activated", self.on_activated)

        cell = Gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 0)

        self.vbox.pack_start(treeview,True,True,0)   

    def on_activated(self,widget,row,column):  
        model = widget.get_model()
        tab_id = model[row][0]
        widget.expand_row(row,False) 
        self.notebook_manager.add_tab(tab_id)



