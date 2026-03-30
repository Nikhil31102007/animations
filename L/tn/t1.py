from manim import *

class test(Scene):
    def construct(self):
        
        Axe=Axes(x_range=[-3,3,3],y_range=[-3,3,3],x_length=6,y_length=6,axis_config={"include_numbers":True})

        Axe.to_edge(LEFT)

        b=RoundedRectangle(stroke_color=GREEN,stroke_opacity=.2,
                           fill_color=GREEN_C,fill_opacity=.8,
                           height=2, width=2)
        s=Circle(stroke_color=GREEN,stroke_opacity=.2,
                           fill_color=GREEN_C,fill_opacity=.8,
                           radius=.3)
        self.add(Axe,Axe.get_axis_labels())
        s.to_edge(DR,buff=.2)
        s.set_width(2)
        self.add(s)
        m = Annulus(inner_radius=0.5, outer_radius=1.2,fill_color= YELLOW, stroke_color=YELLOW, stroke_width=2) 
        mob = ParametricFunction(lambda t: [t,0.2*np.sin(10*t),0],t_range = [-TAU, TAU],color= YELLOW) 



        func = lambda pos: ((pos[0]*UR+pos[1]*LEFT) - pos)  
        gay= StreamLines(func,x_range=[-5,5,1], y_range=[-5,5,1],stroke_width=3)
        self.add(gay)

        line1 = Line( LEFT*0.2, RIGHT ) 
        line2 = Line( DOWN*0.2, UP ) 
        a= Angle(line1, line2, dot=True, color=YELLOW, dot_color=YELLOW) 
        self.add(VGroup(line1, line2, a).move_to(ORIGIN)) 

        self.add(b)
        self.play(Write(Axe))

        self.play(b.animate.shift(RIGHT*2),run_time=.5)
        self.play(b.animate.shift(LEFT*2+DOWN*5),run_time=2)
        self.play(b.animate.shift(RIGHT*1+UP*5),run_time=1)
        self.play(Transform(b,m),run_time=1)
        self.add(mob)
        self.play(mob.animate)
        self.wait(3)

 