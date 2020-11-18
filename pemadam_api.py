import numpy as np

##########
# Class
##########

#class blok
class Blok:
    def __init__(self,hiden,show):
        self.invisible=hiden
        self.visible=show

    def setValue(self,a,b):
        self.invisible=a
        self.visible=b

#class arena
class Arena:
    def __init__(self):
        self.row=27
        self.col=27
        self.bloks=np.array([[Blok("U"," ") for i in range(self.col)]for j in range(self.row)])

    def cetak(self):
        for y in range(self.row):
            for x in range(self.col):
                #dinding "#"
                if y==0 or y==26:
                    self.bloks[y][x].setValue("#","#")
                elif x==0 or x==26:
                    self.bloks[y][x].setValue("#","#")
                elif x==8 and y not in (11,12,13,14,22,23,24,25):
                    self.bloks[y][x].setValue("#","#")
                elif x==13 and y in (5,6,7,8,9,10,11,16,21,22,23,24,25):
                    self.bloks[y][x].setValue("#","#")
                elif x==21 and y in (5,6,7,8,9,10,11,16):
                    self.bloks[y][x].setValue("#","#")
                elif y==5 and x in range(14,21):
                    self.bloks[y][x].setValue("#","#")
                elif y==10 and x in (5,6,7):
                    self.bloks[y][x].setValue("#","#")
                elif y==11 and x in (13,18,19,20,21):
                    self.bloks[y][x].setValue("#","#")
                elif y==15 and x in range(1,8):
                    self.bloks[y][x].setValue("#","#")
                elif y==16 and x in range(13,26):
                    self.bloks[y][x].setValue("#","#")
                elif y==2 and x ==10:
                    self.bloks[y][x].setValue("H","H")
                elif y==10 and x in range(1,5):
                    self.bloks[y][x].setValue("P"," ")
                elif y==11 and x in range(14,18):
                    self.bloks[y][x].setValue("P"," ")
                elif y in range(22,26) and x==8:
                    self.bloks[y][x].setValue("P"," ")
                elif y in range(17,21) and x==13:
                    self.bloks[y][x].setValue("P"," ")
                elif (y==3 and x==3) or (y==18 and x==3) or (y==22 and x==23):
                    self.bloks[y][x].setValue("A","A")
                print(self.bloks[y][x].visible,end=" "),
            print()
    
    def cetakLagi(self):
        for y in range(self.row):
            for x in range(self.col):
                print(self.bloks[y][x].visible,end=" "),
            print()

#class robot
class Robot:
    def __init__(self,arena,y,x):
        self.arena=arena
        self.arena.bloks[y][x].setValue("H","R")
        self.sampingy=2
        self.sampingx=9
        self.depany=3
        self.depanx=10

    #set koordinat samping dan depan
    def setSampingy(self,y):
        self.sampingy=y
    def setSampingx(self,x):
        self.sampingx=x
    def setDepany(self,y):
        self.depany=y
    def setDepanx(self,x):
        self.depanx=x
        
    #gerakan
    def kebawah(self,y,x):
        if self.arena.bloks[y][x].invisible=="H":
            self.arena.bloks[y][x].visible="H"
        elif self.arena.bloks[y][x].invisible=="P":
            self.arena.bloks[y][x].visible=" "
        elif self.arena.bloks[y][x].invisible=="U":
            self.arena.bloks[y][x].visible=" "
        self.arena.bloks[y+1][x].visible="R"

    def kekiri(self,y,x):
        if self.arena.bloks[y][x].invisible=="H":
            self.arena.bloks[y][x].visible="H"
        elif self.arena.bloks[y][x].invisible=="P":
            self.arena.bloks[y][x].visible=" "
        elif self.arena.bloks[y][x].invisible=="U":
            self.arena.bloks[y][x].visible=" "
        self.arena.bloks[y][x-1].visible="R"
    
    def kekanan(self,y,x):
        if self.arena.bloks[y][x].invisible=="H":
            self.arena.bloks[y][x].visible="H"
        elif self.arena.bloks[y][x].invisible=="P":
            self.arena.bloks[y][x].visible=" "
        elif self.arena.bloks[y][x].invisible=="U":
            self.arena.bloks[y][x].visible=" "
        self.arena.bloks[y][x+1].visible="R"

    def keatas(self,y,x):
        if self.arena.bloks[y][x].invisible=="H":
            self.arena.bloks[y][x].visible="H"
        elif self.arena.bloks[y][x].invisible=="P":
            self.arena.bloks[y][x].visible=" "
        elif self.arena.bloks[y][x].invisible=="U":
            self.arena.bloks[y][x].visible=" "
        self.arena.bloks[y-1][x].visible="R"

    def keluar(self,yawal,xawal,yakhir,xakhir):
        if self.arena.bloks[yawal][xawal].invisible=="H":
            self.arena.bloks[yawal][xawal].visible="H"
        elif self.arena.bloks[yawal][xawal].invisible=="P":
            self.arena.bloks[yawal][xawal].visible=" "
        elif self.arena.bloks[yawal][xawal].invisible=="U":
            self.arena.bloks[yawal][xawal].visible=" "
        self.arena.bloks[yakhir][xakhir].visible="R"

    

###########
# methode
###########

#cari ymin
def cariYmin(y,x,arena):
    while arena.bloks[y-1][x].visible != "#" and arena.bloks[y-1][x].invisible != "P" :
        y=y-1
    return y

#cari ymaks
def cariYmaks(y,x,arena):
    while arena.bloks[y+1][x].visible != "#" and arena.bloks[y+1][x].invisible != "P" :
        y=y+1
    return y

#cari xmin
def cariXmin(y,x,arena):
    while arena.bloks[y][x-1].visible != "#" and arena.bloks[y][x-1].invisible != "P" :
        x=x-1
    return x

#cari cmaks
def cariXmaks(y,x,arena):
    while arena.bloks[y][x+1].visible != "#" and arena.bloks[y][x+1].invisible != "P" :
        x=x+1
    return x



###########
# main
###########
print("Program Simulasi Robot Pemadam Api")

#membuat arena
arena=Arena()
arena.cetak()

#standby
y=2 #2
x=10 #10
robot=Robot(arena,y,x)
print("Robot standby")
arena.cetakLagi()

#mulai
print("Mulai...")
yHome=2
xHome=10
api=3
ruang=4
diruangan=False


while api>0 or ruang>0:
    #cek jalan buntu
    if arena.bloks[robot.depany][robot.depanx].invisible=="#" or arena.bloks[robot.depany][robot.depanx].invisible=="#P" :
        sampingYtemp=robot.sampingy
        sampingXtemp=robot.sampingx
        robot.sampingy=robot.depany
        robot.sampingx=robot.depanx
        if sampingYtemp<robot.depany :
            if sampingXtemp<robot.depanx:
                robot.depany=y
                robot.depanx=x+1
            else:
                robot.depany=y+1
                robot.depanx=x
        else :
            if sampingXtemp<robot.depanx:
                robot.depany=y-1
                robot.depanx=x
            else:
                robot.depany=y
                robot.depanx=x-1

    if ruang==1:
        
        yruangmin=cariYmin(y,x,arena)
        yruangmaks=cariYmaks(y,x,arena)
        xruangmin=cariXmin(y,x,arena)
        xruangmaks=cariXmaks(y,x,arena)
        if arena.bloks[yruangmin-1][x].invisible=="P":
            print("satu")
            while y>yruangmin-2 :
                robot.keatas(y,x)
                arena.cetakLagi()
                y=y-1
            robot.sampingy=yruangmin-1
            robot.depany=yruangmin
            diruangan=True
        elif arena.bloks[yruangmaks+1][x].invisible=="P":
            while y<yruangmaks+2 :
                robot.keatas(y,x)
                arena.cetakLagi()
                y=y+1
            robot.sampingy=yruangmaks+1
            robot.depany=yruangmaks
            diruangan=True
        elif arena.bloks[y][xruangmin-1].invisible=="P":
            while x>xruangmin :
                robot.kekiri(y,x)
                arena.cetakLagi()
                x=x-1
            robot.sampingx=xruangmin-1
            robot.depanx=xruangmin
            diruangan=True
        elif arena.bloks[y][xruangmaks+1].invisible=="P":
            while x<xruangmaks :
                robot.keatas(y,x)
                arena.cetakLagi()
                x=x+1
            robot.sampingx=xruangmaks+1
            robot.depanx=xruangmaks
            diruangan=True

    #algoritma di luar ruangan
    if diruangan==False :
        #langkah pertama
        if y==2 and x==10:
            if robot.sampingy<y :
                ymin=cariYmin(y,x,arena)
                while y>ymin :
                    robot.keatas(y,x)
                    arena.cetakLagi()
                    y=y-1
                robot.sampingy=ymin-1
                robot.depany=ymin
            elif robot.sampingy>y :
                ymaks=cariYmaks(y,x,arena)
                while y<ymaks :
                    robot.keatas(y,x)
                    arena.cetakLagi()
                    y=y+1
                robot.sampingy=ymaks+1
                robot.depany=ymaks
            if robot.sampingx<x :
                xmin=cariXmin(y,x,arena)
                while x>xmin :
                    robot.kekiri(y,x)
                    arena.cetakLagi()
                    x=x-1
                robot.sampingx=xmin-1
                robot.depanx=xmin
            elif robot.sampingx>x :
                xmaks=cariXmaks(y,x,arena)
                while x<xmaks :
                    robot.keatas(y,x)
                    arena.cetakLagi()
                    x=x+1
                robot.sampingx=xmaks+1
                robot.depanx=xmaks

        #jika disamping kiri robot dinding
        elif arena.bloks[robot.sampingy][robot.sampingx].invisible =="#" or arena.bloks[robot.sampingy][robot.sampingx].invisible =="#P":
            if robot.depanx<x :
                robot.kekiri(y,x)
                arena.cetakLagi()
                robot.sampingx=robot.sampingx-1
                robot.depanx=robot.depanx-1
                x=x-1
            elif robot.depanx>x :
                robot.kekanan(y,x)
                arena.cetakLagi()
                robot.sampingx=robot.sampingx+1
                robot.depanx=robot.depanx+1
                x=x+1
            elif robot.depany<y :
                robot.keatas(y,x)
                arena.cetakLagi()
                robot.sampingy=robot.sampingy-1
                robot.depany=robot.depany-1
                y=y-1
            elif robot.depany>y :
                robot.kebawah(y,x)
                arena.cetakLagi()
                robot.sampingy=robot.sampingy+1
                robot.depany=robot.depany+1
                y=y+1
        #jika disamping kiri robot pintu
        elif arena.bloks[robot.sampingy][robot.sampingx].invisible =="P":
            if robot.sampingx<x :
                robot.kekiri(y,x)
                arena.cetakLagi()
                x=x-1
                robot.kekiri(y,x)
                arena.cetakLagi()
                x=x-1
                diruangan=True
            elif robot.sampingx>x :
                robot.kekanan(y,x)
                arena.cetakLagi()
                x=x+1
                robot.kekanan(y,x)
                arena.cetakLagi()
                x=x+1
                diruangan=True
            elif robot.sampingy<y:
                robot.keatas(y,x)
                arena.cetakLagi()
                y=y-1
                robot.keatas(y,x)
                arena.cetakLagi()
                y=y-1
                diruangan=True
            elif robot.sampingy>y:
                robot.kebawah(y,x)
                arena.cetakLagi()
                y=y+1
                robot.kebawah(y,x)
                arena.cetakLagi()
                y=y+1
                diruangan=True
        #mencari samping kiri robot dinding selain yang pertama/belok
        else:
            if robot.sampingy<y :
                robot.keatas(y,x)
                y=y-1
                robot.sampingx=robot.sampingx+1
                robot.depany=robot.depany-2
                robot.depanx=robot.depanx+1
                arena.cetakLagi()
            elif robot.sampingy>y :
                robot.kebawah(y,x)
                y=y+1
                robot.sampingx=robot.sampingx-1
                robot.depany=robot.depany+2
                robot.depanx=robot.depanx-1
                arena.cetakLagi()
            elif robot.sampingx<x :
                robot.kekiri(y,x)
                x=x-1
                robot.sampingy=robot.sampingy-1
                robot.depany=robot.depany-1
                robot.depanx=robot.depanx-2
                arena.cetakLagi()
            elif robot.sampingx>x :
                robot.kekanan(y,x)
                x=x+1
                robot.sampingy=robot.sampingy+1
                robot.depany=robot.depany-1
                robot.depanx=robot.depanx+2
                arena.cetakLagi()

    
    #algoritma di dalam ruangan
    else:
        ymaks=cariYmaks(y,x,arena)
        ymin=cariYmin(y,x,arena)
        xmaks=cariXmaks(y,x,arena)
        xmin=cariXmin(y,x,arena)
        yApi=None
        xApi=None
        awaly=y
        awalx=x

        #mencari posisi api
        for j in range(ymin,ymaks+1):
            for i in range(xmin,xmaks+1):
                if arena.bloks[j][i].visible=="A":
                    yApi=j
                    xApi=i
        #memadamkan api
        if yApi!=None and xApi!=None:
            if yApi<=awaly:
                for j in range(yApi+1,awaly):
                    robot.keatas(y,x)
                    y=y-1
                    arena.cetakLagi()
                if xApi<=awalx:
                    for i in range(xApi+1,awalx):
                        robot.kekiri(y,x)
                        x=x-1
                        arena.cetakLagi()
                    #api padam
                    arena.bloks[yApi][xApi].visible=" "
                    arena.cetakLagi()
                    for i in range(xApi+1,awalx):
                        robot.kekanan(y,x)
                        x=x+1
                        arena.cetakLagi()
                else:
                    for i in range(awalx,xApi-1):
                        robot.kekanan(y,x)
                        x=x+1
                        arena.cetakLagi()
                    #api padam
                    arena.bloks[yApi][xApi].visible=" "
                    arena.cetakLagi()
                    for i in range(awalx,xApi-1):
                        robot.kekiri(y,x)
                        x=x-1
                        arena.cetakLagi()
                for j in range(yApi+1,awaly):
                    robot.kebawah(y,x)
                    y=y+1
                    arena.cetakLagi()
            else :
                for j in range(awaly,yApi-1):
                    robot.kebawah(y,x)
                    y=y+1
                    arena.cetakLagi()
                if xApi<=x:
                    for i in range(xApi+1,awalx):
                        robot.kekiri(y,x)
                        x=x-1
                        arena.cetakLagi()
                    #api padam
                    arena.bloks[yApi][xApi].visible=" "
                    arena.cetakLagi()
                    for i in range(xApi+1,awalx):
                        robot.kekanan(y,x)
                        x=x+1
                        arena.cetakLagi()
                else:
                    for i in range(awalx,xApi-1):
                        robot.kekanan(y,x)
                        x=x+1
                        arena.cetakLagi()
                    #api padam
                    arena.bloks[yApi][xApi].visible=" "
                    arena.cetakLagi()
                    for i in range(awalx,xApi-1):
                        robot.kekiri(y,x)
                        x=x-1
                        arena.cetakLagi()
                for j in range(awaly,yApi-1):
                    robot.keatas(y,x)
                    y=y-1
                    arena.cetakLagi()
            api=api-1
        
        #keluar ruangan
        robot.keluar(y,x,robot.sampingy,robot.sampingx)
        arena.cetakLagi()
        if robot.depanx<robot.sampingx:
            if robot.depany>robot.sampingy:
                robot.keluar(robot.sampingy,robot.sampingx,robot.depany,robot.sampingx)
                y=robot.depany
                x=robot.sampingx
            elif robot.depany<robot.sampingy:
                robot.keluar(robot.sampingy,robot.sampingx,robot.sampingy,robot.depanx)
                y=robot.sampingy
                x=robot.depanx
        elif robot.depanx>robot.sampingx:
            if robot.depany>robot.sampingy:
                robot.keluar(robot.sampingy,robot.sampingx,robot.depany,robot.sampingx)
                y=robot.sampingy
                x=robot.depanx
            elif robot.depany<robot.sampingy:
                robot.keluar(robot.sampingy,robot.sampingx,robot.depany,robot.sampingx)
                y=robot.depany
                x=robot.sampingx
        arena.cetakLagi()
        
        #tandai pintu sudah dikunjungi
        if robot.sampingy==10 :
            for i in range(1,4+1):
                arena.bloks[10][i].invisible="#P"
        elif robot.sampingy==11 :
            for i in range(14,17+1):
                arena.bloks[11][i].invisible="#P"
        elif robot.sampingx==8 :
            for i in range(22,25+1):
                arena.bloks[i][8].invisible="#P"
        elif robot.sampingx==13 :
            for i in range(17,20+1):
                arena.bloks[i][13].invisible="#P"

        ruang=ruang-1
        diruangan=False

    #cek
    
    print("y=",y," x=",x," sampingy=",robot.sampingy," sampingx=",robot.sampingx," depany=",robot.depany," depanx=",robot.depanx)
print("Misi selesai, kembali ke Home")
print("y=",y," x=",x)
#balik ke home
if xHome<x:
    xtemp=x
    for i in range(xtemp,xHome,-1):
        robot.kekiri(y,x)
        x=x-1
        arena.cetakLagi()
    ytemp=y
    if yHome<y:
        for j in range(ytemp,yHome,-1):
            robot.keatas(y,x)
            y=y-1
            arena.cetakLagi()
    else:
        for j in range(ytemp,yHome):
            robot.keatas(y,x)
            y=y+1
            arena.cetakLagi()
    y=j

print("Simulasi selesai")
#selesai
