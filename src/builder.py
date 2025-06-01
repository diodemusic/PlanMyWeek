from src.plan import Plan

def build() -> str:
    plan: Plan = Plan(modules=["ITP1", "CM"])
    # path: str = "../plan/weekly_plan.md"

    lessons = plan.get_lessons()
    week = plan.get_week(lessons=lessons)
    markdown = plan.get_markdown(week=week)

    # plan.save_markdown(markdown=markdown, path=path)

    # print(f"saved to: {path}")

    return markdown
