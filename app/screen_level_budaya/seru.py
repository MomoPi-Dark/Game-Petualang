from app.layouts.layout_quest_new import LayoutScreen

questions_data = [
    {
        "font_content_size": 15,
        "bg_sound": "assets/music/budaya/question/ampar_ampar_pisang.mp3",
        "decorations": [],
        "descriptions": [
            "Pisangku belum masak",
            "Masak sedikit, dihurung bari-bari",
            "Masak sedikit, dihurung bari-bari",
            "Mangga lepak mangga lepok",
            "Patah kayu bengkok",
            "Bengkok dimakan api",
            "Apinya canculupan",
        ],
        "answer": "a",
        "btn_a_src": "assets/img/quest/seru/budaya/q1/a.png",
        "btn_b_src": "assets/img/quest/seru/budaya/q1/b.png",
        "btn_c_src": "assets/img/quest/seru/budaya/q1/c.png",
    },
    {
        "font_content_size": "16sp",
        "bg_sound": "assets/music/budaya/question/yamko_rambe_yamko.mp3",
        "decorations": [],
        "descriptions": [
            "Hee yamko rambe yamko aronawa kombe",
            "Hee yamko rambe yamko aronawa kombe",
            "Hongke hongke hongke riro",
            "Hongke jombe jombe riro",
            "Hongke hongke hongke riro",
            "Hongke jombe jombe riro",
        ],
        "answer": "b",
        "btn_a_src": "assets/img/quest/seru/budaya/q2/a.png",
        "btn_b_src": "assets/img/quest/seru/budaya/q2/b.png",
        "btn_c_src": "assets/img/quest/seru/budaya/q2/c.png",
    },
    {
        "font_content_size": "16sp",
        "bg_sound": "assets/music/budaya/question/rasa_sayange.mp3",
        "decorations": [],
        "descriptions": [
            "Rasa sayange.. rasa sayang sayange..",
            "Lihat nona dari jauh rasa sayang sayange",
            "Rasa sayange.. rasa sayang sayange..",
            "Lihat nona dari jauh rasa sayang sayange",
        ],
        "answer": "a",
        "btn_a_src": "assets/img/quest/seru/budaya/q3/a.png",
        "btn_b_src": "assets/img/quest/seru/budaya/q3/b.png",
        "btn_c_src": "assets/img/quest/seru/budaya/q3/c.png",
    },
    {
        "font_content_size": "24sp",
        "bg_sound": "assets/music/budaya/question/gundul_pacul.mp3",
        "decorations": [],
        "descriptions": [
            "Gundul gundul pacul,",
            "cul gembelengan...",
            "Nyunggi nyunggi wakul...",
        ],
        "answer": "b",
        "btn_a_src": "assets/img/quest/seru/budaya/q4/a.png",
        "btn_b_src": "assets/img/quest/seru/budaya/q4/b.png",
        "btn_c_src": "assets/img/quest/seru/budaya/q4/c.png",
    },
    {
        "font_content_size": "24sp",
        "bg_sound": "assets/music/budaya/question/cublak_cublak_suweng.mp3",
        "decorations": [],
        "descriptions": [
            "Cublak-cublak suweng,",
            "suwenge teng gelenter",
            "Mambu ketundhung gudel...",
        ],
        "answer": "c",
        "btn_a_src": "assets/img/quest/seru/budaya/q5/a.png",
        "btn_b_src": "assets/img/quest/seru/budaya/q5/b.png",
        "btn_c_src": "assets/img/quest/seru/budaya/q5/c.png",
    },
]


class BudayaSeruScreen(LayoutScreen):
    def __init__(self, app, **kw):
        super().__init__(
            app=app,
            color_wrong="red",
            questions_data=questions_data,
            home_destination="lagu_budaya",
            bar_timeout_src="assets/img/quest/bar_timeout/budaya.png",
            bg_lyric_src="assets/img/quest/bg_description/budaya.png",
            timeout_duration=40.0,
            group_key_store="budaya",
            key_store="seru",
            **kw
        )
