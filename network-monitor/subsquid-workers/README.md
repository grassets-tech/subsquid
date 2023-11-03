# Subsquid workers (monitor)
![271806613-cfb9fbce-5959-41c7-b7dd-69e8c95bf08a](https://github.com/grassets-tech/subsquid/assets/82155440/55f5d87e-fd55-46ab-a184-15e0bb7835e7)

## Quick worker nodes dashboard

Usage:
 - Supports macOS only.
   
```
subsquid_workers -w <worker_id_1> <worker_id_2>
```

Output:

Workers status:
```
Fetching chunks...

WORKERS STATUS
+-------------+---------+----------------------------+--------+----------------+----------------+---------------+---------------+
|      worker | version |                  last ping | stored | a chunks count | d chunks count | a chunks size | d chunks size |
+-------------+---------+----------------------------+--------+----------------+----------------+---------------+---------------+
| 12D3***QPco |   0.1.4 | 2023-11-03T10:46:41.888000 |   128G |            480 |            480 |          128G |          128G |
| 12D3***rDeV |   0.1.4 | 2023-11-03T10:46:46.136000 |   127G |            470 |            470 |          127G |          127G |
+-------------+---------+----------------------------+--------+----------------+----------------+---------------+---------------+
Total workers: 151
```

Workers uptime:
```
WORKERS UPTIME (MY WORKERS)
+----+-------------+--------+--------+-------+
|  # |        node | uptime | online | local |
+----+-------------+--------+--------+-------+
| 27 | 12D3***QPco |  99.85 |     up |     * |
+----+-------------+--------+--------+-------+

WORKERS UPTIME (ALL WORKERS)
+-----+-------------+--------+--------+-------+
|   # |        node | uptime | online | local |
+-----+-------------+--------+--------+-------+
|   1 | 12D3***5Eq1 |  99.90 |     up |       |
|   2 | 12D3***ZRXp |  99.90 |     up |       |
|   3 | 12D3***tMs3 |  99.90 |     up |       |
|   4 | 12D3***cYN4 |  99.90 |     up |       |
|   5 | 12D3***aRgA |  99.90 |     up |       |
|   6 | 12D3***1gPT |  99.90 |     up |       |
```
