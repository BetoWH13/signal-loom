# Visual integrity regression checklist

Use with an existing Loomfile or a small disposable example. These are **acceptance scenarios**, not claims that a browser test has been executed.

| Scenario | Expected result |
| --- | --- |
| Simple list of three values | Prose or table selected; no gratuitous diagram |
| Queue capacity 3/hour, arrival 5/hour | Sources, queue, capacity and overflow/deferred path remain explicit |
| Two policy traces differ at rule 2 | First divergence labeled; SKIPPED != NOT REACHED |
| Architecture before/after with a moved box | Stable node ID; positional move not misreported as rewired |
| Simplify twelve nodes to seven | Receipt names merges/omissions; essential edges survive or figure is split |
| Exec-friendly label for technical component | Friendly label is mapped to source identity; behavior unchanged |
| JS unavailable or prefers-reduced-motion | Complete static meaning and text alternatives remain present |
| Mobile narrow screen | Inspect actual render for clipped labels and unusable controls |
| Browser/render engine unavailable | Render check reported NOT_RUN, never PASS |
| Unsourced metric | Mark as illustrative or missing; no fabricated number |
| Changed source after review | Old review basis invalidated under existing Loomfile rules |

The canonical `scripts/validate_loomfile.py` and `scripts/inspect_infographic_html.py` remain authoritative for their documented checks. This checklist supplements, not replaces, them. For a complete release assessment, exercise the end-to-end Loomfile review process on real inputs and record actual findings.
