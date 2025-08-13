import requests
import dataclasses


COMMON = "common"
AIRCON = "aircon"
SENSOR = "get_sensor_info"
TIME = "get_datetime"
CTRL = "set_control_info"


@dataclasses.dataclass(kw_only=True)
class Daikin:
    subject: str
    method: str
    Terminalid: str = ""
    Port: int = 0
    mode: int = 1
    stemp: int = "M"  # TEMPERATURE
    shum: int = "AUTO"  # HUMIDITY
    pow: int  # ON: 1 OFF:0
    f_dir_lr: int = "A"
    f_rate: int = "A"
    f_dir_ud: int = "A"


@dataclasses.dataclass(kw_only=True)
class SendQuery(Daikin):
    def __post_init__(self):
        header = {
            "user-agent": "",
            "content-type": "application/json",
        }
        _id = ""
        _pw = ""
        self.url = (
            f"https://api.daikinsmartdb.jp/{self.subject}/{self.method}?id=ID&spw=SPW&port={self.port}&terminalid={self.Terminalid}"
            f"&pow={self.pow}&mode={self.mode}&f_dir_lr=0&f_rate=A&f_dir_ud={self.f_dir_ud}&shum=AUTO&stemp={self.stemp}&f_dir_ud={self.f_dir_ud}"
            f"&stemp{self.stemp}&shum={self.shum}"
        )

        res = requests.get(self.url, headers=header)
        print(self.url, res.text)


check = SendQuery(subject=AIRCON, method=CTRL, pow=1, mode=6)
