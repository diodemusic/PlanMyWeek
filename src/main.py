def build_week() -> dict[str, list[int]]:
    """
    Prompt the user for the number of tasks per module and their durations in minutes.
    Returns:
        plan: A dict mapping module names to a list of task durations.
    """
    modules = ["CM", "ITP1"]
    plan: dict[str, list[int]] = {module: [] for module in modules}

    for module in modules:
        try:
            tasks_amount = int(
                input(f"How many tasks do you have this week for {module}: ")
            )
        except ValueError:
            print("Please enter a valid integer for the number of tasks.")
            return {}

        for i in range(tasks_amount):
            while True:
                duration = input(f"How long is task {i + 1} in minutes for {module}: ")
                if duration.isdigit():
                    plan[module].append(int(duration))
                    break
                else:
                    print("Please enter the duration as a number in minutes.")

    return plan


def parse_markdown(plan: dict[str, list[int]]) -> str:
    """
    Takes a plan dict (module -> list of durations) and returns a Markdown-formatted weekly schedule.
    For each module, divides total duration by 5 days to get a daily target,
    then assigns tasks sequentially, filling each day until the target is met before moving on.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Initialize schedule: day -> module -> list of (task_index, duration)
    schedule: dict[str, dict[str, list[tuple[int, int]]]] = {
        day: {module: [] for module in plan.keys()} for day in days
    }

    # For each module, compute daily target and assign tasks in order
    for module, durations in plan.items():
        total = sum(durations)
        target = total / len(days) if days else total
        day_idx = 0
        accumulated = 0

        for idx, dur in enumerate(durations):
            # If adding this task exceeds the target and we have days left, move to next day
            if accumulated >= target and day_idx < len(days) - 1:
                day_idx += 1
                accumulated = 0

            task_index = idx + 1
            day = days[day_idx]
            schedule[day][module].append((task_index, dur))
            accumulated += dur

    # Build Markdown output
    md_lines: list[str] = ["# Weekly Plan", ""]
    for day in days:
        md_lines.append(f"## {day}")
        md_lines.append("")

        day_data = schedule[day]
        any_tasks = any(day_data[module] for module in plan.keys())
        if not any_tasks:
            md_lines.append("- No tasks scheduled.")
            md_lines.append("")
            continue

        # Print each module's tasks in order
        for module in plan.keys():
            tasks = day_data[module]
            if tasks:
                md_lines.append(f"**{module}:**")
                md_lines.append("")
                for task_idx, dur in tasks:
                    md_lines.append(f"- [ ] Task {task_idx}. {dur} mins")
                md_lines.append("")

    return "\n".join(md_lines)


def main():
    plan = build_week()
    if not plan:
        return
    markdown = parse_markdown(plan)
    print(markdown)


if __name__ == "__main__":
    main()
