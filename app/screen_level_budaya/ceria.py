from app.layouts.layout_quest_new import LayoutScreen

questions_data = [
    {
        "font_content_size": 20,
        "descriptions": [
            "Lagu Ampar-Ampar Pisang",
            "berasal dari daerah mana?",
        ],
        "answer": "b",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/budaya/q1/a.png",  # Jakarta
        "btn_b_src": "assets/img/quest/ceria/budaya/q1/b.png",  # Kalimantan Selatan
        "btn_c_src": "assets/img/quest/ceria/budaya/q1/c.png",  # Jawa Barat
    },
    {
        "font_content_size": 20,
        "descriptions": [
            "Lagu Anak Kambing Saya",
            "Apa yang dicari dalam",
            " lagu Anak Kambing Saya?",
        ],
        "answer": "b",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/budaya/q2/a.png",  # Anak sapi
        "btn_b_src": "assets/img/quest/ceria/budaya/q2/b.png",  # Anak kambing
        "btn_c_src": "assets/img/quest/ceria/budaya/q2/c.png",  # Anak ayam
    },
    {
        "font_content_size": 18,
        "descriptions": [
            "Lagu Cublak-Cublak Suweng",
            "siapa yang bersembunyi?",
        ],
        "answer": "c",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/budaya/q3/a.png",  # Ayam
        "btn_b_src": "assets/img/quest/ceria/budaya/q3/b.png",  # Anak-anak
        "btn_c_src": "assets/img/quest/ceria/budaya/q3/c.png",  # Suweng
    },
    {
        "font_content_size": 20,
        "descriptions": [
            "Lagu Gundul-Gundul Pacul",
            "biasanya dinyanyikan",
            " sambil bermain apa?",
        ],
        "answer": "c",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/budaya/q4/a.png",  # Petak umpet
        "btn_b_src": "assets/img/quest/ceria/budaya/q4/b.png",  # Lompat tali
        "btn_c_src": "assets/img/quest/ceria/budaya/q4/c.png",  # Permainan tradisional
    },
    {
        "font_content_size": 24,
        "descriptions": [
            "Lagu Jali-Jali",
            "terkenal dari mana?",
        ],
        "answer": "b",
        "decorations": [],
        "btn_a_src": "assets/img/quest/ceria/budaya/q5/a.png",  # Sumatera
        "btn_b_src": "assets/img/quest/ceria/budaya/q5/b.png",  # Jakarta
        "btn_c_src": "assets/img/quest/ceria/budaya/q5/c.png",  # Papua
    },
]


class BudayaCeriaScreen(LayoutScreen):
    def __init__(self, app, **kw):
        super().__init__(
            app=app,
            color_wrong="red",
            questions_data=questions_data,
            home_destination="lagu_budaya",
            bar_timeout_src="assets/img/quest/bar_timeout/budaya.png",
            bg_lyric_src="assets/img/quest/bg_description/budaya.png",
            timeout_duration=10.0,
            group_key_store="daerah",
            key_store="ceria",
            **kw
        )
