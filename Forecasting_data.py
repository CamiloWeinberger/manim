from manim import *

class Data_create(Scene):
    def construct(self):
        mob= Square()
        text = MarkupText('Seeing<sub>t</sub>')
        text.next_to(mob, UP)
        
        mob2= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        text2 = MarkupText('S<sub>t</sub>   S<sub>t+1</sub>   S<sub>t+2</sub>   S<sub>t+3</sub>   S<sub>t+3</sub>      ...      S<sub>t+k</sub>').scale(.6)
        text2.next_to(mob2, UP)

        self.play(Create(mob,),Write(text))
        self.wait(2)
        self.play(Transform(mob,mob2), Transform(text,text2))
        self.wait(2)
        self.play(mob2.animate.move_to(UP*0.8 + RIGHT*0.8 ))
        mob2= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        self.play(mob2.animate.move_to(UP*0.4 + RIGHT*0.4))
        mob2= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        self.play(mob2.animate.move_to(UP*0 + RIGHT*0))
        mob2= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        self.play(mob2.animate.move_to(DOWN*0.4 + LEFT*0.4))
        mob2= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        self.play(mob2.animate.move_to(DOWN*0.8 + LEFT*0.8))
        mob2= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        self.play(mob2.animate.move_to(DOWN*1.2 + LEFT*1.2))
        mob = Square(color= RED, fill_opacity = .5)
        text = MarkupText('Dataset').next_to(mob,DOWN*2.4)
        self.play(Create(mob.scale(1.5)), Write(text))
        self.wait(4)

