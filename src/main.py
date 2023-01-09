import kivy
import random
from kivy.app import App
from kivy.uix.label import Label

class JokeApp(App):
    def build(self):
        jokes = [
          
            "Why was the math book sad? Because it had too many problems.",
            "Why did the edge server go bankrupt? Because it ran out of cache."
            "Why did the Java developer teach his young kids about single quotes? Because they build character"
            "Why do most Java programmers wear glasses? Because they don’t see sharp"
            
        ]
        joke = random.choice(jokes)
        return Label(text=joke)

if __name__ == "__main__":
    JokeApp().run()
