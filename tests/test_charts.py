import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "charts"))
import kentigern_mpl as kn  # noqa: E402


def test_alias_resolution():
    assert kn.run_colour("o4b", "light") == kn.colour("green", "light") == kn.colour("cat-5", "light")
    assert kn.run_colour("o1", "dark") == kn.colour("red", "dark")
    assert kn.colour("grey") == kn.colour("cat-other")


def test_themes_differ():
    assert kn.colour("surface", "light") != kn.colour("surface", "dark")


def test_axis_label_uses_slash_not_brackets():
    assert kn.axis_label("Frequency", "Hz") == "Frequency / Hz"
    assert "[" not in kn.axis_label("Mass", "M")
    assert kn.axis_label("Redshift") == "Redshift"


def test_styles_load_and_apply_tokens():
    for theme in ("light", "dark"):
        kn.use(theme)
        fig, ax = plt.subplots()
        assert not ax.spines["top"].get_visible() and not ax.spines["right"].get_visible()
        assert matplotlib.colors.same_color(fig.get_facecolor(), kn.colour("surface", theme))
        plt.close(fig)


def test_example_renders(tmp_path):
    subprocess.run([sys.executable, str(ROOT / "charts/example.py"), str(tmp_path)], check=True)
    for theme in ("light", "dark"):
        assert (tmp_path / f"example-{theme}.png").stat().st_size > 10_000
