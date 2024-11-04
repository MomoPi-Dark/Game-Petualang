from app.layouts.layout_quest_new import LayoutScreen

questions_data = [
    {
        "question": "",
        "answer": "a",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/kebangsaan/q1/a.png",
        "btn_b_src": "assets/img/quest/ceria/kebangsaan/q1/b.png",
        "btn_c_src": "assets/img/quest/ceria/kebangsaan/q1/c.png",
    },
    {
        "question": "",
        "answer": "b",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/kebangsaan/q2/a.png",
        "btn_b_src": "assets/img/quest/ceria/kebangsaan/q2/b.png",
        "btn_c_src": "assets/img/quest/ceria/kebangsaan/q2/c.png",
    },
    {
        "question": "",
        "answer": "c",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/kebangsaan/q3/a.png",
        "btn_b_src": "assets/img/quest/ceria/kebangsaan/q3/b.png",
        "btn_c_src": "assets/img/quest/ceria/kebangsaan/q3/c.png",
    },
    {
        "question": "",
        "answer": "a",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/kebangsaan/q4/a.png",
        "btn_b_src": "assets/img/quest/ceria/kebangsaan/q4/b.png",
        "btn_c_src": "assets/img/quest/ceria/kebangsaan/q4/c.png",
    },
    {
        "question": "",
        "answer": "b",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/kebangsaan/q5/a.png",
        "btn_b_src": "assets/img/quest/ceria/kebangsaan/q5/b.png",
        "btn_c_src": "assets/img/quest/ceria/kebangsaan/q5/c.png",
    },
]


class KebangsaanCeriaScreen(LayoutScreen):
    def __init__(self, app, **kw):
        super().__init__(
            app=app,
            color_wrong="blue",
            questions_data=questions_data,
            home_destination="lagu_kebangsaan",
            bar_timeout_src="assets/img/quest/bar_timeout/kebangsaan.png",
            timeout_duration=10.0,
            group_key_store="kebangsaan",
            key_store="ceria",
            **kw
        )
