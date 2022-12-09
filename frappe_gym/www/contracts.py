import frappe
from frappe import _
import frappe.www.list
from frappe.utils import getdate
from frappe_gym.frappe_gym.doctype.gym_membership.gym_membership import get_contract_status, get_days_left_in_plan

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
   
    # extract the list of contracts for member, some are virtual attributes so need to recalculate as not in DB
    contracts = frappe.get_list("Gym Membership", filters={ 'email': context.email }, fields=["*"], order_by='start_date DESC')
    curr_contracts = []
    for contract in contracts:
        status = get_contract_status(contract.start_date, contract.end_date)
        days_left = get_days_left_in_plan(contract.end_date)
        contract.update({ "contract_status": status})
        contract.update({"days_left": days_left})
        if status == "Active":
            contract.update({ "badge": "badge badge-success"})
        elif status == "Expired":
            contract.update({ "badge": "badge badge-pill badge-warning"})
        elif status == "Not Started":
            contract.update({ "badge": "badge badge-pill badge-info"})
        curr_contracts.append(contract)  
    context.contracts = curr_contracts

    # get the trainer for the user
    if frappe.db.exists("Gym Trainer Subscription",{"member_email": context.email}):
        trainer_name = frappe.db.get_list("Gym Trainer Subscription",filters={"member_email": context.email}, pluck='trainer')
        context.trainer = frappe.get_doc("Trainer",trainer_name[0])