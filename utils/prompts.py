class Prompts:
    def itinerary_text(self, destination, start_date, end_date):
        return f"""
        Estou viajando para {destination} entre os dias {start_date} e {end_date}. 
        Me sugira um roteiro de viagem para cada dia em que estarei viajando.
        """
