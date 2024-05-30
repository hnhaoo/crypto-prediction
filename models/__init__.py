from .random_forest import RandomForest
from .orbit import Orbit
from .prophet import MyProphet
from .xgboost import MyXGboost


MODELS = {'random_forest': RandomForest,
          'orbit': Orbit,
          'prophet': MyProphet,
          'xgboost': MyXGboost,
          }
