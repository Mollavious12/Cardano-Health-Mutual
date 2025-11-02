import reflex as rx
from typing import TypedDict, Optional
from app.states.learning_hub_state import LearningHubState


class Lesson(TypedDict):
    id: str
    title: str
    type: str
    content: str
    completed: bool


class CourseDetail(TypedDict):
    id: str
    title: str
    description: str
    image_url: str
    lessons: list[Lesson]


MOCK_COURSES = {
    "preventive-health-101": {
        "id": "preventive-health-101",
        "title": "Preventive Health 101",
        "description": "Learn the basics of staying healthy and preventing common illnesses.",
        "image_url": "/placeholder.svg",
        "lessons": [
            {
                "id": "l1",
                "title": "Introduction to Preventive Health",
                "type": "article",
                "content": "Preventive health is the practice of promoting health and well-being...",
                "completed": False,
            },
            {
                "id": "l2",
                "title": "Understanding Vaccinations",
                "type": "video",
                "content": "https://www.youtube.com/embed/SVuN-l-H4wA",
                "completed": False,
            },
        ],
    },
    "nutrition-fundamentals": {
        "id": "nutrition-fundamentals",
        "title": "Nutrition Fundamentals",
        "description": "Understand the core principles of a balanced and healthy diet.",
        "image_url": "/placeholder.svg",
        "lessons": [],
    },
    "mental-wellness-basics": {
        "id": "mental-wellness-basics",
        "title": "Mental Wellness Basics",
        "description": "An introduction to mental health and well-being strategies.",
        "image_url": "/placeholder.svg",
        "lessons": [],
    },
    "financial-literacy-for-health": {
        "id": "financial-literacy-for-health",
        "title": "Financial Literacy for Health",
        "description": "Learn how to manage your finances to support your health goals.",
        "image_url": "/placeholder.svg",
        "lessons": [],
    },
}


class CourseState(LearningHubState):
    course: Optional[CourseDetail] = None
    is_loading: bool = False

    @rx.var
    def current_course_id(self) -> str:
        return self.router.page.params.get("course_id", "")

    @rx.event
    def get_course_details(self):
        self.is_loading = True
        course_id = self.current_course_id
        if course_id in MOCK_COURSES:
            self.course = MOCK_COURSES[course_id]
        else:
            self.course = None
        self.is_loading = False

    @rx.event
    def toggle_lesson_completion(self, lesson_id: str):
        if self.course:
            for i, lesson in enumerate(self.course["lessons"]):
                if lesson["id"] == lesson_id:
                    self.course["lessons"][i]["completed"] = not self.course["lessons"][
                        i
                    ]["completed"]