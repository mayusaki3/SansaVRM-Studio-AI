<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000024Z-SVSA
lang: ja-JP
canonical_title: project persistence仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > project persistence仕様

# project persistence仕様

## 1. 目的

本仕様は、SansaVRM Studio AI の project workspace をファイルシステムへ保存・復元・パッケージ化する方式を定義する。

## 2. 対象

対象:

- project.json 保存
- artifact_registry.json 保存
- workflow run 保存
- project package export
- project package import

## 3. project 保存

project workspace は以下の layout で保存する。

```text
project_root/
├ project.json
├ workflow_runs/
├ artifacts/
│ └ artifact_registry.json
├ provenance/
├ reports/
└ logs/
```

## 4. project.json

project.json は project の入口情報を保持する。

必須項目:

- project_id
- project_name
- schema_version
- local_only_default
- artifact_registry_path
- workflow_runs_path

## 5. artifact_registry.json

artifact_registry.json は artifact 一覧を保持する。

必須項目:

- schema_version
- artifacts

artifact は以下を持つ。

- artifact_id
- artifact_type
- path

## 6. workflow run 保存

workflow run は `workflow_runs/{workflow_run_id}.json` として保存する。

## 7. project package export

project package は project_root を zip 化したものとする。

拡張子:

```text
.svsa-project.zip
```

## 8. project package import

project package import は zip を展開し、project.json を読み込む。

## 9. 禁止事項

- project.json なしで project import を成功扱いしてはならない。
- artifact_registry.json が欠落している場合は警告または validation error を返す。
- workflow run の JSON が壊れている場合は、該当 run を failed import として扱う。

## 10. 次アクション

- Python PoC を実装する。
- 保存・読み込みテストを作成する。
- export/import テストを作成する。

---

[目次](../目次.md) > 仕様 > project persistence仕様
