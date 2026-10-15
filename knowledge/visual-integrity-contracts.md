# Visual integrity: semantic contracts and fidelity receipts

This is an **additive** reference for Signal Loom. It does not replace its seven-stage workflow, claim ledger, Story Spine, Loomfile state, human-review gates, or canonical representation guidance.

## Invocation
At PLAN, consult this reference when a diagram or meaning-bearing interaction represents dependencies, topology, policy outcomes, sequence, lifecycle, evidence provenance, or complex simplification. Ordinary prose, simple tables, and charts already governed by the chart-integrity doctrine do not need a second ceremony.

## Visual decision gate
Before drawing, state the reader question, why visual representation beats clear prose or a table, the supporting claim IDs, and the essential relationships. If the question is answered equally well by prose, choose prose. A diagram must not be decoration.

## Semantic contract (before geometry)
For each meaning-bearing figure, record an entry under `state/visual-plan.json` (compatible additive field `semantic_contracts`; do not remove existing fields). Each entry should contain:
- `figure_id` (stable identifier) and `reader_question`;
- `source_claim_ids` (real IDs from `state/claims.jsonl`, or an explicit explanation of an unsourced/illustrative figure);
- `semantic_pattern` and `required_elements` (the elements needed to communicate the meaning, including negative outcomes, failure paths or unknowns when material);
- `representation`, `audience`, and `static_fallback`;
- `planned_omissions` (including reason and effect on interpretation);
- `checks` (what can be checked mechanically versus what requires judgment).

Select patterns by **meaning**, then format: finite-capacity bottleneck (sources, capacity, queue, accepted/deferred outcomes); policy divergence (same rule order, pass/fail/skipped/not reached, first divergence); dependency/failure (dependent, prerequisite, failure consequence); lifecycle (states, guards, retries, terminal outcomes); before/after topology (stable component identity, added/removed/changed/moved/rewired). These are examples, not a requirement to shoehorn every diagram into a fixed catalog. If two patterns both need full treatment, make overview and detail rather than merging into an unreadable figure.

A semantic pattern is a checklist of meaning, not a visual template. A browser-safe chart or static table can still be the right representation.

## Fidelity receipt for simplification
If PLAN, FINISH, or DISTRIBUTE removes, merges, renames, aggregates, or translates source elements, keep a `fidelity_receipts` entry in `state/visual-plan.json`:
- `figure_id`, `source_elements`, `retained`, `combined`, `omitted`, `translated_labels`, `residual_uncertainty`, and `review_status`.
- Each changed or omitted substantive element needs a reason. Preserve causal direction, units, thresholds, denominator, missingness, source IDs, and decision outcomes.
- An audience-friendly label must not claim greater certainty or different causation. For topology comparisons, don't confuse moving a box with rewiring a real dependency.
- Distinguish a deliberate editorial omission from a missing source or an unverified claim.
- If essential meaning cannot survive a requested density limit, split the artifact or refuse the simplification. Do not squeeze text until illegible or quietly drop an edge.

Do not treat a receipt as human approval. Keep all existing review/approval statuses and basis invalidation rules.

## Static-first interaction
The complete explanation, labels, statuses and outcomes must remain discoverable without animation or JavaScript. Motion may demonstrate order but must not manufacture essential meaning. Respect reduced-motion preference; expose text equivalents, visible focus, and usable touch/keyboard controls where relevant. Optional animation defaults off unless it materially teaches.

## Visual verification: separate three evidence layers
1. **Structural:** run the existing Loomfile and HTML validators; verify semantic labels, figure-to-claim references, alternate text, and receipt presence when simplification occurred.
2. **Rendered:** when a browser or renderer is available, inspect real desktop/mobile output for clipped labels, overlaps, connectors obscuring content, contrast, font fallback, reduced motion, and static/no-JS readability. Record tested viewports and concrete findings. A source-code lint pass is *not* a rendering test.
3. **Meaning:** human/independent review compares sources, claim ledger, semantic contract, and figure; check false certainty, missing paths, misleading scales, and silently omitted relationships. Deterministic tools cannot certify this layer.

For each layer report `passed`, `failed`, or `not_run`; never convert unavailable tooling to a passing result. Record actual evidence in the existing `review/diagnostics.json` process. Review, authority, and publication remain independent.

## Brand and provenance
Reuse the project's own palette and typography; don't globally impose another project's styling or a fixed diagram skin. Verify contrast at final rendered label size. If matching a brand requires a contrast adjustment or font fallback, note it in the visual plan and have the user approve consequential deviations. Avoid remote fonts and scripts by default; respect existing trust and publication boundaries.

## Attribution
Conceptual lessons adapted from Cathryn Lavery's MIT-licensed Diagram Design project (https://github.com/cathrynlavery/diagram-design). This reference is an independent extension of Signal Loom; it does not install or embed that third-party skill.
