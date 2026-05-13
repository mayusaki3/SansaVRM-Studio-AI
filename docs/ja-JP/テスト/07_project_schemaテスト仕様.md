<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000023Z-SVSA
lang: ja-JP
canonical_title: project schemaテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > project schemaテスト仕様

# project schemaテスト仕様

## 1. 目的

project schema の validation を確認する。

## 2. テストケース

### TC-SCHEMA-001

目的:

project.json に必須項目が存在することを確認する。

期待結果:

- project_id exists
- schema_version exists
- artifact_registry_path exists

---

### TC-SCHEMA-002

目的:

artifact registry が artifact_id を保持することを確認する。

期待結果:

- artifact_id exists
- artifact_type exists

---

### TC-SCHEMA-003

目的:

workflow step が artifact_id により step 間連携を行うことを確認する。

期待結果:

- input_artifacts exists
- output_artifacts exists

---

### TC-SCHEMA-004

目的:

未知 status を rejection できることを確認する。

入力:

```json
{
  "status": "invalid_status"
}
```

期待結果:

- validation error

---

### TC-SCHEMA-005

目的:

workflow_type=ai_preprocess を許可できることを確認する。

期待結果:

- validation success

---

## 3. カバレッジ観点

- project.json
- artifact registry
- workflow run
- workflow step
- status validation
- artifact reference

---

[目次](../目次.md) > テスト > project schemaテスト仕様
