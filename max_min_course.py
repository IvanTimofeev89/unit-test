courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]

durations = [14, 20, 12, 20]


def get_min_max_course(courses: list, durations: list) -> str:
    courses_list = []

    for course, duration in zip(courses, durations):
        course_dict = {"title": course, "duration": duration}
        courses_list.append(course_dict)

    maxes = []
    minis = []
    for id, duration in enumerate(durations):
        if duration == max(durations):
            maxes.append(id)
        elif duration == min(durations):
            minis.append(id)

    courses_max = [x["title"] for id, x in enumerate(courses_list) if id in maxes]
    courses_min = [x["title"] for id, x in enumerate(courses_list) if id in minis]

    return f'Самый короткий курс(ы): {", ".join(courses_min)} - {min(durations)} месяца(ев) \n' \
           f'Самый длинный курс(ы): {", ".join(courses_max)} - {max(durations)} месяца(ев)'


if __name__ == "__main__":
    print(get_min_max_course(courses, durations))
