# simple example

## The old way

This is using sklearn and [Feast](https://github.com/feast-dev/feast-gcp-driver-ranking-tutorial/blob/master/notebooks/Driver_Ranking_Tutorial.ipynb)

```python 


import feast
from joblib import dump
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load driver order data
orders = pd.read_csv("/content/feast-driver-ranking-tutorial/driver_orders.csv", sep="\t")
orders["event_timestamp"] = pd.to_datetime(orders["event_timestamp"])

# Connect to your feature store provider
fs = feast.FeatureStore(repo_path="/content/feast-driver-ranking-tutorial/driver_ranking")
        
# Retrieve training data from BigQuery
training_df = fs.get_historical_features(
    entity_df=orders,
    feature_refs=[
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:acc_rate",
        "driver_hourly_stats:avg_daily_trips",
    ],
).to_df()

print("----- Feature schema -----\n")
print(training_df.info())

print()
print("----- Example features -----\n")
print(training_df.head())

# Train model
target = "trip_completed"

reg = LinearRegression()
train_X = training_df[training_df.columns.drop(target).drop("event_timestamp")]
train_Y = training_df.loc[:, target]
reg.fit(train_X[sorted(train_X)], train_Y)

# Save model
dump(reg, "driver_model.bin")
```

## The Rome Bridge Way


```

import rome

# Load driver order data
orders = pd.read_csv("/content/feast-driver-ranking-tutorial/driver_orders.csv", sep="\t")
orders["event_timestamp"] = pd.to_datetime(orders["event_timestamp"])

fbstore = rome.bridge_feature_store("feast>=0.28")
fbmodel = rome.bridge_model("linear-regression==1.2.1")

df = fbstore.get(target=orders, feature_name_list=[ "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:acc_rate",
        "driver_hourly_stats:avg_daily_trips"])
fbmodel.set_target("trip_completed")
fbmodel.fit(fbstore)

fbmodel.dump("driver_model.bin")

```








```
