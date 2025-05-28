class Plan:
    def __init__(self, modules: list[str]) -> None:
        self.modules = modules
        self.plan: dict[str, list[str]] = {}

    def __repr__(self) -> str:
        return f"Plan(modules={self.modules}, plan={self.plan})"

    def get_plan_list(self) -> None:
        for module in self.modules:
            lessons_amount = int(input(f"How many lessons do you have this week for {module}: "))
            lessons_num = int(input(f"What's the lesson number for {module}? "))

            self.plan[module] = [f"Lesson {lessons_num}.{i + 1}" for i in range(lessons_amount)]

def main():
    plan: Plan = Plan(modules=["ITP1", "CM"])

    plan.get_plan_list()

    print(plan.__repr__())

if __name__ == "__main__":
    main()
