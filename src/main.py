import sys
import gi #GUI
#from factordb.factordb import FactorDB # FactorDB for prime factorization

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Defining window style attribs
        self.set_default_size (800, 600)
        self.set_title("Awful RSA cracker")

        #BOXES!
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) #Main box
        #TODO:generalizar la creacion de botones
        self.quitbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) #Quit button box


        self.set_child(self.mainbox)

        exp = input_field(desc="e:")
        exp.appnd(self.mainbox)
        
        n = input_field(desc="n (modulo):")
        n.appnd(self.mainbox)

        c = input_field(desc="ciphered message:")
        c.appnd(self.mainbox)


        #Defining child widgets 
        quitbutton = Gtk.Button(label="Quit") #quit button
        self.quitbox.append(quitbutton)
        self.mainbox.append(self.quitbox)

        # Things will go here


    def button1_onpress(self, button1):
        print("hello")

class input_field(): #Builds the boxes needed for a generic input field
    def __init__(self, desc):
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.entrybox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.descbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box.append(self.descbox)
        self.box.append(self.entrybox)

        self.entry = Gtk.Entry()
        self.desc = Gtk.Text(text=desc)

        self.entrybox.append(self.entry)
        self.descbox.append(self.desc)

    def appnd(self,parentbox):
        parentbox.append(self.box)

    def read(self,nose):
        str = self.entry.get_text()
        print(str)


    
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)