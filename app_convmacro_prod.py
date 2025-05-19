import streamlit as st
from typing import Dict, List

# ---------------------------------------------
# 1. Données nutritionnelles
# ---------------------------------------------
FOODS: Dict[str, Dict[str, float]] = {
    "Riz basmati (cru)":       {"kcal": 353, "glucides": 77.8, "proteines": 7.7,  "lipides": 0.8,  "ratio": 3.2, "categorie": "glucide"},
    "Riz complet (cru)":       {"kcal": 362, "glucides": 76.0, "proteines": 7.5,  "lipides": 2.2,  "ratio": 3.1, "categorie": "glucide"},
    "Pâtes complètes (crues)": {"kcal": 348, "glucides": 65.0, "proteines": 13.0, "lipides": 2.5,  "ratio": 2.5, "categorie": "glucide"},
    "Lentilles (crues)":       {"kcal": 352, "glucides": 63.4, "proteines": 24.6, "lipides": 1.1,  "ratio": 2.5, "categorie": "glucide"},
    "Patate douce (crue)":     {"kcal": 86,  "glucides": 20.1, "proteines": 1.6,  "lipides": 0.1,  "ratio": 2.5, "categorie": "glucide"},
    "Flocons d’avoine":        {"kcal": 367, "glucides": 58.7, "proteines": 13.5, "lipides": 7.0,  "ratio": 2.1, "categorie": "glucide"},
    "Pain complet":            {"kcal": 247, "glucides": 41.5, "proteines": 8.4,  "lipides": 2.1,  "ratio": 1.0, "categorie": "glucide"},
    "Pomme de terre (crue)":   {"kcal": 77,  "glucides": 17.5, "proteines": 2.0,  "lipides": 0.1,  "ratio": 1.5, "categorie": "glucide"},
    "Boulgour (cru)":          {"kcal": 342, "glucides": 76.5, "proteines": 12.3, "lipides": 1.3,  "ratio": 2.5, "categorie": "glucide"},
    "Quinoa (cru)":            {"kcal": 368, "glucides": 64.2, "proteines": 14.1, "lipides": 6.1,  "ratio": 2.5, "categorie": "glucide"},
    "Blanc de poulet (cru)":   {"kcal": 110, "glucides": 0.0,  "proteines": 23.5, "lipides": 1.2,  "ratio": 0.75,"categorie": "proteine"},
    "Escalope de dinde (crue)": {"kcal": 105, "glucides": 0.0,  "proteines": 24.0, "lipides": 1.0,  "ratio": 0.75,"categorie": "proteine"},
    "Steak haché 5% (cru)":    {"kcal": 133, "glucides": 0.0,  "proteines": 21.0, "lipides": 5.0,  "ratio": 0.8, "categorie": "proteine"},
    "Saumon (cru)":            {"kcal": 206, "glucides": 0.0,  "proteines": 20.0, "lipides": 13.0, "ratio": 0.85,"categorie": "proteine"},
    "Œuf entier (60g)":        {"kcal": 90,  "glucides": 0.6,  "proteines": 7.5,  "lipides": 6.5,  "ratio": 1.0, "categorie": "proteine"},
    "Tofu ferme nature":       {"kcal": 126, "glucides": 1.6,  "proteines": 13.0, "lipides": 7.7,  "ratio": 1.0, "categorie": "proteine"},
    "Cabillaud (cru)":         {"kcal": 82,  "glucides": 0.0,  "proteines": 18.1, "lipides": 0.7,  "ratio": 0.8, "categorie": "proteine"},
    "Thon en boîte (égoutté)": {"kcal": 169, "glucides": 0.0,  "proteines": 28.6, "lipides": 6.0,  "ratio": 1.0, "categorie": "proteine"},
    "Fromage blanc 0%":        {"kcal": 46,  "glucides": 3.6,  "proteines": 8.4,  "lipides": 0.2,  "ratio": 1.0, "categorie": "proteine"},
}

# ---------------------------------------------
# 2. Fonctions de calcul
# ---------------------------------------------

def calculer_equivalences(
    categorie: str,
    objectif: str,
    aliment_ref: str,
    quantite_cru: float,
    cuisson_huile: bool = False
) -> List[Dict[str, str]]:
    ref = FOODS[aliment_ref]
    if objectif == "glucides":
        cible = quantite_cru * ref["glucides"] / 100
    elif objectif == "proteines":
        cible = quantite_cru * ref["proteines"] / 100
    else:
        cible = quantite_cru * ref["kcal"] / 100

    résultats = []
    for nom, nutr in FOODS.items():
        if nutr["categorie"] != categorie:
            continue
        valeur_nutr = nutr[objectif]
        q_crue = 100 * cible / valeur_nutr if valeur_nutr else 0
        q_cuite = q_crue * nutr["ratio"]
        glucides = q_crue * nutr["glucides"] / 100
        prot_crues = q_crue * nutr["proteines"] / 100
        prot_cuites = (prot_crues / (q_cuite * nutr["proteines"] / 100) * 100) if q_cuite and nutr["proteines"] else 0
        lipides = q_crue * nutr["lipides"] / 100
        kcal = q_crue * nutr["kcal"] / 100

        if cuisson_huile:
            lipides += 10
            kcal += 90

        résultats.append({
            "nom": nom,
            "q_crue":    f"{q_crue:.1f}",
            "q_cuite":   f"{q_cuite:.1f}",
            "glucides":  f"{glucides:.1f}",
            "prot_cuites":f"{prot_cuites:.1f}",
            "lipides":   f"{lipides:.1f}",
            "kcal":      f"{kcal:.1f}",
        })
    return résultats


def calculer_dej(
    sexe: str,
    age: int,
    taille_cm: int,
    poids_kg: float,
    activite: float
) -> int:
    if sexe == "homme":
        mb = 10 * poids_kg + 6.25 * taille_cm - 5 * age + 5
    else:
        mb = 10 * poids_kg + 6.25 * taille_cm - 5 * age - 161
    return round(mb * activite)

# ---------------------------------------------
# 3. Configuration Streamlit
# ---------------------------------------------
st.set_page_config(
    page_title="Convertisseur Nutrition & DEJ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS pour cartes personnalisées
st.markdown(
    """
    <style>
    .card {
        background-color: #1e1e1e;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        color: #fafafa;
        margin-bottom: 16px;
    }
    .card h4 {
        margin: 0 0 8px 0;
        color: #29b6f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout en onglets
tab1, tab2 = st.tabs(["Convertisseur Nutrition", "Calculateur DEJ"])

with tab1:
    st.header("Convertisseur Nutrition")
    with st.sidebar:
        st.subheader("Paramètres")
        cat = st.selectbox(
            "Catégorie",
            options=[("glucide", "Glucides"), ("proteine", "Protéines")],
            format_func=lambda x: x[1]
        )[0]
        obj_opts = [("glucides", "Glucides"), ("kcal", "Calories")] if cat == "glucide" else [("proteines", "Protéines"), ("kcal", "Calories")]
        objectif = st.selectbox("Objectif", options=obj_opts, format_func=lambda x: x[1])[0]
        alim_ref = st.selectbox(
            "Aliment de référence",
            options=[nom for nom, nutr in FOODS.items() if nutr["categorie"] == cat]
        )
        quantite = st.number_input("Quantité (g cru)", min_value=0.0, value=100.0)
        huile = st.checkbox("Ajouter 1 c.à.s. d’huile (+90 kcal)")

    if st.button("Calculer équivalences", key="eqs_btn"):
        eqs = calculer_equivalences(cat, objectif, alim_ref, quantite, huile)
        cols = st.columns(2)
        for idx, eq in enumerate(eqs):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="card">
                    <h4>{eq['nom']}</h4>
                    <p><strong>Cru:</strong> {eq['q_crue']} g  &nbsp;&nbsp; <strong>Cuit:</strong> {eq['q_cuite']} g</p>
                    <p>Glucides: {eq['glucides']} g  |  Prot. cuites: {eq['prot_cuites']} g</p>
                    <p>Lipides: {eq['lipides']} g  |  kcal: {eq['kcal']} kcal</p>
                </div>
                """, unsafe_allow_html=True)

with tab2:
    st.header("Calculateur DEJ")
    with st.sidebar:
        st.subheader("Vos informations")
        sexe = st.selectbox("Sexe", options=[("homme", "Homme"), ("femme", "Femme")], format_func=lambda x: x[1])[0]
        age = st.number_input("Âge", min_value=0, value=25)
        taille = st.number_input("Taille (cm)", min_value=0, value=175)
        poids = st.number_input("Poids (kg)", min_value=0.0, value=70.0)
        ativs = [
            (1.2, "Sédentaire"), (1.375, "Légèrement actif"),
            (1.55, "Modérément actif"), (1.725, "Très actif"), (1.9, "Extrêmement actif")
        ]
        activite = st.selectbox("Activité", options=ativs, format_func=lambda x: x[1])[0]

    if st.button("Calculer ma DEJ", key="dej_btn"):
        dej = calculer_dej(sexe, age, taille, poids, activite)
        st.metric("✨ DEJ estimée (kcal)", dej)
