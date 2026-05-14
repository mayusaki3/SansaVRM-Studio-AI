# SansaVRM Studio AI

SansaVRM Studio AI は、SansaVRM を中心にした構造化 3D アセット制作・変換・検証・AI 前処理支援環境です。

本プロジェクトは、VRM 専用ツールではなく、以下のような幅広いアセットを対象にします。

- humanoid character
- non-humanoid character
- animal
- creature
- robot
- mech
- furniture
- building
- prop
- environment asset

また、本プロジェクトは「画像 → 直接3D生成」に限定せず、以下のような構造化前処理を重視します。

- decomposition
- multi-view generation
- layered asset generation
- provenance generation
- policy / restriction generation
- downstream media generation

## 主な目的

- SansaVRM を内部正規形式として扱う。
- AI なしでも利用可能な Viewer / Validator / Converter を提供する。
- ローカル AI を利用した前処理・分解・多視点生成を提供する。
- 制作状態と流通状態を分離する。
- policy / restriction / provenance を扱う。
- 3D だけでなく image / video generation に接続可能な中間成果物を扱う。

## 現在の状態

現在は architecture stabilization / PoC implementation 段階。

実装済み:

- project workspace
- artifact registry
- workflow engine
- dependency graph
- local server
- minimal validation UI
- copyright risk assessment PoC
- decomposition schema PoC

詳細は以下を参照。

- docs/ja-JP/フィードバック
- docs/ja-JP/仕様
- docs/ja-JP/テスト

## 方針

### AI 必須にしない

SansaVRM Studio AI は、AI 環境がなくても利用可能な構成を目指す。

- Viewer
- Validator
- Converter
- Report Viewer

などは AI なしでも動作可能とする。

### ローカル AI 優先

裸体素体、内部構造、未公開素材、制限付き中間素材を扱う可能性があるため、AI 前処理はローカル AI を原則とする。

### 制作自由 + 流通制御

制作段階では生成物自体を一律禁止しない。

代わりに:

- policy
- restriction
- provenance
- distribution state

を保持し、流通・公開・配布段階で制御する。

## 想定構成

```text
SansaVRM Studio AI
├ Core
│ ├ Viewer
│ ├ Validator
│ ├ Converter
│ └ Report Viewer
│
├ AI Preprocess
│ ├ decomposition
│ ├ multi-view generation
│ ├ prompt generation
│ └ downstream generation support
│
├ Workflow System
│ ├ project workspace
│ ├ artifact registry
│ ├ workflow engine
│ ├ dependency graph
│ └ provenance
│
├ Adapter
│ ├ VRM
│ ├ glTF
│ ├ MuJoCo
│ └ AI providers
│
└ Export
  ├ authoring state
  ├ distribution state
  └ platform export
```

## ローカルサーバー

### 推奨 Python

```text
Python 3.11+
```

### 必要ライブラリ

```bash
pip install fastapi uvicorn
```

### 起動

```bash
uvicorn src.python.local_server:app --reload
```

### ブラウザアクセス

```text
http://127.0.0.1:8000
```

## API

- GET /api/health
- GET /api/project
- GET /api/artifacts
- GET /api/workflow-runs
- GET /api/workflow-graph

## 現在の UI

現在の UI は production UI ではない。

architecture validation を目的とした minimal validation UI である。

確認対象:

- project workspace
- workflow structure
- artifact registry
- dependency graph

## 将来予定

- ComfyUI integration
- Qwen2.5-VL integration
- SAM2 integration
- Zero123++ integration
- distributed execution
- GPU orchestration
- provenance graph
- export pipeline

## ライセンス

MIT License
