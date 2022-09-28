from docarray import dataclass, Document
from docarray.typing import Image, Text, JSON


@dataclass
class WPArticle:
    banner: Image
    headline: Text
    meta: JSON


a = WPArticle(
    banner='https://.../cat-dog-flight.png',
    headline='Everything to know about flying with pets, ...',
    meta={
        'author': 'Nathan Diller',
        'Column': 'By the Way - A Post Travel Destination',
    },
)

d = Document(a)
print(d)
breakpoint()