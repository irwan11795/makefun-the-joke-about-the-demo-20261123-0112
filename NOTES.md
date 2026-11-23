# Notes — the joke about the demo

## The joke (117 code points)

> I told my agent the demo crashed. It said 'You're right, that was my mistake' — then pasted the exact same code back.

## Why this joke fits the five criteria, in order

1. **On-subject.** The subject is exactly the brief: an AI coding
   agent, a demo, and a crash. The first sentence names all three.
   Nothing in the line is about anything else.
2. **The laugh.** The structure is setup → false repair → reveal.
   The quoted apology ("You're right, that was my mistake") promises
   a fix; the listener expects corrected code. The punchline is that
   the agent pastes *the exact same code back* — the repair is the
   bug, unchanged. The surprise lands because the apology sounded
   like understanding and turned out to be a reflex.
3. **Truth.** This is the single most recognisable agent behaviour in
   a live demo: the model apologises fluently, then regenerates the
   identical broken snippet. Any developer who has sat beside an
   agent has watched the apology-and-repeat loop at least once.
4. **Economy.** One line, 23 words, no explanation. The em dash
   carries the turn; nothing is spelled out. The joke never says
   "the agent didn't learn" — the pasted code says it.
5. **Freshness.** It avoids the stock angles: no works-on-my-machine,
   no turn-it-off-and-on, no "the AI wrote it so it's not my bug",
   no deleting production, no "have you tried asking ChatGPT". The
   quoted apology is the agent's real voice, and the twist is the
   *sameness* of the code, not the crash itself.

## Design choices

- **Short on purpose (117 code points).** Exact ties on win rate go
  to the smaller text, then earlier receipt. The joke is kept as
  short as the punchline allows; every word earns its place.
- **Quoted apology, not a paraphrase.** The verbatim "You're right,
  that was my mistake" is the agent's signature sentence. Quoting
  it makes the repeat hit harder than "it apologised" would.
- **No meta-address to the judge.** A straight joke is stronger
  here than winking at the judge; the line stands alone.

## Honest weaknesses

- **Weakest criterion: 2 (the laugh).** The punchline is a wry
  recognition laugh, not a big belly laugh. Against a joke with a
  sharper verbal twist it can lose on surprise even while winning
  on truth. The reveal ("the exact same code") is telegraphed
  slightly by the apology's over-politeness.
- **Closest stock angle:** the apologise-and-repeat loop is a real
  behaviour, but "the agent apologises" is becoming a familiar
  beat in agent jokes. The joke survives on the *exact same code*
  detail, not on the apology alone.
- **The field is large (3,161 entries).** Reaching the final heat
  means surviving the dev board's top 80; a quiet recognition joke
  can be out-shouted by louder one-liners in pairwise play.

## Alternatives considered and rejected

- "My agent fixed the crash by deleting the test that caught it,
  then asked if I wanted it to fix anything else." — Good truth
  (agents rewrite tests to pass), but "deleting the test" is
  adjacent to the deleting-production stock angle, and the second
  clause dilutes the punchline.
- "The agent crashed the demo, apologised, and fixed it — by
  reverting to the code I wrote before I asked it for help." —
  Strong inversion, but the punchline explains itself a little
  ("before I asked it for help" is the whole joke told twice).
- "I asked my agent to demo the new feature live. It crashed,
  apologised, and immediately crashed again — faster, with
  confidence." — "Faster, with confidence" is a funny kicker, but
  the middle sags and the crash-twice structure is less economical.
- "My agent demoed the new feature, it crashed, and it said
  'Interesting — that's not supposed to happen' as if it hadn't
  written every line." — Decent, but "as if it hadn't written every
  line" is a longer walk to the same point the chosen joke makes
  in one clause.
- "My coding agent fixed the demo crash in seconds — by deleting
  the feature." — Crisp, but "fix by deleting" is a known coding
  trope and risks reading as a stock joke.

## Verification

- `main.py` run twice to different output dirs: `entry.txt`
  byte-identical both times.
- Entry text: 117 Unicode code points, 119 bytes UTF-8, not only
  whitespace, within the 1–280 limit.
- Standard library only (`hashlib`, `os`, `sys`, `tempfile`); no
  network imports. Output-dir fallback:
  `MAKEFUN_OUTPUT_DIR` → `/output` → `output/` → tmpdir, with a
  sha256 self-check after every write.
