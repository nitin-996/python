res = {
    'ValidDBInstanceModificationsMessage': {
        'Storage': [
            {
                'StorageType': 'string',
                'StorageSize': [
                    {
                        'From': 123,
                        'To': 123,
                        'Step': 123
                    },
                ],
                'ProvisionedIops': [
                    {
                        'From': 123,
                        'To': 123,
                        'Step': 123
                    },
                ],
                'IopsToStorageRatio': [
                    {
                        'From': 123.0,
                        'To': 123.0
                    },
                ],
                'SupportsStorageAutoscaling': True|False,
                'ProvisionedStorageThroughput': [
                    {
                        'From': 123,
                        'To': 123,
                        'Step': 123
                    },
                ],
                'StorageThroughputToIopsRatio': [
                    {
                        'From': 123.0,
                        'To': 123.0
                    },
                ]
            },
        ],
        'ValidProcessorFeatures': [
            {
                'Name': 'string',
                'DefaultValue': 'string',
                'AllowedValues': 'string'
            },
        ],
        'SupportsDedicatedLogVolume': True|False
    }
}