<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000026Z-SVSA
lang: ja-JP
canonical_title: workflow engine仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > workflow engine仕様

# workflow engine仕様

## 1. 目的

本仕様は、SansaVRM Studio AI における workflow engine の責務、実行単位、依存関係、再実行、再開の方式を定義する。

## 2. 前提

- workflow は project workspace 内でのみ実行する。
- workflow は workflow run と workflow step により構成する。
- step 間のデータ連携は artifact_id を介して行う。
- workflow engine は、artifact dependency graph を更新する。
- 初期 PoC では同期実行を対象とする。

## 3. workflow engine の責務

workflow engine は以下を行う。

- workflow run の作成
- workflow step の実行
- input_artifacts の存在確認
- output_artifacts の登録
- artifact dependency graph の更新
- step status の更新
- workflow run status の更新
- step 単位の再実行
- failed step 以降の再開

## 4. step execution

step は以下の順序で実行する。

1. input_artifacts を検証する。
2. step status を running にする。
3. step handler を実行する。
4. output_artifacts を artifact registry へ登録する。
5. artifact dependency graph を更新する。
6. step status を completed にする。

失敗時は step status を failed にする。

## 5. artifact dependency graph

artifact dependency graph は artifact 間の生成関係を保持する。

```json
{
  "artifact_id": "artifact-decomposition-001",
  "created_by_step": "step-decomposition-001",
  "depends_on": [
    "artifact-source-image-001"
  ]
}
```

## 6. rerun

step を再実行する場合、既存 output artifact は上書きせず、新しい artifact_id を発行する。

理由:

- 過去の run を再現可能にするため。
- 差分比較を可能にするため。
- provenance を保持するため。

## 7. resume

workflow resume は failed step または user_review step から再開できる。

resume 時は、既存 artifact を再利用し、必要な step のみ再実行する。

## 8. 禁止事項

- workflow engine は project workspace なしで実行してはならない。
- input_artifacts が存在しない step を completed にしてはならない。
- rerun 時に既存 artifact を破壊してはならない。
- failed step を成功扱いしてはならない。

## 9. 次アクション

- Python PoC を実装する。
- artifact dependency graph を実装する。
- rerun / resume の最小テストを作成する。

---

[目次](../目次.md) > 仕様 > workflow engine仕様
