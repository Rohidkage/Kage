from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

PREFIX = ["^", "?", "-", "+"]

cmd = [".", "-", "!", "("] # cmd custom


API_HASH = getenv("API_HASH", "ed14750e0b09ba61089d8353fe4e9815")
API_ID = int(getenv("API_ID", "14814105"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001599474353, -1001473548283, -1001578091827, -1001687155877, -1001812143750, -1001704645461, -1001557500960]
BLACKLIST_GCAST = list(
    map(
        int,
        getenv(
            "BLACKLIST_GCAST",
            "-1001599474353 -1001473548283 -1001578091827 -1001687155877 -1001812143750 -1001704645461 -1001557500960",
        ).split(),
    )
)
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001922757411"))
BOT_VER = "2.1.5"
BRANCH = getenv("BRANCH", "master") #don't change
CMD_HANDLER = [".", "?", "!", "(", "-"]
CMD_HNDLR = [".", "?", "!", "(", "-"]
OWNER_ID = getenv("OWNER_ID", "1557184285")
BOT_TOKEN = getenv("BOT_TOKEN", "6226033673:AAEBPb1OQP7QN3YMvZKCFaLDepyeDaKE7WQ")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
CHANNEL = getenv("CHANNEL", "kagestore69")
DB_URL = getenv("DATABASE_URL", "postgres://yyvynghu:MQmRAJ8K0hHq67YADVoapvWekPgNNZwj@jelani.db.elephantsql.com/yyvynghu")
GIT_TOKEN = getenv("GIT_TOKEN", "")
        
GROUP = getenv("GROUP", "userbotkage")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
REPO_URL = getenv("REPO_URL", "https://github.com/Rohidkage/Kage")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDiC5kAg-RyH-0rKdOj8ue1JjejzvlK6p3V7MwPDo01m4lxn6my-SO4I20MUH6jfQV62ty5dQta7xDztHRnEw51UNcxbTRAJxmlENKG8Bqu4d3ICImYt5WwOOhuCMOHJ6NrtR0xJkwbgC_izFQ97o3FAMhWOP4P1EI3QvHjubHXr_MzFuwZ6HxM5QoXUpL7t36rak_ssZiQ7H0dzxrbqc5rs73sQWjLqwtfcx44iXx8i6RREjiEOaJsRVez1Tonby929HfXfra5mtrjRCoW9fjBTee8D-XQGKNMxYUnQx4SMt5CLvX2BGeYaaYusHwA8psuH6Yt-oimK97chbz2oB19HshQSAAAAABc0L8dAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQGnWkoACUn75jmHQeNp9pAleAWGYBBpP0ZLGy2L-DPMgeswRC1Ow3YJ7aUFhAEz_EceeHAZxTreKgrJVAnqr7n_lD3dGssGcbTE6E0ow8YgA1U6YZ2RZPufJbU3d_SjHoqVRAYOP-P5Jsgv-HeP-AAsu71kcz4s4JYPT2UVY98mDc4a6onH3wSl-jtvjmO6fKO30IjWBznAusV0HgT0f1ArlqlakMI4hUqbqFzgqVpT0EZcQbieVpoK98tBnt3ktPbgjor1MIEE50OqxN4ZgGh0d7-6iYRi5aNfuAdfs2XPBDKPwRBbmu3_-omOCM7TNzTGsFRmviBGxXER1c2EyvQtshxACgAAAABn41EqAA")
STRING_SESSION3 = getenv("STRING_SESSION3", "BQF9ztkAvNxnAzBI87uIkTqK_zNPz_UnZlG-FQQTtlDnnacsGy6PToC2PY_qbAaGzy8km8EQOdnG0mFWLs0Ur_2qLg66CI7aq6u2wxpF8nFDCeQCCVNu8emHtAj2ZvKArVG3RsX6o5QDBdtRYfCilIF3Mq8iBbrIrmOS_S7SUlCU6Qlic27w5WEOOOkztXJRF5tFHg3eqTRf1oC_0p9gGG2P_iZKkyV6-Jh8y6oi29RtervNoqNHFQW_cqbmA5oi7lfeYw6NX2OXOmvI4PxgoVx188q0WIlhB7a5CNVjvi0lUFBKcsN-2KgzL9JUaEIn-6vfYm9XxDnVDFc4MJBCCUZ5kS4QygAAAABkbuINAA")
STRING_SESSION4 = getenv("STRING_SESSION4", "AQDLivUAMm1fERA5gTNaj5UMHkitC_zYFnn_OR0QtU8HQHqVpf5SaTaXdlsaGyo3c_EqtJ9P_b2JxH0xdsGRffk_TO5ttnvYBshhB3eO3VUVD4mCJ6yMaRj2oMlXpeTOHzkICGKD1zrsozXSw33kTcRcR5l0wA_mbLs-k4kuVedlUaZxQK9175zeJ-rC2uAAIGYMRTE3VHIj6zr72Xr6flANV4GqzTeh4emAsUikTLdrmMNo8E-Gzy8Q9AKpzrVPGaur9x50rIMyR31P0ocBqwwMOJ5fkgxZhes_b5XJKHM5qbDW0VW9ERaw03jtHHTddf8z5UZvorz-1K3fLyQOkwW2IfodTgAAAAFW3Y4KAA")
STRING_SESSION5 = getenv("STRING_SESSION5", "BQDJqjsAihSij8X5LHJwujU4ta7wJwXx2luSBAimf-q7rmymVjU-YFzh90Rk81AH0gZmifuY4JRusf9ROmBCCRGy8q0bAOIwnD0mZWLzimBivT5ZbnM69ReXrpVQFHoFz0-mVMqgBkf9OBNZ4MpzmSv2v_9kBPBSR3q0o0gbjJKkWqaUE9CYETbyFYW70XKVmVNUnNaV7B4LGp5rfL2atuuqaNPPXpzyX23giZVpT7kz5yHHMHJqPR-_GaxTVXqpCF_mHs5NBy_qqZe8gH7jdrlnHeHgguQEZD8n0z6IyZ_ZlwImqEoW6qzSLaTau92MIPebimzHkDyL6y7Bnlp4JEJoVock4wAAAAByyxiLAA")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")
STRING_SESSION16 = getenv("STRING_SESSION16", "")
STRING_SESSION17 = getenv("STRING_SESSION17", "")
STRING_SESSION18 = getenv("STRING_SESSION18", "")
STRING_SESSION19 = getenv("STRING_SESSION19", "")
STRING_SESSION20 = getenv("STRING_SESSION20", "")
STRING_SESSION21 = getenv("STRING_SESSION21", "")
STRING_SESSION22 = getenv("STRING_SESSION22", "")
STRING_SESSION23 = getenv("STRING_SESSION23", "")
STRING_SESSION24 = getenv("STRING_SESSION24", "")
STRING_SESSION25 = getenv("STRING_SESSION25", "")
STRING_SESSION26 = getenv("STRING_SESSION26", "")
STRING_SESSION27 = getenv("STRING_SESSION27", "")
STRING_SESSION28 = getenv("STRING_SESSION28", "")
STRING_SESSION29 = getenv("STRING_SESSION29", "")
STRING_SESSION30 = getenv("STRING_SESSION30", "")
STRING_SESSION31 = getenv("STRING_SESSION31", "")
STRING_SESSION32 = getenv("STRING_SESSION32", "")
STRING_SESSION33 = getenv("STRING_SESSION33", "")
STRING_SESSION34 = getenv("STRING_SESSION34", "")
STRING_SESSION35 = getenv("STRING_SESSION35", "")
STRING_SESSION36 = getenv("STRING_SESSION36", "")
STRING_SESSION37 = getenv("STRING_SESSION37", "")
STRING_SESSION38 = getenv("STRING_SESSION38", "")
STRING_SESSION39 = getenv("STRING_SESSION39", "")
STRING_SESSION40 = getenv("STRING_SESSION40", "")
STRING_SESSION41 = getenv("STRING_SESSION41", "")
STRING_SESSION42 = getenv("STRING_SESSION42", "")
STRING_SESSION43 = getenv("STRING_SESSION43", "")
STRING_SESSION44 = getenv("STRING_SESSION44", "")
STRING_SESSION45 = getenv("STRING_SESSION45", "")
STRING_SESSION46 = getenv("STRING_SESSION46", "")
STRING_SESSION47 = getenv("STRING_SESSION47", "")
STRING_SESSION48 = getenv("STRING_SESSION48", "")
STRING_SESSION49 = getenv("STRING_SESSION49", "")
STRING_SESSION50 = getenv("STRING_SESSION50", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
