import pygame

#class animation

class AnimateSprite(pygame.sprite.Sprite):

    #define things to do at the beginining of the game
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load("assets/" + sprite_name + ".png")
        self.current_image = 0 #start the anim at 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #define a method do start animation
    def start_animation(self):
        self.animation = True

    #define a method to animate
    def animate(self, loop = False):

        #check if animation is on
        if self.animation:


            #skip to next image
            self.current_image +=1

            #check if at the end of animation
            if self.current_image >= len(self.images):
                #get animation to the start
                self.current_image = 0

                #check if animation is not in loop
                if loop is False:
                    # stop of animation
                    self.animation = False
            #modify the image to the actual one
            self.image = self.images[self.current_image]


#launch sprite images
def load_animation_images(sprite_name):
    #load the images of the file
    images =[]
    #get path for the file
    path = f"assets/{sprite_name}/{sprite_name}"

    #loop all images
    for num in range(1,4):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    #return the list of images
    return images


#create a dictionnary of the images created
#player -> [...Player1.png, ...

animations = {
    "mummy": load_animation_images("mummy"),
    "belaunay": load_animation_images("belaunay")


}