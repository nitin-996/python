res = {
    'HostedZones': [
        {
            'Id': 'string',
            'Name': 'string',
            'CallerReference': 'string',
            'Config': {
                'Comment': 'string',
                'PrivateZone': True|False
            },
            'ResourceRecordSetCount': 123,
            'LinkedService': {
                'ServicePrincipal': 'string',
                'Description': 'string'
            }
        },
    ],
    'Marker': 'string',
    'IsTruncated': True|False,
    'NextMarker': 'string',
    'MaxItems': 'string'
}


for Zones in res["HostedZones"]:
     for key , value in Zones.items():
          print(f"{key} : {value}")


print(help(res))