<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260515-000034Z-SVSA
lang: ja-JP
canonical_title: project type仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > project type仕様

# project type仕様

## 1. 目的

本仕様は、SansaVRM Studio AI における project_type system を定義する。

## 2. 背景

SansaVRM Studio AI は単一 workflow を扱うツールではない。

以下のような異なる目的の project を扱う。

- 画像/プロンプトから SansaVRM を生成する。
- SansaVRM を他形式へ変換する。
- 複数 SansaVRM を合成する。
- policy / restriction を編集する。
- export 用 package を作成する。

そのため、project 毎に workflow、必要 asset、UI、policy、export 処理が異なる。

## 3. 定義

project_type は、project の役割と workflow 構成を定義する識別子である。

## 4. 初期 project_type

### 4.1 image_prompt_to_sansavrm

目的:

- image
- prompt
- decomposition
- multi-view generation
- SansaVRM generation

### 4.2 sansavrm_conversion

目的:

- SansaVRM import
- VRM export
- glTF export
- FBX export
- MMD export
- compatibility validation

### 4.3 sansavrm_outfit_composition

目的:

- body asset
- clothing asset
- fitting
- replacement
- policy rewrite
- derived asset generation

## 5. project_type registry

SansaVRM Studio AI は project_type registry を持つ。

registry は以下を定義する。

- project_type id
- display name
- required asset types
- workflow templates
- supported export types
- workspace UI definition
- policy handlers
- restriction handlers

## 6. Workflow Template

project_type は workflow template を定義する。

例:

```text
image_prompt_to_sansavrm
 ├ decomposition
 ├ copyright risk assessment
 ├ multi-view generation
 └ SansaVRM generation
```

## 7. UI 構造

Project Workspace は project_type に応じて UI を切り替える。

共通 UI:

- Dashboard
- Assets
- Workflow Inspector
- Graph
- Policies
- Provenance
- Export
- Settings

固有 UI:

- Generate Workspace
- Conversion Workspace
- Outfit Workspace

## 8. project schema

project schema は project_type を必須項目として持つ。

## 9. 禁止事項

- project_type 未定義の project を保存してはならない。
- project_type と無関係な workflow template を自動追加してはならない。
- project_type を workflow 実行中に変更してはならない。

## 10. 次アクション

- project schema を更新する。
- project_type registry 実装を追加する。
- Project Viewer UI を作成する。
- project_type 別 Workspace UI を整理する。

---

[目次](../目次.md) > 仕様 > project type仕様
