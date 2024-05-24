from crewai import Crew
from textwrap import dedent
from agents import RoadmapAgents
from tasks import RoadmapTasks

from dotenv import load_dotenv
load_dotenv()

'''

    client_name = "Big Island, Hawaii"
    requirements = ["Honolulu"]
    date_range = ["2024-12-01", "2024-12-10"]
    motivations = ["Hiking", "Beach", "Cultural"]
    roadmap_crew = RoadmapCrew(client_name, requirements, date_range, motivations)
'''


class RoadmapCrew:
    def __init__(self, client_name, requirements, date_range, motivations):
        self.client_name = client_name
        self.requirements = requirements
        self.date_range = date_range
        self.motivations = motivations


    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = RoadmapAgents()
        tasks = RoadmapTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.requirements,
            self.date_range,
            self.motivations
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.client_name,
            self.requirements,
            self.motivations,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.requirements,
            self.date_range,
            self.motivations
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent,
                    city_selection_expert,
                    local_tour_guide
                    ],
            tasks=[
                plan_itinerary,
                identify_city,
                gather_city_info
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result



if __name__ == "__main__":

    """
    # This is the main function that you will use to run your custom crew.
    # To run your crew, you can use the following commands:
    # 1. poetry shell
    # 2. python main.py
    #
    # 3. Or you can use the following command to run the crew directly:
    #    poetry run python main.py
    """
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')

    '''
    origin = input(
        dedent("""
      From where will you be traveling from?
    """))
    cities = input(
        dedent("""
      What are the cities options you are interested in visiting?
    """))
    date_range = input(
        dedent("""
      What is the date range you are interested in traveling?
    """))
    interests = input(
        dedent("""
      What are some of your high level interests and hobbies?
    """))
    '''

    client_name = "Big Island, Hawaii"
    requirements = ["Honolulu"]
    date_range = ["2024-12-01", "2024-12-10"]
    motivations = ["Hiking", "Beach", "Cultural"]
    roadmap_crew = RoadmapCrew(client_name, requirements, date_range, motivations)
    result = roadmap_crew.run()
    print("\n\n########################")
    print("## Here is you Roadmap")
    print("########################\n")
    print(result)
