import frappe
from frappe.utils import getdate, add_to_date
from datetime import datetime


def all():
    pass


def cron():
    print("\nCron Job Running")
    get_last_weeks_bookings()


def get_last_weeks_bookings():
    today = getdate()
    last_week = add_to_date(today, days=-7, as_string=True)
    bookings = frappe.get_all("Class Booking", filters={
                              "status": "Confirmed", "date": ["between", [last_week, today]]})
    for booking in bookings:
        booking_doc = frappe.get_doc("Class Booking", booking.name)
        print(booking.name)
        # booking_doc.send_booking_email()
