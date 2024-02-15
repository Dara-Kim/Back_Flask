from flask import jsonify
from datetime import datetime


class ReportServiceParent:
    def __init__(self, pid):
        self.pid = pid

    # 최신 ratio를 받아오기
    def get_daily_report(self, pid):
        # db check
        languageRatio = 75
        correctedRatio = 80

        return {"languageRatio": languageRatio, "correctedRatio": correctedRatio}

    # 최신 7개 ratio를 받아오기
    def get_weekly_report(self, pid):
        languageRatio = []
        correctedRatio = []

        for day in range(7):
            # db check
            daily_report = self.get_daily_report(pid)

            languageRatio.append(daily_report["languageRatio"])
            correctedRatio.append(daily_report["correctedRatio"])

        return {"languageRatio": languageRatio, "correctedRatio": correctedRatio}

    # 최신 30개 ratio를 받아오기
    def get_monthly_report(self, pid):
        languageRatio = []
        correctedRatio = []

        for day in range(30):
            # db check
            daily_report = self.get_daily_report(pid)

            languageRatio.append(daily_report["languageRatio"])
            correctedRatio.append(daily_report["correctedRatio"])

        return {"languageRatio": languageRatio, "correctedRatio": correctedRatio}

    # def result_code(self):
    #     isSuccess =
    #     code =
    #     message =
