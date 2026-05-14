<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000029Z-SVSA
lang: ja-JP
canonical_title: step handler plugin仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > step handler plugin仕様

# step handler plugin仕様

## 1. 目的

本仕様は、workflow engine における step handler plugin の責務と拡張方式を定義する。

## 2. 前提

- workflow engine は step_type ごとに handler plugin を呼び出す。
- handler plugin は input artifact を受け取り、output artifact を生成する。
- handler plugin は workflow engine 本体から分離する。
- AI 実行系は plugin 側へ隔離する。

## 3. step handler

step handler は以下を持つ。

```python
class StepHandler:
    step_type: str

    def execute(self, context):
        pass
```

## 4. handler registry

workflow engine は handler registry を持つ。

```python
{
  "decomposition": decomposition_handler,
  "copyright_risk_assessment": risk_handler
}
```

## 5. handler 責務

handler は以下を行う。

- input artifact 読み込み
- validation
- AI execution
- output artifact 生成
- provenance 生成
- diagnostics 生成

## 6. 初期 handler 候補

- copyright_risk_assessment
- decomposition
- multi_view_generation
- prompt_pack_generation
- validation
- export

## 7. 禁止事項

- workflow engine 本体へ AI provider 実装を直接埋め込んではならない。
- handler が artifact registry を直接破壊してはならない。
- handler が provenance を記録せず AI 実行してはならない。

## 8. 次アクション

- Python plugin PoC を実装する。
- handler registry を実装する。
- decomposition handler の最小 PoC を作成する。

---

[目次](../目次.md) > 仕様 > step handler plugin仕様
