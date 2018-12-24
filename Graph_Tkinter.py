from tkinter import *
from tkinter import ttk
from Colours import colours

#clear funtion
def clear(frame):
    for wig in frame.grid_slaves():
        wig.grid_forget()
        
def f1(main,frame1):
    clear(frame1)
    #header names and graph title
    Label(frame1, text="Graph title:").grid(row=0,column=0, ipadx=5, ipady=2, padx=2, pady=2)#title
    Label(frame1, text="X header:").grid(row=1,column=0, ipadx=5, ipady=2, padx=2, pady=2)#xheader
    Label(frame1, text="Y header:").grid(row=2,column=0, ipadx=5, ipady=2, padx=2, pady=2)#yheader

    #headers and title inputs
    title, hx, hy = StringVar(),StringVar(),StringVar()
    Entry(frame1, textvariable=main.title).grid(row=0,column=1, ipadx=5,ipady=2, padx=2, pady=2)#title
    Entry(frame1, textvariable=main.hx).grid(row=1,column=1, ipadx=5, ipady=2, padx=2, pady=2)#xheader
    Entry(frame1, textvariable=main.hy).grid(row=2,column=1, ipadx=5, ipady=2, padx=2, pady=2)#yheader
    #formatting
    for wig in frame1.grid_slaves():
        #try to make uniform
        try:
            wig.config(fg="blue",width=20, justify="center" , bd=2, font=("Times",18))
        except:
            continue
    Label(frame1,text="ERROR: INVALID COLOR",fg="#EEE",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)
class series:
    def __init__(self,i,frame):
        #initialising stuff
        self.data = [[StringVar(),StringVar()]]
        self.name = StringVar()
        self.name.set("Series " + str(i))
        #set up colout
        self.colour = StringVar()
        self.colour.set("black")
        #set up line of best fit
        self.lobf = IntVar()
        self.frame = frame
        self.line_type = StringVar()
    def __str__(self):
        return self.name.get()
    def add(self,data):
        #add data
        self.data.append([StringVar(),StringVar()])
        f2(self.frame,data)#refresh
    def rem(self,data):
        if len(self.data) <= 1:#check if there is more than one data point
            data.remove(self)#delete series
        else:            
            self.data.pop(len(self.data)-1)#delete last input
        f2(self.frame,data)#refresh
    def but(self,data):
        #series-specific functions
        self.adder = Button(self.frame,text="Add",command=lambda:self.add(data), fg=self.colour.get())#add data
        self.remmer = Button(self.frame,text="Remove",command=lambda:self.rem(data), fg=self.colour.get())#remove data
        #sort out specific colour
        self.entry = Entry(self.frame, fg=self.colour.get(), width=5,font=("Times",14))#change colour (entry needs font setting)
        self.entry.insert(0,self.colour.get())#set default
        self.entry.config(textvariable=self.colour)#set variable after giving an initial value
        self.line = Checkbutton(self.frame,text="Line of best fit", var=self.lobf,fg=self.colour.get(),command=lambda:f2(self.frame,data))#lobf?
        self.lines = ["Linear","Power","Exponential"]
        #due to certain algorithms, some lines require positive points
        for point in self.data:
            if float(point[0].get()) <= 0:
                #remove if not yet removed
                try:
                    self.lines.remove("Power")
                except:
                    pass
            if float(point[1].get()) <= 0:
                #remove if not yet removed
                try:
                    self.lines.remove("Power")
                except:
                    pass
                #remove if not yet removed
                try:
                    self.lines.remove("Exponential")
                except:
                    pass
        #create an optionmenu for the lines
        if self.line_type.get() in self.lines:
            #if one is already selected
            self.line_type_select = ttk.OptionMenu(self.frame, self.line_type, self.line_type.get(),*self.lines)
        else:
            #linear is default
            self.line_type_select = ttk.OptionMenu(self.frame, self.line_type, self.lines[0],*self.lines)


def add_series(frame,data):
    k = False
    for i,s in enumerate(data):
        if s.name.get() != "Series " + str(i):#check if previous series is available
            data.insert(i, series(i,frame))#if so add it
            k = True
            break
    if not k:#if not, add a new one
        data.append(series(len(data),frame))
    #when data is ammended, refresh frame 2
    f2(frame,data)

def check(f,data):
    #check if data inputs are valid
    x = 0
    for s in data:
        for i in s.data:
            try:
                float(i[0].get())
            except:
                i[0].set("0")
                x = 1
            try:
                float(i[1].get())
            except:
                i[1].set("0")
                x = 1
    if x:#if nothing is wrong, we can leave it
        f2(f,data)

def f2(frame2,data):
        #clear
        clear(frame2)
        #refresh button
        Button(frame2, text="⟳", command=lambda:f2(frame2,data)).grid(column=2*len(data),row=0)
        #inputting information
        inputs(frame2,data)
        #formatting
        for wig in frame2.grid_slaves():
            try:
                if isinstance(wig,Entry):
                    wig.config(justify="center")#align anything center
                    continue#entry widgets get their own font (mainly for title)
                wig.config(justify="center", bd=2,font=("Times",14))#font needs to be the same
            except:
                continue
        #title
        Label(frame2, text="Data Points", justify="center",font=("Georgia",16,"bold underline")).grid(row=0,column=0, ipady=2, padx=2, pady=2,sticky="n",columnspan=2*len(data))

def inputs(frame,data):
    check(frame,data)
    for i,s in enumerate(data):
        s.colour.set(s.colour.get().strip().lower())
        if not s.colour.get() in colours:
            s.colour.set('black')
        colour = s.colour.get()#specific colour for each series
        #title
        title = Entry(frame,width=10, fg=colour)
        title.insert(0,s.name.get())
        title.grid(row=1,column=2*i,pady=2,columnspan=2)
        title.config(font=("Georgia",16,"bold"),textvariable=s.name)
        #x and y headers
        Label(frame,text="x", font=("bold"), fg=colour).grid(row=2,column=2*i)
        Label(frame,text="y", font=("bold"), fg=colour).grid(row=2,column=2*i+1)
        for j,d in enumerate(s.data):
            #create x inputs
            x = Entry(frame,width=6, fg=colour,font=("Times",14))#font does not get standardised
            x.insert(0,d[0])#set initial data
            x.grid(row=3+j,column=2*i,pady=2)#place x
            x.config(textvariable=d[0])#set variable after giving an initial value
            #create y inputs
            y = Entry(frame,width=6, fg=colour,font=("Times",14))#font does not get standardised
            y.insert(0,d[1])#set initial data
            y.grid(row=3+j,column=2*i+1,pady=2)#place y
            y.config(textvariable=d[1])#set variable after giving an initial value
        #get buttons with series-specific functions and place them in the grid
        s.but(data)

        #cannot remove everything
        if len(data)>1 or max(list(map(len,[s.data for s in data])))>1:
            s.adder.grid(row=len(s.data)+3,column=2*i)
            s.remmer.grid(row=len(s.data)+3,column=2*i+1)
        else:
            s.adder.grid(row=len(s.data)+3,column=2*i,columnspan=2)

        #line of best fit option appears only if there are two data points
        if len(s.data) > 1:
            s.line.grid(row=len(s.data)+4,column=2*i,columnspan=2)
            if s.lobf.get():
                s.entry.grid(row=len(s.data)+6,column=2*i+1)
                s.line_type_select.grid(row=len(s.data)+5,column=2*i,columnspan=2)
                Label(frame, text="Colour:", fg=colour).grid(row=len(s.data)+6,column=2*i)
            else:
                s.entry.grid(row=len(s.data)+5,column=2*i+1)
                Label(frame, text="Colour:", fg=colour).grid(row=len(s.data)+5,column=2*i)
        else:
            Label(frame, text="Colour:", fg=colour).grid(row=len(s.data)+4,column=2*i)
            s.entry.grid(row=len(s.data)+4,column=2*i+1)
            s.lobf.set(0)

    #for extra series
    Button(frame,text="Add series",command=lambda:add_series(frame,data)).grid(row=1,column=len(data)*2,rowspan=6+max(list(map(len,[s.data for s in data]))),sticky="ns")
    

class main_code:
    def __init__(self):
        #create root
        self.root = Tk()
        self.root.title("Graph Creator")
        self.canvas = Canvas(self.root)
        self.root.grid
        
        #title
        self.frame0 = Frame(self.root)
        self.frame0.grid(row=0,column=0)
        Label(self.frame0, text="Graph Creator", font=("Georgia",44, "bold underline")).grid(row=0,column=0, ipadx=5, ipady=2, padx=2, pady=2)

        #line
        ttk.Separator(self.root,orient="vertical").grid(row=0,column=1,rowspan=3,stick="ns")

        #create headings
        self.title = StringVar()
        self.hx = StringVar()
        self.hy = StringVar()
        
        #frame 1
        self.frame1 = Frame(self.root)
        self.frame1.grid(row=1,column=0)
        f1(self,self.frame1)

        #frame 2
        self.frame2 = Frame(self.root)
        #create data array
        self.data = [series(0,self.frame2)]
        #add to grid and run
        self.frame2.grid(row=0,column=2,columnspan=3,rowspan=2)
        f2(self.frame2,self.data)
        
    def f2(self):#method can be called from main code
        f2(self.frame2,self.data)
def run():
    global main
    main = main_code()
    return main


