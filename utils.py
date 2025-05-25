import pandas as pd

# Descargar base de gatos de kaggle
"""
['Breed', 
'Age_in_years', 
'Age_in_months', 
'Gender',
'Neutered_or_spayed', 
'Body_length', 
'Weight', 
'Fur_colour_dominant',
'Fur_pattern', 
'Eye_colour', 
'Allowed_outdoor', 
'Preferred_food',
'Owner_play_time_minutes', 
'Sleep_time_hours', 
'Country', 
'Latitude',
'Longitude']
"""
def fromKaggle():
    import kagglehub
    # Download latest version
    path = kagglehub.dataset_download("joannanplkrk/its-raining-cats")
    print("Path to dataset files:", path)
    df = pd.read_csv(f"{path}/cat_breeds_clean.csv", sep=';')
    df.to_excel("gatos.xlsx", index=False)
    df = df[["Breed","Age_in_months","Gender","Body_length","Weight","Fur_colour_dominant","Fur_pattern",
             "Eye_colour","Sleep_time_hours","Country"]]
    df.rename(columns={"Breed":"Raza","Age_in_months":"Edad Meses",
                       "Gender":"Sexo","Body_length":"Longitud Cuerpo",
                       "Weight":"Peso","Fur_colour_dominant":"Color Pelaje",
                       "Fur_pattern":"Patron Pelaje","Eye_colour":"Color Ojos",
                       "Sleep_time_hours":"Horas Sueño","Country":"Pais"}, inplace=True)
    df = df.dropna().drop_duplicates()
    df.to_excel("gatos_clean.xlsx", index=False)
    return df

# Importar datos de Excel
def import_data():
    df = pd.read_excel(f"gatos_clean.xlsx")
    return df

# Importar datos
# def deprecated_importar_datos():
    df = pd.read_csv("datos.csv").dropna().drop_duplicates()
    df["age_range"] = pd.cut(df["age"],bins=[18,40,69],labels=["Menor a 40","Mayor a 40"])
    minima_altura = df["height"].min()
    maxima_altura = df["height"].max()
    df["height_range"] = pd.cut(df["height"],
                                bins=[minima_altura,170,maxima_altura],
                                labels=["Menor a 1,70","Mayor a 1,70"])
    return df