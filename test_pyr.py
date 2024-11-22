from manim import *

class PyrProp(Scene):
    def construct(self):
        text1=MathTex("\Lambda(f_x)")
        text=MathTex(
            "u_3(x\')=",
            "-\\frac{f_1}{f_2}e^{j\kappa(f_1+f_2)}\mathcal{F}[\mathcal{F}[u_1(x)]",
            "]",
        ).move_to(UP*2)
        text1=MathTex(
            "u_3(x\')=",
            "-\\frac{f_1}{f_2}e^{j\kappa(f_1+f_2)}\mathcal{F}[\mathcal{F}[u_1(x)]",
            "\Lambda(f_x)]",
        ).move_to(UP*2)
        
        ax = Axes(
            x_range = [0,10],
            y_range = [0,2],       
        )
        labels = ax.get_axis_labels()
        L1x1 = ax.plot(lambda x: 1, x_range=[0,2], color=RED)
        L1x2 = ax.plot(lambda x: 0, x_range=[0,2], color=RED)
        L2x1 = 
        
        self.add(ax,labels,L1x1,L1x2)
        self.play(Write(text[0]),Write(text[1]),Write(text[2]))
        self.wait(2)
        self.play(Transform(text,text1),)
        self.wait()