<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000022Z-SVSA
lang: ja-JP
canonical_title: project schema仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > project schema仕様

# project schema仕様

## 1. 目的

本仕様は、SansaVRM Studio AI の project workspace を構成する主要 schema を定義する。

対象 schema:

- project.json
- artifact registry
- workflow run
- workflow step

## 2. project.json

project.json は project workspace の入口となる。

必須項目:

```json
{
  "project_id": "prj-20260514-000001",
  "project_name": "sample_project",
  "schema_version": "0.1.0",
  "created_at": "2026-05-14T00:00:00Z",
  "updated_at": "2026-05-14T00:00:00Z",
  "local_only_default": true,
  "artifact_registry_path": "artifacts/artifact_registry.json",
  "workflow_runs_path": "workflow_runs"
}
```

## 3. artifact registry

artifact registry は project 内 artifact の一覧と参照情報を保持する。

必須項目:

```json
{
  "schema_version": "0.1.0",
  "artifacts": [
    {
      "artifact_id": "artifact-source-image-001",
      "artifact_type": "source_image",
      "path": "artifacts/source/source_001.png",
      "created_by_step": "step-input-import-001",
      "provenance_id": "prov-001",
      "hash": "sha256:..."
    }
  ]
}
```

## 4. workflow run

workflow run は project 内で実行された一連の workflow を表す。

必須項目:

```json
{
  "workflow_run_id": "run-20260514-000001",
  "workflow_type": "ai_preprocess",
  "status": "completed",
  "local_only": true,
  "started_at": "2026-05-14T00:00:00Z",
  "completed_at": "2026-05-14T00:05:00Z",
  "steps": []
}
```

## 5. workflow step

workflow step は workflow run 内の処理単位である。

必須項目:

```json
{
  "step_id": "step-decomposition-001",
  "step_type": "decomposition",
  "status": "completed",
  "input_artifacts": [
    "artifact-source-image-001"
  ],
  "output_artifacts": [
    "artifact-decomposition-001"
  ]
}
```

## 6. status

workflow run / workflow step の status は以下を使用する。

- pending
- running
- completed
- failed
- skipped
- cancelled

## 7. artifact_type

標準 artifact_type は以下とする。

- source_image
- source_prompt
- source_reference
- analysis_result
- copyright_risk_result
- segmentation_mask
- decomposition_result
- multi_view_image
- prompt_pack
- validation_result
- distribution_profile
- export_result
- report

## 8. workflow_type

標準 workflow_type は以下とする。

- ai_preprocess
- copyright_risk_assessment
- decomposition
- multi_view_generation
- distribution_preparation
- export

## 9. step_type

標準 step_type は以下とする。

- input_import
- source_analysis
- copyright_risk_assessment
- decomposition
- multi_view_generation
- user_review
- prompt_pack_generation
- downstream_generation_support
- validation
- distribution_preparation
- export

## 10. 禁止事項

- project_id なしで project workspace を保存してはならない。
- artifact registry なしで artifact を参照してはならない。
- workflow step は input_artifacts / output_artifacts を artifact_id で参照しなければならない。
- file path のみで step 間データ連携してはならない。

---

[目次](../目次.md) > 仕様 > project schema仕様
