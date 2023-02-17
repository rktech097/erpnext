import frappe

@frappe.whitelist()
def get_item_code(ref_code):
    data = frappe.db.sql(f"""select parent from `tabItem Customer Detail` where ref_code = '{ref_code}'""",as_dict=1)
    return data
