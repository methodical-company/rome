# Developers

You found yourself here usually because of either:

1. You want to developed a new plugin for Rome Bridge to eiter read from a feature store or you wish to connect a feature store to a Data Science Model.

or

2. You want to develop on the Rome Bridge Project or contribute your already written plugin to Rome Bridge.

## for those who want to build a plugin

You can easily develope insteall and run a plugin by simply inherting from `rome_bridge.feature_store.RomeBaseFeatureStore` class for Feature stores, or `rome_bridge.models.RomeBaseModel`.

Example:

```
>>> from rome_bridge.feature_store import RomeBaseFeatureStore

```

# for those who want to develope on Rome Bridge


## publishing the documentation

Once you can commit to gh-pages on https://github.com/methodical-company/rome-bridge project, you can run the command

```
mkdocs gh-deploy
```
That will deploy to the github pages site.

