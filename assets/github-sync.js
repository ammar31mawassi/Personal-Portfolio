(() => {
  const snapshotUrl = new URL("github-data.json", document.currentScript.src);
  const date = (value) => new Intl.DateTimeFormat("en", {
    day: "numeric", month: "short", year: "numeric", timeZone: "UTC",
  }).format(new Date(value));

  function metadata(repo) {
    const paragraph = document.createElement("p");
    paragraph.className = "github-meta";
    paragraph.textContent = repo.languages.join(" · ");
    if (repo.pushedAt) {
      const time = document.createElement("time");
      time.dateTime = repo.pushedAt;
      time.textContent = `Last push ${date(repo.pushedAt)}`;
      if (paragraph.textContent) paragraph.append(" · ");
      paragraph.append(time);
    }
    return paragraph;
  }

  async function refresh() {
    const response = await fetch(snapshotUrl, { cache: "no-cache" });
    if (!response.ok) throw new Error("GitHub snapshot unavailable");
    const data = await response.json();
    for (const card of document.querySelectorAll(".repo-card, details.project-feature")) {
      const link = card.querySelector('a[href^="https://github.com/ammar31mawassi/"]');
      const repo = data.repositories.find((item) => item.url === link?.href.replace(/\/$/, ""));
      if (!repo) continue;
      const description = card.querySelector("summary p") || card.querySelector("div > p");
      if (description && repo.description) description.textContent = repo.description;
      link.href = repo.url;
      const target = card.querySelector("summary > div") || card.querySelector("div");
      target.append(metadata(repo));
    }

    const section = document.createElement("section");
    section.id = "github-activity";
    const heading = document.createElement("div");
    heading.className = "section-heading";
    const title = document.createElement("h2");
    title.textContent = "Latest on GitHub";
    const note = document.createElement("p");
    note.textContent = `Recent pushes to public repositories. Synced ${date(data.generatedAt)}; refreshed hourly.`;
    heading.append(title, note);
    const grid = document.createElement("div");
    grid.className = "projects-grid";
    for (const repo of data.recent) {
      const card = document.createElement("article");
      card.className = "repo-card";
      const content = document.createElement("div");
      const name = document.createElement("h3");
      name.textContent = repo.name;
      const description = document.createElement("p");
      description.textContent = repo.description || "Explore this project on GitHub.";
      content.append(name, description, metadata({ ...repo, languages: [] }));
      const link = document.createElement("a");
      link.className = "repo-link";
      link.href = `${repo.url}/commits`;
      link.textContent = "View commits";
      link.setAttribute("aria-label", `View commits for ${repo.name}`);
      card.append(content, link);
      grid.append(card);
    }
    section.append(heading, grid);
    document.querySelector("#contact").before(section);
  }

  // The original, curated HTML stays usable if the snapshot cannot be loaded.
  refresh().catch((error) => console.warn(error.message));
})();
