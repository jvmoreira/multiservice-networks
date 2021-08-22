## Network Functions Framework

### Parameters

#### Policing
- Token Bucket
  - rate
  - bucket_size
  - bucket_max_size
  - interval
  - interface
  - debug

- One Rate Three Colors
  - rate
  - bucketF_size
  - bucketF_max_size
  - bucketS_size
  - bucketS_max_size
  - interval
  - host_address
  - target_address

- Two Rate Three Color
  - rateF
  - rateS
  - bucketF_size
  - bucketF_max_size
  - bucketS_size
  - bucketS_max_size
  - interval
  - host_address
  - target_address

#### Shaping
- Token Bucket
  - rate
  - bucket_size
  - bucket_max_size
  - interval
  - queue_max_size
  - interface
  - debug

- Leaky Bucket
  - packets_to_release
  - bucket_max_size
  - interval
  - interface
  - debug
