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
  - interface
  - debug
  - color_aware
  - Se color_aware for 1 necessário os parâmetros abaixo
  - ca_rate
  - ca_bucketF_size
  - ca_bucketF_max_size
  - ca_bucketS_size
  - ca_bucketS_max_size


- Two Rate Three Color
  - rateF
  - rateS
  - bucketF_size
  - bucketF_max_size
  - bucketS_size
  - bucketS_max_size
  - interval
  - interface
  - debug
  - color_aware
  - Se color_aware for 1 necessário os parâmetros abaixo
  - ca_rateF
  - ca_rateS
  - ca_bucketF_size
  - ca_bucketF_max_size
  - ca_bucketS_size
  - ca_bucketS_max_size

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
