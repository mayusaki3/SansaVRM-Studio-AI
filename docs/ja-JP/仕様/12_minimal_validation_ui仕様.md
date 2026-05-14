<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000030Z-SVSA
lang: ja-JP
canonical_title: minimal validation UI仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > minimal validation UI仕様

# minimal validation UI仕様

## 1. 目的

本仕様は、SansaVRM Studio AI の architecture validation を目的とした最小 Web UI を定義する。

本 UI は production UI ではなく、project workspace、artifact registry、workflow run、artifact dependency graph の構造を早期確認するための検証 UI とする。

## 2. 前提

- AI 実行機能は含めない。
- UI は local server から配信する。
- 初期状態は localhost mode とする。
- project / workflow / artifact の構造確認を優先する。

## 3. 画面

### 3.1 Project Summary

表示項目:

- project_id
- project_name
- schema_version
- artifact_count
- workflow_run_count

### 3.2 Artifact List

表示項目:

- artifact_id
- artifact_type
- path

### 3.3 Workflow Run List

表示項目:

- workflow_run_id
- workflow_type
- status
- local_only

### 3.4 Workflow Graph

表示項目:

- artifact_id
- created_by_step
- depends_on

初期 PoC ではテーブル表示でよい。

## 4. API 利用

UI は以下の API を使用する。

- GET /api/health
- GET /api/project
- GET /api/artifacts
- GET /api/workflow-runs
- GET /api/workflow-graph

## 5. 禁止事項

- minimal validation UI に AI 実行機能を直接入れてはならない。
- 制限付き素材の画像プレビューを無制限に表示してはならない。
- LAN 公開を初期状態にしてはならない。

## 6. 次アクション

- static HTML を追加する。
- local server から static UI を配信する。
- 起動手順を README に追加する。

---

[目次](../目次.md) > 仕様 > minimal validation UI仕様
