from app.layouts.layout_quest_new import LayoutScreen

questions_data = [
    {
        "question": "assets/img/quest/_seru/budaya/q1/quest.png",
        "bg_sound": "assets/music/budaya/question/ampar_ampar_pisang.mp3",
        "decorations": [],
        "answer": "a",
        "btn_a_src": "assets/img/quest/_seru/budaya/q1/a.png",
        "btn_b_src": "assets/img/quest/_seru/budaya/q1/b.png",
        "btn_c_src": "assets/img/quest/_seru/budaya/q1/c.png",
    },
    {
        "question": "assets/img/quest/_seru/budaya/q2/quest.png",
        "bg_sound": "assets/music/budaya/question/yamko_rambe_yamko.mp3",
        "decorations": [],
        "answer": "b",
        "btn_a_src": "assets/img/quest/_seru/budaya/q2/a.png",
        "btn_b_src": "assets/img/quest/_seru/budaya/q2/b.png",
        "btn_c_src": "assets/img/quest/_seru/budaya/q2/c.png",
    },
    {
        "question": "assets/img/quest/_seru/budaya/q3/quest.png",
        "bg_sound": "assets/music/budaya/question/rasa_sayange.mp3",
        "decorations": [],
        "answer": "a",
        "btn_a_src": "assets/img/quest/_seru/budaya/q3/a.png",
        "btn_b_src": "assets/img/quest/_seru/budaya/q3/b.png",
        "btn_c_src": "assets/img/quest/_seru/budaya/q3/c.png",
    },
    {
        "question": "assets/img/quest/_seru/budaya/q4/quest.png",
        "bg_sound": "assets/music/budaya/question/gundul_pacul.mp3",
        "decorations": [],
        "answer": "b",
        "btn_a_src": "assets/img/quest/_seru/budaya/q4/a.png",
        "btn_b_src": "assets/img/quest/_seru/budaya/q4/b.png",
        "btn_c_src": "assets/img/quest/_seru/budaya/q4/c.png",
    },
    {
        "question": "assets/img/quest/_seru/budaya/q5/quest.png",
        "bg_sound": "assets/music/budaya/question/cublak_cublak_suweng.mp3",
        "decorations": [],
        "answer": "c",
        "btn_a_src": "assets/img/quest/_seru/budaya/q5/a.png",
        "btn_b_src": "assets/img/quest/_seru/budaya/q5/b.png",
        "btn_c_src": "assets/img/quest/_seru/budaya/q5/c.png",
    },
]


class BudayaSeruScreen(LayoutScreen):
    def __init__(self, app, **kw):
        super().__init__(
            app=app,
            questions_data=questions_data,
            home_destination="lagu_budaya",
            bar_timeout_src="assets/img/quest/bar_timeout/budaya.png",
            timeout_duration=40.0,
            group_key_store="budaya",
            key_store="seru",
            **kw
        )
