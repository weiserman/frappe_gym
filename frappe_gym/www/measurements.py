import frappe
from frappe import _
import frappe.www.list
from frappe.utils import getdate

no_cache = 1

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

    if frappe.db.exists("User", {"email": frappe.session.user}): 
        context.email = frappe.session.user
        context.current_user = frappe.get_doc("User", frappe.session.user)
        context.show_sidebar = True
    else:
       frappe.throw(_("You need to be a Gym member to view this page"), frappe.PermissionError)
   
    # extract the list of measurements for user
    measurements = frappe.get_all("Member Measurements", filters={ 'email': frappe.session.user}, fields=["*"], order_by='signs_date DESC')

    # Lets determine their BMI and warn accordingly
    curr_measurements = []
    for measure in measurements:
        if (measure.bmi<18.5):
            measure.update({ "badge": "badge badge-pill badge-warning"})
        elif (measure.bmi>=18.5 and measure.bmi<25):
            measure.update({ "badge": "badge badge-pill badge-info"})
        elif (measure.bmi>=25 and measure.bmi<30): 
            measure.update({ "badge": "badge badge-pill badge-warning"})
        elif (measure.bmi>=30):
            measure.update({ "badge": "badge badge-pill badge-error"})
        else:
            measure.update({ "badge": "badge badge-pill badge-info"})

        curr_measurements.append(measure)      


    context.measurements = curr_measurements