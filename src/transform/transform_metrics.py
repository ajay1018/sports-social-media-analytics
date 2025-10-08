from pathlib import Path
import pandas as pd, json

RAW = Path("data/raw")
PROC = Path("data/processed"); PROC.mkdir(parents=True, exist_ok=True)

posts = json.loads((RAW/"posts.json").read_text(encoding="utf-8"))
df = pd.DataFrame(posts)
df["engagement"] = df["likes"] + df["retweets"] + df["replies"]

# per-team summary
team_metrics = df.groupby(["league","team"], as_index=False)["engagement"].sum().sort_values("engagement", ascending=False)
team_metrics.to_csv(PROC/"team_metrics.csv", index=False)

# per-league summary
league_metrics = df.groupby("league", as_index=False)["engagement"].sum().sort_values("engagement", ascending=False)
league_metrics.to_csv(PROC/"league_metrics.csv", index=False)

df.to_csv(PROC/"posts_enriched.csv", index=False)
print("[transform] wrote:", PROC/"team_metrics.csv", "and", PROC/"league_metrics.csv")
