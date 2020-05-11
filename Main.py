from kivy.app import App
from kivy.graphics import Canvas
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.core.window import Window


class MyPage(Widget):
	pass
	# def __init__(self, **kwargs):
	# 	super(FrontPage, self).__init__(**kwargs)

class MyApp(App):
	title = "VPN Account Automator"
	Window.set_title(title)

	def build(self):
		return MyPage()

if __name__ == "__main__":
	myApp = MyApp().run()
