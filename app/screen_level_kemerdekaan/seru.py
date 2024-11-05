from app.layouts.layout_quest_new import LayoutScreen

questions_data = [
    {
        "bg_sound": "assets/music/kebangsaan/question/dari_sabang_sampai_merauke.mp3",
        "question": "assets/img/quest/_seru/kebangsaan/q1/quest.png",
        "decoration": [],
        "answer": "b",
        "btn_a_src": "assets/img/quest/_seru/kebangsaan/q1/a.png",
        "btn_b_src": "assets/img/quest/_seru/kebangsaan/q1/b.png",
        "btn_c_src": "assets/img/quest/_seru/kebangsaan/q1/c.png",
    },
    {
        "bg_sound": "assets/music/kebangsaan/question/halo_halo_bandung.mp3",
        "question": "assets/img/quest/_seru/kebangsaan/q2/quest.png",
        "decoration": [],
        "answer": "a",
        "btn_a_src": "assets/img/quest/_seru/kebangsaan/q2/a.png",
        "btn_b_src": "assets/img/quest/_seru/kebangsaan/q2/b.png",
        "btn_c_src": "assets/img/quest/_seru/kebangsaan/q2/c.png",
    },
    {
        "bg_sound": "assets/music/kebangsaan/question/17_agustus.mp3",
        "question": "assets/img/quest/_seru/kebangsaan/q3/quest.png",
        "decoration": [],
        "answer": "b",
        "btn_a_src": "assets/img/quest/_seru/kebangsaan/q3/a.png",
        "btn_b_src": "assets/img/quest/_seru/kebangsaan/q3/b.png",
        "btn_c_src": "assets/img/quest/_seru/kebangsaan/q3/c.png",
    },
    {
        "decoration": [],
        "answer": "a",
        "bg_sound": "assets/music/kebangsaan/question/satu_nusa_satu_bangsa.mp3",
        "question": "assets/img/quest/_seru/kebangsaan/q4/quest.png",
        "btn_a_src": "assets/img/quest/_seru/kebangsaan/q4/a.png",
        "btn_b_src": "assets/img/quest/_seru/kebangsaan/q4/b.png",
        "btn_c_src": "assets/img/quest/_seru/kebangsaan/q4/c.png",
    },
    {
        "bg_sound": "assets/music/kebangsaan/question/bagimu_negeri.mp3",
        "question": "assets/img/quest/_seru/kebangsaan/q5/quest.png",
        "decoration": [],
        "answer": "b",
        "btn_a_src": "assets/img/quest/_seru/kebangsaan/q5/a.png",
        "btn_b_src": "assets/img/quest/_seru/kebangsaan/q5/b.png",
        "btn_c_src": "assets/img/quest/_seru/kebangsaan/q5/c.png",
    },
]


class KebangsaanSeruScreen(LayoutScreen):
    def __init__(self, app, **kw):
        super().__init__(
            app=app,
            questions_data=questions_data,
            home_destination="lagu_kebangsaan",
            bar_timeout_src="assets/img/quest/bar_timeout/kebangsaan.png",
            timeout_duration=40.0,
            group_key_store="kebangsaan",
            key_store="seru",
            **kw
        )
