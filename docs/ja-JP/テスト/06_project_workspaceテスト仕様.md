<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000021Z-SVSA
lang: ja-JP
canonical_title: project workspaceテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > project workspaceテスト仕様

# project workspaceテスト仕様

## 1. 目的

project workspace の保存、workflow run、artifact reference、再開機能を確認する。

## 2. テストケース

### TC-PROJ-001

目的:

workflow を project なしで開始できないことを確認する。

期待結果:

- workflow start rejected

---

### TC-PROJ-002

目的:

workflow run が project 内へ保存されることを確認する。

期待結果:

- workflow_runs directory exists
- workflow run metadata saved

---

### TC-PROJ-003

目的:

step 間データ連携が artifact_id を介して行われることを確認する。

期待結果:

- step metadata contains artifact references
- direct implicit file-only linkage not used

---

### TC-PROJ-004

目的:

project package export が可能であることを確認する。

期待結果:

- .svsa-project.zip generated

---

### TC-PROJ-005

目的:

project package import 後に workflow resume が可能であることを確認する。

期待結果:

- workflow history restored
- artifact registry restored

---

### TC-PROJ-006

目的:

external-service opt-in が provenance に記録されることを確認する。

期待結果:

- provenance contains opt-in state

---

## 3. カバレッジ観点

- project lifecycle
- workflow run persistence
- artifact registry
- project package export/import
- workflow resume
- provenance persistence

---

[目次](../目次.md) > テスト > project workspaceテスト仕様
