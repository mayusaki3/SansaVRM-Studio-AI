<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260513-000018Z-SVSA
lang: ja-JP
canonical_title: authoring workflowテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > authoring workflowテスト仕様

# authoring workflowテスト仕様

## 1. 目的

authoring workflow の lifecycle が期待通り定義されていることを確認する。

## 2. テストケース

### TC-WF-001

目的:

input → analysis → decomposition の順序を確認する。

期待結果:

- decomposition の前に analysis が存在する。

---

### TC-WF-002

目的:

review が generation support の前に存在することを確認する。

期待結果:

- review phase が generation support phase より前に存在する。

---

### TC-WF-003

目的:

validation が distribution preparation より前に存在することを確認する。

期待結果:

- validation phase が distribution preparation phase より前に存在する。

---

### TC-WF-004

目的:

irreversible export warning を distribution preparation で扱うことを確認する。

期待結果:

- irreversible export warning が存在する。

---

### TC-WF-005

目的:

review を通さず inferred layer を正本扱いしないことを確認する。

期待結果:

- inferred layer は review 未完了状態で canonical 扱いされない。

---

## 3. カバレッジ観点

- lifecycle order
- review gating
- validation gating
- irreversible export
- inferred layer review

---

[目次](../目次.md) > テスト > authoring workflowテスト仕様
