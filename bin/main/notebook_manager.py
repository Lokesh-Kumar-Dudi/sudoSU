import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import os
import sys
from pathlib import Path
home= str(Path.home())
sys.path.append(os.path.abspath(home+'/sudoSU/bin/modules'))

class manager:
    def __init__(self,parent):
        self.parent = parent
        self.tabs = {'SUGAIN':0,'SUDIVCOR':0,'SUSORT':0,'SUWIND':0,'SUXWIGB':0,
                        'SUXIMAGE':0,'SUPSWIGB':0,'SUPSIMAGE':0,'SUCDDECON':0,'SUPEF':0,'SUSHAPE':0,
                        'SUFILTER':0,'SUGETHW':0,'SUSHW':0,'A2B':0,'SUNMO':0,'SUSTACK':0,'SUFFT':0,'SUSPECFX':0,
                        'SUVELAN':0,'SUMUTE':0,'SURADON':0,'SEGYREAD':0}
        
    
    def add_tab(self,tab_id):
        if tab_id == "Amplitude Correction":
            pass
        elif tab_id == "SUGAIN":
            from amplitude import sugain
            if self.tabs['SUGAIN'] != 1:
                self.append_tab(self.parent, sugain.nb_page(self.parent))
                self.tabs['SUGAIN'] = 1
            else:
                pass


        elif tab_id == "SUDIVCOR":
            from amplitude import sudivcor
            if self.tabs['SUDIVCOR'] != 1:
                self.append_tab(self.parent, sudivcor.nb_page(self.parent))
                self.tabs['SUDIVCOR'] = 1
            else:
                pass
        elif tab_id == "SUSORT":
            from sorting_windowing import susort
            if self.tabs['SUSORT'] != 1:
                self.append_tab(self.parent, susort.nb_page(self.parent))
                self.tabs['SUSORT'] = 1
            else:
                pass
        elif tab_id=="SUWIND":
            from sorting_windowing import suwind
            if self.tabs['SUWIND'] != 1:
                self.append_tab(self.parent, suwind.nb_page(self.parent))
                self.tabs['SUWIND'] = 1
            else:
                pass
        elif tab_id=="SUMUTE":
            from sorting_windowing import sumute
            if self.tabs['SUMUTE'] != 1:
                self.append_tab(self.parent, sumute.nb_page(self.parent))
                self.tabs['SUMUTE'] = 1
            else:
                pass
        elif tab_id=="SUXWIGB":
            from viewing_exporting import suxwigb
            if self.tabs['SUXWIGB'] != 1:
                self.append_tab(self.parent, suxwigb.nb_page(self.parent))
                self.tabs['SUXWIGB'] = 1
            else:
                pass
        elif tab_id=="SUXIMAGE":
            from viewing_exporting import suximage
            if self.tabs['SUXIMAGE'] != 1:
                self.append_tab(self.parent, suximage.nb_page(self.parent))
                self.tabs['SUXIMAGE'] = 1
            else:
                pass
        elif tab_id=="SUPSWIGB":
            from viewing_exporting import supswigb
            if self.tabs['SUPSWIGB'] != 1:
                self.append_tab(self.parent, supswigb.nb_page(self.parent))
                self.tabs['SUPSWIGB'] = 1
            else:
                pass
        elif tab_id=="SUPSIMAGE":
            from viewing_exporting import supsimage
            if self.tabs['SUPSIMAGE'] != 1:
                self.append_tab(self.parent, supsimage.nb_page(self.parent))
                self.tabs['SUPSIMAGE'] = 1
            else:
                pass
        elif tab_id=="SUCDDECON":
            from decon_shaping import sucddecon
            if self.tabs['SUCDDECON'] != 1:
                self.append_tab(self.parent, sucddecon.nb_page(self.parent))
                self.tabs['SUCDDECON'] = 1
            else:
                pass
        elif tab_id=="SUPEF":
            from decon_shaping import supef
            if self.tabs['SUPEF'] != 1:
                self.append_tab(self.parent, supef.nb_page(self.parent))
                self.tabs['SUPEF'] = 1
            else:
                pass
        elif tab_id=="SUSHAPE":
            from decon_shaping import sushape
            if self.tabs['SUSHAPE'] != 1:
                self.append_tab(self.parent, sushape.nb_page(self.parent))
                self.tabs['SUSHAPE'] = 1
            else:
                pass
        elif tab_id=="SUFILTER":
            from filtering import sufilter
            if self.tabs['SUFILTER'] != 1:
                self.append_tab(self.parent, sufilter.nb_page(self.parent))
                self.tabs['SUFILTER'] = 1
            else:
                pass
        elif tab_id=="SUGETHW":
            from header_tools import sugethw
            if self.tabs['SUGETHW'] != 1:
                self.append_tab(self.parent, sugethw.nb_page(self.parent))
                self.tabs['SUGETHW'] = 1
            else:
                pass
        elif tab_id=="SUSHW":
            from header_tools import sushw
            if self.tabs['SUSHW'] != 1:
                self.append_tab(self.parent, sushw.nb_page(self.parent))
                self.tabs['SUSHW'] = 1
            else:
                pass
        elif tab_id=="A2B":
            from header_tools import a2b
            if self.tabs['A2B'] != 1:
                self.append_tab(self.parent, a2b.nb_page(self.parent))
                self.tabs['A2B'] = 1
            else:
                pass
        elif tab_id=="SUNMO":
            from moveout import sunmo
            if self.tabs['SUNMO'] != 1:
                self.append_tab(self.parent, sunmo.nb_page(self.parent))
                self.tabs['SUNMO'] = 1
            else:
                pass    
        elif tab_id=="SUSTACK":
            from stacking import sustack
            if self.tabs['SUSTACK'] != 1:
                self.append_tab(self.parent, sustack.nb_page(self.parent))
                self.tabs['SUSTACK'] = 1
            else:
                pass 
        elif tab_id=="SUFFT":
            from transforms import sufft
            if self.tabs['SUFFT'] != 1:
                self.append_tab(self.parent, sufft.nb_page(self.parent))
                self.tabs['SUFFT'] = 1
            else:
                pass 
        elif tab_id=="SURADON":
            from transforms import suradon
            if self.tabs['SURADON'] != 1:
                self.append_tab(self.parent, suradon.nb_page(self.parent))
                self.tabs['SURADON'] = 1
            else:
                pass 
        elif tab_id=="SUSPECFX":
            from transforms import suspecfx
            if self.tabs['SUSPECFX'] != 1:
                self.append_tab(self.parent, suspecfx.nb_page(self.parent))
                self.tabs['SUSPECFX'] = 1
            else:
                pass 
        elif tab_id=="SUVELAN":
            from velocity_analysis import suvelan
            if self.tabs['SUVELAN'] != 1:
                self.append_tab(self.parent, suvelan.nb_page(self.parent))
                self.tabs['SUVELAN'] = 1
            else:
                pass 
        elif tab_id=="SEGYREAD":
                from data_conversion import segyread
                if self.tabs['SEGYREAD'] != 1:
                    self.append_tab(self.parent, segyread.nb_page(self.parent))
                    self.tabs['SEGYREAD'] = 1
                else:
                    pass 
    
    def append_tab(self, parent, arg):  
        self.child =  arg
        self.page = self.child.page
        self.title =  self.child.title
        parent.notebook.append_page(self.page, self.title)
        parent.notebook.set_tab_detachable(self.page,True)
        parent.notebook.set_tab_reorderable(self.page,True)
        parent.notebook.set_current_page(parent.notebook.page_num(self.page))

            
            

