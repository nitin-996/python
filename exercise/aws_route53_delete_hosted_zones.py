import boto3

# this script is used to delete all records from all hosted zones declared in aws route53

AWS_PROFILE = 'indifolio'
Route53_Hosted_zones = []

# using profile
session = boto3.Session(profile_name=AWS_PROFILE)
route53 = session.client("route53")

list_zones = route53.list_hosted_zones()

for hosted_zone in list_zones["HostedZones"]:
    zone_id = hosted_zone["Id"].split("/")[-1]
    Route53_Hosted_zones.append(zone_id)


# fetching existing records zone by zone
paginator = route53.get_paginator("list_resource_record_sets")

for zone in Route53_Hosted_zones:
    records_sets = []

    for page in paginator.paginate(HostedZoneId=zone):
        records_sets.extend(page["ResourceRecordSets"])

    # build changes list for this zone only
    changes = []
    for record in records_sets:
        if record["Type"] in ("NS", "SOA"):
            continue   # ❌ skip required records
        changes.append({
            "Action": "DELETE",
            "ResourceRecordSet": record
        })

    # delete in batches of 100
    for i in range(0, len(changes), 100):
        batch = changes[i:i+100]
        response = route53.change_resource_record_sets(
            HostedZoneId=zone,
            ChangeBatch={"Changes": batch}
        )
        print(f"Submitted batch {i//100 + 1} for zone {zone}. Change ID: {response['ChangeInfo']['Id']}")