from typing import Any, Text, Dict, List

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker


from .constants import PIZZAS, DRINKS, PRICE_TABLES


class ActionListPizza(Action):
    def name(self) -> Text:
        return "action_list_pizza"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        message = "Temos disponíveis as pizzas:" + "\n- ".join(PIZZAS)
        dispatcher.utter_message(text=message)

        return []


class ActionListDrink(Action):
    def name(self) -> Text:
        return "action_list_drink"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        message = "Temos disponíveis as seguintes bebidas: " + "\n- ".join(DRINKS)
        dispatcher.utter_message(text=message)

        return []


class ActionListMenu(Action):
    def name(self) -> Text:
        return "action_list_menu"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        message = "Temos disponíveis as pizzas de " + "\n" + "\n- ".join(PIZZAS) + "\n"
        message += "\nE as seguintes bebidas: " + "\n- ".join(DRINKS)
        dispatcher.utter_message(text=message)

        return []


class ActionShowTotal(Action):
    def name(self) -> Text:
        return "action_show_total"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        message = ""

        total = 0
        for key in ("pizza", "drink"):
            item = tracker.get_slot(key)

            if not item:
                continue

            item = item.lower()

            value = PRICE_TABLES.get(item, 15)

            message += f"{item} = R$ {value},00\n"
            total += value

        message += f"Total = R$ {total},00"

        dispatcher.utter_message(text=message)

        return []
