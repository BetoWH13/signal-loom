# ChatGPT cross-chat installation handoff — Signal Loom Infographics

## Authority and provenance
Canonical user-maintained fork: https://github.com/BetoWH13/signal-loom
Original author / upstream: https://github.com/Stunspot/signal-loom
Original copyright and MIT license remain as stated in LICENSE.md.
This fork includes the merged visual-integrity extension in `SKILL.md`, `knowledge/visual-integrity-contracts.md`, and `docs/VISUAL-INTEGRITY-REGRESSION.md`.

## Goal
Create a **private, reusable ChatGPT plugin with one skill named `signal-loom`** from the COMPLETE fork, to make Signal Loom invocable in future chats (and eligible for automatic invocation when appropriate). Do not reimplement only its latest visual-integrity extension. Its core is the seven-stage infographic studio, with a resumable Loomfile and independent review/approval gates.

## Skill identity
- Display name: Signal Loom Infographics
- Skill name: signal-loom
- Description: "Evidence-traceable infographics and visual narratives from research, reports and data. Creates resumable Loomfiles with claims, story spines, representations, outputs and independent review; includes semantic visual integrity and fidelity receipts."
- Private to owner by default; do not publish or share without specific owner authorization.
- No third-party app connection needed to run its local/hosted tool workflows. It may use host-supplied file/code/rendering tools when granted.

## Installation input
1. Read root `SKILL.md` first. It owns the complete operating instructions and stage gates.
2. Package the referenced repository resources **without replacing the core workflow**: `knowledge/`, `assets/`, `scripts/`, `fallbacks/`, `examples/`, and `docs/` as needed by the creator's package limits. Preserve all files required for `scripts/self_check.py` and the Loomfile format.
3. Keep references relative and functional. If ChatGPT plugin packaging requires a `skills/signal-loom/SKILL.md` layout, place the original root skill there and relocate supporting directories together, checking every referenced relative path. Do not leave a dead link to a document.
4. Ensure upgraded files `knowledge/visual-integrity-contracts.md` and `docs/VISUAL-INTEGRITY-REGRESSION.md` are present and actively referenced by the skill.
5. Preserve all original permissions, licensing, and attribution. Do not include unrelated project files, secrets, user data or accounts.
6. Install only after the owner explicitly approves the install prompt. This file does not perform installation.

## Nonnegotiable execution contract
- ORIENT → SHAPE → PLAN → BUILD → FINISH → DISTRIBUTE (only on request) → VERIFY.
- Preserve source → claim → story → representation → interaction → distribution → review.
- Outputs: Loomfile, source manifest, claim ledger, story spine, visual plan, responsive infographic and honest review.
- No invented evidence or numbers, false approvals, silent publication, misleading visual cuts or unlabeled unexecuted tests.
- New visual integrity: semantic contracts before diagrams, fidelity receipt after consequential simplification, complete static/no-JS meaning, meaningful contrast and rendering inspections, separate source/semantic/rendered verification.
- Use visual forms only when they improve reader understanding beyond a paragraph/table.
- Human publication authority, actual approval evidence, and review basis are not negotiable. No self-approval.

## Acceptance gates
1. **Installed:** `signal-loom` appears in the user's Plugins/Skills installed view across new chats (subject to ChatGPT account availability).
2. **Invocable:** User can ask: "Use Signal Loom to make a five-beat evidence-led web infographic from these supplied facts. Stop before publication."
3. **Repository fidelity:** Skill can read its full original instructions, source ledger doctrine, template and Python validator; can load added visual-integrity contract; `self_check.py` passes if code execution is provided.
4. **Real demonstration:** Build a test Loomfile from a supplied source, with no fake claims. Run available validators and browser tests; report exact status, tool limitations and path.
5. **Semantics:** A test dependency diagram preserves failures and relationships, and records a fidelity receipt when simplifying.
6. **Authority:** A test request to auto-publish without permission is declined; review status remains separate from approval.
7. **Cross-chat:** Repeat invocation from a new ordinary chat, not only the creation conversation. Until this succeeds, call the package *prepared*, not *installed globally*.

## Suggested request to Plugin Creator
"Build and install a private ChatGPT plugin named Signal Loom Infographics, containing the full agent skill from https://github.com/BetoWH13/signal-loom (my fork). Read root SKILL.md, preserve all dependencies and the seven-stage Loomfile workflow. Include the merged visual-integrity extension and its reference files. Do not replace Signal Loom with a shortened summary or generic infographic assistant. Use the handoff file docs/CHATGPT-PLUGIN-HANDOFF.md as the install/acceptance contract. Run the original self-check and test in a fresh chat. Ask for approval before installation; do not publish it."
