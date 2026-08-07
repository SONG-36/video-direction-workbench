# Scrape Creators Result Recording Contract

- Version: V0.1
- Status: Draft
- Authority: Evidence Recording Contract
- Scope: Evidence record format, artifact path convention, redaction rules, field observation rules, and capability verdict rules for later Scrape Creators reconnaissance tests.
- Depends On: [04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md](04_SCRAPE_CREATORS_RECONNAISSANCE_PLAN.md), [05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md](05_SCRAPE_CREATORS_ENDPOINT_TEST_MATRIX.md)
- Supersedes: None
- Last Updated: 2026-08-07
- Approved By: Pending Andy Review

## 1. Campaign Identity

Candidate object: `ReconnaissanceCampaign`.

Minimum fields:

- campaign_id
- provider
- campaign_scope
- endpoint_matrix_version
- started_at
- completed_at
- campaign_status
- operator
- environment
- account_plan_boundary
- evidence_root_path
- notes

The campaign covers all 29 currently observed endpoints. It is not complete while any endpoint remains `Not Run` without explanation.

## 2. Endpoint Test Run Identity

Candidate object: `EndpointTestRun`.

Every actual endpoint call records:

- campaign_id
- endpoint_test_run_id
- provider
- api_family
- endpoint_name
- executed_at
- environment
- request_purpose
- request_parameters_redacted
- authentication_type_redacted
- http_status_or_tool_status
- elapsed_time_ms
- response_size_bytes if observable
- canonical_redacted_request_artifact_path
- canonical_request_fingerprint
- raw_response_artifact_path
- response_hash
- record_count
- pagination_state
- error_code
- error_message_redacted
- plan_or_quota_observation
- human_notes

`endpoint_test_run_id` links request, response, redacted copy, field observations, endpoint result, and final report references.

## 3. Request Evidence

Candidate object: `RequestRecord`.

Request evidence must record:

- endpoint_test_run_id
- endpoint_id
- endpoint_name
- request_purpose
- request_method_or_tool_action if observable
- request_parameters_redacted
- authentication_type_redacted
- environment
- executed_at
- operator
- canonical_redacted_request_artifact_path
- canonical_request_fingerprint
- redaction_notes

Never persist the true raw HTTP request. Request evidence must be a canonical redacted request record only.

Forbidden in request evidence:

- API key plaintext
- Authorization header value
- Cookie value
- signature secret
- raw authentication payload
- Secret
- Session token
- account-control material

If a secret appears in query string, headers, body, or tool arguments, it must be redacted before any request evidence is persisted.

## 3A. Canonical Redacted Request

Candidate object: `CanonicalRedactedRequest`.

Canonical redacted request evidence should preserve the business-reviewable request conditions without storing secrets or account-control material.

Minimum fields:

- endpoint_test_run_id
- endpoint_id
- endpoint_name
- request_method_or_tool_action if observable
- canonical_url_or_action_redacted
- request_parameters_redacted
- header_names_present_redacted
- authentication_type_redacted
- body_shape_redacted if applicable
- environment
- executed_at
- operator
- redaction_notes
- canonical_request_fingerprint

`canonical_request_fingerprint` identifies whether two tests used equivalent redacted request conditions. It is based only on canonical redacted request evidence; it must not be based on secret-bearing raw request content. It is not authentication information and must not be usable to recover an API key or other secret.

## 4. Response Evidence

Candidate object: `ResponseRecord`.

Response evidence must record:

- endpoint_test_run_id
- http_status_or_tool_status
- elapsed_time_ms
- response_size_bytes if observable
- raw_response_artifact_path
- redacted_response_artifact_path
- response_hash
- response_hash_algorithm
- redacted_response_hash if needed for long-term review
- redacted_response_hash_algorithm if needed for long-term review
- record_count
- pagination_state
- observed_top_level_shape
- redaction_status
- notes

Raw response files are immutable and must not be edited. Review uses redacted copies. After saving a raw response and before any Git operation, operators must perform secret scan and sensitive-field review.

If a raw response contains credential, session token, private account data, or other sensitive material, it must be isolated and must not be committed. `response_hash` is calculated against the original saved raw response content. Redacted response evidence may have a separate hash when needed for long-term review. Raw and redacted response hashes must not be mixed.

## 5. Field Observation

Candidate object: `FieldObservation`.

Field observation table:

| field | meaning |
|---|---|
| field_path | Path in observed response. |
| observed_type | Observed JSON or CSV type. |
| observed_presence | Always, sometimes, absent, or unknown from tested cases. |
| nullable | Whether null was observed. |
| zero_observed | Whether numeric zero was observed. |
| empty_string_observed | Whether empty string was observed. |
| example_value_redacted | Safe redacted example. |
| semantic_hypothesis | Human-readable hypothesis, not a fact unless verified. |
| verification_status | Observed, Inferred, Documented, Conflicting, or Unknown. |
| source_endpoint | Endpoint where field was observed. |
| cross_endpoint_equivalent | Candidate equivalent field in another endpoint. |
| interpretation_risk | Business risk if misread. |
| notes | Review notes. |

Only `Observed` or sourced `Documented` fields can enter a formal field contract candidate. `Inferred` must never be presented as verified fact.

## 6. Pagination Observation

Candidate object: `PaginationObservation`.

Record:

- endpoint_test_run_id
- pagination_supported
- first_page_artifact
- next_page_artifact
- cursor_or_token_field
- end_page_behavior
- repeated_page_behavior
- expired_cursor_behavior
- maximum_observed_count
- hard_limit_observed
- unknowns

Pagination conclusion must distinguish "no pagination observed" from "pagination not tested".

## 7. Error Observation

Candidate object: `ErrorObservation`.

Record:

- endpoint_test_run_id
- tested_error_case
- safe_negative_case
- http_status_or_tool_status
- error_code
- error_message_redacted
- retryable
- account_risk
- interpretation
- evidence_path

Negative cases must stay low risk. Do not run destructive, abusive, or account-risk tests.

## 8. Cost / Quota Observation

Candidate object: `CostQuotaObservation`.

Record:

- endpoint_test_run_id
- billable_observed
- billing_unit_if_visible
- quota_header_or_ui_signal
- remaining_quota_if_visible
- rate_limit_signal
- retry_after_signal
- plan_gate_signal
- unknowns
- evidence_path

Do not intentionally flood endpoints or attempt to trigger account blocks.

## 9. Business Interpretation Observation

Record:

- endpoint_id
- supported_business_questions
- candidate_signal_layer
- cannot_prove
- P0_suitability
- future_stage_suitability
- exclusion_reason_if_any
- interpretation_boundary
- human_notes

Public content, shop visibility, and ad visibility must not be converted into real buying audience, real conversion rate, true GMV attribution, or guaranteed creative success.

## 10. Capability Verdict

Candidate object: `CapabilityVerdict`.

Allowed final capability verdicts:

- Adopt For P0
- Adopt For Future Stage
- Research Only
- Reject
- Blocked Pending Access

Verdict fields:

- endpoint_id
- final_capability_verdict
- verdict_reason
- evidence_refs
- remaining_unknowns
- contract_impact
- approved_by
- decision_date

Verdict is not the same as test status. A passed endpoint can still be Research Only or Reject for business reasons.

## 10A. Test Status To Capability Verdict Mapping

Test Status and Capability Verdict are separate. Endpoint Test Status describes the observed execution result or governance state. Capability Verdict describes the business capability decision. Final Capability Verdict values remain limited to:

- Adopt For P0
- Adopt For Future Stage
- Research Only
- Reject
- Blocked Pending Access

The following mapping is required before the campaign can be marked complete:

| Test Status | Allowed Final Verdicts | Required Notes / Evidence |
|---|---|---|
| Passed | Adopt For P0; Adopt For Future Stage; Research Only; Reject | Real call evidence, field observations, interpretation boundary, and business reason. `Pending Test` is forbidden when Campaign Complete. |
| Partially Passed | Adopt For P0; Adopt For Future Stage; Research Only; Reject; Blocked Pending Access | Real call evidence plus clear `remaining_unknowns`; explain why partial evidence is or is not enough. |
| Failed | Reject; Research Only; Blocked Pending Access | Failure evidence and reason. Failure can come from unknown parameters, temporary endpoint issues, or plan limits; it must not automatically become Reject. |
| Blocked By Prerequisite | Blocked Pending Access; Research Only | Evidence of missing prerequisite. Use Research Only only when documentation or other endpoints provide enough limited conclusion. |
| Blocked By Authorization | Blocked Pending Access | Authorization boundary evidence and remaining access decision. |
| Blocked By Plan Or Quota | Blocked Pending Access | Plan, quota, budget, or rate-limit evidence. |
| Endpoint Unavailable | Reject; Blocked Pending Access | Evidence and recovery judgment; decide whether unavailable appears permanent or potentially recoverable. |
| Not Applicable | Reject; Research Only | Business reason explaining why the endpoint is outside the campaign's useful scope. |
| Deferred By Human Decision | Research Only; Blocked Pending Access | Record `human_decision_status: Deferred`. Use Research Only when deliberately not testing but preserving future research; use Blocked Pending Access when waiting for permission, budget, or access. |
| Not Run | Not allowed when Campaign Complete | Only allowed while campaign is in progress; no endpoint may remain Not Run at campaign completion. |

`Pending Test` is allowed only during an in-progress campaign. It is not a final Capability Verdict.

## 11. Artifact Paths

Later actual tests should use:

```text
research/
└── scrape_creators/
    └── campaigns/
        └── <campaign_id>/
            ├── CAMPAIGN_MANIFEST.md
            ├── requests_canonical_redacted/
            │   └── <endpoint_id>/
            ├── responses_raw/
            │   └── <endpoint_id>/
            ├── responses_redacted/
            │   └── <endpoint_id>/
            ├── field_observations/
            │   └── <endpoint_id>/
            ├── endpoint_results/
            │   └── <endpoint_id>/
            └── FINAL_RECONNAISSANCE_REPORT.md
```

This round does not create a real campaign directory.

Artifact rules:

- Raw HTTP requests are not persisted.
- Canonical redacted request evidence is saved separately from responses.
- Raw response is not modified.
- Redacted copy is used for review.
- Raw and redacted files are stored separately.
- Secrets must not enter Git.
- `responses_raw` does not enter Git by default.
- Whether raw response files enter Git requires separate human approval after secret scan and sensitive-field review.
- Large and sensitive files are not committed by default.
- SHA256 must be recorded for raw response evidence when possible.
- Redacted response hash must be separate from raw response hash if retained.
- Canonical redacted request and response artifacts link through `endpoint_test_run_id`.

## 12. Redaction And Secret Handling

Forbidden in records and review files:

- API key plaintext
- Authorization header
- Cookie
- Secret
- Session token
- Account takeover material
- Private account data outside the test scope

Redaction must preserve business review value while removing secrets. Redacted values should indicate type, such as `<redacted_api_key>` or `<redacted_cookie>`.

Raw response and redacted response artifacts remain separate. Raw response Git inclusion is blocked by default until a separate human decision approves the exact protected artifact set after sensitive-data review.

## 13. Change Discipline

- This is a test recording contract, not implementation code.
- No Python class, Pydantic Schema, JSON Schema, database table, UI, or CLI is created by this document.
- Field observations from one endpoint must not silently become global field contracts.
- Any formal SIG-P0 field contract change requires later review.
- Raw evidence, redacted evidence, field observations, and verdicts must stay traceable.
