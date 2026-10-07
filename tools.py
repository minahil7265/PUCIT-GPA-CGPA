from __future__ import annotations
import os
# ---------------------------------------------------------------------------
# 5.1 PUCIT grade 
# ---------------------------------------------------------------------------
GRADE_BANDS: list[tuple[int, str, float]] = [
    (85, "A", 4.0),
    (80, "A-", 3.7),
    (75, "B+", 3.3),
    (70, "B", 3.0),
    (65, "B-", 2.7),
    (61, "C+", 2.3),
    (58, "C", 2.0),
    (55, "C-", 1.7),
    (50, "D", 1.0),
    (0, "F", 0.0),
]

COURSES: dict[int, list[tuple[str, str, float]]] = {
    1: [
        ("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0),
    ],
    2: [
        ("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5),
    ],
    3: [
        ("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5),
    ],
    4: [
        ("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5),
    ],
    5: [
        ("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5),
    ],
    6: [
        ("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5),
    ],
    7: [
        ("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5),
    ],
    8: [
        ("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5),
    ],
}


def marks_to_grade_points(marks: int) -> float:
    """Convert marks (0-100) to grade points (0-4.0).
    
    Args:
        marks: Numeric marks from a single course (0-100).
    
    Returns:
        Grade point value (0.0-4.0).
    """
    if not isinstance(marks, (int, float)):
        return "Error: marks must be a number"
    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"
    for threshold, _letter, points in GRADE_BANDS:
        if marks >= threshold:
            return points
    return 0.0 


def calculate_semester_gpa(
    grade_points: list[float], credit_hours: list[float]
) -> float:
    """Calculate credit-weighted GPA for one semester.
    
    Args:
        grade_points: List of grade points (0.0-4.0) for each course.
        credit_hours: List of credit hours for each course.
    
    Returns:
        Semester GPA (0.0-4.0).
    """
    if not grade_points or not credit_hours:
        return "Error: grade_points and credit_hours must not be empty"
    if len(grade_points) != len(credit_hours):
        return "Error: grade_points and credit_hours must be the same length"
    if any(ch <= 0 for ch in credit_hours):
        return "Error: credit hours must be greater than 0"
    if any(gp < 0 or gp > 4.0 for gp in grade_points):
        return "Error: grade points must be between 0.0 and 4.0"

    total_quality_points = sum(gp * ch for gp, ch in zip(grade_points, credit_hours))
    total_credit_hours = sum(credit_hours)
    return round(total_quality_points / total_credit_hours, 2)


def calculate_new_cgpa(
    current_cgpa: float,
    completed_credit_hours: float,
    semester_gpa: float,
    semester_credit_hours: float,
) -> float:
    """Project new CGPA after adding a semester's result.
    
    Args:
        current_cgpa: Current CGPA (0.0-4.0).
        completed_credit_hours: Total credit hours completed so far.
        semester_gpa: GPA for this semester (0.0-4.0).
        semester_credit_hours: Total credit hours this semester.
    
    Returns:
        New CGPA (0.0-4.0).
    """
    if current_cgpa < 0 or current_cgpa > 4.0:
        return "Error: current_cgpa must be between 0.0 and 4.0"
    if semester_gpa < 0 or semester_gpa > 4.0:
        return "Error: semester_gpa must be between 0.0 and 4.0"
    if completed_credit_hours < 0:
        return "Error: completed_credit_hours cannot be negative"
    if semester_credit_hours <= 0:
        return "Error: semester_credit_hours must be greater than 0"

    numerator = (
        current_cgpa * completed_credit_hours
        + semester_gpa * semester_credit_hours
    )
    denominator = completed_credit_hours + semester_credit_hours
    return round(numerator / denominator, 2)


def required_gpa_for_target(
    target_cgpa: float,
    current_cgpa: float,
    completed_credit_hours: float,
    remaining_credit_hours: float,
) -> float:
    """Calculate GPA needed to reach a target CGPA.
    
    Args:
        target_cgpa: Desired final CGPA (0.0-4.0).
        current_cgpa: Current CGPA (0.0-4.0).
        completed_credit_hours: Credit hours already completed.
        remaining_credit_hours: Credit hours left to complete.
    
    Returns:
        Required GPA over remaining credit hours (may exceed 4.0 if impossible).
    """
    if target_cgpa < 0 or target_cgpa > 4.0:
        return "Error: target_cgpa must be between 0.0 and 4.0"
    if current_cgpa < 0 or current_cgpa > 4.0:
        return "Error: current_cgpa must be between 0.0 and 4.0"
    if completed_credit_hours < 0:
        return "Error: completed_credit_hours cannot be negative"
    if remaining_credit_hours <= 0:
        return "Error: remaining_credit_hours must be greater than 0"

    total_ch = completed_credit_hours + remaining_credit_hours
    numerator = target_cgpa * total_ch - current_cgpa * completed_credit_hours
    return round(numerator / remaining_credit_hours, 2)


def get_semester_courses(semester: int) -> str:
    """Get official courses and credit hours for a semester.
    
    Args:
        semester: Semester number (1-8).
    
    Returns:
        Formatted string listing courses and total credit hours.
    """
    if not isinstance(semester, int):
        return "Error: semester must be an integer"
    if semester < 1 or semester > 8:
        return "Error: semester must be between 1 and 8"

    courses = COURSES[semester]
    lines = [f"Semester {semester} courses:"]
    total = 0.0
    for code, name, ch in courses:
        lines.append(f"  {code} - {name} ({ch} ch)")
        total += ch
    lines.append(f"Total credit hours: {total}")
    return "\n".join(lines)


def get_remaining_credit_hours(current_semester: int) -> float:
    """Get total graded credit hours remaining after current semester.
    
    Args:
        current_semester: Current semester number (1-8).
    
    Returns:
        Total credit hours in all remaining semesters.
    """
    if not isinstance(current_semester, int):
        return "Error: current_semester must be an integer"
    if current_semester < 1 or current_semester > 8:
        return "Error: current_semester must be between 1 and 8"

    total = 0.0
    for sem in range(current_semester + 1, 9):
        total += sum(ch for _code, _name, ch in COURSES[sem])
    return total


def save_report(filename: str, content: str) -> str:
    """Save a calculation report to a text file.
    
    Args:
        filename: Name for the report file.
        content: Full content to save in the report.
    
    Returns:
        Confirmation message or error string.
    """
    if not filename or not filename.strip():
        return "Error: filename must not be empty"
    if not content or not content.strip():
        return "Error: content must not be empty"

    safe_name = os.path.basename(filename.strip())
    if not safe_name.lower().endswith(".txt"):
        safe_name += ".txt"

    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    path = os.path.join(reports_dir, safe_name)

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except OSError as exc:
        return f"Error: could not save report ({exc})"

    return f"Report saved as {safe_name}"