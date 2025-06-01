class Plan:
    def __init__(self, modules: list[str]) -> None:
        self.modules = modules

    def __repr__(self) -> str:
        return f"Plan(modules={self.modules}, week={self.week})"

    def get_lessons(self) -> list[dict[str, str]]:
        lessons: list[dict[str, str]] = []

        for module in self.modules:
            try:
                lessons_amount: int = int(input(f"How many lessons do you have this week for {module}: "))
            except:
                print("error")
                quit()

            try:
                first_lesson: str = input("Please enter the name of the first lesson in the following format: \"4.4\": ").split(".")
                topic_num: int = int(first_lesson[0])
                lessons_decimal_num: int = int(first_lesson[1])
            except:
                print("error")
                quit()

            for i in range(lessons_amount):
                lessons.append({module: f"Lesson {topic_num}.{lessons_decimal_num + i}"})

        return lessons

    def get_week(self, lessons: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
        week: dict[str, list[dict[str, str]]] = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }

        days = list(week.keys())

        for idx, lesson in enumerate(lessons):
            day = days[idx % len(days)]
            week[day].append(lesson)

        return week

    def get_markdown(self, week: dict[str, list[dict[str, str]]]) -> str:
        markdown: str = ""

        module_week: int = int(input("What week is it? "))
        markdown += f"# Weekly Plan - Week {module_week}\n\n"

        for day, lessons in week.items():
            markdown += f"## {day}\n\n"

            if not lessons:
                markdown += f"- No tasks scheduled.\n"

            for lesson in lessons:
                markdown += f"- [ ] {list(lesson.keys())[0]} {list(lesson.values())[0]}\n"

            markdown += "\n"

        return markdown[:-1]

    # def save_markdown(self, markdown: str, path: str) -> None:
    #     with open(path, "w") as f:
    #         f.write(markdown)
