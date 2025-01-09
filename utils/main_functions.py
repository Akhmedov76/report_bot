from datetime import datetime
from main.constants import ReportType
import pytz


def change_utc_to_local(utc_time):
    utc_datetime = datetime.fromisoformat(utc_time)
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    tashkent_time = utc_datetime.astimezone(tashkent_tz)
    return tashkent_time.strftime("%Y-%m-%d %H:%M:%S")


def create_report(data):
    report_text = str()
    report_summ = 0
    report_text += f"\n 📝 Jami hisobotlar soni: {len(data)} ta\n\n"
    for index, report in enumerate(data):
        new_amount = f"{int(report['amount']):,}".replace(",", " ")
        created_at = change_utc_to_local(str(report['created_at']))
        report_text += f"{index + 1}. {str(new_amount)} so'm, {report['description']}, {created_at}" + "\n \n"
        report_summ += report['amount']
    report_summ = "{:,}".format(report_summ).replace(",", " ")
    report_text += f"✅ Umumiy hisob: {report_summ} so'm"

    return_data = {
        "report_text": report_text,
        "report_summ": report_summ
    }
    return return_data


def create_global_report(data):
    report_text = str()
    report_summ = 0
    report_text += f"\n 📝 Jami hisobotlar soni: {len(data)} ta\n\n"
    for index, report in enumerate(data):
        new_amount = f"{int(report['amount']):,}".replace(",", " ")
        created_at = change_utc_to_local(str(report['created_at']))
        if report['type'] == ReportType.income.value:
            report_summ += report['amount']
            report_text += f"{index + 1}. Daromad, {str(new_amount)} so'm, {report['description']}, {created_at}" + "\n \n"
        elif report['type'] == ReportType.expense.value:
            report_text += f"{index + 1}. Xarajat, {str(new_amount)} so'm, {report['description']}, {created_at}" + "\n \n"
            report_summ -= report['amount']
    report_summ = "{:,}".format(report_summ).replace(",", " ")
    report_text += f"✅ Umumiy hisob: {report_summ} so'm"
    return_data = {
        "report_text": report_text,
        "report_summ": report_summ
    }
    return return_data