from flask import Blueprint, request, jsonify
from provider.stats.parent_stats import ReportServiceParent
from provider.stats.child_stats import ReportServiceChild

report_router = Blueprint("/reports", __name__)


@report_router.route("/reports/parent", methods=["GET"])
def ReportServiceParent_displaying_report():
    pid = request.json.get("pid")

    Report = ReportServiceParent(pid)
    daily_report = Report.get_daily_report(pid)
    # weekly_report = Report.get_weekly_report(pid)
    # monthly_report = Report.get_monthly_report(pid)

    return jsonify(
        {
            "daily_report": daily_report,
            # "weekly_report": weekly_report,
            # "monthly_report": monthly_report,
        }
    )


@report_router.route("/reports/child", methods=["GET"])
def ReportServiceChild_displaying_report():
    pid = request.json.get("pid")

    Report = ReportServiceChild(pid)
    daily_report = Report.get_daily_report(pid)
    # weekly_report = Report.get_weekly_report(pid)
    # monthly_report = Report.get_monthly_report(pid)

    return jsonify(
        {
            "daily_report": daily_report,
            # "weekly_report": weekly_report,
            # "monthly_report": monthly_report,
        }
    )
