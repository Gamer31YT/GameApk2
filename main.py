from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongBall(Widget):

    #Скорость движения нашего шарика по двум осям 
    velocity_x = NumericProperty(0) # type: ignore
    velocity_y = NumericProperty


class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongGame().run()