from plan import Plan

def main():
    plan: Plan = Plan(modules=["ITP1", "CM"])

    lessons = plan.get_lessons()
    week = plan.get_week(lessons=lessons)

    print(week)

if __name__ == "__main__":
    main()
