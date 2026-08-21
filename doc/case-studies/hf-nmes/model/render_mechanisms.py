"""Render the four draft ProposedMechanisms converging on six_mwd (see
mechanisms.py) on top of the full model 4D graph, so the sparseness of each
pathway is visible at a glance — each mechanism gets its own edge color, and
edges that aren't part of any current mechanism are greyed out.

Usage:
    python render_mechanisms.py
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from mechanisms import build_six_mwd_mechanisms
from model_4d import build_claims, build_variables
from render_graph import _EXPOSURE_IDS, _OUTCOME_IDS, _node_style

OUT_DIR = Path(__file__).resolve().parent

_MECHANISM_COLORS = {
    "mechanism-six_mwd-peripheral": "#d62728",           # red
    "mechanism-six_mwd-cardiac": "#1f77b4",               # blue
    "mechanism-six_mwd-balance_gait": "#2ca02c",          # green
    "mechanism-six_mwd-mechanical_efficiency": "#9467bd",  # purple
}


def build_dot() -> str:
    variables = build_variables()
    claims = build_claims(variables)
    id_by_variable_id = {v.variable_id: node_id for node_id, v in variables.items()}
    mechanisms = build_six_mwd_mechanisms()

    # (cause_id, effect_id) -> list of mechanism_ids that include this edge
    edge_mechanisms: dict[tuple[str, str], list[str]] = {}
    for mechanism in mechanisms:
        for c in mechanism.pathway:
            key = (id_by_variable_id[c.cause.variable_id], id_by_variable_id[c.effect.variable_id])
            edge_mechanisms.setdefault(key, []).append(mechanism.mechanism_id)

    lines = [
        "digraph Model4D_Mechanisms {",
        "  rankdir=LR;",
        '  node [shape=box, fontname="Helvetica"];',
        '  edge [fontname="Helvetica"];',
    ]
    for node_id, variable in variables.items():
        label = variable.label.replace('"', '\\"')
        lines.append(f'  "{node_id}" [label="{label}", {_node_style(node_id)}];')

    for claim in claims:
        cause_id = id_by_variable_id[claim.cause.variable_id]
        effect_id = id_by_variable_id[claim.effect.variable_id]
        mech_ids = edge_mechanisms.get((cause_id, effect_id), [])
        if mech_ids:
            # one edge per mechanism sharing this pair, offset so overlaps are visible
            for mech_id in mech_ids:
                color = _MECHANISM_COLORS[mech_id]
                lines.append(f'  "{cause_id}" -> "{effect_id}" [color="{color}", penwidth=2.5];')
        else:
            lines.append(f'  "{cause_id}" -> "{effect_id}" [color="#cccccc"];')

    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    dot_text = build_dot()
    dot_path = OUT_DIR / "model4d_mechanisms.dot"
    dot_path.write_text(dot_text)
    print(f"Wrote {dot_path}")

    dot_bin = shutil.which("dot")
    if not dot_bin:
        print("Graphviz `dot` not found on PATH.")
        return
    for fmt in ("png", "svg"):
        out_path = OUT_DIR / f"model4d_mechanisms.{fmt}"
        subprocess.run([dot_bin, f"-T{fmt}", str(dot_path), "-o", str(out_path)], check=True)
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
