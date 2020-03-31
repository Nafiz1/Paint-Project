#paintproject.py

# individual features:
# undo/redo
# eyedropper
# polygon
# brush
# clear
# music
# spray paint
# highlight selected
# tool description
# show size as circle

#importing
from pygame import *
from random import *
from math import *
from pygame import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

root = Tk()#initializes the Tk engine
root.withdraw()#hides default window


screen = display.set_mode((1024,768))

#colors of tool boxes
black = (0,0,0)
red = (255,0,0)

#loading music and images

#music
init()
mixer.music.load("background/MarioSong.mp3")
mixer.music.play(-1) #loops music
#background
background = image.load("background/background.jpg")
background = transform.scale(background, (1024, 768))
palette = image.load("background/palette.png")
palette = transform.smoothscale(palette, (200, 150))
#stamps
luigi = image.load("stamps/luigi.png")
mario = image.load("stamps/mario.png")
peach = image.load("stamps/peach.png")
bowser = image.load("stamps/bowser.png")
mushroom = image.load("stamps/mushroom.png")
boo = image.load("stamps/boo.png")
#toolbox pictures
pencil = image.load("tool icons/pencil.png")
pencil = transform.smoothscale(pencil, (50, 50))
eraser = image.load("tool icons/eraser.png")
eraser = transform.smoothscale(eraser, (50, 50))
clear = image.load("tool icons/clear.png")
clear = transform.smoothscale(clear, (50, 50))
brush = image.load("tool icons/brush.png")
brush = transform.smoothscale(brush, (50, 50))
eyedropper = image.load("tool icons/eyedropper.png")
eyedropper = transform.smoothscale(eyedropper,(50,50))
spraypaint = image.load("tool icons/spraypaint.png")
spraypaint = transform.smoothscale(spraypaint,(50,50))
rectangle = image.load("tool icons/rectangle.png")
rectangle = transform.smoothscale(rectangle,(50,50))
unfilledrectangle = image.load("tool icons/unfilledrectangle.png")
unfilledrectangle = transform.smoothscale(unfilledrectangle,(50,50))
circle = image.load("tool icons/circle.png")
circle = transform.smoothscale(circle,(50,50))
unfilledcircle = image.load("tool icons/unfilledcircle.png")
unfilledcircle = transform.smoothscale(unfilledcircle,(50,50))
lines = image.load("tool icons/lines.png")
lines = transform.smoothscale(lines,(50,50))
polygon = image.load("tool icons/polygon.png")
polygon = transform.smoothscale(polygon,(50,50))
undo = image.load("tool icons/undo.png")
undo = transform.smoothscale(undo,(40,40))
redo = image.load("tool icons/redo.png")
redo = transform.smoothscale(redo,(40,40))
load = image.load("tool icons/load.png")
save = image.load("tool icons/save.png")
#music pictures
stop = image.load("tool icons/stop.png")
pause = image.load("tool icons/pause.png")
play = image.load("tool icons/play.png")
#text
penciltext = image.load("text/penciltext.jpg")
erasertext = image.load("text/erasertext.jpg")
cleartext = image.load("text/cleartext.jpg")
brushtext = image.load("text/brushtext.jpg")
stampstext = image.load("text/stampstext.jpg")
eyedroppertext = image.load("text/eyedroppertext.jpg")
spraypainttext = image.load("text/spraypainttext.jpg")
rectangletext = image.load("text/rectangletext.jpg")
unfilledrectangletext = image.load("text/unfilledrectangletext.jpg")
circletext = image.load("text/circletext.jpg")
unfilledcircletext = image.load("text/unfilledcircletext.jpg")
linestext = image.load("text/linestext.jpg")
polygontext = image.load("text/polygontext.jpg")
stoptext = image.load("text/stoptext.jpg")
pausetext = image.load("text/pausetext.jpg")
playtext = image.load("text/playtext.jpg")
undotext = image.load("text/undotext.jpg")
redotext = image.load("text/redotext.jpg")
savetext = image.load("text/savetext.jpg")
loadtext = image.load("text/loadtext.jpg")
palettetext = image.load("text/palettetext.jpg")

#bliting background images

#background
screen.blit(background,(0,0))
screen.blit(palette,(5,615))
#stamps
screen.blit(luigi,(220,600))
screen.blit(mario,(350,600))
screen.blit(peach,(466,600))
screen.blit(bowser,(567,600))
screen.blit(mushroom,(687,600))
screen.blit(boo,(795,600))
#toolbox pictures
screen.blit(pencil,(15,80))
screen.blit(eraser,(85,80))
screen.blit(clear,(15,150))
screen.blit(brush,(85,150))
screen.blit(eyedropper,(15,220))
screen.blit(spraypaint,(85,220))
screen.blit(rectangle,(15,290))
screen.blit(unfilledrectangle,(85,290))
screen.blit(circle,(15,360))
screen.blit(unfilledcircle,(85,360))
screen.blit(lines,(15,430))
screen.blit(polygon,(85,430))
screen.blit(undo,(25,510))
screen.blit(redo,(85,510))
screen.blit(load,(960,370))
screen.blit(save,(960,440))
#music pictures
screen.blit(stop,(960,100))
screen.blit(pause,(960,170))
screen.blit(play,(960,240))

#making rects

#background
canvasRect = Rect(160,80,775,500)
paletteRect = Rect(5,615,200,150)
#tools
pencilRect = Rect(15,80,50,50)
eraserRect = Rect(85,80,50,50)
clearRect = Rect(15,150,50,50)
brushRect = Rect(85,150,50,50)
eyedropperRect = Rect(15,220,50,50)
spraypaintRect = Rect(85,220,50,50)
rectangleRect = Rect(15,290,50,50)
unfilledrectangleRect = Rect(85,290,50,50)
circleRect = Rect(15,360,50,50)
unfilledcircleRect = Rect(85,360,50,50)
linesRect = Rect(15,430,50,50)
polygonRect = Rect(85,430,50,50)
undoRect = Rect(25,510,40,40)
redoRect = Rect(85,510,40,40)
colorsquareRect = Rect(5,590,200,20)
sizesquareRect = Rect(910,600,102,102)
descriptionRect = Rect(753,8,244,64)
loadRect = Rect(960,370,40,40)
saveRect = Rect(960,440,40,40)
#music
stopRect = Rect(960,100,40,40)
pauseRect = Rect(960,170,40,40)
playRect = Rect(960,240,40,40)
#stamps
luigiRect = Rect(220,600,122,143)
marioRect = Rect(350,600,108,143)
peachRect = Rect(466,600,93,143)
bowserRect = Rect(567,600,112,143)
mushroomRect = Rect(687,600,100,143)
booRect = Rect(795,600,100,143)

draw.rect(screen,(0,0,0),(908,598,106,106)) #size circle border
draw.rect(screen,(0,0,0),(158,78,779,504)) #canvas border
draw.rect(screen,(255,255,255),canvasRect) #drawing the canvas

#default
color = (255,0,0)
tool = "pencil"
size = 1
pencilsize = 1

#polygon list
pointlist = [] #keeps points for polygon tool

#undo/redo list
undolist = []
redolist = []
#first frame in the undo list is blank
canvascopy = screen.subsurface(canvasRect).copy() #makes copy of blank screen
undolist.append(canvascopy)

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type == MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my) and e.button==1:
                #when the mouse is finished the action it makes a copy and puts it in undo
                canvascopy = screen.subsurface(canvasRect).copy()
                undolist.append(canvascopy)

        if e.type==MOUSEBUTTONDOWN and e.button==1:
            if undoRect.collidepoint(mx,my):
                if len(undolist) > 1: #so it wont crash if you go less then 1
                    redolist.append(undolist[-1]) #redo gets the most recent picture in the undo list
                    undolist.remove(undolist[-1]) #undo gets rid of the most recent picture
                    screen.blit(undolist[-1],(160,80)) #blits the second most recent picture
            if redoRect.collidepoint(mx,my):
                if len(redolist) > 0: #so it wont crash if you go less then 0
                    screen.blit(redolist[-1],(160,80)) #redo first blits the picture
                    undolist.append(redolist[-1]) #undo gets the picture
                    redolist.remove(redolist[-1]) #redo gets rid of the picture
            if tool == "polygon":
                if canvasRect.collidepoint(mx,my):
                    #adds vertices to the polygon where the mouse clicks
                    draw.line(screen,color,(mx,my),(mx,my),1) #to show where the vertices are
                    pointlist.append(mouse.get_pos())

        if e.type == MOUSEBUTTONDOWN:
            if e.button==1: #so scroll wheel does not interfere
                cx,cy = mouse.get_pos() #mouse button click x and y variable
                back = screen.copy()
            if e.button == 4: #when scrolled up
                if size<51: #max size
                   size += 1
                if pencilsize<4: #max pencil size
                    pencilsize += 1
            if e.button == 5: #when scrolled down
                #minimum size
                if size>1:
                   size -= 1
                if pencilsize>1:
                   pencilsize -= 1

    #-------------------------------
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos() #mouse position variable

    if key.get_pressed()[K_ESCAPE]:
        break

    #drawing the rects
    draw.rect(screen,(black),pencilRect,2)
    draw.rect(screen,(black),eraserRect,2)
    draw.rect(screen,(black),clearRect,2)
    draw.rect(screen,(black),eyedropperRect,2)
    draw.rect(screen,(black),brushRect,2)
    draw.rect(screen,(black),spraypaintRect,2)
    draw.rect(screen,(black),rectangleRect,2)
    draw.rect(screen,(black),unfilledrectangleRect,2)
    draw.rect(screen,(black),circleRect,2)
    draw.rect(screen,(black),unfilledcircleRect,2)
    draw.rect(screen,(black),linesRect,2)
    draw.rect(screen,(black),polygonRect,2)
    draw.rect(screen,(black),undoRect,2)
    draw.rect(screen,(black),redoRect,2)
    draw.rect(screen,color,colorsquareRect)
    draw.rect(screen,(255,255,255),sizesquareRect)
    draw.rect(screen,(black),stopRect,2)
    draw.rect(screen,(black),pauseRect,2)
    draw.rect(screen,(black),playRect,2)
    draw.rect(screen,(255,255,255),descriptionRect)
    draw.rect(screen,(black),descriptionRect,2)
    draw.rect(screen,(black),saveRect,2)
    draw.rect(screen,(black),loadRect,2)
    draw.rect(screen,(black),marioRect,2)
    draw.rect(screen,(black),luigiRect,2)
    draw.rect(screen,(black),peachRect,2)
    draw.rect(screen,(black),bowserRect,2)
    draw.rect(screen,(black),mushroomRect,2)
    draw.rect(screen,(black),booRect,2)

    #show size as a circle
    if tool == "pencil":#pencil size is different
        draw.circle(screen,color,(961,651),pencilsize)
    else:
        draw.circle(screen,color,(961,651),size)

    #tool selection code
    if pencilRect.collidepoint(mx,my) or tool == "pencil":
        draw.rect(screen,(red),pencilRect,2)#outlined when hovered over or tool chosen
        screen.blit(penciltext,(755,10))#puts the description of the tool
        if mb[0] == 1: #if clicked tool changes
            tool = "pencil"            
    if eraserRect.collidepoint(mx,my) or tool == "eraser":
        draw.rect(screen,(red),eraserRect,2)
        screen.blit(erasertext,(755,10))
        if mb[0] == 1:
            tool = "eraser"
    if clearRect.collidepoint(mx,my) or tool == "clear":
        draw.rect(screen,(red),clearRect,2)
        screen.blit(cleartext,(755,10))
        if mb[0] == 1:
            tool = "clear"
    if brushRect.collidepoint(mx,my) or tool == "brush":
        draw.rect(screen,(red),brushRect,2)
        screen.blit(brushtext,(755,10))
        if mb[0] == 1:
            tool = "brush"
    if eyedropperRect.collidepoint(mx,my) or tool == "eyedropper":
        draw.rect(screen,(red),eyedropperRect,2)
        screen.blit(eyedroppertext,(755,10))
        if mb[0] == 1:
            tool = "eyedropper"
    if spraypaintRect.collidepoint(mx,my) or tool == "spraypaint":
        draw.rect(screen,(red),spraypaintRect,2)
        screen.blit(spraypainttext,(755,10))
        if mb[0] == 1:
            tool = "spraypaint"
    if rectangleRect.collidepoint(mx,my) or tool == "rectangle":
        draw.rect(screen,(red),rectangleRect,2)
        screen.blit(rectangletext,(755,10))
        if mb[0] == 1:
            tool = "rectangle"
    if unfilledrectangleRect.collidepoint(mx,my) or tool == "unfilledrectangle":
        draw.rect(screen,(red),unfilledrectangleRect,2)
        screen.blit(unfilledrectangletext,(755,10))
        if mb[0] == 1:
            tool = "unfilledrectangle"
    if circleRect.collidepoint(mx,my) or tool == "circle":
        draw.rect(screen,(red),circleRect,2)
        screen.blit(circletext,(755,10))
        if mb[0] == 1:
            tool = "circle"
    if unfilledcircleRect.collidepoint(mx,my) or tool == "unfilledcircle":
        draw.rect(screen,(red),unfilledcircleRect,2)
        screen.blit(unfilledcircletext,(755,10))
        if mb[0] == 1:
            tool = "unfilledcircle"
    if linesRect.collidepoint(mx,my) or tool == "lines":
        draw.rect(screen,(red),linesRect,2)
        screen.blit(linestext,(755,10))
        if mb[0] == 1:
            tool = "lines"
    if polygonRect.collidepoint(mx,my) or tool == "polygon":
        draw.rect(screen,(red),polygonRect,2)
        screen.blit(polygontext,(755,10))
        if mb[0] == 1:
            tool = "polygon"

    #stamp selection code
    if luigiRect.collidepoint(mx,my) or tool == "luigi":
        draw.rect(screen,(255,0,0),luigiRect,2)
        screen.blit(stampstext,(755,10))
        if mb[0] == 1:
            tool = "luigi"
    if marioRect.collidepoint(mx,my) or tool == "mario":
        draw.rect(screen,(255,0,0),marioRect,2)
        screen.blit(stampstext,(755,10))
        if mb[0] == 1:
            tool = "mario"
    if peachRect.collidepoint(mx,my) or tool == "peach":
        draw.rect(screen,(255,0,0),peachRect,2)
        screen.blit(stampstext,(755,10))
        if mb[0] == 1:
            tool = "peach"
    if bowserRect.collidepoint(mx,my) or tool == "bowser":
        draw.rect(screen,(255,0,0),bowserRect,2)
        screen.blit(stampstext,(755,10))
        if mb[0] == 1:
            tool = "bowser"
    if mushroomRect.collidepoint(mx,my) or tool == "mushroom":
        draw.rect(screen,(255,0,0),mushroomRect,2)
        screen.blit(stampstext,(755,10))
        if mb[0] == 1:
            tool = "mushroom"
    if booRect.collidepoint(mx,my) or tool == "boo":
        draw.rect(screen,(255,0,0),booRect,2)
        screen.blit(stampstext,(755,10))
        if mb[0] == 1:
            tool = "boo"

    #music code
    if stopRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),stopRect,2) #only outlines when hovered over
        screen.blit(stoptext,(755,10))
        if mb[0] == 1:
            mixer.music.stop()
            mixer.music.play(-1)
            mixer.music.pause()
            #first stops the music and pauses it so unpause button can work
    if pauseRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),pauseRect,2)
        screen.blit(pausetext,(755,10)) #pauses music
        if mb[0] == 1:
            mixer.music.pause()
    if playRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),playRect,2)
        screen.blit(playtext,(755,10))
        if mb[0] == 1:
            mixer.music.unpause() #unpauses music

    #undo/redo selection code
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),undoRect,2) #only outlines when hovered over
        screen.blit(undotext,(755,10))
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),redoRect,2)
        screen.blit(redotext,(755,10))

    #save/load
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),loadRect,2)
        screen.blit(loadtext,(755,10))
        if mb[0] == 1:
            result = askopenfilename(filetypes = [("Picture files", "*.bmp")]) #asks user for file name
            print(result)
            if result != "":#if user didnt type anything dont continue
                screen.blit(image.load(result),(160,80)) #blits the picture onto the canvas
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),saveRect,2)
        screen.blit(savetext,(755,10))
        if mb[0] == 1:
            result = asksaveasfilename() #asks user for file name
            print(result)
            if result != "":#if user didnt type anything dont continue
                #adds bmp extension to end
                #only saves the canvas
                image.save(screen.subsurface(canvasRect), result+".bmp")
                
    #color palette selection
    if paletteRect.collidepoint(mx,my):
        screen.blit(palettetext,(755,10))
        if mb[0] == 1:
            color = screen.get_at((mx,my))

    #when the mouse is on the canvas
    if mb[2] == 1 and canvasRect.collidepoint(mx,my): #left click to make the polygon
        screen.set_clip(canvasRect)
        if tool == "polygon":
            if len(pointlist) > 1: #if point is 1 cant draw polygon
                draw.polygon(screen,color,pointlist,size)
                pointlist = [] #resets when polygon is made
        screen.set_clip(None)

    if mb[0] == 1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        #tools
        if tool == "pencil":
            draw.line(screen,color,(omx,omy),(mx,my),pencilsize)
        if tool == "eraser":
            dist = max(hypot(mx-omx,my-omy),1) #finds distance from old mouse position to mouse position
            sx = (mx-omx)/dist #small x
            sy = (my-omy)/dist #small y
            #for every pixel in distance make a circle
            for i in range(int(dist)):
                draw.circle(screen,(255,255,255),(int(omx+sx*i),int(omy+sy*i)),size)
        if tool == "clear":
            draw.rect(screen,(255,255,255),canvasRect) #makes a white square the size of the background
        if tool == "brush":
            #same as eraser
            dist = max(hypot(mx-omx,my-omy),1)
            sx = (mx-omx)/dist
            sy = (my-omy)/dist
            for i in range(int(dist)):
                draw.circle(screen,color,(int(omx+sx*i),int(omy+sy*i)),size)
        if tool == "eyedropper":
            color = screen.get_at((mx,my))
        if tool == "spraypaint":
            for i in range(size):#to make spraypaint faster
                #makes random x and y points in the size of the circle
                rx = randint(mx-size,mx+size)
                ry = randint(my-size,my+size)
                dist=((mx-rx)**2+(my-ry)**2)**0.5
                #if distance of dots is more then size of circle(radius) it doesnt make dots
                if dist<=size:
                    draw.line(screen,color,(rx,ry),(rx,ry))
        if tool == "rectangle":
            screen.blit(back,(0,0))
            #starts at where the mouse clicks
            #length and width is mouse position minus click position
            draw.rect(screen,color,(cx,cy,mx-cx,my-cy))
        if tool == "unfilledrectangle":
            screen.blit(back,(0,0))
            # draws 4 rectangles to make it seem like 1 rectangle
            # +1 size so it works if size is 1
            # +1 to mx and my because it is drawn 1 pixel off
            # minus size//2 to draw the rectangle in the middle of the mouse
            # width of rectangle depends on size
            draw.rect(screen,color,(cx-(size//2),cy-(size//2),size+1,my+1-cy)) #makes rectangle from my to cy
            draw.rect(screen,color,(cx-(size//2),cy-(size//2),mx+1-cx,size+1)) #makes rectangle from mx to cx
            draw.rect(screen,color,(mx-(size//2),my-(size//2),size+1,cy-my+1)) #makes rectangle from cy to my
            draw.rect(screen,color,(mx-(size//2),my-(size//2),cx-mx+1,size+1)) #makes rectangle from cx to mx
            #make rectangles in each corner to get rid of missing corners
            draw.rect(screen,color,(cx-(size//2),cy-(size//2),size+1,size+1))
            draw.rect(screen,color,(mx-(size//2),my-(size//2),size+1,size+1))
            draw.rect(screen,color,(cx-(size//2),my-(size//2),size+1,size+1))
            draw.rect(screen,color,(mx-(size//2),cy-(size//2),size+1,size+1))
        if tool == "circle":
            screen.blit(back,(0,0))
            circlesize = Rect(cx,cy,mx-cx,my-cy)
            circlesize.normalize()
            draw.ellipse(screen,color,circlesize)
        if tool == "unfilledcircle":
            screen.blit(back,(0,0))
            unfilledcirclesize = Rect(cx,cy,mx-cx,my-cy)
            unfilledcirclesize.normalize()
            #shakes the circle
            #makes circles 1 pixel off to the first one
            unfilledcirclesize1 = Rect(cx+1,cy+1,mx-cx,my-cy)
            unfilledcirclesize1.normalize()
            unfilledcirclesize2 = Rect(cx-1,cy+1,mx-cx,my-cy)
            unfilledcirclesize2.normalize()
            unfilledcirclesize3 = Rect(cx+1,cy-1,mx-cx,my-cy)
            unfilledcirclesize3.normalize()
            unfilledcirclesize4 = Rect(cx-1,cy-1,mx-cx,my-cy)
            unfilledcirclesize4.normalize()
            if size*2<unfilledcirclesize.width and size*2<unfilledcirclesize.height:
                draw.ellipse(screen,color,unfilledcirclesize,size)
                if size > 2:#to make larger sizes look smoother
                    draw.ellipse(screen,color,unfilledcirclesize1,size)
                    draw.ellipse(screen,color,unfilledcirclesize2,size)
                    draw.ellipse(screen,color,unfilledcirclesize3,size)
                    draw.ellipse(screen,color,unfilledcirclesize4,size)
            else: #if width too big, makes a normal ellipse
                draw.ellipse(screen,color,unfilledcirclesize)
        if tool == "lines":
            screen.blit(back,(0,0))
            draw.line(screen,color,(cx,cy),(mx,my),size)
        #stamps
        if tool == "mario":
            screen.blit(back,(0,0))
            screen.blit(mario, (mx-54,my-71))
        if tool == "luigi":
            screen.blit(back,(0,0))
            screen.blit(luigi, (mx-61,my-71))
        if tool == "peach":
            screen.blit(back,(0,0))
            screen.blit(peach, (mx-46,my-71))
        if tool == "bowser":
            screen.blit(back,(0,0))
            screen.blit(bowser, (mx-56,my-71))
        if tool == "mushroom":
            screen.blit(back,(0,0))
            screen.blit(mushroom, (mx-50,my-71))
        if tool == "boo":
            screen.blit(back,(0,0))
            screen.blit(boo, (mx-50,my-71))
        screen.set_clip(None)

    omx,omy = mx,my #old mx and old my
    #-------------------------------
    display.flip()
quit()




