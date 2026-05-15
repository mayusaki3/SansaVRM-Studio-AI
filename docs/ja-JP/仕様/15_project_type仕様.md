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
- 他形式から SansaVRM へ変換する。
- 複数 SansaVRM から必要な要素のみを集め、新しい SansaVRM を組み立てる。
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

SansaVRM と外部形式の双方向変換を扱う。

入力候補:

- SansaVRM
- VRM
- glTF / GLB
- FBX
- MMD
- その他 adapter が対応する形式

出力候補:

- SansaVRM
- VRM
- glTF / GLB
- FBX
- MMD
- その他 adapter が対応する形式

主な処理:

- SansaVRM import
- external format import
- SansaVRM export
- external format export
- compatibility validation
- conversion diagnostics
- loss report
- preserve_only / unsupported / source_raw handling
- policy / restriction preservation

### 4.3 sansavrm_assembly

目的:

複数の SansaVRM から必要な asset / layer / metadata / policy / provenance を選択し、新しい SansaVRM を組み立てる。

入力候補:

- source SansaVRM A
- source SansaVRM B
- source SansaVRM C
- body layer
- clothing layer
- hair layer
- accessory layer
- material set
- expression set
- physics setting
- policy / restriction block
- provenance block

出力候補:

- assembled SansaVRM
- derived SansaVRM
- distribution SansaVRM
- export package
- assembly report

主な処理:

- source SansaVRM import
- component selection
- layer extraction
- compatibility validation
- conflict detection
- policy merge
- restriction merge
- provenance merge
- derived asset generation
- assembly report generation

想定例:

```text
SansaVRM A: body / face / rig
SansaVRM B: clothing / material
SansaVRM C: hair / accessory
↓
SansaVRM D: assembled character
```

### 4.4 sansavrm_outfit_composition

目的:

`outfit_composition` は `sansavrm_assembly` の特殊ケースとして扱う。

主に body asset と clothing asset の組み合わせ、fitting、replacement、policy rewrite、derived asset generation を扱う。

将来的には `sansavrm_assembly` の workflow template 内へ統合する可能性がある。

## 5. project_type registry

SansaVRM Studio AI は project_type registry を持つ。

registry は以下を定義する。

- project_type id
- display name
- required asset types
- workflow templates
- supported import types
- supported export types
- workspace UI definition
- policy handlers
- restriction handlers
- component selection rules
- merge rules

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

```text
sansavrm_conversion
 ├ source import
 ├ compatibility validation
 ├ conversion mapping
 ├ conversion execution
 ├ diagnostics / loss report
 └ target export
```

```text
sansavrm_assembly
 ├ source SansaVRM import
 ├ component scan
 ├ component selection
 ├ compatibility validation
 ├ conflict detection
 ├ policy / restriction merge
 ├ provenance merge
 ├ assembly execution
 └ assembly report
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
- Assembly Workspace
- Outfit Workspace

## 8. project schema

project schema は project_type を必須項目として持つ。

## 9. 禁止事項

- project_type 未定義の project を保存してはならない。
- project_type と無関係な workflow template を自動追加してはならない。
- project_type を workflow 実行中に変更してはならない。
- sansavrm_conversion で変換方向を記録せずに conversion workflow を実行してはならない。
- sansavrm_assembly で source SansaVRM と選択 component の対応を記録せずに assembly workflow を実行してはならない。
- policy / restriction の conflict を検出せずに assembled SansaVRM を distribution state として扱ってはならない。

## 10. 次アクション

- project schema を更新する。
- project_type registry 実装を追加する。
- Project Viewer UI を作成する。
- project_type 別 Workspace UI を整理する。
- sansavrm_conversion の conversion direction schema を定義する。
- sansavrm_assembly の component selection schema を定義する。
- policy / restriction merge rule を定義する。

---

[目次](../目次.md) > 仕様 > project type仕様
