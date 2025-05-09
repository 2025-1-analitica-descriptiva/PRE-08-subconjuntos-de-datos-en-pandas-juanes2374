# %%
import pandas as pd  #  type: ignore

pd.set_option("display.notebook_repr_html", False)


# %%
# Carga del archivo desde un repo en GitHub
truck_events = pd.read_csv("../files/input/truck_event_text_partition.csv")

# Cabecera del archivo
truck_events.head()
