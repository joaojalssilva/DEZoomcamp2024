if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Rows with 0 passengers: ", data['passenger_count'].isin([0]).sum())
    print("Rows with 0 trip distance: ", data['trip_distance'].isin([0]).sum())

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.replace('(?=[A-Z])(?<=[a-z])', '_', regex=True)
                .str.lower()
             )

    print(data['vendor_id'].unique())
    print("vendor_id" in data.columns )
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, "There are rides with 0 passengers"
    assert output['trip_distance'].isin([0]).sum() == 0, "There are rides with 0 trip distance"
    assert ("vendor_id" in output.columns) == True, "There is no column named 'vendor_id'"
