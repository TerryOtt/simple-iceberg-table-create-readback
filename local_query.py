import boringcatalog
import pathlib
import polars
import pyiceberg.table


data_dir: str = "./data"
catalog_name: str = "local"
catalog_json: str = f"{data_dir}/catalogs/catalog_{catalog_name}.json"
iceberg_dir: str = f"{data_dir}/iceberg_table"


def _main() -> None:
    datapath: pathlib.Path = pathlib.Path(data_dir)
    if not datapath.exists() or not datapath.is_dir():
        raise RuntimeError("Need to run local_create before this script")

    iceberg_catalog: boringcatalog.BoringCatalog = boringcatalog.BoringCatalog(
        name        = catalog_name,
        warehouse   = iceberg_dir,
        uri         = catalog_json,
    )

    # Get iceberg table handle from catalog
    iceberg_table: pyiceberg.table.Table = iceberg_catalog.load_table("dataset_xyz_namespace.dataset_xyz_table")
    
    # Get a polars lazyframe (no data, just a plan to get data!) from PyIceberg table
    polars_lf: polars.LazyFrame = iceberg_table.to_polars()

    # Prove all the data is there if we need it -- collect() finalizes query plan and pulls data
    polars_fulldata_df: polars.DataFrame = polars_lf.collect()
    print(f"\nFull table data out of Iceberg:\n{polars_fulldata_df}")


if __name__ == "__main__":
    _main()

