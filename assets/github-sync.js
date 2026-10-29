(() => {
  const snapshotUrl = new URL('github-data.json', document.currentScript.src);
  const formatDate = (value) => new Intl.DateTimeFormat('en-GB', {
    day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC',
  }).format(new Date(value));
  const validUrl = (value) => {
    const url = new URL(value);
    return url.origin === 'https://github.com' && /^\/ammar31mawassi\/[^/]+$/.test(url.pathname);
  };
  async function refresh() {
    const response = await fetch(snapshotUrl, { cache: 'no-cache' });
    if (!response.ok) throw new Error('GitHub snapshot unavailable; showing curated project information.');
    const data = await response.json();
    for (const card of document.querySelectorAll('[data-repo]')) {
      const repo = data.repositories.find((item) => item.name === card.dataset.repo);
      if (!repo || !validUrl(repo.url)) continue;
      const description = card.querySelector('.repo-description');
      if (description && repo.description) description.textContent = repo.description;
      card.querySelector('.repo-link').href = repo.url;
      const meta = card.querySelector('[data-github-meta]');
      meta.replaceChildren();
      if (repo.languages.length) meta.append(repo.languages.join(' / '));
      if (repo.pushedAt) {
        const time = document.createElement('time');
        time.setAttribute('datetime', repo.pushedAt);
        time.textContent = `Updated ${formatDate(repo.pushedAt)}`;
        if (meta.textContent) meta.append(' · ');
        meta.append(time);
      }
    }
    const list = document.querySelector('#activity-list');
    for (const repo of data.recent) {
      if (!validUrl(repo.url)) continue;
      const row = document.createElement('article');
      row.className = 'activity-row';
      const heading = document.createElement('h3');
      const link = document.createElement('a');
      link.href = `${repo.url}/commits`;
      link.textContent = repo.name;
      link.setAttribute('aria-label', `View recent commits for ${repo.name}`);
      heading.append(link);
      const description = document.createElement('p');
      description.textContent = repo.description || 'Explore the latest work on GitHub.';
      const time = document.createElement('time');
      time.setAttribute('datetime', repo.pushedAt);
      time.textContent = formatDate(repo.pushedAt);
      row.append(heading, description, time);
      list.append(row);
    }
    const status = document.querySelector('#sync-status');
    status.textContent = `Public activity · synced ${formatDate(data.generatedAt)}`;
    status.title = 'Refreshed hourly from GitHub. Scheduled runs may be delayed.';
    document.querySelector('#github-activity').hidden = !list.children.length;
  }
  // HTML contains the full project list even when the data request fails.
  refresh().catch((error) => console.warn(error.message));
})();
