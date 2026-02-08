import boringcatalog
import shutil
import pathlib
import polars
import pyiceberg.table


data_dir: str = "./data"
catalog_name: str = "local"
catalog_json: str = f"{data_dir}/catalogs/catalog_{catalog_name}.json"
iceberg_dir: str = f"{data_dir}/iceberg_table"


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
        warehouse   = iceberg_dir,
        uri         = catalog_json,
    )

    # Create namespace -- this is a catalog ONLY operation,
    #   nothing is created in warehouse dir
    iceberg_catalog.create_namespace_if_not_exists("dataset_xyz_namespace")

    # Create table with required namespace identifier
    #
    #   NOTE: first operation that actually modifies Iceberg table directory structure
    #         creates dataset_xyz_namespace/dataset_xyz_table/metadata/[five digit zero padded version of this table]-[GUID].metadata.json"
    #
    # Only AFTER filesystem changes are all durably persisted to disk, THEN the catalog
    #       is updated. Iceberg operations are atomic, so catalog is only updated when
    #       we know FOR SURE all data is safely on disk
    #
    #       Catalog changes:
    #           - New table in "tables" section" with contents
    #               - Table namespace
    #               - Table's unique name within its namespace
    #               - Pointer to current (latest) metadata file
    #           
    new_iceberg_table: pyiceberg.table.Table = iceberg_catalog.create_table(
        "dataset_xyz_namespace.dataset_xyz_table", 
        schema=polars_df.to_arrow().schema
    )

    # Now write the contents of our Polars dataframe to our Iceberg table, 
    #       using our catalog handle so ACID guarantees are protected
    polars_df.write_iceberg(new_iceberg_table, mode='append')

    # data created (Parquet format)

    # Metadata updated with
    #   current table metadata version
    #   previous table metadata version

    print( "\n"
           "*********************************************************\n"
          f"BoringTable catalog  : {catalog_json}\n"
          f"Apache Iceberg table : {iceberg_dir}\n"
           "*********************************************************\n"
           "\n" )


if __name__ == "__main__":
    _main()
