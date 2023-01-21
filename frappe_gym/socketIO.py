import frappe

# This is called from the doc_events hook


def new_class_booking(arg1, arg2):
    print("=====New class booking")
    frappe.publish_realtime(
        "msgprint", "{'message':'test','custom_app'}, after_commit=True")
