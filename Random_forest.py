from  manim import *

class Random_forest(Scene):
    def construct(self):
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

        self.play(FadeIn(mob0.scale(.5)))
        self.wait(2)
        self.play(Rotate(mob0,PI/2),
                  Transform(mob0,mob0.add_highlighted_cell((2,2),color=RED).add_highlighted_cell((3,2),color=RED).add_highlighted_cell((4,2),color=RED).add_highlighted_cell((5,2),color=RED).add_highlighted_cell((6,2),color=RED).add_highlighted_cell((7,2),color=RED)),
                  Transform(mob0,mob0.add_highlighted_cell((2,3),color=BLUE).add_highlighted_cell((3,3),color=BLUE).add_highlighted_cell((4,3),color=BLUE).add_highlighted_cell((5,3),color=BLUE).add_highlighted_cell((6,3),color=BLUE).add_highlighted_cell((7,3),color=BLUE)),
                  Transform(mob0,mob0.add_highlighted_cell((2,4),color=GREEN).add_highlighted_cell((3,4),color=GREEN).add_highlighted_cell((4,4),color=GREEN).add_highlighted_cell((5,4),color=GREEN).add_highlighted_cell((6,4),color=GREEN).add_highlighted_cell((7,4),color=GREEN)),
                  Transform(mob0,mob0.add_highlighted_cell((2,5),color=YELLOW).add_highlighted_cell((3,5),color=YELLOW).add_highlighted_cell((4,5),color=YELLOW).add_highlighted_cell((5,5),color=YELLOW).add_highlighted_cell((6,5),color=YELLOW).add_highlighted_cell((7,5),color=YELLOW)),
                  Transform(mob0,mob0.add_highlighted_cell((2,6),color=ORANGE).add_highlighted_cell((3,6),color=ORANGE).add_highlighted_cell((4,6),color=ORANGE).add_highlighted_cell((5,6),color=ORANGE).add_highlighted_cell((6,6),color=ORANGE).add_highlighted_cell((7,6),color=ORANGE)),        
                  )
        
        t1 = Table([['S0','T0','C0','P0','o0']], include_outer_lines=True).scale(.3).move_to(UP*1.2 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t2 = Table([['S1','T1','C1','P1','o1']], include_outer_lines=True).scale(.3).move_to(UP*0.8 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t3 = Table([['S2','T2','C2','P2','o2']], include_outer_lines=True).scale(.3).move_to(UP*.4 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t4 = Table([['S3','T3','C3','P3','o3']], include_outer_lines=True).scale(.3).move_to(UP*0 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        self.play(Transform(mob0,t1),FadeIn(t2),FadeIn(t3),FadeIn(t4))
        
        t2_1 = Table([['S1','T1','C1','P1','o1']], include_outer_lines=True).scale(.3).move_to(UP*1.2 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t3_1 = Table([['S2','T2','C2','P2','o2']], include_outer_lines=True).scale(.3).move_to(UP*.8 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t4_1 = Table([['S3','T3','C3','P3','o3']], include_outer_lines=True).scale(.3).move_to(UP*.4 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        self.play(Transform(mob0,t1))
        self.play(t2_1.animate.move_to(UP*1.2 + LEFT*1),t3_1.animate.move_to(UP*1.2 + RIGHT*2))#,t4_1.animate.move_to(UP*1.2 + RIGHT*5))
        
        t5 = Table([['S2','T2','C2','P2','o2']], include_outer_lines=True).scale(.3).move_to(UP*.8 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t6 = Table([['S3','T3','C3','P3','o3']], include_outer_lines=True).scale(.3).move_to(UP*.4 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        self.play(t5.animate.move_to(UP*.8 + LEFT*1),t6.animate.move_to(UP*.8 + RIGHT*2))
         
        t7 = Table([['S3','T3','C3','P3','o3']], include_outer_lines=True).scale(.3).move_to(UP*.4 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        self.play(t7.animate.move_to(UP*.4 + LEFT*1))
        
        t8 = Table([['S4','T4','C4','P4','o4']], include_outer_lines=True).scale(.3).move_to(DOWN*0.4 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t9 = Table([['S4','T4','C4','P4','o4']], include_outer_lines=True).scale(.3).move_to(DOWN*0.4 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        t10 = Table([['S5','T5','C5','P5','o5']], include_outer_lines=True).scale(.3).move_to(DOWN*1.2 + LEFT*4).add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE)
        self.play(t8.animate.move_to(UP*0 + LEFT*1),t9.animate.move_to(UP*0.4 + RIGHT*2),t10.animate.move_to(UP*0 + RIGHT*2))
        self.wait(2)
        t11 = Table([['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
                    ], include_outer_lines=False).scale(.2)
        t11.add_highlighted_cell((1,1),color=RED).add_highlighted_cell((1,2),color=BLUE).add_highlighted_cell((1,3),color=GREEN).add_highlighted_cell((1,4),color=YELLOW).add_highlighted_cell((1,5),color=ORANGE).add_highlighted_cell((1,6),color=RED).add_highlighted_cell((1,7),color=BLUE).add_highlighted_cell((1,8),color=GREEN).add_highlighted_cell((1,9),color=YELLOW).add_highlighted_cell((1,10),color=ORANGE).add_highlighted_cell((1,11),color=RED).add_highlighted_cell((1,12),color=BLUE).add_highlighted_cell((1,13),color=GREEN).add_highlighted_cell((1,14),color=YELLOW).add_highlighted_cell((1,15),color=ORANGE)
        t11.add_highlighted_cell((2,1),color=RED).add_highlighted_cell((2,2),color=BLUE).add_highlighted_cell((2,3),color=GREEN).add_highlighted_cell((2,4),color=YELLOW).add_highlighted_cell((2,5),color=ORANGE).add_highlighted_cell((2,6),color=RED).add_highlighted_cell((2,7),color=BLUE).add_highlighted_cell((2,8),color=GREEN).add_highlighted_cell((2,9),color=YELLOW).add_highlighted_cell((2,10),color=ORANGE).add_highlighted_cell((2,11),color=RED).add_highlighted_cell((2,12),color=BLUE).add_highlighted_cell((2,13),color=GREEN).add_highlighted_cell((2,14),color=YELLOW).add_highlighted_cell((2,15),color=ORANGE)
        t11.add_highlighted_cell((3,1),color=RED).add_highlighted_cell((3,2),color=BLUE).add_highlighted_cell((3,3),color=GREEN).add_highlighted_cell((3,4),color=YELLOW).add_highlighted_cell((3,5),color=ORANGE).add_highlighted_cell((3,6),color=RED).add_highlighted_cell((3,7),color=BLUE).add_highlighted_cell((3,8),color=GREEN).add_highlighted_cell((3,9),color=YELLOW).add_highlighted_cell((3,10),color=ORANGE).add_highlighted_cell((3,11),color=RED).add_highlighted_cell((3,12),color=BLUE).add_highlighted_cell((3,13),color=GREEN).add_highlighted_cell((3,14),color=YELLOW).add_highlighted_cell((3,15),color=ORANGE)
        t11.add_highlighted_cell((4,1),color=RED).add_highlighted_cell((4,2),color=BLUE).add_highlighted_cell((4,3),color=GREEN).add_highlighted_cell((4,4),color=YELLOW).add_highlighted_cell((4,5),color=ORANGE).add_highlighted_cell((4,6),color=RED).add_highlighted_cell((4,7),color=BLUE).add_highlighted_cell((4,8),color=GREEN).add_highlighted_cell((4,9),color=YELLOW).add_highlighted_cell((4,10),color=ORANGE).add_highlighted_cell((4,11),color=RED).add_highlighted_cell((4,12),color=BLUE).add_highlighted_cell((4,13),color=GREEN).add_highlighted_cell((4,14),color=YELLOW).add_highlighted_cell((4,15),color=ORANGE)
        t12 = Square(grid_xstep = .4, grid_ystep=.4, color= RED, fill_opacity = .5)
        self.play(FadeOut(mob0),FadeOut(t2),FadeOut(t3),FadeOut(t4),FadeOut(t5),FadeOut(t6),FadeOut(t7),FadeOut(t8),
                  FadeOut(t9),FadeOut(t10),FadeOut(t2_1),FadeOut(t3_1),FadeOut(t4_1),
                  FadeIn(t11.move_to(LEFT*4)),FadeIn(t12.move_to(RIGHT*4)),
                  FadeIn(Arrow(LEFT,RIGHT,color= WHITE).move_to(2*LEFT)),
                  FadeIn(Arrow(LEFT,RIGHT,color= WHITE).move_to(2*RIGHT)),
                  FadeIn(Square(color= WHITE)),
                  FadeIn(MarkupText('<small>Model</small>')),
                  FadeIn(MarkupText('<small>Input (Past)</small>').move_to(4*LEFT+UP*2)),
                  FadeIn(MarkupText('<small>Output (Future)</small>').move_to(4*RIGHT+UP*2)),
                  )
    