import boringcatalog
import shutil
import pathlib
import polars


data_dir = "./data/"
aws_region: str = "us-east-2"
iceberg_namespace: str = "dataset_xyz_namespace"
catalog_name: str = "aws_cat"
catalog_json: str = f"./data/catalogs/catalog_{catalog_name}.json"
iceberg_table_name: str = "dataset_xyz_table"
table_s3_bucket_name: str = "iceberg-demo.firsttracks.net"


def _main() -> None:
    
    data: dict[str, list[str | int]] = {
        "Fruit": ["Apple", "Apple", "Pear"],
        "Color": ["Red", "Yellow", "Green"],
        "Count": [2, 1, 1]
    }

    polars_df: polars.DataFrame = polars.DataFrame(data)

    print(f"\n{polars_df}")

    # Remove data dir if it exists
    datapath: pathlib.Path = pathlib.Path(data_dir)
    if datapath.exists() and datapath.is_dir():
        shutil.rmtree(datapath)

    iceberg_catalog: boringcatalog.BoringCatalog = boringcatalog.BoringCatalog(
        name        = catalog_name,
        **{
            "uri"       : catalog_json,
            "warehouse" : f"s3://{table_s3_bucket_name}",
            "s3.region" : aws_region,
        }
    )

    # Create namespace -- this is a catalog ONLY operation,
    #   nothing is created in warehouse dir
    iceberg_catalog.create_namespace_if_not_exists(iceberg_namespace)

    new_iceberg_table: pyiceberg.table.Table = iceberg_catalog.create_table(
        f"{iceberg_namespace}.{iceberg_table_name}",
        schema=polars_df.to_arrow().schema
    )

    polars_df.write_iceberg(new_iceberg_table, mode='append')

    print( "\n"
           "*********************************************************\n"
          f"BoringTable catalog  : {catalog_json}\n"
          f"Apache Iceberg table : s3://{table_s3_bucket_name}/{iceberg_namespace}\n"
          f"Dataset table        : s3://{table_s3_bucket_name}/{iceberg_namespace}/{iceberg_table_name}\n"
           "*********************************************************\n"
           "\n" )






if __name__ == "__main__":
    _main()
