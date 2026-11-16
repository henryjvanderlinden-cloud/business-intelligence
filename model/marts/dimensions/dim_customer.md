---
id: nsdn:mart:dim:customer
kind: dimension
name: dim_customer
status: accepted
ruled_in: ADR-0039, ADR-0040
defined_in: docs/10_architecture/141_the-first-slice-business-vault-and-mart.md
written_by: claude-fable-5-2
written_at: 2026-11-15T21:30:00Z
step: S13-016
method: written by hand from note 141 as ruled
hub: hub_customer
pit: pit_customer
bridge: brg_customer__segment
subject_area: parties
---

## Attributes

- customer_id | from=key.CustomerID
- customer_name | from=sat_customer__wwi.CustomerName | unknown=Unknown
- customer_category_id | via=customer_category | pit=pit_customer_category | from=key.CustomerCategoryID
- customer_category | via=customer_category | pit=pit_customer_category | from=sat_customer_category__wwi.CustomerCategoryName | unknown=Unknown
- buying_group_id | via=buying_group | pit=pit_buying_group | from=key.BuyingGroupID
- buying_group | via=buying_group | pit=pit_buying_group | from=sat_buying_group__wwi.BuyingGroupName | when_none=No buying group | unknown=Unknown

## Notes

Conformed (ADR-0026). A customer without a buying group is an independent customer, a state and not a gap, hence the label. The bill-to customer is a second role of this dimension. Category and buying group are shown as currently known (ADR-0039 decision 4).
