from django.db import models
import pandas as pd
# Create your models here.
class ex_obj:
    name: str
    price: int
    
class stock_cls:
    name: str
    full_name: str
    df: pd.DataFrame()