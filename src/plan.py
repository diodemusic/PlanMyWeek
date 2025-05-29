# TODO: add week header to MD
# week: int = 8 # int(input("What week is it? "))
# self.markdown += f"# Weekly Plan - Week {week}\n\n"

class Plan:
    def __init__(self, modules: list[str]) -> None:
        self.modules = modules

    def __repr__(self) -> str:
        return f"Plan(modules={self.modules}, week={self.week})"

    def get_lessons(self) -> list[dict[str, str]]:
        lessons: list[dict[str, str]] = []

        for module in self.modules:
            lessons_amount: int = 3 # int(input(f"How many lessons do you have this week for {module}: "))
            lessons_num: int = 4 # int(input(f"What's the lesson number for {module}? "))

            for i in range(lessons_amount):
                lessons.append({module: f"Lesson {lessons_num}.{i + 1}"})

        return lessons

    def get_week(self, lessons: list[dict[str, str]]) -> dict[str, list[str]]:
        week: dict[str, list[str]] = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
        }

        days = list(week.keys())

        for i in range(len(days)):
            if list(lessons[i].keys())[0] == self.modules[0]:
                week[days[i]].append(lessons[i])

        for i in reversed(range(len(days))):
            if list(lessons[i + 1].keys())[0] == self.modules[1]:
                week[days[i]].append(lessons[i + 1])

        return week
