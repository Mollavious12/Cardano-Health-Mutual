import reflex as rx
from typing import TypedDict


class Course(TypedDict):
    id: str
    title: str
    category: str
    description: str
    image_url: str
    progress: int
    completed: bool


class LearningHubState(rx.State):
    """State for the Learning Hub."""

    courses: list[Course] = [
        {
            "id": "preventive-health-101",
            "title": "Preventive Health 101",
            "category": "Preventive Health",
            "description": "Learn the basics of staying healthy and preventing common illnesses.",
            "image_url": "/placeholder.svg",
            "progress": 65,
            "completed": False,
        },
        {
            "id": "nutrition-fundamentals",
            "title": "Nutrition Fundamentals",
            "category": "Nutrition",
            "description": "Understand the core principles of a balanced and healthy diet.",
            "image_url": "/placeholder.svg",
            "progress": 30,
            "completed": False,
        },
        {
            "id": "mental-wellness-basics",
            "title": "Mental Wellness Basics",
            "category": "Mental Health",
            "description": "An introduction to mental health and well-being strategies.",
            "image_url": "/placeholder.svg",
            "progress": 0,
            "completed": False,
        },
        {
            "id": "financial-literacy-for-health",
            "title": "Financial Literacy for Health",
            "category": "Financial Literacy",
            "description": "Learn how to manage your finances to support your health goals.",
            "image_url": "/placeholder.svg",
            "progress": 90,
            "completed": False,
        },
    ]

    @rx.var
    def categories(self) -> list[str]:
        return sorted(list(set((course["category"] for course in self.courses))))

    @rx.var
    def completed_courses(self) -> int:
        return sum((1 for course in self.courses if course["completed"]))

    @rx.event
    def update_course_progress(self, course_id: str, new_progress: int):
        for i, course in enumerate(self.courses):
            if course["id"] == course_id:
                self.courses[i]["progress"] = new_progress
                if new_progress >= 100:
                    self.courses[i]["completed"] = True
                return

    @rx.event
    def mark_course_complete(self, course_id: str):
        for i, course in enumerate(self.courses):
            if course["id"] == course_id:
                self.courses[i]["progress"] = 100
                self.courses[i]["completed"] = True
                return