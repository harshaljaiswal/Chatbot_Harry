import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from api.ai import Agent
import json

#initialize the agent
agent = Agent(
     '<subscription-key>',
     '9eb285851f6d47a5a1d970e77b16f3de',
     'f1d3838773f04e4bb94dc3706a94647e',
)

class CalcGridLayout(GridLayout):
    def __init__(self):
        super(CalcGridLayout,self).__init__()

    def API_call(self,user_input):
        response = agent.query(user_input)
        result = response['result']
        fulfillment = result['fulfillment']
        return fulfillment['speech']


class calculatorApp(App):
    def build(self):
        return CalcGridLayout()

calcApp= calculatorApp()
calcApp.run()