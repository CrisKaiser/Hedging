from datetime import datetime, timedelta

class DateCalc:

    @staticmethod
    def getDateNDaysAfter(start_date, n):
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        new_date_obj = start_date_obj + timedelta(days=n)
        date = new_date_obj.strftime('%Y-%m-%d')
        return date

    @staticmethod
    def isDateBefore(date1, date2):
        date1_obj = datetime.strptime(date1, '%Y-%m-%d')
        date2_obj = datetime.strptime(date2, '%Y-%m-%d')
        return date1_obj < date2_obj

    @staticmethod
    def areDatesEqual(date1, date2):
        date1_obj = datetime.strptime(date1, '%Y-%m-%d')
        date2_obj = datetime.strptime(date2, '%Y-%m-%d')
        return date1_obj == date2_obj
