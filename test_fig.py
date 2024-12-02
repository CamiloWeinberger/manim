from manim import *
import scipy.io as scio
import matplotlib.pyplot as plt

class Prop(Scene):
    def construct(self):
        resol = 128
        X, Y = np.meshgrid(np.linspace(-1,1,resol),np.linspace(-1,1,resol))
        R = np.sqrt(X**2+Y**2)*np.sqrt(2)
        pup = R<=.5

        PSF = np.fft.fftshift(np.fft.fft2(pup*np.exp(1j*pup*np.pi*2)))
        PSF = np.abs(PSF)**2
        PSF2 = np.fft.fftshift(np.fft.fft2(pup*np.exp(1j*R*2*np.pi*2)))
        PSF2 = np.abs(PSF2)**2
        imag = ImageMobject(np.uint8(PSF/PSF.max()*255)).set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        imag2 = ImageMobject(np.uint8(PSF2/PSF.max()*255)).set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])

        imag.height = 7
        imag2.height = 7
        
        self.add(imag)
        self.wait()
        self.play(Transform(imag,imag2),)
        self.wait()



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
        imag = ImageMobject('fig1.jpg').to_edge(RIGHT,buff=1)
        imag2 = ImageMobject('fig2.jpg').to_edge(RIGHT,buff=1)

        
        self.add(imag,ax,labels,L1x1,L1x2)
        self.play(Write(text[0]),Write(text[1]),Write(text[2]))
        self.wait(2)
        self.play(Transform(text,text1),Transform(imag,imag2),)
        self.wait()
