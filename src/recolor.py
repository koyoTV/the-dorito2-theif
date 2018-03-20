import pygame

def recolor(surface, colorfactor):
    newsurface = surface.copy()
    newsurface = newsurface.convert_alpha()
    for x in range(newsurfaceface.get_width()):
        for y in range(newsurface.get_height()):
            currentcolor = newsurface.get_at([x,y])
            newred = (currentcolor[0] + colorfactor[0])%256
            newgreen = (currentcolor[1] + colorfactor[1])%256
            newblue = (currentcolor[2] + colorfactor[2])%256
            newsurface.set_at([x,y]), (newred, newgreen, newblue, currentcolor[3])))
    return newsurface
            
