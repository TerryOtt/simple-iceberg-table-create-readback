# Local Iceberg Demo

## Summary 

Simplest way I could think to show how to create, read, and write data to.from
an Apache Iceberg table in Python.

This demo uses [Boring Catalog](https://github.com/boringdata/boring-catalog) for its 
[Iceberg Catalog](https://medium.com/itversity/iceberg-catalogs-a-guide-for-data-engineers-a6190c7bf381).
Boring Catalog is dead-simple, consisting of a single JSON file for all its state. Full stop.
As we are aiming for _simple_, Boring Catalog is all that's needed. No need to launch other software 
like Hive MetaStore or create a hosted Iceberg catalog using a cloud provider, as with AWS Glue.

[create_local_iceberg_table.py](https://github.com/TerryOtt/simple-iceberg-table-create-readback/blob/main/create_local_iceberg_table.py)
creates an Iceberg table using Boring and writes a trivial Polars DataFrame (three rows) to it.

Going the other direction, 
[query_local_iceberg_table.py](https://github.com/TerryOtt/simple-iceberg-table-create-readback/blob/main/query_local_iceberg_table.py) 
uses Boring and Polars to query data from the Iceberg table into a Polars DataFrame.


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

