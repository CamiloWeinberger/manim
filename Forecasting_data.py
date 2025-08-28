from manim import *

class Data_create(Scene):
    def construct(self):
        ## SCENE 0
        mob0 = Table( 
            [['index', 'Seeing', 'Tau', 'Cn2', 'Air pressure', 'others'], 
            ['dd-mm-yyy 00:00','0.427 ','0.01011','0.7290','744.18','...'],
            ['dd-mm-yyy 00:05','0.962 ','0.04186','0.5140','742.40','...'],
            ['dd-mm-yyy 00:10','0.479 ','0.04225','0.6590','745.04','...'],
            ['dd-mm-yyy 00:15','0.672 ','0.06018','0.5657','742.98','...'],
            ['dd-mm-yyy 00:20','0.838 ','0.06203','0.4962','741.71','...'],
            ['...','...','...','...','...','...'],
            ], include_outer_lines=True)
        #mob = Rectangle(height=4, width=1.6, grid_xstep=1, grid_ystep=7, color=WHITE).move_to(DOWN*.4 + LEFT*2.1)
        mob= Rectangle(height=1.6 ,width=4,grid_xstep =.5, grid_ystep=0,color= WHITE).move_to(DOWN*.4 + LEFT*2.1).rotate(-PI/2)

        self.play(FadeIn(mob0.scale(.5)))
        self.wait(2)
        self.play(Rotate(mob0,PI/2),
                  Transform(mob0,mob0.add_highlighted_cell((2,2),color=RED).add_highlighted_cell((3,2),color=RED).add_highlighted_cell((4,2),color=RED).add_highlighted_cell((5,2),color=RED).add_highlighted_cell((6,2),color=RED).add_highlighted_cell((7,2),color=RED)),
                  )
        self.wait(1)
        text = MarkupText('Seeing')
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
        
        #self.play(Create(mob,),Write(text))
        
        self.play(FadeOut(mob0),
                  FadeIn(mob),
                  FadeIn(text))
        #self.wait(1)
        self.play(Transform(mob,raw), Transform(text,text2))
        self.wait(1)
        self.play(raw2.animate.move_to(UP*0.8 + RIGHT*0.8),
                  raw3.animate.move_to(UP*0.4 + RIGHT*0.4),
                  raw4.animate.move_to(UP*0 + RIGHT*0),
                  raw5.animate.move_to(DOWN*0.4 + LEFT*0.4),
                  raw6.animate.move_to(DOWN*0.8 + LEFT*0.8),
                  raw7.animate.move_to(DOWN*1.2 + LEFT*1.2))
        self.play(Create(mob2.scale(1.5)), Write(text3))
        self.wait(1)
        self.play(FadeOut(text),FadeOut(text2),FadeOut(text3),FadeOut(raw),FadeOut(mob), FadeOut(raw), 
                  FadeOut(raw2),FadeOut(raw3), FadeOut(raw4), FadeOut(raw5),
                  FadeOut(raw6),FadeOut(raw7))
        #self.wait(2)
        ## SCENE 2
        arrow1 = Arrow(2*LEFT, 2*RIGHT,color= YELLOW).next_to(mob2,UP)
        arrow2 = Arrow(2*LEFT, 2*RIGHT,color= YELLOW).rotate(-PI/2).next_to(mob2,LEFT)
        text4 = MarkupText('<small>Sampling</small>').next_to(arrow1,UP)
        text5 = MarkupText('<small>Batch</small>').rotate(PI/2).next_to(arrow2,LEFT)
        self.play(Create(arrow1),Write(text4),Create(arrow2),Write(text5))
        self.wait(1)
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
        T1 = MarkupText('Air pressure',color=BLUE).move_to(LEFT*4.8 + DOWN*2).scale(.5)
        T2 = MarkupText('Cn2',color=GREEN).move_to(LEFT*2.8 + DOWN*2).scale(.5)
        T3 = MarkupText('Tau<sub>0</sub>',color=YELLOW).move_to(LEFT*5.4 + DOWN*2.5).scale(.5)
        T4 = MarkupText('Seeing',color=RED).move_to(LEFT*3.8 + DOWN*2.5).scale(.5)
        T5 = MarkupText('others',color=ORANGE).move_to(LEFT*2.2 + DOWN*2.5).scale(.5)
        T6 = MarkupText('Seeing',color=RED).move_to(RIGHT*4 + DOWN*2).scale(.5)
        
        self.play(mob2.animate.move_to(LEFT*3.8 + UP*0.2).scale(1/1.5),
                  FadeIn(Data5.move_to(LEFT*3.6 + UP*0.4)),
                  FadeIn(Data4.move_to(RIGHT*4)),
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
        
     