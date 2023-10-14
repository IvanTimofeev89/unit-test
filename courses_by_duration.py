courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]

durations = [14, 20, 12, 20]


def sort_by_duration(courses: list, durations: list) -> list:
    courses_list = []
    for course, duration in zip(courses, durations):
        course_dict = {"title": course, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = course["duration"]
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)

    durations_dict = dict(sorted(durations_dict.items()))

    result_list = []
    for duration, ids in durations_dict.items():
        for id in ids:
            result_list.append(f'{courses_list[id]["title"]} - {duration} месяцев')
    return result_list


if __name__ == '__main__':
    print(sort_by_duration(courses, durations))
