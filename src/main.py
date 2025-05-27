def build_week() -> dict[str, list[tuple[str, int]]]:
    """
    Prompt the user for the number of tasks per module, their names, and durations in minutes.
    Returns:
        plan: A dict mapping module names to a list of (task name, duration) tuples.
    """
    modules = ["ITP1", "CM"]
    plan: dict[str, list[tuple[str, int]]] = {module: [] for module in modules}

    for module in modules:
        try:
            tasks_amount = int(
                input(f"How many tasks do you have this week for {module}: ")
            )
        except ValueError:
            print("Please enter a valid integer for the number of tasks.")
            return {}

        for i in range(tasks_amount):
            task_name = input(f"Enter a name for task {i + 1} in {module}: ")
            while True:
                duration = input(f"How long is '{task_name}' in minutes for {module}: ")
                if duration.isdigit():
                    plan[module].append((task_name, int(duration)))
                    break
                else:
                    print("Please enter the duration as a number in minutes.")

    return plan


def parse_markdown(plan: dict[str, list[tuple[str, int]]]) -> str:
    """
    Takes a plan dict (module -> list of (name, duration)) and returns a Markdown-formatted weekly schedule.
    For each module, divides total duration by 5 days to get a daily target,
    then assigns tasks sequentially, filling each day until the target is met before moving on.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Initialize schedule: day -> module -> list of (task_name, duration)
    schedule: dict[str, dict[str, list[tuple[str, int]]]] = {
        day: {module: [] for module in plan.keys()} for day in days
    }

    # For each module, compute daily target and assign tasks in order
    for module, tasks in plan.items():
        total = sum(duration for _, duration in tasks)
        target = total / len(days) if days else total
        day_idx = 0
        accumulated = 0

        for task_name, dur in tasks:
            if accumulated >= target and day_idx < len(days) - 1:
                day_idx += 1
                accumulated = 0

            day = days[day_idx]
            schedule[day][module].append((task_name, dur))
            accumulated += dur

    # Build Markdown output
    week = int(input("What week are you on? "))

    md_lines: list[str] = [f"# Weekly Plan - Week {week}", ""]
    for day in days:
        md_lines.append(f"## {day}")
        md_lines.append("")

        day_data = schedule[day]
        any_tasks = any(day_data[module] for module in plan.keys())
        if not any_tasks:
            md_lines.append("- No tasks scheduled.")
            md_lines.append("")
            continue

        for module in plan.keys():
            tasks = day_data[module]
            if tasks:
                md_lines.append(f"**{module}:**")
                md_lines.append("")
                for name, dur in tasks:
                    md_lines.append(f"- [ ] {name}: {dur} mins")
                md_lines.append("")

    return "\n".join(md_lines)


def main():
    plan = build_week()
    if not plan:
        return
    markdown = parse_markdown(plan)

    # Save to markdown file
    output_file = "weekly_plan.md"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Weekly plan saved to {output_file}")
    except IOError as e:
        print(f"Error saving file {output_file}: {e}")

    # Also print to console
    print(markdown)


if __name__ == "__main__":
    main()
