import sys
sys.path.append('/home/nitin/Prac_TECH/python/moduleDir')
import mymodule


print(mymodule.pi)

# def dicData():
#     return {
#        "data":{
#             "user": {
#             "id": 101,
#             "name": "Magdhalina",
#             "email": "magdhalina@example.com",
#             "roles": ["admin", "editor"],
#             "preferences": {
#                 "notifications": {
#                     "email": True,
#                     "sms": False
#                 },
#                 "theme": "dark"
#             }
#         },
#         "projects": [
#             {
#                 "id": "proj-001",
#                 "name": "Website Redesign",
#                 "status": "active",
#                 "members": [
#                     {"id": 201, "name": "Alice", "role": "designer"},
#                     {"id": 202, "name": "Bob", "role": "developer"},
#                 ]
#             },
#             {
#                 "id": "proj-002",
#                 "name": "Mobile App",
#                 "status": "archived",
#                 "members": [
#                     {"id": 203, "name": "Carol", "role": "tester"},
#                     {"id": 204, "name": "Dave", "role": "developer"},
#                 ]
#             }
#         ],
#         "account": {
#             "plan": "Pro",
#             "usage": {
#                 "storage_gb": 34.8,
#                 "api_calls": {
#                     "this_month": 12039,
#                     "last_month": 9321
#                 }
#             },
#             "billing": {
#                 "currency": "USD",
#                 "next_payment_due": "2025-05-10",
#                 "payment_methods": [
#                     {"type": "card", "last4": "1234"},
#                     {"type": "paypal", "email": "user@paypal.com"}
#                 ]
#             }
#         }
#        }
#     }

# data = dicData()

# for extract_dic_data in data["data"]:
#     print(extract_dic_data)


