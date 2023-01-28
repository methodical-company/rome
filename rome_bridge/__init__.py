from .explorer import RomeExplorer
from .feature_stores import RomeBaseFeatureStore
from .models import RomeBaseModel

ROME_EXPLORER = RomeExplorer()

def bridge_feature_store(feature_store_name: str, explorer=ROME_EXPLORER) -> RomeBaseFeatureStore:
    """bridge the feature store

        Args:
            feature_store_name (str): The Name of the Feature Store Class as a String
            explorer (RomeExplorer): if not provided the default global explorer is used

        Returns:
            RomeBaseFeatureStore
    """


def bridge_model(model_name: str, explorer=ROME_EXPLORER) -> RomeBaseModel:
    """bridge the model

        Args:
            model_name (str): The Name of the Feature Store Class as a String
            explorer (RomeExplorer): if not provided the default global explorer is used

        Returns:
            RomeBaseModel
    """
