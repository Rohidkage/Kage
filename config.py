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
STRING_SESSION1 = getenv("STRING_SESSION1", "BQDiC5kAVAHq1aNrSyNH89zkMIETSqy618bMOp65455-vKwXA0gmifPpEEqS4ux9cYdLEHjjA0vZiE2PQgbr-79Iv772Z5SwXmqxZk9F5zZYz19nHleNx0BmRQfIU5EPz2cV7Uxf8CR6H5qGBvrDSwKLG5is2Y4F0riE_uJF7RDuG6jgzEva7rkWILQOmVTXorkCfstRGmuafQ7kBSZ3irtV-jFfrZdtMoadubwJ-0EVBcO6gPbIF3ij1npdHWJfFWaxNaXpaDmrWlnEGhkiIZIr6pkT6qE2DDDnNo3_yejmPzgMdw6q_ZpxJ5hiMwcmG85l0Pjl5hTHOFEUWClV-yhqqq2aeAAAAABc0L8dAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQGnWkoACUn75jmHQeNp9pAleAWGYBBpP0ZLGy2L-DPMgeswRC1Ow3YJ7aUFhAEz_EceeHAZxTreKgrJVAnqr7n_lD3dGssGcbTE6E0ow8YgA1U6YZ2RZPufJbU3d_SjHoqVRAYOP-P5Jsgv-HeP-AAsu71kcz4s4JYPT2UVY98mDc4a6onH3wSl-jtvjmO6fKO30IjWBznAusV0HgT0f1ArlqlakMI4hUqbqFzgqVpT0EZcQbieVpoK98tBnt3ktPbgjor1MIEE50OqxN4ZgGh0d7-6iYRi5aNfuAdfs2XPBDKPwRBbmu3_-omOCM7TNzTGsFRmviBGxXER1c2EyvQtshxACgAAAABn41EqAA")
STRING_SESSION3 = getenv("STRING_SESSION3", "BQF9ztkAvNxnAzBI87uIkTqK_zNPz_UnZlG-FQQTtlDnnacsGy6PToC2PY_qbAaGzy8km8EQOdnG0mFWLs0Ur_2qLg66CI7aq6u2wxpF8nFDCeQCCVNu8emHtAj2ZvKArVG3RsX6o5QDBdtRYfCilIF3Mq8iBbrIrmOS_S7SUlCU6Qlic27w5WEOOOkztXJRF5tFHg3eqTRf1oC_0p9gGG2P_iZKkyV6-Jh8y6oi29RtervNoqNHFQW_cqbmA5oi7lfeYw6NX2OXOmvI4PxgoVx188q0WIlhB7a5CNVjvi0lUFBKcsN-2KgzL9JUaEIn-6vfYm9XxDnVDFc4MJBCCUZ5kS4QygAAAABkbuINAA")
STRING_SESSION4 = getenv("STRING_SESSION4", "AQDLivUAMm1fERA5gTNaj5UMHkitC_zYFnn_OR0QtU8HQHqVpf5SaTaXdlsaGyo3c_EqtJ9P_b2JxH0xdsGRffk_TO5ttnvYBshhB3eO3VUVD4mCJ6yMaRj2oMlXpeTOHzkICGKD1zrsozXSw33kTcRcR5l0wA_mbLs-k4kuVedlUaZxQK9175zeJ-rC2uAAIGYMRTE3VHIj6zr72Xr6flANV4GqzTeh4emAsUikTLdrmMNo8E-Gzy8Q9AKpzrVPGaur9x50rIMyR31P0ocBqwwMOJ5fkgxZhes_b5XJKHM5qbDW0VW9ERaw03jtHHTddf8z5UZvorz-1K3fLyQOkwW2IfodTgAAAAFW3Y4KAA")
STRING_SESSION5 = getenv("STRING_SESSION5", "BQDJqjsAihSij8X5LHJwujU4ta7wJwXx2luSBAimf-q7rmymVjU-YFzh90Rk81AH0gZmifuY4JRusf9ROmBCCRGy8q0bAOIwnD0mZWLzimBivT5ZbnM69ReXrpVQFHoFz0-mVMqgBkf9OBNZ4MpzmSv2v_9kBPBSR3q0o0gbjJKkWqaUE9CYETbyFYW70XKVmVNUnNaV7B4LGp5rfL2atuuqaNPPXpzyX23giZVpT7kz5yHHMHJqPR-_GaxTVXqpCF_mHs5NBy_qqZe8gH7jdrlnHeHgguQEZD8n0z6IyZ_ZlwImqEoW6qzSLaTau92MIPebimzHkDyL6y7Bnlp4JEJoVock4wAAAAByyxiLAA")
STRING_SESSION6 = getenv("STRING_SESSION6", "BQCTvFYArHJ1xd4RAuLckw1f5XuTTgtq06RUISvPohdqJCYJ9uhFxNheZA9AZNJVAQI0bYtugwPEWD2PB-pwTVQqHJVALvN71rvJ6jVsAlNGvwFoKFAVacxZxUX3wFFwSj_D261Mt0U1vNImNzwZabXk0zila2kesX9V6fH-IE-_HAja6KUMZjJUfakXQ2glIoQ7V6G_vEfsrNfX3Wef35IwV-Q0QI3CSwFQBOz4M573AkgbIae6kJQN6OPYmo81ulX8XosBV3SqpifcqyTzBAVqpC-AFDcGSlfQg8Z-BtSIOvS_HM6j3q1OyNOkqyPdvfAdOwA4cq0iIVWWbzYbnTDhxp65nwAAAABvGdHuAA")
STRING_SESSION7 = getenv("STRING_SESSION7", "BQGIZJQAlZY8iJ8pjPXsPy7s4sE8CBPwq2QJEPdGxO3eWbq6fYrwlcIhMOESnBL6YsngDGN161qtxAQvDBfPf3gujcFLiIWODh-rSOGnykVlaYUmHsTYoh1-RiQoATSqRsE0UsAPUy2sNV7Ph2xiEPmif_VrcorQn-JghGDT45H-Tc1LGFISNliquNncqhW3n4Z3ThOu1ba6sIdmQk-TxUXVkhlhd-E_r1D4Oae9aWQME_eD3u5yLFoIWzmECetIoGrSdFyIJGTWK4poZbqZHzLfCh2yQF_P-sHBm2l8m57Ysz18sorx5TY48tsN2F6na3YHBN6foZay_hlLVJbuYgbYSesY2QAAAABQzCpBAA")
STRING_SESSION8 = getenv("STRING_SESSION8", "BQG5O2AAQhMlp-aAhmuHPTxFLc_tq3ZbtYbmgfJgmlqJRu1o4v2tO6ixQDUPN9Kyz2RxVywn2gxWuq3BDSucX1SWLyHjrFJkfy9dVgnsMcDI9F3rDloQcDQp-PoOXSDTo9ltcpRPVbUTCz9n2VmHJM33e3nttH2sqt1YBtKHIurwMDXrclR1BAWUUernkO4hhVuqPWINmqWfvpLKLxtnt2bsER-oKnaTzccqwqmzLQsIWyo2H3WuCBdaKH4o1hpoLJgi6YU_-qTjAwRq1Vcv6M0h6u7C1oxfkiBoKVgmGjqwO70ET3FK_K95Sogua4k9Dy-1GDRwgb58GNcrJVtFht1Hpq6rmQAAAABhk2GMAA")
STRING_SESSION9 = getenv("STRING_SESSION9", "BQFvvkUAV9AFSvkGwh1Us79GruLwOWt7Kbe9mPiAZdbrTh2GBlNV-cE6pYMLWxoR8KlKusugIeKKGl_MQVEmCDaNTQ_w4grdmlb8TENGc2X6QKpLyibBm6od6BC2HuxNhXTf5hKQnEoAAYlbTzOSvGhb_Lvz9HA4gWY1m1WeD7-8vwxmCl1dJKi0tpiQ2T_bbD9eKFkQB8wevqjv-mENPmDJCsq7L38NrUsXLr36ODcjtZ3_m_TYFVVAUrvtNGio_pE9oH6mLcUx0TRzsQ2BhwQka-lqjAFiuxJdNRkELkHR1grJMHTK_nqsKJMQbAfl0NiipJIQjs4XhXXIkuUajvIxfbdWxgAAAABxNCGXAA")
STRING_SESSION10 = getenv("STRING_SESSION10", "BQFEDJoAM6QExdLaI3iAUqHoxDZT3CPTHhKaqCsypfTv2cGbF-fhidq-rIfkvVWcv6IxRErSBbWXBNTeuggnoxS0Gf-gjKN__EIyNewFNMdvP3CvfALXVPbld7XtVHrBraCPXtMKN5hkz258HYKmR7eYCq82RRWRrep4k2YbsZ6POBvJ275a4--aAjD6BdUIQWxtlXjbdprDEKw7sOmogrqTADL8dUb3YX8RN1B8mKGrNJxFs19gcCN6RSubMUpH0gsN3UJs-8Kp04t_ax6uW_TaNqv0ARUMnRJHqPixX54odnlyUsNefdTig3nZSfG4UCamLI5Xabiiz2qEmBwhSejQLT721wAAAABhzubTAA")
STRING_SESSION11 = getenv("STRING_SESSION11", "BQAY8JIAVlqpmwmI1wa7sg8gJjang-qEUYrbeo4dxK0wPUU29aAi2lq7oeQDYYCuc8gsGtMgFPov_OoP1TtCTLsm8hQd6c4Z8qb-jkYtO6lg2pVQSYijipjQbRzJ1kNfn5cRKhhsS0_zl4IuFKkazH3kXUHPuMPibs0L9iLM5ItigLup32JMJ5tqO4E0azI3TgFEbEwXthS_D4TOOcojMospZ70ChV6DDc4GmSUzEqEWgkh5EsA3ULBJVcIacTCr3l3IoIWKuq5A6D1Pjen-dUwCpdAvwMKOXf8-KUBQAXDGeJ8fgeaDWcehSFTVzpA8G4cePxJC7Ur9E7I9jCi7wVURGqEzngAAAAFd4ap4AA")
STRING_SESSION12 = getenv("STRING_SESSION12", "BQF2PCUAAirAiLGjXM6hVjD7qtV2LQ5QNmY_76asKajUF832WrZc_6cdeGxiJtQP8NuLzOMox4yYXu2TjpserMVKuSXHfcqISRXvdzUVbGV5hIPw0oJ4Xhii9Auu8FP1WOJB1FhmemNb9WGCtp9eEpBHB3m-0IwYy1RlJV1jtvPXe9fVHXxHOHnvfo_MnMk4fg0dnbZFBG1UHUwO54XMN5DHI5fAdOKh1dV4V5Xg9ihJm2S2dMDTUzYzv1nU0FNPPMqEgld7zRCs1HLsBEm-Gvlfpv8aZVA8-4g1FLiVCSpL8gSI_PWZJnxoWzF37V9tGl2C2ehdPFJi-QZq5ARLEFE1I4i2hQAAAAA-R1lwAA")
STRING_SESSION13 = getenv("STRING_SESSION13", "BQFm3MMAbOf9pUb4ezPEE_A0bN0uY-YkjR3Daxz2e9Z3Kx2TaNWykUzxiAo5vi0Xl25uohK5YVG8BPPEiGU2lXtRAG-Sb84yFhgY3oI7V7uhDTEdAbs-HNjUqsSIqYJoDsmAbKlZm7JkuzRyKwODeyhIhw6PmLFZ_ijM21VIQqjGOsG0e9XgW5HQK6JBLLV_f3Sby_B-OJG2oebr6DvsoAmu_MIRpYL8JiPYr1cQ6k7XEhZ9LqxeB1TLzkzkiiys64IHKdeWVXPzK7AF3KgYIT7rlj5Yej51ozwvgkxoIoEOEG8oBs7YVV00V93h8RuIH6H5CNyrHhn3RvWmPvPaoCItqa1mXwAAAABOzBGHAA")
STRING_SESSION14 = getenv("STRING_SESSION14", "BQF-_GAAp6R5HbKOB5ADQRPrZ1i5dzzst9pWw4eYcS4hFcAlBAUzTuEOZvFeSCsbClHPXgzLHXTKdRN8nX9BprmbnjmAFeb6gVqGP6yZNTdFK67gtzDtoXNAV66b2lPOTXNhasuKP2bUrYpHOHBQhch9c7mhbxPxzoPC-AbCxm5BHf54JAeVZdL7eUMyoL1Rj_SxtKxyK16MI8kpWGu0YQLWOnhNl8sVAQVTlcxr4ldI0yBYH1wRzyY0WTwzj-KcIsRR6PzWLowZyQ_W2k3AN5qH0UJ5zXvJIROqar2CCZNTG6AlYhToGnwtMQtfP2AC1jnboyB7DJNdp2AQcG5l4hVDu_Tf8AAAAAAy38uuAA")
STRING_SESSION15 = getenv("STRING_SESSION15", "AQFOasMAvtHMsUHtKIa0hUoogx-EMlHtphh1ljj2zJGwUBDZcqcxy_F5-2njEmwwudJCF7PyjbbFQqGLwC6Aj3GUg2ZAzpcCYriBx5vD9TExWduZPMKKy5BMEZ4WDaQ7ZJtAyGyuKHUHB1HAcXvLL2hLdeiLIa1uZvbZzUHeDi-BwmcJjeU9NCR5t6jNFEbT1kQCyOiIlK3EXlNH5lnPZFlpcLlKWDiQPWdSjCHJHIg47eUSzCiqYt75FO-SZg6Fx032GwCf7ma7CxCaqvV3EctGZBRre0fS8XYQS3C4j3-vEtQfrxLl_O2xd9GPGQlKpUgRsjxUhQ_EMw0uUMGBLuroUwltzAAAAAFoGXIpAA")
STRING_SESSION16 = getenv("STRING_SESSION16", "BQAY8JIAA9xwj7NokIkvKP25yZKXiSP4M5AmpbZra_53NGUKyDNVdhH-cTkdL73h4ANfXIwjjVOIr46Z7FeynhHGxbNqYXibCzJWh_Q1bvG1C9qaBtTvIdXwK3-bkUS6HIkzcADJpLB69zuHwzhAPZcvap4fyOs_v1v9eSu5lh_FO6Yr0KLJXKUFf8brZdbCjSeTMDNTGf0CDLeHARk8PO2-fveDUyhMxNapAX5mHuRCWJ-wxLTy_2xOuCQSvM8_cw7-jtsiI_nPPRgVBA55s99eAw5TEFsy7py0tcxyl0AeqyWWHje3FAsgSpJnoU8UG4sB-vnspI6ECDolaTkrJHR7b8lvxAAAAAEzgH4IAA")
STRING_SESSION17 = getenv("STRING_SESSION17", "BQAY8JIAEkyOdlb_T-qdzpRm1ktqlY53SfPRFHYP0hfXaUt6iWK3juBjVkdLSb80719dpOKQCUx5JZFD0dZVxhYKhEsW8waLIdDk53HlLcffArb-y0iK3fdTskKW9pvtL_BbYXS9fLGkGodSG1-kx1LJWkM_rQ-S2455XFlT7zsyzfgSWAy7EsuNm-zT8GlOcZONFlA15jJEsxMaDZZmcXoEIs7WQj47khWcvNrthgmk8oeqiFL85DiU-KU-FrTeGlC0QBeEaV4z4jmzpDz0HMQEeu0OKIpQ9ohxKFozrNHJSVoNlYFd6AI2QICMbyaBJkf61E_rTEcptugzaWcSEMLWnEEIQgAAAABt1A_SAA")
STRING_SESSION18 = getenv("STRING_SESSION18", "BQAY8JIAuGN9TIo7ZaMFpjU1f7Dc7480s7rOc1Xfb9jCjHzxMNkkqrLSwb1dFbDei5VrfmEvbHXTbo2xw7VQ0Mi6eNCv-vgL77AHS7p4ObqmfMwVaMjw_voIdOlo7tO_tkzOieO0OqlP6-D2E6UpZEGzWHe7NYXkMw1_fE2Y1GW2MjiUVm8NjCHpjNd1paweCs789GzNeFuKh_7eEkDGSLyH-n1qX19kZJk1shpD10DqBBNUaev11yEtZzcxAHENzq8Lx5ZcS1z6qyoZjMDARlEF_cRP3G3VKwjZy9RsgCAU9cJTs8_O_72QxhQnMDpJEnPmqhDAvtcgSCWTaQ3Zzok5dZ6VogAAAABJL3M7AA")
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
