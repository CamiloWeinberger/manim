from manim import *

class PyrProp(Scene):
    def construct(self):
        text1=MathTex("\Lambda(f_x)")
        text=MathTex(
            "u_3(x\')=",
            "-\\frac{f_1}{f_2}e^{j\kappa(f_1+f_2)}\mathcal{F}[\mathcal{F}[u_1(x)]",
            "]",
        )
        text1=MathTex(
            "u_3(x\')=",
            "-\\frac{f_1}{f_2}e^{j\kappa(f_1+f_2)}\mathcal{F}[\mathcal{F}[u_1(x)]",
            "\Lambda(f_x)]",
        )
        
        self.play(Write(text[0]),Write(text[1]),Write(text[2]))
        self.wait(2)
        self.play(Transform(text,text1),)
        self.wait()