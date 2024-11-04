import random

from app.customs.image import CustomImage


def random_decorations_budaya():
    images = [
        CustomImage(
            source="assets/img/quest/decorations/1.png",
            pos_hint={"x": 0.4, "center_y": 0.14},
        ),
        CustomImage(
            source="assets/img/quest/decorations/2.png",
            pos_hint={"x": 0.4, "center_y": 0.14},
        ),
        CustomImage(
            source="assets/img/quest/decorations/3.png",
            pos_hint={"x": 0.4, "center_y": 0.18},
        ),
        CustomImage(
            source="assets/img/quest/decorations/4.png",
            pos_hint={"x": 0.4, "center_y": 0.16},
        ),
        CustomImage(
            source="assets/img/quest/decorations/5.png",
            pos_hint={"x": 0.68, "center_y": 0.16},
        ),
    ]

    return random.choice(images)


def random_decorations_kemerdekaan():
    images = [
        CustomImage(
            source="assets/img/quest/decorations/6.png",
            pos_hint={"x": 0.4, "center_y": 0.14},
        ),
        CustomImage(
            source="assets/img/quest/decorations/7.png",
            pos_hint={"x": 0.4, "center_y": 0.14},
        ),
        CustomImage(
            source="assets/img/quest/decorations/8.png",
            pos_hint={"x": 0.4, "center_y": 0.14},
        ),
    ]

    return random.choice(images)
