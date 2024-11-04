from app.layouts.layout_quest_new import LayoutScreen

questions_data = [
    {
        "font_content_size": "18sp",
        "bg_sound": "assets/music/kebangsaan/question/dari_sabang_sampai_merauke.mp3",
        "question": [
            "Sambung-menyambung menjadi satu",
            "Itulah Indonesia",
            "Indonesia tanah airku",
            "Aku berjanji padamu",
        ],
        "decoration": [],
        "answer": "b",
        "btn_a_src": "assets/img/quest/seru/kebangsaan/q1/a.png",
        "btn_b_src": "assets/img/quest/seru/kebangsaan/q1/b.png",
        "btn_c_src": "assets/img/quest/seru/kebangsaan/q1/c.png",
    },
    {
        "font_content_size": "18sp",
        "bg_sound": "assets/music/kebangsaan/question/halo_halo_bandung.mp3",
        "question": [
            "Sudah lama beta",
            "Tidak Berjumpa dengan kau",
            "Sekarang sudah menjadi lautan api",
            "Mari Bung rebut kembali",
        ],
        "decoration": [],
        "answer": "a",
        "btn_a_src": "assets/img/quest/seru/kebangsaan/q2/a.png",
        "btn_b_src": "assets/img/quest/seru/kebangsaan/q2/b.png",
        "btn_c_src": "assets/img/quest/seru/kebangsaan/q2/c.png",
    },
    {
        "font_content_size": "20sp",
        "bg_sound": "assets/music/kebangsaan/question/satu_nusa_satu_bangsa.mp3",
        "question": ["Tanah Air", "Pasti Jaya Untuk Slama-lamanya"],
        "decoration": [],
        "answer": "c",
        "btn_a_src": "assets/img/quest/seru/kebangsaan/q3/a.png",
        "btn_b_src": "assets/img/quest/seru/kebangsaan/q3/b.png",
        "btn_c_src": "assets/img/quest/seru/kebangsaan/q3/c.png",
    },
    {
        "font_content_size": "18sp",
        "bg_sound": "assets/music/kebangsaan/question/17_agustus.mp3",
        "question": [
            "Tujuh belas Agustus tahun empat lima",
            "Itulah hari kemerdekaan kita",
            "Hari merdeka nusa dan bangsa...",
        ],
        "decoration": [],
        "answer": "a",
        "btn_a_src": "assets/img/quest/seru/kebangsaan/q4/a.png",
        "btn_b_src": "assets/img/quest/seru/kebangsaan/q4/b.png",
        "btn_c_src": "assets/img/quest/seru/kebangsaan/q4/c.png",
    },
    {
        "font_content_size": "23sp",
        "bg_sound": "assets/music/kebangsaan/question/bagimu_negeri.mp3",
        "question": [
            "Padamu negeri kami berjanji",
        ],
        "decoration": [],
        "answer": "b",
        "btn_a_src": "assets/img/quest/seru/kebangsaan/q5/a.png",
        "btn_b_src": "assets/img/quest/seru/kebangsaan/q5/b.png",
        "btn_c_src": "assets/img/quest/seru/kebangsaan/q5/c.png",
    },
]


class KebangsaanSeruScreen(LayoutScreen):
    def __init__(self, app, **kw):
        super().__init__(
            app=app,
            color_wrong="blue",
            questions_data=questions_data,
            home_destination="lagu_kebangsaan",
            bar_timeout_src="assets/img/quest/bar_timeout/kebangsaan.png",
            bg_lyric_src="assets/img/quest/bg_description/kebangsaan.png",
            timeout_duration=40.0,
            group_key_store="kebangsaan",
            key_store="seru",
            **kw
        )
