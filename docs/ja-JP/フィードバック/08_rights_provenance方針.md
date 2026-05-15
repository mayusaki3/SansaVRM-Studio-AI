<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260515-000035Z-SVSA
lang: ja-JP
canonical_title: rights provenance方針
canonical_document: true
document_type: note
transport: [download, ui_copy]
-->

[目次](../目次.md) > フィードバック > rights provenance方針

# rights provenance方針

## 1. 目的

本メモは、SansaVRM Studio AI で必要となった rights provenance / acquisition provenance 要件を整理し、後で SansaVRM 本体へフィードバックするための整理メモである。

## 2. 背景

SansaVRM Studio AI では以下を扱う。

- AI generated asset
- imported asset
- converted asset
- assembled asset
- derived asset
- distribution package

また、複数 SansaVRM から component を選択し、新しい SansaVRM を assembly する workflow を想定している。

そのため、単なる asset lineage ではなく、rights provenance を保持する必要がある。

## 3. 必要情報

想定項目:

- acquisition_method
- acquisition_location
- acquisition_timestamp
- rights_holder
- license_snapshot
- derivation_chain
- assembly_source
- conversion_history
- policy_change_history
- review_result
- restriction_state

## 4. acquisition_method 例

- self_created
- purchase
- download
- ai_generated
- converted
- assembled
- derived
- captured
- scanned

## 5. assembly provenance

assembly workflow では component 単位 provenance を保持する必要がある。

例:

```text
hair:
  source=SansaVRM_A

clothing:
  source=SansaVRM_B
```

## 6. 目的

rights provenance は以下の目的で使用する。

- distribution governance
- policy inheritance
- restriction merge
- review traceability
- conversion diagnostics
- AI learning restriction
- commercial usage validation
- adult content restriction
- provenance tracking

## 7. 改ざん対策

SansaVRM はファイルフォーマットであるため、完全な改ざん防止は困難。

ただし、以下は検討価値がある。

- provenance consistency validation
- provenance conflict detection
- provenance chain verification
- external provenance database
- signed provenance block
- provenance review log

## 8. SansaVRM 側フィードバック候補

将来的に、SansaVRM 本体へ以下を提案する。

- rights_provenance block
- acquisition provenance schema
- assembly provenance schema
- conversion provenance schema
- policy merge provenance
- provenance validation API
- provenance diagnostics
- provenance review state

## 9. ロードマップ位置づけ

本項目は以下フェーズで扱う。

### Phase A

Studio AI 側 provenance PoC

### Phase B

SansaVRM 側 feedback 提案

### Phase C

SansaVRM schema integration

### Phase D

cross-tool provenance validation

## 10. 次アクション

- component provenance schema を整理する。
- assembly provenance schema を整理する。
- policy merge provenance を整理する。
- SansaVRM 側申し送り資料を作成する。

---

[目次](../目次.md) > フィードバック > rights provenance方針
