# this script is used to modified rds instance size

import boto3


Profile = "MMA"

session = boto3.Session(profile_name=Profile)

rds = session.client("rds")

res = rds.describe_valid_db_instance_modifications(
    DBInstanceIdentifier="database-1")['DBInstances'][0]

print(res)
# for db_data, value in res["ValidDBInstanceModificationsMessage"].items():

#     #    print(type(db_data))
#     if (db_data == "Storage"):
#         for item in value:
#             print(item)

#  When you call modify_db_instance and only provide the parameters you want to change, everything else remains unchanged.
# So in my case, instance storage, IOPS, and other configurations will stay exactly as they are, unless I include them in the call.
# response = rds.modify_db_instance(
#     DBInstanceIdentifier='database-1',
#     DBInstanceClass='db.t4g.xlarge',
#     ApplyImmediately=True

# )

# response2 = rds.modify_db_instance(
#     DBInstanceIdentifier='database-1',
#     DBInstanceClass='db.t4g.micro',
#     ApplyImmediately=True

# )

# print("Modification initiated:", response['DBInstance']['DBInstanceIdentifier'])

# # Wait until DB is available
# waiter = rds.get_waiter('db_instance_available')
# waiter.wait(DBInstanceIdentifier='mydb')
# print("Modification complete, DB is available")