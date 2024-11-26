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
        ).set_color(BLACK)
        labels = ax.get_axis_labels().set_color(BLACK)
        L1x1 = ax.plot(lambda x: 1, x_range=[0,2], color=RED)
        L1x2 = ax.plot(lambda x: 0, x_range=[0,2], color=RED)
        L2x1 = ax.plot(lambda x: x/4-2/4, x_range=[2,6], color=RED)
        L2x2 = ax.plot(lambda x: 1+2/4-x/4, x_range=[2,6], color=RED)
        
        L3x1 = ax.plot(lambda x: 1, x_range=[6,8], color=RED)
        L3x2 = ax.plot(lambda x: 0, x_range=[6,8], color=RED)
        L4x1 = ax.plot(lambda x: 2/3, x_range=[6,8], color=RED)
        L4x2 = ax.plot(lambda x: 1/3, x_range=[6,8], color=RED)
        
        self.add(ax,labels,L1x1,L1x2,L2x1,L2x2,L3x1,L3x2,L4x1,L4x2)
        self.play(Write(text[0]),Write(text[1]),Write(text[2]))
        self.wait(2)
        self.play(Transform(text,text1),)
        self.wait()