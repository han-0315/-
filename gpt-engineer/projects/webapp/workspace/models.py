from dataclasses import dataclass

@dataclass
class BlogPost:
    title: str
    content: str
    author: str
    date: str

@dataclass
class ContactFormSubmission:
    name: str
    email: str
    message: str
