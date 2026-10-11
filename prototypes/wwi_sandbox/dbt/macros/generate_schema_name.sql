-- Use the schema named in config as it is (staging, vault, marts), not prefixed with the target's schema.
{% macro generate_schema_name(custom_schema_name, node) -%}
    {{ custom_schema_name if custom_schema_name is not none else target.schema }}
{%- endmacro %}
