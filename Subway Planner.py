from tkinter import *

class SubwayPlanner:
    def __init__(self):
        self.stations = {}
        self.lines = {}
        self.connnects = {}
        self.stations2 = []
        
    def createSt(self,station_name):
        if not self.getStation(station_name):
            self.stations2.append(int(station_name))
            self.stations2.sort()
            self.stations[station_name] = Station(station_name)
            check = 0
            for i in self.stations2:
                if int(station_name) == i:
                    pass
                else:
                    if int(station_name) > i:
                        self.stations[str(i)].addNorth(int(station_name))
                        self.stations[station_name].addSouth(i)
                    else:
                        self.stations[str(i)].addSouth(int(station_name))
                        self.stations[station_name].addNorth(i)
        else:
            return False
        
    def newLine(self,start,end,line,time):
        start2 = int(start)
        end2 = int(end)
        if not self.getLine(line) and self.getStation(start) and self.getStation(end):
            self.lines[line] = Line()
            self.lines[line].connect(start,end,time)
        else:
            return False
        
    def newConnect(self,start,end,line,time):
        if not self.getStation(start) or not self.getStation(end) or not self.getLine(line):
            return False
        else:
            start2 = int(start)
            end2 = int(end)
            if self.lines[line].getStop(start,end,time):
                return False
            else:
                self.lines[line].connect(start,end,time)

    def getStation(self,name):
        if name in self.stations:
            return True
        else:
            return False
        
    def getLine(self,name):
        if name in self.lines:
            return True
        else:
            return False
        
    def plan(self,start,end,line):
        not_done = True
        time = 0
        mintime = 0
        if int(start)<int(end):
            stops =  self.stations[start].getNorthList()
            stops.sort()
            #if len(stops) == 1:
                #time += self.lines['4'].getTime(str(start),str(stops[0]))
            #else:
            for i in stops:
                time += self.lines[line].getTime(str(start),str(i))
                start = i
                if i == int(end):
                        break
                
            return time
                          
        else:
            stops = self.stations[start].getSouthList()
            stops.sort()
            #if len(stops) == 1:
                #time += self.lines['4'].getTime(str(start),str(stops[0]))
            #else:
            for i in range(1,len(stops)+1):
                time += self.lines[line].getTime(str(start),str(stops[-i]))
                start = stops[-i]
                if i == int(end):
                    break
                    
            return time
            
    def best(self,start,end):
        train = ''
        mintime = 0
        for j in self.lines:
            time = self.plan(start,end,j)
            if mintime == 0:
                mintime = time
                train = j
                time = 0
            elif mintime > time:
                mintime = time
                train = j
                time = 0
                    
        return mintime, train
                
class Line:
    def __init__(self):
        self.connections = []
        
    def connect(self,station1,station2,time):
        self.connections.append([str(station1),str(station2),time])
    def lis(self):
        return self.connections
        
    def getStop(self,start,end,time):
        x = [start,end,time]
        y = [end,start,time]
        for i in self.connections:
            if x == i or y == i:
                return True
        if True:
            return False
        
    def getTime(self,start,end):
        for i in self.connections:
            if ((i[0] == start) and (i[1] == end)) or ((i[0] == end) and (i[1] == start)):
                return int(i[2])
        
        
    
class Station():
    def __init__(self,station_name):
        self.sn = station_name
        self.north = []
        self.south = []
        
    def __str__(self):
        return self.sn
    
    def getSouthList(self):
        return self.south
    
    def getNorthList(self):
        return self.north
    
    def addNorth(self,name):
        self.north.append(name)
        
    def addSouth(self,name):
        self.south.append(name)
        
    def getNorth(self,name):
        if name in self.north:
            return True
        else:
            return False
        
    def getSouth(self,name):
        if name in self.south:
            return True
        else:
            return False


        
class UserInterface:
    def __init__(self,root):
        self.c = root
        self.s = SubwayPlanner()

    def processStation(self, event):
        while self.s.createSt(str(self.newS.get())) == False:
            self.c.destroy()
            self.c = Tk()
            self.createStation2()   
        self.c.destroy()
        self.c = Tk()
        self.intro('Success')

    def createStation2(self):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Failed Try Again").grid(row=0)
        Label(self.c, text="Enter Name of Station").grid(row=1)
        self.newS = Entry(self.c)
        self.newS.grid(column=0,row=2)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=0,row=3)
        P1.bind("<Button-1>", self.processStation)
        B1 = Button(self.c, text = 'Back Home')
        B1.grid(column=0,row=4)
        B1.bind("<Button-1>", self.intro2)
        
    def createStation(self, event):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Enter Name of Station").grid(row=0)
        self.newS = Entry(self.c)
        self.newS.grid(column=0,row=1)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=0,row=2)
        P1.bind("<Button-1>", self.processStation)
        B1 = Button(self.c, text = 'Back Home')
        B1.grid(column=0,row=3)
        B1.bind("<Button-1>", self.intro2)

    def processStation2(self, event):
        while self.s.newLine(str(self.start.get()),str(self.end.get()),str(self.line.get()),int(self.time.get())) == False:
            self.c.destroy()
            self.c = Tk()
            self.createLine2()   
        self.c.destroy()
        self.c = Tk()
        self.intro('Success')

    def createLine2(self):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Failed Try Again").grid(row=0)
        Label(self.c, text="Enter Name of One Existing Stop").grid(row=1)
        Label(self.c, text="Enter Name of Another Existing Stop").grid(row=2)
        Label(self.c, text="Enter Name of Train").grid(row=3)
        Label(self.c, text="Enter Time of Travel").grid(row=4)
        self.start = Entry(self.c)
        self.end = Entry(self.c)
        self.line = Entry(self.c)
        self.time = Entry(self.c)
        self.start.grid(row=1, column=1)
        self.end.grid(row=2, column=1)
        self.line.grid(row=3, column=1)
        self.time.grid(row=4, column=1)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=5)
        P1.bind("<Button-1>", self.processStation2)
        BH = Button(self.c, text = 'Back Home')
        BH.grid(row=6)
        BH.bind("<Button-1>", self.intro2)

    def createLine(self, event):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Enter Name of One Existing Stop").grid(row=0)
        Label(self.c, text="Enter Name of Another Existing Stop").grid(row=1)
        Label(self.c, text="Enter Name of Train").grid(row=2)
        Label(self.c, text="Enter Time of Travel").grid(row=3)
        self.start = Entry(self.c)
        self.end = Entry(self.c)
        self.line = Entry(self.c)
        self.time = Entry(self.c)
        self.start.grid(row=0, column=1)
        self.end.grid(row=1, column=1)
        self.line.grid(row=2, column=1)
        self.time.grid(row=3, column=1)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=4)
        P1.bind("<Button-1>", self.processStation2)
        BH = Button(self.c, text = 'Back Home')
        BH.grid(row=5)
        BH.bind("<Button-1>", self.intro2)
        #s.newLine(start,end,line,time)

    def processStation3(self, event):
        while self.s.newConnect(str(self.start.get()),str(self.end.get()),str(self.line.get()),int(self.time.get())) == False:
            self.c.destroy()
            self.c = Tk()
            self.addStops2()   
        self.c.destroy()
        self.c = Tk()
        self.intro('Success')

    def addStops2(self, event):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Failed Try Again").grid(row=0)
        Label(self.c, text="Enter Name of One Existing Stop").grid(row=1)
        Label(self.c, text="Enter Name of Another Existing Stop").grid(row=2)
        Label(self.c, text="Enter Name of Train").grid(row=3)
        Label(self.c, text="Enter Time of Travel").grid(row=4)
        self.start = Entry(self.c)
        self.end = Entry(self.c)
        self.line = Entry(self.c)
        self.time = Entry(self.c)
        self.start.grid(row=1, column=1)
        self.end.grid(row=2, column=1)
        self.line.grid(row=3, column=1)
        self.time.grid(row=4, column=1)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=5)
        P1.bind("<Button-1>", self.processStation3)
        BH = Button(self.c, text = 'Back Home')
        BH.grid(row=6)
        BH.bind("<Button-1>", self.intro2)
        #s.newConnect(start,end,line,time)

    def addStops(self, event):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Enter Name of One Existing Stop").grid(row=0)
        Label(self.c, text="Enter Name of Another Existing Stop").grid(row=1)
        Label(self.c, text="Enter Name of Train").grid(row=2)
        Label(self.c, text="Enter Time of Travel").grid(row=3)
        self.start = Entry(self.c)
        self.end = Entry(self.c)
        self.line = Entry(self.c)
        self.time = Entry(self.c)
        self.start.grid(row=0, column=1)
        self.end.grid(row=1, column=1)
        self.line.grid(row=2, column=1)
        self.time.grid(row=3, column=1)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=4)
        P1.bind("<Button-1>", self.processStation3)
        BH = Button(self.c, text = 'Back Home')
        BH.grid(row=5)
        BH.bind("<Button-1>", self.intro2)

    def processStation4(self, event):
        start=str(self.start.get())
        end=str(self.end.get())
        while self.s.best(start,end) == False:
            self.c.destroy()
            self.c = Tk()
            self.FBR22()   
        self.c.destroy()
        self.c = Tk()
        x,y = self.s.best(start,end)
        self.intro(str(x)+' minutes on Train '+str(y))

    def FBR2(self, event):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Failed, Try Again").grid(row=0)
        Label(self.c, text="Enter Name of Start Station").grid(row=1)
        Label(self.c, text="Enter Name of End Station").grid(row=2)
        self.start = Entry(self.c)
        self.end = Entry(self.c)
        self.start.grid(row=1, column=1)
        self.end.grid(row=2, column=1)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=3)
        P1.bind("<Button-1>", self.processStation4)
        BH = Button(self.c, text = 'Back Home')
        BH.grid(row=4)
        BH.bind("<Button-1>", self.intro2)
        #s.best(start,end)

    def FBR(self, event):
        self.c.destroy()
        self.c = Tk()
        Label(self.c, text="Enter Name of Start Station").grid(row=0)
        Label(self.c, text="Enter Name of End Station").grid(row=1)
        self.start = Entry(self.c)
        self.end = Entry(self.c)
        self.start.grid(row=0, column=1)
        self.end.grid(row=1, column=1)
        P1 = Button(self.c, text = 'Process')
        P1.grid(column=3)
        P1.bind("<Button-1>", self.processStation4)
        BH = Button(self.c, text = 'Back Home')
        BH.grid(row=2)
        BH.bind("<Button-1>", self.intro2)
        #s.best(start,end)
    def intro2(self, event):
        self.c.destroy()
        self.c = Tk()
        B1 = Button(self.c, text = 'Create a Station')
        B2 = Button(self.c, text = 'Create a Line')
        B3 = Button(self.c, text = 'Add a Connection Between Stops on an Existing Line')
        B4 = Button(self.c, text = 'Find Best Route')
        B1.pack()
        B2.pack()
        B3.pack()
        B4.pack()
        B1.bind("<Button-1>", self.createStation)
        B2.bind("<Button-1>", self.createLine)
        B3.bind("<Button-1>", self.addStops)
        B4.bind("<Button-1>", self.FBR)
        
    def intro(self,begin='Begin'):
        Label(self.c, text=begin).grid(row=0)
        B1 = Button(self.c, text = 'Create a Station')
        B2 = Button(self.c, text = 'Create a Line')
        B3 = Button(self.c, text = 'Add a Connection Between Stops on an Existing Line')
        B4 = Button(self.c, text = 'Find Best Route')
        B1.grid(row=1)
        B2.grid(row=2)
        B3.grid(row=3)
        B4.grid(row=4)
        B1.bind("<Button-1>", self.createStation)
        B2.bind("<Button-1>", self.createLine)
        B3.bind("<Button-1>", self.addStops)
        B4.bind("<Button-1>", self.FBR)
    
        

root = Tk()
x = UserInterface(root)
x.intro()
root.mainloop( )

    
