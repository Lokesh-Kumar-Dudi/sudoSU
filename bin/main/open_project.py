import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import glob, os




class open_project:
    def __init__(self,parent):
        self.parent = parent
        self.open_project_dialogue()

    def open_project_dialogue(self):
        dialog = Gtk.FileChooserDialog(title="Please choose a Project",
                                        parent=None,action=Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.add_buttons(Gtk.STOCK_CANCEL, 2, "Select", 1)
        dialog.set_default_size(800, 400)
        dialog.set_current_folder(self.parent.props.sudoSU_projects)

        response = dialog.run()
        if response == 1:
            self.parent.props.curr_project = dialog.get_filename()
            self.parent.iconview.refresh(self.parent.props.curr_project)
            self.parent.workflow_treeview.refresh(self.parent.props.curr_project)
            self.parent.props.segy_file = ""
            os.chdir(self.parent.props.curr_project)
            file =glob.glob("*.segy")
            if file:
                self.parent.props.segy_file = self.parent.props.curr_project+"/"+str(file[0])
            else:
                self.parent.props.segy_file =None
            self.parent.home_obj.set_assets(self.parent.props.segy_file)
            self.parent.run("cd "+self.parent.props.curr_project+"\nclear\n")
            self.parent.send_message("Opened Project: "+self.parent.props.curr_project,1)
        elif response == 2:
            pass
        
        dialog.destroy()