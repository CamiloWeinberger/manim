from manim import *

class PyrProp(Scene):
    def construct(self):
        text=MathTex("")
        text=MathTex(
            "u_3(x\')=",
            "-\\frac{f_1}{f_2}e^{j\kappa(f_1+f_2)}\mathcal{F}", "[\mathcal{F}[u_1(x)]","","]]",
        )
        text1=MathTex(
             "u_3(x\')=",
            "-\\frac{f_1}{f_2}e^{j\kappa(f_1+f_2)}\mathcal{F}", "[\mathcal{F}","\Lambda(f_x)","]]",
        )
        
        self.play(Write(text,))
        self.wait()
        self.play(ReplacementTransform(text,text1))
        self.wait()