import Graph_Tkinter
from tkinter import *
import math
import turtle as tur
from Colours import colours

def plot(point,colour = "black"):
    x = point[0]
    y = point[1]
    #plots a point
    tur.color(colour)
    tur.pu()
    tur.goto(x-5,y-5)
    tur.pd()
    tur.goto(x+5,y+5)
    tur.pu()
    tur.goto(x+5,y-5)
    tur.pd()
    tur.goto(x-5,y+5)
class Graph:
    def __init__(self,point_array,title,x_head,y_head):
        try:
            tur.reset()
        except:
            pass
        tur.ht()
        tur.speed(0)
        self.points = point_array
        self.xs = []
        self.ys = []
        for x in self.points:
            #splits up the xs and ys into arrays
            self.xs.append(x[0])
            self.ys.append(x[1])
        #stores headings
        self.t = title
        self.x_heading = x_head
        self.y_heading = y_head
        self.graph()
    def values(self):
        #finds max and min
        self.max_x = max(self.xs)
        self.max_y = max(self.ys)
        self.min_x = min(self.xs)
        self.min_y = min(self.ys)
        #finds powers and bases 
        if self.max_x-self.min_x != 0:
            self.x_n = int(math.log10(self.max_x-self.min_x)//1)
        elif self.max_x != 0:
            self.x_n = int(math.log10(self.max_x)//1)
        else:
            self.x_n = 0
        if self.max_y-self.min_y != 0:
            self.y_n = int(math.log10(self.max_y-self.min_y)//1)
        elif self.max_y != 0:
            self.y_n = int(math.log10(self.max_y)//1)
        else:
            self.y_n = 0
        #rounds to find a suitable range
        self.x_a = math.ceil(self.max_x/(10**self.x_n))*10**self.x_n
        self.y_a = math.ceil(self.max_y/(10**self.y_n))*10**self.y_n
        self.x_b = self.min_x//(10**self.x_n)*10**self.x_n
        self.y_b = self.min_y//(10**self.y_n)*10**self.y_n
        self.x_range = self.x_a - self.x_b
        #if you have the same x, the range is 1 to avoid div 0 erros
        if self.x_range == 0:
            self.x_range = 1
        self.y_range = self.y_a - self.y_b
        #if you have the same y, the range is 1 to avoid div 0 erros
        if self.y_range == 0:
            self.y_range = 1
        #origin for mapping
        self.x_origin = -500
        self.y_origin = -250
        origin = [self.x_origin,self.y_origin]

    def scale_p(self,point):
        #splits up a point array before scaling
        x = point[0]
        y = point[1]
        self.new_x = (((x - self.x_b) * 1000)/self.x_range) + self.x_origin
        self.new_y = (((y - self.y_b) * 500)/self.y_range) + self.y_origin
        return [self.new_x,self.new_y]
    def scale_x(self,x):
        #just scales in the x direction
        self.new_x = (((x - self.x_b) * 1000)/self.x_range) + self.x_origin
        return self.new_x
    def scale_y(self,y):
        #just scales in the y direction
        self.new_y = (((y - self.y_b) * 500)/self.y_range) + self.y_origin
        return self.new_y
    def axis(self,colour = "black"):
        #draws two axis
        tur.pu()
        tur.color(colour)
        tur.goto(self.x_origin,0-self.y_origin)
        tur.pd()
        tur.goto(self.x_origin,self.y_origin)
        tur.goto(0-self.x_origin,self.y_origin)
    def headings(self,tit,x_head,y_head):
        #writes the axis names
        tur.pu()
        tur.goto(0,50-self.y_origin)
        tur.pd()
        tur.write(tit,False,"center",("Times",24,"underline"))
        tur.pu()
        tur.goto(self.x_origin-50, 0)
        tur.pd()
        tur.write(y_head,False,"right",("Times",14,"underline"))
        tur.pu()
        tur.goto(0, self.y_origin-75)
        tur.seth(0)
        tur.pd()
        tur.write(x_head,False,"center",("Times",14,"underline"))
    def numbers(self):
        #writes the numbers on the axis at even intervals
        x = self.x_b
        while x <= self.x_a:
            tur.pu()
            tur.goto(self.scale_x(x),self.y_origin - 25)
            tur.pd()
            try:
                x = int(x)
            except:
                pass
            tur.write(str(x),False,"center",("Times",11,"normal"))
            if self.x_n > 0:
                x += 10**self.x_n
                x = round(x,-self.x_n+1)
            else:   
                x += 10/(10**math.fabs(self.x_n))/10
                x = round(x,-self.x_n)
        y = self.y_b
        while y <= self.y_a: 
            tur.pu()
            tur.goto(self.x_origin - 25,self.scale_y(y))
            tur.pd()
            try:
                y = int(y)
            except:
                pass
            tur.write(str(y),False,"center",("Times",11,"normal"))
            if self.y_n > 0:
                y += 10**self.y_n
                y = round(y,-self.y_n+1)
            else:   
                y += 10/(10**math.fabs(self.y_n))/10
                y = round(y,-self.y_n)
    def plot_points(self):
        #self explanitory
        for point in self.points:
            self.new = self.scale_p(point)
            plot(self.new,self.colour)
    def graph(self):
        #the different sections that need doing to create a graph template
        self.values()
        self.axis()
        self.headings(self.t,self.x_heading,self.y_heading)
        self.numbers()
    def mean(self,xs,ys):
        #finds the mean xs and ys
        self.x_mean = sum(xs)/len(ys)
        self.y_mean = sum(ys)/len(ys)
        self.mean_point = [self.x_mean,self.y_mean]
    def mean_distances(self,mean,point):
        #finds numbers for the gradient
        self.mean_distance = 0.0
        self.x_squared_distance = 0.0
        for y in point:
            self.mean_distance += (y[0] - mean[0])*(y[1] - mean[1])
            self.x_squared_distance += (y[0] - mean[0])**2
    def find_gradient(self,num1,num2):
        #finds the gradient
        if num2 == 0:
            #removes a div 0 error
            self.gradient = None
        else:
            self.gradient = num1/num2
    def find_bias(self,mean,gradient):
        #finds the y-intercept
        if gradient == None:
            #if there is an infinite gradient, it never crosses the y axis
            self.bias = 0
        else:
            self.bias = mean[1] - (gradient * mean[0])
    def linear_draw(self,colour = "black"):
        #draws the line
        tur.pu()
        tur.color(colour)
        if self.gradient == None:
            #specific graph if no gradient
            self.no_gradient()
        else:
            self.new_x_a = (self.y_b - self.bias) / self.gradient
            self.new_y_a = self.x_b * self.gradient + self.bias
            self.new_x_b = (self.y_a - self.bias) / self.gradient
            self.new_y_b = self.x_a * self.gradient + self.bias
            #go to two of the four sides the line crosses
            if self.new_x_a >= self.x_b and self.new_x_a <= self.x_a:
                tur.goto(self.scale_x(self.new_x_a),self.scale_y(self.y_b))
                tur.pd()
            if self.new_y_a >= self.y_b and self.new_y_a <= self.y_a:
                tur.goto(self.scale_x(self.x_b),self.scale_y(self.new_y_a))
                tur.pd()
            if self.new_x_b >= self.x_b and self.new_x_b <= self.x_a:
                tur.goto(self.scale_x(self.new_x_b),self.scale_y(self.y_a))
                tur.pd()
            if self.new_y_b >= self.y_b and self.new_y_b <= self.y_a:
                tur.goto(self.scale_x(self.x_a),self.scale_y(self.new_y_b))
    def no_gradient(self):
        #in this case, there is not change in x
        tur.goto(self.scale_x(self.x_a),self.scale_y(self.min_y))
        tur.goto(self.scale_x(self.x_b),self.scale_y(self.min_y))
        print("x = " + str(self.min_x))
    def power_draw(self,colour = "black"):
        #draws the line
        tur.pu()
        tur.color(colour)
        if self.gradient == None:
            #specific graph if no gradient
            self.no_gradient()
        else:
            x = self.x_b
            while x <= self.x_a + self.x_n:
                y = 10**self.bias * x**self.gradient
                if y >= self.y_b and y <= self.y_a + self.y_n:  
                    tur.goto(self.scale_x(x),self.scale_y(y))
                    tur.pd()
                x += math.fabs(self.x_range/100)
    def exponential_draw(self,colour = "black"):
        #draws the line
        tur.pu()
        tur.color(colour)
        if self.gradient == None:
            #specific graph if no gradient
            self.no_gradient()
        else:
            x = self.x_b
            while x <= self.x_a + self.x_n:
                y = math.exp(self.bias) * math.exp(x*self.gradient)
                if y >= self.y_b and y <= self.y_a + self.y_n:  
                    tur.goto(self.scale_x(x),self.scale_y(y))
                    tur.pd()
                x += math.fabs(self.x_range/100)
    def linear(self):
        #algorithm for a linear regression
        self.points = zip(self.xs,self.ys)
        self.mean(self.xs,self.ys)
        self.mean_distances(self.mean_point,self.points)
        self.find_gradient(self.mean_distance,self.x_squared_distance)
        self.find_bias(self.mean_point,self.gradient)
        self.linear_draw(self.colour)
        if self.gradient:
            print("y = " + str(self.gradient) + " * x + " + str(self.bias))
    def power(self):
        #algorithm for a power law
        self.power_xs = list(map(lambda x: math.log10(x),self.xs))
        self.power_ys = list(map(lambda y: math.log10(y),self.ys))
        self.power_points = zip(self.power_xs,self.power_ys)
        self.mean(self.power_xs,self.power_ys)
        self.mean_distances(self.mean_point,self.power_points)
        self.find_gradient(self.mean_distance,self.x_squared_distance)
        self.find_bias(self.mean_point,self.gradient)
        self.power_draw(self.colour)
        if self.gradient:
            print("y = " + str(10**self.bias) + " * x ** " + str(self.gradient))
    def exponential(self):
        #algorithm for an exponential relationship
        self.exponential_ys = list(map(lambda y: math.log(y),self.ys))
        self.exponential_points = zip(self.xs,self.exponential_ys)
        self.mean(self.xs,self.exponential_ys)
        self.mean_distances(self.mean_point,self.exponential_points)
        self.find_gradient(self.mean_distance,self.x_squared_distance)
        self.find_bias(self.mean_point,self.gradient)
        self.exponential_draw(self.colour)
        if self.gradient:
            print("y = " + str(math.exp(self.bias)) + " * " + str(math.exp(self.gradient)) + " ** x")
    def line(self,series):
        #create a line for each series
        self.colour = series.colour.get()
        #create arrays of data as floats
        self.xs = list(float(i[0].get()) for i in series.data)
        self.ys = list(float(i[1].get()) for i in series.data)
        self.points = zip(self.xs,self.ys)
        self.plot_points()
        #draw line of best fit
        if series.line_type.get() == "Linear":
            self.linear()
        elif series.line_type.get() == "Exponential":
            self.exponential()
        elif series.line_type.get() == "Power":
            self.power()
    def name(self,length,series):
        total = 6
        #intorduce key
        tur.pu()
        tur.goto(-500,-300)
        tur.color("blue")
        tur.write("Key:",False,"center",("Lucida Console",12,"bold"))
        #write each series in its colour and spaced evenly in a line
        for s in series:
            tur.color(s.colour.get())
            tur.pu()
            tur.goto(600*total/length-500,-300)
            total += len(str(s))
            tur.write(str(s),False,"center",("Lucida Console",10,"normal"))
        
def check(data):
    #see if there are any values that cannot be expressed as floats
    for s in data:
        for i in s.data:
            try:
                float(i[0].get())
            except:
                return False
            try:
                float(i[1].get())
            except:
                return False
    return True
            
def draw():
    #check everything
    main.f2()
    all_points = []
    if check(main.data):
        for s in main.data:
            s.colour.set(s.colour.get().lower().strip())
            if s.colour.get().lower().strip() in colours:#check if colour is valid
                #update colour variables
                Label(main.frame1,text="ERROR: INVALID COLOR",fg="#EEE",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)
            else:
                s.colour.set('black')
                Label(main.frame1,text="ERROR: INVALID COLOR",fg="red",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)
                return
            for p in s.data:
                if (s.line_type.get() == "Exponential" or s.line_type.get() == "Power") and float(p[1].get()) <= 0:
                    Label(main.frame1,text="ERROR: INVALID LINE",fg="red",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)
                    return
                elif s.line_type.get() == "Power" and float(p[0].get()) <= 0:
                    Label(main.frame1,text="ERROR: INVALID LINE",fg="red",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)
                    return
                all_points.append([float(p[0].get()),float(p[1].get())])
##        #if no error messages, draw the graph and delete the widget
##        main.root.destroy()
        #cover up error messages
        Label(main.frame1,text="ERROR: INVALID INPUT",fg="#EEE",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)
        Label(main.frame1,text="ERROR: INVALID LINE",fg="#EEE",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)
        #draw the graw
        graph = Graph(all_points, main.title.get(),main.hx.get(),main.hy.get())
        #sort out each series
        name_length = 5
        for s in main.data:
            graph.line(s)
            name_length += len(str(s)) + 1
        graph.name(name_length,main.data)
    else:
        Label(main.frame1,text="ERROR: INVALID INPUT",fg="red",font=("Times",18,"bold"),justify="center").grid(row=3,column=0, ipadx=5,ipady=2, padx=2, pady=2)

points = []
main = Graph_Tkinter.run()
#draw button
Button(main.frame1,text="Draw!",command=draw,fg="blue",width=20, justify="center" , bd=2, font=("Times",18)).grid(row=3,column=1, ipadx=5,ipady=2, padx=2, pady=2)

#tkinter function
main.root.mainloop()
