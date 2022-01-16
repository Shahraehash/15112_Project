from cmu_112_graphics import *
from tkinter import *
import random
import string
import math
#all colors referenced from: http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png

def appStarted(app):
    #splash page formatting
    app.splashPage = True
    app.startButtonDim = ((app.width/2-40,app.height/2+90),(app.width/2-5,app.height/2+123))
    app.breastCancerPic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Term Project/breast_cancer.jpg')
    #image for breast cancer image: https://www.thermofisher.com/blog/proteomics/personalizing-medicine-targeting-breast-cancer-cell-membrane-proteomics/
    app.instructionsdimensions = (app.width/2-100,110,app.width/2+100,130)
    #instructions page
    app.InstructionsPage = False
    app.splashbutton = (app.width/2-100,45,app.width/2+100,65)
    app.breastPagePic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Term Project/BreastPage.png')
    app.cellPagePic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Term Project/CellPage.png')
    app.organellePagePic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Term Project/Organelle.png')
    app.DNAPagePic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Term Project/DNA.png')
    app.DNATogglePagePic = app.loadImage('/Users/raehash/Desktop/CMU Freshman Year/15-112/Term Project/DNAToggle.png')
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
    app.inputCellsbutton = [(30,55,180,95,'Input # of Cells:'),
                            (230,55,380,95,'Input Mutation:'),
                            (430,55,580,95,'Input Treatment:')]
    app.inputCellbuttonPressed = None
    app.inputcells = 0
    app.inputcount = 0
    app.inputbreastcellenter = False
    app.inputmutation = ''
    app.inputtreatment = '' 
    app.FinalOutcome = ''
    #age 
    app.age = False
    app.ageOfPatient = 0
    app.ageslider = (app.width/2-5,app.height/2+30,app.width/2+5,app.height/2+110)
    app.agesImmuneSystem = {0:1,10:5,20:7,60:8,70:6,80:5,90:1}
    #data distribution of age immune system impact from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4707740/
    app.ageset = (app.width/2-150,475,app.width/2+150,525)
    #datavisualization
    app.datavisualization = (450,10,580,40,"Data Visualization")
    app.datavisualizationpage = False
    app.datavisualizationicon = False
    app.xbox = (60,60,70,70,"X")
    app.axes = 13
    app.totalxaxes = []
    app.xaxis = 0
    app.healthycells = []
    app.cancercells = [0]
    app.xaxes = []
    app.yaxes = []
    app.xincrement = 0
    app.yincrement = 0
    app.incrementOfHealthy = 1
    app.healthycellcoordinates = []
    app.cancercellcoordinates = []
    app.incrementOfCancer = 1
    app.iterationOfdataVisualization = 1
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
    app.LocalTreatment = False
    app.RegionalTreatment = False
    app.DistantTreatment = False
    app.treatments = {'Localized': 0.99,
                      'Regional': 0.86,
                      'Distant': 0.27}
    #ratio of treatment impacts: https://www.cancer.org/cancer/breast-cancer/understanding-a-breast-cancer-diagnosis/breast-cancer-survival-rates.html
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
    app.mitochondriatext = {1: 'The mitND6 gene affected cell migration & invasion', 
                            2: 'Mitochondria have PCGs Mutations:ND1,ND3,ND4,ND5',
                            3: 'mtDNA mutation perturb OXPHOS system in cancer'}
    #Research for mitochondria impact: https://bmccancer.biomedcentral.com/articles/10.1186/s12885-015-1349-z, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3664469/, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0233461#pone.0233461.ref015
    app.proteintext = {1: 'Premature end to protein synthesis for stop codon',
                       2: 'Less effective protein for incorrect amino acid',
                       3: 'Abnormal protein products for shift in read'}
    #Research for protein: https://www.nature.com/scitable/definition/nonsense-mutation-228/, https://www.genome.gov/genetics-glossary/Missense-Mutation, https://www.nature.com/scitable/definition/frameshift-mutation-frame-shift-mutation-frameshift-203/
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
                             2:"gctcctctcacgcttcagtccttctactgt",
                             3:"gccaatggggaccctgtctg"}
    app.mutateDNAsequence = ''
    app.mutationtext = ''
    #Nonsense-Mutation DNA: https://www.ncbi.nlm.nih.gov/nuccore/NM_001276696.3, https://www.frontiersin.org/articles/10.3389/fonc.2017.00323/full
    #Mis-sense Mutation DNA: https://cancerres.aacrjournals.org/content/canres/early/2010/01/26/0008-5472.CAN-09-2850.full.pdf
    #FrameShift Mutation DNA: https://www.ncbi.nlm.nih.gov/nuccore/NM_001002295.2,https://bmccancer.biomedcentral.com/articles/10.1186/1471-2407-14-278
    #DNA Toggle Page
    app.DNATogglePage = False
    app.DNAToggleSequence = []
    app.indexright = 10
    app.indexleft = 0

def mouseDragged(app,event):
    if app.age:
        #set age of patient
        if 225 < event.x < 375:
            app.ageslider = (event.x-5,app.height/2+30,event.x+5,app.height/2+110)
            app.ageOfPatient = event.x%225

def mousePressed(app,event):
    if (app.splashPage == True):
        #splash page and true statements
        (x1,y1,x2,y2) = app.instructionsdimensions
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            #enter instructions page
            app.InstructionsPage = True
            app.splashPage = False
        ((cx1,cy1),(cx2,cy2)) = app.startButtonDim
        if (cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2):
            #start button
            app.splashPage = False
            app.breastcell = True
            app.breastcellicons = True
            app.age = True
    if app.InstructionsPage == True:
        (x3,y3,x4,y4) = app.splashbutton
        if x3 <= event.x <= x4 and y3 <= event.y <= y4:
            #to exit instructions page
            app.InstructionsPage = False
            app.splashPage = True
    if (app.breastcell == True):
        (x9,y9,x10,y10) = app.ageset
        if x9 <= event.x <= x10 and y9 <= event.y <= y10:
            #set age of patient
            app.age = False
        app.datavisualizationicon = True 
        (x7,y7,x8,y8,_) = app.datavisualization
        if x7 <= event.x <= x8 and y7 <= event.y <= y8:
            #enter datavisualization page
            app.breastcell = False
            app.breastcellicons = False
            app.datavisualizationpage = True
            datavisualizationLevel(app)
        for elem in app.inputCellsbutton:
            #input number of cells/mutation/treatment
            (x1,y1,x2,y2,name) = elem
            if name == 'Input # of Cells:' and x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.inputCellbuttonPressed = 1
            if name == 'Input Mutation:' and x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.inputCellbuttonPressed = 2
            if name == 'Input Treatment:' and x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.inputCellbuttonPressed = 3
        for elem in app.displaybreast:
            #enter non mutated page
            (x1,y1,x2,y2) = elem
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.breastcell = False
                if app.inputcells > 0:
                    app.mutateCellcount = int((len(app.mutateddisplaybreast)/int(app.inputcells))*len(app.cellCenters))
                app.cellPage = True
                app.icons = True
                app.mutationiconsbool = True
        for elem in app.mutateddisplaybreast:
            #enter mutated page
            (x1,y1,x2,y2) = elem
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                app.breastcell = False
                if app.inputcells > 0:
                    app.mutateCellcount = int((len(app.mutateddisplaybreast)/int(app.inputcells))*len(app.cellCenters))
                app.cellPage = True
                app.mutate = True
                app.icons = True
                app.mutationiconsbool = True
    if app.datavisualizationpage == True and app.breastcell == False and app.splashPage == False and app.InstructionsPage == False:
        (x5,y5,x6,y6,_) = app.xbox
        if x5 <= event.x <= x6 and y5 <= event.y <= y6:
            #data visualization page
            app.datavisualizationpage = False
            app.breastcell = True
            app.breastcellicons = True
    if app.breastcell == False and app.splashPage == False and app.InstructionsPage == False and app.datavisualizationpage == False:
        app.datavisualizationicon = False
        #iteration between the pages
        app.breastcellicons = True
        (hx1,hy1,hx2,hy2,_) = app.homebutton
        if hx1 <= event.x <= hx2 and hy1 <= event.y <= hy2:
            app.cellPage = app.organellePage = app.DNAPage = app.DNATogglePage = app.mutationiconsbool = app.icons = False
            app.breastcell = True
            app.datavisualiazationicon = True
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
                    if mutation == app.nonsensemut:
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
                app.inputcells = (app.inputcells*(10**app.inputcount)) + int(event.key)
                app.inputcount += 1
            if event.key == 'Enter':
                app.FinalOutcome = '"Patient is Healthy"'
                app.inputbreastcellenter = True
                breastcellLevel(app)
                app.healthycells += [int(app.inputcells)]
        if app.inputCellbuttonPressed == 2:
            #mutation input
            if event.key in string.ascii_letters:
                app.inputmutation += event.key
            if event.key == 'Enter':
                app.FinalOutcome = f'"Patient has been diagnosed with a {app.inputmutation} Breast Cancer"'
                app.inputbreastcellenter = True
                breastcellLevel(app)
        if app.inputCellbuttonPressed == 3:
            #treatment input
            if event.key in string.ascii_letters:
                app.inputtreatment += event.key
            if event.key == 'Enter':
                app.FinalOutcome = f'"Patient undergoes a {app.inputtreatment} Therapy"'
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
            if (55 < (x1+xadd) < 545 and 105 < (y1+yadd) < 545) or (55 < (x2+xadd) < 545 and 105 < (y2+yadd) < 545):
                app.displaybreast.append((x1+xadd,y1+yadd,x2+xadd,y2+yadd))
            else:
                if (x1+xadd) < 55:
                    app.displaybreast.append(((x1+xadd)+50,y1+yadd,(x2+xadd)+50,y2+yadd))
                elif (y1+yadd) < 105:
                    app.displaybreast.append(((x1+xadd),(y1+yadd)+100,(x2+xadd),(y2+yadd)+100))
                elif 545 < (y2+yadd):
                    app.displaybreast.append((x1+xadd,(y1+yadd)-100,x2+xadd,(y2+yadd)-100))
                elif 545 < (x2+xadd): 
                    app.displaybreast.append(((x1+xadd)-50,y1+yadd,(x2+xadd)-50,y2+yadd))
        if app.nonsenseMutations or app.missenseMutations or app.frameshiftMutations:
            if app.nonsenseMutations:
                index = 0
                numCells = app.f['Nonsense-Mutation'] 
                app.f['Nonsense-Mutation'] = app.f['Nonsense-Mutation']*(2**index) #linear distribution
                #How to create a linear distribution: https://www.genetics.org/content/148/4/1667
                countOfMutatedCells = 0
                #iterate to get to number Cells
                while countOfMutatedCells <= numCells:
                    countOfMutatedCells += 1
                    cellindex = random.randint(0,len(app.displaybreast)-1)
                    #random cell is mutated
                    if len(app.displaybreast) == 1:
                        app.FinalOutcome = 'The Patient has died!'
                    else:
                        app.mutateddisplaybreast += [app.displaybreast[cellindex]]
                        app.displaybreast.remove(app.displaybreast[cellindex])
                        app.xaxis += 1
                        app.totalxaxes += [app.xaxis]
                        app.healthycells += [len(app.displaybreast)]
                        app.cancercells += [len(app.mutateddisplaybreast)]
                index += 1
                app.f['Nonsense-Mutation'] += 1
            if app.missenseMutations:
                numCells = (app.f['Mis-Sense Mutation'])/(math.log(app.inputcells,math.e)-math.log(1,math.e)) #binary distribution
                #How to get the binary distribution: https://www.genetics.org/content/148/4/1667
                countOfMutatedCells = 0
                while countOfMutatedCells <= numCells:
                    countOfMutatedCells += 1
                    cellindex = random.randint(0,len(app.displaybreast)-1)
                    if len(app.displaybreast) == 1:
                        app.FinalOutcome = 'The Patient has died!'
                    else:
                        app.mutateddisplaybreast += [app.displaybreast[cellindex]]
                        app.displaybreast.remove(app.displaybreast[cellindex])
                        app.xaxis += 1
                        app.totalxaxes += [app.xaxis]
                        app.healthycells += [len(app.displaybreast)]
                        app.cancercells += [len(app.mutateddisplaybreast)]
            if app.frameshiftMutations:
                numCells = (app.f['Frame-Shift Mutation'])*(3*(10**-4)) # number of nucleotide distribution
                #How to create a distribution based on number of nucleotides https://www.genetics.org/content/148/4/1667
                countOfMutatedCells = 0
                while countOfMutatedCells <= numCells:
                    countOfMutatedCells += 1
                    cellindex = random.randint(0,len(app.displaybreast)-1)
                    if len(app.displaybreast) == 1:
                        app.FinalOutcome = 'The Patient has died!'
                    else:
                        app.mutateddisplaybreast += [app.displaybreast[cellindex]]
                        app.displaybreast.remove(app.displaybreast[cellindex])
                        app.xaxis += 1
                        app.totalxaxes += [app.xaxis]
                        app.healthycells += [len(app.displaybreast)]
                        app.cancercells += [len(app.mutateddisplaybreast)]
        if app.LocalTreatment or app.RegionalTreatment or app.DistantTreatment:
            if app.DistantTreatment:
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
                        app.healthycells += [len(app.displaybreast)]
                        app.cancercells += [len(app.mutateddisplaybreast)]
            if app.RegionalTreatment:
                count = 0
                while count <= round((app.treatments['Regional']*len(app.mutateddisplaybreast))):
                    count += 1
                    cellindex = random.randint(0,len(app.mutateddisplaybreast)-1)
                    #random element of mutated display
                    if len(app.mutateddisplaybreast) == 1:
                        app.FinalOutcome = 'Patient Survived'
                    else:
                        app.displaybreast += [app.mutateddisplaybreast[cellindex]]
                        app.mutateddisplaybreast.remove(app.mutateddisplaybreast[cellindex])
                        app.healthycells += [len(app.displaybreast)]
                        app.cancercells += [len(app.mutateddisplaybreast)]
            if app.LocalTreatment:
                count = 0
                while count <= round((app.treatments['Localized']*len(app.mutateddisplaybreast))):
                    count += 1
                    cellindex = random.randint(0,len(app.mutateddisplaybreast)-1)
                    #random element of mutated display
                    if len(app.mutateddisplaybreast) == 1:
                        app.FinalOutcome = 'Patient Survived'
                    else:
                        app.displaybreast += [app.mutateddisplaybreast[cellindex]]
                        app.mutateddisplaybreast.remove(app.mutateddisplaybreast[cellindex])
                        app.healthycells += [len(app.displaybreast)]
                        app.cancercells += [len(app.mutateddisplaybreast)]
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
        immunesystem(app)
    elif app.cellPage:
        mutateCellLevel(app)
    elif app.organellePage:
        organelleLevel(app)
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
                #color
                app.mutateddisplaybreastcolor = 'wheat3'
                app.missenseMutations = app.frameshiftMutations = False
                app.nonsenseMutations = app.mutate = True
            if app.inputmutation == 'missense':
                #color
                app.mutateddisplaybreastcolor = 'wheat2'
                app.nonsenseMutations = app.frameshiftMutations = False
                app.missenseMutations = app.mutate = True
            if app.inputmutation == 'frameshift':
                #color
                app.mutateddisplaybreastcolor = 'wheat1'
                app.nonsenseMutations = app.missenseMutations = False
                app.frameshiftMutations = app.mutate = True
        if app.inputtreatment == 'Local' or app.inputtreatment == 'Regional' or app.inputtreatment == 'Distant':
            if app.inputtreatment == 'Local':
                app.LocalTreatment = True
                app.mutate = False
            if app.inputtreatment == 'Regional':
                app.RegionalTreatment = True
                app.mutate = False
            if app.inputtreatment == 'Distant':
                app.DistantTreatment = True
                app.mutate = False

def immunesystem(app):
    if app.breastcell:
        cellindex = random.randint(0,len(app.mutateddisplaybreast)-1)
        #distribution based on age of patients
        if 0 <= app.ageOfPatient <= 10:
            num = app.agesImmuneSystem[0]
        elif 10 <= app.ageOfPatient <= 20:
            num = app.agesImmuneSystem[10]
        elif 20 <= app.ageOfPatient <= 60:
            num = app.agesImmuneSystem[20]
        elif 60 <= app.ageOfPatient <= 70:
            num = app.agesImmuneSystem[60]
        elif 70 <= app.ageOfPatient <= 80:
            num = app.agesImmuneSystem[70]
        elif 80 <= app.ageOfPatient <= 90:
            num = app.agesImmuneSystem[80]
        else: 
            num = app.agesImmuneSystem[90]
        while num > 0:
            app.displaybreast += [app.mutateddisplaybreast[cellindex]]
            app.mutateddisplaybreast.remove(app.mutateddisplaybreast[cellindex])
            num -= 1

def datavisualizationLevel(app):
    if app.iterationOfdataVisualization == 1:
        element = 1
        while element < app.axes+2:
            #datavisualization
            app.xincrement = len(app.totalxaxes)//app.axes
            app.yincrement = int(9/4*(int(app.inputcells)//app.axes))
            app.xaxes += [app.xincrement*element]
            app.yaxes += [app.yincrement*element]
            element += 1 
        app.iterationOfdataVisualization += 1
    for index1 in range(len(app.healthycells)-2):
        #create graph for the healthy cells
        if index1 == 0:
            #first position
            firstcell = app.healthycells[0]
            for index2 in range(len(app.yaxes)-1):
                if app.yaxes[index2] <= firstcell <= app.yaxes[index2+1]:
                    y1 = 450-(25*(index2+1))
            (x0,y0) = (125,y1)
            for index3 in range(len(app.yaxes)-1):
                if app.yaxes[index3] <= app.healthycells[1] <= app.yaxes[index3+1]:
                    y2 = 450-(25*(index3+1))
            (x1,y1) = (150,y2)
            app.healthycellcoordinates += [(x0,y0,x1,y1)]
        else:
            for index4 in range(len(app.yaxes)-1):
                if app.yaxes[index4] <= app.healthycells[index1] <= app.yaxes[index4+1]:
                    y1 = 450-(25*index4)
            (x0,y0) = (125+(25*app.incrementOfHealthy),y1)
            for index5 in range(len(app.yaxes)-1):
                if app.yaxes[index5] <= app.healthycells[index1] <= app.yaxes[index5+1]:
                    y2 = 450-(25*index5)
            (x1,y1) = (125+(25*(app.incrementOfHealthy+1)),y2)
            (_,y2,_,y3) = app.healthycellcoordinates[-1]
            if x1 < 500:
                if y2 != y0 and y3 != y1:
                    app.healthycellcoordinates += [(x0,y3,x1,y1)]
                    app.incrementOfHealthy += 1
    for index6 in range(len(app.cancercells)-2):
        #create graph for the cancer cells
        if index6 == 0:
            firstcell = app.cancercells[0]
            for index7 in range(len(app.yaxes)-1):
                if app.yaxes[index2] <= firstcell <= app.yaxes[index2+1]:
                    y1 = 450-(25*(index7+1))
            (x0,y0) = (125,y1)
            for index8 in range(len(app.yaxes)-1):
                if app.yaxes[index8] <= app.cancercells[1] <= app.yaxes[index8+1]:
                    y2 = 450-(25*(index8+1))
            (x1,y1) = (150,y2)
            app.cancercellcoordinates += [(x0,y0,x1,y1)]
        else:
            for index9 in range(len(app.yaxes)-1):
                if app.yaxes[index9] <= app.cancercells[index6] <= app.yaxes[index9+1]:
                    y1 = 450-(25*index9)
            (x0,y0) = (125+(25*app.incrementOfCancer),y1)
            for index10 in range(len(app.yaxes)-1):
                if app.yaxes[index10] <= app.cancercells[index6] <= app.yaxes[index10+1]:
                    y2 = 450-(25*index10)
            (x1,y1) = (125+(25*(app.incrementOfCancer+1)),y2)
            (_,y2,_,y3) = app.cancercellcoordinates[-1]
            if x1 < 500:
                if y2 != y0 and y3 != y1:
                    app.cancercellcoordinates += [(x0,y3,x1,y1)]
                    app.incrementOfCancer += 1
            
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
        app.mutationtext = 'Mutation in basepairs 189-191: CGA -> TGA'
    if app.missenseMutations:
        app.mutateDNAsequence = ''
        index = 2
        app.mutationtext = 'Mutation in basepairs 80,791: T -> G'
    if app.frameshiftMutations:
        app.mutateDNAsequence = ''
        index = 3
        app.mutationtext = 'Mutation in basepairs 310,316,317: G,G,T -> A,T,C'
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
    canvas.create_text(app.width/2, 35, text='Breast Cancer Visualizer', font='Arial 32 bold')
    canvas.create_text(app.width/2, 85,text='Press the Cancer Cell to Begin',font='Arial 26 bold')
    x1,y1,x2,y2 = app.instructionsdimensions
    canvas.create_rectangle(x1,y1,x2,y2, fill = 'steel blue')
    canvas.create_text((x1+x2)/2, (y1+y2)/2, text = 'Instructions')

def instructionspage(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'steel blue')
    x1,y1,x2,y2 = app.splashbutton
    canvas.create_rectangle(x1,y1,x2,y2, fill = 'RoyalBlue3')
    canvas.create_text((x1+x2)/2, (y1+y2)/2, text = 'Return Back to Splash Page')
    canvas.create_text(app.width/2, 20, text = 'Instructions', font = 'Arial 32 bold')
    #breast cell section 
    canvas.create_text(65, 100, text = 'Breast Cell Page', font = 'Arial 15')
    canvas.create_image(65,162,image = ImageTk.PhotoImage(app.breastPagePic))
    canvas.create_text(340,115, text = 'At this page, use the slider bar to input the age of the individual.')
    canvas.create_text(340,127, text = 'After pressing the confirmation, enter the number of million cells ')
    canvas.create_text(340,140, text = 'between 1 and 108 and type in a mutation (Nonsense, Missense, ')
    canvas.create_text(340,153, text = 'Frameshift) and press enter. Notice the cells beginning to mutate. ')
    canvas.create_text(340,166, text = 'As the cells change color to depict the mutation. Now you may ')
    canvas.create_text(340,180, text = 'choose to add a therapy to the cancer cells and see the cells ')
    canvas.create_text(340,193, text = 'beginning to revive in the sample. At any point after seeing the ')
    canvas.create_text(340,206, text = 'cells, press the data visualization to see the growth of the cells ')
    canvas.create_text(340,219, text = 'or the cells to move close up level.')
    #cell section 
    canvas.create_text(65, 225, text = 'Cell Page', font = 'Arial 15')
    canvas.create_image(65,287,image = ImageTk.PhotoImage(app.cellPagePic))
    canvas.create_text(340,240, text = 'At this page, notice the same ratio of cells mutated at this stage')
    canvas.create_text(340,253, text = 'In addition notice the greater amount of signals expressed by cells.')
    canvas.create_text(340,266, text = 'As well notice the format of the page with the distinct icons to ')
    canvas.create_text(340,280, text = 'toggle between the different pages and the different mutations. The')
    canvas.create_text(340,293, text = 'highlighted pages are the specific location of the page here. This ')
    canvas.create_text(340,306, text = 'will stay consistent for the rest of the three pages. Press one of')
    canvas.create_text(340,320, text = 'the cells to move to the organelle page.')
    #organelle section
    canvas.create_text(65, 350, text = 'Organelle Page', font = 'Arial 15')
    canvas.create_image(65,412,image = ImageTk.PhotoImage(app.organellePagePic))
    canvas.create_text(340,365, text = 'At this page, notice the different organelles (mitochondria, nucleus')
    canvas.create_text(340,377, text = 'and ribosomes where one undergoes transcription). In addition, notice')
    canvas.create_text(340,390, text = 'inside the nucleus the DNA where its a depiction of the specific DNA')
    canvas.create_text(340,403, text = 'that undergo that mutation that was selected. In addition notice if the')
    canvas.create_text(340,416, text = 'cell is mutated then there is a greater transcription of proteins.')
    canvas.create_text(340,430, text = 'If you press the DNA you enter the DNA page.')
    #DNA section
    canvas.create_text(65, 475, text = 'DNA Page', font = 'Arial 15')
    canvas.create_image(65,537,image = ImageTk.PhotoImage(app.DNAPagePic))
    canvas.create_image(163,537,image = ImageTk.PhotoImage(app.DNATogglePagePic))
    canvas.create_text(405,490, text = 'At this page, notice the DNA of the different cell and mutation.')
    canvas.create_text(405,503, text = 'The bottom of the page there is a key for the nucleotides for ')
    canvas.create_text(405,516, text = 'the DNA expressed for the mutated or unmutated DNA. Then ')
    canvas.create_text(405,530, text = 'presss the nucleotides on the screen to enter a toggle page for ')
    canvas.create_text(405,543, text = 'the DNA. Here you can use the arrow keys to iterate through')
    canvas.create_text(405,556, text = 'all of the nucleotides for the DNA.')

def agePage(app,canvas):
    #age section of page
    canvas.create_text(app.width/2,290,text = 'Choose Age of Patient from 0-150:')
    canvas.create_rectangle(app.width/2-75,app.height/2+50,app.width/2+75,app.height/2+90,fill = 'seashell3')
    (x1,y1,x2,y2) = app.ageslider
    canvas.create_rectangle(x1,y1,x2,y2, fill = 'dim gray')
    canvas.create_text(235,420,text = '0')
    canvas.create_text(370,420,text = '150')
    (x3,y3,x4,y4) = app.ageset
    canvas.create_rectangle(x3,y3,x4,y4, fill = 'light cyan')
    canvas.create_text((x3+x4)/2,(y3+y4)/2, text = f'Press this to set age of patient to: {app.ageOfPatient}')

def breastcellpage(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'snow2')
    canvas.create_text(app.width/2,25, text = 'Breast Cells', font = 'Arial 28 bold')
    canvas.create_rectangle(50,145,550,595, fill = 'PaleTurquoise1')
    for elem in app.displaybreast:
        #if there is no mutation
        x1,y1,x2,y2 = elem
        canvas.create_oval(x1,y1,x2,y2, fill = app.displaybreastcolor)
    for elem in app.mutateddisplaybreast:
        #if ther is a mutation
        x1,y1,x2,y2 = elem
        canvas.create_oval(x1,y1,x2,y2, fill = app.mutateddisplaybreastcolor)
    canvas.create_rectangle(47,142,555,595,outline = 'black', width = '16')
    name = ''
    for elem in app.inputCellsbutton:
        #input button press
        (x1,y1,x2,y2,label) = elem
        canvas.create_rectangle(x1,y1,x2,y2,fill='mint cream')
        canvas.create_text((x1+x2)/2,(y1+y2)/2,text = label)
    if app.inputCellbuttonPressed == 1:
        #return number of cells
        cx1,cy1,cx2,cy2,_ = app.inputCellsbutton[0]
        canvas.create_rectangle(cx1,cy1,cx2,cy2,fill='mint cream')
        name = app.inputcells
        canvas.create_text((cx1+cx2)/2,(cy1+cy2)/2,text = name)
    elif app.inputCellbuttonPressed == 2:
        #return mutation
        mx1,my1,mx2,my2,_ = app.inputCellsbutton[1]
        canvas.create_rectangle(mx1,my1,mx2,my2,fill='mint cream')
        name = app.inputmutation
        canvas.create_text((mx1+mx2)/2,(my1+my2)/2,text = name)
    elif app.inputCellbuttonPressed == 3:
        #return treatment 
        tx1,ty1,tx2,ty2,_= app.inputCellsbutton[2]
        canvas.create_rectangle(tx1,ty1,tx2,ty2,fill='mint cream')
        name = app.inputtreatment
        canvas.create_text((tx1+tx2)/2,(ty1+ty2)/2,text = name)
    canvas.create_text(app.width/2,115, text = app.FinalOutcome)

def datavisualizationpage(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill ='snow2')
    canvas.create_rectangle(app.width/2-250,app.height/2-250,app.width/2+250,app.height/2+250,fill = 'snow3')
    (x1,y1,x2,y2,word) = app.xbox
    canvas.create_rectangle(x1,y1,x2,y2, fill = 'ivory2')
    canvas.create_text((x1+x2)/2,(y1+y2)/2,text = word)
    #axes
    canvas.create_text(125,75,text = 'Number of Cells')
    canvas.create_line(125,100,125,500)
    canvas.create_line(125,100,115,110)
    canvas.create_line(125,100,135,110)
    indexy = 0
    while indexy <= app.axes:
        canvas.create_line(115,100+25*(indexy+1),135,100+25*(indexy+1))
        indexy += 1
    canvas.create_text(110,465,text = '0')
    canvas.create_text(500,500,text = 'Cycle')
    canvas.create_line(75,450,500,450)
    canvas.create_line(490,440,500,450)
    canvas.create_line(490,460,500,450)
    indexx = 0
    while indexx <= app.axes:
        canvas.create_line(125+25*(indexx+1),440,125+25*(indexx+1),460)
        indexx += 1
    #axes segmentation
    for indexx in range(len(app.xaxes)):
        canvas.create_text(150+25*(indexx%(len(app.xaxes))),475,text = str(app.xaxes[indexx]))
    for indexy in range(len(app.yaxes)-1):
        canvas.create_text(100,425-25*(indexy%(len(app.yaxes)-1)),text = str(app.yaxes[indexy]))
    #legend
    canvas.create_rectangle(425,75,525,110,fill = 'royal blue')
    canvas.create_text(475,92,text = 'Healthy Cells')
    canvas.create_rectangle(425,115,525,150, fill = 'orange red')
    canvas.create_text(475,132,text = 'Cancer Cells')
    #Line graphs
    for elem1 in app.healthycellcoordinates:
        (x1,y1,x2,y2) = elem1
        canvas.create_line(x1,y1,x2,y2,fill = 'royal blue')
    for elem2 in app.cancercellcoordinates[:len(app.healthycellcoordinates)]:
        (x3,y3,x4,y4) = elem2
        canvas.create_line(x3,y3,x4,y4,fill = 'orange red')

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
            cellColor = 'wheat3'
        elif cellmutation == 2:
            cellColor = 'wheat2'
        elif cellmutation == 3:
            cellColor = 'wheat1'
        else:
            cellColor = "tan" 
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
        cellColor = 'wheat3'
    if app.missenseMutations:
        cellColor = 'wheat2'
    if app.frameshiftMutations:
        cellColor = 'wheat1'
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
    if app.mutate:
        if app.nonsenseMutations: 
            typeOfMutation = 1
        elif app.missenseMutations:
            typeOfMutation = 2
        elif app.frameshiftMutations:
            typeOfMutation = 3
        #mitochondria text
        canvas.create_rectangle(10,app.height-30,350,app.height-10,fill = 'PeachPuff2')
        canvas.create_text(180,app.height-20,text = app.mitochondriatext[typeOfMutation])
        canvas.create_line(10,app.height-30,mcx,(mcy+mr2)-5)
        canvas.create_line(350,app.height-30,mcx,(mcy+mr2)-5)
        canvas.create_oval(mcx-2,(mcy+mr2)-7,mcx+2,(mcy+mr2)-3,fill='gray')
        #protein text
        canvas.create_rectangle(app.width/2-100,250,app.width/2+200,270,fill='PeachPuff2')
        canvas.create_text(app.width/2+50,260,text = app.proteintext[typeOfMutation])
        canvas.create_line(app.width/2-100,270,app.width/2-28,335)
        canvas.create_line(app.width/2+200,270,app.width/2-28,335)
        canvas.create_oval((app.width/2-30),333,(app.width/2-26),337,fill='gray')

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
        filler = len(app.basepairs[2])*2/3
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "BRCA1 Gene: Nucelotides 80,780-80,810")
    elif app.frameshiftMutations: #frameshift mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"3", "Royal"+tFill+"3", "Spring"+gFill+"4", cFill+"3"
        filler = len(app.basepairs[3])*3/2
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "GATA3 Gene: Nucelotides 300-320")
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
        #the DNA rods
        ((cx,cy),(r1,r2)) = elem
        canvas.create_oval(cx-r1,cy-r2,cx+r1,cy+r2,fill = 'brown')
    canvas.create_rectangle(0,0,app.width,200, fill = "white", outline = "white")
    canvas.create_text(app.width/2, 30, text = 'DNA Page',font = 'Arial 28 bold')
    if app.mutate:
        canvas.create_rectangle(app.width/2-60,app.height/2-100,app.width/2+260,app.height/2-75,fill= 'LemonChiffon2')
        canvas.create_text(app.width/2+100,app.height/2-85,text = app.mutationtext)
        canvas.create_line(app.width/2-50,app.height/2-75,app.width/2+100,app.height/2-40)
        canvas.create_line(app.width/2+250,app.height/2-75,app.width/2+100,app.height/2-40)
        canvas.create_oval(app.width/2+95,app.height/2-35,app.width/2+105,app.height/2-45,fill = 'gray')


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
        #iterate nucleotides
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
    #just the home button
    (x1,y1,x2,y2,word) = app.homebutton
    canvas.create_rectangle(x1,y1,x2,y2,fill = 'plum1')
    canvas.create_text((x1+x2)/2,(y1+y2)/2,text = word)

def datavisualiazationicon(app,canvas):
    #the datavisualization button
    (x3,y3,x4,y4,word2) = app.datavisualization
    canvas.create_rectangle(x3,y3,x4,y4,fill = 'medium purple')
    canvas.create_text((x3+x4)/2,(y3+y4)/2,text = word2)

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
    if app.InstructionsPage:
        instructionspage(app,canvas)
    if app.datavisualizationpage:
        datavisualizationpage(app,canvas)
    if app.breastcell:
        breastcellpage(app,canvas)
    if app.age:
        agePage(app,canvas)
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
    if app.datavisualizationicon:
        datavisualiazationicon(app,canvas)
    if app.icons:
        icons(app,canvas)
    if app.mutationiconsbool:
        mutationicons(app,canvas)

runApp(width = 600, height = 600)