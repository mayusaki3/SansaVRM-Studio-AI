<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000025Z-SVSA
lang: ja-JP
canonical_title: project persistenceテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > project persistenceテスト仕様

# project persistenceテスト仕様

## 1. 目的

project workspace の保存・読み込み・package export/import を確認する。

## 2. テストケース

### TC-PERSIST-001

目的:

project.json を保存できることを確認する。

期待結果:

- project.json exists

---

### TC-PERSIST-002

目的:

artifact_registry.json を保存できることを確認する。

期待結果:

- artifact_registry.json exists

---

### TC-PERSIST-003

目的:

workflow run JSON を保存できることを確認する。

期待結果:

- workflow_runs/*.json exists

---

### TC-PERSIST-004

目的:

project package export が成功することを確認する。

期待結果:

- .svsa-project.zip generated

---

### TC-PERSIST-005

目的:

project package import 後に project metadata を復元できることを確認する。

期待結果:

- project_id restored
- workflow_runs restored

---

### TC-PERSIST-006

目的:

project.json 欠落時に import error を返すことを確認する。

期待結果:

- import validation error

---

## 3. カバレッジ観点

- project save
- artifact registry save
- workflow run save
- export/import
- validation
- restoration

---

[目次](../目次.md) > テスト > project persistenceテスト仕様
