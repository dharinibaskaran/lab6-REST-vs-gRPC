| Method           | Local   | Same-Zone   | Different Region  |
|------------------|---------|-------------|-------------------|
| REST add         | 2.42    | 3.20        | 281.69            |
| gRPC add         | 0.77    | 0.70        | 138.54            |
| REST rawimg      | 4.50    | 14.51       | 1130.64           |
| gRPC rawimg      | 8.94    | 14.30       | 192.90            |
| REST dotproduct  | 2.95    | 3.49        | 283.37            |
| gRPC dotproduct  | 0.93    | 0.88        | 138.70            |
| REST jsonimg     | 37.23   | 46.87       | 1275.70           |
| gRPC jsonimg     | 28.03   | 28.72       | 305.01            |
| PING             | 5123    | 6124        | 28048             |
```

You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.