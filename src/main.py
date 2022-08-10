import kivy
from kivy.app import App
from kivy.uix.label import Label
import pyjokes
  

My_joke = pyjokes.get_joke(language="en", category="neutral")
  

  

class MyApp(App):

    def build(self):
        self.title = 'Developer Joke'
      
        return Label(text=My_joke)

      


if __name__ == '__main__':
    MyApp().run()