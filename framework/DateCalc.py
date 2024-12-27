from datetime import datetime, timedelta

class DateCalc:

    @staticmethod
    def getDateNDaysAfter(start_date, n):
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        new_date_obj = start_date_obj + timedelta(days=n)
        date = new_date_obj.strftime('%Y-%m-%d')
        return date
