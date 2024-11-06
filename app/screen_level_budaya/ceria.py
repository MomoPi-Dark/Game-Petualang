from app.layouts.layout_quest_new import LayoutScreen

questions_data = [
    {
        "question": "assets/img/quest/_ceria/budaya/q1/quest.png",
        "answer": "b",
        "decorations": [],
        "btn_a_src": "assets/img/quest/_ceria/budaya/q1/a.png",
        "btn_b_src": "assets/img/quest/_ceria/budaya/q1/b.png",
        "btn_c_src": "assets/img/quest/_ceria/budaya/q1/c.png",
    },
    {
        "question": "assets/img/quest/_ceria/budaya/q2/quest.png",
        "answer": "c",
        "decorations": [],
        "btn_a_src": "assets/img/quest/_ceria/budaya/q2/a.png",
        "btn_b_src": "assets/img/quest/_ceria/budaya/q2/b.png",
        "btn_c_src": "assets/img/quest/_ceria/budaya/q2/c.png",
    },
    {
        "question": "assets/img/quest/_ceria/budaya/q3/quest.png",
        "answer": "c",
        "decorations": [],
        "btn_a_src": "assets/img/quest/_ceria/budaya/q3/a.png",
        "btn_b_src": "assets/img/quest/_ceria/budaya/q3/b.png",
        "btn_c_src": "assets/img/quest/_ceria/budaya/q3/c.png",
    },
    {
        "question": "assets/img/quest/_ceria/budaya/q4/quest.png",
        "answer": "a",
        "decorations": [],
        "btn_a_src": "assets/img/quest/_ceria/budaya/q4/a.png",
        "btn_b_src": "assets/img/quest/_ceria/budaya/q4/b.png",
        "btn_c_src": "assets/img/quest/_ceria/budaya/q4/c.png",
    },
    {
        "question": "assets/img/quest/_ceria/budaya/q5/quest.png",
        "answer": "b",
        "decorations": [],
        "btn_a_src": "assets/img/quest/_ceria/budaya/q5/a.png",
        "btn_b_src": "assets/img/quest/_ceria/budaya/q5/b.png",
        "btn_c_src": "assets/img/quest/_ceria/budaya/q5/c.png",
    },
]


class BudayaCeriaScreen(LayoutScreen):
    def __init__(self, app, **kw):
        super().__init__(
            app=app,
            questions_data=questions_data,
            home_destination="lagu_budaya",
            bar_timeout_src="assets/img/quest/bar_timeout/budaya.png",
            timeout_duration=10.0,
            group_key_store="budaya",
            key_store="ceria",
            **kw
        )
