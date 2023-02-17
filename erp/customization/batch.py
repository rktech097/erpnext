import frappe
from frappe.model.document import Document
class Batch(Document):
    def autoname(self):
        if self.reference_doctype =="Purchase Receipt":
            sup = frappe.db.get_value("Purchase Receipt", self.reference_name, 'name')
            item = frappe.db.get_value("Purchase Receipt", self.reference_name,"items")
            a = sup.split("-")
            b = a[3]
            self.abbr = b
            self.naming_series = "B-.{abbr}.-.###"
            self.batch_id = self.naming_series
            item = frappe.db.get_value("Purchase Receipt", self.reference_name,"items")
            frappe.msgprint(item)
            for i in item:
                data = frappe.db.get_value('Purchase Receipt Item',{"parent":self.reference_name},['mill_coil_id','obs_losses1',
                'obs_losses2','grade','obs_losses3','qc_remarks','width'],as_dict=1)
                frappe.msgprint(data.mill_coil_id)
                i.mill_coil_id = data.mill_coil_id
                # self.grade = data.grade
                # self.obs_losses1 = data.obs_losses1
                # self.obs_losses2 = data.obs_losses2
                # self.obs_losses = data.obs_losses3
                # self.qc_remarks = data.qc_remarks
                # self.width = data.width


            