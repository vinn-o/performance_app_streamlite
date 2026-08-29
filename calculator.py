def calculate_performance(assignment, study_time, attendance):
    score = (
        (attendance/100) *30 +
        (study_time/10) *30 +
        (assignment /100) * 40
    )
    return round(score, 2)


def get_results(score):
    if score >=50:
        return "PASS"
    else:
        return "IMPROVE"
    