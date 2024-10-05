
import pygame
import random
import pandas as pd
pygame.init()



class Game:
    """
    To use this class simply initialize and instance and call the .loop() method
    inside of a pygame event loop (i.e while loop). Inside of your event loop
    you can call the .draw() and .move_paddle() methods according to your use case.
    Use the information returned from .loop() to determine when to end the game by calling
    .reset().
    """
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    
    scale = 5
    trace = 1
    cap = 0.5
    G = 0.011
    speeddivisor = 1.3
    trace1 = []
    trace2 = []
    trace3 = []

    
    def __init__(self, window, window_width, window_height,setstart=[[1.123]]):
        def rand():
          return random.randint(-50,50) 
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        self.setstart = setstart
        def randf():
            return (random.random() - 0.5) /self.speeddivisor
        if self.setstart[0][0] != 1.123:
            
            self.ball1xy = [self.setstart[0][0],self.setstart[0][1] ,self.setstart[0][2],self.setstart[0][3],10,(255, 0, 0)]
            self.ball2xy = [self.setstart[1][0] ,self.setstart[1][1] ,self.setstart[1][2] ,self.setstart[1][3],20,(0, 255, 0)]
            self.ball3xy = [self.setstart[2][0],self.setstart[2][1],self.setstart[2][2] ,self.setstart[2][3],40,(0, 0, 255)]
        else:
            self.ball1xy = [self.window_width/2 + rand(),self.window_height/2 + rand(),randf(),randf(),10,(255, 0, 0)]
            self.ball2xy = [self.window_width/2 + rand() ,self.window_height/2 + rand(),randf(),randf(),20,(0, 255, 0)]
            self.ball3xy = [self.window_width/2+ rand(),self.window_height/2 + rand(),randf(),randf(),40,(0, 0, 255)]

    
    def grav(self):
        def mapt(bool):
            if bool:
                return -1
            return 1

        def grav(m1,m2,dist):
            if dist ==0:
                return 0
            top = self.G * m1 * m2
            bot = dist * dist + 0.4
            return top/bot
             
        def dist(x1,x2,y1,y2):
            p1 = abs(x1-x2) **2
            p2 = abs(y1-y2) **2
            fin =(p1+p2) **0.5
            #if fin <3: fin =3
            return fin
        def force(x1,x2,y1,y2,ma,mb,xory):
            distance = dist(x1,x2,y1,y2)
            if xory == 0:
                p1 = abs(x1-x2)
                p2 = grav(ma,mb,distance)
                return p2 * (p1/distance)
            else:
                p1 = abs(y1-y2)
                p2 = grav(ma,mb,distance)
                return p2 * (p1/distance)

        m1 = self.ball1xy[4]
        m2 = self.ball2xy[4]
        m3 = self.ball3xy[4]

        dist12 = [mapt(self.ball1xy[0] >= self.ball2xy[0]),mapt(self.ball1xy[1] >= self.ball2xy[1]), force(self.ball1xy[0],self.ball2xy[0],self.ball1xy[1],self.ball2xy[1],m1,m2,0),force(self.ball1xy[0],self.ball2xy[0],self.ball1xy[1],self.ball2xy[1],m1,m2,1)]
        dist13 = [mapt(self.ball1xy[0] >= self.ball3xy[0]),mapt(self.ball1xy[1] >= self.ball3xy[1]), force(self.ball1xy[0],self.ball3xy[0],self.ball1xy[1],self.ball3xy[1],m1,m3,0),force(self.ball1xy[0],self.ball3xy[0],self.ball1xy[1],self.ball3xy[1],m1,m3,1)]
        dist23 = [mapt(self.ball2xy[0] >= self.ball3xy[0]),mapt(self.ball2xy[1] >= self.ball3xy[1]), force(self.ball2xy[0],self.ball3xy[0],self.ball2xy[1],self.ball3xy[1],m2,m3,0),force(self.ball2xy[0],self.ball3xy[0],self.ball2xy[1],self.ball3xy[1],m2,m3,1)]
        

        
        apply1 = [0,0]
        apply2 = [0,0]
        apply3 = [0,0]

        apply1[0] += dist12[0] * dist12[2]
        apply1[1] += dist12[1] * dist12[3]
        apply2[0] += -1 * dist12[0] * dist12[2]
        apply2[1] += -1 * dist12[1] * dist12[3]

        apply1[0] += dist13[0] * dist13[2]
        apply1[1] += dist13[1] * dist13[3]
        apply3[0] += -1 * dist13[0] * dist13[2]
        apply3[1] += -1 * dist13[1] * dist13[3]

        apply2[0] += dist23[0] * dist23[2]
        apply2[1] += dist23[1] * dist23[3]
        apply3[0] += -1 * dist23[0] * dist23[2]
        apply3[1] += -1 * dist23[1] * dist23[3]


        


        #change velocities
        self.ball1xy[2] += apply1[0]
        if self.ball1xy[2] > self.cap: self.ball1xy[2] = self.cap
        self.ball1xy[3] += apply1[1]
        if self.ball1xy[3] > self.cap: self.ball1xy[3] = self.cap

        self.ball2xy[2] += apply2[0]
        if self.ball2xy[2] > self.cap: self.ball2xy[2] = self.cap
        self.ball2xy[3] += apply2[1]
        if self.ball2xy[3] > self.cap: self.ball2xy[3] = self.cap

        self.ball3xy[2] += apply3[0]
        if self.ball3xy[2] > self.cap: self.ball3xy[2] = self.cap
        self.ball3xy[3] += apply3[1]
        if self.ball3xy[2] > self.cap: self.ball3xy[2] = self.cap


        #change positions
        self.ball1xy[0] += self.ball1xy[2]
        self.ball1xy[1] += self.ball1xy[3]

        self.ball2xy[0] += self.ball2xy[2]
        self.ball2xy[1] += self.ball2xy[3]

        self.ball3xy[0] += self.ball3xy[2]
        self.ball3xy[1] += self.ball3xy[3]





    def draw(self):
        self.window.fill(self.BLACK)
        pygame.draw.circle(self.window, self.ball1xy[5], (self.ball1xy[0], self.ball1xy[1]), self.ball1xy[4]/self.scale)
        pygame.draw.circle(self.window, self.ball2xy[5], (self.ball2xy[0], self.ball2xy[1]), self.ball2xy[4]/self.scale)
        pygame.draw.circle(self.window, self.ball3xy[5], (self.ball3xy[0], self.ball3xy[1]), self.ball3xy[4]/self.scale)

        for loca in self.trace1:
            pygame.draw.circle(self.window, self.ball1xy[5], (loca), self.trace)
        for loca in self.trace2:
            pygame.draw.circle(self.window, self.ball2xy[5], (loca), self.trace)
        for loca in self.trace3:
            pygame.draw.circle(self.window, self.ball3xy[5], (loca), self.trace)
        
        self.trace1.append((self.ball1xy[0], self.ball1xy[1]))
        self.trace2.append((self.ball2xy[0], self.ball2xy[1]))
        self.trace3.append((self.ball3xy[0], self.ball3xy[1]))
        max_trace_length = 100  # Limit to the last 100 positions
        if len(self.trace1) > max_trace_length:
            self.trace1.pop(0)
        if len(self.trace2) > max_trace_length:
            self.trace2.pop(0)
        if len(self.trace3) > max_trace_length:
            self.trace3.pop(0)


    
    def loop(self):
        """
        Executes a single game loop.

        :returns: GameInformation instance stating score 
                  and hits of each paddle.
        """
        self.grav()

    def reset(self):
        """Resets the entire game."""
        print("reset")
        self.window.fill(self.BLACK)
        def rand():
          return random.randint(-50,50) 
        def randf():
            return (random.random() - 0.5) /self.speeddivisor
        if self.setstart[0][0] != 1.123:
            
            self.ball1xy = [self.setstart[0][0],self.setstart[0][1] ,self.setstart[0][2],self.setstart[0][3],10,(255, 0, 0)]
            self.ball2xy = [self.setstart[1][0] ,self.setstart[1][1] ,self.setstart[1][2] ,self.setstart[1][3],20,(0, 255, 0)]
            self.ball3xy = [self.setstart[2][0],self.setstart[2][1],self.setstart[2][2] ,self.setstart[2][3],40,(0, 0, 255)]
        else:
            self.ball1xy = [self.window_width/2 + rand(),self.window_height/2 + rand(),randf(),randf(),10,(255, 0, 0)]
            self.ball2xy = [self.window_width/2 + rand() ,self.window_height/2 + rand(),randf(),randf(),20,(0, 255, 0)]
            self.ball3xy = [self.window_width/2+ rand(),self.window_height/2 + rand(),randf(),randf(),40,(0, 0, 255)]
        self.trace1 = []
        self.trace2 = []
        self.trace3 = []
