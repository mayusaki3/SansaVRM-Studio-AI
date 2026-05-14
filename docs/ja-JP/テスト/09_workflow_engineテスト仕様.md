<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000027Z-SVSA
lang: ja-JP
canonical_title: workflow engineテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > workflow engineテスト仕様

# workflow engineテスト仕様

## 1. 目的

workflow engine の step execution、artifact dependency graph、rerun、resume を確認する。

## 2. テストケース

### TC-WE-001

目的:

input_artifact が存在しない場合、step が failed になることを確認する。

---

### TC-WE-002

目的:

step 実行後に artifact dependency graph が更新されることを確認する。

---

### TC-WE-003

目的:

rerun 時に新しい artifact_id が生成されることを確認する。

---

### TC-WE-004

目的:

resume 時に既存 artifact を再利用できることを確認する。

---

## 3. カバレッジ観点

- step execution
- dependency graph
- rerun
- resume
- status transition

---

[目次](../目次.md) > テスト > workflow engineテスト仕様
