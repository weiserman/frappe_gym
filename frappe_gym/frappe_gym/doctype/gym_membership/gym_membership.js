// Copyright (c) 2022, Agile.co.za and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership", {
    // when gym plan is changed then update the end date of contract
    length: function (frm) {
        frm.set_value(
            "end_date",
            frappe.datetime.add_days(frm.doc.start_date, frm.doc.length)
        );
    },
    // when contract start date is amended, then adjust the termination date
    start_date: function (frm) {
        frm.set_value(
            "end_date",
            frappe.datetime.add_days(frm.doc.start_date, frm.doc.length)
        );
    },
    // set filters for active gym plans and all users
    refresh: function (frm) {
        frm.set_query("plan", function () {
            return {
                filters: {
                    active: 1,
                },
            };
        });
    },
});
