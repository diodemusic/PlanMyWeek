class Plan:
    def __init__(self, modules: list[str]) -> None:
        self.modules = modules
        self.lessons: list[dict[str, str]] = []
        self.week: dict[str, list[str]] = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
        }

    def __repr__(self) -> str:
        return f"Plan(modules={self.modules}, lessons={self.lessons}, week={self.week})"

    def _get_plan_list(self) -> None:
        for module in self.modules:
            lessons_amount: int = int(input(f"How many lessons do you have this week for {module}: "))
            lessons_num: int = int(input(f"What's the lesson number for {module}? "))

            for i in range(lessons_amount):
                self.lessons.append({module: f"Lesson {lessons_num}"})

    def _get_week(self) -> None:
        j = 0

        for i in range(len(self.lessons)):
            if j > 4:
                j = 0

            self.week[list(self.week.keys())[j]].append(self.lessons[i])

            j += 1

    def main(self):
        self._get_plan_list()
        self._get_week()

def main():
    plan: Plan = Plan(modules=["ITP1", "CM"])
    plan.main()
    print(plan.week)

if __name__ == "__main__":
    main()

# week: int = 8 # int(input("What week is it? "))
# self.markdown += f"# Weekly Plan - Week {week}\n\n"
