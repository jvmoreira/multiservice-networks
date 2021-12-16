## Network Functions Framework

### Parameters

#### Policing
<details>
<summary>Token Bucket</summary>

```JSON
{
  "function": "token-bucket",
  "category": "policing",

  "rate": 50,
  "bucket_size": 100,
  "bucket_max_size": 200,
  "interval": 0.5,
  "client-interface": " ",
  "server-interface": " ",
  "debug": 1
}
```
</details>

<details>
<summary>One Rate Three Colors</summary>

```JSON
{
  "function": "one-rate-three-color",
  "category": "policing",

  "rate": 100,
  "bucketF_size": 1000,
  "bucketF_max_size": 2000,
  "bucketS_size": 2000,
  "bucketS_max_size": 4000,
  "interval": 1,
  "client-interface": " ",
  "server-interface": " ",
  "debug": 1,
}
```

if color-aware mode add:

```JSON
{
  "color_aware": 1,
  "ca_bucketF_size": 500,
  "ca_bucketF_max_size": 1000,
  "ca_bucketS_size": 800,
  "ca_bucketS_max_size": 1200,
  "ca_rate": 100
}
```

</details>

<details>
<summary>Two Rate Three Color</summary>

```JSON
{
  "function": "two-rate-three-color",
  "category": "policing",

  "rateF": 150,
  "rateS": 200,
  "bucketF_size": 2000,
  "bucketF_max_size": 2500,
  "bucketS_size": 1500,
  "bucketS_max_size": 3000,
  "interval": 1.0,
  "client-interface": " ",
  "server-interface": " ",
  "debug": 1,
}
```

if color-aware mode add:

```JSON
{
  "color_aware": 1,
  "ca_bucketF_size": 1000,
  "ca_bucketF_max_size": 1500,
  "ca_bucketS_size": 1500,
  "ca_bucketS_max_size": 3000,
  "ca_rateF": 200,
  "ca_rateS": 100
}
```
</details>

#### Shaping
<details>
<summary>Token Bucket</summary>

```JSON
{
  "function": "token-bucket",
  "category": "shaping",

  "rate": 50,
  "bucket_size": 100,
  "bucket_max_size": 200,
  "interval": 0.5,
  "queue_max_size": 25,
  "client-interface": " ",
  "server-interface": " ",
  "debug": 1
}
```
</details>

<details>
<summary>Leaky Bucket</summary>

```JSON
{
  "function": "leaky-bucket",
  "category": "shaping",

  "packets_to_release": 3,
  "bucket_max_size": 30,
  "interval": 0.3,
  "client-interface": " ",
  "server-interface": " ",
  "debug": 1
}
```
</details>
