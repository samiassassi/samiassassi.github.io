"""One-off: build the simplified northern-Algeria wilaya map used on the Research page.

Run with any Python that has geopandas (e.g. D:/north_africa_3d/.venv):
    D:/north_africa_3d/.venv/Scripts/python.exe tools/make_map.py
Writes assets/map.json  ->  {"w": width, "h": height, "wilayas": [{"n": name, "d": svgpath, "c": [x, y]}]}
Source: FEWS NET DZ_Admin1_2021 (48 wilayas).
"""
import json
import math
from pathlib import Path

import geopandas as gpd
from shapely.geometry import box

ROOT = Path(__file__).resolve().parents[1]
SRC = r"D:/ALG_ENSA crop diversity mapping/DZ_Admin_2021/DZ_Admin1_2021.shp"

W_LON, E_LON, S_LAT, N_LAT = -2.4, 9.4, 30.6, 38.0   # northern Algeria window
SCALE = 82                                           # px per degree latitude
KX = math.cos(math.radians(34))

g = gpd.read_file(SRC).to_crs(4326)
g["geometry"] = g.geometry.intersection(box(W_LON, S_LAT, E_LON, N_LAT)).simplify(0.018, preserve_topology=True)
g = g[~g.geometry.is_empty]

w = round((E_LON - W_LON) * KX * SCALE)
h = round((N_LAT - S_LAT) * SCALE)


def xy(lon, lat):
    return round((lon - W_LON) * KX * SCALE, 1), round((N_LAT - lat) * SCALE, 1)


def ring(coords):
    pts = [xy(*c[:2]) for c in coords]
    return "M" + "L".join(f"{x},{y}" for x, y in pts) + "Z"


out = []
for _, r in g.iterrows():
    geom = r.geometry
    polys = [geom] if geom.geom_type == "Polygon" else [p for p in getattr(geom, "geoms", []) if p.geom_type == "Polygon"]
    d = "".join(ring(p.exterior.coords) for p in polys if p.area > 0.002)
    if not d:
        continue
    c = r.geometry.representative_point()
    out.append({"n": r["ADMIN1"], "d": d, "c": list(xy(c.x, c.y))})

a0 = gpd.read_file(SRC.replace("Admin1", "Admin0")).to_crs(4326)
a0 = a0.geometry.union_all().intersection(box(W_LON, S_LAT, E_LON, N_LAT)).simplify(0.012, preserve_topology=True)
polys0 = [a0] if a0.geom_type == "Polygon" else [p for p in a0.geoms if p.geom_type == "Polygon"]
outline = "".join(ring(p.exterior.coords) for p in polys0 if p.area > 0.002)

(ROOT / "assets" / "map.json").write_text(json.dumps({"w": w, "h": h, "px_per_km": round(SCALE / 111.32, 4), "proj": {"w_lon": W_LON, "n_lat": N_LAT, "s_lat": S_LAT, "e_lon": E_LON, "kx": KX, "scale": SCALE}, "outline": outline, "wilayas": out}, ensure_ascii=False), encoding="utf-8")
print(w, h, len(out), sorted(o["n"] for o in out))
