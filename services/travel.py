from .client.open_ia import OpenAIClient
from utils.prompts import Prompts


class Travel:
    def __init__(self, start_date, end_date, destination):
        self.start_date = start_date
        self.end_date = end_date
        self.destination = destination

    def plan(self):
        return self.travel_itinerary()

    def travel_itinerary(self):
        prompt = Prompts().itinerary_text(self.destination, self.start_date, self.end_date)
        openai = OpenAIClient()
        response = openai.question(prompt)
        return response.choices[0].message.content
