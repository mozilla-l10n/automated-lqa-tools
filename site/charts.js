/* The landing page's charts, drawn with Chart.js from bot.json: the
 * suggestion bot's two, and the findings raised and fixed per week.
 *
 * Loaded by app.js only when the landing page is shown, after
 * vendor/chart.umd.min.js. Colours come from style.css's custom properties,
 * so light and dark mode stay defined in one place; the charts are redrawn
 * when the colour scheme changes.
 */
"use strict";

(function () {
  let data = null;
  const live = [];

  const css = (name) =>
    getComputedStyle(document.documentElement).getPropertyValue(name).trim();

  const weekLabel = (iso) =>
    new Date(`${iso}T00:00:00`).toLocaleDateString("en", { month: "short", day: "numeric" });

  const OUTCOMES = [
    ["approved", "Approved"],
    ["rejected", "Rejected"],
    ["pending", "Awaiting review"],
  ];

  // The highest non-empty segment of a week's stack: it alone gets the
  // rounded data end, and every segment under it a 2px surface gap on top.
  function topmost(index) {
    for (let i = OUTCOMES.length - 1; i >= 0; i--) {
      if (data[OUTCOMES[i][0]][index]) return i;
    }
    return -1;
  }

  function common(c) {
    return {
      responsive: true,
      maintainAspectRatio: true,
      aspectRatio: 2.4,
      animation: false,
      interaction: { mode: "index", intersect: false },
      plugins: {
        legend: {
          position: "top",
          align: "start",
          labels: { color: c.muted, boxWidth: 12, boxHeight: 12, useBorderRadius: true, borderRadius: 2 },
        },
        tooltip: {
          footerFont: { weight: "normal" },
          callbacks: {
            title: (items) => `Week of ${data.weeks[items[0].dataIndex]}`,
            footer: (items) => `${data.sent[items[0].dataIndex]} sent`,
          },
        },
      },
      scales: {
        x: {
          grid: { display: false },
          border: { color: c.axis },
          ticks: { color: c.tick },
        },
        y: {
          beginAtZero: true,
          grid: { color: c.grid },
          border: { display: false },
          ticks: { color: c.tick },
        },
      },
    };
  }

  function sentChart(canvas, c) {
    const options = common(c);
    options.scales.x.stacked = true;
    options.scales.y.stacked = true;
    options.scales.y.ticks.precision = 0;
    return new Chart(canvas, {
      type: "bar",
      data: {
        labels: data.weeks.map(weekLabel),
        datasets: OUTCOMES.map(([key, label], i) => ({
          label,
          data: data[key],
          backgroundColor: c[key],
          maxBarThickness: 24,
          borderSkipped: "start",
          borderColor: c.surface,
          borderWidth: (ctx) => ({ top: i < topmost(ctx.dataIndex) ? 2 : 0 }),
          borderRadius: (ctx) =>
            i === topmost(ctx.dataIndex) ? { topLeft: 4, topRight: 4 } : 0,
        })),
      },
      options,
    });
  }

  function rateChart(canvas, c) {
    const options = common(c);
    // Weeks centred in their band, as in the bar chart above, so the two
    // read as one timeline.
    options.scales.x.offset = true;
    options.scales.y.max = 100;
    options.scales.y.ticks.stepSize = 25;
    options.scales.y.ticks.callback = (v) => `${v}%`;
    options.plugins.tooltip.callbacks.label = (item) => {
      const key = item.datasetIndex ? "rejected" : "approved";
      const i = item.dataIndex;
      return ` ${item.dataset.label}: ${Math.round(item.raw)}% (${data[key][i]} of ${data.sent[i]})`;
    };
    const line = (label, key, values) => ({
      label,
      data: values,
      borderColor: c[key],
      backgroundColor: c[key],
      borderWidth: 2,
      pointRadius: 4,
      pointHoverRadius: 6,
      pointBorderColor: c.surface,
      pointBorderWidth: 2,
      // A week with nothing sent has no rate: leave a gap there.
      spanGaps: false,
    });
    return new Chart(canvas, {
      type: "line",
      data: {
        labels: data.weeks.map(weekLabel),
        datasets: [
          line("Acceptance rate", "approved", data.acceptance),
          line("Rejection rate", "rejected", data.rejection),
        ],
      },
      options,
    });
  }

  function findingsChart(canvas, c) {
    const f = data.findings;
    const options = common(c);
    options.scales.y.ticks.precision = 0;
    options.plugins.tooltip.callbacks = {
      title: (items) => `Week of ${f.weeks[items[0].dataIndex]}`,
    };
    const bars = (label, key) => ({
      label,
      data: f[key],
      backgroundColor: c[key],
      maxBarThickness: 16,
      // A 2px surface gap between the week's two bars.
      borderColor: c.surface,
      borderWidth: { left: 1, right: 1 },
      borderSkipped: "start",
      borderRadius: { topLeft: 4, topRight: 4 },
    });
    return new Chart(canvas, {
      type: "bar",
      data: {
        labels: f.weeks.map(weekLabel),
        datasets: [bars("Raised", "raised"), bars("Fixed", "fixed")],
      },
      options,
    });
  }

  function draw() {
    while (live.length) live.pop().destroy();
    if (!data) return;
    const sent = document.getElementById("chart-sent");
    const rate = document.getElementById("chart-rate");
    const findings = document.getElementById("chart-findings");
    const c = {
      approved: css("--approved"), rejected: css("--rejected"), pending: css("--pending"),
      raised: css("--raised"), fixed: css("--fixed"),
      surface: css("--bg"), muted: css("--muted"), tick: css("--tick"),
      grid: css("--grid"), axis: css("--axis"),
    };
    Chart.defaults.font.family = 'system-ui, -apple-system, "Segoe UI", sans-serif';
    Chart.defaults.color = c.muted;
    // The bot's charts are absent until a suggestion has been sent, and the
    // findings chart until a finding has been recorded.
    if (sent && rate) live.push(sentChart(sent, c), rateChart(rate, c));
    if (findings && data.findings) live.push(findingsChart(findings, c));
  }

  window.drawBotCharts = async function () {
    if (!data) {
      const res = await fetch("bot.json");
      if (!res.ok) throw new Error(`${res.status}`);
      data = await res.json();
    }
    draw();
  };

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", draw);
})();
