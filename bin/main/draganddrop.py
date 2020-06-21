#!/usr/bin/python3
import re
import os
import glob
import ntpath
import gi
from gi.repository import Gtk, Gdk, GdkPixbuf
from pathlib import Path
home= str(Path.home())

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY


def find(str):
    pattern = ".su"
    if re.search(pattern, str):
        return True
    else:
        return False


class DragSourceIconView(Gtk.IconView):

    def __init__(self):
        Gtk.IconView.__init__(self)
        model = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        self.set_text_column(COLUMN_TEXT)
        self.set_pixbuf_column(COLUMN_PIXBUF)
        self.set_model(model)

        self.enable_model_drag_source(
            Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
        self.connect("drag-data-get", self.on_drag_data_get)
        # self.set_selection_mode(3)
        self.set_columns(3)

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)

        if info == TARGET_ENTRY_TEXT:
            text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
            data.set_text(text, -1)
        elif info == TARGET_ENTRY_PIXBUF:
            pixbuf = self.get_model().get_value(selected_iter, COLUMN_PIXBUF)
            data.set_pixbuf(pixbuf)

    def refresh(self, arg=home):
        self.get_model().clear()
        lis = [name for name in glob.glob(arg+'/*.segy')]
        lis.sort()
        for i in lis:
            self.add_item(ntpath.basename(i), "text-x-generic")
        su_lis = [name for name in glob.glob(arg+'/*.su')]
        su_lis.sort()
        for i in su_lis:
            self.add_item(ntpath.basename(i), "text-x-generic")
        

    def add_item(self, text, icon_name):
        pixbuf = Gtk.IconTheme.get_default().load_icon(icon_name, 15, 0)
        self.get_model().append([text, pixbuf])
