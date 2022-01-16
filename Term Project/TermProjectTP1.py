from cmu_112_graphics import *

def appStarted(app):
    #splash page formatting
    app.splashPage = True
    app.startButtonDim = ((app.width/2-100,app.height/2+50),(app.width/2+100,app.height/2+100))
    app.splashPageCellOrganellesCenters = [(app.width/2-50,app.height/2+55),(app.width/2-72,app.height/2+65),(app.width/2-65,app.height/2+90),
                                           (app.width/2-35,app.height/2+70), (app.width/2-25,app.height/2+75), (app.width/2-15,app.height/2+62), 
                                           (app.width/2-40,app.height/2+93), (app.width/2-45,app.height/2+73), (app.width/2-7,app.height/2+85),
                                           (app.width/2+50,app.height/2+55),(app.width/2+72,app.height/2+65),(app.width/2+65,app.height/2+90),
                                           (app.width/2+35,app.height/2+70), (app.width/2+25,app.height/2+75), (app.width/2+15,app.height/2+92), 
                                           (app.width/2+40,app.height/2+93), (app.width/2+45,app.height/2+73), (app.width/2+5,app.height/2+85),]

    #icons for all of the pages
    app.icons = False
    topright = app.width-90
    app.icondimensions = [((topright,25),(topright+70,75),1),
                          ((topright,75),(topright+70,125),2),
                          ((topright,125),(topright+70,175),3)]
    app.mutationiconsbool = False
    app.mutationIcons = [((app.width/2-280,100),(app.width/2-150,150),"Nonsense-Mutation"),
                         ((app.width/2-125,100),(app.width/2+15,150),"Mis-Sense Mutation"),
                         ((app.width/2+40,100),(app.width/2+180,150),"Frame-Shift Mutation")]
   
    #mutations
    #mutations for page
    app.nonsenseMutations = True
    app.missenseMutations = False
    app.frameshiftMutations = False

    #mutations button
    app.mutationButton = (50,30,150,70, "Mutate")
    app.mutate = False

    #visualization of Cell page
    app.cellPage = False
    app.radius = 10
    app.cellCenters = [((15, app.height-25),(app.radius, app.radius*2)),
                       ((70, app.height-25),(app.radius, app.radius*2)),
                       ((15, app.height-100),(app.radius, app.radius*2))]

    #visualization of Organelle page
    app.organellePage = False
    app.organelleCellDimensions = ((app.width/2,2*app.height/3),(app.width/2-20,100))
    app.organelleDNA = []

    #visualization of DNA page
    app.DNAPage = False
    DNArod1 = ((app.width/2,app.height/5+150),(app.width/2,20))
    DNArod2 = ((app.width/2,4*app.height/5-10),(app.width/2,20))
    app.DNAdimensions = [DNArod1,DNArod2]
    app.basepairs = {1:"gagcgctgctcagatagcgatggtctggcccctcctcagcatcttatccgagtggaaggaaatttgcgtgtggagtatttggat",
                     2:"cgaggagagtgaagaagtca",
                     3:"aactgtcagaccaccacaaccacactctggaggaggaatgccaatggggaccctgtctgc"}
    app.DNAsequence = ''
    #Nonsense-Mutation: https://www.ncbi.nlm.nih.gov/nuccore/NM_001276696.3, https://www.frontiersin.org/articles/10.3389/fonc.2017.00323/full
    #Mis-sense Mutation: https://cancerres.aacrjournals.org/content/canres/early/2010/01/26/0008-5472.CAN-09-2850.full.pdf
    #FrameShift Mutation: https://www.ncbi.nlm.nih.gov/nuccore/NM_001002295.2,https://bmccancer.biomedcentral.com/articles/10.1186/1471-2407-14-278

    #Toggle Visualization DNA Page
    app.DNATogglePage = False
    app.DNAToggleSequence = []
    if app.nonsenseMutations: 
        for c in app.basepairs[1]:
            app.DNAToggleSequence += [c]
    if app.missenseMutations:
        for c in app.basepairs[2]:
            app.DNAToggleSequence += [c]
    if app.frameshiftMutations:
        for c in app.basepairs[3]:
            app.DNAToggleSequence += [c]
    app.indexright = 10
    app.indexleft = 0
    #pause function
    app.paused = False

def mousePressed(app,event):
    ((cx1,cy1),(cx2,cy2)) = app.startButtonDim
    if (app.splashPage == True) and (cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2):
        #splash page and true statements
        app.splashPage = False
        app.cellPage = True
        app.icons = True
        app.mutationiconsbool = True
    if app.splashPage == False:
        #iteration between the pages
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
            if string == "Mis-Sense Mutation" and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #mis-sense mutations
                app.nonsenseMutations = app.frameshiftMutations = False
                app.missenseMutations = True
                app.mutate = False
            if string == "Frame-Shift Mutation" and cx1 <= event.x <= cx2 and cy1 <= event.y <= cy2:
                #frame-shift mutationss
                app.nonsenseMutations = app.missenseMutations = False
                app.frameshiftMutations = True
                app.mutate = False
        mutatecx1, mutatecy1, mutatecx2, mutatecy2,mutatetext = app.mutationButton
        if mutatecx1 <= event.x <= mutatecx2 and mutatecy1 <= event.y <= mutatecy2:
            #mutate button
            app.mutate = True
        if app.cellPage:
            for elem in app.cellCenters:
                ((cx,cy),(r1,r2)) = elem
                if cx-r1 <= event.x <= cx+r1 and cy-r2 <= event.y <= cy+r2:
                    app.cellPage = False
                    app.organellePage = True
        if app.organellePage:
            ((cellcx, cellcy), (cellr1, cellr2)) = app.organelleCellDimensions
            topleftx,toplefty,bottomrightx,bottomrighty=((cellcx*3/2)-(cellr1/4)+30),(cellcy-(cellr2*2/3)+30),((cellcx*3/2)+(cellr1/4)-30),(cellcy*5/4-(cellr2/3)-30)
            if topleftx <= event.x <= bottomrightx and toplefty <= event.y <= bottomrighty:
                app.organellePage = False
                app.DNAPage = True
        if app.DNAPage:
            (((dnarodcx1,dnarodcy1),(dnarodr11,dnarodr21)),((dnarodcx2,dnarodcy2),(dnarodr12,dnarodr22))) = app.DNAdimensions
            if dnarodcx1-dnarodr11 <= event.x <= dnarodcx2+dnarodr12 and dnarodcy1-dnarodr21 <= event.y <= dnarodcy2+dnarodr22:
                app.DNAPage = False
                app.DNATogglePage = True

def keyPressed(app,event):
    if app.nonsenseMutations: 
        location = app.basepairs[1]
    if app.missenseMutations:
        location = app.basepairs[2]
    if app.frameshiftMutations:
        location = app.basepairs[3]
    if app.DNATogglePage:
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
    if (not app.paused):
        doStep(app) 

def doStep(app):
    if app.cellPage:
        if app.mutate: 
            mutateCellLevel(app)
        cellLevel(app)
    if app.organellePage:
        organelleLevel(app)
    if app.DNAPage:
        DNALevel(app)

       
def cellLevel(app):
    fibonaccinumber = 2
    cellx, celly = 150, 220
    app.cellCenters = [((15, app.height-25),(app.radius, app.radius*2)),
                       ((70, app.height-25),(app.radius, app.radius*2)),
                       ((15, app.height-100),(app.radius, app.radius*2))]
    while len(app.cellCenters) < 250:
        #create all of the cells starting from bottom left corner
        for elem in app.cellCenters[-fibonaccinumber:]:
            ((cx,cy),(r1,r2)) = elem
            if ((cx+cellx,cy),(r1,r2)) not in app.cellCenters:
                app.cellCenters.append(((cx+cellx,cy),(r1,r2)))
            elif ((cx,cy-celly),(r1,r2)) not in app.cellCenters:
                app.cellCenters.append(((cx,cy-celly),(r1,r2)))
            fibonaccinumber += 1

def mutateCellLevel(app):
    fibonaccinumber = 2
    cellx, celly = 75, 125
    app.cellCenters = [((15, app.height-25),(app.radius, app.radius*2)),
                       ((70, app.height-25),(app.radius, app.radius*2)),
                       ((15, app.height-100),(app.radius, app.radius*2))]
    while len(app.cellCenters) < 500:
    #create all of the cells starting from bottom left corner
        for elem in app.cellCenters[:fibonaccinumber]:
            ((cx,cy),(r1,r2)) = elem
            if ((cx+cellx,cy),(r1,r2)) not in app.cellCenters:
                app.cellCenters.append(((cx+cellx,cy),(r1,r2)))
            elif ((cx,cy-celly),(r1,r2)) not in app.cellCenters:
                app.cellCenters.append(((cx,cy-celly),(r1,r2)))
            fibonaccinumber += 1       

def organelleLevel(app):
    #create the template for the DNA sequence at this level
    if app.nonsenseMutations:
        app.organelleDNA = []
        while len(app.organelleDNA) < 16:
            for c in app.basepairs[1][:8]:
                app.organelleDNA += [c]
            for c in app.basepairs[1][-8:]:
                app.organelleDNA += [c]
    if app.missenseMutations:
        app.organelleDNA = []
        while len(app.organelleDNA) < 16:
            for c in app.basepairs[2][:8]:
                app.organelleDNA += [c]
            for c in app.basepairs[2][-8:]:
                app.organelleDNA += [c]
    if app.frameshiftMutations:
        app.organelleDNA = []
        while len(app.organelleDNA) < 16:
            for c in app.basepairs[3][:8]:
                app.organelleDNA += [c]
            for c in app.basepairs[3][-8:]:
                app.organelleDNA += [c]

def DNALevel(app):
    #create DNA sequence for the different mutations
    if app.nonsenseMutations:
        app.DNAsequence = ''
        for c in app.basepairs[1]:
            app.DNAsequence += c
    if app.missenseMutations:
        app.DNAsequence = ''
        for c in app.basepairs[2]:
            app.DNAsequence += c
    if app.frameshiftMutations:
        app.DNAsequence = ''
        for c in app.basepairs[3]:
            app.DNAsequence += c        
        
def splashpage(app,canvas):
    #splash page of the app
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'SeaGreen3')
    canvas.create_oval(0,200,app.width,app.height+350, fill= 'DarkOliveGreen2', outline = 'DarkOliveGreen2')
    canvas.create_oval(0,250,app.width,app.height+250, fill= 'DarkOliveGreen3', outline = 'DarkOliveGreen3')
    canvas.create_text(app.width/2, 75, text='Breast Cancer Visualizer', font='Arial 32 bold')
    canvas.create_text(app.width/2, 125,text='Press the Cancer Cell to Begin',font='Arial 26 bold')
    ((cx1,cy1),(cx2,cy2)) = app.startButtonDim
    cradius = 40
    midpointx = (cx1+cx2)/2
    canvas.create_rectangle(cx1+60, cy1, cx2-60, cy2+10, fill='MediumOrchid4', outline = 'MediumOrchid4')
    canvas.create_oval((midpointx+cx1)/2-cradius, (cy1+cy2)/2-cradius+10,(midpointx+cx1)/2+cradius,(cy1+cy2)/2+cradius+10, fill = 'MediumOrchid4', outline = 'MediumOrchid4')
    canvas.create_oval((midpointx+cx2)/2-cradius, (cy1+cy2)/2-cradius+10,(midpointx+cx2)/2+cradius,(cy1+cy2)/2+cradius+10, fill = 'MediumOrchid4', outline = 'MediumOrchid4')
    canvas.create_rectangle(cx1+20, cy1, cx2-20, cy2, fill='MediumOrchid2', outline = 'MediumOrchid2')
    canvas.create_oval((midpointx+cx1)/2-cradius, (cy1+cy2)/2-cradius,(midpointx+cx1)/2+cradius,(cy1+cy2)/2+cradius, fill = 'MediumOrchid2', outline = 'MediumOrchid2')
    canvas.create_oval((midpointx+cx2)/2-cradius, (cy1+cy2)/2-cradius,(midpointx+cx2)/2+cradius,(cy1+cy2)/2+cradius, fill = 'MediumOrchid2', outline = 'MediumOrchid2')
    for elem in app.splashPageCellOrganellesCenters:
        cx,cy = elem
        radius1, radius2 = 3,7
        canvas.create_oval(cx-radius1,cy-radius2,cx+radius1,cy+radius2,fill="SlateBlue1", outline = "SlateBlue1")

def cellpage(app,canvas):
    color = 'sky blue'
    canvas.create_rectangle(0,0,app.width,app.height, fill = color) #background color
    if app.nonsenseMutations:
        cellColor = 'wheat1'
    if app.missenseMutations:
        cellColor = 'wheat2'
    if app.frameshiftMutations:
        cellColor = 'wheat3'
    for elem in app.cellCenters:
        ((cx,cy),(r1,r2))= elem
        canvas.create_oval(cx-r1,cy-r2,cx+r1,cy+r2,fill=cellColor) #cells
        canvas.create_oval(cx-(r1/2),cy-(r2*2/3),cx+(r1/2),cy-(r2/3), fill= "peach puff") #nucelus
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
    canvas.create_oval(cellcx-cellr1,cellcy-cellr2,cellcx+cellr1,cellcy+cellr2,fill=cellColor) #cell
    canvas.create_oval((cellcx*3/2)-(cellr1/4),cellcy-(cellr2*2/3),(cellcx*3/2)+(cellr1/4),cellcy*5/4-(cellr2/3), fill= "peach puff") #nucleus
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
        if count < 9: DNAadjx += 5
        else: DNAadjx -= 5
    canvas.create_line((cellcx*3/2)-(cellr1/4)+30,cellcy-(cellr2*2/3)+30,(cellcx*3/2)+(cellr1/4)-30,cellcy*5/4-(cellr2/3)-30,fill= "brown", width = 10)
    canvas.create_line((cellcx*3/2)+(cellr1/4)-30,cellcy-(cellr2*2/3)+30,(cellcx*3/2)-(cellr1/4)+30,cellcy*5/4-(cellr2/3)-30,fill= "brown", width = 10)
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
        filler = len(app.basepairs[1])/12
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "TP53 Gene: Nucelotides 170-250")

    elif app.missenseMutations: #missense mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"2", "Royal"+tFill+"2", "Spring"+gFill+"3", cFill+"2"
        filler = len(app.basepairs[2])*3/2
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "BRCA1 Gene: Nucelotides 80,780-80,798")

    elif app.frameshiftMutations: #frameshift mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"3", "Royal"+tFill+"3", "Spring"+gFill+"4", cFill+"3"
        filler = len(app.basepairs[3])/6
        #Labels of Gene
        canvas.create_text(app.width/2, app.height-70, text = "GATA3 Gene: Nucelotides 1,530-1,590")
    
    for c in app.DNAsequence:
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
    elif app.missenseMutations: #missense mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"2", "Royal"+tFill+"2", "Spring"+gFill+"3", cFill+"2"
    elif app.frameshiftMutations: #frameshift mutations
        aColor, tColor, gColor, cColor = "Indian"+aFill+"3", "Royal"+tFill+"3", "Spring"+gFill+"4", cFill+"3"
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
            if app.DNAPage:
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
    if app.cellPage:
        cellpage(app,canvas)
    if app.organellePage:
        organellepage(app,canvas)
    if app.DNAPage:
        DNApage(app,canvas)
    if app.DNATogglePage:
        DNATogglePage(app,canvas)
    if app.icons:
        icons(app,canvas)
    if app.mutationiconsbool:
        mutationicons(app,canvas)

runApp(width = 600, height = 600)