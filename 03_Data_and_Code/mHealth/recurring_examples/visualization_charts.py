"""Build TikZ figures and a browser chart from verified aggregate tables."""

import json
import altair as alt
import pandas as pd
from common import OUTPUT, ROOT
from visualization import MONTHS

FIGURES = ROOT.parents[2] / "06_Lecture_Notes" / "figures"
BLUE, ORANGE = "#13294B", "#FF5F05"


def coordinates(x, y):
    return " ".join(f"({a:.8f},{b:.8f})" for a, b in zip(x, y))


def tikz_figures(monthly, cdf, result):
    FIGURES.mkdir(exist_ok=True)
    bars = r"""\begin{tikzpicture}
\begin{axis}[ybar,bar width=22pt,width=12.5cm,height=6.3cm,
 ymin=0,ymax=100,ylabel={Calendar Days With Logs (\%)},
 xtick={0,1},xticklabels={May,June},enlarge x limits=0.6,
 legend style={at={(0.5,-0.17)},anchor=north,legend columns=2,column sep=10pt},
 nodes near coords,point meta=y,
 every node near coord/.append style={font=\footnotesize,/pgf/number format/fixed,/pgf/number format/precision=1}]
\addplot[draw=IlliniBlue,fill=IlliniBlue!18] coordinates {ALL};
\addplot[draw=IlliniOrange,fill=IlliniOrange!18] coordinates {CONDITIONAL};
\legend{All eligible users,Users with logs that month}
\end{axis}
\end{tikzpicture}
"""
    bars = bars.replace("ALL", coordinates([0, 1], monthly.logging_percent))
    bars = bars.replace("CONDITIONAL", coordinates([0, 1], monthly.conditional_logging_percent))
    (FIGURES / "M02_logging_denominators.tex").write_text(bars)
    distribution = r"""\begin{tikzpicture}
\begin{axis}[width=12.5cm,height=6.5cm,xmin=0,xmax=100,ymin=0,ymax=100,
 xlabel={User's Calendar Days With Logs (\%)},ylabel={Users at or Below That Value (\%)},
 legend style={at={(0.03,0.97)},anchor=north west},grid=major]
"""
    for month, style in zip(MONTHS, ["IlliniBlue,solid", "IlliniOrange,dashed"]):
        part = cdf.loc[cdf.period.eq(month)]
        points = "(0,0) " + coordinates(part.logging_percent, part.cumulative_percent)
        distribution += rf"\addplot[{style},const plot] coordinates {{{points}}};" + "\n"
    distribution += "\\legend{May,June}\n\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M02_logging_distribution.tex").write_text(distribution)
    comparison = result["paired_change"]
    intervals = r"""\begin{tikzpicture}
\begin{axis}[width=11cm,height=5.5cm,xmin=-10,xmax=1,ymin=-0.6,ymax=1.6,
 xlabel={June Minus May (Percentage Points)},ytick={0,1},
 yticklabels={{Independent days (incorrect)},{Paired user bootstrap}},
 grid=major]
\addplot[Storm,dashed] coordinates {(0,-0.5) (0,1.5)};
"""
    for y, low, high, color in [
        (1, comparison["ci_low_pp"], comparison["ci_high_pp"], "IlliniBlue"),
        (0, comparison["naive_ci_low_pp"], comparison["naive_ci_high_pp"], "Storm"),
    ]:
        points = coordinates([low, high], [y, y])
        intervals += rf"\addplot[{color},very thick,mark=|,mark size=5pt] coordinates {{{points}}};" + "\n"
        intervals += rf"\addplot[{color},only marks,mark=*] coordinates {{({comparison['change_pp']:.8f},{y})}};" + "\n"
    intervals += "\\end{axis}\n\\end{tikzpicture}\n"
    (FIGURES / "M03_logging_uncertainty.tex").write_text(intervals)


def interactive_chart(monthly, cdf):
    records = []
    for row in monthly.to_dict(orient="records"):
        for population, users, denominator, value in [
            ("All eligible users", row["eligible_users"], row["calendar_user_days"], row["logging_percent"]),
            ("Users with logs", row["users_with_logs"], row["logger_calendar_days"], row["conditional_logging_percent"]),
        ]:
            records.append({"period": row["period"], "population": population,
                            "users": users, "calendar_days": denominator,
                            "observed_days": row["observed_user_days"], "percent": value})
    table = pd.DataFrame(records)
    month = alt.param(name="month", value=MONTHS[0],
                      bind=alt.binding_select(options=MONTHS, name="Month: "))
    bars = alt.Chart(table).transform_filter(alt.datum.period == month).mark_bar().encode(
        x=alt.X("population:N", title=None, axis=alt.Axis(labelAngle=0)),
        y=alt.Y("percent:Q", title="Calendar Days With Logs (%)", scale=alt.Scale(domain=[0, 100])),
        color=alt.Color("population:N", scale=alt.Scale(range=[BLUE, ORANGE]), legend=None),
        tooltip=[alt.Tooltip("population:N"), alt.Tooltip("percent:Q", format=".2f"),
                 "users:Q", "observed_days:Q", "calendar_days:Q"],
    ).properties(width=320, height=300, title="The Denominator Changes the Rate")
    curve = alt.Chart(cdf).transform_filter(alt.datum.period == month).mark_line(
        interpolate="step-after", color=BLUE
    ).encode(
        x=alt.X("logging_percent:Q", title="User's Days With Logs (%)", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("cumulative_percent:Q", title="Users at or Below (%)", scale=alt.Scale(domain=[0, 100])),
        order="logging_percent:Q",
        tooltip=[alt.Tooltip("logging_percent:Q", format=".2f"),
                 alt.Tooltip("cumulative_percent:Q", format=".2f"), "users_at_value:Q", "eligible_users:Q"],
    ).properties(width=320, height=300, title="Distribution Across All Eligible Users")
    chart = alt.hconcat(bars, curve).add_params(month).configure_axis(
        labelColor=BLUE, titleColor=BLUE, labelFontSize=12, titleFontSize=12
    ).configure_title(color=BLUE, fontSize=15).configure_view(stroke=None)
    chart.save(OUTPUT / "visualization_interactive.vl.json")
    html = chart.to_html(embed_options={"renderer": "svg", "actions": False})
    table_text = table.rename(columns={
        "period": "Month", "population": "Population", "users": "Users",
        "calendar_days": "Calendar User-Days", "observed_days": "Days With Logs",
        "percent": "Days With Logs (%)",
    }).to_html(index=False, float_format=lambda x: f"{x:.2f}", border=0)
    n = int(monthly.eligible_users.iloc[0])
    introduction = (
        "<main><h1>mHealth: Logging Coverage</h1><p>Marketing Analytics · By Nathan Yang</p>"
        f"<p>{n} users observed before May 2016. The left chart compares two denominators. "
        "The right chart retains every eligible user, including users with no recorded days. "
        "Change the month to inspect both views. Both axes retain the same scales.</p>"
    )
    description = (
        "<h2>Chart Data</h2><p>Calendar user-days equal users multiplied by days in the month. "
        "No logged day means no observed food entry, without implying zero consumption. "
        "These descriptive comparisons do not estimate a treatment effect.</p>"
        + table_text
        + "<p>Internet access is required to display the charts. "
        "The data table remains available offline.</p></main>"
    )
    css = """<style>body{font:16px system-ui;color:#13294B;max-width:1000px;margin:32px auto;padding:0 24px}
    h1{border-bottom:3px solid #FF5F05;padding-bottom:12px}p{line-height:1.55;max-width:850px}
    table{border-collapse:collapse;font-size:14px}td,th{padding:10px;border-bottom:1px solid #C6C7C6;text-align:right}
    #vis{max-width:100%;overflow-x:auto}th{background:#EEF1F5}select{font-size:16px;padding:6px}.vega-bindings{margin:15px 0}</style>"""
    html = html.replace("</head>", css + "</head>").replace("<body>", "<body>" + introduction)
    html = html.replace("</body>", description + "</body>")
    (OUTPUT / "visualization_interactive.html").write_text(html)


if __name__ == "__main__":
    monthly = pd.read_csv(OUTPUT / "visualization_monthly.csv")
    cdf = pd.read_csv(OUTPUT / "visualization_ecdf.csv")
    result = json.loads((OUTPUT / "visualization.json").read_text())
    pd.testing.assert_frame_equal(monthly, pd.DataFrame(result["months"]), check_dtype=False)
    assert cdf.groupby("period").users_at_value.sum().eq(result["paired_change"]["users"]).all()
    tikz_figures(monthly, cdf, result)
    interactive_chart(monthly, cdf)
    print("Built three TikZ figures, the Vega-Lite specification, and interactive HTML.")
