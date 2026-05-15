<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260515-000036Z-SVSA
lang: ja-JP
canonical_title: governance evaluation仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > governance evaluation仕様

# governance evaluation仕様

## 1. 目的

本仕様は、SansaVRM Studio AI が SansaVRM の governance / policy / restriction 情報を解釈し、workflow、step、component 操作の可否を判定する仕組みを定義する。

## 2. 責務分離

SansaVRM Studio AI は、許諾条件そのものを決定しない。

SansaVRM 側が保持する governance / policy / restriction を authority とし、Studio AI はその条件を評価して workflow を制御する consumer として動作する。

## 3. 基本方針

- policy / restriction の定義主体は SansaVRM 側である。
- Studio AI は policy evaluation engine を持つ。
- workflow 実行前に project / asset / component の許諾条件を評価する。
- workflow step 実行前に step 単位で評価する。
- assembly / conversion / decomposition では component 単位で評価する。
- 許可されない操作は UI で非表示、無効化、または実行時エラーにする。

## 4. 評価対象 operation

初期候補:

- view
- edit
- decompose
- extract_component
- assemble
- convert
- export
- redistribute
- commercial_use
- ai_training
- ai_generation_reference
- publish

## 5. 評価対象 scope

初期候補:

- project
- asset
- component
- layer
- material
- expression
- physics
- export_target

## 6. 評価 API

Studio AI 内部では、以下のような判定関数を持つ。

```text
can_view(subject, target)
can_edit(subject, target)
can_decompose(subject, target)
can_extract_component(subject, target)
can_assemble(subject, target)
can_convert(subject, target, target_format)
can_export(subject, target, export_target)
can_redistribute(subject, target)
can_use_commercially(subject, target)
can_use_for_ai_training(subject, target)
```

## 7. 分解不可の扱い

SansaVRM governance が decomposition / component extraction を禁止している場合、Studio AI は以下を行う。

- component extraction workflow を実行しない。
- component 選択 UI に対象 component を表示しない、または disabled 表示にする。
- 分解結果を新しい asset として export しない。
- assembly source component として使用しない。

## 8. assembly 不可の扱い

assembly が禁止されている component / layer は、新しい SansaVRM の構成要素として選択できない。

## 9. conversion 制限の扱い

export target または target format が禁止されている場合、対応する conversion / export workflow を実行しない。

## 10. conflict handling

複数 source asset を assembly する場合、各 source asset / component の governance を評価し、最も制限の強い条件を優先する。

ただし、具体的な merge rule は SansaVRM 側 governance 仕様に従う。

Studio AI は独自に許諾条件を緩和してはならない。

## 11. UI 連携

UI は governance evaluation result に基づき以下を行う。

- 操作ボタンを無効化する。
- 非許可 component を選択不能にする。
- 禁止理由を表示する。
- warning / review required を表示する。
- policy conflict を表示する。

## 12. validation result

評価結果は workflow diagnostics として保持する。

候補:

```json
{
  "operation": "extract_component",
  "target": "hair_layer",
  "allowed": false,
  "reason": "decomposition_denied_by_source_policy",
  "source_policy_id": "policy-001"
}
```

## 13. 禁止事項

- Studio AI は SansaVRM governance を無視して workflow を実行してはならない。
- Studio AI は許諾条件を独自に緩和してはならない。
- 許可されていない component を assembly source として使用してはならない。
- 分解不可 asset の component を個別 export してはならない。
- conversion direction の制限を確認せず export してはならない。

## 14. 次アクション

- governance evaluation PoC を実装する。
- project_type workflow へ governance check を接続する。
- UI の operation button 制御へ接続する。
- SansaVRM 側 governance schema 確定後に評価ロジックを更新する。

---

[目次](../目次.md) > 仕様 > governance evaluation仕様
