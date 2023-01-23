"""Provide several explorer utilities for navigating capabilities loaded into Rome Bridge

Example:
```
>>> from rome_bridge import explorer
>>> explore = explorer.RomeExplorer()
>>> explore.print_feature_store_description("RomeFeast")
RomeFeast

```

"""

from feature_stores.rome_feast import RomeFeast
from feature_stores import RomeBaseFeatureStore
from typing import Optional

class RomeExplorer:
    """
    Rome Explorer Class for finding and explaining Rome Feature Stores.

    ...

    Attributes
    ----------
    feature_stores : str 
       list of installed feature_stores


    Methods
    -------
    describe_feature_store(feature_store_name="feature_store"):
        prints information about the feature_stores


    """
    def __init__(self, additional_feature_stores: list[RomeBaseFeatureStore]=[] ) -> None:
        """__init__ for RomeExplorer

        Args:
            additional_feature_stores (list[RomeBaseFeatureStore], optional): additonal loaded feature stores. Defaults to [].
        """
        self.modules = [RomeFeast, ] 
        self.modules += additional_feature_stores

    def print_feature_store_description(self, feature_store_name: str) -> None:
        """Prints out a description of the Feature Store installed in Rome

        Args:
            feature_store_name (str): The Name of the Feature Store Class as a String

        Returns:
            None
        """
        out_str = feature_store_name 
        print(out_str)
