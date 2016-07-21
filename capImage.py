import pygame
import pygame.camera
import indicoio

#capturing photo using pygame
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()
img = cam.get_image()
import pygame.image
pygame.image.save(img, "photo.png")
pygame.camera.quit()

#Sentiment analysis
def calculateSentimate(path):
	indicoio.config.api_key = '1329497cc5ba31312cd9f0777ffb4bad'
	#filepath='/home/suparna/Pictures/1.png'
	print(indicoio.fer(path))
	return indicoio.fer(path)


calculateSentimate("photo.png")

