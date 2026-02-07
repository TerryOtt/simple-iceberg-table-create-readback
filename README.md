# Local Iceberg Demo

## Summary 

Simplest way I could think to show how to create, read, and write data to.from
an Apache Iceberg table in Python.

_Note_: This demo uses [Boring Catalog|https://github.com/boringdata/boring-catalog] for
its Iceberg Catalog. Boring Catalog is dead-simple system using a single JSON file, 
which is all we want for a proof of concept. No need to start Hive MetaStore or use 
AWS Glue's Data Catalog and make network connections.

Once we have an Iceberg Catalog, 
[create_local_iceberg_table.py|https:///blob/main/create_local_iceberg_table.py] 
creats an Iceberg table and writes a three-row Polars DataFrame to it.

Going the other direction, 
[query_local_iceberg_table.py|https:///query_local_icevberg_table.py] read data from
the Iceberg table into a Polars DataFrame.


## Create An Iceberg Table

```
$ uv run create_local_iceberg_table.py
Using CPython 3.12.3 interpreter at: /usr/bin/python3.12
Creating virtual environment at: .venv
Installed 46 packages in 24ms
shape: (3, 3)
┌───────┬────────┬───────┐
│ Fruit ┆ Color  ┆ Count │
│ ---   ┆ ---    ┆ ---   │
│ str   ┆ str    ┆ i64   │
╞═══════╪════════╪═══════╡
│ Apple ┆ Red    ┆ 2     │
│ Apple ┆ Yellow ┆ 1     │
│ Pear  ┆ Green  ┆ 1     │
└───────┴────────┴───────┘
Apache Iceberg table created in ./iceberg_table

$
```

## Query Data From An Iceberg Table

```
$ uv run query_local_iceberg_table.py

Full table data out of Iceberg:
shape: (3, 3)
┌───────┬────────┬───────┐
│ Fruit ┆ Color  ┆ Count │
│ ---   ┆ ---    ┆ ---   │
│ str   ┆ str    ┆ i64   │
╞═══════╪════════╪═══════╡
│ Apple ┆ Red    ┆ 2     │
│ Apple ┆ Yellow ┆ 1     │
│ Pear  ┆ Green  ┆ 1     │
└───────┴────────┴───────┘

$
```

