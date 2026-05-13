<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000020Z-SVSA
lang: ja-JP
canonical_title: project workspace仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > project workspace仕様

# project workspace仕様

## 1. 目的

本仕様は、SansaVRM Studio AI における project workspace の概念、保存単位、workflow step 間のデータ連携、project package の保存方式を定義する。

## 2. 結論

SansaVRM Studio AI は、workflow を直接開始しない。

必ず project workspace を作成し、その project 内で workflow run を実行する。

理由:

- 入力素材、生成物、検証結果、補正指示、provenance を一体管理する必要がある。
- step 間データ連携を file path の暗黙参照にすると再現性が失われる。
- 途中再開、再実行、差分比較、流通版 export を成立させる必要がある。
- local-only / external-service opt-in の記録を project 単位で保持する必要がある。

## 3. project workspace

project workspace は、Studio AI の作業単位である。

project は以下を保持する。

- project metadata
- source inputs
- workflow runs
- artifacts
- prompts
- decomposition results
- validation results
- risk assessment results
- provenance
- export results

## 4. project metadata

project metadata は以下を持つ。

```json
{
  "project_id": "prj-20260514-000001",
  "project_name": "sample_project",
  "created_at": "2026-05-14T00:00:00Z",
  "updated_at": "2026-05-14T00:00:00Z",
  "schema_version": "0.1.0",
  "local_only_default": true
}
```

## 5. workflow run

workflow run は、project 内で実行された一連の処理を表す。

```json
{
  "workflow_run_id": "run-20260514-000001",
  "workflow_type": "ai_preprocess",
  "status": "completed",
  "started_at": "2026-05-14T00:00:00Z",
  "completed_at": "2026-05-14T00:05:00Z"
}
```

## 6. workflow step

workflow step は、workflow run 内の処理単位である。

標準 step 候補:

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

## 7. step 間データ連携

step 間のデータ連携は、artifact reference により行う。

file path を直接受け渡すのではなく、artifact_id を介して参照する。

```json
{
  "step_id": "step-decomposition-001",
  "input_artifacts": [
    "artifact-source-image-001"
  ],
  "output_artifacts": [
    "artifact-decomposition-001"
  ]
}
```

## 8. artifact

artifact は、project 内で生成・保存される成果物である。

artifact は以下を持つ。

```json
{
  "artifact_id": "artifact-decomposition-001",
  "artifact_type": "decomposition_result",
  "path": "artifacts/decomposition/decomposition_001.json",
  "created_by_step": "step-decomposition-001",
  "provenance_id": "prov-001",
  "hash": "sha256:..."
}
```

## 9. artifact_type

標準 artifact_type 候補:

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

## 10. project directory layout

project workspace の標準 layout は以下とする。

```text
project_root/
├ project.json
├ workflow_runs/
│ └ run-20260514-000001.json
├ artifacts/
│ ├ source/
│ ├ analysis/
│ ├ risk/
│ ├ decomposition/
│ ├ multiview/
│ ├ prompts/
│ ├ validation/
│ ├ distribution/
│ └ export/
├ provenance/
├ reports/
└ logs/
```

## 11. project package

project 一式は、project package として保存できる。

標準形式:

```text
.svsa-project.zip
```

project package は project_root を zip 化したものとする。

## 12. 再開と再実行

Studio AI は project.json と workflow_runs を読み込み、以下を行えること。

- workflow run の履歴表示
- step 単位の再実行
- artifact 単位の再利用
- user_review 以降の再開
- export profile の再適用

## 13. 禁止事項

- workflow を project なしで実行してはならない。
- step 間で artifact_id を介さず暗黙の file path のみで連携してはならない。
- local-only 設定を workflow run に記録せず実行してはならない。
- external-service opt-in の有無を provenance に記録せず実行してはならない。

## 14. 次アクション

- project.json schema を定義する。
- artifact registry schema を定義する。
- workflow run schema を定義する。
- project package export / import の PoC を実装する。

---

[目次](../目次.md) > 仕様 > project workspace仕様
