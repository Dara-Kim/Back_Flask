from flask import jsonify
from datetime import datetime


class ReportServiceChild:
    def __init__(self, pid):
        self.pid = pid

    # 최신 ratio를 받아오기
    def get_daily_report(self, pid):
        # db check
        mood = 75
        correctedRatio = 80

        return {"mood": mood, "correctedRatio": correctedRatio}

    # 최신 7개 ratio를 받아오기
    def get_weekly_report(self, pid):
        mood = []
        correctedRatio = []

        for day in range(7):
            # db check
            daily_report = self.get_daily_report(pid)

            mood.append(daily_report["mood"])
            correctedRatio.append(daily_report["correctedRatio"])

        return {"mood": mood, "correctedRatio": correctedRatio}

    # 최신 30개 ratio를 받아오기
    def get_monthly_report(self, pid):
        mood = []
        correctedRatio = []

        for day in range(30):
            # db check
            daily_report = self.get_daily_report(pid)

            mood.append(daily_report["mood"])

        return {"mood": mood}

    # def result_code(self):
    #     isSuccess =
    #     code =
    #     message =
