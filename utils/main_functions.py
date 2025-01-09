from datetime import datetime

import pytz


def change_utc_to_local(utc_time):
    print(utc_time)
    utc_datetime = datetime.fromisoformat(utc_time)
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    tashkent_time = utc_datetime.astimezone(tashkent_tz)
    return tashkent_time.strftime("%Y-%m-%d %H:%M:%S")


def create_report(data):
    report_text = str()
    report_summ = 0
    report_text += f"\n 📝 Jami hisobotlar soni: {len(data)} ta\n\n"
    for index, report in enumerate(data):
        new_amount = "{:,}".format(report['amount']).replace(",", " ")
        created_at = change_utc_to_local(str(report['created_at']))
        report_text += f"{index + 1}. {new_amount} so'm, {report['description']}, {created_at}" + "\n \n"
        report_summ += report['amount']
    report_summ = "{:,}".format(report_summ).replace(",", " ")
    report_text += f"✅ Umumiy hisob: {report_summ} so'm"

    return_data = {
        "report_text": report_text,
        "report_summ": report_summ
    }
    return return_data
