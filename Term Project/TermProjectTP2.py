from cmu_112_graphics import *
from tkinter import *
import random
import string
import math

def appStarted(app):
    #splash page formatting
    app.splashPage = True
    app.startButtonDim = ((app.width/2-40,app.height/2+90),(app.width/2-5,app.height/2+123))
    app.breastCancerPic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Term Project/breast_cancer.jpg')
    #https://www.thermofisher.com/blog/proteomics/personalizing-medicine-targeting-breast-cancer-cell-membrane-proteomics/
    
    #breast cell page
    app.breastcell = False
    app.breastcellicons = False
    app.breastcancercells =[]
    while len(app.breastcancercells) < 10:
        a = random.randint(10,115)
        b = random.randint(10,115)
        if len(app.breastcancercells)%2 == 0:
            app.breastcancercells += [((a,b),(5,10))]
        else: 
            app.breastcancercells += [((a,b),(10,5))]
    app.displaybreast = []
    app.displaybreastcolor = 'tan'
    app.homebutton = (20,10,100,40,"Home")
    app.inputCellsbutton = [(30,50,180,90,'Input # of Cells:'),
                            (230,50,380,90,'Input Mutation:'),
                            (430,50,580,90,'Input Treatment:')]
    app.inputCellbuttonPressed = None
    app.inputcells = 0
    app.inputcount = 0
    app.inputbreastcellenter = False
    app.inputmutation = ''
    app.inputtreatment = '' 
    app.FinalOutcome = '"Final Outcome of the Mutation/Therapy Displayed Here"'
    
    #equations of mutations
    app.f = {'Nonsense-Mutation': 1, 'Mis-Sense Mutation': 2, 'Frame-Shift Mutation': 691}
    app.mutateddisplaybreast = []
    app.mutateddisplaybreastcolor = ''

    #icons for all of the pages
    app.icons = False
    topright = app.width-80
    app.icondimensions = [((topright,25),(topright+70,75),1),
                          ((topright,75),(topright+70,125),2),
                          ((topright,125),(topright+70,175),3)]
    app.mutationiconsbool = False
    app.mutationIcons = [((app.width/2-280,125),(app.width/2-150,175),"Nonsense-Mutation"),
                         ((app.width/2-125,125),(app.width/2+15,175),"Mis-Sense Mutation"),
                         ((app.width/2+40,125),(app.width/2+180,175),"Frame-Shift Mutation")]

    #mutations for page
    app.nonsenseMutations = False
    app.missenseMutations = False
    app.frameshiftMutations = False

    #treatment for page
    app.nonsenseTreatment = False
    app.missenseTreatment = False
    app.frameshiftTreatment = False
    app.treatments = {'Localized': 0.99,
                      'Regional': 0.86,
                      'Distant': 0.99}
    #https://www.cancer.org/cancer/breast-cancer/understanding-a-breast-cancer-diagnosis/breast-cancer-survival-rates.html

    #mutations button
    app.mutationButton = (app.width/2-50,70,app.width/2+50,110, "Mutate")
    app.mutate = False

    #visualization of Cell page
    app.cellPage = False
    app.radius = 20
    app.mutateCellcount = 0

    #the cells that are created and the processing of them based on the mutation
    app.cellmutation = 0
    app.nonsensemut = 1
    app.missensemut = 2
    app.frameshiftmut = 3
    app.cellCenters = [(( 50, 320),(app.radius, app.radius*2),app.cellmutation),
                       ((160, 350),(app.radius*2, app.radius),app.cellmutation),
                       ((100, 500),(app.radius, app.radius*2),app.cellmutation),
                       ((240, 420),(app.radius*2, app.radius),app.cellmutation),
                       ((360, 470),(app.radius, app.radius*2),app.cellmutation),
                       ((450, 290),(app.radius*2, app.radius),app.cellmutation),
                       ((480, 395),(app.radius, app.radius*2),app.cellmutation),
                       ((510, 530),(app.radius*2, app.radius),app.cellmutation)]  
    app.signals = []
    while len(app.signals) < 20:
        a = random.randint(10,590)
        b = random.randint(210,590)
        app.signals += [(a,b,5)]

    #visualization of Organelle page
    app.organellePage = False
    app.organelleCellDimensions = ((app.width/2,2*app.height/3),(app.width/2-20,100))
    app.organelleDNA = []
    app.ribosomeColor = 'purple1'
    app.mitochondriaColor = 'hot pink'
    app.ribosomeColor = 'purple4'
    app.mitochondriaColor = 'deep pink'
    app.otherorganellesDimensions = [((50,410,100,410,75,440),app.ribosomeColor),
                                     ((250,350,300,350,275,320),app.ribosomeColor),
                                     ((300,450,350,450,325,480),app.ribosomeColor),
                                     ((175,400),(30,40),app.mitochondriaColor)]

    #visualization of DNA page
    app.DNAPage = False
    DNArod1 = ((app.width/2,app.height/5+150),(app.width/2,20))
    DNArod2 = ((app.width/2,4*app.height/5-10),(app.width/2,20))
    app.DNAdimensions = [DNArod1,DNArod2]
    app.basepairs = {1:"cctcctcagcatcttatccgagtggaaggaaatt",
                     2:"gctcctctcactcttcagtccttctactgt",
                     3:"gccaatgggggccctggttg"}
    app.DNAsequence = ''
    app.mutationbasepairs = {1:"cctcctcagcatcttatctgagtggaaggaaatt",
                             2:"gctcctctcactcttcagtccttctactgt",
                             3:"gccaatggggaccctgtctg"}
    app.mutateDNAsequence = ''
    #Nonsense-Mutation: https://www.ncbi.nlm.nih.gov/nuccore/NM_001276696.3, https://www.frontiersin.org/articles/10.3389/fonc.2017.00323/full
    #Mis-sense Mutation: https://cancerres.aacrjournals.org/content/canres/early/2010/01/26/0008-5472.CAN-09-2850.full.pdf
    #FrameShift Mutation: https://www.ncbi.nlm.nih.gov/nuccore/NM_001002295.2,https://bmccancer.biomedcentral.com/articles/10.1186/1471-2407-14-278

    #DNA Toggle Page
    app.DNATogglePage = False
    app.DNAToggleSequence = []
    app.indexright = 10
    app.indexleft = 0

def mousePressed(app,event):
    ((cx1,cy1),(cx2,cy2)) = app.startButtonDim
    if (app.splashPage == True) and (cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2):
        #splash page and true statements
        app.splashPage = False
        app.breastcell = True
        app.breastcellicons = True
    if (app.breastcell == True):
        for elem in app.inputCellsbutton:
            (x1,y1,x2,y2,name) = elem
            if name == 'Input # of Cells:' and x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.inputCellbuttonPressed = 1
            if name == 'Input Mutation:' and x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.inputCellbuttonPressed = 2
            if name == 'Input Treatment:' and x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.inputCellbuttonPressed = 3
        for elem in app.displaybreast:
            (x1,y1,x2,y2) = elem
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.breastcell = False
                if app.inputcells > 0:
                    app.mutateCellcount = int((len(app.mutateddisplaybreast)/int(app.inputcells))*len(app.cellCenters))
                app.cellPage = True
                app.icons = True
                app.mutationiconsbool = True
        for elem in app.mutateddisplaybreast:
            (x1,y1,x2,y2) = elem
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.breastcell = False
                if app.inputcells > 0:
                    app.mutateCellcount = int((len(app.mutateddisplaybreast)/int(app.inputcells))*len(app.cellCenters))
                app.cellPage = True
                app.mutate = True
                app.icons = True
                app.mutationiconsbool = True
    if app.breastcell == False and app.splashPage == False:
        #iteration between the pages
        app.breastcellicons = True
        (hx1,hy1,hx2,hy2,_) = app.homebutton
        if hx1 <= event.x <= hx2 and hy1 <= event.y <= hy2:
            app.cellPage = app.organellePage = app.DNAPage = app.DNATogglePage = app.mutationiconsbool = app.icons = False
            app.breastcell = True
        for elem in app.icondimensions:
            #the icons on the right of the screen
            ((cx1,cy1),(cx2,cy2),level) = elem
            if level == 1 and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #cell Page
                app.DNAPage = app.organellePage = app.DNATogglePage = False
                app.cellPage = True
            if level == 2 and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #DNA Page
                app.cellPage = app.DNAPage = app.DNATogglePage = False
                app.organellePage = True
            if level == 3 and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #Organelle Page
                app.cellPage = app.organellePage = app.DNATogglePage = False
                app.DNAPage = True
        for elem in app.mutationIcons:
            #the icons for mutations
            ((cx1,cy1),(cx2,cy2),string) = elem
            if string == "Nonsense-Mutation" and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #nonsense mutations
                app.nonsenseMutations = True
                app.missenseMutations = app.frameshiftMutations = False
                app.mutate = False
                app.DNAToggleSequence = []
                for c in app.basepairs[1]:
                    app.DNAToggleSequence += [c]
            elif string == "Mis-Sense Mutation" and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #mis-sense mutations
                app.nonsenseMutations = app.frameshiftMutations = False
                app.missenseMutations = True
                app.mutate = False
                app.DNAToggleSequence = []
                for c in app.basepairs[2]:
                    app.DNAToggleSequence += [c]
            elif string == "Frame-Shift Mutation" and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #frame-shift mutations
                app.nonsenseMutations = app.missenseMutations = False
                app.frameshiftMutations = True
                app.mutate = False
                app.DNAToggleSequence = []
                for c in app.basepairs[3]:
                    app.DNAToggleSequence += [c]
        mutatecx1, mutatecy1, mutatecx2, mutatecy2,_ = app.mutationButton
        if mutatecx1 <= event.x <= mutatecx2 and mutatecy1 <= event.y <= mutatecy2:
            #mutate button
            app.mutate = True
        elif app.cellPage:
            #presssing from cells to organelles
            for elem in app.cellCenters:
                ((cx,cy),(r1,r2),mutation) = elem
                if cx-r1 <= event.x <= cx+r1 and cy-r2 <= event.y <= cy+r2:
                    print(mutation)
                    if mutation == app.nonsensemut:
                        print('i am not supposed to be here')
                        app.missenseMutations = app.frameshiftMutations = False
                        app.nonsenseMutations = True
                    elif mutation == app.missensemut:
                        app.nonsenseMutations = app.frameshiftMutations = False
                        app.missenseMutations = True
                    elif mutation == app.frameshiftmut:
                        app.nonsenseMutations = app.missenseMutations = False
                        app.frameshiftMutations = True
                    app.cellPage = app.DNAPage = app.DNATogglePage = False
                    app.organellePage = True
        elif app.organellePage:
            #pressing from organelle level to DNA
            ((cellcx, cellcy), (cellr1, cellr2)) = app.organelleCellDimensions
            topleftx,toplefty,bottomrightx,bottomrighty=((cellcx*3/2)-(cellr1/4)+30),(cellcy-(cellr2*2/3)+30),((cellcx*3/2)+(cellr1/4)-30),(cellcy*5/4-(cellr2/3)-30)
            if topleftx <= event.x <= bottomrightx and toplefty <= event.y <= bottomrighty:
                app.cellPage = app.organellePage = app.DNATogglePage = False
                app.DNAPage = True
            for elem in app.cellCenters:
                ((cx,cy),(r1,r2),mutation) = elem
                if mutation == app.nonsensemut:
                    app.missenseMutations = app.frameshiftMutations = False
                    app.nonsenseMutations = True
                if mutation == app.missensemut:
                    app.nonsenseMutations = app.frameshiftMutations = False
                    app.missenseMutations = True
                if mutation == app.frameshiftmut:
                    app.nonsenseMutations = app.missenseMutations = False
                    app.frameshiftMutations = True
        elif app.DNAPage:
            #pressing the DNA to get to the toggle page
            (((dnarodcx1,dnarodcy1),(dnarodr11,dnarodr21)),((dnarodcx2,dnarodcy2),(dnarodr12,dnarodr22))) = app.DNAdimensions
            if dnarodcx1-dnarodr11 <= event.x <= dnarodcx2+dnarodr12 and dnarodcy1-dnarodr21 <= event.y <= dnarodcy2+dnarodr22:
                app.cellPage = app.organellePage = app.DNAPage = False
                app.DNATogglePage = True

def keyPressed(app,event):
    #breast Cancer page
    if app.breastcell:
        if app.inputCellbuttonPressed == 1:
            #number of cells 
            if event.key in string.digits:
                #input digits
                app.inputcells += int(event.key)*(10**app.inputcount)
                app.inputcount += 1
            if event.key == 'Enter':
                app.inputbreastcellenter = True
                breastcellLevel(app)
        if app.inputCellbuttonPressed == 2:
            #mutation input
            if event.key in string.ascii_letters:
                app.inputmutation += event.key
            if event.key == 'Enter':
                app.inputbreastcellenter = True
                breastcellLevel(app)
        if app.inputCellbuttonPressed == 3:
            #treatment input
            if event.key in string.ascii_letters:
                app.inputtreatment += event.key
            if event.key == 'Enter':
                app.inputbreastcellenter = True
                breastcellLevel(app)
    #iteration for DNA Toggle Page
    if app.DNATogglePage:
        if app.nonsenseMutations: 
            location = app.basepairs[1]
        if app.missenseMutations:
            location = app.basepairs[2]
        if app.frameshiftMutations:
            location = app.basepairs[3]
        if app.DNATogglePage:
            #DNA Toggle Page from Left to Right
            if event.key == "Right" and app.indexright < len(location):
                app.DNAToggleSequence.pop(0)
                app.DNAToggleSequence.append(location[app.indexright])
                app.indexright += 1
                app.indexleft += 1
            if event.key == "Left" and app.indexleft > 0:
                app.DNAToggleSequence.pop()
                app.DNAToggleSequence.insert(0,location[app.indexleft-1])
                app.indexright -= 1
                app.indexleft -= 1

def timerFired(app):
    #floating concept for the first page
    if app.breastcell:
        for index in range(len(app.displaybreast)-1):
            xadd = yadd = 0
            if index%9 == 0:
                xadd = -5
            if index%9 == 1:
                yadd = -5
            if index%9 == 2:
                xadd = 5
            if index%9 == 5 or index%9 == 7:
                yadd = 5
            (x1,y1,x2,y2) = app.displaybreast[index]
            app.displaybreast.remove((x1,y1,x2,y2))
            if (50 < (x1+xadd) < 550 and 100 < (y1+yadd) < 550) or (50 < (x2+xadd) < 550 and 100 < (y2+yadd) < 550):
                app.displaybreast.append((x1+xadd,y1+yadd,x2+xadd,y2+yadd))
            else:
                if (x1+xadd) < 50:
                    app.displaybreast.append(((x1+xadd)+50,y1+yadd,(x2+xadd)+50,y2+yadd))
                elif (y1+yadd) < 100:
                    app.displaybreast.append(((x1+xadd),(y1+yadd)+100,(x2+xadd),(y2+yadd)+100))
                elif 550 < (y2+yadd):
                    app.displaybreast.append((x1+xadd,(y1+yadd)-100,x2+xadd,(y2+yadd)-100))
                elif 550 < (x2+xadd): 
                    app.displaybreast.append(((x2+xadd)-50,y1+yadd,(x2+xadd)-50,y2+yadd))
        if app.nonsenseMutations or app.missenseMutations or app.frameshiftMutations:
            if app.nonsenseMutations:
                index = 0
                numCells = app.f['Nonsense-Mutation'] 
                app.f['Nonsense-Mutation'] = app.f['Nonsense-Mutation']*(2**index) #linear distribution
                #https://www.genetics.org/content/148/4/1667
                countOfMutatedCells = 0
                #iterate to get to number Celles
                while countOfMutatedCells <= numCells:
                    countOfMutatedCells += 1
                    cellindex = random.randint(0,len(app.displaybreast)-1)
                    #random cell is mutated
                    if len(app.displaybreast) == 1:
                        app.FinalOutcome = 'The Patient has died!'
                    else:
                        app.mutateddisplaybreast += [app.displaybreast[cellindex]]
                        app.displaybreast.remove(app.displaybreast[cellindex])
                index += 1
                app.f['Nonsense-Mutation'] += 1
            if app.missenseMutations:
                numCells = (app.f['Mis-Sense Mutation'])/(math.log(app.inputcells,math.e)-math.log(1,math.e)) #binary distribution
                #https://www.genetics.org/content/148/4/1667
                countOfMutatedCells = 0
                while countOfMutatedCells <= numCells:
                    countOfMutatedCells += 1
                    cellindex = random.randint(0,len(app.displaybreast)-1)
                    if len(app.displaybreast) == 1:
                        app.FinalOutcome = 'The Patient has died!'
                    else:
                        app.mutateddisplaybreast += [app.displaybreast[cellindex]]
                        app.displaybreast.remove(app.displaybreast[cellindex])
            if app.frameshiftMutations:
                numCells = (app.f['Frame-Shift Mutation'])*(3*(10**-4)) # number of nucleotide distribution
                #https://www.genetics.org/content/148/4/1667
                countOfMutatedCells = 0
                while countOfMutatedCells <= numCells:
                    countOfMutatedCells += 1
                    cellindex = random.randint(0,len(app.displaybreast)-1)
                    if len(app.displaybreast) == 1:
                        app.FinalOutcome = 'The Patient has died!'
                    else:
                        app.mutateddisplaybreast += [app.displaybreast[cellindex]]
                        app.displaybreast.remove(app.displaybreast[cellindex])
        if app.nonsenseTreatment or app.missenseTreatment or app.frameshiftTreatment:
            if app.nonsenseTreatment:
                count = 0
                while count <= round((app.treatments['Distant']*len(app.mutateddisplaybreast))):
                    count += 1
                    cellindex = random.randint(0,len(app.mutateddisplaybreast)-1)
                    #random element of mutated display
                    if len(app.mutateddisplaybreast) == 1:
                        app.FinalOutcome = 'Patient Survived'
                    else:
                        app.displaybreast += [app.mutateddisplaybreast[cellindex]]
                        app.mutateddisplaybreast.remove(app.mutateddisplaybreast[cellindex])
            if app.missenseTreatment:
                count = 0
                while count <= round((app.treatments['Regional']*len(app.mutateddisplaybreast))):
                    count += 1
                    cellindex = random.randint(0,len(app.mutateddisplaybreast)-1)
                    if len(app.mutateddisplaybreast) == 1:
                        app.FinalOutcome = 'Patient Survived'
                    else:
                        app.displaybreast += [app.mutateddisplaybreast[cellindex]]
                        app.mutateddisplaybreast.remove(app.mutateddisplaybreast[cellindex])
            if app.frameshiftTreatment:
                count = 0
                while count <= round((app.treatments['Localized']*len(app.mutateddisplaybreast))):
                    count += 1
                    cellindex = random.randint(0,len(app.mutateddisplaybreast)-1)
                    if len(app.mutateddisplaybreast) == 1:
                        app.FinalOutcome = 'Patient Survived'
                    else:
                        app.displaybreast += [app.mutateddisplaybreast[cellindex]]
                        app.mutateddisplaybreast.remove(app.mutateddisplaybreast[cellindex])
    elif app.cellPage:
        count = 0
        for elem in app.signals:
            #movement of signals
            (cx,cy,r) = elem
            app.signals.remove((cx,cy,r))
            if (cx-r) < 10 or (cy-r) < 210:
                app.signals.append(((cx%10)-r,(cy%210)-r,r))
            elif (cx+r) > 590 or (cy+r) > 590:
                app.signals.append(((cx%10)+r,(cy%210)+r,r))
            else:
                if count%4 == 0:
                    app.signals.append((cx+r,cy+r,r))
                elif count%4 == 1:
                    app.signals.append((cx-r,cy+r,r))
                elif count%4 == 2:
                    app.signals.append((cx+r,cy-r,r))
                elif count%4 == 3:
                    app.signals.append((cx-r,cy-r,r))
                count += 1
        doStep(app)
    elif app.organellePage:
        doStep(app)
    elif app.DNAPage:
        doStep(app)
    elif app.DNATogglePage:
        i = 0
        while i < 1:
            DNAToggleLevel(app)
            i += 1

def doStep(app):
    if app.breastcell:
        breastcellLevel(app)
    elif app.cellPage:
        mutateCellLevel(app)
    elif app.organellePage:
        organelleLevel(app)
        if app.mutate:
            mutateOrganelleLevel(app)
    elif app.DNAPage:
        DNALevel(app)
        if app.mutate:
            mutateDNALevel(app)

def breastcellLevel(app):
    #creation of the initial breast cell level as if there is a 9x9 grid
    if app.inputbreastcellenter:
        if app.inputCellbuttonPressed == 1 or app.inputCellbuttonPressed == 2: 
            numberofcells = int(app.inputcells)
            cellpergrid = numberofcells//12
            listOfCols = [150,300,450,600]
            listofRows = [50,175,300,425,550]
            for col in listOfCols[:-1]:
                for row in listofRows[:-1]:
                    for index in range(cellpergrid):
                        ((cx,cy),(r1,r2)) = app.breastcancercells[index]
                        app.displaybreast.append((row+cx-r1,col+cy-r2,row+cx+r1,col+cy+r2))
        if app.inputmutation == 'nonsense' or app.inputmutation == 'missense' or app.inputmutation == 'frameshift':
            if app.inputmutation == 'nonsense':
                app.mutateddisplaybreastcolor = 'wheat1'
                app.missenseMutations = app.frameshiftMutations = False
                app.nonsenseMutations = app.mutate = True
            if app.inputmutation == 'missense':
                app.mutateddisplaybreastcolor = 'wheat2'
                app.nonsenseMutations = app.frameshiftMutations = False
                app.missenseMutations = app.mutate = True
            if app.inputmutation == 'frameshift':
                app.mutateddisplaybreastcolor = 'wheat3'
                app.nonsenseMutations = app.missenseMutations = False
                app.frameshiftMutations = app.mutate = True
        if app.inputtreatment == 'nonsense' or app.inputtreatment == 'missense' or app.inputtreatment == 'frameshift':
            if app.inputtreatment == 'nonsense':
                app.nonsenseTreatment = True
                app.mutate = False
            if app.inputtreatment == 'missense':
                app.missenseTreatment = True
                app.mutate = False
            if app.inputtreatment == 'frameshift':
                app.frameshiftTreatment = True
                app.mutate = False

def cellLevel(app):
    pass

def mutateCellLevel(app):
    setOfCenters = app.cellCenters
    while app.mutateCellcount >= 1:
        app.mutateCellcount -= 1
        indexofcenter = random.randint(0,len(setOfCenters)-1)
        ((cx,cy),(r1,r2),color) = setOfCenters[indexofcenter]
        if app.nonsenseMutations:
            color = 1
        elif app.missenseMutations:
            color = 2
        elif app.frameshiftMutations:
            color = 3
        setOfCenters.pop(indexofcenter)
        setOfCenters.append(((cx,cy),(r1,r2),color))
    #double the number of signals
    index = 0
    while index < 20:
        (cx,cy,r) = app.signals[index]
        app.signals += [(cx*2,cy*2,r)]
        index += 1

def organelleLevel(app):
    #create the template for the DNA sequence at this level
    if app.nonsenseMutations:
        app.organelleDNA = []
        index = 1
    if app.missenseMutations:
        app.organelleDNA = []
        index = 2
    if app.frameshiftMutations:
        app.organelleDNA = []
        index = 3
    while len(app.organelleDNA) < 16:
        for c in app.basepairs[index][:8]:
            app.organelleDNA += [c]
        for c in app.basepairs[index][-8:]:
            app.organelleDNA += [c]

def mutateOrganelleLevel(app):
    pass

def DNALevel(app):
    #create DNA sequence for the different mutations
    if app.nonsenseMutations:
        app.DNAsequence = ''
        index = 1
    if app.missenseMutations:
        app.DNAsequence = ''
        index = 2
    if app.frameshiftMutations:
        app.DNAsequence = ''
        index = 3
    for c in app.basepairs[index]:
        app.DNAsequence += c        
        
def mutateDNALevel(app):
    if app.nonsenseMutations:
        app.mutateDNAsequence = ''
        index = 1
    if app.missenseMutations:
        app.mutateDNAsequence = ''
        index = 2
    if app.frameshiftMutations:
        app.mutateDNAsequence = ''
        index = 3
    for c in app.mutationbasepairs[index]:
        app.mutateDNAsequence += c  

def DNAToggleLevel(app):
    #Toggle Visualization DNA Page
    if app.nonsenseMutations: 
        for c in app.basepairs[1]:
            app.DNAToggleSequence += [c]
    if app.missenseMutations:
        for c in app.basepairs[2]:
            app.DNAToggleSequence += [c]
    if app.frameshiftMutations:
        for c in app.basepairs[3]:
            app.DNAToggleSequence += [c]

def splashpage(app,canvas):
    #splash page of the app
    canvas.create_rectangle(0,0,app.width,app.height,fill = 'RoyalBlue3')
    canvas.create_image(app.width/2,app.height/2+50,image=ImageTk.PhotoImage(app.breastCancerPic))
    canvas.create_text(app.width/2, 75, text='Breast Cancer Visualizer', font='Arial 32 bold')
    canvas.create_text(app.width/2, 125,text='Press the Cancer Cell to Begin',font='Arial 26 bold')

def breastcellpage(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'snow2')
    canvas.create_text(app.width/2,25, text = 'Breast Cells', font = 'Arial 28 bold')
    canvas.create_rectangle(50,145,550,595, fill = 'PaleTurquoise1')
    for elem in app.displaybreast:
        x1,y1,x2,y2 = elem
        canvas.create_oval(x1,y1,x2,y2, fill = app.displaybreastcolor)
    for elem in app.mutateddisplaybreast:
        x1,y1,x2,y2 = elem
        canvas.create_oval(x1,y1,x2,y2, fill = app.mutateddisplaybreastcolor)
    canvas.create_rectangle(47,142,555,595,outline = 'black', width = '16')
    name = ''
    for elem in app.inputCellsbutton:
        (x1,y1,x2,y2,label) = elem
        canvas.create_rectangle(x1,y1,x2,y2,fill='mint cream')
        canvas.create_text((x1+x2)/2,(y1+y2)/2,text = label)
    if app.inputCellbuttonPressed == 1:
        cx1,cy1,cx2,cy2,_ = app.inputCellsbutton[0]
        canvas.create_rectangle(cx1,cy1,cx2,cy2,fill='mint cream')
        name = app.inputcells
        canvas.create_text((cx1+cx2)/2,(cy1+cy2)/2,text = name)
    elif app.inputCellbuttonPressed == 2:
        mx1,my1,mx2,my2,_ = app.inputCellsbutton[1]
        canvas.create_rectangle(mx1,my1,mx2,my2,fill='mint cream')
        name = app.inputmutation
        canvas.create_text((mx1+mx2)/2,(my1+my2)/2,text = name)
    elif app.inputCellbuttonPressed == 3:
        tx1,ty1,tx2,ty2,_= app.inputCellsbutton[2]
        canvas.create_rectangle(tx1,ty1,tx2,ty2,fill='mint cream')
        name = app.inputtreatment
        canvas.create_text((tx1+tx2)/2,(ty1+ty2)/2,text = name)
    canvas.create_text(app.width/2,110, text = app.FinalOutcome)

def cellpage(app,canvas):
    color = 'sky blue'
    canvas.create_rectangle(0,0,app.width,app.height, fill = color) #background color
    #signals
    for elem in app.signals:
        (cx,cy,r) = elem
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill ='light pink')
    #cells
    for elem in app.cellCenters:
        ((cx,cy),(r1,r2),cellmutation)= elem
        if cellmutation == 1:
            cellColor = 'wheat1'
        elif cellmutation == 2:
            cellColor = 'wheat2'
        elif cellmutation == 3:
            cellColor = 'wheat3'
        else:
            cellColor = "white" 
        canvas.create_oval(cx-r1,cy-r2,cx+r1,cy+r2,fill=cellColor) #cells
        if r2 > r1:
            canvas.create_oval(cx+(r1/2),cy-(r2*2/3),cx-(r1/2),cy-(r2/3), fill= "peach puff") #nucelus
        else:
            canvas.create_oval(cx+(r1*2/3),cy-(r2/2),cx+(r1/3),cy+(r2/2), fill = "peach puff")
    canvas.create_rectangle(0,0,app.width,200, fill= "white", outline = "white") #top border
    canvas.create_text(app.width/2, 30, text='Cell Page', font='Arial 28 bold')
    

def organellepage(app,canvas):
    color = 'sky blue'
    canvas.create_rectangle(0,0,app.width,app.height, fill = color) #background color
    aFill, gFill, cFill, tFill = 'Red', 'Green', 'goldenrod', 'Blue'
    aColor, tColor, gColor, cColor = "Indian"+aFill+"3", "Royal"+tFill+"3", "Spring"+gFill+"4", cFill+"3"
    #all of the organelles drawing
    ((cellcx, cellcy), (cellr1, cellr2)) = app.organelleCellDimensions
    if app.nonsenseMutations:
        cellColor = 'wheat1'
    if app.missenseMutations:
        cellColor = 'wheat2'
    if app.frameshiftMutations:
        cellColor = 'wheat3'
    canvas.create_oval(cellcx-cellr1,cellcy-cellr2+5,cellcx+cellr1,cellcy+cellr2+5,fill='dim gray') #cell
    canvas.create_oval(cellcx-cellr1,cellcy-cellr2,cellcx+cellr1,cellcy+cellr2,fill=cellColor)
    #nucleus and DNA
    canvas.create_oval((cellcx*3/2)-(cellr1/4),cellcy-(cellr2*2/3)+5,(cellcx*3/2)+(cellr1/4),cellcy*5/4-(cellr2/3)+5, fill= "rosy brown")
    canvas.create_oval((cellcx*3/2)-(cellr1/4),cellcy-(cellr2*2/3),(cellcx*3/2)+(cellr1/4),cellcy*5/4-(cellr2/3), fill= "peach puff", outline = "peach puff")
    DNAadjx = 30 #adjustments for putting them between the lines
    DNAadjy = 30
    count = 0 
    for elem in app.organelleDNA:
        leftsidex,leftsidey, rightsidex,rightsidey = ((cellcx*3/2)-(cellr1/4)+DNAadjx),(cellcy-(cellr2*2/3)+DNAadjy),((cellcx*3/2)+(cellr1/4)-DNAadjx),(cellcy-(cellr2*2/3)+DNAadjy)
        if elem == 'a':
            canvas.create_line(leftsidex,leftsidey,(rightsidex+leftsidex)/2,rightsidey,fill = aColor)
            canvas.create_line((rightsidex+leftsidex)/2, leftsidey,rightsidex,rightsidey,fill = tColor)
        if elem == 'g':
            canvas.create_line(leftsidex,leftsidey,(rightsidex+leftsidex)/2,rightsidey,fill = gColor)
            canvas.create_line((rightsidex+leftsidex)/2, leftsidey,rightsidex,rightsidey,fill = cColor)
        if elem == 't':
            canvas.create_line(leftsidex,leftsidey,(rightsidex+leftsidex)/2,rightsidey,fill = tColor)
            canvas.create_line((rightsidex+leftsidex)/2, leftsidey,rightsidex,rightsidey,fill = aColor)
        if elem == 'c':
            canvas.create_line(leftsidex,leftsidey,(rightsidex+leftsidex)/2,rightsidey,fill = cColor)
            canvas.create_line((rightsidex+leftsidex)/2, leftsidey,rightsidex,rightsidey,fill = gColor)
        count += 1
        DNAadjy += 5
        if count < 9: 
            DNAadjx += 5
        else: 
            DNAadjx -= 5
    canvas.create_line((cellcx*3/2)-(cellr1/4)+30,cellcy-(cellr2*2/3)+30,(cellcx*3/2)+(cellr1/4)-30,cellcy*5/4-(cellr2/3)-30,fill= "brown", width = 10)
    canvas.create_line((cellcx*3/2)+(cellr1/4)-30,cellcy-(cellr2*2/3)+30,(cellcx*3/2)-(cellr1/4)+30,cellcy*5/4-(cellr2/3)-30,fill= "brown", width = 10)
    #other organelles
    #mrna
    i = 0
    x1,y1,x2,y2 = 295,345,298,335
    while i < 11:
        if i%4 == 0:
            canvas.create_rectangle(x1+5*i,y1,x2+5*i,y2,fill = aColor)
        elif i%4 == 1:
            canvas.create_rectangle(x1+5*i,y1,x2+5*i,y2,fill= gColor)
        elif i%4 == 2:
            canvas.create_rectangle(x1+5*i,y1,x2+5*i,y2,fill = tColor)
        elif i%4 == 3:
            canvas.create_rectangle(x1+5*i,y1,x2+5*i,y2,fill= cColor)
        i += 1
    canvas.create_rectangle(275,343,350,349,fill = 'brown',outline = 'brown')
    #amino acids
    index = 0
    (cx,cy,r) = (245,355,5)
    if app.mutate:
        maxvalue = 15
        color = 'OliveDrab1'
    else:
        maxvalue = 10
        color = 'DarkOliveGreen2'
    while 0 <= index < maxvalue: 
        if index < 3:
            canvas.create_oval(cx-(index*r)-r,cy+(index*r)-r,cx-(index*r)+r,cy+(index*r)+r,fill = color)
        if 3 <= index < 5: 
            canvas.create_oval(cx-(3*r)-r,cy+(index*r)-r,cx-(3*r)+r,cy+(index*r)+r,fill = color)
        index1 = 3
        if 5 <= index < 10 and 0 <= index1:
            canvas.create_oval(cx-(index1*r)+r,cy+(index*r)-r,cx-(index1*r)-r,cy+(index*r)+r,fill = color)
            index1 -= 1
        index2 = 10
        if 10 <= index < maxvalue:
            canvas.create_oval(cx+(index*r)-r-60,cy+(index2*r)-r,cx+(index*r)+r-60,cy+(index2*r)+r,fill = color)
        index += 1
    #ribosomes
    for elem in app.otherorganellesDimensions[:-1]:
        ((x1,y1,x2,y2,x3,y3),rcolor) = elem
        if app.mutate: 
            rcolor = 'purple2'
        else:
            rcolor = 'purple1'
        canvas.create_polygon(x1,y1,x2,y2,x3,y3+5,x1,y1, fill = 'purple4')
        canvas.create_polygon(x1,y1,x2,y2,x3,y3,x1,y1, fill = rcolor)
    #mitochondria
    ((mcx,mcy),(mr1,mr2),mcolor) = app.otherorganellesDimensions[-1]
    if app.mutate: 
        mcolor = 'PaleVioletRed2'
    else:
        mcolor = 'PaleVioletRed1'
    canvas.create_oval(mcx-mr1,mcy-mr2+5,mcx+mr1,mcy+mr2+5, fill = 'PaleVioletRed4')
    canvas.create_oval(mcx-mr1,mcy-mr2,mcx+mr1,mcy+mr2, fill = mcolor, outline = mcolor)
    canvas.create_line(((mcx-mr1)+10),((mcy-mr2)+10),((mcx+mr1)-5),((mcy-mr2)+20),
                       ((mcx-mr1)+3),((mcy-mr2)+30),((mcx+mr1)-2),((mcy-mr2)+40),
                       ((mcx-mr1)+2),((mcy-mr2)+50),((mcx+mr1)-5),((mcy-mr2)+60),
                       ((mcx-mr1)+10),((mcy-mr2)+70))

    canvas.create_rectangle(0,0,app.width,200, fill = "white", outline = "white")
    canvas.create_text(app.width/2, 30, text='Organelle Page', font='Arial 28 bold')


def DNApage(app,canvas):
    color = 'peach puff'
    canvas.create_rectangle(0,0,app.width,app.height, fill = color) #background color
    aFill, gFill, cFill, tFill = 'Red', 'Green', 'goldenrod', 'Blue' #nucelotides colors
    topleftx,toplefty, bottomrightx,bottomrighty = 5,app.height/5+150,10,app.height/5+250 #topbar
    bottomleftx,bottomlefty,toprightx,toprighty = 5, app.height/5+350,10,app.height/5+250 #bottombar
    if app.nonsenseMutations: #nonsense mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"1", "Royal"+tFill+"1", "Spring"+gFill+"2", cFill+"1"
        filler = len(app.basepairs[1])*1/2
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "TP53 Gene: Nucelotides 200-230")

    elif app.missenseMutations: #missense mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"2", "Royal"+tFill+"2", "Spring"+gFill+"3", cFill+"2"
        filler = len(app.basepairs[2])*1/2
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "BRCA1 Gene: Nucelotides 80,780-80,810")

    elif app.frameshiftMutations: #frameshift mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"3", "Royal"+tFill+"3", "Spring"+gFill+"4", cFill+"3"
        filler = len(app.basepairs[3])*1/2
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "GATA3 Gene: Nucelotides 300-330")
    if app.mutate:
        sequence = app.mutateDNAsequence
    else: 
        sequence = app.DNAsequence
    for c in sequence:
        if c == "a":
            canvas.create_rectangle(topleftx,toplefty,bottomrightx+filler,bottomrighty, fill = aColor)   
            canvas.create_rectangle(bottomleftx,bottomlefty,toprightx+filler,toprighty, fill = tColor)  
        if c == "g":
            canvas.create_rectangle(topleftx,toplefty,bottomrightx+filler,bottomrighty, fill = gColor)
            canvas.create_rectangle(bottomleftx,bottomlefty,toprightx+filler,toprighty, fill = cColor)     
        if c == "c":
            canvas.create_rectangle(topleftx,toplefty,bottomrightx+filler,bottomrighty, fill = cColor)
            canvas.create_rectangle(bottomleftx,bottomlefty,toprightx+filler,toprighty, fill = gColor)     
        if c == "t":
            canvas.create_rectangle(topleftx,toplefty,bottomrightx+filler,bottomrighty, fill = tColor)
            canvas.create_rectangle(bottomleftx,bottomlefty,toprightx+filler,toprighty, fill = aColor)     
        topleftx += filler
        bottomrightx += filler
        bottomleftx += filler
        toprightx += filler
        #Annotation of the Nucelotides
        canvas.create_rectangle(10,app.height-40, 70, app.height-20, fill = aColor)
        canvas.create_text(40,app.height-30, text = "Adenine")
        canvas.create_rectangle(170,app.height-40, 230, app.height-20, fill = tColor)
        canvas.create_text(200,app.height-30, text = "Thymine")
        canvas.create_rectangle(330,app.height-40, 390, app.height-20, fill = gColor)
        canvas.create_text(360,app.height-30, text = "Guanine")
        canvas.create_rectangle(490,app.height-40, 550, app.height-20, fill = cColor)
        canvas.create_text(520,app.height-30, text = "Cytosine")
    
    for elem in app.DNAdimensions:
        ((cx,cy),(r1,r2)) = elem
        canvas.create_oval(cx-r1,cy-r2,cx+r1,cy+r2,fill = 'brown')
    canvas.create_rectangle(0,0,app.width,200, fill = "white", outline = "white")
    canvas.create_text(app.width/2, 30, text = 'DNA Page',font = 'Arial 28 bold')


def DNATogglePage(app,canvas):
    color = 'peach puff'
    canvas.create_rectangle(0,0,app.width,app.height, fill = color)
    canvas.create_rectangle(-50,75,app.width+50,275, fill = 'brown')
    canvas.create_rectangle(-50,app.height-75,app.width+50,app.height+75, fill = 'brown')
    aFill, gFill, cFill, tFill = 'Red', 'Green', 'goldenrod', 'Blue' #nucelotides colors
    if app.nonsenseMutations: #nonsense mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"1", "Royal"+tFill+"1", "Spring"+gFill+"2", cFill+"1"
        canvas.create_text(app.width/2,237,text = 'TP53 Gene: Nucelotides 170-250')
    elif app.missenseMutations: #missense mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"2", "Royal"+tFill+"2", "Spring"+gFill+"3", cFill+"2"
        canvas.create_text(app.width/2,237,text = 'BRCA1 Gene: Nucelotides 80,780-80,798')
    elif app.frameshiftMutations: #frameshift mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"3", "Royal"+tFill+"3", "Spring"+gFill+"4", cFill+"3"
        canvas.create_text(app.width/2,237,text = 'GATA3 Gene: Nucelotides 1,530-1,590')
    nucleotidemod = app.width/10
    counter = 0
    for c in app.DNAToggleSequence:
        if c == 'a':
            canvas.create_rectangle(0+(nucleotidemod*counter),275,app.width/10+(nucleotidemod*(counter+1)),((app.height-75)+275)/2,fill = aColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((275)+(((app.height-75)+275)/2))/2,text = 'A')
            canvas.create_rectangle(0+(nucleotidemod*counter),((app.height-75)+275)/2,app.width/10+(nucleotidemod*(counter+1)),app.height-75,fill= tColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((((app.height-75)+275)/2)+(app.height-75))/2,text = 'T')
        if c == 't':
            canvas.create_rectangle(0+(nucleotidemod*counter),275,app.width/10+(nucleotidemod*(counter+1)),((app.height-75)+275)/2,fill = tColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((275)+(((app.height-75)+275)/2))/2,text = 'T')
            canvas.create_rectangle(0+(nucleotidemod*counter),((app.height-75)+275)/2,app.width/10+(nucleotidemod*(counter+1)),app.height-75,fill= aColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((((app.height-75)+275)/2)+(app.height-75))/2,text = 'A')
        if c == 'g':
            canvas.create_rectangle(0+(nucleotidemod*counter),275,app.width/10+(nucleotidemod*(counter+1)),((app.height-75)+275)/2,fill = gColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((275)+(((app.height-75)+275)/2))/2,text = 'G')
            canvas.create_rectangle(0+(nucleotidemod*counter),((app.height-75)+275)/2,app.width/10+(nucleotidemod*(counter+1)),app.height-75,fill= cColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((((app.height-75)+275)/2)+(app.height-75))/2,text = 'C')
        if c == 'c':
            canvas.create_rectangle(0+(nucleotidemod*counter),275,app.width/10+(nucleotidemod*(counter+1)),((app.height-75)+275)/2,fill = cColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((275)+(((app.height-75)+275)/2))/2,text = 'C')
            canvas.create_rectangle(0+(nucleotidemod*counter),((app.height-75)+275)/2,app.width/10+(nucleotidemod*(counter+1)),app.height-75,fill= gColor)
            canvas.create_text(((-nucleotidemod+(nucleotidemod*counter))+(app.width/10+(nucleotidemod*(counter+1))))/2,((((app.height-75)+275)/2)+(app.height-75))/2,text = 'G')
        counter += 1
    canvas.create_rectangle(0,0,app.width,200, fill = "white", outline = "white")
    canvas.create_text(app.width/2, 30, text = 'DNA Toggle Page',font = 'Arial 28 bold')

def breastcellicons(app,canvas):
    (x1,y1,x2,y2,word) = app.homebutton
    canvas.create_rectangle(x1,y1,x2,y2,fill = 'plum1')
    canvas.create_text((x1+x2)/2,(y1+y2)/2,text = word)

def icons(app,canvas):
    #the right hand side icons
    for elem in app.icondimensions:
        ((cx1,cy1),(cx2,cy2),level) = elem
        canvas.create_rectangle(cx1,cy1,cx2,cy2)
        if level == 1:
            if app.cellPage:
                canvas.create_rectangle(cx1,cy1,cx2,cy2, fill = "firebrick1")
            canvas.create_text((cx1+cx2)/2, (cy1+cy2)/2, text='Cell')
        if level == 2:
            if app.organellePage:
                canvas.create_rectangle(cx1,cy1,cx2,cy2, fill = "firebrick1")
            canvas.create_text((cx1+cx2)/2, (cy1+cy2)/2, text='Organelle')
        if level == 3:
            if app.DNAPage or app.DNATogglePage:
                canvas.create_rectangle(cx1,cy1,cx2,cy2, fill = "firebrick1")
            canvas.create_text((cx1+cx2)/2, (cy1+cy2)/2, text='DNA')
        
def mutationicons(app,canvas):
    #mutate button
    (mutatecx1, mutatecy1, mutatecx2, mutatecy2, mutatetext) = app.mutationButton
    canvas.create_rectangle(mutatecx1, mutatecy1, mutatecx2, mutatecy2, fill = 'thistle')
    canvas.create_text((mutatecx1+mutatecx2)/2,(mutatecy1+mutatecy2)/2, text = mutatetext)
    #all of the mutations possible icons
    for elem in app.mutationIcons:
        ((cx1,cy1),(cx2,cy2),word) = elem
        canvas.create_rectangle(cx1,cy1,cx2,cy2)
        if word == "Nonsense-Mutation" and app.nonsenseMutations:
            canvas.create_rectangle(cx1,cy1,cx2,cy2, fill = 'indian red')
        if word == "Mis-Sense Mutation" and app.missenseMutations:
            canvas.create_rectangle(cx1,cy1,cx2,cy2, fill = 'indian red')
        if word == "Frame-Shift Mutation" and app.frameshiftMutations:
            canvas.create_rectangle(cx1,cy1,cx2,cy2, fill = 'indian red')
        canvas.create_text((cx1+cx2)/2, (cy1+cy2)/2, text=word)

def redrawAll(app,canvas):
    if app.splashPage:
        splashpage(app,canvas)
    if app.breastcell:
        breastcellpage(app,canvas)
    if app.cellPage:
        cellpage(app,canvas)
    if app.organellePage:
        organellepage(app,canvas)
    if app.DNAPage:
       DNApage(app,canvas)
    if app.DNATogglePage:
       DNATogglePage(app,canvas)
    if app.breastcellicons:
        breastcellicons(app,canvas)
    if app.icons:
        icons(app,canvas)
    if app.mutationiconsbool:
        mutationicons(app,canvas)

runApp(width = 600, height = 600)