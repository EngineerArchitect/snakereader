# -*- coding: utf8 -*-
"""Snake Reader is Optical Character Recognition program fully written in Python by students of Wrocław University of Technology (Computer Science). Program uses neural network in recognition stage and optional dictionary checking later. It has it's own GUI but can also be used by a command line (as a plugin).\n
Interface module enables communication beetwen user and program. After program start an object from GUI class are created. When in command line something more than the name of program is (name of input, output file and options), the CommandLine cless object are created"""
import sys
import wx
import os

sys.path.append(sys.path[0]+"\\files")

from control import *
class GUI(Control) :
    """Grafical interface class inherit from Control class. In GUI is another method: showInterface"""
    def showInterface(self) :
        """Opens grafical interface (an object from wx.Frame class)"""
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        Snakereader = MyFrame(None, -1, "")
        app.SetTopWindow(Snakereader)
        Snakereader.Show()
        app.MainLoop()
class CommandLine(Control) :
    """Activates when program starts from command line. CommandLine class inherit from Control class. In CommandLine is another method: readCommandLine"""
    def readCommandLine(self) :
        """Reads and changes options"""
        for i in range (0, len(sys.argv)):
            if sys.argv[i] == '-d':
                self.options[0] = sys.argv[i+1]
            if sys.argv[i] == '-s':
                self.options[1] = sys.argv[i+1]
            if sys.argv[i] == '-r':
                self.options[2] = sys.argv[i+1]
            if sys.argv[i] == '-q':
                self.options[3] = sys.argv[i+1]
            if sys.argv[i] == '-rq':
                self.options[4] = sys.argv[i+1]
            if sys.argv[i] == '-p':
                self.options[5] = sys.argv[i+1]

#-----------------GUI----------------#

ID_OPEN = 11
ID_SAVE = 12
ID_EXIT = 13

ID_OPT = 21
ID_DEF = 22
ID_SAVE_O = 23

ID_O_OK = 211
ID_O_CA = 212

ID_RECOG = 31

ID_DOCUM = 41
ID_REQUIR = 42
ID_ABOUT = 43

ID_OPEN_B = 51
ID_RECOG_B = 52
ID_SAVE_B = 53
ID_OPT_B = 54

class Options(wx.Frame):
    """Opens window with options. User can make changes: choose a dictionary, choose quality of dictionary verification and give some helpful technical data: Font size, Scan resolution"""
    def __init__(self, dicList, *args, **kwds):
        """Class costructor. There all elements (buttons, radioboxes, lines, etc.)are created"""
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_4 = wx.StaticText(self, -1, "")
        self.radio_box_1 = wx.RadioBox(self, -1, "Choose a dictonary", choices=dicList, majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_2 = wx.RadioBox(self, -1, "Choose quality", choices=["ok","poor"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.radio_box_3 = wx.RadioBox(self, -1, "Choose recognition quality", choices=["good","poor"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.static_line_1 = wx.StaticLine(self, -1)
        self.label_5 = wx.StaticText(self, 5, "Technical data:")
        self.label_6 = wx.StaticText(self, -1, "Font size   ")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, interface.options[1])
        self.label_7 = wx.StaticText(self, -1, "Scan resolution   ")
        self.text_ctrl_4 = wx.TextCtrl(self, -1, interface.options[2])
        self.label_8 = wx.StaticText(self, -1, "Parameters file   ")
        self.text_ctrl_5 = wx.TextCtrl(self, -1, interface.options[5])
        self.static_line_2 = wx.StaticLine(self, -1)
        self.button_1 = wx.Button(self, ID_O_OK, "OK")
        self.button_2 = wx.Button(self, ID_O_CA, "Cancel")
        wx.EVT_BUTTON(self.button_1, ID_O_OK, self.OnOK)
        wx.EVT_BUTTON(self.button_2, ID_O_CA, self.OnCancel)
        self.__set_properties()
        self.__do_layout()
        
        # end wxGlade
        
    def OnOK(self, e):
        """Approves all changes"""
        interface.options[0] = interface.dictionaries[self.radio_box_1.GetSelection()]
        interface.options[1] = self.text_ctrl_3.GetValue()
        interface.options[2] = self.text_ctrl_4.GetValue()
        interface.options[5] = self.text_ctrl_5.GetValue()
        if self.radio_box_2.GetSelection()==0:
            interface.options[3] = "ok"
        else:
            interface.options[3] = "poor"
        if self.radio_box_3.GetSelection()==0:
            interface.options[4] = "1"
        else:
            interface.options[4] = "0"
        self.Close(True)

    def OnCancel(self, e):
        """Annuls all changes"""
        self.Close(True)
        
    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Options")
        self.SetSize((400, 400))
        self.SetBackgroundColour(wx.Colour(236, 233, 216))
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.radio_box_1.SetSelection(interface.dictionaries.index(interface.options[0]))
        if interface.options[3]=="ok":
            self.radio_box_2.SetSelection(0)
        else:
            self.radio_box_2.SetSelection(1)
        if interface.options[4]=="1":
            self.radio_box_3.SetSelection(0)
        else:
            self.radio_box_3.SetSelection(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(2, 2, 0, 0)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11.Add(self.label_4, 0, 0, 0)
        sizer_12.Add(self.radio_box_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_12.Add(self.radio_box_2, 0, 0, 0)
        sizer_12.Add(self.radio_box_3, 0, 0, 0)
        sizer_11.Add(sizer_12, 200, wx.EXPAND, 0)
        sizer_11.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_10.Add(sizer_11, 3, wx.EXPAND, 0)
        sizer_13.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 0, 0, 0)
        grid_sizer_1.Add(self.label_7, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 0, 0, 0)
        grid_sizer_1.Add(self.label_8, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add(self.text_ctrl_5, 0, 0, 0)
        sizer_15.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_14.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_13.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_13.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_10.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_2.Add(self.button_2, wx.ALIGN_RIGHT, 5, 0)
        sizer_2.Add(self.button_1, wx.ALIGN_RIGHT, 5, 0)
        sizer_10.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_10, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class Options

class MyScroll(wx.ScrolledWindow):
    """A place for a preview of input file"""
    def __init__(self, parent, id = -1, size = 356, bitmap=None):
        """Class costructor."""
        wx.ScrolledWindow.__init__(self, parent, id, wx.Point(0, 0), (350,700), wx.SUNKEN_BORDER)
        if bitmap!=None:
            """self.bitmap_2 = wx.Image((bitmap), wx.BITMAP_TYPE_ANY)
            W = self.bitmap_2.GetWidth()
            H = self.bitmap_2.GetHeight()
            if (W/H > 350/700):
                NewW = 350
                NewH = 350 * H / W
            else:
                NewH = 700
                NewW = 700 * W / H
            self.bitmap_2 = self.bitmap_2.Scale(NewW,NewH)
            bitmap = self.bitmap_2"""
            self.buffer=wx.Bitmap(bitmap)
        else:
            self.buffer=wx.EmptyBitmap(350,700)
        dc=wx.BufferedDC(None, self.buffer)

        wx.EVT_PAINT(self,self.OnPaint)
        
    def OnPaint(self,event):
        """Draw input bitmap or jpg on screen"""
        dc = wx.BufferedPaintDC(self,self.buffer)

# end of class MyScroll

class MyFrame(wx.Frame):
    """Main window"""
    def __init__(self, *args, **kwds):
        """Class costructor. MenuBar, ToolBar, place for bitmap prwview and final text are created there"""
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.Snakereader_menubar = wx.MenuBar()
        self.SetMenuBar(self.Snakereader_menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(11, "Open", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(12, "Save", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(13, "Exit", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(21, "Options", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(22, "Default", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(23, "Save Options", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "Options")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(31, "Recognize", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "Recognize")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(41, "Documention", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(42, "Requirements", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(43, "About Snakereader", "", wx.ITEM_NORMAL)
        self.Snakereader_menubar.Append(wxglade_tmp_menu, "Help")
        # Menu Bar end
        
        # Tool Bar
        self.Snakereader_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.Snakereader_toolbar)
        self.Snakereader_toolbar.AddLabelTool(51, "Open", wx.Bitmap(".//files//Open.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Open", "")
        self.Snakereader_toolbar.AddLabelTool(52, "Recognize", wx.Bitmap(".//files//Recognize.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Recognize", "")
        self.Snakereader_toolbar.AddLabelTool(53, "Save", wx.Bitmap(".//files//Save.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Save", "")
        self.Snakereader_toolbar.AddSeparator()
        self.Snakereader_toolbar.AddLabelTool(54, "Options", wx.Bitmap(".//files//Options.bmp", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Options", "")
        # Tool Bar end

        
        self.bitmap = MyScroll(self)
        
        self.static_line = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        self.picture = None
        scroll=wx.ScrolledWindow(self,-1)
        self.text = "An outcome text will be there"
        self.text_ctrl = wx.TextCtrl(self, -1, self.text, style=wx.TE_MULTILINE)
        
        self.__set_properties()
        self.__do_layout(self.bitmap)

        self.Bind(wx.EVT_MENU, self.a, id=11)
        # end wxGlade
        

        wx.EVT_MENU(self, ID_OPEN, self.OnOpen)
        wx.EVT_MENU(self, ID_SAVE, self.OnSave)
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)
        wx.EVT_MENU(self, ID_OPT, self.OnOpt)
        wx.EVT_MENU(self, ID_DEF, self.OnDef)
        wx.EVT_MENU(self, ID_SAVE_O, self.OnSaveO)
        wx.EVT_MENU(self, ID_RECOG, self.OnRecog)
        #wx.EVT_MENU(self, ID_DOCUM, self.OnDocum)
        wx.EVT_MENU(self, ID_REQUIR, self.OnRequir)
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
        wx.EVT_TOOL(self, ID_OPEN_B, self.OnOpen)
        wx.EVT_TOOL(self, ID_RECOG_B, self.OnRecog)
        wx.EVT_TOOL(self, ID_SAVE_B, self.OnSave)
        wx.EVT_TOOL(self, ID_OPT_B, self.OnOpt)
      


    def OnOpen(self,e):
        """Read in input file, and creates MyScroll class object to display a preview"""
        self.dirname = ''
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.filename=dialog.GetFilename()
            self.dirname=dialog.GetDirectory()
            self.picture = interface.inputFile(unicode.encode(self.dirname+"\\"+self.filename))
            self.bitmap_1 = (unicode.encode(self.dirname+"\\"+self.filename))

            """ tu jest skalowanie, ale na obrazku,
                po skalowaniu otrzymujemy tez obrazek.
                No i nie mozna go podac do MyScroll,
                tzn. nie mozna zrobic czegos takiego:
                self.bitmap = MyScroll(self, bitmap = self.bitmap_2)
                nie bylo by problemu gdyby bitmap_2 byla zadana jak 7 linijek wyzej.
                Rozwiazaniem mogloby byc zapisanie bitmap_2
                do jakiegos pliku tymczasowego, wywolanie MyScroll
                i zniszczenie pliku, ale to troche niefajna metoda
                moze masz jakis pomysl??
            
            self.bitmap_2 = wx.Image(unicode.encode(self.dirname+"\\"+self.filename), wx.BITMAP_TYPE_ANY) 
            W = self.bitmap_2.GetWidth()
            H = self.bitmap_2.GetHeight()
            if (W/H > 350/700):
                NewW = 350
                NewH = 350 * H / W
            else:   
                NewH = 700
                NewW = 700 * W / H
            self.bitmap_2 = self.bitmap_2.Scale(NewW,NewH)"""
            
            self.bitmap = MyScroll(self)
            self.__do_layout(self.bitmap)
            self.bitmap = MyScroll(self, bitmap = self.bitmap_1)
            self.__do_layout(self.bitmap)

        dialog.Destroy()

    def OnSave(self,e):
        """Save final text (or modyfied by user) in  indicated file """
        self.dirname = ''
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            self.filename=dialog.GetFilename()+".txt"
            self.dirname=dialog.GetDirectory()
            outputFile = open(os.path.join(self.dirname, self.filename), "w")
            outputFile.write(self.text_ctrl.GetValue())
            outputFile.close()

    def OnExit(self,e):
        """Close main window"""
        self.Close(True)
    
    def OnOpt(self,e):
        """Creates an optionsWindow - Options class object"""
        optionsWindow=Options(interface.dictionaries, None)
        optionsWindow.Show()

    def OnDef(self,e):
        """Set default options (without dictionry veryfication, no data about font size and scan resolution)"""
        interface.options=['None','','','ok','1','parameters.bin']

    def OnSaveO(self,e):
        """Save current (seted by user) options in file"""
        interface.saveOptions()

    def OnRecog(self,e):
        """Sets program working"""
        maxValue=1
        dialog = wx.ProgressDialog("Recognition", "Please wait...", maxValue, style = wx.PD_ELAPSED_TIME|wx.PD_APP_MODAL|wx.PD_SMOOTH)
        try:
            self.text=interface.textRecognition(self.picture)
        except (IOError,AttributeError), details:
            print "Error:", details
            dialog.Destroy()
        value=1
        dialog.Update(value,"Done")
        self.text_ctrl.Destroy()
        self.text_ctrl = wx.TextCtrl(self, -1, self.text, style=wx.TE_MULTILINE)
        self.__set_properties()
        self.__do_layout(self.bitmap)
        dialog.Destroy()

    #def OnDocum(self,e):
    
    def OnRequir(self,e):
        """Shows message dialog with requirements to input data"""
        dialog = wx.MessageDialog(self, "INPUT DATA:\n"
                                  "text document as a picture (bmp or jpg format):\n"
                                  "\t - polish language,\n"
                                  "\t - not handwriting,\n"
                                  "\t - text (and background) in one colour and tint,\n"
                                  "\t - contrast between text and background,\n"
                                  "\t - resolution min 300dpi,\n"
                                  "\t - homogeneous arrangement (without text areas, pictures, etc.)\n\n"
                                  "OUTPUT DATA:\n"
                                  "document converted to an electronic form and saved in txt format", "Requirements", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

        
    def OnAbout(self,e):
        """Shows message dialog with informations abaut program"""
        dialog = wx.MessageDialog(self, "Snakereader is an Open Source project \n"
                                  "created by students of Wroclaw University of Technology \n\n"
                                  "Wroclaw, 2007","About", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()     
    

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Snakereader")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap(".//files//Snake.bmp", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((1000, 581))
        self.Snakereader_toolbar.SetToolBitmapSize((30, 30))
        self.Snakereader_toolbar.Realize()
        self.text_ctrl.SetMinSize((675, 488))
        # end wxGlade

    def __do_layout(self, bitmap):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.bitmap, 0, 0, 0)
        sizer_1.Add(self.static_line, 0, wx.EXPAND, 0)
        sizer_1.Add(self.text_ctrl, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def a(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `a' not implemented!"
        event.Skip()

# end of class MyFrame







#-----------------INTERFACE----------------#
                
##sys.argv.append('1lin7.bmp')
##sys.argv.append('a.txt')
##sys.argv.append('-q')
##sys.argv.append('poor')
if len(sys.argv)>1:
    commandLine=CommandLine()
    commandLine.readCommandLine()
    try:
        picture=commandLine.inputFile(sys.argv[1])
    except IOError, details:
        print "Error:", details
    else:
        try:
            text=commandLine.textRecognition(picture)
        except IOError, details:
            print "Error:", details
        else:
            outputFile=open(sys.argv[2],'w')
            outputFile.write(text)
            outputFile.close()
else:
    interface=GUI()
    interface.showInterface()
