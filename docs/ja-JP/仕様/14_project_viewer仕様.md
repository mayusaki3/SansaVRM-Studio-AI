<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260515-000033Z-SVSA
lang: ja-JP
canonical_title: project viewer仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > project viewer仕様

# project viewer仕様

## 1. 目的

本仕様は、SansaVRM Studio AI の起動後に表示する Project Viewer と、Project Workspace への遷移構造を定義する。

## 2. 結論

SansaVRM Studio AI は、起動直後に workflow 画面を表示しない。

起動後は Project Viewer を表示し、既存 project の選択、新規 project 作成、project package import を行ってから Project Workspace へ遷移する。

## 3. 画面遷移

```text
起動
  ↓
Project Viewer
  ├ 既存 project を開く
  ├ 新規 project を作成する
  ├ project package を import する
  └ 最近使った project を開く
      ↓
Project Workspace
```

## 4. Project Viewer

Project Viewer は project 一覧と project 操作を提供する。

表示項目:

- project_id
- project_name
- project_type
- updated_at
- project_root
- status

操作:

- open
- new
- import
- remove from list
- reveal in file manager

## 5. Project Workspace

Project Workspace は、選択された project を編集・検証・出力する画面である。

Project Workspace は project_type に応じた固有 UI と、全 project 共通 UI を持つ。

## 6. 共通 UI

Project Workspace の共通 UI は以下を持つ。

- Dashboard
- Assets
- Workflow Inspector
- Artifact Dependency Graph
- Policy / Restriction
- Provenance
- Export
- Settings

## 7. project_type 固有 UI

project_type に応じて固有 UI を切り替える。

例:

- image_prompt_to_sansavrm: prompt / image input / decomposition / multi-view
- sansavrm_conversion: format mapping / compatibility / loss report
- sansavrm_outfit_composition: body / clothing / fitting / policy rewrite

## 8. minimal validation UI の位置づけ

現在の minimal validation UI は、Project Workspace 内の Workflow Inspector および Artifact Dependency Graph の初期 PoC として扱う。

今後は、起動直後 UI ではなく、Project Workspace の一部として整理する。

## 9. 禁止事項

- project 未選択状態で workflow を実行してはならない。
- project_type を持たない project を新規作成してはならない。
- Project Viewer で制限付き素材の preview を無制限に表示してはならない。

## 10. 次アクション

- project_type 仕様を作成する。
- project schema に project_type を追加する。
- Project Viewer UI PoC を作成する。
- project list persistence を定義する。

---

[目次](../目次.md) > 仕様 > project viewer仕様
