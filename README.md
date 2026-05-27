# test-observability-rca-sample-pytest

Pytest counterpart of [`test-observability-rca-sample`](https://github.com/Sanskar-002/test-observability-rca-sample).

Provides a minimal app + selenium/pytest spec that intentionally produces
distinct test failure shapes per branch, so BrowserStack Test
Observability's AI RCA + Bad PR Causation can be trained / verified.

This repo specifically exercises **preprod / regression** envs where
the local browserstack-sdk wrapper is supported, and wires
**Smart Test Selection** so `rcaData.related_prs` is populated.

## Branches

| Branch | Spec | App URL the spec hits | Expected RCA verdict |
|---|---|---|---|
| `main` | clean | clean (`celadon-duckanoo`) | 6/6 pass |
| `bad-dev-pr` | clean | **broken** (`tranquil-custard`) | 6/6 fail with app-side fault shapes → Bad Dev PR |
| `bad-automation-pr` | **broken selectors / expected text** | clean (`celadon-duckanoo`) | 6/6 fail with spec-side fault shapes → Bad Automation PR |

## Running locally

```bash
pip install -r requirements.txt
export BROWSERSTACK_USERNAME=...
export BROWSERSTACK_ACCESS_KEY=...
# Tells Smart Test Selection which feature branch this run represents
export BROWSERSTACK_ORCHESTRATION_SMART_SELECTION_FEATURE_BRANCHES='{"RCA_SAMPLE_PYTEST":"bad-dev-pr"}'

browserstack-sdk pytest tests/
```

## Smart Test Selection config

- `selection_config.json` declares this repo as `RCA_SAMPLE_PYTEST`.
- `browserstack.yml` enables `runSmartSelection` and points at the JSON.
- The `BROWSERSTACK_ORCHESTRATION_SMART_SELECTION_FEATURE_BRANCHES` env
  var must be set per run to indicate which feature branch is under test.

## Notes

- Builds appear under the `bad-pr-causation-samples` project on Test
  Observability; each run registers a build and streams per-test events.
