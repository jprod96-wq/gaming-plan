/*
  Progress sync for tracker.html, rdr2.html and companion.html.
  All progress (localStorage keys below) is mirrored to one secret GitHub Gist, so phone and PC share it.
  Each device connects once with a GitHub token that only has the "gist" scope. The token stays on the device.
  Conflicts: last save wins (fine for one person switching devices).
*/
(function () {
  const PREFIXES = ["gamingTracker.", "rdr2Companion.", "companion.", "readingTracker."]; // what gets synced
  const K = { token: "gpSync.token", gist: "gpSync.gist", updated: "gpSync.updated", synced: "gpSync.syncedAt" };
  const FILE = "gaming-plan-sync.json";
  const API = "https://api.github.com";

  let applying = false, pushTimer = null, status = "off", lastError = "";

  const synced = key => PREFIXES.some(p => key.startsWith(p));
  const snapshot = () => Object.fromEntries(Object.keys(localStorage).filter(synced).map(k => [k, localStorage.getItem(k)]));
  const token = () => localStorage.getItem(K.token);
  const gh = (path, opts = {}) => fetch(API + path, {
    ...opts,
    headers: { Authorization: `Bearer ${token()}`, Accept: "application/vnd.github+json", ...(opts.headers || {}) },
  }).then(r => { if (!r.ok) throw new Error(`GitHub ${r.status}`); return r.json(); });

  // Notice every progress save the pages make, without changing their code
  const origSet = Storage.prototype.setItem;
  Storage.prototype.setItem = function (key, value) {
    origSet.call(this, key, value);
    if (this === localStorage && !applying && synced(key)) {
      origSet.call(localStorage, K.updated, String(Date.now()));
      schedulePush();
    }
  };

  function schedulePush() {
    if (!token()) return;
    clearTimeout(pushTimer);
    pushTimer = setTimeout(push, 2000);
  }

  async function push(keepalive = false) {
    if (!token() || !localStorage.getItem(K.gist)) return;
    clearTimeout(pushTimer);
    const body = { updatedAt: +localStorage.getItem(K.updated) || Date.now(), data: snapshot() };
    try {
      setStatus("syncing");
      await gh(`/gists/${localStorage.getItem(K.gist)}`, {
        method: "PATCH", keepalive,
        body: JSON.stringify({ files: { [FILE]: { content: JSON.stringify(body) } } }),
      });
      origSet.call(localStorage, K.synced, String(Date.now()));
      setStatus("ok");
    } catch (e) { fail(e); }
  }

  async function pull() {
    if (!token() || !localStorage.getItem(K.gist)) return;
    try {
      setStatus("syncing");
      const gist = await gh(`/gists/${localStorage.getItem(K.gist)}`);
      const remote = JSON.parse(gist.files[FILE]?.content || "{}");
      const localUpdated = +localStorage.getItem(K.updated) || 0;
      origSet.call(localStorage, K.synced, String(Date.now()));
      if ((remote.updatedAt || 0) > localUpdated) {
        apply(remote);
        location.reload(); // re-render the page with the newer progress
        return;
      }
      if (localUpdated > (remote.updatedAt || 0)) await push();
      setStatus("ok");
    } catch (e) { fail(e); }
  }

  function apply(remote) {
    applying = true;
    Object.keys(localStorage).filter(synced).forEach(k => { if (!(k in remote.data)) localStorage.removeItem(k); });
    Object.entries(remote.data || {}).forEach(([k, v]) => origSet.call(localStorage, k, v));
    origSet.call(localStorage, K.updated, String(remote.updatedAt));
    applying = false;
  }

  async function connect(newToken) {
    origSet.call(localStorage, K.token, newToken.trim());
    try {
      setStatus("syncing");
      // Reuse the sync gist if another device created it already; otherwise create it from this device
      const gists = await gh("/gists?per_page=100");
      const found = gists.find(g => g.files[FILE]);
      if (found) {
        origSet.call(localStorage, K.gist, found.id);
        origSet.call(localStorage, K.updated, "0"); // a newly connected device takes the cloud copy
        await pull();
      } else {
        const body = { updatedAt: Date.now(), data: snapshot() };
        const g = await gh("/gists", { method: "POST", body: JSON.stringify({
          description: "Gaming Plan progress sync", public: false,
          files: { [FILE]: { content: JSON.stringify(body) } },
        }) });
        origSet.call(localStorage, K.gist, g.id);
        origSet.call(localStorage, K.updated, String(body.updatedAt));
        setStatus("ok");
      }
    } catch (e) { localStorage.removeItem(K.token); fail(e); }
  }

  function disconnect() {
    [K.token, K.gist, K.synced].forEach(k => localStorage.removeItem(k));
    setStatus("off");
  }

  function fail(e) { lastError = e.message; setStatus("error"); }

  // ---------- Small UI: a button in the corner + a panel ----------
  const css = `
    .gps-btn { position: fixed; left: 14px; bottom: 14px; z-index: 20; font: 13px system-ui, "Segoe UI", sans-serif;
      background: var(--surface); color: var(--text-secondary); border: 1px solid var(--border); border-radius: 999px;
      padding: 6px 12px; cursor: pointer; box-shadow: 0 4px 16px rgba(0,0,0,.25); }
    .gps-panel { position: fixed; left: 14px; bottom: 56px; z-index: 20; width: min(340px, calc(100vw - 28px));
      background: var(--surface); color: var(--text-primary); border: 1px solid var(--border); border-radius: 12px;
      padding: 14px 16px; font: 14px/1.45 system-ui, "Segoe UI", sans-serif; box-shadow: 0 8px 30px rgba(0,0,0,.35); }
    .gps-panel[hidden] { display: none; }
    .gps-panel h3 { margin: 0 0 8px; font-size: 15px; }
    .gps-panel p { margin: 6px 0; color: var(--text-secondary); font-size: 13px; }
    .gps-panel input { width: 100%; box-sizing: border-box; font: inherit; padding: 7px 10px; margin: 6px 0; border-radius: 8px;
      border: 1px solid var(--border); background: var(--page); color: var(--text-primary); }
    .gps-panel button { font: inherit; cursor: pointer; border-radius: 8px; border: 1px solid var(--border);
      background: transparent; color: var(--text-primary); padding: 5px 12px; margin-right: 6px; }
    .gps-panel code { font-size: 12px; word-break: break-all; }
    @media (max-width: 760px) { /* phones: top-right, clear of the tracker's bottom nav */
      .gps-btn { left: auto; right: 12px; bottom: auto; top: calc(12px + env(safe-area-inset-top)); padding: 6px 11px; }
      .gps-panel { left: auto; right: 12px; bottom: auto; top: calc(56px + env(safe-area-inset-top)); }
    }`;
  const style = document.createElement("style"); style.textContent = css; document.head.appendChild(style);
  const btn = document.createElement("button"); btn.className = "gps-btn";
  const panel = document.createElement("div"); panel.className = "gps-panel"; panel.hidden = true;
  btn.onclick = () => { panel.hidden = !panel.hidden; renderPanel(); };
  document.addEventListener("DOMContentLoaded", () => { document.body.append(btn, panel); setStatus(status); });

  function setStatus(s) {
    status = s;
    const at = +localStorage.getItem(K.synced);
    const phone = matchMedia("(max-width: 760px)").matches;
    btn.textContent = phone ? { off: "☁ Off", syncing: "☁ …", error: "⚠ Sync", ok: "☁ ✓" }[s] : { off: "☁ Sync off", syncing: "☁ Syncing…", error: "⚠ Sync error",
      ok: "☁ Synced" + (at ? " " + new Date(at).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }) : "") }[s];
    if (!panel.hidden) renderPanel();
  }

  function renderPanel() {
    if (!token()) {
      panel.innerHTML = `<h3>☁ Sync this device</h3>
        <p>Paste your GitHub token (only the <b>gist</b> permission). Connect the device that has your progress first.</p>
        <input type="password" id="gps-token" placeholder="ghp_…" autocomplete="off">
        <button id="gps-connect">Connect</button>`;
      panel.querySelector("#gps-connect").onclick = () => connect(panel.querySelector("#gps-token").value);
    } else {
      panel.innerHTML = `<h3>☁ Sync is on</h3>
        <p>${status === "error" ? "⚠ Last sync failed: " + lastError + ". Check your connection or token." : "Progress is shared between your devices."}</p>
        <p>Last synced: ${localStorage.getItem(K.synced) ? new Date(+localStorage.getItem(K.synced)).toLocaleString() : "not yet"}</p>
        <p>Sync ID (for Claude): <code>${localStorage.getItem(K.gist) || "…"}</code></p>
        <button id="gps-now">Sync now</button><button id="gps-off">Disconnect</button>`;
      panel.querySelector("#gps-now").onclick = pull;
      panel.querySelector("#gps-off").onclick = disconnect;
    }
  }

  // Offline support / app install (sw.js); only works on the https site, not the local file
  if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js");

  // Pull when the page opens or comes back into view; push right away when leaving
  if (token()) pull();
  document.addEventListener("visibilitychange", () => {
    if (!token()) return;
    if (document.visibilityState === "visible") pull();
    else if (pushTimer) push(true);
  });
})();
