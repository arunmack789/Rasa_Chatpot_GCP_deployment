# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from health import Calorie
from typing import Any, Text, Dict, List
#from rasa_core_sdk,
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:

        return "action_calorie"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        #min_cal = Calorie(food)[0]
        min_cal = int(Calorie(name)[1])
        max_cal = int(Calorie(name)[0])

        #maxi = tracker.get_slot("maxi")
        #mini = tracker.get_slot("mini")
        #print(max_cal)
        message = "You Choosen Food has minimium {0} calories  and Maximum {1} calories".format(min_cal,max_cal)
        #dispatcher.utter_template("utter_food_name",tracker,maxi=max_cal,mini=min_cal)
        dispatcher.utter_message(message)
        #return [SlotSet("maxi",max_cal),SlotSet("mini",min_cal)]
        return []