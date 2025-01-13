from manim import *

class Data_create(Scene):
    def construct(self):
        ## SCENE 1
        mob= Square()
        text = MarkupText('Seeing t<sub>k</sub>')
        text.next_to(mob, UP)
        
        raw= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        text2 = MarkupText('S<sub>t<sub>0</sub></sub>   S<sub>t<sub>1</sub></sub>   S<sub>t<sub>2</sub></sub>   S<sub>t<sub>3</sub></sub>   S<sub>t<sub>4</sub></sub>   S<sub>t<sub>5</sub></sub>   S<sub>t<sub>6</sub></sub>    ...    S<sub>t<sub>n</sub></sub>').scale(.6)
        text2.next_to(raw, UP)
        
        raw2= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        raw3= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        raw4= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        raw5= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        raw6= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        raw7= Rectangle(height=.4 ,width=6,grid_xstep = .4, grid_ystep=0,color= WHITE).move_to(UP*1.2 + RIGHT*1.2)
        mob2 = Square(color= RED, fill_opacity = .5)
        text3 = MarkupText('Dataset').next_to(mob2,DOWN*2.4)
        
        self.play(Create(mob,),Write(text))
        self.wait(1)
        self.play(Transform(mob,raw), Transform(text,text2))
        self.wait(1)
        self.play(raw2.animate.move_to(UP*0.8 + RIGHT*0.8),
                  raw3.animate.move_to(UP*0.4 + RIGHT*0.4),
                  raw4.animate.move_to(UP*0 + RIGHT*0),
                  raw5.animate.move_to(DOWN*0.4 + LEFT*0.4),
                  raw6.animate.move_to(DOWN*0.8 + LEFT*0.8),
                  raw7.animate.move_to(DOWN*1.2 + LEFT*1.2))
        self.play(Create(mob2.scale(1.5)), Write(text3))
        self.wait(2)
        self.play(FadeOut(text),FadeOut(text2),FadeOut(text3),FadeOut(raw),FadeOut(mob), FadeOut(raw), 
                  FadeOut(raw2),FadeOut(raw3), FadeOut(raw4), FadeOut(raw5),
                  FadeOut(raw6),FadeOut(raw7))
        #self.wait(2)
        ## SCENE 2
        arrow1 = Arrow(2*LEFT, 2*RIGHT,color= YELLOW).next_to(mob2,UP)
        arrow2 = Arrow(2*LEFT, 2*RIGHT,color= YELLOW).rotate(-PI/2).next_to(mob2,LEFT)
        text4 = MarkupText('<small>Sequence</small>').next_to(arrow1,UP)
        text5 = MarkupText('<small>Sample</small>').rotate(PI/2).next_to(arrow2,LEFT)
        self.play(Create(arrow1),Write(text4),Create(arrow2),Write(text5))
        self.wait(2)
        self.play(FadeOut(arrow1),FadeOut(arrow2),FadeOut(text4),FadeOut(text5))
        #self.wait(1)
        
        #class Data_block(Scene):
        #def construct(self):        
        ## SCENE 3
        #mob2 = Square(color= RED, fill_opacity = .5).scale(1.5)
        Data1 = Square(color= BLUE, fill_opacity = .5)
        Data2 = Square(color= GREEN, fill_opacity = .5)
        Data3 = Square(color= YELLOW, fill_opacity = .5)
        Data4 = Square(color= RED, fill_opacity = .5)
        Data5 = Square(color= ORANGE, fill_opacity = .5)
        
        #self.play(Create(mob2))
        T1 = MarkupText('Wind speed',color=BLUE).move_to(LEFT*5.2 + DOWN*2).scale(.5)
        T2 = MarkupText('Temperature',color=GREEN).move_to(LEFT*2.8 + DOWN*2).scale(.5)
        T3 = MarkupText('Pressure',color=YELLOW).move_to(LEFT*5.4 + DOWN*2.5).scale(.5)
        T4 = MarkupText('Seeing',color=RED).move_to(LEFT*3.8 + DOWN*2.5).scale(.5)
        T5 = MarkupText('others',color=ORANGE).move_to(LEFT*2.2 + DOWN*2.5).scale(.5)
        T6 = MarkupText('Seeing',color=RED).move_to(RIGHT*4 + DOWN*2).scale(.5)
        
        self.play(mob2.animate.move_to(RIGHT*4).scale(1/1.5))
        self.play(
                  FadeIn(Data5.move_to(LEFT*3.6 + UP*0.4)),
                  FadeIn(Data4.move_to(LEFT*3.8 + UP*0.2)),
                  FadeIn(Data3.move_to(LEFT*4)),
                  FadeIn(Data2.move_to(LEFT*4.2 + DOWN*.2)),
                  FadeIn(Data1.move_to(LEFT*4.4+DOWN*0.4)),
                  FadeIn(Arrow(LEFT,RIGHT,color= WHITE).move_to(2*LEFT)),
                  FadeIn(Arrow(LEFT,RIGHT,color= WHITE).move_to(2*RIGHT)),
                  FadeIn(Square(color= WHITE)),
                  FadeIn(MarkupText('<small>Model</small>')),
                  FadeIn(MarkupText('<small>Input (Past)</small>').move_to(4*LEFT+UP*2)),
                  FadeIn(MarkupText('<small>Output (Future)</small>').move_to(4*RIGHT+UP*2)),
                  FadeIn(VGroup(T1,T2,T3,T4,T5,T6))
                  )
        
        self.wait(4)
        
     