import frappe

def get_context(context):
    # Get all the published workouts
    context.workouts = frappe.get_list("Gym Workout Plan", filters={"is_published": 1},fields=["plan_name", "description", "photo", "route"])
    frappe.log(context.workouts)