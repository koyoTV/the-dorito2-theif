import pygame

def spriteSheetToList( sourceImage, numberColumns):
    imageList = []
    sourceRect = sourceImage.get_rect()
    spriteWidth = sourceRect.width / numberColumns
    spriteHeight = sourceRect.height
    for column in range(numberColumns):
        subImage = sourceImage.subsurface(pygame.Rect((spriteWidth*column,0),
                                                      (spriteWidth,spriteHeight)))
        imageList.append(subImage)
    return imageList
