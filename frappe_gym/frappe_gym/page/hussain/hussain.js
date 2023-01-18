frappe.pages['hussain'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'test',
		single_column: true
	});
}