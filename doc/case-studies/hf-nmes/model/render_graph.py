"""Render model 4D's Stage 1 domain objects (see model_4d.py) as a Graphviz
graph. Graphviz DOT is plain text with no Models4PT/DAGitty dependency; if
the `dot` command-line tool is installed, this also renders a PNG/SVG.

Usage:
    python render_graph.py            # writes model4d_graph.dot (+ .png/.svg if `dot` is found)
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from model_4d import build_claims, build_variables

OUT_DIR = Path(__file__).resolve().parent

# Node roles from the DAGitty source (model4d_dagitty.txt): exposures vs. outcomes.
_EXPOSURE_IDS = {"at", "es"}
_OUTCOME_IDS = {"six_mwd", "hrqol", "vo2_max"}


def _node_style(node_id: str) -> str:
    if node_id in _EXPOSURE_IDS:
        return 'style=filled,fillcolor="#ffd9a8"'  # exposures (AT, ES)
    if node_id in _OUTCOME_IDS:
        return 'style=filled,fillcolor="#a8d5ff"'  # outcomes
    return 'style=filled,fillcolor="#eeeeee"'


def build_dot() -> str:
    variables = build_variables()
    claims = build_claims(variables)

    id_by_variable_id = {v.variable_id: node_id for node_id, v in variables.items()}

    lines = [
        "digraph Model4D {",
        '  rankdir=LR;',
        '  node [shape=box, fontname="Helvetica"];',
        '  edge [fontname="Helvetica"];',
    ]
    for node_id, variable in variables.items():
        label = variable.label.replace('"', '\\"')
        lines.append(f'  "{node_id}" [label="{label}", {_node_style(node_id)}];')
    for claim in claims:
        cause_id = id_by_variable_id[claim.cause.variable_id]
        effect_id = id_by_variable_id[claim.effect.variable_id]
        lines.append(f'  "{cause_id}" -> "{effect_id}";')
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    dot_text = build_dot()
    dot_path = OUT_DIR / "model4d_graph.dot"
    dot_path.write_text(dot_text)
    print(f"Wrote {dot_path}")

    dot_bin = shutil.which("dot")
    if not dot_bin:
        print("Graphviz `dot` not found on PATH — install it to render an image "
              "(e.g. `brew install graphviz`), or paste the .dot file into an "
              "online Graphviz viewer.")
        return

    for fmt in ("png", "svg"):
        out_path = OUT_DIR / f"model4d_graph.{fmt}"
        subprocess.run([dot_bin, f"-T{fmt}", str(dot_path), "-o", str(out_path)], check=True)
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
