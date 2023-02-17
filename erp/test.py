import frappe
import json
import requests
from datetime import date
from datetime import time
from datetime import timedelta,datetime

@frappe.whitelist()
def indiamart_sona():
        end_time = str(datetime.now() + timedelta(hours = 5, minutes = 30))
        start_time = str(datetime.now() + timedelta(hours = 5, minutes = 24))
        url = "https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key=mR21Fbpl4nfIQfes5nSD7luKpVHMmTc=/Start_Time/"+start_time+"/End_Time/"+end_time+"/"
        response = requests.request("GET", url).json()
        data = responsedata2 = data["RESPONSE"][0]
	
        #frappe.log_error(start_time,"Sona nahi")
        #frappe.log_error(response,"Sona Response")
        for one in data2:
            if "Error_Message" not in one:
                lst = []
                mp = {}
                mp['QUERY_ID']= one.get("UNIQUE_QUERY_ID","")
                mp['Company'] = one.get("SENDER_COMPANY","")
                mp['Street'] = one.get("SENDER_ADDRESS","")
                mp['Last_Name']= one.get("SENDER_NAME","NA")
                mp['Email']=one.get("SENDER_EMAIL","")
                mp['Subject'] = one.get("SUBJECT","")
                mp['Mobile'] = one.get("SENDER_MOBILE","")
                mp['Message'] = one.get("QUERY_MESSAGE","")
                mp['City'] = one.get("SENDER_CITY","")
                mp['Select_State']= one.get("SENDER_STATE","")
                mp['Country']= one.get("SENDER_COUNTRY_ISO","")
                mp['Lead_Source'] = "IndiaMart"
                lst.append(mp)
                mp1 = {}
                mp1['data'] = lst
                url1 = "https://accounts.zoho.com/oauth/v2/token?grant_type=refresh_token&refresh_token=1000.0d5dcbbfc1471dde07b64475f5723927.b85fe4f2de6dfdfe21953b363548cd7e&client_id=1000.SQCDLZHVKV991Y6DZHLVLIMES75U9T&client_secret=2abd8a75e3b908eadabf03639b8ed9b0c1d5bbf42b&redirect_uri=https://developers.google.com/oauthplayground/"
                response1 = requests.request("POST", url1).json()
                url2 = "https://www.zohoapis.com/crm/v2.1/Leads"
                payload = json.dumps(mp1)
                headers = {
                   'Authorization': "Zoho-oauthtoken  "+ response1.get("access_token"),
                   'Content-Type': 'application/json',
                   }
                response2 = requests.request("POST", url2, headers=headers, data=payload).json()
                #data response2.get("data")
                #code = data.get("code")