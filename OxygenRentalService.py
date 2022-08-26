import sqlite3
import sys
import ORSdb
import datetime
from rental import rental
from customer import customer
from tkinter import messagebox

shop_list = []
cust = customer('default')
shop = rental('default')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import OxygenRentalService_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    ORSdb.create_conn()
    global val, w, root
    root = tk.Tk()
    OxygenRentalService_support.set_Tk_var()
    top = New_Toplevel (root)
    OxygenRentalService_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_New_Toplevel(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    OxygenRentalService_support.set_Tk_var()
    top = New_Toplevel (w)
    OxygenRentalService_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    ORSdb.conn.close()
    global w
    w.destroy()
    w = None

class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("693x569+356+151")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Oxygen Rental Service")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # Rental Shop Page

        self.Frame4 = tk.Frame(top)
        self.Frame4.place(relx=0.0, rely=0.0, relheight=1.014, relwidth=1.003)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Labelframe4 = tk.LabelFrame(self.Frame4)
        self.Labelframe4.place(relx=0.043, rely=0.04, relheight=0.273
                               , relwidth=0.906)
        self.Labelframe4.configure(relief='groove')
        self.Labelframe4.configure(foreground="black")
        self.Labelframe4.configure(text='''Shop details''')
        self.Labelframe4.configure(background="#d9d9d9")
        self.Labelframe4.configure(highlightbackground="#d9d9d9")
        self.Labelframe4.configure(highlightcolor="black")

        self.Label10 = tk.Label(self.Labelframe4)
        self.Label10.place(relx=0.032, rely=0.222, height=21, width=74
                           , bordermode='ignore')
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Shop Name:''')

        self.Label11 = tk.Label(self.Labelframe4)
        self.Label11.place(relx=0.032, rely=0.444, height=21, width=94
                           , bordermode='ignore')
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Available stock:''')

        self.Label12 = tk.Label(self.Labelframe4)
        self.Label12.place(relx=0.206, rely=0.222, height=21, width=144
                           , bordermode='ignore')
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Label''')

        self.Label13 = tk.Label(self.Labelframe4)
        self.Label13.place(relx=0.206, rely=0.444, height=21, width=154
                           , bordermode='ignore')
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''Label''')

        self.Label14 = tk.Label(self.Labelframe4)
        self.Label14.place(relx=0.508, rely=0.222, height=21, width=154
                           , bordermode='ignore')
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(anchor='w')
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''Increase/Decrease Stock:''')

        self.Spinbox3 = tk.Spinbox(self.Labelframe4, from_=1.0, to=100.0)
        self.Spinbox3.place(relx=0.516, rely=0.444, relheight=0.141
                            , relwidth=0.103, bordermode='ignore')
        self.Spinbox3.configure(activebackground="#f9f9f9")
        self.Spinbox3.configure(background="white")
        self.Spinbox3.configure(buttonbackground="#d9d9d9")
        self.Spinbox3.configure(disabledforeground="#a3a3a3")
        self.Spinbox3.configure(font="TkDefaultFont")
        self.Spinbox3.configure(foreground="black")
        self.Spinbox3.configure(highlightbackground="black")
        self.Spinbox3.configure(highlightcolor="black")
        self.Spinbox3.configure(insertbackground="black")
        self.Spinbox3.configure(selectbackground="blue")
        self.Spinbox3.configure(selectforeground="white")
        self.Spinbox3.configure(textvariable=OxygenRentalService_support.spinbox3)

        self.Button1 = tk.Button(self.Labelframe4, command = self.incr_stock)
        self.Button1.place(relx=0.651, rely=0.444, height=20, width=20
                           , bordermode='ignore')
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(anchor='s')
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''+''')

        self.Button2 = tk.Button(self.Labelframe4, command = self.decr_stock)
        self.Button2.place(relx=0.69, rely=0.444, height=20, width=20
                           , bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(anchor='s')
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''-''')

        self.Button3 = tk.Button(self.Labelframe4, command = self.log_out)
        self.Button3.place(relx=0.857, rely=0.667, height=24, width=67
                           , bordermode='ignore')
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Log Out''')

        self.Labelframe5 = tk.LabelFrame(self.Frame4)
        self.Labelframe5.place(relx=0.043, rely=0.343, relheight=0.576
                               , relwidth=0.906)
        self.Labelframe5.configure(relief='groove')
        self.Labelframe5.configure(foreground="black")
        self.Labelframe5.configure(text='''Current Renters''')
        self.Labelframe5.configure(background="#d9d9d9")

        self.Scrolledlistbox2 = ScrolledListBox(self.Labelframe5)
        self.Scrolledlistbox2.place(relx=0.048, rely=0.175, relheight=0.754
                                    , relwidth=0.906, bordermode='ignore')
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(cursor="xterm")
        self.Scrolledlistbox2.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(foreground="black")
        self.Scrolledlistbox2.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="blue")
        self.Scrolledlistbox2.configure(selectforeground="white")

        self.Label15 = tk.Label(self.Labelframe5)
        self.Label15.place(relx=0.048, rely=0.116, height=21, width=567
                           , bordermode='ignore')
        self.Label15.configure(anchor='w')
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(relief="raised")
        self.Label15.configure(
            text='''Name                                           Date                                                        Basis                    Qty.        Rate''')

        self.TSeparator2 = ttk.Separator(self.Labelframe5)
        self.TSeparator2.place(relx=0.3, rely=0.115, relheight=0.81
                               , bordermode='ignore')
        self.TSeparator2.configure(orient="vertical")

        self.TSeparator3 = ttk.Separator(self.Labelframe5)
        self.TSeparator3.place(relx=0.746, rely=0.115, relheight=0.81
                               , bordermode='ignore')
        self.TSeparator3.configure(orient="vertical")

        self.TSeparator4 = ttk.Separator(self.Labelframe5)
        self.TSeparator4.place(relx=0.603, rely=0.115, relheight=0.81
                               , bordermode='ignore')
        self.TSeparator4.configure(orient="vertical")

        self.TSeparator5 = ttk.Separator(self.Labelframe5)
        self.TSeparator5.place(relx=0.817, rely=0.115, relheight=0.81
                               , bordermode='ignore')
        self.TSeparator5.configure(orient="vertical")

        # customer rental page

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.0, rely=0.0, relheight=1.014, relwidth=1.003)
        self.Frame3.configure(relief='flat')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Labelframe2 = tk.LabelFrame(self.Frame3)
        self.Labelframe2.place(relx=0.505, rely=0.02, relheight=0.645
                , relwidth=0.462)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Rent Cylinders''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Labelframe2)
        self.Label2.place(relx=0.063, rely=0.254, height=34, width=84
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Select Basis:''')

        self.Radiobutton1 = tk.Radiobutton(self.Labelframe2)
        self.Radiobutton1.place(relx=0.063, rely=0.381, relheight=0.124
                , relwidth=0.65, bordermode='ignore')
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Hourly Basis - Rs 400 per hour''')
        self.Radiobutton1.configure(value=1)
        self.Radiobutton1.configure(variable=OxygenRentalService_support.selectedBasis)

        self.Label1 = tk.Label(self.Labelframe2)
        self.Label1.place(relx=0.063, rely=0.095, height=33, width=104
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Enter Amount:''')

        # change spinbox range to be stock of shop selected
        self.Spinbox1 = tk.Spinbox(self.Labelframe2, from_=1.0, to=5.0, state="readonly")
        self.Spinbox1.place(relx=0.406, rely=0.11, relheight=0.06
                , relwidth=0.266, bordermode='ignore')
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="blue")
        self.Spinbox1.configure(selectforeground="white")
        self.Spinbox1.configure(textvariable=OxygenRentalService_support.spinbox)

        self.Radiobutton2 = tk.Radiobutton(self.Labelframe2)
        self.Radiobutton2.place(relx=0.063, rely=0.54, relheight=0.124
                , relwidth=0.619, bordermode='ignore')
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Daily Basis - Rs 1500 per day''')
        self.Radiobutton2.configure(value=2)
        self.Radiobutton2.configure(variable=OxygenRentalService_support.selectedBasis)

        self.Radiobutton3 = tk.Radiobutton(self.Labelframe2)
        self.Radiobutton3.place(relx=0.063, rely=0.698, relheight=0.124
                , relwidth=0.681, bordermode='ignore')
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(text='''Weekly Basis - Rs 4000 per week''')
        self.Radiobutton3.configure(value=3)
        self.Radiobutton3.configure(variable=OxygenRentalService_support.selectedBasis)

        self.RentButton = tk.Button(self.Labelframe2, state = 'disabled', command = self.rent)
        self.RentButton.place(relx=0.719, rely=0.857, height=24, width=67
                , bordermode='ignore')
        self.RentButton.configure(activebackground="#ececec")
        self.RentButton.configure(activeforeground="#000000")
        self.RentButton.configure(background="#d9d9d9")
        self.RentButton.configure(disabledforeground="#a3a3a3")
        self.RentButton.configure(foreground="#000000")
        self.RentButton.configure(highlightbackground="#d9d9d9")
        self.RentButton.configure(highlightcolor="black")
        self.RentButton.configure(pady="0")
        self.RentButton.configure(text='''Rent''')

        self.Labelframe1 = tk.LabelFrame(self.Frame3)
        self.Labelframe1.place(relx=0.033, rely=0.023, relheight=0.922
                , relwidth=0.442)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Select Provider''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Scrolledlistbox1 = ScrolledListBox(self.Labelframe1)
        self.display_shop_details()
        self.Scrolledlistbox1.place(relx=0.065, rely=0.067, relheight=0.811,
                                    relwidth=0.853, bordermode='ignore')
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="hand2")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="blue")
        self.Scrolledlistbox1.configure(selectforeground="white")

        self.RefreshButton = tk.Button(self.Labelframe1, command = self.display_shop_details)
        self.RefreshButton.place(relx=0.686, rely=0.911, height=24, width=67
                                 , bordermode='ignore')
        self.RefreshButton.configure(activebackground="#ececec")
        self.RefreshButton.configure(activeforeground="#000000")
        self.RefreshButton.configure(background="#d9d9d9")
        self.RefreshButton.configure(disabledforeground="#a3a3a3")
        self.RefreshButton.configure(foreground="#000000")
        self.RefreshButton.configure(highlightbackground="#d9d9d9")
        self.RefreshButton.configure(highlightcolor="black")
        self.RefreshButton.configure(pady="0")
        self.RefreshButton.configure(text='''Refresh''')

        self.Labelframe3 = tk.LabelFrame(self.Frame3)
        self.Labelframe3.place(relx=0.505, rely=0.697, relheight=0.25
                               , relwidth=0.462)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Current Rental Status''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.Message1 = tk.Message(self.Labelframe3)
        self.Message1.place(relx=0.06, rely=0.246, relheight=0.598
                , relwidth=0.563, bordermode='ignore')
        self.Message1.configure(anchor='nw')
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''No cylinders rented yet''')
        self.Message1.configure(width=180)

        self.ReturnButton = tk.Button(self.Labelframe3, state = 'disabled', command = self.return_bttn)
        self.ReturnButton.place(relx=0.719, rely=0.4, height=24, width=67
                , bordermode='ignore')
        self.ReturnButton.configure(activebackground="#ececec")
        self.ReturnButton.configure(activeforeground="#000000")
        self.ReturnButton.configure(background="#d9d9d9")
        self.ReturnButton.configure(disabledforeground="#a3a3a3")
        self.ReturnButton.configure(foreground="#000000")
        self.ReturnButton.configure(highlightbackground="#d9d9d9")
        self.ReturnButton.configure(highlightcolor="black")
        self.ReturnButton.configure(pady="0")
        self.ReturnButton.configure(text='''Return''')

        self.LogOutButton = tk.Button(self.Labelframe3, command = self.log_out)
        self.LogOutButton.place(relx=0.719, rely=0.656, height=24, width=67
                                , bordermode='ignore')
        self.LogOutButton.configure(activebackground="#ececec")
        self.LogOutButton.configure(activeforeground="#000000")
        self.LogOutButton.configure(background="#d9d9d9")
        self.LogOutButton.configure(disabledforeground="#a3a3a3")
        self.LogOutButton.configure(foreground="#000000")
        self.LogOutButton.configure(highlightbackground="#d9d9d9")
        self.LogOutButton.configure(highlightcolor="black")
        self.LogOutButton.configure(pady="0")
        self.LogOutButton.configure(text='''Log Out''')

        # Starting Page

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.014, relwidth=1.003)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.0, rely=-0.04, relheight=1.04, relwidth=0.482)
        self.Frame2.configure(relief='flat')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.053, rely=0.35, height=21, width=150)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 14")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Welcome to''')

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.048, rely=0.388, height=51, width=299)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 22")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Oxygen Rental Service''')

        self.TSeparator1 = ttk.Separator(self.Frame2)
        self.TSeparator1.place(relx=0.065, rely=0.505, relwidth=0.779)

        self.Message2 = tk.Message(self.Frame2)
        self.Message2.place(relx=0.052, rely=0.524, relheight=0.064
                            , relwidth=0.6)
        self.Message2.configure(anchor='w')
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(font="-family {Segoe UI} -size 10")
        self.Message2.configure(foreground="#4f4f4f")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Rent oxygen cylinders flexibly.''')
        self.Message2.configure(width=190)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.662, rely=0.101, height=31, width=104)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 14")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''LOG IN''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.532, rely=0.263, height=21, width=73)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Log in as:''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.547, rely=0.364, height=21, width=34)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Name''')

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.547, rely=0.525, height=21, width=64)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Password''')

        self.TEntry1 = ttk.Entry(self.Frame1)
        self.TEntry1.place(relx=0.547, rely=0.424, relheight=0.042
                           , relwidth=0.368)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.Radiobutton4 = tk.Radiobutton(self.Frame1)
        self.Radiobutton4.place(relx=0.662, rely=0.263, relheight=0.051
                                , relwidth=0.141)
        self.Radiobutton4.configure(activebackground="#ececec")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="#ffffff")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(foreground="#000000")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify='left')
        self.Radiobutton4.configure(text='''Customer''')
        self.Radiobutton4.configure(value=1)
        self.Radiobutton4.configure(variable=OxygenRentalService_support.login_method)

        self.Radiobutton5 = tk.Radiobutton(self.Frame1)
        self.Radiobutton5.place(relx=0.835, rely=0.263, relheight=0.051
                                , relwidth=0.083)
        self.Radiobutton5.configure(activebackground="#ececec")
        self.Radiobutton5.configure(activeforeground="#000000")
        self.Radiobutton5.configure(background="#ffffff")
        self.Radiobutton5.configure(disabledforeground="#a3a3a3")
        self.Radiobutton5.configure(foreground="#000000")
        self.Radiobutton5.configure(highlightbackground="#d9d9d9")
        self.Radiobutton5.configure(highlightcolor="black")
        self.Radiobutton5.configure(justify='left')
        self.Radiobutton5.configure(text='''Shop''')
        self.Radiobutton5.configure(value=2)
        self.Radiobutton5.configure(variable=OxygenRentalService_support.login_method)

        self.TEntry2 = ttk.Entry(self.Frame1, show = '*')
        self.TEntry2.place(relx=0.547, rely=0.586, relheight=0.042
                           , relwidth=0.368)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.547, rely=0.687, height=21, width=214)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Stock (If creating new shop account):''')

        self.Spinbox2 = tk.Spinbox(self.Frame1, from_=1.0, to=999.0)
        self.Spinbox2.place(relx=0.849, rely=0.691, relheight=0.038
                            , relwidth=0.065)
        self.Spinbox2.configure(activebackground="#f9f9f9")
        self.Spinbox2.configure(background="white")
        self.Spinbox2.configure(buttonbackground="#d9d9d9")
        self.Spinbox2.configure(disabledforeground="#a3a3a3")
        self.Spinbox2.configure(font="TkDefaultFont")
        self.Spinbox2.configure(foreground="black")
        self.Spinbox2.configure(highlightbackground="black")
        self.Spinbox2.configure(highlightcolor="black")
        self.Spinbox2.configure(insertbackground="black")
        self.Spinbox2.configure(selectbackground="blue")
        self.Spinbox2.configure(selectforeground="white")
        self.Spinbox2.configure(textvariable=OxygenRentalService_support.spinbox2)

        self.new_button = ttk.Button(self.Frame1, command = self.create_new)
        self.new_button.place(relx=0.835, rely=0.808, height=25, width=56)
        self.new_button.configure(takefocus="")
        self.new_button.configure(text='''New''')

        self.existing_button = ttk.Button(self.Frame1, command = self.login_bttn)
        self.existing_button.place(relx=0.705, rely=0.808, height=25, width=76)
        self.existing_button.configure(takefocus="")
        self.existing_button.configure(text='''Existing''')

        OxygenRentalService_support.spinbox.trace('w', self.check_rent_inputs)
        OxygenRentalService_support.selectedBasis.trace('w', self.check_rent_inputs)

    def create_new(self):
        userType = OxygenRentalService_support.login_method.get()
        name = self.TEntry1.get()

        if userType == 1:
            try:
                ORSdb.insert_customer(name)
                messagebox.showinfo("Information", "Account successfully created!")
            except Exception:
                messagebox.showwarning("Warning", "User name already taken!")

        if userType == 2:
            stockCount = int(OxygenRentalService_support.spinbox2.get())
            try:
                ORSdb.insert_shop(name, stockCount, stockCount)
                messagebox.showinfo("Information", "Account successfully created!")
            except Exception:
                messagebox.showwarning("Warning", "Shop name already taken!")

        ORSdb.conn.commit()
        ORSdb.display_tables()


    def login_bttn(self):
        userType = OxygenRentalService_support.login_method.get()

        if userType == 1:
            name = self.TEntry1.get()
            ORSdb.cursr.execute("SELECT * FROM CUSTOMER WHERE NAME = (?)", (name,))
            custRecord = ORSdb.cursr.fetchall()

            if len(custRecord) == 0:
                messagebox.showwarning("Warning", "User not found.")

            else:
                if custRecord[0][1] == None:
                    global cust
                    cust = customer(name)

                else:
                    cust = customer(name, custRecord[0][1], custRecord[0][2], custRecord[0][3], datetime.datetime.strptime(custRecord[0][4], '%Y-%m-%d %H:%M:%S.%f'), custRecord[0][5])
                    if cust.rentalBasis == 1:
                        basis_text = 'Hourly'
                    elif cust.rentalBasis == 2:
                        basis_text = 'Daily'
                    else:
                        basis_text = 'Weekly'
                    self.ReturnButton['state'] = tk.NORMAL
                    self.Message1.configure(text=str(cust.cylinders) + ' cylinder(s) rented from ' + cust.shopName
                                             + '\n\nRental basis: ' + basis_text
                                             + '\nTime of rent: ' + cust.rentalTime.strftime('%d-%m-%Y %H:%M:%S'))

                for x in ORSdb.conn.execute("SELECT * FROM RENTAL"):
                    shop_list.append(rental(x[0], x[1], x[2]))

                self.display_shop_details()
                self.Frame3.tkraise()

        if userType == 2:
            name = self.TEntry1.get()
            ORSdb.cursr.execute("SELECT * FROM RENTAL WHERE NAME = (?)", (name,))
            shopRecord = ORSdb.cursr.fetchall()

            if len(shopRecord) == 0:
                messagebox.showwarning("Warning", "User not found.")

            else:
                global shop
                shop = rental(name, shopRecord[0][1], shopRecord[0][2])
                self.Label12.configure(text = name)
                self.Label13.configure(text = str(shop.stock)+' (Total = '+str(shop.stockTotal)+')')

                self.Scrolledlistbox2.delete(0, tk.END)
                for x in ORSdb.conn.execute("SELECT NAME, RENTAL_TIME, RENTAL_BASIS, CYLINDERS FROM CUSTOMER WHERE SHOP = (?)", (name,)):
                    i = 0
                    s1 = 20 - len(x[0])
                    if x[2] == 1:
                        basis_text = 'Hourly'
                        rate_text = 'Rs 400'
                        s2 = 5
                    elif x[2] == 2:
                        basis_text = 'Daily'
                        rate_text = 'Rs 1500'
                        s2 = 6
                    else:
                        basis_text = 'Weekly'
                        rate_text = 'Rs 4000'
                        s2 = 6

                    self.Scrolledlistbox2.insert(i, x[0]+" "*s1+x[1][:19]+" "*5+basis_text+" "*s2+str(x[3])+" "*5+rate_text)

                self.Frame4.tkraise()

    def log_out(self):
        global shop_list
        global shop
        global cust
        shop_list = []
        shop = rental('Default')
        cust = customer('Default')
        OxygenRentalService_support.spinbox.set('')
        OxygenRentalService_support.selectedBasis.set(0)
        self.Message1.configure(text='''No cylinders rented yet''')
        self.Label12.configure(text='')
        self.Label13.configure(text='')
        self.Scrolledlistbox2.delete(0, tk.END)
        OxygenRentalService_support.spinbox3.set('')
        self.TEntry1.delete(0, tk.END)
        self.TEntry2.delete(0, tk.END)
        OxygenRentalService_support.login_method.set(0)
        OxygenRentalService_support.spinbox2.set('')

        self.Frame1.tkraise()

    def incr_stock(self):
        n = int(OxygenRentalService_support.spinbox3.get())
        shop.stock += n
        shop.stockTotal += n
        ORSdb.increase_stock(shop.name, n)
        ORSdb.conn.commit()
        self.Label13.configure(text=str(shop.stock) + ' (Total = ' + str(shop.stockTotal) + ')')

    def decr_stock(self):
        n = int(OxygenRentalService_support.spinbox3.get())
        shop.stock -= n
        shop.stockTotal -= n
        ORSdb.decrease_stock(shop.name, n)
        ORSdb.conn.commit()
        self.Label13.configure(text=str(shop.stock) + ' (Total = ' + str(shop.stockTotal) + ')')


    def display_shop_details(self):
        self.Scrolledlistbox1.delete(0, tk.END)
        for i in range(len(shop_list)):
            self.Scrolledlistbox1.insert(i, shop_list[i].displaystock())

    def check_rent_inputs(self, var, index, mode):
        n = OxygenRentalService_support.spinbox.get()
        b = OxygenRentalService_support.selectedBasis.get()
        name, cylinder, basis, time = cust.displayDetails()
        if n and b and not(cylinder):
            self.RentButton['state'] = tk.NORMAL
        else:
            self.RentButton['state'] = tk.DISABLED

    def rent(self):
        s = self.Scrolledlistbox1.curselection()
        n = int(OxygenRentalService_support.spinbox.get())
        b = OxygenRentalService_support.selectedBasis.get()

        if len(s) == 0:
            messagebox.showinfo("Information", "Please select a rental provider!")

        elif shop_list[s[0]].stock < n:
            messagebox.showwarning("Warning", "Quantity of cylinders requested is greater than that available from the selected shop!")

        else:

            cust.shopName = self.Scrolledlistbox1.get(s[0]).split(" ")[0]

            if b == 1:
                cust.rentalTime = shop_list[s[0]].rentHourlyBasis(cust.requestCylinder(n))
                cust.rentalBasis = 1

            if b == 2:
                cust.rentalTime = shop_list[s[0]].rentDailyBasis(cust.requestCylinder(n))
                cust.rentalBasis = 2

            if b == 3:
                cust.rentalTime = shop_list[s[0]].rentWeeklyBasis(cust.requestCylinder(n))
                cust.rentalBasis = 3

            messagebox.showinfo("Information", "Cylinders successfully rented.")
            self.RentButton['state'] = tk.DISABLED
            self.ReturnButton['state'] = tk.NORMAL
            self.display_shop_details()

            name, cylinder, basis, time = cust.displayDetails()
            if basis == 1:
                basis_text = 'Hourly'
            elif basis == 2:
                basis_text = 'Daily'
            else:
                basis_text = 'Weekly'

            self.Message1.configure(text = str(cylinder)+' cylinder(s) rented from '+cust.shopName
                                    +'\n\nRental basis: '+basis_text
                                    +'\nTime of rent: '+time.strftime('%d-%m-%Y %H:%M:%S'))

            ORSdb.update_rent(cust.name, cylinder, name, basis, time)
            ORSdb.conn.commit()
            ORSdb.display_tables()

    def return_bttn(self):
        cust_shop = [x for x in shop_list if x.name == cust.shopName][0]
        cust.bill = cust_shop.returnCylinder(cust.returnCylinder())
        ORSdb.update_return(cust.name, cust_shop.name, cust.cylinders)
        ORSdb.conn.commit()
        cust.shopName = None
        cust.rentalBasis, cust.rentalTime, cust.cylinders = None, None, None
        messagebox.showinfo('Information', 'Cylinders returned successfully.\nYour bill amount is Rs '+str(cust.bill))
        self.Message1.configure(text = 'No cylinders rented.')
        self.ReturnButton['state'] = tk.DISABLED
        self.display_shop_details()
        ORSdb.display_tables()
# includes the GUI Elements and event definitions



# The following code is added to facilitate the Scrolled widgets specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





