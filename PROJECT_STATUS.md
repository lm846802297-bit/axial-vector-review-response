# 2026-11-14 live status: post-PR #106 / #113 merge audit

> This entry supersedes earlier live summaries below wherever they list PR #106 or #113 as open/draft, report an older main SHA, or describe either branch as an active PR. It also supersedes the pre-merge PR #56 status and the 2026-11-06 response-PDF validation metadata: PR #56 merged on 2026-11-12, and the response PDF layout fix on this maintenance branch is described below. Older dated entries remain as historical snapshots.

## Repository-management update (2026-11-14)

- Four A4–A5 portal research notes were read and checked against their associated scoped script outputs; chronology and matching-scale limits were clarified without changing results. Baseline review: 133 reviewed, 329 pending. See `docs/repository-management/SIXTEENTH_REVIEW_PORTAL_A4_A5_NOTES_2026-11-15.md`.

- Five A4–A5 portal output summaries were individually checked against script reruns. A4d initially failed due to undefined `p2`; the SymPy declaration and a full-script regression check were added. All five scripts now exit zero. No complete pole or UV–EFT matching is claimed. At that checkpoint the baseline register had 129 reviewed, 333 pending; see `docs/repository-management/FIFTEENTH_REVIEW_PORTAL_A4_A5_2026-11-15.md`.

- Four Global-06 protocols and compact-result records were reviewed against their digitized profile and summary files. The raw 36 chunks remain referenced to a conversation ZIP not verified in this review. Numerical checks remain scoped to the original stage. At that checkpoint the baseline register had 124 reviewed, 338 pending; see `docs/repository-management/FOURTEENTH_REVIEW_GLOBAL06_2026-11-15.md`.

- Three C4-C4 research reports were individually reviewed against their output archives; malformed math delimiters were repaired. All 80 quadrature base anchors match the recovered pinned table exactly, while the 80 overlapping radial anchors agree to `3.33e-16` relative. See `docs/repository-management/THIRTEENTH_REVIEW_C4C4_REPORTS_2026-11-15.md`; at that checkpoint baseline review had 120 reviewed and 342 pending. No new scattering integrals were run.

- Seven C4-C3/C4-C4 archive descriptions were individually reviewed. Their manifests pass, but the currently tracked 96-row anchor differs in floating-point final digits from the historical input pinned by two programs. The original byte-pinned object has been recovered, both program paths repaired, and 17 unit/input checks pass. The origin of the later differences is unknown; no scattering integrations were rerun. See `docs/repository-management/TWELFTH_REVIEW_C4C3_C4C4_2026-11-15.md`. At that checkpoint: 117 reviewed, 345 pending.

- Five A2–A3 portal calculation records were reviewed individually at `fe1c308`; four corresponding scripts ran successfully under Python 3.12.14 / SymPy 1.14.0. One Markdown rendering error was fixed without changing physics. See `docs/repository-management/ELEVENTH_REVIEW_PORTAL_A2_A3_2026-11-15.md`. At that checkpoint the baseline register recorded 110 reviewed and 352 pending; these checks do not establish complete gauge-invariant matching.

- Legacy section 250–259 and 261–262 Python scripts were rerun locally: all 12 exited zero; sections 253 and 262 have small floating-point residual-text differences from archived logs. Section 260 passed its first 69 checks but failed its byte-for-byte archived stdout comparison at section 250 because the interpreter version differs. See `docs/repository-management/LEGACY_LOG_REVIEW_2026-11-14.md`; Mathematica was not rerun.

- A manifest review found three provenance issues: the fermion snapshot README does not match its historical checksum; the dated GR-path manifest matches historical commit `ba581642dd749d8a4c54ea9553a2c3d1baf839c3` while three files changed later; and the compressed radial-scalar scan belongs to a later run than the 2026-11-09 record. Commit `9ae7955` confirms the earlier data and source; row-level comparison isolates differences to two bound columns. The current uncompressed CSV is not committed. Old manifests and payloads are retained; current checksum sidecars and explicit limitations are documented in `docs/repository-management/MANIFEST_REVIEW_2026-11-14.md`.

- Maintenance PR #115 incorporated `main` at merge commit `e4dd7ec` with an unchanged maintenance tree; refresh branch comparison before integration. Workflow review reports were relocated under `docs/repository-management/workflow-reviews/` with a blob/SHA-256 manifest; YAML execution paths were not changed.
- The old `research/stellar-cooling-constraints-20261105/review_package_extracted/` mentioned in historical entries below was retired; use `research/stellar-cooling-constraints-20261105/REVIEW_PACKAGE_INDEX_2026-11-13.md` and the collaborator archive instead.
- The previous 63-page PDF had a clipped figure caption. On this maintenance branch the full original caption is preserved immediately after the figure, and the matched 64-page TeX/PDF build has undergone contact-sheet inspection and page-boundary checks. The two four-page referee PDF variants have equal extracted text but different annotations. See `docs/repository-management/ROOT_PDF_EXTRACTION_AUDIT_2026-11-14.md`.

## Current repository state

- **Current branch:** `main` (PR #113 merge-state anchor `d2f4037cc965eb2f4184f695dc81a95e1b8283c9`; current main HEAD at the 2026-11-14 document-audit snapshot is `fbab624435c853e90e3955009a545e28c5f5be98`, five documentation-only commits later).
- **PR #106 — merged (Squash):** `71ce83e72dd4688f09462e54209d3a47e7172e03`. Archives the 10 MeV B.2 energy/GR/polarization audit, GR ray kernel, polarization state-counting module, exact B.13 explicit-spinor audit, and regression tests.
- **PR #113 — merged (Squash):** `d2f4037cc965eb2f4184f695dc81a95e1b8283c9`. Archives P1-B Global-02–05 radial/energy screens, selected high-order checks, exact-B.13 high-energy-band B.1/B.2 comparison, and the low-x support finding.
- **PR #56 — merged 2026-11-12:** author-directed integration of the fixed-profile axial-EFT ballistic-cooling benchmark and related research. Merge status is not scientific acceptance: the pure-vector Blinov Fig. 7 10 MeV high-absorption discrepancy remains unresolved (+92.24691% in the literal fixed-ω lane); no opacity/profile rescaling is accepted, and the axial curve remains conditional rather than a complete SN1987A transport/exclusion result.
- **Formal response on the maintenance branch:** same-source build, 64 pages, 501,004 bytes, SHA-256 `095daf18a7202d11f9bf9f48077ab2ab82c1f10386059da9bf9633ae4d9ea679`. Full original Figure 1 caption is retained in the adjacent text after the figure. Layout inspection does not establish scientific validity; the prior 63-page file (`e0a2114e…`) remains recoverable from Git history and the dated Overleaf package.
- **No open research/physics PRs remain** after the merge audit. The separate Draft repository-management PR #115 is open on `maintenance/repository-organization-audit-20261114`; it contains navigation, classification, audit documentation and a separately recorded spectral-window comparison; it does not overwrite original scientific outputs or change physical conclusions. The branch was synchronized with main at `e4dd7ec` and must be reviewed against the latest main before merge.
- PR #106's exact-kernel workflow passed compilation, the explicit-spinor audit, and 38 regression tests across five suites (run #43534265182).
- The Global-05 low-x driver was rerun from the exact packaged source/profile. All 80 low-order points were finite/nonnegative; maximum detailed-balance residual was (4.6060\times10^{-15}), and maximum final-muon shell residual was (1.6261\times10^{-13}). The script writes the summary and regenerable 80-point JSON/CSV records.
- **Physics acceptance remains open:** the low-x check is only a 16-radius, five-energy low-order screen. Full 1687-radius low-x coverage, complete full-band B.1/B.2 transport, the Fig. 7 strong-absorption reconciliation, and any SN1987A/axial-limit update are not accepted. The literal scalar B.2 baseline and production axial curve remain unchanged.

---

# 2026-11-13 live status: post-PR94 archive extraction

> This section supersedes earlier live entries below wherever they report earlier main SHAs, PR states, archive locations, or branch counts. The historical records remain intact.

## Current repository state

- Main immediately after PR #94: `2bebb38c7ff8966b048b133d67c1aa7bd37aa496`.
- **PR #94 — merged:** generated delivery archives were replaced by extracted files. The Major 3 Overleaf package, Higgs-portal document package, and axial stellar-cooling independent-review snapshot are now stored as ordinary files with file-level checksums and extraction provenance.
- **PR #93 — closed as superseded:** its archive-based packaging path was not merged. Its report and package index are now represented by the extracted review snapshot and the root-level review index; the ZIP-building workflow is not retained.
- **PR #88/#89 — merged, then cleaned:** the Overleaf bundle was verified and extracted. The committed ZIP and its archive-only sidecar manifest were removed after their contents and original manifest were preserved as individual files.
- **PR #87 — merged:** six selected B.13/B.16 moving-muon recovery artifacts are in main. The 0.1 MeV vertex-preserving scan remains explicitly not converged.
- **PR #77 — merged; PR #83 — duplicate and closed:** the Major 4.4 provenance outputs already in main were not overwritten.
- **PR #84/#85 — merged:** C4-C4-B full-radial and separate two-VEV benchmark results remain in their previously defined scientific scopes.
- No physics calculations, rate kernels, opacity tables, or constraint curves were changed by PR #94. The pure-vector Blinov Fig. 7 benchmark remains **NOT PASSED** at the 10 MeV strong-absorption end.

## Archive policy and current locations

Generated review/delivery ZIPs and Base64 ZIP parts are not committed to main. Their extracted contents are stored at:

- `deliverables/Overleaf_Reply_Letter_PR72_2026-11-13/`
- `deliverables/higgs_portal_mixing_md_with_svg/`
- `research/stellar-cooling-constraints-20261105/review_package_extracted/`

See `deliverables/README.md` and `research/stellar-cooling-constraints-20261105/REVIEW_PACKAGE_INDEX_2026-11-13.md` for the import paths, source snapshot, and checksums.

The official SFHo/FRDM v1.03 upstream input archives under `research/stellar-cooling-constraints-20261105/blinov_reproduction/data/sfho-frdm-v1.03/` are a separate case: they are original EOS source inputs used by the current reassembly/provenance workflow, not generated handoff bundles. They are retained pending a separate extraction and data-reader migration; they were not deleted without verifying a replacement input path.

## Branch audit refresh

At the post-PR94 audit snapshot, the repository had 100 refs including main (99 non-main). After synchronizing the completed/superseded delivery and duplicate branches to main, the compare summary was 74 diverged, 16 behind-only, 9 identical, and 0 ahead-only. These are ancestry categories, not counts of unmerged research results. The pre-PR94 96-ref inventory remains preserved as a historical snapshot; the updated summary is recorded in `research/BRANCH_INVENTORY_2026-11-13.json`.

The workflow-generated branch named `${GITHUB_REF_NAME}` was deliberately retained: it contains independent fermion-sector matrix audit outputs related to the Major 1 Higgs–singlet workstream and is not an archive-only branch. It requires its own scoped review rather than a branch reset.

---

# 2026-11-13 live status: post-integration branch audit

> This live section supersedes older dated entries below wherever they report earlier main SHAs, PR states, branch counts, or active-branch inventories. The branch inventory is a snapshot against the main SHA recorded below; it is not a request to rebase or merge every divergent branch.

## Current repository and PR state

- Audited main baseline: `a74707637837dfd577e15e530c896959ed12baa2` (after PR #89).
- **PR #87 — merged:** selected B.13/B.16 moving-muon validation artifacts recovered onto a clean main-based branch. The 0.1 MeV vertex-preserving scan remains explicitly not converged.
- **PR #88 — merged:** current-main Major 3 Overleaf bundle rebuilt with its required TeX, BibTeX, bibliography style, figure PDF, reference PDF, and README.
- **PR #89 — merged:** corrected the Overleaf ZIP's embedded and external SHA-256 manifests. The current ZIP is 777,561 bytes with SHA-256 `6c3d74091df33f316ea01694738a5b2392d9a882576704a7c3690a6569037323`; every embedded file hash and CRC-32 was rechecked against the stored bytes.
- **PR #77 — merged:** Major 4.4 post-merge provenance refreshes and the package-relative projector-test import fix. PR #83 was closed as a duplicate of #77, not as lost research.
- **PR #84 and PR #85 — merged:** C4-C4-B full-radial archive and the separately scoped two-VEV microphysics benchmark.
- No open PRs were present at the post-PR #89 repository snapshot. This status/audit update is documentation-only.

## Post-inventory checksum and documentation corrections (2026-11-13)

- **PR #90 — merged** at `dc3e3339238cbae7b72f73228518ca36a89a837d`: corrected the B.13/B.16 recovery manifest's report digest to `485bc6ce837f6bd45b9dd7958c7049b5426f5d6508638c9976f2b55267bbd4f4`. The four other artifact hashes were independently verified and unchanged; no source or numerical output changed.
- **PR #91 — merged** at `d106b9a6f16116918a92da775fa7113b2718a221`: added the all-branch inventory and updated the live status/audit documentation.
- Latest main after these follow-on merges: `dc3e3339238cbae7b72f73228518ca36a89a837d`. The branch inventory remains a point-in-time snapshot against `a74707637837dfd577e15e530c896959ed12baa2` (96 refs including main). Two post-snapshot refs were created for PR #90 (checksum-only) and PR #91 (documentation-only); they do not add research content.
- No open PRs remained after PR #90 and PR #91 were merged.

## All-branch audit

- The repository had **96 branch refs including main**, hence **95 non-main branches**.
- Against main `a74707637837dfd577e15e530c896959ed12baa2`, all 95 non-main refs were compared: **79 diverged**, **16 were behind-only**, **0 were ahead-only**, and **0 were identical**.
- Of the 79 diverged branches, 76 had branch-side changed-path entries in the compare result; 3 had no branch-side path entries. These counts are ancestry/diff triage, not a statement that every divergent branch contains unmerged work. Squash-merged branches commonly remain divergent.
- Full per-branch names, head SHAs, ahead/behind counts, and compare-path counts are recorded in [BRANCH_INVENTORY_2026-11-13.json](research/BRANCH_INVENTORY_2026-11-13.json).
- Do not bulk-merge stale branches to eliminate `ahead_by` counts. Merge only isolated, genuinely new content after provenance, input hashes, output hashes, and current-main overlap have been checked.

## Research and scientific acceptance boundaries

- The moving-muon source branch is retained as historical research; PR #87 extracted only six missing B.13/B.16 artifacts. Its later profile/provenance changes were not copied over the profile used by the archived results.
- Major 4.4's three B.13/B.16 output records (`b13_b16_comparison_2026-11-12.json`, `b13_b16_low_mass_scan_2026-11-12.json`, and `validation_manifest_2026-11-12.json`) are already in main with run commit `c611005c6cb343f8a53b282e14d15a8b6468b541`. The three additional numerical files differing only at floating-point roundoff were not used to overwrite main.
- The pure-vector Blinov Fig. 7 physical benchmark remains **NOT PASSED** at the 10 MeV strong-absorption end. Software/CI success, grid convergence, archive integrity, and physical benchmark acceptance remain distinct. No opacity/profile rescaling or updated axial constraint curve is authorized by these integrations.
- The Major 3 historical branch is not re-imported: PR #72 already integrated the response, while PR #88/#89 provide the current-main Overleaf package with verified integrity metadata.
- Other substantial branches (including the ongoing Higgs–singlet and separate stellar-review-package work) remain separate workstreams and require their own scoped review; this audit does not delete or merge them.

---

## Historical 2026-11-12 status snapshot (superseded)

 older dated entries below wherever they report an earlier main SHA, PR state, validation run, or branch count. Historical records remain intact.

## Repository and PR state

- Main baseline before this status commit: `f6ced63236a02f1e5f7645e23291b6b5cbe3659e`.
- PR #56 was squash-merged into main at `293d047013cce0dc3fbc44b2cd679f2df0f253dd` on 2026-11-12 08:47:43 UTC. It is **Closed / Merged**. This was a research integration, not scientific acceptance of the Blinov Fig. 7 benchmark.
- The former PR #56 branch `codex/major44-axial-cooling-constraints-20261105` is retained as a post-merge validation branch; it is not an open PR.
- PR #53 (original-UV axial stellar cooling), #68 (Belle II radial-scalar study), and #69 (Higgs–singlet mixing) remain **Open / Draft**.
- The active research/data branch set is the four PR/source branches (including the retained #56 validation branch), C4-C4, moving-muon, P1-IIIe EOS, PR57 source bundle, and SFHo/FRDM transfer. Older divergent branches without active PRs are retained as historical work and are not automatically rebased into the active line.

## Numerical validation and failure classification

- **Run #158** ([43135845410](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43135845410), trigger SHA `071d19490bc3`) ended `cancelled` under the old `timeout-minutes: 25` job setting. The first unittest discovery completed 337 tests with one intentional skip; the second discovery logged 92 passing tests before cancellation and had no final summary. The log contains no failed assertion, traceback, or calculation exception. Classify this as a runtime timeout/interruption; the run is incomplete.
- **Run #43202685556** ([run](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43202685556), trigger SHA `d31ee50393b2866e9ea5c58dc374207fa6cae851`) completed with one test-import error: `test_vector_longitudinal_projector.py` used a top-level import for a module in the same `finite_mixing.thermal_integrals` package. The first discovery reported 359 tests, one import error and one intentional skip; no physics assertion failed. The subsequent test discovery, reference scans, saved-output checks and figure regeneration were skipped. Classify this as a Python package/import-path defect, not a matrix-element or transport failure.
- **Import fix:** commit `c611005c6cb343f8a53b282e14d15a8b6468b541` changes the test to a package-relative import (`from .audit_vector_longitudinal_projector import ...`). The fix is independently exercised by the successful Moving-muon and Vector-to-axial workflows below.
- **Finite-mixing UV coupling map:** Run [#43206544272](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544272) completed successfully on `c611005`; the UV coupling-map and endpoint tests passed.
- **Vector-to-axial local response:** Run [#43206544724](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544724) completed successfully on `c611005`. Its 81 tests passed; local response, dimuon thermal-integral, moving-muon semi-Compton, and SFHo local moving-Compton outputs were generated and committed as `ee683e350707b237c1b801923f4d3713e2054327`.
- **Moving-muon thermal response:** Run [#43206544350](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544350) completed successfully on `c611005`. Its 81 tests passed; explicit-spinor checks, matrix-element/thermal convergence, vector-current T/L source audit, exact B.13 vs B.14--B.16 local comparison, and low-mass vector scan all completed. The reproducibility manifest and numerical outputs were committed as `b145d600e79f8000dfd3efb386cc9f2b5d367756`.
- **Major 4.4 full numerical validation:** Run [#43206544367](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544367) remains `in_progress` on trigger SHA `c611005`. Both archive SHA gates and the first research-level rate/transport/independent-kernel test discovery have completed successfully. The second Blinov reproduction and EOS regression test discovery is now running; reference scans, saved-output checks, and figure regeneration have not yet been recorded. Do not call the full workflow passed. The two completed output commits above change generated JSON outputs, not the source/test code exercised by this run.
- **Run #43202685556 checksum gates:** the C4C3 SHA-256 manifest step and the SFHo/FRDM manifest/reassembly step both completed successfully before the import error stopped the workflow. The C4C3 manifest contains 14 entries; all 14 target paths exist. The SFHo/FRDM release manifest contains five entries and its asset names match the downloader metadata.
- **Archive identity:** all 15 Git blobs in the C4C3 archive directory (14 payload files plus the manifest) and all 8 Git blobs in the vendored SFHo/FRDM directory are identical across main, the post-merge validation branch, and the Run #432 trigger tree. This confirms source/archive identity; the actual byte-level SHA checks are the successful workflow gates above. The C4C3 result remains a fixed-local-energy, flat-space radial-scattering/opacity diagnostic, not a full transport solution.
- **Other moving-muon workflow failures retained:** (i) B.16 polarization transport previously stopped before integration because a direct script import lacked the research root on `PYTHONPATH` (workflow environment defect); (ii) the escape phase-space decomposition stopped at a byte-level Fig. 7 fingerprint guard despite only approximately (10^{-16})-level JSON float reserialization changes (guard/canonicalization issue; no integration completed); (iii) P1-IIIe C4-C3 radial scattering stopped at checkout because escaped GitHub expressions generated an invalid refspec (workflow expression defect; no rate shard ran). These must not be described as physical calculation failures or successful calculations.
- **Physical result:** pure-vector Blinov Fig. 7 remains **NOT PASSED**. The recorded 10 MeV strong-absorption residual is approximately +92.43%. Neither a successful software test suite nor archive checks resolve this discrepancy or unlock a production axial-vector exclusion.

## Active branch synchronization

The following active branches are synchronized to the main baseline above with `behind_by=0`. This status commit is propagated to each branch with a non-force, two-parent merge; the final comparisons are recorded after propagation.

| Branch | Purpose | Required behind_by |
|---|---|---:|
| `research/stellar-cooling-original-uv-model-20261105` | PR #53 | 0 |
| `codex/major44-axial-cooling-constraints-20261105` | PR #56 post-merge validation | 0 |
| `research/major1-scalar-pole-belleii-20261109` | PR #68 | 0 |
| `research/major1-higgs-scalar-mixing-20261109` | PR #69 | 0 |
| `research/c4c4-energy-dependence-20261112` | C4-C4 follow-up | 0 |
| `research/moving-muon-thermal-rates-20261107` | Moving-muon local rates | 0 |
| `transfer/p1iii-eos-latest-source-20261111` | P1-III EOS source/data | 0 |
| `transfer/pr57-source-bundle-20261110` | PR #57 source archive | 0 |
| `transfer/sfho-frdm-release-transfer-20261111` | SFHo/FRDM archive | 0 |

No force-push or branch deletion is part of this synchronization. A zero `behind_by` count establishes ancestry synchronization only; it does not imply that the research branch is scientifically complete.

## Interpretation policy

- CI success validates only the tests and checks that actually ran on the recorded SHA.
- A test skip must retain its reason and must not be counted as a pass.
- A generated scan or figure is not a physical reproduction until the literature benchmark and all declared model/transport assumptions pass their own acceptance criteria.
- Preserve failed, cancelled, and unresolved physical-validation records. Do not use branch cleanup or successful software CI to erase a scientific discrepancy.
---

## 2026-11-09 最终更新：PR #72 Major Point 3 选择性恢复与重新编译（构建通过）

- Major Point 3 保持两部分结构：原始单 VEV \(S\)-only 模型，以及可选的 \(\sigma+3N_R\) type-I seesaw 完成机制。原模型的残余 \(Z_2\)、Weinberg 算符选择规则、\(M_\nu^{(S)}\) 分块纹理和 \(U_{\rm PMNS}=\operatorname{diag}(1,U_{23})\) 结论保留。
- 扩展部分给出新增场及电荷、三个 Dirac Yukawa 项、四个标量辅助 Majorana 项、两个裸 Majorana 项、\(m_D\)、\(M_R\)、完整 \(6\times6\) 质量矩阵、type-I seesaw、轻/重 Takagi 对角化和解析逆构造；不加入数值 benchmark 或全局扫描。
- 显式写出新增右手中微子的线性与立方 \(U(1)_X\) anomaly cancellation 求和，并逐项展示 Dirac Yukawa 与 Majorana 项的规范电荷抵消。
- 恢复双单态 seesaw 的具体文献对应：Borah et al. 的 Table I、Eq. (4)、其后展示的 \(M_R,M_D\) 矩阵及 Eq. (8)；He et al. 的 Sec. II、Eqs. (1)--(5)。修正旧记录中将 Borah et al. 的 Eq. (7) 误列为中微子质量矩阵依据的问题；该式实际给出带电轻子质量矩阵。
- 恢复 Asai et al. 单电荷一标量模型的 \((M_\nu^{-1})_{\mu\mu}=(M_\nu^{-1})_{\tau\tau}=0\) two-zero-minor 结构，并说明现有电荷二标量 \(S\) 允许 \(M_R\) 的两个对角项，因此该预测不适用于当前双单态构造。
- 恢复双 VEV 关系 \(m_{A'}^2=g_X^2(4v_s^2+v_\sigma^2)\)、\(r_\sigma=v_\sigma^2/(4v_s^2)\) 及 \(v_s=m_{A'}/[2g_X\sqrt{1+r_\sigma}]\)。同时说明 \(r_\sigma\to0\) 会恢复残余 \(Z_2\)，因此不是完整 PMNS 混合的扩展极限。
- 恢复含 \(\kappa S^\dagger\sigma^2+\mathrm{h.c.}\) 的可重整化扩展标量势，并说明该项固定两个 singlet VEV 的相对相位。未将 \(m_s^2=2\lambda_Sv_s^2\) 当作扩展模型的一般质量关系；未加入 \(y_{s\ell\ell}\) 的扩展标量唯象映射、标量质量对角化或新实验扫描。
- Major Point 4.1 引用 Major Point 3 的结论与方程，不重复 seesaw 推导。原论文正文、原论文 bibliography、图表和科研计算均不修改；所有非中微子现象学仍以原始单 VEV \(S+\mathrm{VLL}\) 模型为基准。
- 英文写作参照用户原论文 axial_vector_model_building-v6.pdf，采用直接陈述、模型定义先行、方程紧接物理结论的组织方式。

**最终构建：** GitHub Actions [Run #152](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42573218957) 成功。58 页 A4 PDF，441,891 bytes；SHA-256：7d5f3dbb4b959dcb43268a1ebe5ec2cb046cb7502d33244b1e3864b53a6fbc23。LaTeX/BibTeX、PDF 结构、字体嵌入、引用与交叉引用检查均通过；BibTeX missing-entry/database warnings 为 0，无 Overfull box，保留一处原有 Underfull \hbox（badness 1199，源码第 609--611 行）。58 页均以 150 dpi 渲染，生成 10 份联系表。
**工作流清理：** 临时分支白名单已恢复为 main 原样；最终 PR diff 不包含 workflow 修改。
**当前状态：** PR #72 保持 Open、未合并；最终 PDF 已提交到 PR 分支。

# PROJECT_STATUS — Axial-vector paper revision and referee response

## 2026-11-12 最新分支、校验和与 Run #158 审计

- **main 基准与活跃分支同步：** `main=310a24a53e8448f0388072cfdbf55749fde713f9`。四个开放 PR（#53、#56、#68、#69）以及五个持续研究/数据分支（C4-C4、moving-muon、P1-IIIe EOS、PR57 source bundle、SFHo/FRDM transfer）均逐个执行 `main...head` 比较，九个分支全部 `behind_by=0`，均保留各自独有提交。比较结果：#53 14/0、#56 734/0、#68 26/0、#69 412/0、C4-C4 659/0、moving-muon 1536/0、P1-IIIe EOS 1350/0、PR57 source bundle 1125/0、SFHo/FRDM transfer 1342/0（格式均为 ahead/behind）。PR #53、#56、#68、#69 仍保持 Open / Draft；PR #56 在本记录更新前 head 为 `960f4079287a05f820f66d45e387d6a42c0b5e53`。
- **moving-muon 研究分支同步：** `research/moving-muon-thermal-rates-20261107` 原 head `004d640f6a2f10fef149580eba89b41c1c9acfd9`，相对 main 原先 `ahead_by=1535, behind_by=48`。已采用双父节点 merge commit `5f4c91fa0294a3007d5f6e812ceb1b938c5d7895` 将 main 合入，保留原分支研究历史、README 和 neutrino inverse-decay 审计脚本，采用 main 已纠正的 B.16 外层输入审计，并携带当前 PR #56 的回复信、PDF、项目状态和正文同步清单。未 force-push；合并后比较为 `ahead_by=1536, behind_by=0`。该分支的 LaTeX build 已由 Run [#43151746827](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43151746827) 触发，等待 PDF 构建验收。
- **Run #158（2026-11-12）：** [Major 4.4 EFT numerical validation](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43135845410) 在触发提交 `071d19490bc3` 上运行，最终为 `cancelled`，不是测试断言失败。日志明确显示 job 的 `timeout-minutes: 25`；第一组 unittest 完成 337 项、1 项按设计跳过，其余通过；第二组测试在取消前又记录 92 个 `... ok`，但没有最终测试汇总。日志没有 `FAILED`、`ERROR`、Traceback 或 AssertionError。第二组及后续数值扫描、输出重建和归档步骤均未完成。由于该 run 的 SHA `071d194` 比当前 PR #56 head `75251a5` 落后一个 PDF/audit 提交，即使旧 run 的测试阶段通过，也不能作为当前 head 的完整验收。
- **失败分类：** 当前唯一能确认的直接原因是 CI job 25 分钟超时；不能归类为物理计算错误，也不能归类为测试条件断言错误。现有测试通过记录仅覆盖已完成的测试，不替代未完成的后续验证。
- **Run #43151547062（当前 PR #56 head）：** 在 head `960f407` 上重新启动完整 Major 4.4 workflow。C4C3 14 项和 SFHo/FRDM 实际归档校验步骤均已通过；截至本次状态更新，第一组 research-level unittest 正在运行，尚无最终汇总。较早的 Run #43150499259 在父提交 `e9a0223` 上也通过同一组 checksum gates，仍在运行；它不是当前 head 的最终验收替代品。
- **Run #43149443570（2026-11-12）：** 新的 90 分钟 workflow 已完成 C4C3 14 项 SHA-256 检查及 SFHo/FRDM manifest、分块、BIN 重组检查；随后进入 Blinov/EOS unittest，但该 run 最终 `cancelled`，没有最终测试汇总，也未执行后续 reference scans、saved-output validation 或 figure regeneration。日志没有 `FAILED`、`ERROR`、Traceback 或 AssertionError；取消发起者未在可读 run metadata 中披露，不能推断为物理错误或断言失败。该 run 证明前置 checksum gates 通过，不构成数值 CI 完整通过。
- **C4C3 归档 SHA-256：** 对 `c4c3_direct_local_recomputation_2026-11-11/SHA256SUMS.txt` 中全部 14 个条目，从 PR #56 当前文件内容重新取得原始字节并独立计算 SHA-256，14/14 与清单完全一致。包括 301×4 径向率、1204 条逐项对照、opacity/tau、checkpoint、summary、源码及 provenance。归档结论仍限定为固定局域能量、平直空间径向散射光学深度诊断，不等同于完整输运解。
- **SFHo/FRDM v1.03 归档：** GitHub Release `sfho-frdm-v1.03-data` 五项资产 digest 与顶层 `sfho_frdm_v1.03_manifest.sha256` 逐项一致。Run [#43149443570](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43149443570) 的归档步骤已实际校验三个 BIN 分块（62,914,560 B、62,914,560 B、35,262,951 B），逐片 SHA-256 全部通过；重组得到 161,092,071 B 的 `sfho_frdm_bin.zip`，SHA-256 为 `45479eaf46e1aa9b1ca3502baf4aaeea60ff0021a21d621f10a75eafb8b8949c`，与目标清单一致。SPP（28,240,340 B）和 COMP（45,332,354 B）实际字节校验也通过。Manual 与 Shen98 的 digest 与 GitHub Release 资产元数据一致；本次 runner 未重新下载这两个资产，故将其标记为 Release-digest 核对，而非本地字节重算。
- **CI 修复：** Major 4.4 job 的 timeout 已提高到 90 分钟；将 concurrency 改为专属 `major44-eft-validation-${github.ref}` 组并设置 `cancel-in-progress: false`，避免新的提交或其他研究 workflow 中断正在运行的完整数值验收。C4C3 14 项 SHA-256 与 SFHo/FRDM 分块重组检查已在 Run #43149443570 实际通过。下一次 run 必须在当前 PR #56 head 上完整完成两组 unittest、reference scans、saved-output validation 和 figure regeneration，才可记为 CI 完整通过。
- **物理验收边界不变：** 纯矢量 B.16 的 10 MeV 强耦合端仍为约 `2.43963596e52 erg/s`，相对 Blinov Fig. 7 高约 `92.4284%`；Fig. 7 物理复现仍未通过。Run #158 的取消或后续 CI 通过均不能改变该物理结论，也不解冻生产轴矢量限制曲线。


> **P1-IIIe-B SFHo/FRDM v1.03 真实表数据与局域闭合（2026-11-11，后续数值修正）：** 官方 Basel 五个对象的获取器、五项 SHA-256 manifest 与 Release 归档已核对；Release tag sfho-frdm-v1.03-data 指向 e68eae83385dcb62b31b7fa12bf32f85a2e7a819，五个资产 digest 与 manifest 一致，总计 322,921,457 B。HTTP HEAD 的 --check-urls 只证明 HTTP 200 与 Content-Length 匹配，不被描述为远端内容哈希验证。224 点闭合采用 1024 阶 Gauss–Legendre；独立 1024/2048 对照在 448 个核子状态上的最大 Fdeg 绝对差为 4.7117e-8，数密度最大相对差为 1.0115e-8；1024 阶对 fixture 的最大 Fdeg 绝对差为 4.995e-11。旧 512 阶在冷、高密度中子状态可有 2.73% 偏差，因此 fixture 与原始表复算测试均已统一到 1024 阶。有效域仍为 224 点采样网格上的 208/224 格；中子最大偏差 6.1345e-4，质子（Xp≥1e-6）最大偏差 8.8578e-5。其余 16 格并非全部冻结：nB=1.10e-12 与 1e-10 fm⁻³ 的 8 格为明确平台；1e-8 的 4 格为过渡；1e-6 的 4 格更接近闭合但仍未满足 1e-3。16 格均为核子主导组成，Xn+Xp≈1，组成随 Yp 变化。自然单位稀释度在 T=63.096 MeV、nB=1e-6 fm⁻³ 时为 3.06e-5。核团比例统计代码已改为只使用 308 个物理密度行；由于本次未重读原始 composition archive，更新后的整表比例暂不作数值声明。五对象 Manifest、下载器与审计 JSON 的名称和哈希集合一致。本次独立 JavaScript fixture 交叉核验 12 组检查全部通过；这不是 Python unittest 运行结果。18 项 Python 测试（新增一项校验 vendored 分块布局）已在 head 5dd24ac 上、以 SFHO_TABLES_DIR 指向解包后的 v1.03 表重跑：P1-IIIe-A 15/15、P1-IIIe-B 18/18 全过。CI 也已在同一 head 通过（run 42922595906，success，23 s：fixture 路径 Ran 14 tests … OK (skipped=1)，四项原始表测试按设计跳过，自检断言块通过）。原始归档现已入库：spp/comp/manual 原样提交，161 092 071 B 的 extended 表拆为三个 60 MiB 分块，配 MANIFEST.sha256（7 条）与 reassemble_sfho_frdm_archives.py；往返重组与已发布文件逐字节一致（sha256 45479eaf…b8949c），shen98 仍只存 Release。本轮之前的「无新的 Python 测试或 CI 通过声明」等表述已被以上结果取代。

> **2026-11-10 纯矢量 Fig. 7 复现状态：** PR #57 已于 2026-11-12 合并至 PR #56 的研究分支（合并提交 `60c69a0b810b679a90683e638fc0a3bc9dd209e4`）；原始来源分支保留用于历史溯源。当前统一背景为 vertex-preserving profile B，SHA-256 为 `9fb14e796d6e7731f21993632af43ba2c6ed642ffe66b1e9de8ccbac240c001c`。B.1 独立源项、B.2 独立路径、B.1+B.2 端到端重组和局域碰撞核检查已有成功的数值验收记录；最新高阶独立网格 B.16 基准在 10 MeV 强耦合端为 `2.43963596e52 erg/s`，相对 Fig. 7 高出 `92.4284%`，尚未通过物理复现验收。能量/方向分箱程序已修正子区域掩码并加入回归测试，但高阶分箱结果尚未生成。最后一次有意触发的资源预检 Run [#42663539198](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42663539198) 仍在 runner 分配前失败，`steps=null`、`logs_url=null`、没有 runner ID；不再重复触发空跑。下一次执行固定为恢复 Runner 后或本地运行同一脚本，且必须通过完全相同的网格哈希、基准闭合和分箱归一化验收。

> **B.2 路径能量与径向插值的独立验收（2026-11-09）：** 固定 B.1 源项径向阶数 40、能量 100、角 16、路径 32，仅将 B.2 局域吸收率径向插值网格从 40 提高到 640。B.1 thin source 在所有插值网格间保持不变；三个质量点的最后两级 320→480、480→640 最大光度变化均小于 1%，因此独立 opacity 插值验收通过。两级变化分别为：0.1 MeV 0.4025%、0.1577%；1 MeV 0.1028%、0.0393%；10 MeV 0.00193%、0.00152%。但粗网格 40→640 对固定能量光度造成的最大变化分别达到 42.14%、9.73%、0.175%，说明此前低质量 B.2 基准存在严重的路径吸收率插值不足。采用 640 阶插值后，B.16 路径红移在峰值/强端的变化分别为：0.1 MeV −0.00747%/−5.9078%；1 MeV −0.51366%/−11.6001%；10 MeV −5.21614%/−28.8724%。这些结果取代原 40 阶径向插值下的低质量红移数值；它们仍是 B.16 矢量碰撞核下的 B.2 诊断，不是 B.13 精确核的传播结果。详见 [B.2 径向 opacity 插值收敛审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B2_OPACITY_INTERPOLATION_CONVERGENCE_2026-11-09.md) 与 JSON。Run [#42581429474](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42581429474) 全部通过。

> **B.13 低质量全局收敛状态（2026-11-09）：** 0.1、1 MeV 的 B.13 全局径向/能量/角/路径积分与全网格碰撞核阶数检查正在运行，当前尚无最终验收结果。已通过的局域核收敛不替代全局 B.1+B.2 收敛；同时，B.2 矢量基准已显示路径 opacity 插值网格是低质量区的重要数值维度，因此 B.13 全局结果必须结合其自身的路径插值分辨率审查，不能仅依据 source radial order 40→80 的变化作最终结论。

> **B.13 全局替换结果：** 在 10 MeV 纯矢量 benchmark 中，按单负缪子约定同时替换 B.1 Compton 源项和 B.2 Compton reduced opacity，得到弱端/峰值/强端偏差分别为 \\(-28.11\\%\\)、\\(-16.34\\%\\)、\\(+131.53\\%\\)。B.13 的 optically-thin 总源为 B.16 的 78.898%；B.13 负缪子 Compton 源为 B.16 Compton 源的 34.07%。源项与吸收项必须同时替换；source-only 和 opacity-only 结果仅为反事实诊断。该结果没有修复 B.16--Fig. 7 的差异，且尚不作为最终精度预测。

> **数值与 CI 状态：** B.16 同网格闭合残差为 0；B.13 详细平衡最大残差约 \\(1.5\\times10^{-14}\\)，最终缪子质量壳残差约 \\(3.7\\times10^{-13}\\)。最新局域碰撞核全网格审计 Run [#42565336032](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42565336032) 成功；当前 vertex-preserving profile B 上的固定能量/路径红移三质量审计 Run [#42568420651](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42568420651) 也成功，JSON 已归档为 `outputs/b16_global_redshift_audit_2026-11-09.json`，其 profile SHA-256 与当前 9fb14e... 完全一致。重复并发 Run #42568424558 的数值步骤通过，但在首个 run 已归档同名输出后发生 add/add 归档冲突，不构成计算失败。B.13 全局 quadrature Run [#42542328275](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42542328275) 的计算和数值验证步骤通过，但归档上传步骤失败；另一个径向/能量扫描 Run [#42536610504](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42536610504) 成功。因此 B.13 全局替换仍标为独立诊断，不宣称所有收敛输出均已完整归档。

> **正式版本文献边界：** JHEP 06 (2026) 155 的 Sec. 4.1 将 \\(\\omega\\) 描述为无穷远能量，而 Appendix B.1 的 \\(N(r)^2\\) 与 \\(m_V/N(r)\\) 下限对应源点局域能量；B.2 沿路径固定同一 \\(\\omega\\)。此外，论文给出完整 Compton 相空间式 B.13 及近似表达式 B.14--B.16，但 Fig. 7 文字没有明确指出数值实现采用哪一种，且文章未提供配套数据或代码。当前 B.16 仍是工作基准，不能据此声称已确认作者未公开代码的具体实现。详见 [能量与 Compton 处方文献复核](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_ENERGY_VARIABLE_AND_PATH_REDSHIFT_CONVENTION_AUDIT_2026-11-09.md)。

> **B.2 路径能量与径向收敛审计（2026-11-09）：** 三质量点 fixed-\(\\omega\) 与 path-redshift-only 计算已完成。最高测试网格下，强耦合端红移敏感性分别为 −5.64%（0.1 MeV）、−11.55%（1 MeV）、−28.85%（10 MeV）；该分支仍是固定 Euclidean chord 的敏感性诊断，不是完整 GR。能量、角度、路径积分的单维加密均通过 1% 筛选，但径向 60→80 节点变化在 0.1、1 MeV 分别仍达 7.63%、1.87%，因此低质量全局曲线尚未收敛。独立吸收率插值审计显示 0.1 MeV 需至少约 240–320 节点才进入 1% 稳定区间。现已增加 B.1 源径向阶数 80–200、同时固定 640 节点 opacity grid 的解耦审计，运行中。详见 [B.2 路径能量与径向收敛状态](research/stellar-cooling-constraints-20261105/blinov_reproduction/B2_PATH_ENERGY_AND_RADIAL_CONVERGENCE_STATUS_2026-11-09.md)。

> **B.13/B.16 三质量点对照（2026-11-09）：** 纯矢量 B.13 全局源项与吸收率已在 0.1、1、10 MeV 完整替换计算。主产生区 5--12 km 内，B.13/B.16 源项比约为 0.338、0.338、0.340；Compton 约化吸收率比约为 0.353、0.352、0.360。B.13 局域矩阵元在 (8 km,15 MeV)、(12.5 km,20 MeV)、(15 km,30 MeV) 的高阶积分检查均通过 0.1% 项目筛选阈值，0.1 与 1 MeV 的最大末级变化分别为 0.0283% 和 0.0288%。这不是全局 B.1+B.2 积分的收敛证明。三质量点的 Fig. 7 强耦合端偏差分别为 +0.33%、+138.84%、+131.59%；10 MeV 仅为超出低质量 Compton 适用区的压力测试。详见 [B.13/B.16 三质量点源项、吸收率与收敛审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_THREE_MASS_SOURCE_OPACITY_AND_CONVERGENCE_AUDIT_2026-11-09.md)。低质量局域核 Run [#42575922722](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42575922722) 通过。

> **B.16 约化 Compton opacity 解析化简（2026-11-09）：** 将 B.16、B.19 和 B.4 直接合并后，显式 Bose 因子严格抵消，得到 `Gamma_abs* = [16 pi alpha alphaV/(3 m_mu^2)] (n_mu F_deg) [1+mV^2/(2 omega^2)]`；B.2 光学深度还需除以 `vV`。因此路径红移不会通过残留 Bose 因子改变约化 Compton opacity，而是通过有限质量项和 B.2 的 `1/vV` 改变它。详见 [跨质量 opacity 与能量约定诊断](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_CROSS_MASS_OPACITY_AND_ENERGY_CONVENTION_DIAGNOSTIC_2026-11-09.md)。

> **22--25 km 中微子化学势敏感性（2026-11-09）：** 在当前 profile B 上，对 22--25 km 的 mu_numu 分别赋值 ±1、±3 MeV，并对每个情形完整重算 B.1+B.2。该壳层占 8--15 km 源项的 neutrino path-tau 19.1084%，但强耦合端逸出光度分别只改变 +0.0172% 和 +0.1505%；±号结果精确对称。说明该区间的路径吸收重要，但其未确定的 mu_numu 延拓在 ±3 MeV 测试范围内不是 Fig. 7 大偏差的原因。Run [#42572982267](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42572982267) 全部通过。详见 [22--25 km 中微子化学势敏感性审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_OUTER_NUMU_SENSITIVITY_22_25KM_2026-11-09.md)。

> **B.14 非相对论缪子近似诊断（2026-11-09）：** 使用 B.17 的 susceptibility 权重 (p^2 f_\mu(1-f_\mu))，并按低质量 B.16 源项径向权重 (r^2N^2(n_\mu F_{\rm deg})T^4) 加权，得到缪子平均速度约 0.761、rms 速度约 0.775；约 93.2% susceptibility 权重满足 (v_\mu>0.5)，约 71.7% 满足 (p_\mu>m_\mu)。约 79.1% 的低质量 Compton 源来自 8--12 km，该区间平均速度约 0.74--0.78。因此 B.14 的非相对论/无反冲近似在主要源区并非显然受控；这只是分布诊断，不等同于 B.13 速率误差，需由 0.1、1 MeV 的全局 B.13 对照定量判断。详见 [B.14 非相对论缪子近似诊断](research/stellar-cooling-constraints-20261105/blinov_reproduction/B13_NONRELATIVISTIC_MUON_APPROXIMATION_DIAGNOSTIC_2026-11-09.md)。独立脚本、测试和 JSON 已归档，Run [#42572394290](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42572394290) 全部通过。

> **跨质量 opacity/能量约定诊断（2026-11-09）：** 当前 profile B 的 0.1、1、10 MeV 结果显示：B.16 Compton 源项份额分别为 99.978%、97.870%、32.005%；Compton 对 source-weighted mean opacity 的份额分别为 99.931%、93.471%、10.222%。10 MeV 的中微子逆衰变贡献了 89.778% 的平均光学深度，且 20--25 km 占总平均光学深度 28.895%。路径红移诊断在 10 MeV 改善强端偏差（+92.24% 到 +36.74%），但在 0.1、1 MeV 分别使强端偏差从 -36.16% 变为 -39.35%、从 -5.35% 变为 -16.17%；因此它不是可全质量采用的修正。详见 [跨质量 opacity 与能量约定诊断](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_CROSS_MASS_OPACITY_AND_ENERGY_CONVENTION_DIAGNOSTIC_2026-11-09.md)。

> **方法重建纠正（2026-11-09）：** 缺少同快照 A(r)/M(r) 不妨碍复现 Blinov 发表版 Appendix B。其 B.1 使用 lapse 的 N(r)^2 与 m_V/N(r) 局域发射能量处方；B.2 明确使用欧几里得直线弦，未包含 A(r)、proper-distance 因子或测地线弯曲。这与其引用的 Caputo et al. arXiv:2201.09890 Supplemental C 一致：Garching pseudo-Newtonian 模型采用平直空间坐标，lapse 负责发射能量红移和 N^2 光度因子。A(r)/M(r) 仅是完整 GR 扩展所需，不是 Fig. 7 论文处方复现的前置条件。B.1 的局域源能量与无穷远守恒能量已通过精确 Jacobian 变换和独立数值积分验证为完全等价，三个通道的相对残差均为 0；对应 Run [#42573725261](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42573725261) 通过。唯一剩余的能量约定问题是 B.2 沿路径固定 omega 是否为字面局域能量，还是作者数值实现中隐含了 E_infinity/N(r')。详见 [发表版引力与能量处方重建](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_PUBLISHED_GRAVITY_AND_ENERGY_PRESCRIPTION_RECONSTRUCTION_2026-11-09.md)。

> **物理输入边界：** Caputo 的 T(r) 与 mu_mu/T 在 5--20 km 与 Bollig Figs. 1、4 的直接矢量曲线交叉吻合；原始 Fig. 4 明确支持 Caputo 而非 Ferreira 的 mu_mu/T digitization。Caputo 的绝对 n_mu 与其自身 Fermi 积分一致，但 Bollig Fig. 3 的密度在 5--15 km 平均低约 5%，12--15 km 低约 8.8%；B.17 使用的是同一 T, mu_mu 分布决定的 susceptibility n_mu F_deg，不得按 Fig. 3 密度比直接重标度。20--25 km 的部分热力学输入仍属图像外延或未分辨分支。lapse N(r) 在 0--20 km 还得到 Zuowei Liu 2026-10-31 会议报告 slide 65 的独立视觉交叉支持，但这不是机器精度验证。原始 20--25 km 热力学剖面仍未完全核验；同快照 A(r)/M(r) 只影响可选完整 GR 扩展，不阻碍按论文 B.1--B.5 复现。

> **原始数据获取审计（2026-11-09）：** 官方 Garching 目录列出的 Bollig/Hüdepohl 径向 hydro 数据、径向中微子数据以及 Robert Bollig 的 Python TOV solver 入口均返回 HTTP 401；官方目录明确说明部分档案需密码并要求联系数据负责人。arXiv:2610.35379 的后续研究同样指向 Garching archive，而不是提供独立公开镜像。当前没有获得同一快照的原始 (A(r))、(M(r)) 或 hydro 表。详见 [公开 profile 与 metric 数据可用性审计](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_PUBLIC_PROFILE_AND_METRIC_SOURCE_AVAILABILITY_AUDIT_2026-11-09.md)。不绕过访问控制，不以通用 TOV 求解器或其他快照替代原始数据。

> **方法边界：** Fig. 7 工作基准继续采用 Appendix B.2 字面给出的标量、偏振求和吸收率；逐偏振传播、路径红移和 B.13 精确移动缪子计算保留为独立诊断。没有进行经验性源项/吸收率/光度重标度，没有修改生产轴矢量曲线、论文正文或正式回复信。只有纯矢量基准通过独立物理验收后，才解冻轴矢量限制曲线。最终验收结论见 [B16_VECTOR_BENCHMARK_ACCEPTANCE_GATE_2026-11-09.md](research/stellar-cooling-constraints-20261105/blinov_reproduction/B16_VECTOR_BENCHMARK_ACCEPTANCE_GATE_2026-11-09.md)：数值模块通过，但 Fig. 7 物理复现未通过；PR #57 保持 Open / Draft。

> **2026-11-07 矢量 benchmark 更新：** 作者指定仅复现 Blinov et al.，采用现有重建剖面，不要求精细恒星模型或原始表作为前置条件。已定量对照该文 Fig. 4，发现偏振求和吸收率与逐偏振单粒子宽度的区别；完整 Fig. 7 中 10 MeV 光度仍有差异。旧“矢量端点 223 MeV”是稀疏采样误读，当前逐偏振计算闭合点约 259.1 MeV。详见 [矢量 benchmark 核查](research/stellar-cooling-constraints-20261105/VECTOR_BENCHMARK_AUDIT_2026-11-07.md)。PR #56 仍为 Draft；这些诊断并不构成最终物理验证。

**历史基线快照日期：** 2026-11-06（PR #38–#50 已合并；PR #54、#55 已合并；PR #52 Closed / 未合并且保留研究分支；PR #53、#56 Open / Draft）。当前研究状态以本文档最上方的 2026-11-09 摘要及对应验收报告为准。

## 2026-11-09 最终更新：PR #67 回复信写作风格统一（已 Squash merge）
[PR #67](https://github.com/lm846802297-bit/axial-vector-review-response/pull/67) 从 PR #66 合并后的 main 基线 `d3b234efbce270cd92b7ea55e31e02680114fc3a` 创建，分支为 `review/referee-response-style-20261109`。本节记录最终编译、视觉检查、独立审稿人视角 diff 复核及最终合并状态。

- **检索与写作依据：** 已核对原论文 `main-v6.tex`、正式回复信、长期写作规范、正文待同步清单、DEC-15 及 PR #64/#65 修订台账。英文科研文体以原论文 Abstract、Introduction、Model Setup 和 Conclusion 为直接参照；未将模型生成的中文材料误作个人英文写作样本。
- **回复信内容：** S-01–S-20 的语言与段落组织修订均保留。非中微子问题继续采用原论文单 VEV `S+\mathrm{VLL}` 模型；可选 `\sigma+3N_R` seesaw 仅用于 Major Points 3/4.1。未修改论文正文、bibliography、图表、科研脚本、物理推导或实验结论。
- **最终编译：** GitHub Actions [Run #121](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42562306315) 成功，构建提交为 `de61388aedefa30edee59b127ff63f7f45b3a4dd`。当前分支 TeX 与该构建输入逐字一致，唯一差异是构建后移除的一行临时 LaTeX 注释。PDF 已由该工作流提交到 PR 分支。最终 PDF 为 58 页 A4、444,658 bytes；BibTeX 处理 41 条文献；最终 LaTeX 检查无未解析引用或交叉引用；字体全部嵌入；无 Overfull 警告，保留一处轻微 Underfull `\hbox`。PDF SHA-256：`6583031a7dea51abfb7e48207ae5b39e90892f9e5bde6eff2f45dd854292aabf`。
- **视觉检查：** 58 页均已渲染，并通过 10 份联系表逐页检查；未发现公式裁切、表格列越界或页面重叠。第 5 页留白仍存在，原因是 Table II 整体排至第 6 页；第 58 页参考文献位于页面上部、底部留白较大。这两处均为非阻断性分页现象。
- **Table II 排版：** 保留 `\small`、三列宽度、所有表格文字、数值和引用；将 `center` 环境改为局部 `\centering` 分组，并将行间距从 3 pt 降至 1.5 pt。规范化间距后，表格内容与原版逐字相同。此调整没有将整张表移回第 5 页。
- **参数窗口复核：** Major Point 2 和 Minor Point 1 均明确写出 Fig. 2 的显示范围 `10^{-6}\leq g_X\leq1`，即上限为 `10^0=1`，与原图一致。动能混合部分的 `g_X=0.1` 是数值表的参考归一化；正文明确说明 Fig. 2 延伸至 `g_X=1` 时相应估计放大十倍，两者不矛盾。
- **独立审稿人视角 diff 复核：** 对 PR base 至当前 head 的实际 diff 逐项复核。27/27 个 reviewer quote block、137/137 个 `\[...\]` 显示公式块、4/4 个 equation 环境、48 条 citation commands（74 次 citation-key 出现、41 个唯一 keys）、4 个 equation labels 及 4 个 ref/eqref 均保持一致。LaTeX 花括号净计数为 0；除 Table II 有意将一个 `center` 环境替换为局部分组外，其余环境 begin/end 计数不变。表格内容经间距规范化后完全一致；Minor Point 5 的宽度公式仅移动位置，没有改变公式或数值。未发现物理结论、公式、benchmark、适用条件或引用被误删，也未发现新增的未经支持的物理主张。
- **清理：** 10 份临时联系表已从分支删除；临时构建触发注释已删除；临时 workflow allowlist 已从 main 工作流恢复；PR 仍仅包含 4 个预期文件（PROJECT_STATUS、正式 PDF、正式 TeX、修改清单）。
- **独立审查边界：** 已完成一次独立视角的第二遍 reviewer-style diff 审计，结论为无阻断项。该审计是本轮复核记录，不冒称第三方 GitHub reviewer 的正式批准。PR #67 已由 Draft 转为 Ready for review，并于 2026-11-09 Squash merge 至 main；合并提交为 `144bf8ab444a328587d8bfa82ea375355dd2b40b`。

**合并结论：** PR #67 已成功合并；正式回复信 TeX、58 页 PDF、项目状态记录和完整修改/审查清单均进入 main。论文正文、bibliography、图表和科研脚本未修改。
## 2026-11-09 更新：回复信文献库单文件化（独立 PR）

- 正式回复信 `Replies_to_Referee_3_referee_facing_2026-11-04.tex` 的文献调用统一为 `\bibliography{references}`。
- 新增仓库根目录 `references.bib`，合并原论文文献库中的 166 条记录，以及回复信专用的 2+2 条补充记录；共 168 条实际文献记录，168 个 citation keys 唯一；已排除两项 REVTeX 专用 `@CONTROL` 控制条目。
- 正式回复信的 41 个实际引用键均在合并文献库中找到；未发现缺失或重复键。
- 删除不再单独调用的 `Replies_to_Referee_3_neutrino_references.bib` 和 `Replies_to_Referee_3_additional_references.bib`。原论文目录 `overleaf-source/axial-vector-model-building-v6/references.bib` 保持原样，论文正文及历史版本不受影响。
- 根目录现有 `JHEP.bst` 继续作为回复信的文献样式文件。
- **后续约定：** 独立回复信/Overleaf 项目默认维护单一 `references.bib`；只有在确有独立文献体系时才拆分。论文正文继续使用其项目目录下自己的 `references.bib`。

**构建验收：** GitHub Actions [Run #133](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42565134337) 成功。LaTeX/BibTeX 编译通过；BibTeX 无 missing-entry/database warning（`warning$ -- 0`）；最终 LaTeX 日志无未解析引用/交叉引用；PDF 字体全部嵌入，无 Overfull 警告，保留一处轻微 Underfull `\hbox`。PDF 为 58 页 A4、444,658 bytes；所有页面均已由工作流渲染。新 PDF SHA-256：`a58f2fcf38ddc8d7aa6a3dff6f1ccd3f5a258534778f130ba497632c5334c38b`。
**工作流清理：** 为本次 PR 临时增加的分支白名单和 `references.bib` 触发路径已恢复；PR 最终 diff 不包含 workflow 修改。
**当前状态：** PR #70 保持 Open；单文件文献库源码、更新后的 58 页 PDF 和状态记录均已提交到 PR 分支，等待最终审查与合并。


## 2026-11-09 更新：PR #64 已合并

[PR #64](https://github.com/lm846802297-bit/axial-vector-review-response/pull/64) 已 squash merge 至 main，合并提交 `1e487bbdf79906489eb85651d05ddf830949acf0`。正式回复信结构、第二轮措辞精简和标量约束表分隔线均已进入 main；论文正文未修改。合并前独立审查记录覆盖科学论证及随后纯排版 diff，本地对相同回复信源码完整编译生成 56 页 PDF；只对表格和部分页面放大检查、全页缩略图巡检，未进行全 PDF 逐页高分辨率验收。GitHub 构建项为 SKIPPED，未做数值复算或新文献核验。仓库根目录历史 PDF 不应视为与此次 TeX 同步；后续需生成并核验正式交付版本。

Major 1.3 的 10–150 GeV 诊断不是全微扰质量范围扫描，Major 4.4 未形成完整轴矢量 SN1987A 输运／排除曲线；论文正文同步仍待基于作者选定的活动源码实施。

## 2026-11-09 更新：PR #64 回复信标量约束表排版

按作者要求，在 Major 1.1 的六项标量约束之间添加横向分隔线及留白，便于区分限制；移除新增排版命令后 TeX 与上一 head 完全一致，未改数值、公式、引用或适用条件。本地重新编译得到 56 页 PDF，并放大检查第 6 页表格；此局部检查不代表全 PDF 的逐页高分辨率验收。此前独立科学审查针对 `e8b69296`，本次排版 diff 已由修改者核对，尚无新的 GitHub review。未修改论文正文。

## 2026-11-09 更新：PR #64 独立差异审查

独立审查者核对了 base `b5115cee` 至回复信 head `e8b69296` 的实际 diff 和删除／合并台账；审查范围内未发现独立物理结论、计算证据或关键条件被误删，防御性措辞没有阻止合并的问题。详细结论和未解决项见 [独立审查记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-09/PR64第二轮独立审查记录_2026-11-09.md)。本记录不等于 GitHub review。本地对 56 页 PDF 做全页缩略图巡检，并对受影响页面及表格做局部放大检查；不视为全部页面高分辨率逐页视觉验收。GitHub 检查显示 SKIPPED。论文正文未修改。

## 2026-11-09 更新：PR #64 第二轮防御性措辞精简

PR #64 在独立审查基础上精简 Major 1.3、2、3、4.2–4.4 和 Minor 5、6.5 的重复措辞，保留各项计算和科学适用条件；Minor 6.3 的 Belle 数值为直接回答审稿问题而保留。逐项对照见 [第二轮措辞修订台账](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-09/PR64第二轮措辞修订与保留台账_2026-11-09.md)。本地完整 LaTeX/BibTeX 编译生成 56 页 PDF；逐页视觉检查、CI 和数值复算未执行。作者修改者自查不替代独立 review。Major 1.3 全微扰区间扫描和 Major 4.4 完整 SN 输运曲线仍未完成；论文正文未修改。

**状态快照日期：** 2026-11-09（PR #38–#50、#54–#55、#60–#61、#63–#66 已合并；PR #53/#56/#57 Open / Draft；PR #52/#62 Closed / 未合并；PR #67 Merged（Squash merge））

**本状态快照的初始核验基线：** 243b0e62d9c3912525d1144971a1e81c2af84db7（PR #36 合并前）  
**项目启动机制合并提交：** [9b4e17519230e9eef65b34b643d3a1f8c19f46a2](https://github.com/lm846802297-bit/axial-vector-review-response/commit/9b4e17519230e9eef65b34b643d3a1f8c19f46a2)  
**用途：** 每次启动项目时快速恢复当前阶段、权威文件和下一步工作。本文件是可更新的状态快照，不替代物理推导、原始论文、计算证据或作者最新指示。

> **更新原则：** 任务完成、作者改变观点、PR 合并、论文基线更换或计算结论更新后，应检查并更新本文件。尚未重新核验的内容标为“待核验”，不得沿用旧状态作确定陈述。

## 2026-11-09 更新：Major Points 2–4 回复结构调整（PR #64）

[PR #64](https://github.com/lm846802297-bit/axial-vector-review-response/pull/64) 从当前 `main` 的 `b5115cee164561c881ef58e44c2bc1bb77d6c6f1` 创建，工作分支为 `review/major-response-structure-20261109`，合并前为 Open。目标是统一落实“总体回复简洁、具体子回复提供充分物理依据、公式和定量结果”的组织原则。

- **Major 2：** 总体 Reply 压缩为显示窗口及其非普适边界的说明；原有实验覆盖、低/高质量端理由、规范与 Yukawa 微扰性、标量质量条件和 Fig. 2 区域解释均保留，并增加主题导航。
- **Major 3：** 将结尾的总体审稿人 quote 移至开头，合并重复的总体回复；3.1/3.2 的残余对称性、Weinberg 算符、质量矩阵、type-I seesaw、逆重构、PMNS、异常与双 VEV 适用范围推导均保留。
- **Major 4.1：** 保留对 \(U_{\rm PMNS}=\operatorname{diag}(1,U_{23})\) 的直接回答、可选 \(\sigma+3N_R\) 场内容、seesaw 重构和双 VEV 边界；将与 Major 3.1/3.2 重复的详细推导改为交叉引用。
- **Major 4.2–4.4：** 保留现有公式、数值、实验比较和适用条件，增加主题标题；Major 4.3 增加简洁总体回答。
- **长期规范：** 《审稿回复写作原则》新增强制 §5.1，明确 Overall Reply 与具体子回复的职责。
- **内部记录：** [Major 2–4 回复结构审查与修订记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-09/Major2-4回复结构审查与修订记录_2026-11-09.md)列出修改前后基线、内容保留、移动/合并台账及验证边界。
- **静态核查：** TeX 132,901 → 130,069 字符；39 个唯一引用键及其集合不变；equation labels 不变；花括号与 LaTeX 环境配对通过。引用出现次数 80 → 72，减少项来自重复段落及 Minor Point 6.2 旧表述中的重复引用。Minor Point 6.2 现以三句正面说明 representative 的含义、来源归一化/质量范围/源假设及表格用途。
- **未执行：** 完整 LaTeX/BibTeX 编译、PDF 逐页视觉检查、数值重算、文献重新核验和全仓库测试。论文正文、图表、BibTeX 与科研脚本未修改。

**下一步：** 独立审查者检查 PR #64 的实际 TeX diff 与删除/合并台账；通过后再进行最新回复信的完整编译和 PDF 视觉检查。PR #64 不自动合并。


### 2026-11-09 追加：PR #64 全信防御性措辞审查

作者确认后，对 PR #64 正式回复信完成一次全信防御性措辞审查，目标是删除不增加科学信息的重复免责声明，同时保留必要的物理适用条件。

- **Major 1.3：** 合并局部 Higgs-pole 诊断窗口与非全局扫描说明；以正面措辞说明 scalar-suppressed benchmark 是 \(A'\) effective-current 与 scalar-mediated observables 的现象学分离，且 \(s\) 仍是 UV 物理自由度。CP-even scalar-bubble、soft bubble-plus-contact、fermionic hard subcalculation、mixing-only rate、complex-pole、near-degenerate diagnostics 等不同计算层级的独立限制全部保留。
- **Major 2：** 将 plotting-window 的非普适性集中说明一次；精简实验覆盖、耦合端点、表格和总结中的重复解释。保留低质量 \((g-2)_\mu\) 渐近式、约 \(0.57\,\mathrm{MeV}\) 交点、天体物理重叠、实验质量覆盖、规范/VLL Yukawa 微扰性和逐点标量条件；Fig. 2 的四种区域解释保留。
- **Major 3/4.1：** 只精简结尾重复的模型边界说明；可选 \(\sigma+3N_R\) 完成机制与原单 VEV 模型的区分、双 VEV 适用条件、全部矩阵和 seesaw 公式保留。
- **Major 4.3 / Minor 3–4：** 合并重复的混合角免责声明；保留独立角度条件、矢量/轴矢量比值、LEP 对照、VLL fit 适用性及原有引用。
- **Major 4.4：** 将防御式结尾改为 neutrino coalescence、charged-muon axial semi-Compton、kinetic-mixing-induced electromagnetic processes 的正面过程分类；详细输运和适用范围限制保留。
- **Overall Summary：** 改为概括已给出的 seesaw 构造、动能混合、有限矢量效应、Table II 和恒星冷却过程区分；删除泛化的全局排除免责声明。
- **静态核查：** 本轮 TeX 字符数 \(130{,}069\rightarrow128{,}331\)；72 次引用出现、39 个唯一 citation keys、equation labels 均保持不变；LaTeX 环境栈与花括号检查通过。
- **验证边界：** 仅完成源码级静态核查；完整 LaTeX/BibTeX 编译、PDF 逐页视觉检查、数值重算、源文献重新核验和全仓库测试未执行。论文正文、图表、BibTeX 和科研脚本未修改。

**删除/合并记录：** 仅合并相同命题、相同适用条件的重复总结；没有删除独立物理结论、公式、数值 benchmark、引用或计算适用范围。详细逐点记录见 [Major 2–4 回复结构审查与修订记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-09/Major2-4回复结构审查与修订记录_2026-11-09.md) §7。PR #64 仍待独立 reviewer 检查实际 diff；不自动合并。

## 2026-11-06 更新：PR #55 Minor Points 论证扩充与长期写作规范（已合并）

[PR #55](https://github.com/lm846802297-bit/axial-vector-review-response/pull/55) 已于 2026-11-06 Squash Merge 至 main，合并提交为 [7ef9a4a65fc0f9afd25ed857325760775faf71bd](https://github.com/lm846802297-bit/axial-vector-review-response/commit/7ef9a4a65fc0f9afd25ed857325760775faf71bd)。以下保留该 PR 的正式回复信与写作规范修改记录。

- **正式回复信：** 在此前 Major 3、Major 4.2、Major 4.3 和 Minor 6.5 结尾修订基础上，进一步扩充 Minor 1–5、6.1、6.2、6.4、6.5、6.6；Minor 6.3 经核对保持不变。所有非中微子问题继续采用原论文单 VEV \(S+\mathrm{VLL}\) 模型。
- **后续最小纠错：** Major 3 明确原始 \(S\)-only 模型与可选 \(\sigma+3N_R\) seesaw 的区别；Major 4.3 统一 \(\mu/\tau\) 的带符号耦合并将 small-mixing 统一称为 condition/domain；Minor 3 澄清带符号耦合与绝对值；Minor 4 澄清四个混合角分别受同一数值上限约束而非彼此相等。另补充 Major 2 的 VLL Yukawa 微扰性依赖、Major 4.2 的保守不等式和 Major 4.4 的完整超新星输运限定。Major 1.3 的局部扫描边界保持不变。
- **新增物理论证：** Minor 5 增加 \(A_{\rm LR}^\mu\)、\(P_\tau\) 的手征振幅解析投影、\(A'\) 总宽度部分道分解、\(ee\) 通道高动量 kinetic-mixing 适用性以及 \(e^+e^-\to Zs\) 的 Higgsstrahlung 缩放关系；Minor 6.5 从两个活性 chiral-neutrino 道推导寿命上界、boost 后飞行距离和 dimuon 阈值抑制。没有加入未经复核的 collider reach 数值。
- **长期规范：** 在审稿回复写作原则新增强制 §2.2「论证充分性原则：从结论陈述到可复核的物理论证」，并同步 §5、§6、§6.1、§7。覆盖物理原因、公式来源、benchmark/近似/数值意义、实验适用性映射和多子问题逐项回答；强调不机械增加篇幅。
- **内部记录：** Minor Points 论证扩充与复核记录、全信结尾修订审查记录均已写入 2026-11-06 目录。
- **静态验收：** 78 次引用出现、39 个唯一 citation keys 全部解析；LaTeX 环境配对、花括号、标签和交叉引用检查通过；Minor 6.3 与 main 原段落逐字一致。
- **完整 LaTeX/PDF 验收：** 已通过 GitHub Actions Run [#3](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42146091113) 对 PR 分支源码完成 `latexmk -g -pdf -bibtex` 编译；最终 PDF 为 59 页 A4，根目录文件为 [Replies_to_Referee_3_referee_facing_2026-11-04.pdf](Replies_to_Referee_3_referee_facing_2026-11-04.pdf)，生成提交为 `8c21ff02a216e636e1655ddb0d1c38488ec6714b`。最终 LaTeX `.log` 无未解析引用/交叉引用，BibTeX `.blg` 无缺失条目或数据库错误；59 页均以 150 dpi 渲染并完成人工页面预览检查。未发现公式/表格裁切、缺字、溢出页边距、空白页或异常分页。仅有一处非阻塞 `Underfull \hbox`（badness 1199，TeX 第 555–557 行），未发现 `Overfull`。
- **本轮未涉及：** 论文正文、图表和 BibTeX 数据库均未修改；完整数值脚本 clean-environment 重跑、detector-level collider 模拟和全仓库测试套件仍未执行。Actions 仅用于正式回复信编译、引用检查和页面渲染。

**合并状态：** PR #55 已合并至 main。其 59 页正式回复信 PDF 和视觉验收记录保留在本节；后续 Major 4.4 的轴矢量 EFT 冷却计算由独立 PR #56 处理。

## 2026-11-06 历史快照：PR #56 Major 4.4 轴矢量 EFT 恒星冷却 benchmark（当时 Open / Draft，2026-11-12 合并）

[PR #56](https://github.com/lm846802297-bit/axial-vector-review-response/pull/56) 保持 Open / Draft，分支为 `codex/major44-axial-cooling-constraints-20261105`；**尚未合并**。

- **与 PR #53 的区别：** PR #53 继续研究原论文单 VEV UV 模型的完整恒星冷却匹配；PR #56 是专门支持 Major 4.4 的固定剖面轴矢量 EFT ballistic-cooling benchmark。PR #56 使用原论文的低能电流归一化 \(g_A^\mu=-g_X\)、\(g_V^\mu=0\)、\(g_{\nu_\mu}=+g_X\)、\(g_{\nu_\tau}=-g_X\)，不引入新的 UV 场、不采用双 VEV 映射，也不把 Major 3 的可选 seesaw 带入本计算。
- **回复信整合：** Major 4.4 增加轴矢量半康普顿、三偏振输运、三通道竞争、冷却带和数值敏感性；Major 2 增加新图交叉引用；Summary 与新恒星物理参考文献同步。正式回复信仍不包含 PR、CI 或内部任务状态。
- **数值验收：** 19 项单元测试通过；28 个独立振幅对照点的最大相对误差为 \(2.8801\times10^{-12}\)；75 个基准质量点、80 个轴矢量绘图质量点、每点 301 个耦合。冷却带的质量端点位于 255–260 MeV；10 MeV 薄极限半康普顿份额约 91.4%，100 MeV 中微子份额约 99.4%。
- **PDF 验收（历史构建，2026-11-06）：** Run #42230873049 在旧 head `403915f7eea0feead83b6bb78a64fb50c3ad56fe` 上构建了 65 页 A4 PDF，并完成 150-dpi 全页渲染、PDF 结构、字体和引用检查；该构建的历史 SHA-256 为 `cc998df36c809fd47acf8d714b1c286e1d4d1f7a8f1a56cd4df0cd27540832ea`。它早于 2026-11-09 至 11-12 的后续 TeX 修改，不能作为最终合并版 TeX/PDF 的同源验收。当前根目录 PDF（commit `293d047`）为 500,497 bytes、SHA-256 `e0a2114e5e932d02794a1cdf074c9214ed201f71ff37fc25a72314af05ed4051`；必须对当前 TeX 重新执行完整 LaTeX/BibTeX 构建和逐页渲染后，才能恢复“当前 PDF 已验证”的状态。此前末页只有最后一条参考文献，但不是空白页；缩小整套参考文献字号未减少页数，因此恢复标准字号。
- **GeV 对比图：** 新增 outputs/axial_stellar_constraints_gev.png/.pdf，完全复用已有扫描数据，只将质量坐标由 MeV 转为 GeV；原宽版 MeV 图和回复信版 MeV 图均保留。阴影只标示当前面板与 Fig. 2 展示窗口的可见交集，不表示重绘 Fig. 2 全部范围。
- **GeV 竖版回复信图：** 新增 outputs/axial_stellar_constraints_reply_gev.png/.pdf；与 GeV 宽版使用同一数据和坐标变换，采用上下两面板竖排，并在下方面板保留完整的 “Fraction of optically thin axial luminosity” 纵轴标签。正式回复信 TeX 已切换到新 PDF，根目录回复信 PDF 已重新编译。
- **图形验证：** GitHub Actions Run [42230567245](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42230567245) 通过：19/19 单元测试、28 组独立半康普顿振幅对照（最大相对误差 2.8801e-12）、保存扫描检查及四类 MeV/GeV 图形再生成和发布均成功；GeV 竖版回复信 PNG 已完成视觉检查。最终 PDF 构建见 Run [42230873049](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42230873049)。
- **边界：** 这是指定剖面和所列通道下的条件性 ballistic benchmark，不是完整超新星流体模拟、全介质输运、LESN/高能中微子重铸或完整 UV 参数空间排除。论文正文未修改。PR #56 保持 Draft，等待作者审阅与明确合并决定。

## 2026-11-05 更新：模型范围纠正与研究 PR 替代关系

PR #50 已于 2026-11-05 Squash Merge 至 main，合并提交为 [51a245b0a36703f40c24ca469d6969e70abc8954](https://github.com/lm846802297-bit/axial-vector-review-response/commit/51a245b0a36703f40c24ca469d6969e70abc8954)。本次进一步纠正研究范围：Major Point 3/4.1 的额外中微子完成机制只属于对应问题的专门回复论证，不改变原论文 UV 场内容，也不改变其他审稿问题的模型基准。

**2026-11-05 统一原则（DEC-15）：** 原论文单 VEV 模型是所有非中微子问题的默认基准；Major 3/4.1 可独立讨论中微子机制；不同模型公式和实验限制不得未经重新推导或 matching 直接混用；回复信讨论扩展不代表论文已采用；每个问题必须明确模型、场内容、理论输入、参数关系、近似、适用范围和证据来源。目标是回应原论文的审稿质疑，而不是逐步把论文扩展成另一个 UV 模型。详见研究决策登记表 DEC-15 与审稿回复写作原则 §2.1。

- **旧 PR #30：** 已关闭且未合并；其错误采用双 VEV 映射的 PR #51 也已关闭且未合并。现由 [PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) 替代。PR #53 从当前 main 创建，严格使用原论文单 VEV 模型 \(m_{A'}=2|g_X|v_s\)、\(G=a_s\)，保留通用电流半康普顿振幅和局部热率计算。六项单 VEV 映射测试通过；介质静止系 T/L opacity、trapping、SN profile 和最终 SN1987A/LESN 曲线仍未完成。
- **旧 PR #32：** 已关闭且未合并；现由 [PR #52](https://github.com/lm846802297-bit/axial-vector-review-response/pull/52) 替代。PR #52 从当前 main 创建，研究原论文的单 VEV 径向标量，保留 Belle II 来源台账、重铸协议、逐点分类框架和部分宽度计算器。Belle II 逐质量补充数据提取、实验 benchmark 复现、完整宽度/分支比/寿命、产生率、接受度和质量扫描仍未完成。
- **PR #52：** 已 Closed、未合并；其研究分支 `research/radial-scalar-original-model-belleii-20261105` 仍保留，研究成果未合并、未删除。
- **PR #53：** 保持 Open / Draft；其研究分支 `research/stellar-cooling-original-uv-model-20261105` 独立保留。
- PR #52/#53 均不修改论文正文或正式回复信，也不是当前审稿回复的前置条件。PR #56 仅补充正式回复信 Major 4.4 的条件性轴矢量 EFT 冷却论证和图，不修改论文正文，也不引入额外中微子场。旧 PR 的讨论和提交保留作历史溯源，不合并其错误模型范围的提交。

- **PR #54：** 已合并至 `main`，合并提交为 [`0f3816e3e62dd7668fca1d4aee5e8749708f99f2`](https://github.com/lm846802297-bit/axial-vector-review-response/commit/0f3816e3e62dd7668fca1d4aee5e8749708f99f2)。该 PR 修正正式回复信中 Major 1、2、4.2、4.4 对 Major 3 扩展的跨问题引用，并将中微子完成机制限定为 Major 3/4.1 专门回复内容。

**统一模型边界：** 除 Major Point 3/4.1 的专门中微子回复段落外，所有非中微子审稿回复和专题研究均以原论文 \(S+\mathrm{VLL}\) 单 VEV UV 模型为准。不得将 Major Point 3/4.1 中讨论的可选扩展机制作为原论文已经采用的场内容。
## 2026-11-05 更新：PR #53 原论文单 VEV 轴矢量恒星冷却计算（Draft）

[PR #53](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) 从当前 main 的 `d3c8c573e0b219dbcb4be62dc57f77fdc04c4f96` 创建，替代旧 PR #30 及错误采用双 VEV 映射的 PR #51；两者均关闭且未合并。

- **原论文模型映射：** \(S=(v_s+s+ia_s)/\sqrt2\)、\(Q_X(S)=2\)、\(m_{A'}=2|g_X|v_s\)、\(G=a_s\)。在小 VLL 混合 benchmark 下 \(y_{s\ell\ell}=m_\ell/v_s\)，Goldstone/current 关系为 \(m_\ell/v_s=2|g_A^\ell|m_\ell/m_{A'}\)（\(|g_A^\ell|=|g_X|\)）。
- **保留的计算：** 显式 Dirac 旋量半康普顿振幅、EM Ward identity、实验室系/CM 截面对照、Klein–Nishina 对照、轴矢量纵向标度、均匀介质局部热产生率及积分阶数/截断扫描。
- **原模型中微子规范流边界：** \(A'\to\nu\bar\nu\) 仅使用原论文 \(L_\mu-L_\tau\) 活性味规范流（无质量近似下的 \(\nu_\mu,\nu_\tau\)，电子味不耦合）；不引入额外中微子态或质量完成机制。
- **本地验收：** 单 VEV 映射测试 6/6 通过；通用电流半康普顿振幅的 Ward residual 分别为 \(2.252\times10^{-9}\)、\(2.159\times10^{-9}\)；热率 order 10→12 的率和发射率变化分别为 0.0108% 和 0.0202%。详细数值见 PR #53 的 validation record。
- **分支比口径：** PR #53 的 \(\mathrm{BR}_{\nu\bar\nu}\) 数值仅为保留 \(\nu\bar\nu+\mu^+\mu^-\) 的两通道近似；动能混合诱导的 \(e^+e^-\) 及其他开放道未纳入，不能当作完整物理分支比。
- **未完成：** 介质静止系 T/L 分辨吸收、opacity、trapping、SN profile、diffusion 和最终 SN1987A/LESN 曲线；不声称已得到超新星排除。
- **范围：** PR #53 保持 Open / Draft；不修改论文正文或正式回复信。

## 2026-11-05 更新：Major Point 1.3 公式链条与近极点诊断补强（PR #49，已合并）

[PR #49](https://github.com/lm846802297-bit/axial-vector-review-response/pull/49) 的基准为 main SHA 4abcf13c45789f75deee27a4b6a3cc9480639448，分支为 review/major1.3-higgs-portal-higgs-strength-20261104，已于 2026-11-05 合并至 main。本轮仅修改回复信及其内部证据/同步文档，不修改论文正文。

- **P0：** 正式回复补入 \(2\times2\) charged-lepton/VLL 质量矩阵、规范基底 \(h,s\) Yukawa 顶角、质量本征态旋转、\(C,D,K\) 定义和完整质量本征态一圈费米子自能公式。
- **P0：** 补入 exact full-minus-light EFT subtraction、保留的 bubble-plus-contact soft 子集，以及 hard/soft 数值分解。将结果记为 \(\Pi_{hs}^{\mathrm{ret}}\)，并明确该 soft 子集不是完整同阶 EFT soft/counterterm 集，避免把条件性数值写成完整 UV pole 预测。
- **P0：** 修正“zero-tree-level-mixing”歧义：\(\lambda_{HS}^{\mathrm{EFT}}(M_E)=0\) 是匹配 EFT 的局域混合边界；对应 \(\lambda_{HS}^{\mathrm{UV}}(M_E)=-\Delta\lambda_{HS}^{E}\ne0\)。补充 portal-induced mass entry 与 loop counting。
- **P0：** 将 \(\mu_h^{\mathrm{pole}}\) 改为 \(\delta\mu_h^{(\mathrm{mix,LO})}\)，明确它是 mixing-only leading rate diagnostic，而不是完整物理 pole signal strength。
- **P1：** 明确 \(m_s\) 是未混合对角质量输入；补充 \(\Gamma_s(s\to A'A',\mu^+\mu^-,\tau^+\tau^-)\) 公式及 Benchmark B 的开闭道条件、宽度和非简并极点位置。
- **P1：** 补充 \(\lambda_S\le4\pi\) 对应的 \(m_s^{\max}=\sqrt{8\pi}v_s\)：Benchmark A 为 \(355.4\) GeV，B 为 \(1579.2\) GeV。明确 \(10\)--\(150\) GeV 是 Higgs 极点附近局部诊断窗口，不是整个微扰性区间的扫描。
- **近极点数值：** Plan-C-lite 脚本新增 \(125.20\)--\(125.30\) GeV、\(0.1\) MeV 步长的复数极点局部扫描。相同 1001 点算法已在 in-session Python 环境独立复现；A/B 的 1001 个点均收敛。更新后的仓库脚本尚未在干净容器中整文件重跑，验证记录明确区分了这两类证据。
- **P2-lite：** 已新增 CP-even radial-scalar 三类 bubble 图的解析表达式和可复现数值脚本；正式回复信现直接包含等质量与非等质量 \(\Delta\bar B_0\) 的闭式表达式、Feynman 参数表示及代表性函数值。\(m_s=100\) GeV 与 \(m_s=m_h\) 两点的零动量相减子集数值仍只作为内部诊断：\(m_s=100\) GeV 时子集模长为 A: \(24.7547\) GeV\(^2\)、B: \(0.641797\) GeV\(^2\)，分别为当前保留费米子 \(|\Pi_{hs}^{ret}|\) 的 57.77 和 6.656 倍。闭式结果与 8,000 区间 Simpson 积分对全部 12 个 benchmark/质量/拓扑组合的最大相对差为 \(9.97\times10^{-15}\)，2k/4k/8k/16k 收敛检查通过。该比值只说明不能单凭形式 loop counting 断言标量项相对有限费米子结果必然很小；此子集不是完整两圈 UV--EFT 匹配，不能直接加到 \(\Pi_{hs}^{ret}\) 或作为物理极点修正。Goldstone 顶角已解析列出，但其数值贡献需与 gauge/ghost、混合 VLL--scalar 图及 tadpole/VEV 反项一起处理；近简并区继续标为未评估。详见 2026-11-05/Portal_induced_scalar_loop_power_counting_P2_lite_2026-11-05.md。
- **低能 EFT 交叉核查：** 补充 \(q^2\ll m_s^2,m_{A'}^2\) 下的 scalar four-lepton operator 与 \(A'\)-exchange 系数尺度比较：\(|C_{\mu\mu}^{(s)}/C^{(A')}|\sim4m_\mu^2/m_s^2\leq4.5\times10^{-4}\)（\(m_s\geq10\) GeV），而 \(\tau\tau\) 在 \(m_s=10\) GeV 时仍可达约 \(0.13\)。该比较仅是不同 Lorentz 结构的系数量级，不是过程级率比；不据此忽略 tau-sensitive scalar processes。
- **范围：** Major 1.3 继续只讨论原始单标量 \(S+\mathrm{VLL}\) 两态系统，不混入 \(\sigma,N_R,\mathrm{PMNS}\) 或三态标量势；近简并区不赋予 allowed/excluded 状态。

**验证边界：** 没有运行 CI；没有对更新后的 Plan-C-lite 脚本做干净容器整文件执行；回复信 PDF 尚未按 PR #49 的 TeX 重编译或视觉检查。main 根目录现有 48 页 PDF 仍是 PR #49 修改前的旧版，不包含 PR #49 的 TeX 修改。PR #49 已于 2026-11-05 合并。

## 2026-11-05 更新：回复信解析论证一致性修订（PR #50，已合并）

[PR #50](https://github.com/lm846802297-bit/axial-vector-review-response/pull/50) 已 Squash Merge，合并提交为 [51a245b0a36703f40c24ca469d6969e70abc8954](https://github.com/lm846802297-bit/axial-vector-review-response/commit/51a245b0a36703f40c24ca469d6969e70abc8954)；分支为 review/response-analytic-consistency-20261105。正式回复信的本轮修改限于以下内容：

- **Minor Point 6.1：** 将 \(g_X\) 上限从旧值 \(10^{-1}\) 修正为实际 Fig. 2 展示窗口的 \(1\)，与 Major Point 2 和 Minor Point 1 一致。
- **Major Point 4.4：** 引入 Kahn et al. (2017) 的轴矢量恒星冷却讨论；用 \(O(10^{-10})\) 表示 Wang--Zhang 矢量参考的 SN1987A 灵敏度；明确 neutrino coalescence 与不可见宽度使用原论文 active-flavor \(L_\mu-L_\tau\) 规范流；不引入额外中微子态、active--heavy mixing 或 Major Point 3 的可选完成机制。
- **Major Point 4.4：** 新增矢量流守恒、轴矢量流散度及 Goldstone 等效纵向耦合关系，解释矢量 semi-Compton 产生率不能直接移植；将低动量 kinetic-mixing 抑制限定为电磁流介导过程，不用于 neutrino coalescence 或直接轴矢量 semi-Compton。
- **Major Point 1.3：** 本轮复核后撤销最初拟议的三处文字精简，恢复 PR #50 修改前 `main` 的原有表述；PR #50 最终不修改该部分，完整保留闭式泡图表达式、UV--EFT 匹配、benchmark 数值、数值验证精度及各子集的适用范围和未完成项。
- 新增 [解析论证完整性审查与修订记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-05/回复信解析论证完整性审查与修订记录_2026-11-05.md)。

**验证边界：** TeX 花括号、环境配对、标签唯一性和 citation-key 静态核查通过；36 个唯一引用键均可解析。新增公式片段通过独立 pdflatex 编译。完整回复信 PDF 尚未重编译或逐页视觉检查；未运行 CI；没有新增超新星输运计算；论文正文未修改。根目录现有 PDF 仍是 2026-11-04-r2 历史编译件，不包含 PR #49/#50 的 TeX 更新。

## 2026-11-04 更新：Major 4.4 轴矢量 stellar-cooling 文献调查（PR #46）

PR #46 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 [b453e9be09a4f67d00cb90dfb85435c07472c5b4](https://github.com/lm846802297-bit/axial-vector-review-response/commit/b453e9be09a4f67d00cb90dfb85435c07472c5b4)。新增文档 [Major 4.4 轴矢量 stellar-cooling 文献适用性调查](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.4-轴矢量stellar-cooling文献适用性调查_2026-11-04.md)，并更新 README 导航与 DEC-09。

调查确认：Kahn et al. 2017 已明确讨论轴矢量 \(U(1)\) 的 stellar cooling，但没有本文模型的 SN1987A 数值曲线；EPS-HEP 2019 有轴矢量核子耦合 SN 报告；Bell et al. 2024 对轴矢量核子流使用的是 vector SN proxy。对本文最直接的定量映射是与常规 \(L_\mu-L_\tau\) 完全相同的中微子 coalescence 与不可见中微子宽度。常规矢量 \(L_\mu-L_\tau\) 的完整 SN 曲线不能直接移植，因为轴矢量缪子 semi-Compton、纵向模式、\(\mu^+\mu^-\) 阈值宽度和 LESN 能量沉积不同。

- 保留“stellar cooling 对 sub-GeV 区域相关”的判断，不把矢量模型曲线作为本文轴矢量模型的完整排除。
- 文档区分直接轴矢量文献、矢量 \(L_\mu-L_\tau\) SN 参考、相同的中微子子过程，以及尚需模型特定计算的部分。
- 不修改回复信 TeX 正文或论文源码；本次仅修复回复信的 BibTeX 构建依赖并补全三条文献元数据，不声称完成新的 SN luminosity、opacity、trapping、LESN 或 WD emissivity 计算。
- 未运行 LaTeX 编译、PDF 视觉检查或 CI；这些状态不作通过声明。
 
### 回复信参考文献与 BibTeX 问号核查（2026-11-04）

作者指出回复信 PDF 中多处引用显示为 `[?]`。对当前根目录权威 TeX 与两份 BibTeX 数据库进行了静态核查：

- 找到 **45 条引用命令、72 次 citation-key 出现、34 个唯一 citation keys**；34 个键全部存在于两份 `.bib` 数据库中。
- 未发现重复 citation keys；两份 BibTeX 文件的花括号静态平衡检查通过；TeX 源码没有 `[?]` 或 `??` 字面占位符。
- 因此，当前源码证据不支持“34 个引用键缺失”的判断。更可能的问题是 BibTeX 生成/读取环节，而不是正文的 `\cite` 键没有对应条目。
- 定位到关键构建隐患：回复信位于仓库根目录，使用 `\bibliographystyle{JHEP}`；原 `JHEP.bst` 仅位于 `overleaf-source/axial-vector-model-building-v6/`。本地 BibTeX 路径测试表明，默认样式搜索不会递归发现任意项目子目录中的 `.bst`。现已将原文件逐字节复制到仓库根目录；其 Git blob SHA-1 与原文件相同：`d39cbe846e531ed7be07eebb11be0bd72d675579`。
- 补全三条被引用文献的元数据：`NA64:2023lightDM` 加入 PRL 131 (2023) 161801 与 DOI；`geiregat1990first` 加入 DOI；`He:2024twoSingletHNL` 加入 arXiv:2401.14687。2026 年的 `Fiorillo:2026wso` 与 `Wang:2026supernova` 仍为预印本，未虚构期刊或 DOI。
- 最新可恢复包为 [2026-11-04-r2 manifest](archive/reply-letter/snapshots/2026-11-04-r2/manifest.md)，包括回复信 TeX、两份 BibTeX 数据库和 `JHEP.bst`。
- **回复信 PDF 已按要求完成重编译与视觉检查（2026-11-04）。** 以源码基线 `edce6a37a162e9fe97b5162bd2107656f50865db` 执行 `pdflatex → bibtex → pdflatex → pdflatex`；BibTeX 成功读取两份数据库及根目录 `JHEP.bst`，生成 34 条文献。最终 PDF 共 48 页，未发现未解析引用/交叉引用或 `[?]`/`??` 标记，所有字体均已嵌入。检查了全篇缩略图及表格、公式、参考文献页；未见裁切、重叠或不可读内容。编译日志保留一条 `Overfull \hbox (44.0084pt too wide)`，对应源码第 757–774 行的 NA64 六列表格（PDF 第 29 页）；该表在视觉检查中仍完整可读。正式 PDF 已提交到仓库根目录。此项没有运行 CI.

 
### 同步补充：正式回复信不可变源码备份

PR #46 同时加入正式回复信归档结构 `archive/reply-letter/`。根目录 TeX 仍是唯一可编辑权威版本；归档目录中的 `.snapshot` 文件只用于恢复，不作为第二份工作稿。

- 源版本固定为 main commit `d9b262798f80c0f109f328b1b0019191e99d5437`。
- 已保存回复信 TeX、两份 BibTeX 输入文件及根目录 `JHEP.bst`；最新 r2 快照的四份归档文件均记录 Git blob SHA-1。
- 归档说明和 manifest 记录原始路径、blob SHA-1、恢复步骤及 GitHub 按 commit SHA 下载完整仓库快照的链接。
- TeX 静态扫描未发现 `\input`、`\include` 或 `\includegraphics` 依赖；`JHEP.bst` 已作为仓库根目录构建依赖保存，LaTeX packages 仍属于编译环境依赖。正式 PDF 已在后续提交 `a9edb509dc47932b872465b5d0dd1263bd1c26da` 中编译并上传；编译来源与 PDF SHA-1 见 [2026-11-04-r2 manifest](archive/reply-letter/snapshots/2026-11-04-r2/manifest.md)。
- Git tag `reply-letter-2026-11-04` 尚未创建。Tag 是 Git ref，不能作为文件纳入 PR diff；建议 PR 合并后将该 annotated tag 指向上述固定源 commit，而不是后续 main HEAD。



## 2026-11-04 更新：Major 4.3 有限矢量耦合与小混合参数域（PR #45）

PR #45 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 `bc2a1c20e277d51ef2d6add68c84b1c5af1c533b`（[GitHub commit](https://github.com/lm846802297-bit/axial-vector-review-response/commit/bc2a1c20e277d51ef2d6add68c84b1c5af1c533b)）。修改前重新阅读了 `AGENTS.md`、`README-先读这里.md`、强制写作规范、main 正式回复信、正文同步清单、DEC-08 和 2026-10-23 第三段会议文字稿。

正式回复 Major 4.3 明确将本文轴矢量现象学限定在有限 VLL 质量下的 `|theta_lL|, |theta_lR| <= 1e-2` 小混合域，并用 `m_l ≃ theta_lL theta_lR M_E` 说明该域对应有限的多 TeV VLL 质量。新增 vector-specific 与 axial 限制映射条件：
`tan^2(theta_lR) < gV_lim(mA')/gA_lim(mA')`，
并说明在角度上限处，矢量专属耦合限制必须比同质量、同假设下的轴矢量限制严格约四个数量级，才可能产生更强的共同 `g_X` 限制。回复保留 trident 与 `(g-2)_mu` 过程贡献比，明确它们不是独立实验排除限；增加 BaBar/Belle II/CMS 四缪子 FSR 在远离阈值区的 vector/axial 同阶 reach 对照；新增 dimuon 阈值的宽度比及质量依赖角度条件，避免将小混合结论推广到阈值敏感衰变或所有实验。

- 修改正式回复信 Major 4.3；新增内部专项推导记录；同步论文正文待修改清单、DEC-08 和本状态文件。
- 不修改论文源码，不新增矢量排除图，不进行全 UV 扫描或 collider recast。
- 静态核验覆盖 TeX 花括号、环境配对、方程标签、公式与现有 benchmark 的一致性；具体结果见 PR 描述。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些验证通过。

## 2026-11-04 更新：Major 3 / 4.1 中微子记号与 S-only 条件性表述（PR #44）

PR #44 已于 2026-11-04 Squash Merge 至 `main`，合并提交为 `e78ae8a4b26a9b595e64ad0eaf52e7e836e50751`。正式回复信统一以 `y^nu_alpha` 表示中微子 Dirac Yukawa 耦合，并保留 `y_e, y_mumu, y_mutau, ...` 作为带电轻子 Yukawa 参数。Major 3 的 `m_D` 定义和 Major 4.1 的重复定义均已同步。

Major 4.1 将 S-only 纹理明确限定为：只有原电荷二标量 S 提供残余 Z2 破缺、没有其他破缺来源时，允许的中微子质量纹理保持 `e ⊕ (mu,tau)` 分块。文字同时明确该纹理是条件性对称性结论，不是原始带电轻子构造已经给出的中微子质量预测。Major 3 的 EFT 段落也统一为相同条件表述。

- 修改文件：正式回复信 TeX、Major 3 专项修改对照、论文正文待同步修改清单。
- 保留原 charged-lepton Yukawa 记号，避免将 `y_e` 等重新解释为中微子 Yukawa。
- 静态检查：中微子 Dirac 项和两处 `m_D` 均使用 `y^nu_alpha`；S-only 条件措辞一致；方程标签唯一；TeX 花括号及环境配对通过。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些检查通过；论文正文未修改。

## 2026-11-04 更新：Major 4.1 PMNS 论证强化（PR #43）

[PR #43](https://github.com/lm846802297-bit/axial-vector-review-response/pull/43) 已于 2026-11-04 通过 Squash Merge 合并至 main，合并提交为 9889beff08d827ede166f196f47fbb94db4a26f8。该修订严格按《审稿回复写作原则》处理 Major 4.1：先精确说明 S-only 残余 Z2 所给出的 U_PMNS = diag(1, U_23) 结构（允许非平凡 μ–τ 旋转，但缺少电子味混合，因此“严格单位矩阵”并不准确）；再给出保留 S、增加电荷一 σ 与三个 N_R 的可重整化完成机制；随后用 seesaw、含 U_L 的 PMNS 关系和 M_R = −m_D^T M_ν^−1 m_D 逆构造展示一般三味混合的构造性实现；最后核对新增单态中微子的异常抵消及双 VEV 的 A′ 质量关系。

- 正式回复只增加面向审稿人的物理论证；没有把分支、PR、内部任务或正文同步状态写入回复信。
- 内部[论文正文待同步修改清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)已同步记录 Major 4.1 的论证结构；论文源码、references 和 PDF 未修改。
- 已做静态检查：TeX 花括号平衡、begin/end 环境配对、无重复 equation label，Major 3 的方程引用和文献键存在。
- **未进行完整 LaTeX 编译、PDF 视觉检查或 CI。** 不宣称这些检查通过。

## 2026-11-04 更新：Major 4.2 动能混合与 NA64 质量依赖比较

Major 4.2 已补充有限轻子混合产生的非零动能混合、四态矢量耦合/真空极化、物理重态简并与共同裸质量下的残余阈值，并明确重 VLL 匹配尺度边界条件 \(\epsilon_{\rm ind}(\mu_{\rm match})=0\)。该条件只约束独立局域项，不令完整动量依赖物理混合函数为零。

[PR #42](https://github.com/lm846802297-bit/axial-vector-review-response/pull/42) 已于 2026-11-04 通过 Squash Merge 合并至 `main`，合并提交为 `de036d3cbb0fbf654055f5a0d14c67e81bc3061c`。回复 TeX 已扩展 NA64 Fig. 3 的 10、100、200、300 MeV 四点视觉读取区间；300 MeV 计入 dimuon 宽度并使用 `epsilon_eff = |epsilon_gammaA'| sqrt(Br_inv)`。读图区间约有 0.2--0.3 dex 不确定度，明确不是官方机器可读数据或 detector-level recast。按作者决定，本轮未重新编译完整回复 PDF；仓库中的 45 页 PDF 仍是本轮 TeX 更新前的历史快照，不应作为最新回复信使用。CI 状态检查为空。

- [Major 4.2 论证与论文修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-暗光子限制与论文修改对照_2026-11-04.md) 包含 K-01–K-05 正文同步建议、原始文献位置、四点 NA64 对照和适用条件。
- [计算入口](计算脚本/Major42_kinetic/check_kinetic_dark_photon.py) 与 [JSON](计算脚本/Major42_kinetic/outputs/kinetic_dark_photon_2026-11-04.json) 保存四点积分、Br_inv、epsilon_eff、NA64 视觉区间及比值。独立 mpmath 计算在 35/55 位精度下复核；仓库脚本尚未在仓库运行环境直接执行。
- [Major 4.2 验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major4.2-验证记录_2026-11-04.md) 记录当前源文件哈希和验证边界。
- **PDF 状态：** 当前 45 页回复 PDF 是本轮扩展前的编译快照，尚未根据最新 TeX 重新编译，不能作为本轮最终 PDF；需要重新编译并逐页检查。
- 原论文源码、bibliography 和 Fig. 2 未改；正文待按清单同步。Major 2/3 的核验哈希作为各自历史快照保留。

## 2026-11-04 已合并：Major 2 参数窗口

本轮基于 PR #40 合并提交 `f3d54dc9ec3c89bb6b8cbd22ecab6a92c4c83c3e`，按作者最新说明修改 Major 2：低质量端 g−2 已在图示实验室约束中主导，其渐近直线可继续延伸，扩图主要重复该区间；高质量端所用现有实验灵敏度减弱。天体物理适用条件与 UV 微扰性解释保留。

[PR #41](https://github.com/lm846802297-bit/axial-vector-review-response/pull/41) 已合并，合并提交 `49edfcee028717de3a315d76b6aad3e10a268e83`。正式回复和 PDF 已完成本轮核验：42 页，34 个引用键可解析，27 段审稿人引文及 Major 3 原文保持不变。

- 核对实际 Fig. 2 后，将回复 Major 2、Minor 1 和 DEC-06 的耦合上限从误写的 0.1 改为图中的 **1**；原图未改。
- [Major 2 修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-Fig2参数范围与论文修改对照_2026-11-04.md) 记录作者思路、推导、文献与 R-01–R-06 正文修改建议；[验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major2-验证记录_2026-11-04.md) 记录实际检查结果。
- 原论文源码和图文件不在本次修改范围；正文需按清单后续同步。两个作者本地原始 PDF 继续保留，不上传。
- 当前回复 PDF 随本轮更新；Major 3 验证记录的哈希保留为 PR #40 历史快照，避免与同名新 PDF 混淆。

## 2026-11-04 已合并：Major 3 中微子完成机制

作者已明确要求采用本轮文献调查结果修改回复并提交 PR。[PR #40](https://github.com/lm846802297-bit/axial-vector-review-response/pull/40) 已按作者要求合并，合并提交 `f3d54dc9ec3c89bb6b8cbd22ecab6a92c4c83c3e`。该工作原基于 GitHub main `613bca12`；GitHub 是同步到本地的基准，不将旧本地工作稿回推覆盖主线。以下为 PR #40 的成果与验证快照。

- 正式回复 Major 3/4.1 专门讨论双单态 type-I seesaw、详细算符/质量矩阵/PMNS/异常论证；该扩展仅属于中微子回复，不改变原论文场内容。Major 1、2、4.2–4.4 及其他非中微子回答继续使用原论文单 VEV (S+\mathrm{VLL}) 模型。
- 新增回复专用文献文件 `Replies_to_Referee_3_neutrino_references.bib`；归档论文 `main-v6.tex` 和 `references.bib` 未改。
- **原论文需要修改。** [N-01–N-14 修改对照](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-中微子完成机制与论文修改对照_2026-11-04.md) 列明位置、前后差异及条件；状态为待正文修改。
- 研究决策 DEC-01/02 已按作者新指示更新并保留旧立场；最小 S-only 的分块定理继续成立。
- 作者指定的两份 `审稿意见-gpt/专题研究/2026-11-04-*` 调查/候选稿一并归档；正式回复仍以根目录 TeX 为准。
- 本地两个原始 PDF 按作者要求保留，不纳入本次提交；其余仓库内容从 GitHub 主线更新并跟踪本次 PR 分支。
- 本轮 TeX 完整编译成功（41 页）；32 个引用键和 4 个标签均可解析，27 段审稿人引文与 main 一致。全文缩略图和新增关键页面已检查，详见 [Major 3 验证记录](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Major3-验证记录_2026-11-04.md)。该记录以源文件 SHA-256 标识核验对象。
- 回复信 PDF 已随 PR #40 一并提交，路径为 [2026-11-04 编译版](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-04/Replies_to_Referee_3_referee_facing_2026-11-04.pdf)，可与同目录的修改对照、验证记录直接比较。
- NuFIT 6.1 中心值上的 seesaw 构造脚本已复跑；完整输入/矩阵/耦合/残差 JSON 和运行入口见 [PMNS 重构结果](计算脚本/PMNS_Major3/outputs/pmns_tree_level_reconstruction_2026-11-04.json) 与 [PMNS 研究更新](审稿意见-gpt/当前执行/PMNS_Major3路线决策与扩展模型解析核查_2026-10-27.md)。该点是树级存在性示例，不是统计拟合或全参数约束结论。

以下为本轮前已合并工作的状态记录；若与本节的中微子路线冲突，以本节和最新决策登记表为准。

## 1. 项目当前阶段

当前项目处于**正式回复信主线已形成、Major/Minor 一致性审查已完成；PR #38、PR #39 均已合并；PR #39 已统一标量约束相关回复并归档 Table II 的详细论文修改方案；论文源码与 bibliography 尚未修改，待后续按清单同步**的阶段。

已完成：
- 完整回复信主线按会议决策整理并合并（PR #33）。
- 回复信最终一致性审查并合并（PR #34）。
- 正式回复信与内部论文修改清单的职责规范已合并（PR #35）。
- 本轮建立项目启动读取机制和可修改的研究决策登记表。

不能据此声称：
- 论文正文已完成所有同步修改；
- 当前 2026-11-03 回复信 TeX 已重新编译并完成 PDF 视觉验收；
- 标量的完整 collider recast 或全质量范围允许区间已经得到；
- 轴矢量模型完整 SN1987A/LESN 输运与排除曲线已经完成。

## 2. 每次启动的最小读取集合

每次开始项目任务，先读：
1. [AGENTS.md](AGENTS.md)：强制规则和任务路由。
2. 本文件：当前项目状态。
3. [README-先读这里.md](README-先读这里.md)：仓库导航。

随后按任务追加读取，不要无差别加载全部历史文件：

| 任务 | 追加读取 |
|---|---|
| 回复信撰写/审查 | [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md)、[当前回复信](Replies_to_Referee_3_referee_facing_2026-11-03.tex)、[正文待同步清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md)，以及对应审稿原文/会议证据 |
| 论文正文修改 | 正文清单、作者选定的活动源文件及依赖、v6 只读基线、相关物理证据 |
| 物理推导/数值研究 | [研究决策动态登记表](审稿意见-gpt/项目规范/研究决策与不可回退事项.md)、v5.7 相关章节、原始模型公式、专题计算账本和原始文献 |
| GitHub/文档维护 | AGENTS、目标目录 README、实际 PR/分支状态和相关验证说明 |

不要每次完整读取 v5.7、所有会议文字稿或全部计算日志；先定位专题，再按需读取证据。

## 3. 当前权威文件

| 文件 | 用途 | 状态 |
|---|---|---|
| [正式回复信 TeX（当前 main 版本）](Replies_to_Referee_3_referee_facing_2026-11-04.tex) | 当前唯一权威回复信 | PR #38 已合并；包含标量偏宽度、可见分支比、Belle 数值阈值条件及 Belle II spin-0 文献修正 |
| [正文待同步清单](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-03/论文正文待同步修改清单_2026-11-03.md) | 内部正文修改追踪 | Table II 专项修改清单已在 PR #39 分支整理；论文正文尚未修改，其他项目仍待核对 |
| [审稿回复写作原则](审稿意见-gpt/写作规范/审稿回复写作原则.md) | 回复信与内部清单的长期规范 | 已合并 |
| [研究决策与不可回退事项](审稿意见-gpt/项目规范/研究决策与不可回退事项.md) | 当前研究立场及变更历史 | 动态文档，允许作者随最新观点修改 |
| [原始论文 v6 PDF](axial_vector_model_building-v6.pdf) | 归档论文事实基线 | 根目录只读归档 |
| [Overleaf v6 源码归档](overleaf-source/axial-vector-model-building-v6/) | v6 源码、文献和图表 | 不能自动假定等于作者当前 Overleaf 工作版本 |
| [原始审稿报告](dw13678_report_1_a.pdf) | 审稿原文 | 核对原文措辞优先使用 PDF |
| [2026-10-23 会议观点总结](审稿意见-gpt/会议记录/2026-10-23/会议观点总结_2026-10-23.md) | 会议决策历史 | 不替代物理核验或作者最新指示 |
| [v5.6 执行手册](审稿意见-gpt/当前执行/审稿意见分析与执行手册_v5.6-主分析全任务映射与原子步骤版-20261019.md) | 任务 ID、依赖、步骤和验收框架 | §0.1 是 2026-10-27 状态快照，不再是最新状态源 |
| [v5.7 技术参考](审稿意见-gpt/审稿意见分析v5.7-物理校核与专题连续阅读版.md) | 物理推导和专题技术参考 | 2026-10-20 版本，按需读取 |

## 4. GitHub 工作状态（本次核验）

### 正式回复信修订（已合并）
- [PR #38：Add scalar partial widths and correct Belle II scalar interpretations](https://github.com/lm846802297-bit/axial-vector-review-response/pull/38)：已于 2026-11-04 合并，Squash commit 为 [f1dec3b9a0142a13444749ea1dfda432287e8b81](https://github.com/lm846802297-bit/axial-vector-review-response/commit/f1dec3b9a0142a13444749ea1dfda432287e8b81)。当前正式回复信为根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex`。
- 已补入 s→A′A′、s→ℓ⁺ℓ⁻ 的偏宽度和可见分支比论证，限定 Belle 1 GeV 数值映射的 m_A′ > 0.5 GeV 条件，并纠正 Belle-II:2023ydz 与 Belle-II:2024wtd 的 scalar-specific interpretation 分类。
- 内部正文待同步清单和 2026-11-04 Belle II 文献核查记录已同步更新；论文源码没有修改。

### Table II 回复信修订与论文修改方案（PR #39 已合并）
- [PR #39：Revise referee response and add Table II manuscript revision plan](https://github.com/lm846802297-bit/axial-vector-review-response/pull/39)（已合并，squash commit `76268abf`）：统一 Major Point 1、Minor Point 6.2 和 Summary 的标量约束数值、文献来源及物理适用条件；保留详细的未来论文修改清单。回复信不包含标量约束图；是否在论文中加入配套图留待后续决定。
- PR #39 仅修改正式回复信和内部清单/核查文档；未修改 main-v6.tex 或 references.bib。论文 Table II、正文解释和 Fiorillo v2 的 BibTeX 更新留待后续正文修订。回复信 TeX 尚未编译，PDF 视觉验收尚未完成。

### 已合并
- [PR #33](https://github.com/lm846802297-bit/axial-vector-review-response/pull/33)：按会议决策整理完整回复信。
- [PR #34](https://github.com/lm846802297-bit/axial-vector-review-response/pull/34)：Major/Minor 最终一致性审查；统一 Major 3/4.1 的 PMNS 结论及 Major 1/Minor 5 的 portal 假设。
- [PR #35](https://github.com/lm846802297-bit/axial-vector-review-response/pull/35)：回复信写作规范和项目级读取规则。
- [PR #36](https://github.com/lm846802297-bit/axial-vector-review-response/pull/36)：项目启动读取机制、PROJECT_STATUS 和可修改的研究决策登记表。

### PR 状态汇总
| PR | 状态 | 当前已知边界 |
|---|---|---|
| [#53 原论文单 VEV 轴矢量恒星冷却/半康普顿计算](https://github.com/lm846802297-bit/axial-vector-review-response/pull/53) | Open / Draft；2026-11-05 新建 | 原论文单 VEV 映射与局部振幅/热率已验收；完整介质 T/L opacity 和 SN 输运仍未完成 |
| [#56 Major 4.4 轴矢量 EFT ballistic-cooling benchmark](https://github.com/lm846802297-bit/axial-vector-review-response/pull/56) | Merged 2026-11-12（author-directed integration） | 固定剖面 EFT benchmark 已进入 main；合并不代表矢量 Fig. 7 复现或轴矢量 SN1987A transport/exclusion 通过。10 MeV 强吸收端差异仍未解决；不允许 opacity/profile rescaling |
| [#52 原论文单 VEV 标量 Belle II 后续研究](https://github.com/lm846802297-bit/axial-vector-review-response/pull/52) | Closed / 未合并；保留研究分支 | 保留来源台账、重铸协议和部分宽度框架；Belle II 补充数据提取、benchmark 复现和 UV 重铸尚未完成 |
| [#54 Major 3/4.1 回复范围隔离与原论文模型一致性](https://github.com/lm846802297-bit/axial-vector-review-response/pull/54) | 已合并；2026-11-05 | Major 3/4.1 扩展仅限中微子回复论证；跨问题引用已隔离 |
| [#55 Minor Points 论证扩充与长期写作规范](https://github.com/lm846802297-bit/axial-vector-review-response/pull/55) | 已合并；2026-11-06 | 正式回复信、Minor Points 和写作规范已进入 main |

PR #53 与 PR #56 是两个不同工作流：#53 针对原论文单 VEV UV 模型的进一步恒星冷却研究；#56 是支撑 Major 4.4 的固定剖面 EFT benchmark。#56 不替代 #53，也不代表完整 UV 恒星冷却问题已经解决。#52 已关闭；#54/#55 已合并。

## 5. 正式回复信与论文正文的状态边界

### 正式回复信
- 当前 main 权威回复信为根目录 `Replies_to_Referee_3_referee_facing_2026-11-04.tex`；PR #38 已合并，保留 PR #33/#34 的既有回复主线。
- 本次合并补入 Eq. (33) 的 s→A′A′ 与 s→ℓ⁺ℓ⁻ 偏宽度、visible-branching-ratio 论证；限定 Belle 1 GeV 数值映射只在 m_A′ > 0.5 GeV 时直接适用；并纠正 Belle II 两篇 scalar-specific 搜索的描述。
- 本轮 Major 3 修订版已完整编译并作全文缩略图及关键页面检查，见顶部更新及验证记录；此前未编译状态已由本次验证替代。
- PR #31 生成的 PDF 位于 2026-10-28 历史目录，文件名为 Replies_to_Referee_3_referee_facing_2026-10-28.pdf；它不是当前 2026-11-03 回复信的最终编译件。
- 当前编译件位于本地被忽略的 work/neutrino/latex-build/；未将历史 PDF 当作本轮验证证据。最终对外提交前仍须与已修订论文作整套一致性验收。

### 论文正文
- 仓库保存原始 v6 PDF 和 Overleaf v6 源码归档。
- 2026-11-03 内部清单记录 Introduction、Eq. (27)、Table II、PMNS/Weinberg 算符、Higgs portal、kinetic mixing、有限 vector component、Muon Collider 和 Conclusion 等同步事项。
- 清单中的“待修改”“待决定/修改”“待核对”状态仍应按实际源文件复核。
- **待确认：** 作者当前选定的 Overleaf 工作版本是否与 v6 归档相同。确认前不得将 v6 归档当作活动稿件覆盖式编辑。

## 6. 当前建议的工作顺序

1. 审阅本轮 Major 3 回复与 N-01–N-14 正文修改对照；本轮回复编译和关键页面检查已有验证记录。
2. PR #39 已合并。下一步另行确认作者当前使用的 Overleaf 正文基线，再按已归档清单实施论文修改；不得把未实施的正文修改写成已完成。
3. 优先核对影响主要物理主张的 PMNS、标量约束、portal/mixing 和参数范围；完成后更新清单中的实际正文位置和状态。
4. PR #52 已关闭且保留研究分支；PR #53 继续原论文单 VEV UV 恒星冷却研究；PR #56 作为 Major 4.4 的固定剖面 EFT response-support benchmark 保持 Draft。PR #56 不替代 PR #53，也不作为完整 UV 恒星冷却已完成的证据。未完成工作不得写成已得到的排除结论。
5. 关键 PR 合并、作者改变路线、正文基线更新或专题验收后，更新本文件和相关决策条目。

## 7. 状态可信度约定

- **已核验：** 本次直接检查 main 文件、PR 元数据或可追溯证据。
- **已有记录，需复核：** 历史文档/PR 描述有记录，但本轮未重新执行计算或测试。
- **待确认：** 缺少当前源文件、作者选择或必要证据。
- **未完成：** 当前证据明确表明工作尚未闭环。

本文件是项目管理状态快照，不是物理结果的独立证明。物理结论以模型定义、可复核推导、实际计算和原始实验文献为准。


## 2026-11-10 update: focused 10 MeV research plan

The next research stage is restricted to the high-order energy-resolved escape distribution at the 10 MeV strong-absorption endpoint. The staged plan is [RESEARCH_PLAN_10MEV_HIGH_ORDER_PHASE_SPACE_2026-11-10.md](research/stellar-cooling-constraints-20261105/blinov_reproduction/RESEARCH_PLAN_10MEV_HIGH_ORDER_PHASE_SPACE_2026-11-10.md). It defines the calculation contract, exact baseline/closure gates, the required source-versus-escaped energy/radius/direction distributions, and conditional follow-up diagnostics. No 0.1 or 1 MeV scan or axial-vector curve update is authorized by this stage.

The plan review identified one output-integrity gap before execution: the phase-space script previously archived only the top 80 joint radius-energy-direction cells, which would not allow an independent reconstruction of all one-dimensional marginals. The script now archives the complete non-empty joint table as `joint_radius_energy_direction_bins`, while retaining the top-80 convenience view. The workflow and local runbook now require closure of the complete joint source and escaped-luminosity partitions, including their global subregion fractions.

Stage A has confirmed the research branch, PR #57 status, archived profile/Fig. 7 fingerprints, and high-order baseline configuration (200/640/200/32/64; 842 energy nodes after lapse-threshold insertion). The exact baseline strong-end point is \(g=4.171689650228597\times10^{-8}\), \(L_{\rm B.16}=2.4396359573610326\times10^{52}\,\mathrm{erg\,s^{-1}}\), and \(P_{\rm esc}=3.251774019352899\times10^{-4}\). The regression suite contains three tests, but it has **not** been executed in this environment; the long physical calculation has not started. Proceed to Stage A runtime tests and then the single high-order run, without changing the calculation contract.


## 2026-11-10 update: complete joint-table validation and latest execution status

The high-order phase-space script now archives the full non-empty radius-energy-direction joint table. The workflow additionally checks escape-probability closure against the archived baseline and independently reconstructs all radius, energy, and four-bin direction marginals from the full joint table. This prevents the top-80 display subset from being mistaken for a complete partition.

The latest push-triggered workflow, [Run #42666123613](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42666123613), again failed before runner allocation: job exists, but `steps=null` and `logs_url=null`. Thus neither regression tests nor the high-order physical calculation executed. Do not interpret this as a numerical failure and do not trigger more empty runs. The next valid execution route is a local checkout of this exact branch or GitHub Actions after hosted-runner provisioning is restored.


## 2026-11-11 update: SFHo real-table and Fig. 12 cross-check

P1-IIIe-A/B now has an authenticated local raw-data run and a full local test
execution. The current combined suite passes **35/35** locally and in GitHub Actions. Run
[#42953524476](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42953524476)
downloaded the three original Release ZIPs, verified their SHA-256 values,
extracted the tables, and passed 15/15 plus 20/20 tests with zero skips.
The decoded physical SPP grid contains 1,496,880 cells; the excluded-volume
identity has maximum residual 7.975e-8. The composition table has 1,521,828
physical cells, of which 1,121,375 (73.6861%) are nuclei-containing. Its free
neutron/proton densities reproduce X_n n_B and X_p n_B to 4.44e-16 relative
precision. The composition layer-0 NSE neutron-side input is now documented as
conditional: it is zero and unused in the 400,453 no-nuclei cells and is not
interchangeable with the Extended EOS thermodynamic chemical potential.

P1-IIId Fig. 12 has been extracted from native APS/SCOAP3 PDF vector paths (page 15;
APS SHA-256 d660eb39..., SCOAP3 mirror SHA-256 c3b92fe6...). The E-K temperature profile agrees with the archived
Caputo profile at 55 radii with 0.071% RMS relative residual and with Bollig
Fig. 1 at 391 radii with 0.095% RMS. At ten common radii from 1 to 15 km, the
E-K n,p curves agree with Caputo reconstructed free-neutron/free-proton
profiles at 0.58% RMS each. The upper two density-axis glyphs are visually ambiguous vector outlines, not
extractable text spans; both mappings remain archived, and equal log spacing
plus the same-model comparison selects the corrected mapping without claiming
a definitive typesetting error. The sum n+p
tracks Caputo n_B(1-X_cluster), not total n_B.

This is a cross-publication check of the same Garching SFHo-18.8 model lineage,
not an independent hydrodynamic simulation validation. No raw Garching profile
has been obtained, and no B.2 opacity, pure-vector Fig. 7 result, or axial
cooling curve is changed. Fiorillo Table 1 weighted F_NN averages remain open
because their original space-time weights are not contained in the EOS tables.
The reproducible Fig. 12 vector workflow completed successfully in Run
[#42952924997](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42952924997),
using the checksum-pinned SCOAP3 copy because APS direct download returns HTTP
403 to hosted runners. The reproducible extraction and cross-check scripts and their workflow are in
`research/stellar-cooling-constraints-20261105/blinov_reproduction/`.


**P1-IIId source-version clarification (2026-11-11):** The reproducible
native-vector extraction is tied to the checksum-verified SCOAP3 copy of the
published APS PDF (SHA-256 `c3b92fe6cf2a8bd3fec84925e2baababfe0c707327a68135013f953ed3d87d43`,
2,749,668 bytes), validated in GitHub Actions Run
[#42953625693](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42953625693).
The arXiv v3 PDF is not used for path indexing: although its text/version
matches the published paper, its internal vector-object ordering differs, so
published-PDF path indices 25/181/182 do not identify the corresponding curves
in that file. Numerical cross-checks below remain based on the SCOAP3 source.


**P1-IIId completion / P1-IIIe handoff (2026-11-11):** The final Fig. 12
native-vector extraction, PDF-axis glyph audit, and Caputo/Bollig pointwise
cross-check passed in GitHub Actions
[#42955259591](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/42955259591).
The E–K temperature profile has 0.0707% RMS residual against Caputo Fig. 1
(55 common radii) and 0.0953% against Bollig Fig. 1 (391 radii). At ten radii
from 1 to 15 km, E–K free-neutron and free-proton densities agree with Caputo
reconstructions at 0.580% and 0.586% RMS; their sum agrees with
\((1-X_{\rm cluster})n_B\) at 0.574% RMS. Caputo's own Fig. 1/Fig. 4 closure
supports the free-proton reconstruction. The cluster fraction is
\(X_{\rm cluster}=1-Y_n-Y_p\), rising to 8.85% at 15 km. This is a
cross-publication consistency check of the same Garching SFHo-18.8 lineage,
not independent hydrodynamic validation. Next: map the validated
\(T,n_n^{\rm free},n_p^{\rm free}\) profiles onto the authenticated SFHo EOS
tables and calculate local nucleon chemical potentials/occupation factors,
keeping cluster-bound baryons separate. No B.2 opacity, vector Fig. 7 result,
or axial cooling curve is changed.



## 2026-11-11: P1-IIIe-C local Caputo-to-SFHo EOS key-radius mapping

A first local mapping is complete at ten audited Caputo SFHo-18.8 radii from
1 to 15 km, using the official SFHo/FRDM v1.03 EOS files whose extracted
SHA-256 hashes are recorded in the new P1-IIIe-C JSON. The EOS interpolation
coordinate is the total proton fraction \(Y_p^{\rm tot}=Y_e+Y_\mu\), not the
free-proton abundance \(Y_p\). The wrong-coordinate test fails at the
few-percent composition level, while the correct coordinate reproduces
Caputo \(X_n,X_p,X_{\rm cluster}\) at maximum absolute differences
\(2.02\times10^{-5}\), \(1.67\times10^{-5}\), and \(2.67\times10^{-5}\).

The SPP filling factor agrees with the value inferred from Caputo densities
to \(1.74\times10^{-4}\) maximum absolute difference. Direct Fermi-integral
density closure is 0.177% maximum for neutrons and 0.603% for protons.
The chemical-potential correction needed for exact density closure is below
0.18 MeV; the resulting change in \(F_{NN}^{\rm deg}\) is below
\(3.7\times10^{-4}\). The 2048-point quadrature is converged against 512
points at better than \(2\times10^{-13}\) in density.

Local static factors span \(F_{nn}^{\rm deg}=0.242\)--0.731 and
\(F_{pp}^{\rm deg}=0.460\)--0.983. Relative to a vacuum-mass ideal gas at the
same local free-nucleon densities, the EOS effective masses lower these
factors by up to 31.6% (neutrons) and 26.6% (protons) in the inner core.
These are snapshot-local static factors, not Fiorillo Table 1 mass-time
weighted averages; no dynamic response, opacity, transport, or cooling curve
is changed.

The reproducible profile builder, mapping script, input CSV, detailed output,
and report are in
`research/stellar-cooling-constraints-20261105/blinov_reproduction/`:
`build_caputo_profile_key_radii.py`,
`map_caputo_sfho_eos_profile.py`,
`outputs/caputo_profile_key_radii_2026-11-11.csv`,
`outputs/caputo_sfho_eos_profile_key_radii_2026-11-11.csv`,
`outputs/caputo_sfho_eos_profile_key_radii_2026-11-11.json`, and
`B16_P1IIIE_C_CAPUTO_PROFILE_TO_SFHO_EOS_2026-11-11.md`.

The independent GitHub Actions profile-map validation is running. Next is to
extend the same mapping from ten key radii to the full 0.05-km Caputo
composition profile, retaining clusters as a separate component.



### 2026-11-09 追加：PR #64 独立审稿人视角复核

已对 PR #64 当前正式 TeX 与实际 diff 进行独立审稿人视角检查，并对照 referee 原文、AGENTS.md、《审稿回复写作原则》§3.1、§6、§7、正文待同步清单和模型决策登记表。

- **总体结论：** Major 1–4 与当前 Minor 小节均有可识别的直接回答；没有发现系统性过度肯定，也没有发现 Major 1–4 将可选 \(\sigma+3N_R\) 双 VEV 中微子完成机制误用于原论文非中微子问题。
- **当前主要风险：** 仍是防御性措辞和重复限定偏多，集中在 Major 1.3、Major 2、Major 4.3、Major 4.4、Minor 5、Minor 6.5；Major 1.1 与 Minor 6.3 另有重复的 scalar-search 映射内容。
- **必须保留的限定：** portal matching 与近简并诊断的不同证据边界、\(\epsilon_{\rm ind}=0\) 与物理动能混合的区别、trident/\((g-2)_\mu\)/dimuon threshold 的过程差异、neutrino-coalescence current-level equality 与完整 SN transport 的区别、各实验的 branching fraction/acceptance/promptness 条件。
- **实质性范围余项：** Major 1.3 数值扫描为 \(10\)–\(150\) GeV，低于 Benchmark A/B 的完整微扰上限 \(355.4/1579.2\) GeV；Major 4.4 没有完整 axial SN1987A transport/exclusion curve。两者均在回复信中按当前证据范围表述，不应通过修辞夸大为已完成。
- **下一步：** 先精简同一物理命题的重复否定句和总结句，再复核实际 diff；不新增物理计算、不改论文正文。

详细逐点结论、模型边界核查、实验适用条件和建议修改位置见 [PR #64 独立审稿人视角复核](审稿意见-gpt/当前执行/论文修改与一致性核查/2026-11-09/PR64独立审稿人视角复核_2026-11-09.md)。该复核形成时 PR #64 尚未合并；当前状态见顶部更新。

## 2026-11-12 后续 CI 失败分类与修复

- **Major 4.4 数值验证：** Run #43151547062（触发 head `960f407`）与较早 Run #43150499259（触发 head `e9a0223`）均已通过 C4C3 14 项 SHA-256 和 SFHo/FRDM 实际分块重组检查；最后检查时两者仍在第一组 research-level unittest 中，尚无最终测试汇总。Run #43149443570 已取消，不能作为完整数值验收。
- **C4C3 历史失败分类：** Run #43039883023 与 #43039533642 均在 `actions/checkout` 阶段因工作流将 `\${{ github.sha }}` 写成带反斜杠的字面值而报 `fatal: invalid refspec`；Python、单元测试和计算分片全部 skipped。该问题属于 workflow 配置错误，不是核散射计算或验收阈值失败。独立的 301 点 workflow Run #43039856965 已成功。
- **C4C3 workflow 修复：** 在 moving-muon 分支提交 `683aee8` 中移除误转义的 GitHub Actions 表达式，并统一 shard 输出文件名；新 Run [#43152133071](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43152133071) 已排队，等待重新执行 unit tests、20 个 shard 与 merge acceptance。
- **回复信 PDF 审计失败分类：** Run #43151746827 的 LaTeX、BibTeX、PDF 结构、交叉引用和字体检查均通过；仅 `audit_reply.py` 的 27 段原文比较失败，原因是 moving-muon 分支仍使用旧基线 `7ef9a4a`，而 TeX 已同步到 main 的 `310a24a`。不是排版或物理内容失败。
- **回复信审计修复：** moving-muon 分支提交 `4003781`，采用 PR #56 已验证的 `BASE=310a24a` 审计脚本；提交 `d1d79aa` 将 `audit_reply.py` 纳入 push/pull_request 触发路径。新 Run [#43152263886](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43152263886) 已排队，待完成 PDF 构建与 27 段保留审计。
- **物理验收边界：** 上述 checkout/refspec 与源文档基线问题均归类为 workflow/test-baseline 配置问题。它们不能作为物理计算错误证据；同样，前置 checksum gates 通过也不代表 Blinov Fig. 7 或轴矢量冷却曲线已经通过独立复现。

## 2026-11-12 15:30 CST — 最新数值验收与活跃分支同步复核

- **当前 main 基线：** `310a24a53e8448f0388072cfdbf55749fde713f9`。本次重新执行 GitHub compare（`main...head`），四个开放 Draft PR 及五个持续研究/数据分支均为 `behind_by=0`：
  - PR #53：`ahead=14, behind=0`；
  - PR #56：`ahead=758, behind=0`；
  - PR #68：`ahead=26, behind=0`；
  - PR #69：`ahead=412, behind=0`；
  - C4-C4：`ahead=659, behind=0`；
  - moving-muon：`ahead=1542, behind=0`；
  - P1-IIIe EOS：`ahead=1350, behind=0`；
  - PR57 source bundle：`ahead=1125, behind=0`；
  - SFHo/FRDM transfer：`ahead=1342, behind=0`。
  比较时 PR #53/#56/#68/#69 均为 Open / Draft。PR #56 最新分支 head 为 `b68897c8c0ac6ade36ebe70aa27124cb380265a5`。

- **Run #158 结论：** [Run #43135845410](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43135845410) 在旧 SHA `071d194` 上以 `cancelled` 结束；它不是测试断言失败，也不能作为最终数值验收。其后已启动具备 90 分钟 timeout、独立 concurrency group 且 `cancel-in-progress=false` 的新 workflow。

- **完整数值验收：** [Run #43164221257](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43164221257) 在 SHA `3f7ce66f210edf966d8bb3b7d20f7716b28135e8` 上 `success`。以下步骤全部成功：C4C3 14 项 SHA-256 manifest、SFHo/FRDM Release manifest 与分块重组、research-level rate/transport/kernel tests、Blinov/EOS regression tests、reference scans/independent rate audits、saved-scan validation、figure regeneration、reproducibility checks 及 figure publishing。该验收提交是当前 PR #56 head 的祖先，当前 head 比验收 SHA 多 6 个提交；这 6 个提交触及 VALIDATION_AND_REVIEW、Blinov/EOS 数值 JSON 与 finite-mixing 数值输出。因此 Run #43164221257 是强而完整的前序数值验收，但**不是当前 head 的逐字节同 SHA 验收**；不得把它写成当前 head 已完整复验。

- **校验和复核边界：** C4C3 的 14 项 SHA-256 与 SFHo/FRDM 的分块、重组及 Release manifest 校验已由 Run #43164221257 的真实步骤通过。C4C3 清单路径为 `blinov_reproduction/c4c3_direct_local_recomputation_2026-11-11/SHA256SUMS.txt`；SFHo/FRDM 清单路径为 `blinov_reproduction/data/sfho-frdm-v1.03/MANIFEST.sha256` 和顶层 `sfho_frdm_v1.03_manifest.sha256`。Manual 与 Shen98 的核对属于 Release digest 元数据比对，不冒称 runner 本地重新下载并计算字节哈希。

- **物理结论独立保留：** 即使上述数值 workflow 完整通过，也只说明其测试合同、归档校验和数值程序检查通过。纯矢量 Blinov Fig. 7 的 10 MeV 强耦合端仍有约 92.43% 差异，物理复现仍未通过；不得将其改写为已复现，不解冻生产轴矢量限制曲线。

- **下一步：** 对当前 head `b68897c` 重新运行完整 Major 4.4 数值验收，重点覆盖上述 6 个后续提交改动的输出 JSON、Blinov/EOS reference scans、saved-output checks 和 figure regeneration。完成前，Run #43164221257 继续标注为前序祖先提交的完整通过记录，而当前 head 标注为待同 SHA 复验。


## 2026-11-12 15:59 CST — PR #56 semi-Compton polarization source audit

- **PR #56 live state:** Open / Draft, target `main`, current head `532652c5c93e1ca890905976d6192a9984423f1f`; current main base `310a24a53e8448f0388072cfdbf55749fde713f9`. A fresh GitHub compare reports `ahead_by=763, behind_by=0`. The branch remains a research branch and was not merged.
- **HEAD reconciliation:** the earlier reported SHA `44720ab5d4efe81096b2151948d84c17dfb69b5e` is no longer the live PR head. The branch advanced through subsequent archived scans and the new source-audit documentation. Use the live PR metadata before any subsequent write or merge.
- **Four named Actions runs:** Moving-muon thermal response [#43164221127], vector-to-axial local response [#43164221273], finite-mixing UV coupling-map [#43164221246], and Major 4.4 EFT numerical validation [#43164221257] all report `completed/success`. All four ran on `3f7ce66f210edf966d8bb3b7d20f7716b28135e8`. The current head is 11 commits ahead of that tested SHA. These are successful historical runs, not same-HEAD CI acceptance; do not describe the current head as fully revalidated by those runs. No already-passed workflow was repeated in this documentation task.
- **New theory document:** [WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md](research/stellar-cooling-constraints-20261105/finite_mixing/WANG_ZHANG_SEMICOMPTON_POLARIZATION_AUDIT_2026-11-12.md) was added and indexed in `finite_mixing/README.md` and `VALIDATION_AND_REVIEW.md`.
- **Formula result:** the PDF labels are (5.9a,b), (B.1a,b), (B.2)–(B.6a,b), and (A.15). The printed (B.6) integrates to (5.9) after restoring the common phase-space factor beta, but each printed polarization component has a negative angular region. The conserved-vector-current soft limit instead has unsuppressed transverse production and longitudinal production suppressed by \(m_{Z'}^2/E_\gamma^2\). The integrated comparison is not fixed by a pure T/L label swap: the suppressed coefficient still differs by a factor \(3/2\), and the differential angular functions remain inconsistent.
- **Additional amplitude issue:** the printed (B.1b) u-channel gamma-matrix ordering appears inconsistent with the crossed Compton amplitude and its Ward identities. The generic-angle (B.2)/(B.4) trace comparison is consistent with the expected common factor 4 from initial-state averaging; the subtracted longitudinal trace requires a more stable direct projection.
- **Scope:** no production code, CI workflow, opacity normalization, manuscript, referee-response TeX/PDF, or published constraint figure was changed. No rescaling or replacement cross section was inserted into the transport benchmark. The pure-vector Blinov Fig. 7 gate remains **NOT PASSED**; no axial/finite-mixing luminosity or exclusion curve is released.
- **Next theory tasks:** derive (B.2)/(B.4) from the correctly ordered amplitude at exact finite mass; compute the longitudinal contribution directly with \(P_L^{\mu\nu}\); trace the phase-space Jacobian, beta factor, and initial-state averages into (B.6); identify the first step where the source formulas diverge. Do not introduce a fitted rescaling or modify the production transport benchmark before that audit is complete.


## 2026-11-12 — Direct vector longitudinal projector audit

- **PR #56 remains Open / Draft** on branch codex/major44-axial-cooling-constraints-20261105; no merge was performed. The branch is kept separate from the production transport benchmark.
- **New reproducible files:** research/stellar-cooling-constraints-20261105/finite_mixing/thermal_integrals/audit_vector_longitudinal_projector.py, test_vector_longitudinal_projector.py, and outputs/vector_longitudinal_direct_projector_summary_2026-11-12.json.
- **Direct P_L:** the rank-one longitudinal mode is evaluated at amplitude level using the exact Ward-equivalent polarization \(\widetilde\epsilon_L=\epsilon_L-q/m_{Z'}\), written in a cancellation-free form. This is valid for the conserved vector current only; it is not applied to the axial current.
- **36-point local acceptance:** physical/Ward polarization agreement \(3.27\times10^{-7}\); independent trace/explicit-spinor agreement \(8.37\times10^{-11}\); correct vector Ward residual \(1.34\times10^{-14}\); all direct longitudinal rates positive. Local regression assertions pass. The new commits use [skip ci]; no already-passed GitHub Actions workflow was rerun.
- **Printed B.1b:** the literal printed u-channel gamma order fails \(q_\mu\mathcal M^\mu=0\), while the crossed \(\gamma^\nu S_u\gamma^\mu\) order satisfies it. Treat this as a printed equation-ordering inconsistency, not proof of the authors' internal implementation.
- **B.3 diagnosis:** 80-digit evaluation does not remove the B.3/direct-\(P_L\) residual. At small \(x=m_{Z'}/E_\gamma\), the scan supports the numerical leading laws \((B_2/T_{\rm exact})-1\simeq 2x^2(E_\gamma/m_\mu)/(1+\cos^2\theta)\) and \((B_3/L_{\rm direct})-1\simeq-2(E_\gamma/m_\mu)/(1-\cos^2\theta)\). At \(x=10^{-3}\), \(E_\gamma\le0.1\) MeV, the maximum relative fit errors are 0.154% and 0.0921%. A symbolic finite-recoil derivation remains pending.
- **Physical interpretation:** the B.2 residual is \(O(x^2 E_\gamma/m_\mu)\), the same mass order as the physical longitudinal signal. Subtracting B.2 from B.4 amplifies this into an \(O(E_\gamma/m_\mu)\) relative bias in B.3. This is not solely floating-point cancellation.
- **Scope boundary:** no production kernel, opacity, thermal integral, transport curve, manuscript, referee-response TeX/PDF, or published constraint figure was modified. The pure-vector Blinov Fig. 7 gate remains **NOT PASSED**; no axial/finite-mixing constraint curve is released.
- **Next P0 work:** derive the finite-recoil correction symbolically from the full crossed amplitude; establish the coefficients of the two asymptotic laws; then rederive the B.6 phase-space/Jacobian mapping and clarify the beta and initial-state averaging conventions. Do not rescale opacity or update production constraints before these steps are complete.


## 2026-11-12 preserved PR #69 / RC-001 upstream research notes

The following non-duplicated status entries were present on the active PR #69 branch but not yet in the main status ledger. They are retained here so that synchronizing PR #69 to main does not erase the cross-repository QLD8/EOM research context. These entries describe upstream algebraic work and open matching tasks; they do not add QLD8 coefficients to the PR #69 scalar two-point functions.

## 2026-11-10 update: explicit tree-level evanescents for EOM-generated Fierz channels

The upstream PR #11 is pinned at `49b70f5fce4966787b0dd41e741c35d3084bcf60`. The [EOM-generated chiral Fierz note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) now gives explicit \(E_{XY;V}^{\mu,rs}\) and \(E_{XY;T}^{\mu\nu,rs}\) differences for the scalar-vector and scalar-tensor channels generated by the second-order fermion EOM. The definitions include the operator-level Grassmann minus sign, the Levi-Civita terms, and the three-component chiral tensor basis; no \(O(\epsilon)\) physical-operator admixture is included at definition stage.

The 4D projections were checked in 34 exact matrix identities (8704/8704 components) plus six self-duality relations. The next step is no longer merely to list Fierz channels: it is to compute their one-loop mixing into the physical and evanescent dimension-eight basis, include UV-generated higher gamma strings, and match the same-order EFT soft/counterterm contributions.

Upstream runs 42735130364 and 42735130363 failed with empty job-step lists and unavailable logs; no CI pass is claimed. No coefficient is imported into PR #69 scalar two-point functions.

## 2026-11-10 update: EOM-generated scalar-vector and scalar-tensor Fierz projections

The upstream PR #11 is now pinned at `49b70f5fce4966787b0dd41e741c35d3084bcf60`. The new [EOM-generated chiral Fierz note](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD-EOM-generated-chiral-Fierz-identities.md) and exact SymPy audit establish the four scalar-vector chiral identities, the two opposite-chirality scalar-tensor identities including their Levi-Civita terms, and the two same-chirality scalar-tensor identities in the three-component self-dual basis.

Validation: 34 exact matrix identities passed (8704/8704 components), along with six chiral tensor self-duality checks. These are four-dimensional spinor projections and tree-level evanescent-difference definitions, not a one-loop mixing calculation.

The existing four scalar-pair evanescents are not closed after second-order EOM substitution. The generated vector/tensor structures need their own d-dimensional evanescent definitions, followed by a complete UV/EFT counterterm and soft-matching calculation. Upstream PR runs 42734711989 and 42734712057 failed with empty job-step lists and unavailable logs; no CI pass is claimed. No coefficient is imported into PR #69 scalar two-point functions.

## 2026-11-10 update: derivative-aware QLD8 Fierz/IBP and second-order fermion EOM

The upstream PR #11 now contains the following additional records, pinned at `49b70f5fce4966787b0dd41e741c35d3084bcf60`:

- [Derivative-aware Fierz/IBP ledger](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD8-derivative-Fierz-IBP-ledger.md): exact covariant-IBP identity for the complete source-pair sum, three Laplacian Leibniz classes, 9 ordered source pairs, 36 derivative placements, and the derivative-label map through spinor Fierz rearrangement.

- [Second-order fermion-EOM map](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD8-second-order-fermion-EOM-map.md): sign-checked Dirac-square identity and EOMs for \(Q_L,u_R,d_R,L_e,e_R\), including the generated Higgs-derivative and field-strength four-fermion structures.

Local exact checks passed for the derivative-placement bookkeeping and for the Minkowski Clifford algebra, Dirac-square curvature sign, Higgs-source hypercharges, and \(U(1)_X\) neutrality. The source-square IBP identity applies to the full product-rule sum, not to each placement individually.

A crucial open issue is now explicit: the four scalar-pair Fierz-difference evanescents are not closed after second-order EOM substitution. The generated \(\gamma^\mu D_\mu H\) and \(\sigma^{\mu\nu}\mathscr F_{\mu\nu}\) structures require an enlarged \(d\)-dimensional evanescent basis before one-loop renormalization and finite matching.

Upstream PR-triggered runs 42733380866 and 42733381140 both failed with empty job-step lists; log retrieval returned 404, so the cause is unknown. No CI pass is claimed. No QLD8 coefficient is imported into the PR #69 scalar two-point prediction.

## 2026-11-10 update: exact four-dimensional chiral Fierz algebra

- The upstream QLD8 source-pair census is now supplemented by exact four-dimensional chiral Fierz identities. The RR/LL scalar-tensor and RL/LR vector tensor identities were verified component by component, 1024/1024 exact components, using SymPy. See [RC-001-QLD-chiral-Fierz-identities.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD-chiral-Fierz-identities.md).

- The operator-level Fierz relations include the minus sign from reordering anticommuting fermion fields. The note also provides candidate minimal Fierz-difference evanescent definitions, but does not claim a complete d-dimensional evanescent basis or finite one-loop scheme conversion.

- A dedicated PR-triggered GitHub Actions workflow was added with SymPy 1.14.0 pinned. No run or combined status is currently returned for the latest upstream head; no CI pass is claimed. The exact SymPy identities were executed locally and passed.

- The upstream master fixes \(D=4-2\epsilon\) and \(\overline{\mathrm{MS}}\), but has not yet frozen the \(\gamma_5\) prescription or complete evanescent basis. The next gate is to choose and document these before d-dimensional Fierz/IBP reduction and finite Wilson-coefficient matching.

## 2026-11-10 update: QLD8 source-square channel census

- Upstream RC-001 now expands the leading Higgs source into \(J_d\), \(J_u\), and \(J_e\), and classifies the source-square term into nine ordered source pairs: three diagonal pairs and three cross pairs plus their Hermitian conjugates. See [RC-001-QLD-source-square-Fierz-channel-census.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD-source-square-Fierz-channel-census.md).

- The census distinguishes opposite-projector scalar pairs (vector-current Fierz channels) from same-projector pairs (scalar/tensor channels), and keeps the crossed quark-color contractions, antisymmetric weak contractions, flavor tensors, and four product-rule derivative placements per ordered pair explicit. These placements are not independent Wilson coefficients.

- Exact bookkeeping passed locally. No explicit \(d\)-dimensional Fierz/IBP reduction, evanescent counterterm basis, or final fermionic dimension-eight basis is claimed.

- The latest pinned upstream head 49b70f5fce4966787b0dd41e741c35d3084bcf60 has no workflow run/combined status returned. The latest known Candidate schema validation run 42724054652 on the preceding head failed with no job steps/logs available; no upstream CI pass is claimed.

- Next physical step: explicit \(d\)-dimensional Fierz and IBP reduction of the six source-pair structures, followed by the remaining mixed-background hard/soft matching.

## 2026-11-10 update: model-specific Higgs-source and flavor-charge census

- Upstream RC-001 now records the complete leading-renormalizable Higgs EOM source for the original flavor-diagonal axial model and the dimension-five \(C_5\) source at higher order. See [RC-001-QLD-Higgs-source-EOM-model-map.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD-Higgs-source-EOM-model-map.md).

- The charged-lepton \(U(1)_X\) Yukawa charge matrix shows that diagonal \(\mu,\tau\) renormalizable Yukawas are forbidden, but \(\bar L_\mu H\tau_R\) and \(\bar L_\tau H\mu_R\) are gauge-allowed. The original block-diagonal model sets these off-diagonal entries to zero by its flavor-diagonal assumption. They must not be called gauge-forbidden.

- The source map includes quark and electron renormalizable sources, explicit \(C_5\) axial sources, the leading fermion EOMs, and the \(M_E^{-5}\)/\(M_E^{-6}\) suppression of dimension-five source insertions in the \(O(M_E^{-4})\) operators. It does not perform Fierz reduction or claim a nonredundant fermionic dimension-eight basis.

- The exact charge and power-counting audit passed locally. The latest upstream Candidate schema validation run 42724054652 failed with an empty job-step list and no retrievable log; no upstream CI pass is claimed.

- Next step: reduce the source/current operators with fermion EOM and Fierz identities while retaining gamma-traceless derivative components and evanescent terms.

## 2026-11-10 update: C5 sign, gauge conventions, and QLD8 total currents

- The original v6 UV mass matrix has the heavy-block Schur complement \(m_{\ell,\mathrm{Schur}}=-y_\ell\lambda_\ell v_hv_s/(2M_{E_\ell})\). With the displayed EFT convention \(\mathcal L_5=-C_{5,\ell}S_\ell\bar L_\ell H\ell_R+\mathrm{h.c.}\), the coefficient is \(C_{5,\ell}=-y_\ell\lambda_\ell/M_{E_\ell}\).

- The positive relation printed in v6 Eq. (5-d), with the same displayed operator orientation and UV Lagrangian, gives the opposite signed mass. This is recorded as an internal manuscript-sign issue; no manuscript or referee-response edit is made. PR #69/RC-001 retain the Schur-complement convention. Existing results depending only on \(|C_5|^2\) or \(|C_5|^4\) are unchanged.

- The two covariant-derivative conventions are related by \(A_\mu^+=-A_\mu^-\): \(D^+=D^-\), raw component field strengths flip, the commutator curvature is invariant, and the raw-field gauge EOM changes sign. Coefficient translation is basis-dependent; the explicit dictionary is recorded in the convention audit.

- Added the exact-rational C5/gauge audit module and seven tests to PR #69; the workflow is configured to run and archive them. No new GitHub Actions run has yet been observed on the current PR head, so CI acceptance remains pending.

- In upstream high-energy-theory-research PR #11, the leading-renormalizable \(J_Y\), \(J_2^a\), and normalized \(J_X\) currents for the original one-VEV model are now fully expanded for the restricted QLD8 gauge-EOM representatives. See [RC-001-QLD-total-current-expansion.md](https://github.com/lm846802297-bit/high-energy-theory-research/blob/49b70f5fce4966787b0dd41e741c35d3084bcf60/research/RC-001-QLD-total-current-expansion.md). The exact-rational bookkeeping passed locally. Upstream Candidate schema validation run 42724054652 failed, but its job-step list was empty and logs were unavailable; no CI pass is claimed.

- Next physical step: fermion-EOM/Fierz reduction of the generated QLD8 source/current operators, followed by mixed-background hard/soft matching. No QLD8 coefficient is added to the PR #69 scalar two-point functions.

## 2026-11-10 update: RC-001 derivative-operator interface added to PR #69

- Added [RC001_UPSTREAM_INTERFACE.md](research/major1-higgs-scalar-mixing-20261109/RC001_UPSTREAM_INTERFACE.md) to the existing PR #69 branch. No new PR was opened.

- The interface pins high-energy-theory-research PR #11 at head commit 49b70f5fce4966787b0dd41e741c35d3084bcf60 and maps the RC-001 charged-lepton/VLL/Higgs/singlet interactions to the original one-VEV axial \(S+\mathrm{VLL}\) model.

- The interface keeps the upstream repository as the sole source for calculation scripts and validation artifacts. It distinguishes the fermionic QLD8 derivative operator, the bosonic Higgs higher-derivative source, and PR #69's scalar-potential \(O_8^{\rm pot}=(H^\dagger H)^2(S^\dagger S)^2\).

- The C5 sign and SM covariant-derivative convention have now been algebraically audited and mapped in C5_GAUGE_CONVENTION_AUDIT_2026-11-10.md. The printed v6 Eq. (5-d) coefficient remains an internal manuscript-sign discrepancy; no manuscript or formal reply edit is made.

- The upstream non-Abelian IBP/EOM result is treated as a restricted algebraic mapping, not a complete dimension-eight basis or a new scalar self-energy contribution. The latest workflow on the pinned upstream head has no successful CI status; the reported failed run has no retrievable step/log detail.

- PR #69 remains Open / Draft. Its scalar self-energy benchmarks, finite \(O_8^{\rm pot}\) matching, and physical-pole limitations are unchanged. This interface does not promote QLD8 coefficients into \(\Pi_{hh}\), \(\Pi_{hs}\), or \(\Pi_{ss}\).

**Current repository status correction:** PR #72 was merged on 2026-11-09 (merge time 06:46 UTC); the older 2026-11-09 status snapshot below that still labels PR #72 Open is superseded by this entry. PR #69 remains the active Higgs–radial-scalar research branch for this interface.

## 2026-11-12 preserved P1-IIIe SFHo/FRDM real-table closure note

The following non-duplicated source-archive status note is retained from the SFHo/FRDM transfer branch. It records the numerical validity domain and remaining test limitations; it is not a claim that every original-table test ran in the current environment.

> **P1-IIIe-B SFHo/FRDM v1.03 真实表数据与局域闭合（2026-11-11，后续数值修正）：** 官方 Basel 五个对象的获取器、五项 SHA-256 manifest 与 Release 归档已核对；Release tag sfho-frdm-v1.03-data 指向 e68eae83385dcb62b31b7fa12bf32f85a2e7a819，五个资产 digest 与 manifest 一致，总计 322,921,457 B。HTTP HEAD 的 --check-urls 只证明 HTTP 200 与 Content-Length 匹配，不被描述为远端内容哈希验证。224 点闭合采用 1024 阶 Gauss–Legendre；独立 1024/2048 对照在 448 个核子状态上的最大 Fdeg 绝对差为 4.7117e-8，数密度最大相对差为 1.0115e-8；1024 阶对 fixture 的最大 Fdeg 绝对差为 4.995e-11。旧 512 阶在冷、高密度中子状态可有 2.73% 偏差，因此 fixture 与原始表复算测试均已统一到 1024 阶。有效域仍为 224 点采样网格上的 208/224 格；中子最大偏差 6.1345e-4，质子（Xp≥1e-6）最大偏差 8.8578e-5。其余 16 格并非全部冻结：nB=1.10e-12 与 1e-10 fm⁻³ 的 8 格为明确平台；1e-8 的 4 格为过渡；1e-6 的 4 格更接近闭合但仍未满足 1e-3。16 格均为核子主导组成，Xn+Xp≈1，组成随 Yp 变化。自然单位稀释度在 T=63.096 MeV、nB=1e-6 fm⁻³ 时为 3.06e-5。核团比例统计代码已改为只使用 308 个物理密度行；由于本次未重读原始 composition archive，更新后的整表比例暂不作数值声明。五对象 Manifest、下载器与审计 JSON 的名称和哈希集合一致。本次独立 JavaScript fixture 交叉核验 12 组检查全部通过；这不是 Python unittest 运行结果。17 项 Python 测试尚未重新执行，四项原始表测试仍需 SFHO_TABLES_DIR；当前执行环境无法把 Release 二进制附件下载到数值运行环境。无新的 Python 测试或 CI 通过声明。


## 2026-11-12 repository synchronization and numerical validation checkpoint

- Latest main at this checkpoint: `c7dedb4a0ab8e12cbc78b3c6b621b7a52ce89da5`.
- Open research PRs #53, #68, and #69 are each synchronized with main (`behind_by=0`). PR #56 was merged on 2026-11-12 at `293d047013cce0dc3fbc44b2cd679f2df0f253dd`; its research branch remains available and is also synchronized with main (`behind_by=0`). PR #57 remains merged into the PR #56 research branch.
- The active C4-C4, moving-muon, P1-IIIe EOS source-transfer, PR #57 source-bundle, and SFHo/FRDM transfer branches were each one commit behind main because main added only this file's Major 4.4 validation-status update. They were fast-forward-history synchronized by merge commits; no research files or data blobs were rewritten.
- Final comparison against main reports `behind_by=0` for all nine checked active research/transfer branches: PR #53, merged-PR #56 research branch, PR #68, PR #69, C4-C4, moving-muon, P1-IIIe EOS transfer, PR #57 source bundle, and SFHo/FRDM transfer.
- Major 4.4 EFT numerical validation Run [43206544367](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544367) completed successfully on commit `c611005c6cb343f8a53b282e14d15a8b6468b541`. Its steps include C4C3 direct-recomputation SHA-256 manifest verification, SFHo/FRDM release-manifest verification and archive reconstruction, research-level rate/transport/kernel tests, Blinov and EOS regression tests, independent rate audits, saved-scan reproducibility, and figure regeneration. This is a software/data reproducibility acceptance on that exact commit, not by itself a claim that the published Blinov Fig. 7 physical benchmark has been fully reproduced.
- The contemporaneous failure Run [43202685556](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43202685556) occurred during unittest discovery: 359 tests were run, with one import error because `finite_mixing.thermal_integrals.test_vector_longitudinal_projector` could not import `audit_vector_longitudinal_projector`. The other executed tests passed; downstream stages were skipped. A later run on a newer commit passed the full numerical-validation workflow. The earlier cancellation of Run #158 is not counted as a physical failure.
- Preserve the distinction between CI checks, archive integrity, numerical convergence, and physical benchmark acceptance. Any remaining physical Fig. 7 discrepancy or unvalidated transport assumption must remain explicitly open until its dedicated comparison passes.


## 2026-11-13 PR #77 — Major 4.4 post-merge follow-up

- Follow-up PR: [#77](https://github.com/lm846802297-bit/axial-vector-review-response/pull/77), **Open / Draft**, base `main`; branch `research/major44-postmerge-followup-20261113`.
- Created from main commit `657224b7107dd2844a9d623acd37b09c3e8b6d5f`; the follow-up branch has one commit ahead and `behind_by=0`.
- The 13-path post-merge comparison was reviewed. The PR retains eight provenance-only JSON refreshes, the package-relative import correction for the direct longitudinal-projector test, and the review record in `VALIDATION_AND_REVIEW.md`. It excludes three JSON outputs with only final-digit floating-point differences and the workflow's comment-only change.
- Major 4.4 EFT validation [Run #43206544367](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43206544367) completed successfully on source commit `c611005c6cb343f8a53b282e14d15a8b6468b541`. This is software/data reproducibility evidence, not physical Fig. 7 acceptance.
- **Physics gate remains open:** pure-vector Blinov Fig. 7 is **NOT PASSED**; the 10 MeV high-absorption discrepancy remains unresolved. No opacity/profile rescaling, production-kernel replacement, or axial constraint update is accepted.
- Historical status note superseded on 2026-11-13: PR #77 was merged; PR #83 was closed as its duplicate. See the current branch-integration audit.


## 2026-11-13 current-main research index and archive-policy update

- Current canonical navigation is research/MAIN_RESEARCH_INDEX_2026-11-13.md. It maps Major 1, Major 3, Major 4.4, C4-C4-A/Aq/B, the original one-VEV line, the two-VEV extension, and collaborator deliverables to their current-main paths and merge history.
- PR #100 was closed as redundant after confirming PR #85 already integrated the two-VEV baseline and main had since consolidated the shared thermal implementation. No old duplicate implementation was merged.
- The two-VEV formula/implementation review is recorded in research/stellar-cooling-two-vev-20261105/PHYSICS_CROSSCHECK_2026-11-13.md. It confirms the stated mass/Goldstone algebra while documenting the physical CP-odd state, PMNS/charged-N_R caveats, frame-dependent T/L split, and missing independent azimuthal convergence scan.
- The original 12-part/75-member review-package provenance metadata is retained under research/stellar-cooling-collaborator-archive-20261113/provenance/original-review-package/; duplicate source payloads are not copied there.
- Generated collaborator ZIPs are no longer uploaded as GitHub Actions artifacts. The builder remains for local packaging and direct handoff only.
- The pure-vector Blinov Fig. 7 physical benchmark remains **NOT PASSED** at the 10 MeV strong-absorption end. No axial limit curve is promoted by this documentation and repository-organization update.


- Thirteen legacy GitHub Actions ZIP artifacts from earlier packaging runs were deleted by cleanup run #43358373940. All 13 original workflow runs were re-queried and returned zero remaining artifacts. The temporary cleanup workflow was removed after success.


## 2026-11-13 physics and branch audit continuation

- The direct axial-current / Goldstone amplitude identity is now encoded as a regression: q_nu M_A^nu = 2 m_mu M_P for the source's gamma^nu(gV - gA gamma5) convention. The five-point independent spinor check closes at or below 9.0e-13; see PHYSICS_CROSSCHECK_2026-11-13.md.
- The pure-axial Goldstone map is explicitly separated from finite right-handed mixing. For g_A=-g_X cos^2(theta_R), the current-side Ward requirement includes cos^2(theta_R); the full UV phase projection at finite mixing remains open.
- A nontrivial unitary PMNS regression confirms Tr(G_nu^dagger G_nu)=2 while producing off-diagonal flavour couplings. The minimal-model U_PMNS=I assumption remains an approximation, not an oscillation fit.
- Branch-by-branch tree/blob findings and deletion candidates are recorded in research/BRANCH_DISPOSITION_2026-11-13.md. PR #102 remains active and must be preserved.


## 2026-11-13 branch cleanup execution

- First batch complete: 11 stale refs with heads already reachable from main were deleted and individually verified absent by cleanup run #43364401393.
- Their commits remain reachable from main; no research commit history was discarded.
- The active PR #102 branch and divergent Major 1, Major 4.4, C4-C4-A/B, and two-VEV history branches were not touched.
- The temporary pruning workflow is removed in the follow-up documentation PR after successful execution.


## 2026-11-13 second branch cleanup execution

- Five completed administrative branches were deleted and verified absent by run #43364866549.
- The cleanup checked each expected SHA and refused any branch used by an open PR.
- Their merged PR histories remain available; no research source, numerical output, or research-history branch was removed.
- The one-time cleanup workflow was removed after success.


## 2026-11-13 current Major 4.4 branch status

- PR #102 v1 is closed without merge; its branch is retained as a historical snapshot.
- Historical snapshot before the 2026-11-14 merges: PR #106 v2 was the active draft and was synchronized with main. It included the P0 polarization Boltzmann state-counting addendum and seven algebraic regression tests; its scalar B.2 reference and axial-vector curves remained unchanged.
- B.1 local-energy/\(E_\infty\) integration is exactly equivalent by a Jacobian change of variables.
- B.2 fixed-\(\omega\) gives +92.43%; the redshift-only conserved-\(E_\infty\) diagnostic gives +36.91% but retains Euclidean chords.
- The generic static-spherical GR ray kernel passes six independently executed tests, but the reconstructed profile lacks same-snapshot \(B(r)\) and \(M(r)\); the paper's Garching pseudo-Newtonian baseline is spatially flat.
- The 15–25 km shells contribute 56.71% of source-weighted mean total optical depth; 110–510 MeV supplies 94.43% of escaped luminosity.
- Local mode sums/detailed balance pass at \(10^{-14}\), while scalar B.2 and mode-resolved propagation differ by 76.37. Keep them separate; no opacity correction or axial-curve update is authorized.


## 2026-11-13 P0 polarization state-counting

The active PR #106 line now contains the analytic mode-resolved Boltzmann collision-term derivation, total-occupation closure, and seven algebraic regression tests. The literal scalar B.2 reproduction remains unchanged; the physical no-mixing transport lane remains mode-resolved pending the exact B.13 Compton polarization kernel.


## 2026-11-13 P1 exact B.13 polarization-kernel validation

The exact moving-muon B.13 local kernel already resolves \(L,+,-\), both muon charges, exact recoil, Fermi blocking, Bose enhancement, and independent production/absorption. A new independent explicit-spinor audit now compares the production Dirac trace with explicit on-shell spinors and two physical photon polarizations at five moving-muon kinematic points, for six pure/mixed-current charge cases (30 cases, 90 mode matrix elements).

Local maxima: spinor/trace relative residual \(1.77\times10^{-13}\); explicit photon-Ward amplitude residual \(1.47\times10^{-13}\); final-muon shell residual \(6.52\times10^{-16}\); vector longitudinal Ward-shift residual \(3.54\times10^{-14}\). All mode matrix elements are nonnegative. The dedicated P1 GitHub Actions workflow completed successfully: [run #43372084167](https://github.com/lm846802297-bit/axial-vector-review-response/actions/runs/43372084167).

This is a pointwise amplitude validation, not a dense continuous-domain thermal convergence bound or global independent-mode transport result. The scalar B.2 baseline and axial-vector production outputs remain unchanged.
