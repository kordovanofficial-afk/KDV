(() => {
  if (document.getElementById("kv-rail")) return;
  const TEAM = [
    ["ceo", "Claude", "CEO", "Runs the team, routes your asks, morning brief"],
    ["cqro", "Hamna", "Quality", "Fact-checks everything before it reaches you"],
    ["chro", "Noor", "People", "Hiring and reviewing agents"],
    ["cro", "Sana", "Revenue", "Meta ads, offers, sales, conversion"],
    ["cmo", "Omar", "Marketing", "Content, creatives, captions, SEO"],
    ["creative", "Creative Dir.", "Video ads", "Video ad production (under Omar)"],
    ["coo", "Zain", "Operations", "Stock, workshop, PostEx, store report"],
    ["cfo", "Ayesha", "Finance", "Real margins, cash, discount floor"],
  ];
  const rail = document.createElement("aside");
  rail.id = "kv-rail"; rail.setAttribute("aria-label", "Kordovan team");
  const h = document.createElement("div"); h.className = "kv-h"; h.textContent = "Team"; rail.append(h);
  let tip = null;
  const hideTip = () => { if (tip) { tip.remove(); tip = null; } };
  for (const [seat, name, role, does] of TEAM) {
    const b = document.createElement("button"); b.className = "kv-p"; b.type = "button";
    b.title = ""; b.setAttribute("aria-label", name + ", " + role + ". Click to address them in the chat.");
    const img = document.createElement("img"); img.alt = ""; img.src = chrome.runtime.getURL("icons/" + seat + ".png");
    const n = document.createElement("span"); n.className = "kv-n"; n.textContent = name;
    const s = document.createElement("span"); s.className = "kv-s"; s.textContent = role;
    b.append(img, n, s);
    b.addEventListener("mouseenter", () => {
      hideTip(); tip = document.createElement("div"); tip.id = "kv-tip";
      const t = document.createElement("b"); t.textContent = name + " · " + role;
      const d = document.createElement("div"); d.textContent = does;
      const k = document.createElement("small"); k.textContent = "Click to start a message to " + name.split(" ")[0];
      tip.append(t, d, k); document.body.append(tip);
      const r = b.getBoundingClientRect(); tip.style.top = Math.max(8, Math.min(innerHeight - tip.offsetHeight - 8, r.top)) + "px";
    });
    b.addEventListener("mouseleave", hideTip);
    b.addEventListener("click", () => address(name.split(" ")[0] === "Creative" ? "Creative Director" : name));
    rail.append(b);
  }
  const x = document.createElement("button"); x.className = "kv-x"; x.type = "button";
  const setMin = m => { rail.classList.toggle("kv-min", m); x.textContent = m ? "◀" : "hide ▶"; x.setAttribute("aria-label", m ? "Show team" : "Hide team"); try { localStorage.setItem("kv-rail-min", m ? "1" : "0"); } catch (e) {} };
  x.addEventListener("click", () => setMin(!rail.classList.contains("kv-min")));
  rail.append(x);
  let min = false; try { min = localStorage.getItem("kv-rail-min") === "1"; } catch (e) {}
  setMin(min);
  document.body.append(rail);

  function address(name) {
    const box = document.querySelector('[contenteditable="true"][role="textbox"], div.ProseMirror[contenteditable="true"], [contenteditable="true"], textarea');
    if (!box) return;
    box.focus();
    const prefix = name + ", ";
    if (box.tagName === "TEXTAREA") {
      const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, "value").set;
      setter.call(box, prefix + box.value.replace(/^[A-Z][\w .]*, /, ""));
      box.dispatchEvent(new Event("input", { bubbles: true }));
      box.setSelectionRange(box.value.length, box.value.length);
    } else {
      const sel = getSelection(); const range = document.createRange();
      range.selectNodeContents(box); range.collapse(true); sel.removeAllRanges(); sel.addRange(range);
      document.execCommand("insertText", false, prefix);
    }
  }
})();
